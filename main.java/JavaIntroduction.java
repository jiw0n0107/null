public class JavaIntroduction {
    public static void main(String[] args) {
        String title = "Java Programming Language";
        String description = "Java is a high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible.";
        String[] features = {
                "Platform Independence",
                "Object-Oriented",
                "Robust and Secure",
                "Multithreaded",
                "High Performance",
                "Distributed Computing"
        };
        String[] advantages = {
                "Write Once, Run Anywhere (WORA)",
                "Rich API",
                "Large Community Support",
                "Comprehensive Development Tools",
                "Automatic Memory Management",
                "Strong Security Features"
        };

        System.out.println("Introduction to " + title);
        System.out.println(description);
        System.out.println();

        System.out.println("Features of Java:");
        for (String feature : features) {
            System.out.println("- " + feature);
        }
        System.out.println();

        System.out.println("Advantages of Java:");
        for (String advantage : advantages) {
            System.out.println("- " + advantage);
        }
    }
}
