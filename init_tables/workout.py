"""
TODO
"""

from psycopg2.extensions import cursor


def populate_workouts(cur: cursor, rows: list[dict[str, str]]):
    """
    TODO
    """
    for row in rows:
        workout = (row['title'], row['descrip'],row['type'], 
                 row['bodypart'], row['equipment'],row['level'], )
        cur.execute("""
            insert into workout(title, descrip, type, bodypart, equipment, level) 
            values(%s, %s, %s, %s, %s, %s) 
            on conflict do nothing
            """, workout)