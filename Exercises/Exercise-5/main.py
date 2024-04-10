import psycopg2
import configparser


def main():
    # Initialize a connection to the Postgres database
    parser = configparser.ConfigParser()
    parser.read("config.conf")
    host = parser.get("postgres_config", "hostname")
    database = parser.get("postgres_config", "database")
    user = parser.get("postgres_config", "username")
    password = parser.get("postgres_config", "password")
    port = parser.get("postgres_config", "port")

    conn = psycopg2.connect(host=host, 
                            database=database, 
                            user=user, 
                            password=password,
                            port=port)
    

    def execute_ddl_sql(db_conn: psycopg2.connect, script_file: str):
        # Create cursor for future execution
        cursor = db_conn.cursor()
        # Get ddl script from file
        sql_file = open(script_file, 'r')
        # Execute ddl script
        cursor.execute(sql_file.read())




if __name__ == "__main__":
    main()
