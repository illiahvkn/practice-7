"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""


# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.


# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"
math_grades = []
python_grades = []
english_grades = []
current_top_grade = 0
# TODO 1: відкрийте INPUT_FILE через with open(...) as f:
#   і пропустіть рядок заголовка (next(f))
with open(INPUT_FILE, "r", encoding="UTF-8") as f:
    lines = f.readlines()
    for line in lines[1:]:
        line = line.strip()
        line_split = line.split(",")
        math_grades.append(int(line_split[1]))
        math_sum = sum(math_grades)
        python_grades.append(int(line_split[2]))
        python_sum = sum(python_grades)
        english_grades.append(int(line_split[3]))
        english_sum = sum(english_grades)
        n_students = len(lines[1:])
        student_avg = ((int(line_split[1])) + (int(line_split[2]) + int(line_split[3]))) / 3
        student_sum = student_avg
        if student_avg > current_top_grade:
            current_top_grade = student_avg
        math_avg = math_sum / n_students
        python_avg = python_sum / n_students
        english_avg = english_sum / n_students
        avg = (math_avg + python_avg + english_avg) / 3
    print(f"Всього студентів: {n_students}")
    print(f"Найвища середня оцінка: {current_top_grade}")
    print(f"Середня оцінка з математики: {math_avg}")
    print(f"Середня оцінка з Python: {python_avg}")
    print(f"Середня оцінка з англійської мови: {english_avg}")

    with open(OUTPUT_FILE, mode="w", encoding="UTF-8") as report:
        report.write(f"Загальна кількість студентів: {round(n_students, 1)}\n")
        report.write(f"Середній бал: {round(avg, 1)}\n")
        report.write(f"Середня оцінка з математики: {round(math_avg, 1)}\n")
        report.write(f"Середня оцінка з Python: {round(python_avg, 1)}\n")
        report.write(f"Середня оцінка з англійської мови: {round(english_avg, 1)}\n")
# TODO 2: пройдіться по рядках файлу (for line in f:), для кожного рядка:
#   - приберіть символ переносу рядка (line.strip())
#   - розбийте рядок по комі (line.split(","))
#   - перетворіть оцінки на числа (int або float)

# TODO 3: по ходу циклу накопичуйте:
#   - суми оцінок з кожного предмета та кількість студентів
#   - найкращого студента (ім'я та його середній бал) — порівнюйте
#     середній бал поточного студента з найкращим на цей момент

# TODO 4: після циклу порахуйте середній бал по класу з кожного предмета
#   (сума / кількість студентів)


# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):
#
#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (python analyze.py) і перевірте, що в папці
# з'явився файл result.txt.


# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
