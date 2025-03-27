import requests
import sqlite3
import csv
from bs4 import BeautifulSoup

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        company TEXT,
        location TEXT,
        description TEXT,
        application_link TEXT,
        UNIQUE(title, company, location)
    )
""")
conn.commit()

url = "https://realpython.github.io/fake-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

job_listings = soup.find_all("div", class_="card-content")

for job in job_listings:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()

    description_tag = job.find("div", class_="content")
    description = description_tag.text.strip() if description_tag else "No description available"

    link_tag = job.find("a", string="Apply")
    application_link = link_tag["href"] if link_tag else "No application link"

    cursor.execute("""
        INSERT INTO jobs (title, company, location, description, application_link)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(title, company, location) 
        DO UPDATE SET description=excluded.description, application_link=excluded.application_link
    """, (title, company, location, description, application_link))

conn.commit()
print("Job listings updated successfully!")


def filter_jobs(location=None, company=None):
    query = "SELECT * FROM jobs WHERE 1=1"
    params = []
    if location:
        query += " AND location = ?"
        params.append(location)
    if company:
        query += " AND company = ?"
        params.append(company)

    cursor.execute(query, params)
    return cursor.fetchall()


def export_to_csv(filename="filtered_jobs.csv", location=None, company=None):
    jobs = filter_jobs(location, company)
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Location", "Description", "Application Link"])
        writer.writerows(jobs)
    print(f"Jobs exported to {filename}")


conn.close()
