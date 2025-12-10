from openpyxl import load_workbook
import sqlite3

def import_excel(path):
    con = sqlite3.connect("contacts.db")
    cur = con.cursor()

    wb = load_workbook(path)
    ws = wb.active

    first = True
    for row in ws.iter_rows(values_only=True):
        if first:
            first = False
            continue

        cid, name, star, type_, value = row

        cur.execute("INSERT INTO contacts(id,name,is_starred) VALUES (?,?,?)", (cid, name, star))
        cur.execute("INSERT INTO contact_methods(contact_id,method_type,method_value) VALUES (?,?,?)",
                    (cid, type_, value))

    con.commit()
    con.close()
