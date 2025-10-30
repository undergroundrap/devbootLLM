import fs from 'fs';
import path from 'path';

const PUBLIC_DIR = path.join(process.cwd(), 'public');
const REQUIRED_FIELDS = ['id', 'title', 'language', 'description', 'initialCode', 'fullSolution', 'expectedOutput', 'tutorial', 'tags'];
const DIFFICULTY_TAGS = ['Beginner', 'Intermediate', 'Advanced', 'Expert'];

function deepValidateLesson(lesson, language) {
  const issues = [];
  const warnings = [];
  const info = [];

  // 1. Required fields
  REQUIRED_FIELDS.forEach(field => {
    if (!lesson[field]) {
      issues.push(`Missing required field: ${field}`);
    } else if (typeof lesson[field] === 'string' && lesson[field].trim().length === 0) {
      issues.push(`Empty field: ${field}`);
    }
  });

  // 2. ID validation
  if (lesson.id && !Number.isInteger(lesson.id)) {
    issues.push('ID must be an integer');
  }

  // 3. Language validation
  if (lesson.language && lesson.language !== language) {
    issues.push(`Language mismatch: expected ${language}, got ${lesson.language}`);
  }

  // 4. Code validation
  if (lesson.initialCode && lesson.fullSolution) {
    if (lesson.initialCode.trim() === lesson.fullSolution.trim()) {
      issues.push('initialCode is identical to fullSolution (no learning exercise)');
    }

    // Check for syntax patterns (basic)
    if (language === 'python') {
      // Check for Python syntax
      if (lesson.fullSolution.includes('public class')) {
        warnings.push('Full solution appears to contain Java code');
      }
    } else if (language === 'java') {
      // Check for Java syntax
      if (!lesson.fullSolution.includes('class ') && lesson.fullSolution.length > 100) {
        warnings.push('Full solution may be missing class definition');
      }
    }

    // Check code length
    if (lesson.fullSolution.length < 30) {
      warnings.push(`Very short solution (${lesson.fullSolution.length} chars)`);
    }
  }

  // 5. Difficulty tag validation
  const hasDifficultyTag = lesson.tags && lesson.tags.some(tag =>
    DIFFICULTY_TAGS.some(diff => tag.toLowerCase() === diff.toLowerCase())
  );
  if (!hasDifficultyTag) {
    issues.push('Missing difficulty tag (Beginner/Intermediate/Advanced/Expert)');
  }

  // 6. Tag validation
  if (lesson.tags) {
    if (lesson.tags.length < 2) {
      warnings.push(`Only ${lesson.tags.length} tag(s) - consider adding more for discoverability`);
    }
    if (lesson.tags.length > 10) {
      warnings.push(`Many tags (${lesson.tags.length}) - ensure all are relevant`);
    }
  }

  // 7. Tutorial validation
  if (lesson.tutorial) {
    const tutorialLength = lesson.tutorial.replace(/<[^>]+>/g, '').trim().length;

    if (tutorialLength < 300) {
      warnings.push(`Very short tutorial (${tutorialLength} chars)`);
    }

    // Check for generic content
    if (/demonstrated through practical examples/i.test(lesson.tutorial)) {
      warnings.push('Contains generic phrase: "demonstrated through practical examples"');
    }

    // Check for essential sections
    const hasPitfalls = /<h4[^>]*>.*?Common Pitfalls.*?<\/h4>/i.test(lesson.tutorial);
    const hasBestPractices = /<h4[^>]*>.*?Best Practices.*?<\/h4>/i.test(lesson.tutorial);
    const hasExamples = /<h4[^>]*>.*?Examples?.*?<\/h4>/i.test(lesson.tutorial);

    if (!hasExamples) {
      info.push('No Examples section found');
    }
    if (!hasPitfalls && !lesson.tags?.includes('Beginner')) {
      info.push('No Common Pitfalls section');
    }

    // Check for code blocks in tutorial
    const codeBlocks = (lesson.tutorial.match(/<pre/g) || []).length;
    if (codeBlocks === 0) {
      warnings.push('Tutorial has no code examples');
    }
  }

  // 8. Expected output validation
  if (lesson.expectedOutput && lesson.expectedOutput.trim().length === 0) {
    warnings.push('Expected output is empty');
  }

  // 9. Description validation
  if (lesson.description) {
    if (lesson.description.length < 20) {
      warnings.push('Very short description');
    }
    if (lesson.description.length > 300) {
      warnings.push('Very long description - consider being more concise');
    }
  }

  return { issues, warnings, info };
}

