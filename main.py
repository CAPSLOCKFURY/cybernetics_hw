from commands.commands import *

command_map: [int, AbstractCommand] = {
    1: LoginCommand(),
    2: RegisterCommand(),
}


def get_list_of_options_for_non_logged_in():
    return """List of commands, enter number to execute:
    1: Login 
    2: Register
    -1: Exit
    """


def get_list_of_options_for_logged_in():
    return """List of commands, enter number to execute:
    -1: Exit
    """


if __name__ == "__main__":
    while True:
        if SessionHolder.get_current_user() is None:
            print(get_list_of_options_for_non_logged_in())
        else:
            print(get_list_of_options_for_logged_in())
        option = int(input())
        if option == -1:
            break
        command_map[option].execute()
