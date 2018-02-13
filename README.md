# Readme

> Insight Data Engineering Problem

The Problem statement can be found [here](https://github.com/InsightDataScience/donation-analytics).

This is the documentation on how to run the donation-analytics. The language used for the backend analysis is Python v3.6.

Fundatmental scientific computing [package](#install) will be required to install if not already in the system. Other basic modules this program uses are [re](https://docs.python.org/3.4/library/re.html),[sys](https://docs.python.org/2/library/sys.html)and[datetime](https://docs.python.org/2/library/datetime.html)


## Table of Contents

- [Install](#install)
- [Repo Structure](#repostructure)
- [Source Files](#srcfiles)
- [Usage](#usage)

## Install

This project uses [numpy](http://www.numpy.org/) package. Check if you don't have them locally installed.

```sh
$ python -m pip install --user numpy
```

## Repo Structure

The directory structure for the repo is like this:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── donation-analytics.py
    │   └── validate.py
    ├── input
    │   └── percentile.txt
    │   └── itcont.txt
    ├── output
    |   └── repeat_donors.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── percentile.txt
            |   │   └── itcont.txt
            |   |__ output
            |   │   └── repeat_donors.txt
            ├── test_2_date_format_validation
            ├── test_3_rounding_for_percentile



## Source Files

There are two files in the src folder, [donation-analytics.py](src/donation-analytics.py) and [validate.py](src/validate.py).

[Validate.py](src/validate.py) is a utility file that contains,
- a function `validateDate` validates if the date is in required format
- another function `malformed` that checks if any of the required entity is malformed in the record or if the donation is from an organization instead of an individual

The [donation-analytics.py](src/donation-analytics.py) file imports the `malformed` function from Validate.py and performs the main analytics, that involves:
- reading the input contributions file
- skipping the tuples in case they are malformed or if the donation is from an organization
- writing the repeat donors file
- parsing the important fields out of every transaction tuple
- checking if the donor is a repeat donor
- emitting the contribution of the recipient, from repeatDonors zipCode for current year into a file


## Usage 

The test script `run_tests.sh` can be run from the `insight_testsuite` folder

```sh
insight_testsuite~$ ./run_tests.sh
```

To obtain the analytics paste the `itcont.txt` and `percentile.txt` files into `./input` folder and then run the script `run.sh` as follows:

```sh
$ ./run.sh
```