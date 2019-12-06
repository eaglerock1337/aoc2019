# Advent of Code 2019

My Personal Attempt at the Advent of Code 2019 challenge.

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

Scripts can be run by entering the pipenv shell or prefixing the command with `pipenv run`:

```
$ pipenv run python aoc1/rocket.py
$ pipenv shell
(aoc2019) $ python aoc1/rocket.py
(aoc2019) $ cd aoc1
(aoc2019) $ python rocket.py
```

Note that scripts can be run either in the root directory or in the directory for that day.

### Running tests

Tests require the development dependencies, so ensure that `pipenv install -d` is run before running tests. Tests also check for coverage through the pytest-cov plugin.

While 100% test coverage has been achieved for these examples, it does exclude the `if __name__ == '__main__':` code block at the bottom of each file. A `.coveragerc` file has been provided to exclude this line and show 100% coverage, but this will not show if you run tests inside one of the day directories, only in the root of the repo.

```
(aoc2019) $ pytest
(aoc2019) $ pytest --cov=day3
(aoc2019) $ pytest --cov=.
(aoc2019) $ pytest --cov=. --cov-report term-missing -v
```

Feel free use my code as inspiration for your own solutions, and feedback is welcomed! Thanks for viewing!
