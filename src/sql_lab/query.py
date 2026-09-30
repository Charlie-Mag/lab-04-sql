import logging
import os

import mysql.connector


logging.basicConfig(level=logging.INFO)

DBHOST = os.environ.get("DBHOST")
DBNAME = os.environ.get("DBNAME")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")


def get_data_by_group(value):
    """Return rows where the `group` column equals the given value."""
    logging.info("Getting data by group")

    db = mysql.connector.connect(
        host=DBHOST,
        user=DBUSER,
        password=DBPASS,
        database=DBNAME,
    )

    cursor = db.cursor(dictionary=True)

    # Use backticks because group is a SQL keyword.
    query = "SELECT * FROM mock WHERE `group` = %s"
    cursor.execute(query, (value,))

    results = cursor.fetchall()

    cursor.close()
    db.close()

    return results


def plot_counts(groupby):
    """Count rows in the mock table grouped by the selected column."""
    logging.info("Counting rows by column")

    allowed_columns = ["group", "last_name", "email", "gender", "ip_address"]

    if groupby not in allowed_columns:
        raise ValueError("Column is not allowed")

    db = mysql.connector.connect(
        host=DBHOST,
        user=DBUSER,
        password=DBPASS,
        database=DBNAME,
    )

    cursor = db.cursor(dictionary=True)

    # Check allowed_columns before using the column name in the query.
    query = f"SELECT `{groupby}`, COUNT(*) AS count FROM mock GROUP BY `{groupby}`"
    cursor.execute(query)

    results = cursor.fetchall()

    cursor.close()
    db.close()

    return results


def main():
    """Run example queries against the mock table."""
    group_rows = get_data_by_group("basketball")
    print("First rows where group is basketball:")
    print(group_rows[:5])

    counts = plot_counts("group")
    print("Counts by group:")
    print(counts)


if __name__ == "__main__":
    main()