import psycopg2

def get_connection():
        return psycopg2.connect(
                dbname = "Steel_Project",
                user = "auditor_user",
                password = "auditor123",
                host = "localhost"
        )