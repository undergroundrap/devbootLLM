/**
 * Framework lesson validation - syntax-only checking for lessons
 * that require external dependencies (Flask, Spring Boot, etc.)
 */

const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const BASE_TMP_DIR = (process.env.RUN_TMP_DIR && process.env.RUN_TMP_DIR.trim()) || os.tmpdir();

/**
 * Validate Python syntax only (don't execute)
 */
function validatePythonSyntax(code, frameworkName, callback) {
    // Use python -m py_compile for syntax checking
    const tempDir = fs.mkdtempSync(path.join(BASE_TMP_DIR, 'py-syntax-'));
    const filePath = path.join(tempDir, 'check.py');

    fs.writeFileSync(filePath, code);

    // Use python -m py_compile for syntax checking
    const pythonCmd = process.platform === 'win32' ? 'py' : 'python3';
    const args = process.platform === 'win32' ? ['-3', '-m', 'py_compile', filePath] : ['-m', 'py_compile', filePath];

    const check = spawn(pythonCmd, args);
    let stderr = '';

    check.stderr.on('data', (data) => {
        stderr += data.toString();
    });

    check.on('close', (code) => {
        // Cleanup
        try {
            fs.unlinkSync(filePath);
            fs.rmdirSync(tempDir, { recursive: true });
        } catch (_) { /* ignore cleanup errors */ }

        if (code === 0) {
            // Syntax valid
            callback(null, {
                success: true,
                isFramework: true,
                frameworkName: frameworkName || 'Framework',
                message: 'Syntax Valid',
                output: `✓ Python syntax is correct!\n\nℹ️  This is a ${frameworkName || 'framework'} lesson.\nTo run this code locally, install: pip install ${(frameworkName || 'framework').toLowerCase()}\n\nYour code will be validated for syntax only in this platform.`
            });
        } else {
            // Syntax error
            callback(null, {
                success: false,
                isFramework: true,
                frameworkName: frameworkName || 'Framework',
                error: true,
                type: 'syntax',
                output: stderr || 'Syntax error in code'
            });
        }
    });

    check.on('error', (err) => {
        // Cleanup
        try {
            fs.unlinkSync(filePath);
            fs.rmdirSync(tempDir, { recursive: true });
        } catch (_) { /* ignore */ }

        callback(err);
    });
}

/**
 * Validate Java syntax only (compile but don't run)
 */
function validateJavaSyntax(code, frameworkName, callback) {
    const tempDir = fs.mkdtempSync(path.join(BASE_TMP_DIR, 'java-syntax-'));
    const filePath = path.join(tempDir, 'Main.java');

    fs.writeFileSync(filePath, code);

    // Compile only - don't execute
    const compile = spawn('javac', [filePath], { cwd: tempDir });
    let compileError = '';

    compile.stderr.on('data', (data) => {
        compileError += data.toString();
    });

    compile.on('close', (code) => {
        // Cleanup
        try {
            // Remove .java and .class files
            fs.readdirSync(tempDir).forEach(file => {
                fs.unlinkSync(path.join(tempDir, file));
            });
            fs.rmdirSync(tempDir);
        } catch (_) { /* ignore cleanup errors */ }

        if (code === 0) {
            // Compilation successful
            callback(null, {
                success: true,
                isFramework: true,
                frameworkName: frameworkName || 'Framework',
                message: 'Syntax Valid',
                output: `✓ Java code compiles successfully!\n\nℹ️  This is a ${frameworkName || 'framework'} lesson.\nTo run this code locally, add the framework dependency to your pom.xml or build.gradle\n\nYour code has been validated for compilation only in this platform.`
            });
        } else {
            // Check if errors are only framework-related (missing packages/symbols)
            // These are expected for framework code without dependencies
            const isOnlyFrameworkErrors = compileError &&
                !compileError.includes('class, interface, enum, or record expected') &&
                !compileError.includes('illegal start of expression') &&
                !compileError.includes('not a statement') &&
                !compileError.includes(';' + ' expected') &&
                !compileError.includes('reached end of file while parsing') &&
                (compileError.includes('package') && compileError.includes('does not exist') ||
                 compileError.includes('cannot find symbol'));

            if (isOnlyFrameworkErrors) {
                // Framework imports missing, but syntax is valid
                callback(null, {
                    success: true,
                    isFramework: true,
                    frameworkName: frameworkName || 'Framework',
                    message: 'Syntax Valid',
                    output: `✓ Java syntax is correct!\n\nℹ️  This is a ${frameworkName || 'framework'} lesson.\nTo run this code locally, add the framework dependency to your pom.xml or build.gradle\n\nYour code has been validated for syntax only in this platform.\n\nNote: Framework imports are not available in this environment, but your code structure is correct.`
                });
            } else {
                // Actual syntax error
                callback(null, {
                    success: false,
                    isFramework: true,
                    frameworkName: frameworkName || 'Framework',
                    error: true,
                    type: 'compilation',
                    output: compileError || 'Compilation error'
                });
            }
        }
    });

    compile.on('error', (err) => {
        // Cleanup
        try {
            fs.readdirSync(tempDir).forEach(file => {
                fs.unlinkSync(path.join(tempDir, file));
            });
            fs.rmdirSync(tempDir);
        } catch (_) { /* ignore */ }

        callback(err);
    });
}

module.exports = {
    validatePythonSyntax,
    validateJavaSyntax
};
