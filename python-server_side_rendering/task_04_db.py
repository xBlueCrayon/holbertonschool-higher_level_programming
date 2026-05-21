#!/usr/bin/python3
"""Flask app displaying products from JSON, CSV, or SQLite."""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    """Read products from JSON file."""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception:
        return []


def read_csv():
    """Read products from CSV file."""
    products = []

    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                products.append(row)

    except Exception:
        return []

    return products


def read_sql():
    """Read products from SQLite database."""
    products = []

    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, name, category, price FROM Products"
        )

        rows = cursor.fetchall()

        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        conn.close()

    except Exception:
        return []

    return products


@app.route('/products')
def products():
    """Display products page."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    data = []

    if source == 'json':
        data = read_json()

    elif source == 'csv':
        data = read_csv()

    elif source == 'sql':
        data = read_sql()

    else:
        return render_template(
            'product_display.html',
            error="Wrong source"
        )

    if product_id:
        filtered = []

        for product in data:
            if str(product.get('id')) == str(product_id):
                filtered.append(product)

        data = filtered

        if not data:
            return render_template(
                'product_display.html',
                error="Product not found"
            )

    return render_template(
        'product_display.html',
        products=data
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
