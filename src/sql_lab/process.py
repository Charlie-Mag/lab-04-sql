import logging
import os

import mysql.connector
import pandas as pd


logging.basicConfig(level=logging.INFO)

DBHOST = os.environ.get("DBHOST")
DBNAME = os.environ.get("DBNAME")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")


def read_data(filename):
    """Read the CSV file into a pandas DataFrame."""
    logging.info("Reading the CSV file")
    data = pd.read_csv(filename)
    return data


def clean_data(data):
    """Clean the DataFrame before uploading it."""
    logging.info("Cleaning the data")

    # Remove rows with missing values.
    cleaned_data = data.dropna()

    # Make sure id is an integer.
    cleaned_data["id"] = cleaned_data["id"].astype(int)

    return cleaned_data


def load_data(data, table):
    """Create the MySQL table and upload the DataFrame."""
    logging.info("Loading data into MySQL")

    if table != "mock":
        raise ValueError("Table name must be mock")

    try:
        db = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME,
        )

        cursor = db.cursor()

        # Recreate the table so it matches this script.
        cursor.execute("DROP TABLE IF EXISTS mock")

        # Create the table if it does not exist.
        create_table = """
        CREATE TABLE IF NOT EXISTS mock (
            id BIGINT PRIMARY KEY,
            `group` VARCHAR(255),
            last_name VARCHAR(255),
            email VARCHAR(255),
            gender VARCHAR(255),
            ip_address VARCHAR(255)
        )
        """
        cursor.execute(create_table)

        # Insert each row using placeholders.
        insert_query = """
        INSERT INTO mock
        (id, `group`, last_name, email, gender, ip_address)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        for index, row in data.iterrows():
            values = (
                row["id"],
                row["group"],
                row["last_name"],
                row["email"],
                row["gender"],
                row["ip_address"],
            )
            cursor.execute(insert_query, values)

        db.commit()
        logging.info("Data uploaded successfully")

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)

    finally:
        cursor.close()
        db.close()
        logging.info("Database connection closed")


def main():
    """Run the full process."""
    data = read_data("MOCK_DATA.csv")
    cleaned_data = clean_data(data)
    load_data(cleaned_data, "mock")


if __name__ == "__main__":
    main()