class PythonIntroduction:
    def __init__(self):
        self.title = "Python Programming Language"
        self.description = ("Python is an interpreted, high-level and general-purpose programming language. "Python's design philosophy emphasizes code readability with its notable use of significant indentation.")
        self.features = [
            "Easy to learn and use",
            "Expressive language",
            "Interpreted language",
            "Cross-platform language",
            "Free and open-source",
            "Object-oriented",
            "Extensible",
            "Large standard library",
            "GUI Programming support",
            "Integrated",
            "Embeddable"
        ]
        self.advantages = [
            "Simple and easy to learn syntax",
            "Increased productivity",
            "Extensive libraries and frameworks",
            "Vibrant community support",
            "Versatile and powerful",
            "Strong support for integration with other languages and tools"
        ]
    def introduce(self):
        print(f"Introduction to {self.title}")
        print(self.description)
        print()
        print("Features of Python:")
        for feature in self.features:
            print(f"- {feature}")
        print()
        print("Advantages of Python:")
        for advantage in self.advantages:
            print(f"- {advantage}")
if __name__ == "__main__":
    intro = PythonIntroduction()
    intro.introduce()