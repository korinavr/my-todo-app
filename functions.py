FILEPATH= 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items."""
    # docstrings are the explanation of the function
    # use help() function to print the docstring
    with open(filepath) as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do item list in a text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == '__main__':
    print('Hello')
# we use this when we want to include some code into a module,
# and we don't want that to be executed when we import this module
# into another script.

# __name__ for this script == '__main__' when we run the script
# directly, but when we import the module into another script
# __name__ == 'functions' (here is the name of the file)