"""
Intermediate Exercise
Estimated time: 20
Actual time: 15
"""
from prac_06.programming_language import ProgrammingLanguage


def main():
    """Instantiate 3 programming languages and print the dynamically typed languages."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    programming_languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for programming_language in programming_languages:
        if programming_language.is_dynamic():
            print(programming_language.name)


main()
