import os

import aoc
import bs4
import requests


def is_complete(problem_file):
    if not problem_file.is_file():
        print(f"Don't have file {problem_file}")
        return False

    with open(problem_file, "r") as fh:
        soup = bs4.BeautifulSoup(fh, features="html.parser")

    if soup.find_all(class_="day-success"):
        print(f"Day completed: {problem_file}")
        return True

    print(f"Day not completed: {problem_file}")
    return False


def download_problem(day=aoc.today(), year=aoc.year()):
    problem_url = f"https://adventofcode.com/{year}/day/{day}"
    problem_file = aoc.inputs_dir(day) / "problem.html"

    if not is_complete(problem_file):
        print(f"Downloading from {problem_url}")
        session_cookie = os.environ["AOC_COOKIE"]
        cookies = {"session": session_cookie}
        response = requests.get(problem_url, cookies=cookies)
        if not response.status_code == 200:
            print(
                f"Failed to get problem statement for day {day} ({response.status_code}):",
                response.text,
            )
        else:
            with open(problem_file, "w", encoding=response.encoding) as fh:
                fh.write(response.text)


def run_script():
    today = aoc.today()
    for day in range(1, today + 1):
        download_problem(day)


if __name__ == "__main__":
    run_script()
