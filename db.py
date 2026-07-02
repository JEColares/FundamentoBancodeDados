import psycopg2

def get_connection():
        return psycopg2.connect(
                dbname = "Stell_Project",
                user = "postgres",
                password = "postgres",
                host = "localhost"
        )