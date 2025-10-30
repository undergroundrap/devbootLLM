import fs from 'fs';
import path from 'path';

const PUBLIC_DIR = path.join(process.cwd(), 'public');
const DIFFICULTY_TAGS = ['Beginner', 'Intermediate', 'Advanced', 'Expert'];
const REQUIRED_FIELDS = ['id', 'title', 'language', 'description', 'initialCode', 'fullSolution', 'expectedOutput', 'tutorial', 'tags'];

function validateLesson(lesson, language) {
  const issues = [];
  const warnings = [];

  // Check required fields
  REQUIRED_FIELDS.forEach(field => {
    if (!lesson[field]) {
      issues.push(`Missing required field: ${field}`);
    }
  });

  // Check for identical code
  if (lesson.initialCode && lesson.fullSolution) {
    if (lesson.initialCode.trim() === lesson.fullSolution.trim()) {
      issues.push('initialCode identical to fullSolution');
    }
  }

  // Check for difficulty tag
  const hasDifficultyTag = lesson.tags && lesson.tags.some(tag =>
    DIFFICULTY_TAGS.some(diff => tag.toLowerCase() === diff.toLowerCase())
  );
  if (!hasDifficultyTag) {
    issues.push('Missing difficulty tag');
  }

  // Check for very short code (likely placeholder)
  if (lesson.fullSolution && lesson.fullSolution.length < 50) {
    warnings.push('Very short solution (possible placeholder)');
  }

  // Check for empty expected output
  if (!lesson.expectedOutput || lesson.expectedOutput.trim().length === 0) {
    warnings.push('Empty expectedOutput');
  }

  // Check tutorial length
  if (lesson.tutorial && lesson.tutorial.length < 500) {
    warnings.push('Very short tutorial');
  }

  // Check for generic phrases (sampling)
  if (lesson.tutorial) {
    if (/demonstrated through practical examples/i.test(lesson.tutorial)) {
      warnings.push('Contains generic phrase');
    }
  }

  return { issues, warnings };
}

function generateStatistics(lessons, language) {
  const stats = {
    total: lessons.length,
    withIssues: 0,
    withWarnings: 0,
    byDifficulty: { Beginner: 0, Intermediate: 0, Advanced: 0, Expert: 0, None: 0 },
    avgCodeLength: 0,
    avgTutorialLength: 0,
    avgTagCount: 0
  };

  let totalCodeLength = 0;
  let totalTutorialLength = 0;
  let totalTagCount = 0;

  lessons.forEach(lesson => {
    const validation = validateLesson(lesson, language);

    if (validation.issues.length > 0) stats.withIssues++;
    if (validation.warnings.length > 0) stats.withWarnings++;

    // Difficulty distribution
    const difficulty = lesson.tags?.find(tag =>
      DIFFICULTY_TAGS.some(diff => tag.toLowerCase() === diff.toLowerCase())
    );
    if (difficulty) {
      const normalizedDiff = DIFFICULTY_TAGS.find(d => d.toLowerCase() === difficulty.toLowerCase());
      stats.byDifficulty[normalizedDiff]++;
    } else {
      stats.byDifficulty.None++;
    }

    // Averages
    if (lesson.fullSolution) totalCodeLength += lesson.fullSolution.length;
    if (lesson.tutorial) totalTutorialLength += lesson.tutorial.length;
    if (lesson.tags) totalTagCount += lesson.tags.length;
  });

  stats.avgCodeLength = Math.round(totalCodeLength / lessons.length);
  stats.avgTutorialLength = Math.round(totalTutorialLength / lessons.length);
  stats.avgTagCount = (totalTagCount / lessons.length).toFixed(1);

  return stats;
}

