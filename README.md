# Advent of Code 2023

My repository of answers for Advent of Code 2023

## Retrospective

That was fun. My first time doing Advent of Code. Most of the problems were fine. I'm not going to go through them all.

Day 5: First puzzle that gave me pause for thought on part 2. The visualisations of the ranges splitting up and being mapped to different location that appear on [Reddit](https://www.reddit.com/r/adventofcode) weren't hard to envisage. But it took a bit of time to think about the best way of representing them in the code and how to split them up as they went through the functions.

Day 8: The first day (to my recollection) that really invited brute force but made it absolutely impossible. Finding the lowest common multiple of cycle lengths would come up again later.

Day 10: The [Pipemania](https://en.wikipedia.org/wiki/Pipe_Mania) puzzle. This was a lot of fun. I'm not sure I had a best solution to part two, my method for this was flood fill and I handled the squeezing through adjacent elements by expanding each grid element to a 3x3 grid of elements to make the gaps easier to compute.

Day 12: The first day I got stuck on for a while. I should have remembered my DNA sequence matching algorithms and used dynamic programming. I went instead with chopping the puzzle in two around one of the groups of broken springs, working out the possibilities for that set and what would happen in the smaller sub puzzles either side of it (probably not a good analogy but a little like Quicksort). Initially I split on the largest groups (as they should be the most constrained) picking the first if there was a tie but on test cases with lots of equally sized small groups this was way too slow as it wasn't really shrinking the subproblems significantly (one line took seven hours - and then I found I had a bug). I reimplemented splitting on the middle group and it was much much faster. First time I really went onto Reddit afterwards to see what others had been up to.

Day 17: Knocking rust off my theory knowledge to implement path finding.

Day 18: I'll flood fill again ... oh, ... no, that won't work. I didn't know the [Shoelace Formula](https://en.wikipedia.org/wiki/Shoelace_formula) before so this was the first day I had to learn something explicitly new to solve it.

Day 19: Ah, operations on ranges again. A lot easier after getting my head round this for day 5.

Day 20: Another "avoid brute force by using lowest common multiple" day, again aided by having seen this earlier.

Day 21: I wasted so much time on this. I found the puzzle slightly unsatisfying because my solution was so dependent on the special form of the input and wouldn't work on the example data in description. I spent ages trying to cut the grid up and piece back together with off by one errors before realising that it was utterly unnecessary and I could just use the answer from part 1 to do most of the work for me, at which point I threw away lots of work and solved it relatively quickly.

Day 22: Tetris block stacks, fun.

Day 24: I get the impression from Reddit this may become infamous. It certainly took me the longest. I got the simultaneous non-linear equations quickly enough but wasn't sure how to solve them. After trying to think of analytical or clever algorithms for too long I just decided to brute force by assuming y and z velocities were roughly the same as the hailstones and solving for everything else (the range of x values was in the input was larger). Using symbolic solvers never occurred to me, nor did the cleverer cross product trick (change of reference frame) to make the equations more manageable. I'm pleased I found a simple Python solution rather than having to resorted to specialist maths tools with Sympy, Mathematica or Z3.

Day 25: I cheated ;-). I know there are algorithms to find the wires to cut but it was Christmas day so I didn't want to spend much time on it. I dumped the network into Graphviz and manually looked at the resulting image to find the wires to cut. Then I wrote code to work out the partition sizes with those wires excluded. Since then I've gone back and implemented it fully programmatically, first by writing Karger's algorithm, then after looking at Reddit using the NetworkX library implementation of the Stoer–Wagner algorithm which makes it completely (boringly) trivial.


## The Code

How the scripts are run evolved over the course of the month so there's no immediate "here's how to run stuff" but all them are short and which means they shouldn't been too hard understand.

Some general notes:

- Utility code is in `aoc`, this is both stuff that seemed like it was (or might be) repeatedly useful and some library stuff for the bootstrap script.

- `init_day.py` was a daily bootstrap script. It'll only work during the month so don't expect it to be useful without editting. It creates template solution files, test files for them, downloads the days input and Part1 problem statement trying to pull out test examples from that. It doesn't know about Part 2 or submissions. It caches the web requests to save the AoC website. It probably won't work unmodified in 2024 ...

- The later scripts expect the days input to be in a folder `inputs/day_XX` because that's where the bootstrapper puts it along with the problem text. Those files aren't here because everyone gets their own and AoC explicitly ask that [they are not distributed](https://adventofcode.com/2023/about#faq_copying). (You'll find a private submodule that I used for my caching this for my reference.)

- The framework stuff expects various stuff to be in environment. I use Poetry to read it in from a `.env` file. That's machine and person specific so not here either, a not guaranteed to be exhaustive list of stuff in it is
  + `AOC_COOKIE`: your personal session cookie from the AOC website for getting inputs.
  + `AOC_ROOT`: location you've checked this code out to.
  + `PYTHONPATH`: including at the minimum `$AOC_ROOT` for install paths.

- These were written to solve the problems reasonably quickly. I wasn't going for the leader board but I didn't have a lot of spare time either. Don't expect beautiful production code with 100% unit test coverage and carefully considered comments. Most of the scripts are less than 100 lines and only have to work once :-).
