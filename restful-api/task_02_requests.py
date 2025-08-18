#!/usr/bin/python3

import requests
import csv

rr = requests.get("https://jsonplaceholder.typicode.com/posts")
data = rr.json()


def fetch_and_print_posts():
    print(f"Status Code: {rr.status_code}")
    for i in data:
        print(i["title"])


def fetch_and_save_posts():
    if rr.status_code >= 200 and rr.status_code < 300:
        fieldnames = data[0].keys()
        with open("posts.csv", "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
