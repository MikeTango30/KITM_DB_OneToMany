import database.db_conn


class rockband:

    def __init__(self, rockband_id, album_id, rockband_title):
        self.rockband_id = rockband_id
        self.album_id = album_id
        self.rockband_title = rockband_title

    def create_rockband(self):
        query = "INSERT INTO rockbands VALUES(?, ?, ?)"
        params = (None, self.album_id, self.rockband_title)
        self.execute_query(query, params)

    # def get_record_id(self, human_id):
    #     query = "SELECT heart_id FROM hearts WHERE human_id = (?)"
    #     params = (human_id,)
    #     return self.execute_query(query, params, True)
    #
    # def update_record_(self, field, value):
    #     query = "UPDATE hearts SET " + field + " = (?) WHERE heart_id = (?)"
    #     params = (value, self.heart_id)
    #     self.execute_query(query, params)