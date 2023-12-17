from addressbook import AddressBook, Record


def parse_input(user_input):
    if not user_input.strip():
        return "empty", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except ValueError as e:
            return f"ValueError: {e}"
        
        except KeyError as e:
            return f"KeyError: {e}"
        
        except IndexError:
            return "Invalid index in input."
        
        except Exception as e:
            return f"An unexpected error occurred: {e}"
        
    return inner


@input_error
def add_contact(args, book):
    if len(args) >= 2:
        name, phone = args[0], args[1]
        record = book.find(name)

        if not record:
            record = Record(name)
            book.add_record(record)
        record.add_phone(phone)
        return "Contact is added."
    
    else:
        return "Invalid command. Try this way: add [name] [phone]"


@input_error
def change_contact(args, book):
    if len(args) == 3:
        name, old_phone, new_phone = args
        record = book.find(name)

        if record:
            record.edit_phone(old_phone, new_phone)
            return "Phone number is updated."
        
        else:
            return f"Contact '{name}' is not found."
        
    else:
        return "Invalid command. Try this way: change [name] [old phone] [new phone]"


@input_error
def show_phone(args, book):
    if len(args) == 1:
        name = args[0]
        record = book.find(name)

        if record:
            return str(record)
        
        else:
            return f"Contact '{name}' is not found."
        
    else:
        return "Invalid command. Try this way: phone [name]"


@input_error
def show_all(book):
    return "\n".join(str(record) for record in book.data.values())


@input_error
def add_birthday(args, book):
    if len(args) == 2:
        name, birthday = args
        record = book.find(name)

        if record:
            record.add_birthday(birthday)
            return f"Birthday is added for {name}."
        
        else:
            return f"Contact '{name}' not found."
        
    else:
        return "Invalid command. Try this way: add-birthday [name] [birthday]"


@input_error
def show_birthday(args, book):
    if len(args) == 1:
        name = args[0]
        record = book.find(name)

        if record and record.birthday:
            return f"{name}'s birthday: {record.birthday.value}"
        
        else:
            return f"Birthday is not specified for '{name}'."
        
    else:
        return "Invalid command. Try this way: show-birthday [name]"


@input_error
def show_birthdays(book):
    return book.get_birthdays_per_week()


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("Hi! How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(show_birthdays(book))

        else:
            print("Invalid command. Try again!")


if __name__ == "__main__":
    main()
