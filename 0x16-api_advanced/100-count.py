#!/usr/bin/python3
""" Module that counts """
from typing import Dict, List
from requests import get

REDDIT_URL = "https://www.reddit.com/"
HEADERS = {"User-Agent": "my-app/0.0.1"}


def count_words(subreddit: str, word_list: List[str], after: str = "") -> None:
    """
    Prints the count of specified words in the titles .
    """
    word_dic: Dict[str, int] = {word: 0 for word in word_list}

    if after is None:
        sorted_word_list = sorted(
            word_dic.items(), key=lambda x: (-x[1], x[0])
            )
        for w, count in sorted_word_list:
            if count:
                print(f"{w.lower()}: {count}")
        return None

    url = f"{REDDIT_URL}r/{subreddit}/hot/.json"
    params = {"limit": 100, "after": after}

    try:
        r = get(url, headers=HEADERS, params=params, allow_redirects=False)
        r.raise_for_status()
        js = r.json()

        data = js.get("data")
        after = data.get("after")
        children = data.get("children")

        for child in children:
            post = child.get("data")
            title = post.get("title")
            lower = [s.lower() for s in title.split(" ")]

            for w in word_list:
                word_dic[w] += lower.count(w.lower())

        count_words(subreddit, word_list, after)

    except (ValueError, KeyError) as e:
        print(f"Error processing JSON response: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


# Example usage:
# count_words("python", ["programming", "python", "reddit"])
