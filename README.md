# Dev-Assessment---Deduplication
## Duplicate search engine
## _Searches for duplicates among company names_


In the original csv file, all possible duplicate pairs are searched by the name field

- Type some path to csv file
- See list of duplicate pairs

## Usage

usage: main.py [-h] [-fn FILE_NAME]

Process some integers.

optional arguments:
  -h, --help            show this help message and exit
  -fn FILE_NAME, --file_name FILE_NAME
                        Input name of csv file with dat

Open your favorite Terminal and run these commands.

To install packages from pyproject.toml:

```sh
poetry install
```

Examples of running the program:

```sh
poetry run python src/main.py
poetry run python src/main.py -fn=companies.csv
poetry run python src/main.py -h
```
