from terminaltables import AsciiTable


def print_table(table):
    table_items = []
    for item in table:
        table_items.append(item)
    table = AsciiTable(table_items)
    table.inner_heading_row_border = True
    table.inner_row_border = True
    print(table.table)


def print_menu(title, list_options, exit_message):
    print()
    print(title)
    print()
    menu_number = 1
    for options in list_options:
        print("(" + str(menu_number) + ")",  options)
        menu_number += 1
    print("(0)", exit_message)
    print()


def print_error_message(message):
    print("Error: %s" % message)


def get_inputs(list_labels):
    inputs = []

    for item in list_labels:
        input_required = True
        while input_required:
            user_input = input(str(item))
            if user_input != '':
                inputs.append(user_input)
                input_required = False
            else:
                print("Please enter a valid input")
                continue
    return inputs

