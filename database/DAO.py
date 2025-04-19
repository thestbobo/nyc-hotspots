from database.DB_connect import DBConnect
from model.localita import Location

class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getAllProvider():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """
        SELECT DISTINCT (nwhl.Provider) 
        FROM nyc_wifi_hotspot_locations nwhl 
        """

        cursor.execute(query)

        for row in cursor:
            result.append(row["Provider"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getLocationProvider(provider):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """
            SELECT DISTINCT (nwhl.Location), avg(nwhl.Latitude) as avgLat,  avg(nwhl.Longitude) as avgLong
            FROM nyc_wifi_hotspot_locations nwhl 
            where nwhl.Provider = %s
            GROUP by nwhl.Location 
            """

        cursor.execute(query, (provider,))

        for row in cursor:
            result.append(Location(row["Location"], row["avgLat"], row["avgLong"], provider))

        cursor.close()
        conn.close()
        return result
