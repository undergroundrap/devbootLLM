export const lesson = {
  title: "Files.readString + writeString",
  language: "java",
  description: "Write \"Hello\" to a file with Files.writeString, then read it back and print it.",
  initialCode: `import java.nio.file.*;
public class Main {
    public static void main(String[] args) throws Exception {
        Path p = Path.of("msg.txt");
        // Write \"Hello\" to p, read it back, then print the text
    }
}
`,
  fullSolution: `import java.nio.file.*;
public class Main {
    public static void main(String[] args) throws Exception {
        Path p = Path.of("msg.txt");
        Files.writeString(p, "Hello");
        String s = Files.readString(p);
        System.out.println(s);
    }
}
`,
  expectedOutput: "Hello",
  tutorial: `<p class=\"mb-4 text-gray-300\">Since Java 11, Files.writeString/readString make small text file I/O concise. Use Path.of to build a path relative to the working directory.</p>
<h4 class=\"font-semibold text-gray-200 mb-2\">Example:</h4>
<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">Path p = Path.of("sample.txt");
Files.writeString(p, "Hi");
System.out.println(Files.readString(p)); // Hi</pre></div>`
};

