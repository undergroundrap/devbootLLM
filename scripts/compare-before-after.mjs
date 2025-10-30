import fs from 'fs';
import path from 'path';

const PUBLIC_DIR = path.join(process.cwd(), 'public');

function parseValidationReport(reportText) {
  const metrics = {};

  // Parse key metrics from the text report
  const totalMatch = reportText.match(/Total lessons:\s*(\d+)/);
  if (totalMatch) metrics.totalLessons = parseInt(totalMatch[1]);

  const issuesMatch = reportText.match(/Critical issues:\s*(\d+)/);
  if (issuesMatch) metrics.criticalIssues = parseInt(issuesMatch[1]);

  const warningsMatch = reportText.match(/Warnings:\s*(\d+)/);
  if (warningsMatch) metrics.warnings = parseInt(warningsMatch[1]);

  const gradeMatch = reportText.match(/OVERALL GRADE:\s*([A-F][+-]?)/);
  if (gradeMatch) metrics.grade = gradeMatch[1];

  // Parse Python metrics
  const pythonTotalMatch = reportText.match(/PYTHON LESSONS:[\s\S]*?Total lessons:\s*(\d+)/);
  if (pythonTotalMatch) metrics.pythonTotal = parseInt(pythonTotalMatch[1]);

  const pythonIssuesMatch = reportText.match(/PYTHON LESSONS:[\s\S]*?Lessons with CRITICAL issues:\s*(\d+)/);
  if (pythonIssuesMatch) metrics.pythonIssues = parseInt(pythonIssuesMatch[1]);

  const pythonWarningsMatch = reportText.match(/PYTHON LESSONS:[\s\S]*?Lessons with warnings:\s*(\d+)/);
  if (pythonWarningsMatch) metrics.pythonWarnings = parseInt(pythonWarningsMatch[1]);

  // Parse Java metrics
  const javaTotalMatch = reportText.match(/JAVA LESSONS:[\s\S]*?Total lessons:\s*(\d+)/);
  if (javaTotalMatch) metrics.javaTotal = parseInt(javaTotalMatch[1]);

  const javaIssuesMatch = reportText.match(/JAVA LESSONS:[\s\S]*?Lessons with CRITICAL issues:\s*(\d+)/);
  if (javaIssuesMatch) metrics.javaIssues = parseInt(javaIssuesMatch[1]);

  const javaWarningsMatch = reportText.match(/JAVA LESSONS:[\s\S]*?Lessons with warnings:\s*(\d+)/);
  if (javaWarningsMatch) metrics.javaWarnings = parseInt(javaWarningsMatch[1]);

  return metrics;
}

function compareMetrics(before, after) {
  const changes = {};
  const regressions = [];
  const improvements = [];

  // Compare each metric
  Object.keys(before).forEach(key => {
    if (typeof before[key] === 'number' && typeof after[key] === 'number') {
      const diff = after[key] - before[key];
      changes[key] = {
        before: before[key],
        after: after[key],
        change: diff,
        changePercent: before[key] > 0 ? ((diff / before[key]) * 100).toFixed(1) : 'N/A'
      };

      // Detect regressions (increase in issues/warnings is bad)
      if (key.includes('Issues') || key.includes('Warnings') || key.includes('issues') || key.includes('warnings')) {
        if (diff > 0) {
          regressions.push({
            metric: key,
            increase: diff,
            severity: key.includes('Critical') || key.includes('Issues') ? 'high' : 'medium'
          });
        } else if (diff < 0) {
          improvements.push({
            metric: key,
            decrease: Math.abs(diff)
          });
        }
      }
    } else if (key === 'grade') {
      changes[key] = {
        before: before[key],
        after: after[key]
      };

      // Check grade changes
      const gradeOrder = ['F', 'D', 'C', 'B-', 'B', 'B+', 'A-', 'A', 'A+'];
      const beforeIndex = gradeOrder.indexOf(before[key]);
      const afterIndex = gradeOrder.indexOf(after[key]);

      if (afterIndex < beforeIndex) {
        regressions.push({
          metric: 'Overall Grade',
          decrease: `${before[key]} → ${after[key]}`,
          severity: 'high'
        });
      } else if (afterIndex > beforeIndex) {
        improvements.push({
          metric: 'Overall Grade',
          increase: `${before[key]} → ${after[key]}`
        });
      }
    }
  });

  return { changes, regressions, improvements };
}

