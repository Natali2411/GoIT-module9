from typing import Tuple, List

records = dict()


def input_error(func: callable) -> callable:
    """
    Decorator that wraps the function to handle possible errors.
    :param func: Function that should be wrapped.
    :return: Wrapped function.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as err:
            print(f"There is no such key {err}. Type a correct name!")
        except ValueError as err:
            print(f"Passed values are incorrect. The trace error is '{err}'")
        except IndexError:
            print("Not all params were passed to execute an action.")
    return wrapper


@input_error
def parse_cli_command(cli_input: str) -> Tuple[str, callable, List[str]]:
    """
    Method that parses the typed commands from CLI.
    :param cli_input: String from CLI.
    :return: Function name, function object and function arguments.
    """
    if cli_input == ".":
        return "good_bye", COMMANDS["good bye"], []
    for command_name, func in COMMANDS.items():
        if cli_input.startswith(command_name):
            return command_name, func, cli_input[len(command_name):].strip().split()
    return "unknown", unknown, []


@input_error
def hello() -> str:
    """
    Method that returns greeting to the user.
    :return: Greeting string.
    """
    return "How can I help you?"


@input_error
def add(*args) -> str:
    """
    Method that adds user contacts to the dictionary.
    :param args: Username and phone that should be stored.
    :return: The string with information about adding data into the dictionary.
    """
    rec_id = args[0]
    rec_value = args[1]
    if rec_id in records:
        return f"The client with the name '{rec_id}' can't be added repeatedly, " \
               f"use a 'change' command to update the number for existing user!"
    records[rec_id] = rec_value
    return f"The contact with name '{rec_id}' and '{rec_value}' " \
           f"has been successfully added"


@input_error
def change(*args) -> str:
    """
    Method that changes user contacts in the dictionary if such user exists in the
    dictionary.
    :param args: Username and phone that should be stored.
    :return: The string with information about changing data in the dictionary.
    """
    rec_id = args[0]
    rec_value = args[1]
    old_rec_value = records[rec_id]
    records[rec_id] = rec_value
    return f"The phone number has been successfully changed for contact with name " \
           f"'{rec_id}' from '{old_rec_value}' to '{rec_value}'"


@input_error
def phone(*args) -> str:
    """
    Method that returns phone number by passed username.
    :param args: Username whose phone number should be shown.
    :return: The string with user's phone number.
    """
    rec_id = args[0]
    return f"The phone number for the client with name '{rec_id}' is '{records[rec_id]}'"


@input_error
def show_all() -> str:
    """
    Method that shows all users's phone numbers.
    :return: String with all phone numbers of all users.
    """
    return f"Clients phone numbers are: {records}"


@input_error
def good_bye() -> str:
    """
    Method that returns "Good bye!" string.
    :return: "Good bye!" string.
    """
    return "Good bye!"


@input_error
def unknown() -> str:
    """
    Method can be called when was typed a command that can't be recognised.
    :return: String with the explanation that was typed incorrect command.
    """
    return "Unknown command. Try again."


COMMANDS = {
    "hello": hello,
    "add": add,
    "change": change,
    "phone": phone,
    "show all": show_all,
    "good bye": good_bye,
    "close": good_bye,
    "exit": good_bye
}


def main() -> None:
    """
    Method is responsible for creating an endless loop where all additional function is
    calling. The loop can be stopped by passing the appropriate commands (close, exit,
    good bye).
    :return: None.
    """
    while True:
        cli_input = input("Type a command>>> ")
        func_name, func, func_args = parse_cli_command(cli_input)
        print(func(*func_args))
        if func_name in ("good bye", "close", "exit"):
            break


if __name__ == "__main__":
    main()
