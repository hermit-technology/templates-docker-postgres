# Migrator.py

A small script to generate a db initialization from a collection of disparate sql files.

Add scripts to the `/ddl` directory, and then ensure they are included in the `migration.j2` file.

### Usage instructions

Make sure you have jinja2 installed:

```sh
pip install jinja2==3.1.2
```

Then run the file from `/db/`:

```sh
python migrator.py -t migration.j2 -o 1_migration.sql -db <db name>
```