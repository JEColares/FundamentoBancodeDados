import psycopg2

def get_connection():
        return psycopg2.connect(
                dbname = "Steel_Project",
                user = "postgres",
                password = "postgres",
                host = "localhost"
        )