async function main() {
  try {
    console.log('='.repeat(80));
    console.log('COMPREHENSIVE LESSON QUALITY VALIDATION');
    console.log('='.repeat(80));
    console.log();

    const pythonLessons = JSON.parse(
      fs.readFileSync(path.join(PUBLIC_DIR, 'lessons-python.json'), 'utf-8')
    );
    const javaLessons = JSON.parse(
      fs.readFileSync(path.join(PUBLIC_DIR, 'lessons-java.json'), 'utf-8')
    );

    // Validate all lessons
    console.log('Validating Python lessons...');
    const pythonResults = pythonLessons.map(lesson => ({
      lesson,
      validation: validateLesson(lesson, 'python')
    }));

    console.log('Validating Java lessons...');
    const javaResults = javaLessons.map(lesson => ({
      lesson,
      validation: validateLesson(lesson, 'java')
    }));

    // Generate statistics
    const pythonStats = generateStatistics(pythonLessons, 'python');
    const javaStats = generateStatistics(javaLessons, 'java');

    console.log();
    console.log('='.repeat(80));
    console.log('VALIDATION SUMMARY');
    console.log('='.repeat(80));
    console.log();

    console.log('PYTHON LESSONS:');
    console.log(`  Total lessons: ${pythonStats.total}`);
    console.log(`  Lessons with CRITICAL issues: ${pythonStats.withIssues}`);
    console.log(`  Lessons with warnings: ${pythonStats.withWarnings}`);
    console.log(`  Average code length: ${pythonStats.avgCodeLength} chars`);
    console.log(`  Average tutorial length: ${pythonStats.avgTutorialLength} chars`);
    console.log(`  Average tags per lesson: ${pythonStats.avgTagCount}`);
    console.log();
    console.log('  Difficulty distribution:');
    Object.entries(pythonStats.byDifficulty).forEach(([diff, count]) => {
      if (count > 0) {
        const percent = ((count / pythonStats.total) * 100).toFixed(1);
        console.log(`    ${diff}: ${count} (${percent}%)`);
      }
    });

    console.log();

    console.log('JAVA LESSONS:');
    console.log(`  Total lessons: ${javaStats.total}`);
    console.log(`  Lessons with CRITICAL issues: ${javaStats.withIssues}`);
    console.log(`  Lessons with warnings: ${javaStats.withWarnings}`);
    console.log(`  Average code length: ${javaStats.avgCodeLength} chars`);
    console.log(`  Average tutorial length: ${javaStats.avgTutorialLength} chars`);
    console.log(`  Average tags per lesson: ${javaStats.avgTagCount}`);
    console.log();
    console.log('  Difficulty distribution:');
    Object.entries(javaStats.byDifficulty).forEach(([diff, count]) => {
      if (count > 0) {
        const percent = ((count / javaStats.total) * 100).toFixed(1);
        console.log(`    ${diff}: ${count} (${percent}%)`);
      }
    });

    console.log();

    // Show critical issues if any
    const pythonIssues = pythonResults.filter(r => r.validation.issues.length > 0);
    const javaIssues = javaResults.filter(r => r.validation.issues.length > 0);

    if (pythonIssues.length > 0 || javaIssues.length > 0) {
      console.log('='.repeat(80));
      console.log('CRITICAL ISSUES FOUND');
      console.log('='.repeat(80));

      if (pythonIssues.length > 0) {
        console.log(`\nPython (${pythonIssues.length} lessons):`);
        pythonIssues.slice(0, 5).forEach(({ lesson, validation }) => {
          console.log(`  Lesson ${lesson.id}: ${validation.issues.join(', ')}`);
        });
        if (pythonIssues.length > 5) {
          console.log(`  ... and ${pythonIssues.length - 5} more`);
        }
      }

      if (javaIssues.length > 0) {
        console.log(`\nJava (${javaIssues.length} lessons):`);
        javaIssues.slice(0, 5).forEach(({ lesson, validation }) => {
          console.log(`  Lesson ${lesson.id}: ${validation.issues.join(', ')}`);
        });
        if (javaIssues.length > 5) {
          console.log(`  ... and ${javaIssues.length - 5} more`);
        }
      }
    } else {
      console.log('='.repeat(80));
      console.log('✅ NO CRITICAL ISSUES FOUND!');
      console.log('='.repeat(80));
    }

    console.log();

    // Quality grade
    console.log('='.repeat(80));
    console.log('QUALITY GRADE CALCULATION');
    console.log('='.repeat(80));
    console.log();

    const totalIssues = pythonStats.withIssues + javaStats.withIssues;
    const totalWarnings = pythonStats.withWarnings + javaStats.withWarnings;
    const totalLessons = pythonStats.total + javaStats.total;

    const issueRate = (totalIssues / totalLessons) * 100;
    const warningRate = (totalWarnings / totalLessons) * 100;

    console.log(`Total lessons: ${totalLessons}`);
    console.log(`Critical issues: ${totalIssues} (${issueRate.toFixed(2)}%)`);
    console.log(`Warnings: ${totalWarnings} (${warningRate.toFixed(2)}%)`);
    console.log();

    let grade = 'A+';
    let reasoning = [];

    if (issueRate > 5) {
      grade = 'B';
      reasoning.push(`${issueRate.toFixed(1)}% critical issues (target: <5%)`);
    } else if (issueRate > 2) {
      grade = 'A-';
      reasoning.push(`${issueRate.toFixed(1)}% critical issues (target: <2%)`);
    } else if (issueRate > 0) {
      grade = 'A';
      reasoning.push(`${issueRate.toFixed(1)}% critical issues (target: 0%)`);
    }

    if (warningRate > 20 && grade === 'A+') {
      grade = 'A';
      reasoning.push(`${warningRate.toFixed(1)}% warnings (acceptable but not perfect)`);
    }

    console.log(`OVERALL GRADE: ${grade}`);
    if (reasoning.length > 0) {
      console.log('\nReasoning:');
      reasoning.forEach(r => console.log(`  - ${r}`));
    } else {
      console.log('\nAll quality metrics meet A+ standards!');
    }

    // Save report
    const report = {
      timestamp: new Date().toISOString(),
      summary: {
        totalLessons,
        criticalIssues: totalIssues,
        warnings: totalWarnings,
        grade
      },
      python: {
        stats: pythonStats,
        issuesCount: pythonIssues.length,
        issues: pythonIssues.slice(0, 20).map(({ lesson, validation }) => ({
          id: lesson.id,
          title: lesson.title,
          issues: validation.issues
        }))
      },
      java: {
        stats: javaStats,
        issuesCount: javaIssues.length,
        issues: javaIssues.slice(0, 20).map(({ lesson, validation }) => ({
          id: lesson.id,
          title: lesson.title,
          issues: validation.issues
        }))
      }
    };

    const reportPath = path.join(process.cwd(), 'FINAL_VALIDATION_REPORT.json');
    fs.writeFileSync(reportPath, JSON.stringify(report, null, 2));

    console.log();
    console.log('='.repeat(80));
    console.log(`Detailed report saved to: ${reportPath}`);

  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
}

main();
