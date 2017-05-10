import sys
import os
import ui
import queries
import psycopg2


def connection():
    try:
        # setup connection string
        connect_str = "dbname='andreakanya' user='andreakanya' host='' password='misamaci79'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # set autocommit option, to do every query when we call it
        conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        return conn
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)


def choose():
    inputs = ui.get_inputs(["Please enter a number: "])
    option = inputs[0]
    if option == "1":
        queries.get_firstname_lastname_mentors()
    elif option == "2":
        queries.get_nickname_mentor_miskolc()
    elif option == "3":
        queries.get_data_carol()
    elif option == "4":
        queries.get_data_unkowngirl()
    elif option == "5":
        queries.add_new_applicant()
    elif option == "6":
        queries.change_phonenumber()
    elif option == "7":
        queries.delete_by_domain()
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
               "Delete by domain"]
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
