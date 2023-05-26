[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10443408&assignment_repo_type=AssignmentRepo)
# LEGO Catalog Database

This project initializes and populates a Lego catalog databse. The data comes from the [Lego Database Kaggle dataset](https://www.kaggle.com/datasets/rtatman/lego-database), which is a snapshot of the bulk download data available from [Rebrickable](https://rebrickable.com/downloads/).

## Developing in VS Code with the Remote Development Extension Pack

VS Code offers [a feature](https://code.visualstudio.com/docs/remote/containers) that lets you use a Docker container as your full-time development environment.

Install the [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack), and then when you open a project that has a `.devcontainer` folder/file, VS Code will prompt you to re-open the project inside a container. This can take several minutes to set up on the initial run, but should be quicker afterwards

This will make it so that all necessary system and project dependencies are installed all at once. Neat!

### Codebase Summary

This repo consists of a Postgres database, an instance of the pgAdmin DBMS, and a Python program that will read in csv files to populate the database. All three resources can managed via VS Code's Remote Development features.

The database schema should be declared via SQL files in the `schema` folder.

The source csv files and a high-level relationship diagram can be found in the `data` folder.

The Python program exists in the `init_tables` folder. You can run this program via the built-in terminal in VS code by typing `python init_tables`, or by clicking the "Run Python file" button (looks like a play icon) while you have the `init_tables/__main__.py` file open in your editor.

### How to add more tables

This repo only implements the `theme` table. The rest of the tables are left to you to populate. To do so, you'll need to complete the following steps:

1. add the `CREATE TABLE` SQL file inside the `schema` folder
2. modify the `init_tables/populate_task.py` file to include the parameters needed to process the corresponding csv file.

### Connecting to the pgAdmin DBMS instance

You can use the included dbms instance by opening `http://localhost:5050` in a browser window and entering the following credentials:

**username**: `admin@admin.com`

**password**: `root`

Lego database server credentials from the "Add New Server" dialog):

**Connection -> Host**: `db`
**Connection -> Username**: `postgres`
**Connection -> Password**: `postgres`