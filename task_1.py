def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue

                name, salary = line.strip().split(",")

                if not name.strip():
                    raise ValueError("Missing developer name")

                total += int(salary)
                count += 1

    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0
    except (ValueError, UnicodeError):
        print("Некоректні дані у файлі.")
        return 0, 0
    except OSError:
        print("Не вдалося прочитати файл.")
        return 0, 0

    if count == 0:
        return 0, 0

    average = total / count

    if average.is_integer():
        average = int(average)

    return total, average


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")