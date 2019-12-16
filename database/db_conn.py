import sqlite3

def execute_query(self, query, params, select=None):
    try:
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()

        if select is not None:
            record_id = cursor.execute(query, params).fetchone()[0]
            return record_id

        cursor.execute(query, params)
        connection.commit()
    except sqlite3.DatabaseError as error:
        print(error)
    finally:
        # noinspection PyUnboundLocalVariable
        cursor.close()
        # noinspection PyUnboundLocalVariable
        connection.close()