import sqlite3

DB_PATH = "data/INFO.db"

def query_plate(plate_number):
    db = sqlite3.connect(DB_PATH)
    c = db.cursor()
    FIND = ("SELECT OWNER, CONTACT, MODEL FROM info WHERE PLATE=?")
    c.execute(FIND, (plate_number,))
    result = c.fetchall()
    db.close()
    return result
