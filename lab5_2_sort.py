import re

items = [
    "English",
    "інформація",
    "android",
    "Windows",
    "Добрий день",
    "матриця",
    "актова зала",
    "біоресурси",
    "єдиний",
    "кава",
    "Інститут",
    "Їжак",
    "їсти",
    "Zoo",
    "python"
]

CYRILLIC_RE = re.compile(r'^[\u0400-\u04FF]')

def starts_with_cyrillic(s: str) -> bool:
    s = s.strip()
    return bool(CYRILLIC_RE.match(s))

def sort_key(s: str):
    normalized = s.casefold()
    group = 0 if starts_with_cyrillic(s) else 1
    return (group, normalized)

def main():
    print("Заданий список:")
    print(items)
    sorted_items = sorted(items, key=sort_key)
    print("\nВідсортований список:")
    print(sorted_items)

if __name__ == "__main__":
    main()