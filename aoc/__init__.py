import datetime
import os
import pathlib as path
import sys

import requests


def year():
    return datetime.datetime.now().year


def today():
    return datetime.datetime.now().day


def download_input(day=today(), year=year()):
    if os.path.exists(cached_input(day)):
        print("Input data already cached, no download required")
        return

    session_cookie = os.environ["AOC_COOKIE"]
    cookies = {"session": session_cookie}
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    print("Fetching data from", url)
    response = requests.get(url, cookies=cookies)
    assert (
        response.status_code == 200
    ), f"Got error {response.status_code}: {response.text}"
    with open(cached_input(day), "w", encoding="ascii") as fh:
        fh.write(response.text)


def inputs_dir(day=today()):
    root = path.Path(os.environ["AOC_ROOT"])
    return root / f"inputs/day_{day:02}"


def cached_input(day=today()):
    return inputs_dir(day) / "input.txt"


def run_script(func, day=today()):
    test_mode = "-t" in sys.argv
    if test_mode:
        # Look for plausible test file names.
        for candidate in ["test.txt", "test_0.txt", "test_1.txt"]:
            input_file = path.Path(candidate)
            if input_file.is_file():
                break
    elif len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        download_input(day)
        input_file = cached_input(day)

    print(f"Reading from {input_file}")
    with open(input_file, "r", encoding="ascii") as fh:
        lines = [line.strip() for line in fh.readlines()]

    return func(lines)
