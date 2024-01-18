#!/usr/bin/python3
"""Task 0 Module"""


def number_of_subscribers(subreddit):
    """Makes a query to the reddit api then return an object that shows
    number of users"""
    import requests

    sub_info = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False,
    )
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