async function main() {
  try {
    const args = process.argv.slice(2);

    if (args.length < 1) {
      console.error('Usage: node compare-before-after.mjs <baseline-file> [current-file]');
      console.error('');
      console.error('Examples:');
      console.error('  node compare-before-after.mjs baseline.txt');
      console.error('  node compare-before-after.mjs baseline.txt current.txt');
      process.exit(1);
    }

    const baselinePath = args[0];
    let currentReport;

    console.log('='.repeat(80));
    console.log('BEFORE/AFTER COMPARISON');
    console.log('='.repeat(80));
    console.log();

    // Read baseline
    if (!fs.existsSync(baselinePath)) {
      console.error(`❌ Baseline file not found: ${baselinePath}`);
      process.exit(1);
    }

    const baselineText = fs.readFileSync(baselinePath, 'utf-8');
    const beforeMetrics = parseValidationReport(baselineText);

    // Get current report
    if (args.length > 1) {
      // Read from file
      const currentPath = args[1];
      if (!fs.existsSync(currentPath)) {
        console.error(`❌ Current file not found: ${currentPath}`);
        process.exit(1);
      }
      currentReport = fs.readFileSync(currentPath, 'utf-8');
    } else {
      // Run validation now
      console.log('Running current validation...');
      const { execSync } = await import('child_process');
      currentReport = execSync('node scripts/comprehensive-validation.mjs', { encoding: 'utf-8' });
    }

    const afterMetrics = parseValidationReport(currentReport);

    // Compare
    const { changes, regressions, improvements } = compareMetrics(beforeMetrics, afterMetrics);

    // Display results
    console.log('METRIC CHANGES');
    console.log('='.repeat(80));
    console.log();

    const keyMetrics = ['totalLessons', 'criticalIssues', 'warnings', 'grade'];
    keyMetrics.forEach(metric => {
      if (changes[metric]) {
        const change = changes[metric];
        if (metric === 'grade') {
          console.log(`${metric}:`);
          console.log(`  Before: ${change.before}`);
          console.log(`  After:  ${change.after}`);
        } else {
          const changeStr = change.change > 0 ? `+${change.change}` : change.change;
          const indicator = change.change === 0 ? '→' : (change.change > 0 ? '↑' : '↓');
          console.log(`${metric}: ${change.before} ${indicator} ${change.after} (${changeStr})`);
        }
        console.log();
      }
    });

    // Show regressions
    if (regressions.length > 0) {
      console.log('='.repeat(80));
      console.log('⚠️  REGRESSIONS DETECTED');
      console.log('='.repeat(80));
      console.log();

      regressions.forEach(reg => {
        const icon = reg.severity === 'high' ? '🔴' : '🟡';
        console.log(`${icon} ${reg.metric}`);
        if (reg.increase) {
          console.log(`   Increased by: ${reg.increase}`);
        }
        if (reg.decrease) {
          console.log(`   Changed: ${reg.decrease}`);
        }
        console.log();
      });

      console.log('ACTION REQUIRED:');
      console.log('  1. Review the changes made');
      console.log('  2. Run: node scripts/comprehensive-validation.mjs');
      console.log('  3. Consider rolling back: git restore public/lessons-*.json');
      console.log();
    } else {
      console.log('='.repeat(80));
      console.log('✅ NO REGRESSIONS DETECTED');
      console.log('='.repeat(80));
      console.log();
    }

    // Show improvements
    if (improvements.length > 0) {
      console.log('='.repeat(80));
      console.log('🎉 IMPROVEMENTS DETECTED');
      console.log('='.repeat(80));
      console.log();

      improvements.forEach(imp => {
        console.log(`✅ ${imp.metric}`);
        if (imp.decrease) {
          console.log(`   Decreased by: ${imp.decrease}`);
        }
        if (imp.increase) {
          console.log(`   Changed: ${imp.increase}`);
        }
        console.log();
      });
    }

    // Overall verdict
    console.log('='.repeat(80));
    console.log('OVERALL VERDICT');
    console.log('='.repeat(80));
    console.log();

    if (regressions.length === 0 && improvements.length > 0) {
      console.log('✅ SAFE TO COMMIT - Quality improved with no regressions');
      console.log();
      console.log('Suggested commit message:');
      console.log(`git commit -m "Improved lessons: ${improvements.map(i => i.metric).join(', ')}"`);
    } else if (regressions.length === 0 && improvements.length === 0) {
      console.log('✅ SAFE TO COMMIT - Quality maintained (no changes)');
    } else {
      const highSeverity = regressions.filter(r => r.severity === 'high').length;
      if (highSeverity > 0) {
        console.log('❌ DO NOT COMMIT - Critical regressions detected');
        console.log('   Recommended action: git restore public/lessons-*.json');
      } else {
        console.log('⚠️  REVIEW NEEDED - Minor regressions detected');
        console.log('   Review changes carefully before committing');
      }
    }

    console.log();

    // Exit code
    process.exit(regressions.length > 0 ? 1 : 0);

  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
}

main();
