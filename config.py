import pandas as pd
import sqlite3


def config():
    """
    Konfiguracja ustawień programu, który będzie analizowł bazę danych w restaurcji.
    Domyślnie baza danych będzie zapisywana w pliku 'reestauracja.db.
    Jeżeli plik już istnieje, to zostanie on nadpisany.

    Zwraca:
        dict: Słownik z ustawieniami konfiguracyjnymi.

    !UWAGA! baza danych przedstawia fikcyjną restauracje, klientów i pracowników.

    """ 

    config_settings = {
        "db_file_name": "restauracja.db",  # Nazwa pliku bazy danych
        "overwrite_db": True,              # Czy nadpisać istniejącą bazę danych
        "sql_file_path": "databases/restauracja.sql"  # Ścieżka do pliku SQL z definicją bazy danych
    }

    return config_settings

def load_sql_file(file_path):
    """
    Wczytanie skryptu SQL z pliku.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Błąd wczytywania pliku SQL: {e}")
        return None
    
def execute_sql_script(sql_scrip, db_path):
    """
    Wykonywanie skryptu SQL w bazie dnaych SQLite.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.executescript(sql_scrip)
        conn.commit()
        return conn
    except sqlite3.Error as e:
        print(f"Błąd wykonywania skryptu SQL: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
def main():
    #Wczytanie konfiguracji
    config_settings = config()
    db_file_name = config_settings["db_file_name"]
    overwrite_db = config_settings["overwrite_db"]
    sql_file_path = config_settings["sql_file_path"]
