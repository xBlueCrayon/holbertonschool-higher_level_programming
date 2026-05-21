#!/usr/bin/python3
"""Module for consuming and processing API data."""

import requests
import csv


def fetch_and_print_posts():
    """Fetch and print all post titles."""

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts and save them to a CSV file."""

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        data = []

        for post in posts:
            data.append({
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            })

        with open("posts.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=["id", "title", "body"]
            )

            writer.writeheader()
            writer.writerows(data)
