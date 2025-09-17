import pandas as pd
import sqlite3
import config

def load_sql_file(file_path):
    """
    Wczytanie skryptu SQL z pliku.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        sql_script = file.read()
    return sql_script

def execute_sql_script(sql_script):
    """
    Wykonanie skryptu SQL w bazie danych w pamięci.
    """
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    try:
        cursor.executescript(sql_script)
    except sqlite3.OperationalError as e:
        print("Błąd SQL:", e)
        print("Fragment skryptu:", sql_script[:200])  # pokaż początek skryptu
        conn.close()
        return None
    return conn
# ...existing code...

def who_have_raise(conn):
    """
    Wyświetla tylko pracowników, którzy dostaną podwyżkę (stawka > 10.00).
    """
    if conn:
        query = """
        SELECT CONCAT(`Imię Pracownika`, " ", `Nazwisko Pracownika`) AS `Pracownik`, `Stawka za godzine`
        FROM Pracownicy
        WHERE `Stawka za godzine` > 10.00
        """
        df = pd.read_sql_query(query, conn)
        print("Pracownicy z podwyżką:")
        print(df)
        return df
    else:
        print("Brak połączenia z bazą danych.")
        return None

def main():
    sql_script = load_sql_file("databases/restauracja.sql")
    conn = execute_sql_script(sql_script)
    who_have_raise(conn)

if __name__=="__main__":
    main()
