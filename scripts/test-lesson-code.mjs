import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const PUBLIC_DIR = path.join(__dirname, '..', 'public');
const TEMP_DIR = path.join(__dirname, '..', 'temp');

// Create temp directory if it doesn't exist
if (!fs.existsSync(TEMP_DIR)) {
  fs.mkdirSync(TEMP_DIR);
}

function testPythonCode(lesson) {
  const tempFile = path.join(TEMP_DIR, `test_${lesson.id}.py`);

  try {
    // Write the full solution to a file
    fs.writeFileSync(tempFile, lesson.fullSolution);

    // Try to run it
    const rawOutput = execSync(`python "${tempFile}"`, {
      encoding: 'utf-8',
      timeout: 5000
    });

    // Normalize output: convert CRLF to LF, trim trailing newline
    const output = rawOutput.replace(/\r\n/g, '\n').replace(/\n$/, '');
    const expectedOutput = (lesson.expectedOutput || '').replace(/\r\n/g, '\n').replace(/\n$/, '');
    const match = output === expectedOutput;

    // Clean up
    fs.unlinkSync(tempFile);

    return {
      success: true,
      compiled: true,
      output,
      expectedOutput,
      match,
      error: null
    };
  } catch (error) {
    // Clean up on error
    if (fs.existsSync(tempFile)) {
      fs.unlinkSync(tempFile);
    }

    return {
      success: false,
      compiled: false,
      output: null,
      expectedOutput: lesson.expectedOutput,
      match: false,
      error: error.message
    };
  }
}

function testJavaCode(lesson) {
  const tempFile = path.join(TEMP_DIR, 'Main.java');
  const tempClass = path.join(TEMP_DIR, 'Main.class');

  try {
    // Write the full solution to a file
    fs.writeFileSync(tempFile, lesson.fullSolution);

    // Try to compile
    execSync(`javac "${tempFile}"`, {
      encoding: 'utf-8',
      timeout: 10000,
      cwd: TEMP_DIR
    });

    // Try to run
    const rawOutput = execSync(`java -cp "${TEMP_DIR}" Main`, {
      encoding: 'utf-8',
      timeout: 5000
    });

    // Normalize output: convert CRLF to LF, trim trailing newline
    const output = rawOutput.replace(/\r\n/g, '\n').replace(/\n$/, '');
    const expectedOutput = (lesson.expectedOutput || '').replace(/\r\n/g, '\n').replace(/\n$/, '');
    const match = output === expectedOutput;

    // Clean up
    fs.unlinkSync(tempFile);
    if (fs.existsSync(tempClass)) {
      fs.unlinkSync(tempClass);
    }

    return {
      success: true,
      compiled: true,
      output,
      expectedOutput,
      match,
      error: null
    };
  } catch (error) {
    // Clean up on error
    if (fs.existsSync(tempFile)) {
      fs.unlinkSync(tempFile);
    }
    if (fs.existsSync(tempClass)) {
      fs.unlinkSync(tempClass);
    }

    return {
      success: false,
      compiled: error.message.includes('javac') ? false : true,
      output: null,
      expectedOutput: lesson.expectedOutput,
      match: false,
      error: error.message
    };
  }
}

async function main() {
  const args = process.argv.slice(2);

  if (args.length < 1 || !args[0].match(/^\d+$/)) {
    console.log('Usage: node test-lesson-code.mjs <lesson-id> [language]');
    console.log('');
    console.log('Examples:');
    console.log('  node test-lesson-code.mjs 1');
    console.log('  node test-lesson-code.mjs 100 python');
    console.log('  node test-lesson-code.mjs 50 java');
    process.exit(1);
  }

  const lessonId = parseInt(args[0]);
  const language = args[1] ? args[1].toLowerCase() : null;

  console.log('='.repeat(80));
  console.log(`TESTING LESSON ${lessonId} CODE`);
  console.log('='.repeat(80));
  console.log();

  const filesToCheck = [];
  if (!language || language === 'python') {
    filesToCheck.push({ file: 'lessons-python.json', language: 'python' });
  }
  if (!language || language === 'java') {
    filesToCheck.push({ file: 'lessons-java.json', language: 'java' });
  }

  for (const { file, language: lang } of filesToCheck) {
    const lessons = JSON.parse(
      fs.readFileSync(path.join(PUBLIC_DIR, file), 'utf-8')
    );

    const lesson = lessons.find(l => l.id === lessonId);

    if (lesson) {
      console.log(`Testing ${lang.toUpperCase()} - Lesson ${lessonId}: ${lesson.title}`);
      console.log('-'.repeat(80));

      const result = lang === 'python' ? testPythonCode(lesson) : testJavaCode(lesson);

      if (result.compiled) {
        console.log('✅ Code compiles successfully');
      } else {
        console.log('❌ Code failed to compile');
        console.log('Error:', result.error);
      }

      if (result.success && result.output !== null) {
        console.log();
        console.log('Output:');
        console.log(result.output);
        console.log();
        console.log('Expected:');
        console.log(result.expectedOutput);
        console.log();

        if (result.match) {
          console.log('✅ Output matches expected output');
        } else {
          console.log('⚠️  Output does NOT match expected output');
        }
      }

      console.log();
    }
  }

  // Cleanup temp directory
  if (fs.existsSync(TEMP_DIR)) {
    const files = fs.readdirSync(TEMP_DIR);
    files.forEach(file => {
      fs.unlinkSync(path.join(TEMP_DIR, file));
    });
  }
}

main().catch(console.error);
