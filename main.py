import sys
import os
import ui
import queries
import psycopg2
import config


def choose():
    inputs = ui.get_inputs(["Please enter a number: "])
    option = inputs[0]
    if option == "1":
        queries.get_firstname_lastname_mentors(config.connection())
    elif option == "2":
        queries.get_nickname_mentor_miskolc(config.connection())
    elif option == "3":
        queries.get_data_carol(config.connection())
    elif option == "4":
        queries.get_data_unkowngirl(config.connection())
    elif option == "5":
        queries.add_new_applicant(config.connection())
    elif option == "6":
        queries.change_phonenumber(config.connection())
    elif option == "7":
        queries.delete_by_domain(config.connection())
    elif option == "8":
        queries.all_data_database(config.connection())
    elif option == "9":
        queries.select_data_database(config.connection())
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Get the first and last name of mentors",
               "Get the nickname of Miskolc's mentor(s)",
               "Get data from Carol",
               "Get data from the unknown girl by her e-mail address",
               "Add the new applicants",
               "Change pnone number(s)",
               "Delete by domain",
               "General querie: Select all data from table",
               "General querie: Select data from table (attributes shuold separate by comma and sapce)"]
    ui.print_menu("Main menu", options, "Exit program")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(err)


if __name__ == '__main__':
    main()
