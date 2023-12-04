import datetime
import os
import sys

import requests


def download_input():
    if os.path.exists(cached_input()):
        print("No download required")
        return

    session_cookie = os.environ["AOC_COOKIE"]
    cookies = {"session": session_cookie}
    url = f"https://adventofcode.com/{year()}/day/{today()}/input"
    print(url)
    response = requests.get(url, cookies=cookies)
    assert (
        response.status_code == 200
    ), f"Got error {response.status_code}: {response.text}"
    with open(cached_input(), "w", encoding="ascii") as fh:
        fh.write(response.text)


def year():
    return datetime.datetime.now().year


def today():
    return datetime.datetime.now().day


def cached_input():
    return f"../inputs/day_{today():02}/input.txt"


def run_script(func):
    test_mode = "-t" in sys.argv
    if test_mode:
        input_file = "test.txt"
    elif len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        download_input()
        input_file = cached_input()

    print(f"Reading from {input_file}")
    with open(input_file, "r", encoding="ascii") as fh:
        lines = [l.strip() for l in fh.readlines()]

    func(lines)
