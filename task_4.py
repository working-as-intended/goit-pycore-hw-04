def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []

    return parts[0].lower(), parts[1:]


def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command."

    name, phone = args
    contacts[name.capitalize()] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command."

    name, phone = args
    name = name.capitalize()

    if name not in contacts:
        return "Contact not found."

    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command."

    name = args[0].capitalize()

    if name not in contacts:
        return "Contact not found."

    return contacts[name]


def show_all(contacts):
    if not contacts:
        return "No contacts found."

    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")

    return "\n".join(result)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"] and not args:
            print("Good bye!")
            break
        elif command == "hello" and not args:
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all" and not args:
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
