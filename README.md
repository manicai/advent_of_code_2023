My repository of answers for Advent of Code 2023

How the scripts are run evolved over the course of the month so there's no immediate "here's how to run stuff" but all them are short and which means they shouldn't been too hard understand. 

Some general notes:

- Utility code is in `aoc`, this is both stuff that seemed like it was (or might be) repeatedly useful and some library stuff for the bootstrap script.

- `init_day.py` was a daily bootstrap script. It'll only work during the month so don't expect it to be useful without editting. It creates template solution files, test files for them, downloads the days input and Part1 problem statement trying to pull out test examples from that. It doesn't know about Part 2 or submissions. It caches the web requests to save the AoC website. It probably won't work unmodified in 2024 ...

- The later scripts expect the days input to be in a folder `inputs/day_XX` because that's where the bootstrapper puts it along with the problem text. Those files aren't here because everyone gets their own and AoC explicitly ask that [they are not distributed](https://adventofcode.com/2023/about#faq_copying).

- The framework stuff expects various stuff to be in environment. I use Poetry to read it in from a `.env` file. That's machine and person specific so not here either, a not guaranteed to be exhaustive list of stuff in it is
  + `AOC_COOKIE`: your personal session cookie from the AOC website for getting inputs.
  + `AOC_ROOT`: location you've checked this code out to.
  + `PYTHONPATH`: including at the minimum `$AOC_ROOT` for install paths.

- These were written to solve the problems reasonably quickly. I wasn't going for the leader board but I didn't have a lot of spare time either. Don't expect beautiful production code with 100% unit test coverage and carefully considered comments. Most of the scripts are less than 100 lines and only have to work once :-). 
