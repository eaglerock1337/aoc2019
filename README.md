# Advent of Code 2019

My personal attempt at the Advent of Code 2019 challenge.

www.adventofcode.com

www.adventofcode.com/2019

I am attempting to write this in Python with 100% test coverage, and not going for the fastest or simplest solution, but rather a robust solution I can test heavily against and learn PyTest while I practice my daily coding.

## Usage

Note that these solutions require Python 3.7 or later to run.

### Installation

The virtual environment is managed by pipenv. The scripts themselves do not have any dependencies besides the base Python install, but tests and formatting require the development plugins. All dependencies of this are managed by the pipenv:

```
$ sudo pip3 install pipenv
$ pipenv install -d
$ pipenv shell
(aoc2019) $
```

### Running Scripts

While the scripts don't strictly require the virtual environment to run (the only dependencies so far are for development and testing), scripts can be run by entering the pipenv shell or prefixing the command with `pipenv run`:

```
$ python3.7 day1/rocket.py
$ pipenv run python day1/rocket.py
$ pipenv shell
(aoc2019) $ python day1/rocket.py
(aoc2019) $ cd day1
(aoc2019) $ python rocket.py
```

Note that scripts can be run either in the root directory or in the directory for that day.

### Running Tests

Tests require the development dependencies, so ensure that `pipenv install -d` is run before running tests. Tests also check for coverage through the pytest-cov plugin.

While 100% test coverage has been achieved for these examples, it does exclude the `if __name__ == '__main__':` code block at the bottom of each file. A `.coveragerc` file has been provided to exclude this line and show 100% coverage, but this will not show if you run tests inside one of the day directories, only in the root of the repo.

```
(aoc2019) $ pytest
(aoc2019) $ pytest --cov=day3
(aoc2019) $ pytest --cov=.
(aoc2019) $ pytest --cov=. --cov-report term-missing -v
```

## Other Info

I'm using PyTest as my testing framework, and borrow some helpers from Mock. I use Black for code formatting, and have PyLint installed, but haven't been linting my code throughout the process. I might try to lint all of the code if I feel like it, but I doubt I'll get to it.

When challenges call upon earlier code (such as day 5 adding on to the intcode computer from day 2), I copy the existing code into the new folder and work from there, so each day has a fresh directory to work with. This will definitely screw up PyLint, so if I am going to actually lint my code, I'm going to have to ignore duplicate code between days.

Feel free use my code as inspiration for your own solutions, and feedback is welcomed! Thanks for viewing!
