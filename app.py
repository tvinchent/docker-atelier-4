import psycopg2

def connect_to_db():
    try:
        # Connexion à la base de données
        connection = psycopg2.connect(
            user="root",
            password="root",
            host="localhost",
            port="5432",
            database="exo4"
        )

        cursor = connection.cursor()
        
        # Exemple de requête
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"PostgreSQL version: {db_version}")
        
        # Exemple de création de table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        );
        """)
        connection.commit()

        print("Table 'users' créée avec succès.")
        
        # Exemple d'insertion de données
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("John Doe", "john@example.com"))
        connection.commit()
        print("Utilisateur inséré avec succès.")
        
        # Récupérer les données
        cursor.execute("SELECT * FROM users;")
        users = cursor.fetchall()
        print("Utilisateurs :", users)

    except (Exception, psycopg2.Error) as error:
        print("Erreur lors de la connexion à PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connexion PostgreSQL fermée.")


if __name__ == "__main__":
    connect_to_db()
