import sqlite3
import os

db = os.path.join(os.path.dirname(__file__), '..', 'db.sqlite3')
conn = sqlite3.connect(db)
cur = conn.cursor()
try:
    cur.execute("SELECT id, nombreproyecto, link, tipo_video, tipo_video_vertical FROM Girekstudio_proyecto LIMIT 50")
    rows = cur.fetchall()
    if not rows:
        print('No rows found in Girekstudio_proyecto')
    else:
        print('id | nombreproyecto | link | tipo_video | tipo_video_vertical')
        for r in rows:
            print('|'.join(str(x) if x is not None else '' for x in r))
except Exception as e:
    print('Error querying DB:', e)
finally:
    conn.close()

