def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue

                cat_id, name, age = line.strip().split(",")

                if not cat_id or not name or not age.isdigit():
                    raise ValueError("Invalid cat data")

                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except (ValueError, UnicodeError):
        print("Некоректні дані у файлі.")
        return []
    except OSError:
        print("Не вдалося прочитати файл.")
        return []

    return cats


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
