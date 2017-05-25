import ui
import config
import psycopg2


def print_out_data(cursor):
    # Fetch the result of the last execution
    rows = cursor.fetchall()  # list of tuples
    table = [list(item) for item in rows]  # list of list
    column_names = [i[0] for i in cursor.description]
    table.insert(0, column_names)
    ui.print_table(table)


def fetch_data(cursor):
    rows = list(cursor.fetchall())
    # rows.insert(0, [row[0] for row in cursor.description])
    return rows


def get_firstname_lastname_mentors(cursor):
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    print_out_data(cursor)


def get_nickname_mentor_miskolc(cursor):
    cursor.execute(""" SELECT nick_name FROM mentors
                        WHERE city = 'Miskolc';""")
    print_out_data(cursor)


def get_data_carol(cursor):
    cursor.execute(""" SELECT concat(first_name, ' ', last_name) AS full_name, phone_number FROM applicants
                        WHERE first_name = 'Carol';""")
    print_out_data(cursor)


def get_data_unkowngirl(cursor):
    cursor.execute(""" SELECT concat(first_name, ' ', last_name) AS full_name, phone_number FROM applicants
                        WHERE email LIKE '%@adipiscingenimmi.edu';""")
    print_out_data(cursor)


def add_new_applicant(cursor):
    try:
        cursor.execute(""" INSERT INTO applicants (id, first_name, last_name, phone_number, email, application_code)
                            VALUES (11, 'Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823)
                            ;""")
        cursor.execute(""" SELECT * FROM applicants
                            WHERE application_code = 54823 ;""")
        print_out_data(cursor)
    except psycopg2.IntegrityError:
        print("Information already exists.")


def change_phonenumber(cursor):
    cursor.execute(""" UPDATE applicants
                        SET phone_number = '003670/223-7459'
                        WHERE first_name = 'Jemima' AND last_name = 'Foreman';""")
    cursor.execute(""" SELECT phone_number FROM applicants
                        WHERE first_name = 'Jemima' AND last_name = 'Foreman';""")
    print_out_data(cursor)


def delete_by_domain(cursor):
    try:
        cursor.execute("""DELETE FROM applicants
                        WHERE email LIKE '%@mauriseu.net';""")
        cursor.execute("""SELECT * FROM applicants ORDER BY id;""")
        print_out_data(cursor)
    except psycopg2.IntegrityError:
            print("Information already deleted.")


def all_data_database(cursor):
    database = ["Please enter a database for search: "]
    data_list = ui.get_inputs(database)
    data = ''.join(data_list)
    cursor.execute("""SELECT * FROM %s 
                    ORDER BY id;""" % data)
    print_out_data(cursor)


def select_data_database(cursor):
    attribute = ["Please enter an attribute for search: "]
    database = ["Please enter a database for search: "]
    data_in_list1 = ui.get_inputs(attribute)
    data_in_list2 = ui.get_inputs(database)
    data1 = ''.join(data_in_list1)
    data2 = ''.join(data_in_list2)
    cursor.execute("""SELECT {} FROM {}
                    ORDER BY id;""" .format(data1, data2))
    print_out_data(cursor)



