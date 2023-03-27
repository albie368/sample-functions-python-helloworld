import sqlite3, time

def main(args):
    query = "DELETE FROM user WHERE timestamp >= 7200"
    con = sqlite3.connect("main")
    cur = con.cursor()
    cur.execute(query)
    con.close()

