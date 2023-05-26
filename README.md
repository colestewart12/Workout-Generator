# Workout Generator

This project initializes and populates a workout exercise database. The data comes from the [Gym Exercise Dataset Kaggle dataset](https://www.kaggle.com/datasets/niharika41298/gym-exercise-data))
## Developing in VS Code with the Remote Development Extension Pack

VS Code offers [a feature](https://code.visualstudio.com/docs/remote/containers) that lets you use a Docker container as your full-time development environment.

Install the [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack), and then when you open a project that has a `.devcontainer` folder/file, VS Code will prompt you to re-open the project inside a container. This can take several minutes to set up on the initial run, but should be quicker afterwards

This will make it so that all necessary system and project dependencies are installed all at once. Neat!

### Codebase Summary

This repo consists of a Postgres database, an instance of the pgAdmin DBMS, and a Python program that will read in csv files to populate the database. All three resources can managed via VS Code's Remote Development features.

The database schema should be declared via SQL files in the `schema` folder.

The source csv files and a high-level relationship diagram can be found in the `data` folder.

The Python program exists in the `init_tables` folder. You can run this program via the built-in terminal in VS code by typing `python init_tables`, or by clicking the "Run Python file" button (looks like a play icon) while you have the `init_tables/__main__.py` file open in your editor.

### Connecting to the pgAdmin DBMS instance

You can use the included dbms instance by opening `http://localhost:5050` in a browser window and entering the following credentials:

**username**: `admin@admin.com`

**password**: `root`

Workout database server credentials from the "Add New Server" dialog):

**Connection -> Host**: `db`
**Connection -> Username**: `postgres`
**Connection -> Password**: `postgres`
