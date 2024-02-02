import sys
from pathlib import Path
import shutil
import re

OTHERS_FOLDER = 'others'
ARCHIVES_FOLDER = 'archives'
CATEGORIES = {
    'images': ['.jpeg', '.png', '.jpg', '.svg'],
    'videos': ['.avi', '.mp4', '.mov', '.mkv'],
    'musics': ['.mp3', '.ogg', '.wav', '.amr'],
    'documents': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    'archives': ['.zip', '.gz', '.tar']
}

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for c, t in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = t
    TRANS[ord(c.upper())] = t.upper()


def translate(name):
    return name.translate(TRANS)


def normalize(filename: str):
    transliterated_text = translate(filename)
    normalized_text = re.sub(r'\W+', '_', transliterated_text)
    return normalized_text


def move(file, to_folder):
    to_folder.mkdir(exist_ok=True)
    shutil.move(str(file), str(to_folder / file.name))


def clear_empty_folders(path):
    for item in path.iterdir():
        if item.is_dir() and not any(item.iterdir()):
            item.rmdir()


def process_archive(file):
    shutil.unpack_archive(file, file.parent / file.stem)
    file.unlink()


def sort_folder(path):
    known_ext = set()
    unknown_ext = set()
    counter = 0

    for file in path.iterdir():
        if file.is_dir():
            if file.name not in CATEGORIES.keys() and file.name != OTHERS_FOLDER:
                sort_folder(file)
        else:
            if file.stem == '':
                break
            ext = file.suffix.lower()
            normalized_name = normalize(file.stem) + ext
            file = file.rename(normalized_name)

            category = next((cat for cat, exts in CATEGORIES.items() if ext in exts), OTHERS_FOLDER)
            move(file, path / category)

            if category == ARCHIVES_FOLDER:
                process_archive(path / category / file)

            (known_ext if category != OTHERS_FOLDER else unknown_ext).add(ext)
            counter += 1

    return known_ext, unknown_ext, counter


def main():
    print("Homework 6. Сортування папки з мотлохом")
    if len(sys.argv) != 2:
        print("Помилка: невірна кількість переданих аргументів. Наприклад: python sort.py /user/Desktop/Мотлох")
        sys.exit(1)

    sort_folder_path = Path(sys.argv[1])
    if not sort_folder_path.is_dir():
        print(f"Помилка: {sys.argv[1]} не є папкою або не існує")
        sys.exit(1)

    print(f"Папка: {sort_folder_path.name}\n")

    known_ext, unknown_ext, counter = sort_folder(sort_folder_path)
    clear_empty_folders(sort_folder_path)

    print("Програма завершила свою роботу. Ось деяка статистика ...")
    print(f"Кількість файлів: {counter}")
    print(f"Відомі розширення: {', '.join(known_ext)}")
    print(f"Не відомі розширення: {', '.join(unknown_ext)}")


if __name__ == '__main__':
    main()
