from flask import Flask, render_template, request, redirect
import sqlite3
from utils.excel_export import export_excel
from utils.excel_import import import_excel

app = Flask(__name__)

def db():
    return sqlite3.connect('contacts.db')

@app.route("/")
def index():
    con = db()
    cur = con.cursor()
    cur.execute("SELECT * FROM contacts ORDER BY is_starred DESC, name ASC")
    contacts = cur.fetchall()
    con.close()
    return render_template("index.html", contacts=contacts)

@app.route("/add", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        name = request.form["name"]
        con = db()
        cur = con.cursor()
        cur.execute("INSERT INTO contacts(name) VALUES (?)", (name,))
        con.commit()
        con.close()
        return redirect("/")
    return render_template("add_contact.html")

@app.route("/star/<int:id>")
def star(id):
    con = db()
    cur = con.cursor()
    cur.execute("UPDATE contacts SET is_starred = 1 - is_starred WHERE id=?", (id,))
    con.commit()
    con.close()
    return redirect("/")

@app.route("/export")
def export():
    export_excel()
    return "Exported to export.xlsx"

@app.route("/import", methods=["POST"])
def import_file():
    file = request.files["file"]
    file.save("import.xlsx")
    import_excel("import.xlsx")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
