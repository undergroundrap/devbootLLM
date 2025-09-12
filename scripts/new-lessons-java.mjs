export const lessons = [
  {
    title: "Regex Basics: Extract Number",
    language: "java",
    description: "Use java.util.regex to find the first number in a string.",
    initialCode: `import java.util.regex.*;
public class Main {
    public static void main(String[] args) {
        String text = "Order #A-1023-Z";
        // Print the number 1023 using regex
    }
}
`,
    fullSolution: `import java.util.regex.*;
public class Main {
    public static void main(String[] args) {
        String text = "Order #A-1023-Z";
        Matcher m = Pattern.compile("\\d+").matcher(text);
        if (m.find()) {
            System.out.println(m.group());
        }
    }
}
`,
    expectedOutput: "1023",
    tutorial: `<p class=\"mb-4 text-gray-300\">The Pattern/Matcher API searches text for regex patterns. Use find() to locate the next match and group() to retrieve it.</p>
<h4 class=\"font-semibold text-gray-200 mb-2\">Example:</h4>
<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">Matcher m = Pattern.compile("[a-zA-Z]+\\d+").matcher("ID A42 B7");
if (m.find()) {
    System.out.println(m.group()); // A42
}</pre></div>`
  },
  {
    title: "Generics: Upper-Bounded Wildcards",
    language: "java",
    description: "Implement sumOfList(List<? extends Number>) and print the sum of integers.",
    initialCode: `import java.util.*;
public class Main {
    static double sumOfList(/* TODO */) {
        return 0.0;
    }
    public static void main(String[] args) {
        List<Integer> ints = Arrays.asList(1, 2, 3);
        System.out.println(sumOfList(ints));
    }
}
`,
    fullSolution: `import java.util.*;
public class Main {
    static double sumOfList(List<? extends Number> list) {
        double s = 0.0;
        for (Number n : list) s += n.doubleValue();
        return s;
    }
    public static void main(String[] args) {
        List<Integer> ints = Arrays.asList(1, 2, 3);
        System.out.println(sumOfList(ints));
    }
}
`,
    expectedOutput: "6.0",
    tutorial: `<p class=\"mb-4 text-gray-300\">Use ? extends Number to accept lists of Number or its subclasses (Integer, Double, ...). Read from producers (PECS rule).</p>
<h4 class=\"font-semibold text-gray-200 mb-2\">Example:</h4>
<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">static double sum(List<? extends Number> xs) {
    double s = 0;
    for (Number n : xs) s += n.doubleValue();
    return s;
}</pre></div>`
  }
];

