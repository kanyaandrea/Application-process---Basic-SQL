import ui
import main


def print_out_data(cursor):
    # Fetch the result of the last execution
    rows = cursor.fetchall()  # list of tuples
    table = [list(item) for item in rows]  # list of list
    column_names = [i[0] for i in cursor.description]
    table.insert(0, column_names)
    ui.print_table(table)


def get_firstname_lastname_mentors():
    cursor = main.connection().cursor()
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    print_out_data(cursor)


def get_nickname_mentor_miskolc():
    cursor = main.connection().cursor()
    cursor.execute(""" SELECT nick_name FROM mentors
                        WHERE city = 'Miskolc';""")
    print_out_data(cursor)


def get_data_carol():
    cursor = main.connection().cursor()
    cursor.execute(""" SELECT concat(first_name, ' ', last_name) AS full_name, phone_number FROM applicants
                        WHERE first_name = 'Carol';""")
    print_out_data(cursor)


def get_data_unkowngirl():
    cursor = main.connection().cursor()
    cursor.execute(""" SELECT concat(first_name, ' ', last_name) AS full_name, phone_number FROM applicants
                        WHERE email LIKE '%@adipiscingenimmi.edu';""")
    print_out_data(cursor)


def add_new_applicant():
    cursor = main.connection().cursor()
    cursor.execute(""" INSERT INTO applicants (id, first_name, last_name, phone_number, email, application_code)
                        VALUES (11, 'Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823)
                        ;""")
    cursor.execute(""" SELECT * FROM applicants
                        WHERE application_code = 54823 ;""")
    print_out_data(cursor)


def change_phonenumber():
    cursor = main.connection().cursor()
    cursor.execute(""" UPDATE applicants
                        SET phone_number = '003670/223-7459'
                        WHERE first_name = 'Jemima' AND last_name = 'Foreman';""")
    cursor.execute(""" SELECT phone_number FROM applicants
                        WHERE first_name = 'Jemima' AND last_name = 'Foreman';""")
    print_out_data(cursor)


def delete_by_domain():
    cursor = main.connection().cursor()
    cursor.execute("""DELETE FROM applicants
                    WHERE email LIKE '%@mauriseu.net';""")
    cursor.execute("""SELECT * FROM applicants ORDER BY id;""")
    print_out_data(cursor)


def all_data_mentors(database):
    database = ui.get_inputs(["Please enter a database: "])
    cursor = main.connection().cursor()
    cursor.execute("""SELECT * FROM %s 
                    ORDER BY id;""" % database)
    print_out_data(cursor)





