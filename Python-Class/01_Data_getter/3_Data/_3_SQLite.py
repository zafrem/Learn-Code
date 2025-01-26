import _0_Coin_Data_getter as coin_data
import sqlite3
import time

db_name = "example.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()


def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS coin (
            dt DATETIME PRIMARY KEY default current_timestamp,
            current_info INTEGER,
            change_point INTEGER
        )
    ''')
    print("Table created successfully.")


def insert_data(curr_point, changed_point):
    cursor.execute('''
        INSERT INTO coin (current_info, change_point) 
        VALUES (?, ?)
    ''', (curr_point, changed_point))
    conn.commit()
    print(f"Inserted {curr_point}, {changed_point} into the table.")


def read_all_data():
    cursor.execute('SELECT * FROM coin')
    rows = cursor.fetchall()
    print("\nFetched Data:")
    for row in rows:
        print(row)


def close_connection():
    conn.close()
    print("\nDatabase connection closed.")


if __name__ == "__main__":
    coin_name = "BTCUSDC"
    create_table()  # Create the table

    current_info = 0.0
    past_info = 0.0
    _persent = 0.0
    while True:
        time.sleep(5)#60 * 60 * 24)  # Daily

        past_info = current_info
        current_info = coin_data.get_altcoin_current_price(coin_name)
        if 0.0 != past_info:
            _persent = (past_info - current_info) / current_info * 100

        # Insert sample data
        insert_data(current_info, _persent)
        # Fetch and display the data
        read_all_data()

        # Add your own abort conditions.

    close_connection()
