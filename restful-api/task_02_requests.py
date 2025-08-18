#!/usr/bin/python3

import requests
import csv



def fetch_and_print_posts():
    rr = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = rr.json()
    print(f"Status Code: {rr.status_code}")
    for i in data:
        print(i["title"])


def fetch_and_save_posts():
    rr = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = rr.json()
    Fdata = [{k:v for k,v in x.items() if k != 'userId'} for x in data]
    if rr.status_code >= 200 and rr.status_code < 300:
        fieldnames = Fdata[0].keys()
        
        with open("posts.csv", "w") as csvfile:
            print(fieldnames)
            writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(Fdata)

fetch_and_save_posts()