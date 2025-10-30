import fs from 'fs';
import path from 'path';

const PUBLIC_DIR = path.join(process.cwd(), 'public');

function analyzeLesson(lesson) {
  const opportunities = [];
  const scores = {
    tutorial: 0,
    examples: 0,
    tags: 0,
    code: 0
  };

  // Check tutorial length (short tutorials could be enhanced)
  const tutorialLength = (lesson.tutorial || '').replace(/<[^>]+>/g, '').trim().length;
  if (tutorialLength < 800) {
    opportunities.push({
      type: 'Short tutorial',
      priority: 'medium',
      suggestion: 'Add more explanations or examples',
      currentLength: tutorialLength
    });
    scores.tutorial = 1;
  } else if (tutorialLength < 1500) {
    scores.tutorial = 3;
  } else {
    scores.tutorial = 5;
  }

  // Check for examples quality
  const hasExamplesSection = /<h4[^>]*>.*?Examples?.*?<\/h4>/i.test(lesson.tutorial);
  if (hasExamplesSection) {
    const examplesMatch = lesson.tutorial.match(/<h4[^>]*>.*?Examples?.*?<\/h4>(.*?)(?=<h4|<div style="background: rgba\(|$)/is);
    if (examplesMatch) {
      const examplesContent = examplesMatch[1];
      const codeBlocks = (examplesContent.match(/<pre/g) || []).length;

      if (codeBlocks === 0) {
        opportunities.push({
          type: 'No code examples',
          priority: 'high',
          suggestion: 'Add concrete code examples to Examples section'
        });
        scores.examples = 1;
      } else if (codeBlocks === 1) {
        opportunities.push({
          type: 'Single example',
          priority: 'low',
          suggestion: 'Consider adding 1-2 more examples showing variations'
        });
        scores.examples = 3;
      } else {
        scores.examples = 5;
      }
    }
  } else {
    scores.examples = 2; // Has no examples section, but that's okay
  }

  // Check tag count (more tags = better discoverability)
  const tagCount = (lesson.tags || []).length;
  if (tagCount < 3) {
    opportunities.push({
      type: 'Few tags',
      priority: 'low',
      suggestion: 'Add more relevant tags for better discoverability',
      currentCount: tagCount
    });
    scores.tags = 2;
  } else if (tagCount < 5) {
    scores.tags = 4;
  } else {
    scores.tags = 5;
  }

  // Check code complexity (very simple code might benefit from enhancements)
  const codeLength = (lesson.fullSolution || '').length;
  const codeLines = (lesson.fullSolution || '').split('\n').length;

  if (codeLength < 100 && codeLines < 5) {
    opportunities.push({
      type: 'Very simple code',
      priority: 'low',
      suggestion: 'Consider adding comments or a slightly more complex variation',
      currentLength: codeLength
    });
    scores.code = 3;
  } else {
    scores.code = 5;
  }

  // Calculate overall improvement score (lower = more opportunity)
  const totalScore = Object.values(scores).reduce((a, b) => a + b, 0);
  const maxScore = 20;
  const improvementPotential = maxScore - totalScore;

  return {
    opportunities,
    scores,
    improvementPotential,
    safetyLevel: calculateSafetyLevel(opportunities)
  };
}

function calculateSafetyLevel(opportunities) {
  // More opportunities with higher priority = more careful approach needed
  const highPriority = opportunities.filter(o => o.priority === 'high').length;
  const mediumPriority = opportunities.filter(o => o.priority === 'medium').length;

  if (highPriority >= 2) return 'careful';
  if (highPriority === 1 || mediumPriority >= 2) return 'moderate';
  return 'safe';
}

async function main() {
  try {
    const args = process.argv.slice(2);
    const options = {
      difficulty: null,
      limit: 20,
      minOpportunities: 1
    };

    // Parse arguments
    for (let i = 0; i < args.length; i++) {
      if (args[i] === '--difficulty' && args[i + 1]) {
        options.difficulty = args[i + 1].toLowerCase();
        i++;
      }
      if (args[i] === '--limit' && args[i + 1]) {
        options.limit = parseInt(args[i + 1]);
        i++;
      }
      if (args[i] === '--min-opportunities' && args[i + 1]) {
        options.minOpportunities = parseInt(args[i + 1]);
        i++;
      }
    }

    console.log('='.repeat(80));
    console.log('IMPROVEMENT OPPORTUNITIES FINDER');
    console.log('='.repeat(80));
    console.log();

    const pythonLessons = JSON.parse(
      fs.readFileSync(path.join(PUBLIC_DIR, 'lessons-python.json'), 'utf-8')
    );
    const javaLessons = JSON.parse(
      fs.readFileSync(path.join(PUBLIC_DIR, 'lessons-java.json'), 'utf-8')
    );

    // Analyze all lessons
    const pythonAnalysis = pythonLessons
      .map(lesson => ({ lesson, analysis: analyzeLesson(lesson) }))
      .filter(({ analysis }) => analysis.opportunities.length >= options.minOpportunities);

    const javaAnalysis = javaLessons
      .map(lesson => ({ lesson, analysis: analyzeLesson(lesson) }))
      .filter(({ analysis }) => analysis.opportunities.length >= options.minOpportunities);

    // Filter by difficulty if specified
    let filteredPython = pythonAnalysis;
    let filteredJava = javaAnalysis;

    if (options.difficulty) {
      filteredPython = pythonAnalysis.filter(({ lesson }) =>
        lesson.tags?.some(tag => tag.toLowerCase() === options.difficulty)
      );
      filteredJava = javaAnalysis.filter(({ lesson }) =>
        lesson.tags?.some(tag => tag.toLowerCase() === options.difficulty)
      );
    }

    // Sort by improvement potential (highest first)
    filteredPython.sort((a, b) => b.analysis.improvementPotential - a.analysis.improvementPotential);
    filteredJava.sort((a, b) => b.analysis.improvementPotential - a.analysis.improvementPotential);

    // Display results
    console.log(`Found ${filteredPython.length} Python lessons with improvement opportunities`);
    console.log(`Found ${filteredJava.length} Java lessons with improvement opportunities`);
    console.log();

    // Show top Python opportunities
    console.log('='.repeat(80));
    console.log(`TOP ${Math.min(options.limit, filteredPython.length)} PYTHON IMPROVEMENT OPPORTUNITIES`);
    console.log('='.repeat(80));
    filteredPython.slice(0, options.limit).forEach(({ lesson, analysis }, index) => {
      console.log();
      console.log(`${index + 1}. Lesson ${lesson.id}: ${lesson.title}`);
      console.log(`   Improvement Potential: ${analysis.improvementPotential}/20`);
      console.log(`   Safety Level: ${analysis.safetyLevel.toUpperCase()}`);
      console.log(`   Tags: ${(lesson.tags || []).join(', ')}`);
      console.log(`   Opportunities:`);
      analysis.opportunities.forEach(opp => {
        console.log(`     • [${opp.priority.toUpperCase()}] ${opp.type}`);
        console.log(`       → ${opp.suggestion}`);
      });
    });

    console.log();

    // Show top Java opportunities
    console.log('='.repeat(80));
    console.log(`TOP ${Math.min(options.limit, filteredJava.length)} JAVA IMPROVEMENT OPPORTUNITIES`);
    console.log('='.repeat(80));
    filteredJava.slice(0, options.limit).forEach(({ lesson, analysis }, index) => {
      console.log();
      console.log(`${index + 1}. Lesson ${lesson.id}: ${lesson.title}`);
      console.log(`   Improvement Potential: ${analysis.improvementPotential}/20`);
      console.log(`   Safety Level: ${analysis.safetyLevel.toUpperCase()}`);
      console.log(`   Tags: ${(lesson.tags || []).join(', ')}`);
      console.log(`   Opportunities:`);
      analysis.opportunities.forEach(opp => {
        console.log(`     • [${opp.priority.toUpperCase()}] ${opp.type}`);
        console.log(`       → ${opp.suggestion}`);
      });
    });

    console.log();
    console.log('='.repeat(80));
    console.log('RECOMMENDATIONS');
    console.log('='.repeat(80));
    console.log();
    console.log('Safe to improve in bulk (5-10 at a time):');
    const safePython = filteredPython.filter(({ analysis }) => analysis.safetyLevel === 'safe').slice(0, 10);
    const safeJava = filteredJava.filter(({ analysis }) => analysis.safetyLevel === 'safe').slice(0, 10);

    console.log(`  Python: ${safePython.map(({ lesson }) => lesson.id).join(', ')}`);
    console.log(`  Java: ${safeJava.map(({ lesson }) => lesson.id).join(', ')}`);
    console.log();
    console.log('Improve one at a time (needs careful review):');
    const carefulPython = filteredPython.filter(({ analysis }) => analysis.safetyLevel === 'careful').slice(0, 5);
    const carefulJava = filteredJava.filter(({ analysis }) => analysis.safetyLevel === 'careful').slice(0, 5);

    if (carefulPython.length > 0) {
      console.log(`  Python: ${carefulPython.map(({ lesson }) => lesson.id).join(', ')}`);
    }
    if (carefulJava.length > 0) {
      console.log(`  Java: ${carefulJava.map(({ lesson }) => lesson.id).join(', ')}`);
    }

    console.log();
    console.log('='.repeat(80));
    console.log('USAGE EXAMPLES');
    console.log('='.repeat(80));
    console.log();
    console.log('# Find beginner lessons to improve:');
    console.log('node scripts/find-improvement-opportunities.mjs --difficulty beginner --limit 10');
    console.log();
    console.log('# Find lessons with 2+ improvement opportunities:');
    console.log('node scripts/find-improvement-opportunities.mjs --min-opportunities 2');
    console.log();
    console.log('# Find top 5 lessons needing improvement:');
    console.log('node scripts/find-improvement-opportunities.mjs --limit 5');

  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
}

main();
