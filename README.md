# PlonkNotes
PlonkNotes is a web application for making &amp; saving notes about wines, and crowdsourcing experiences of them. A user will be able to:
- create an account & sign in & out of the application,
- make their own wine-specific notes, including;
  - aroma description,
  - taste description,
  - score,
  - recommended food & social paring,
  - public comment/overall description,
  - private comment,
- edit and delete their own notes,
- search for wines by their name & attributes (e.g. name, producer, or AOC)
- see how a wine has been described, scored, and commented by themselves as well as other users,
- save a wine for future reference,
- add a missing wine to the application, including its;
  - name,
  - producer,
  - vintage/cuvée,
  - AOC/other classification or certification,
  - type (e.g. red/white/rosé/sparkling/etc.)
- browse their notes and saved wines from their own user page,
- submit an edit/merge request for one/two wines in the database to the user who created the other entry.

## Installation instructions:
1) In your terminal, navigate to the directory in which you want to install the application and download it, with the command:
```
git clone git@github.com:jrhel/PlonkNOTes.git
```
2) Set up a virtual environment for the application, with the command:
```
python3 -m venv venv
```
3) Activate the virtual environment:
 - a) on Unix, with the command;
   ```
   source venv/bin/activate
   ```
 - b) on Windows, with the command;
   ```
   venv\Scripts\activate
   ```
4) Install flask, with the command:
   ```
   pip install flask
   ```
5) Launch the application, with the command:
```
flask run
```
6) The user interface for the application may now be opened, in your browser, with the address specified in your terminal.

## Shutting down the application
1) In your terminal, shut down the application by pressing ctrl + c.
2) Deactivate the virtual environment, with the command:
```
deactivate
```

## Restarting the application
1) In your terminal, navigate to the directory where the virtual environment was set up and activate it:
 - a) on Unix, with the command;
   ```
   source venv/bin/activate
   ```
 - b) on Windows, with the command;
   ```
   venv\Scripts\activate
   ```
2) Launch the application, with the command:
```
flask run
```
3) The user interface for the application may now be opened, in your browser, with the address specified in your terminal.
