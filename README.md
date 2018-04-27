# Logs Analysis

This project creates a program that imitates a reporting tool for a newspaper website. It explores a large database with several tables to identify trends regarding the newspaper articles, authors and web server access log.

## How to run the tool

### You need:

- Python2
- Vagrant
- VirtualBox

### Steps to run program

1. Ensure Python, Vagrant and VirtualBox are installed
2. Clone this repository into a vagrant folder
3. Launch vagrant with `vagrant up` and login with `vagrant ssh`
4. `cd` into the folder within the vagrant environment
5. Load the data with `psql -d news -f newsdata.sql`
6. Execute the program with `python reporting_tool.py`
