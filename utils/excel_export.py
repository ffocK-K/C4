from openpyxl import Workbook
import sqlite3

def export_excel():
    con = sqlite3.connect("contacts.db")
    cur = con.cursor()

    wb = Workbook()
    ws = wb.active
    ws.append(["ID", "Name", "Starred", "Type", "Value"])

    cur.execute("""
        SELECT contacts.id, contacts.name, contacts.is_starred, contact_methods.method_type, contact_methods.method_value
        FROM contacts LEFT JOIN contact_methods 
        ON contacts.id = contact_methods.contact_id
    """)

    for row in cur.fetchall():
        ws.append(row)

    wb.save("export.xlsx")
    con.close()