function displayValidation(lesson, validation) {
  console.log('='.repeat(80));
  console.log(`LESSON ${lesson.id}: ${lesson.title}`);
  console.log('='.repeat(80));
  console.log();

  console.log('BASIC INFO:');
  console.log(`  Language: ${lesson.language}`);
  console.log(`  Tags: ${(lesson.tags || []).join(', ')}`);
  console.log(`  Description: ${(lesson.description || '').substring(0, 80)}...`);
  console.log();

  console.log('CODE METRICS:');
  console.log(`  Initial code length: ${(lesson.initialCode || '').length} chars`);
  console.log(`  Full solution length: ${(lesson.fullSolution || '').length} chars`);
  console.log(`  Tutorial length: ${(lesson.tutorial || '').replace(/<[^>]+>/g, '').trim().length} chars`);
  console.log(`  Expected output length: ${(lesson.expectedOutput || '').length} chars`);
  console.log();

  // Issues
  if (validation.issues.length > 0) {
    console.log('🔴 CRITICAL ISSUES:');
    validation.issues.forEach(issue => {
      console.log(`  ❌ ${issue}`);
    });
    console.log();
  }

  // Warnings
  if (validation.warnings.length > 0) {
    console.log('🟡 WARNINGS:');
    validation.warnings.forEach(warning => {
      console.log(`  ⚠️  ${warning}`);
    });
    console.log();
  }

  // Info
  if (validation.info.length > 0) {
    console.log('ℹ️  INFORMATION:');
    validation.info.forEach(info => {
      console.log(`  ℹ️  ${info}`);
    });
    console.log();
  }

  // Overall
  console.log('='.repeat(80));
  if (validation.issues.length === 0) {
    if (validation.warnings.length === 0) {
      console.log('✅ EXCELLENT - No issues or warnings');
    } else {
      console.log('✅ GOOD - No critical issues (but has warnings to review)');
    }
  } else {
    console.log('❌ NEEDS FIXING - Critical issues found');
  }
  console.log('='.repeat(80));
}

async function main() {
  try {
    const args = process.argv.slice(2);
    let lessonId = null;
    let language = null;

    // Parse arguments
    for (let i = 0; i < args.length; i++) {
      if (args[i] === '--id' && args[i + 1]) {
        lessonId = parseInt(args[i + 1]);
        i++;
      }
      if (args[i] === '--language' && args[i + 1]) {
        language = args[i + 1].toLowerCase();
        i++;
      }
    }

    if (!lessonId) {
      console.error('Usage: node test-single-lesson.mjs --id <lesson-id> [--language python|java]');
      console.error('');
      console.error('Examples:');
      console.error('  node test-single-lesson.mjs --id 100');
      console.error('  node test-single-lesson.mjs --id 250 --language python');
      process.exit(1);
    }

    console.log('='.repeat(80));
    console.log('SINGLE LESSON DEEP VALIDATION');
    console.log('='.repeat(80));
    console.log();

    // Determine which file(s) to check
    const filesToCheck = [];
    if (!language || language === 'python') {
      filesToCheck.push({ file: 'lessons-python.json', language: 'python' });
    }
    if (!language || language === 'java') {
      filesToCheck.push({ file: 'lessons-java.json', language: 'java' });
    }

    let foundLesson = false;

    for (const { file, language: lang } of filesToCheck) {
      const lessons = JSON.parse(
        fs.readFileSync(path.join(PUBLIC_DIR, file), 'utf-8')
      );

      const lesson = lessons.find(l => l.id === lessonId);

      if (lesson) {
        foundLesson = true;
        console.log(`Found in: ${file}`);
        console.log();

        const validation = deepValidateLesson(lesson, lang);
        displayValidation(lesson, validation);

        // Exit code based on issues
        if (validation.issues.length > 0) {
          process.exit(1);
        }
      }
    }

    if (!foundLesson) {
      console.error(`❌ Lesson ${lessonId} not found`);
      process.exit(1);
    }

    process.exit(0);

  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
}

main();
