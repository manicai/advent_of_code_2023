# How it might be nice to work

    aoc init

Create a directory for today with template files. Download input and problem page. Open problem page in browser.

    aoc init <day> <year>

Do above for specific date.

    aoc run

Run current unsolved part. Offer to submit if a value comes out.

    aoc test

Run pytest on current part.

    aoc run <day> <year>
    aoc run -p <part> -d <day> -y <year>
    aoc test <day> <year>

If we submit and get the answer right redownload the puzzle page.

    aoc try

Run against the test code, don't offer to submit.

    aoc run <file>
    aoc try <file>

Run against a specific file.

- Support languages other that Python: `aoc init --lang=rust`
- Support multiple auth cookies.
- Auto Git commit, push on success.
- Configuration file.
- Run arbitrary script in todays directory `aoc exec black *.py`
