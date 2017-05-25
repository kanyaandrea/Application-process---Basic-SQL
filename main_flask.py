from flask import Flask, render_template, request, redirect, url_for
import config
import queries
from queries import fetch_data, fetch_data_title


app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html", title="Homepage")


@app.route("/mentors")
def get_mentors():
    mentors = fetch_data(queries.select_mentors(config.connection()))
    mentors_title = fetch_data_title(queries.select_mentors(config.connection()))
    return render_template("general.html", table=mentors, tabletitle=mentors_title, title="Mentors with school location")


@app.route("/all-school")
def get_all_school():
    schools = fetch_data(queries.select_schools(config.connection()))
    schools_title = fetch_data_title(queries.select_schools(config.connection()))
    return render_template("general.html", table=schools, tabletitle=schools_title,
                            title="All school - with available mentors there")


@app.route("/mentors-by-country")
def get_mentors_by_country():
    mentors_count = fetch_data(queries.count_mentors(config.connection()))
    mentors_count_title = fetch_data_title(queries.count_mentors(config.connection()))
    return render_template("general.html", table=mentors_count, tabletitle=mentors_count_title,
                            title="Number of mentors by country")


@app.route("/contacts")
def get_contacts():
    contacts = fetch_data(queries.select_contacts(config.connection()))
    contacts_title = fetch_data_title(queries.select_contacts(config.connection()))
    return render_template("general.html", table=contacts, tabletitle=contacts_title,
    title="Schools with contact persons")


@app.route("/applicants")
def get_applicants():
    applicants = fetch_data(queries.select_applicants(config.connection()))
    applicants_title = fetch_data_title(queries.select_applicants(config.connection()))
    return render_template("general.html", table=applicants, tabletitle=applicants_title, title="Applicants")


@app.route("/applicants-and-mentors")
def get_applicants_and_mentors():
    applicants_mentors = fetch_data(queries.select_applicants_with_mentors(config.connection()))
    applicants_mentors_title = fetch_data_title(queries.select_applicants_with_mentors(config.connection()))
    return render_template("general.html", table=applicants_mentors, tabletitle=applicants_mentors_title,
                            title="Applicants with assigned mentors")


if __name__ == "__main__":
    app.run(debug=None)

