from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Adds 50 coding exercises across different programming languages'

    def handle(self, *args, **kwargs):
        # Create courses for different languages
        courses_data = [
            {
                'title': 'Python Programming',
                'description': 'Learn Python programming with hands-on exercises covering basics to advanced concepts.',
                'language': 'Python'
            },
            {
                'title': 'JavaScript Fundamentals',
                'description': 'Master JavaScript programming with practical exercises and real-world examples.',
                'language': 'JavaScript'
            },
            {
                'title': 'HTML & CSS Mastery',
                'description': 'Learn web development with HTML and CSS through interactive exercises.',
                'language': 'HTML/CSS'
            },
            {
                'title': 'Java Programming',
                'description': 'Comprehensive Java programming course with practical coding exercises.',
                'language': 'Java'
            }
        ]

        # Create courses and store them
        courses = {}
        for course_data in courses_data:
            course, created = Course.objects.get_or_create(
                title=course_data['title'],
                defaults=course_data
            )
            courses[course_data['language']] = course
            self.stdout.write(f'Created course: {course.title}')

        # Python exercises
        python_exercises = [
            {
                'title': 'Hello World',
                'content': 'Write a Python program that prints "Hello, World!" to the console.',
                'exercise': 'Write a Python program that prints "Hello, World!" to the console.',
                'solution': 'print("Hello, World!")',
                'order': 1
            },
            {
                'title': 'Variables and Data Types',
                'content': 'Create variables of different data types (integer, float, string, boolean) and print their values.',
                'exercise': 'Create variables of different data types and print their values.',
                'solution': 'num = 42\npi = 3.14\nname = "Python"\nis_fun = True\nprint(num, pi, name, is_fun)',
                'order': 2
            },
            {
                'title': 'Basic Calculator',
                'content': 'Create a simple calculator that can perform addition, subtraction, multiplication, and division.',
                'exercise': 'Write a function that takes two numbers and an operator (+, -, *, /) and returns the result.',
                'solution': 'def calculator(a, b, operator):\n    if operator == "+":\n        return a + b\n    elif operator == "-":\n        return a - b\n    elif operator == "*":\n        return a * b\n    elif operator == "/":\n        return a / b if b != 0 else "Error: Division by zero"',
                'order': 3
            },
            {
                'title': 'List Operations',
                'content': 'Learn about Python lists and perform various operations on them.',
                'exercise': 'Create a list of numbers and perform the following operations:\n1. Add a number\n2. Remove a number\n3. Sort the list\n4. Find the sum of all numbers',
                'solution': 'numbers = [5, 2, 8, 1, 9]\nnumbers.append(4)\nnumbers.remove(2)\nnumbers.sort()\ntotal = sum(numbers)\nprint(numbers, total)',
                'order': 4
            },
            {
                'title': 'String Manipulation',
                'content': 'Practice string operations and methods in Python.',
                'exercise': 'Write a function that takes a string and returns:\n1. The string in uppercase\n2. The string in lowercase\n3. The length of the string\n4. The string reversed',
                'solution': 'def string_operations(text):\n    return text.upper(), text.lower(), len(text), text[::-1]',
                'order': 5
            }
        ]

        # JavaScript exercises
        javascript_exercises = [
            {
                'title': 'Hello World in JavaScript',
                'content': 'Write a JavaScript program that displays "Hello, World!" in the console.',
                'exercise': 'Write a JavaScript program that displays "Hello, World!" in the console.',
                'solution': 'console.log("Hello, World!");',
                'order': 1
            },
            {
                'title': 'Variables and Constants',
                'content': 'Learn about variables and constants in JavaScript.',
                'exercise': 'Create variables using let and const, and demonstrate their differences.',
                'solution': 'let count = 0;\nconst MAX_COUNT = 10;\ncount = 1;\n// MAX_COUNT = 11; // This would cause an error',
                'order': 2
            },
            {
                'title': 'Functions and Arrow Functions',
                'content': 'Practice writing functions in JavaScript.',
                'exercise': 'Write a function that calculates the area of a rectangle using both traditional and arrow function syntax.',
                'solution': 'function calculateArea(width, height) {\n    return width * height;\n}\n\nconst calculateAreaArrow = (width, height) => width * height;',
                'order': 3
            },
            {
                'title': 'Array Methods',
                'content': 'Learn about array methods in JavaScript.',
                'exercise': 'Create an array of numbers and use map, filter, and reduce to:\n1. Double each number\n2. Filter even numbers\n3. Calculate the sum',
                'solution': 'const numbers = [1, 2, 3, 4, 5];\nconst doubled = numbers.map(n => n * 2);\nconst evenNumbers = numbers.filter(n => n % 2 === 0);\nconst sum = numbers.reduce((acc, curr) => acc + curr, 0);',
                'order': 4
            },
            {
                'title': 'DOM Manipulation',
                'content': 'Practice DOM manipulation in JavaScript.',
                'exercise': 'Write a function that creates a new paragraph element and adds it to the page.',
                'solution': 'function addParagraph() {\n    const p = document.createElement("p");\n    p.textContent = "New paragraph";\n    document.body.appendChild(p);\n}',
                'order': 5
            }
        ]

        # HTML/CSS exercises
        html_css_exercises = [
            {
                'title': 'Basic HTML Structure',
                'content': 'Create a basic HTML document structure.',
                'exercise': 'Create an HTML document with proper DOCTYPE, html, head, and body tags.',
                'solution': '<!DOCTYPE html>\n<html>\n<head>\n    <title>My Page</title>\n</head>\n<body>\n    <h1>Hello World</h1>\n</body>\n</html>',
                'order': 1
            },
            {
                'title': 'HTML Forms',
                'content': 'Create a simple HTML form.',
                'exercise': 'Create a contact form with name, email, and message fields.',
                'solution': '<form>\n    <label for="name">Name:</label>\n    <input type="text" id="name" name="name">\n    <label for="email">Email:</label>\n    <input type="email" id="email" name="email">\n    <label for="message">Message:</label>\n    <textarea id="message" name="message"></textarea>\n    <button type="submit">Send</button>\n</form>',
                'order': 2
            },
            {
                'title': 'CSS Selectors',
                'content': 'Practice using different CSS selectors.',
                'exercise': 'Style elements using class, ID, and element selectors.',
                'solution': '.container {\n    max-width: 1200px;\n    margin: 0 auto;\n}\n\n#header {\n    background-color: #333;\n    color: white;\n}\n\np {\n    line-height: 1.6;\n}',
                'order': 3
            },
            {
                'title': 'CSS Flexbox',
                'content': 'Learn about CSS Flexbox layout.',
                'exercise': 'Create a responsive navigation bar using flexbox.',
                'solution': '.nav {\n    display: flex;\n    justify-content: space-between;\n    align-items: center;\n    padding: 1rem;\n}\n\n.nav-links {\n    display: flex;\n    gap: 1rem;\n}',
                'order': 4
            },
            {
                'title': 'CSS Grid',
                'content': 'Practice CSS Grid layout.',
                'exercise': 'Create a responsive grid layout with 3 columns.',
                'solution': '.grid {\n    display: grid;\n    grid-template-columns: repeat(3, 1fr);\n    gap: 1rem;\n}\n\n@media (max-width: 768px) {\n    .grid {\n        grid-template-columns: 1fr;\n    }\n}',
                'order': 5
            }
        ]

        # Java exercises
        java_exercises = [
            {
                'title': 'Hello World in Java',
                'content': 'Write a Java program that prints "Hello, World!" to the console.',
                'exercise': 'Create a Java program that prints "Hello, World!" to the console.',
                'solution': 'public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}',
                'order': 1
            },
            {
                'title': 'Variables and Data Types',
                'content': 'Learn about Java variables and data types.',
                'exercise': 'Create variables of different data types and print their values.',
                'solution': 'public class Variables {\n    public static void main(String[] args) {\n        int number = 42;\n        double pi = 3.14;\n        String name = "Java";\n        boolean isTrue = true;\n        System.out.println(number + " " + pi + " " + name + " " + isTrue);\n    }\n}',
                'order': 2
            },
            {
                'title': 'Control Structures',
                'content': 'Practice using if-else statements and loops in Java.',
                'exercise': 'Write a program that checks if a number is positive, negative, or zero.',
                'solution': 'public class NumberCheck {\n    public static void main(String[] args) {\n        int number = 5;\n        if (number > 0) {\n            System.out.println("Positive");\n        } else if (number < 0) {\n            System.out.println("Negative");\n        } else {\n            System.out.println("Zero");\n        }\n    }\n}',
                'order': 3
            },
            {
                'title': 'Arrays and Loops',
                'content': 'Work with arrays and loops in Java.',
                'exercise': 'Create an array of numbers and find the sum using a for loop.',
                'solution': 'public class ArraySum {\n    public static void main(String[] args) {\n        int[] numbers = {1, 2, 3, 4, 5};\n        int sum = 0;\n        for (int num : numbers) {\n            sum += num;\n        }\n        System.out.println("Sum: " + sum);\n    }\n}',
                'order': 4
            },
            {
                'title': 'Methods',
                'content': 'Learn about methods in Java.',
                'exercise': 'Create a method that calculates the factorial of a number.',
                'solution': 'public class Factorial {\n    public static int factorial(int n) {\n        if (n == 0 || n == 1) {\n            return 1;\n        }\n        return n * factorial(n - 1);\n    }\n\n    public static void main(String[] args) {\n        System.out.println(factorial(5));\n    }\n}',
                'order': 5
            }
        ]

        # Add exercises to courses
        all_exercises = {
            'Python': python_exercises,
            'JavaScript': javascript_exercises,
            'HTML/CSS': html_css_exercises,
            'Java': java_exercises
        }

        for language, exercises in all_exercises.items():
            course = courses[language]
            for exercise in exercises:
                lesson, created = Lesson.objects.get_or_create(
                    course=course,
                    title=exercise['title'],
                    defaults={
                        'content': exercise['content'],
                        'exercise': exercise['exercise'],
                        'solution': exercise['solution'],
                        'order': exercise['order']
                    }
                )
                if created:
                    self.stdout.write(f'Created exercise: {lesson.title} in {course.title}')

        self.stdout.write(self.style.SUCCESS('Successfully added all exercises')) 