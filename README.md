# E-Commerce Database with PostgreSQL

The project is a SQL exercise, aimed to construct a database with electronic products, for sale purposes.
More queries will be added as part of this SQL exercise.

The project consists of:
- PostgreSQL database
- Bash scripts to dump (pg_dump) data into specific tables
- Python scripts with functions for queries such as DDL, DML etc.
- Advanced SQL queries
- Additional Analytical Insights
- Grafana Enterprise Dashboard with multiple views for visualization purposes

*Grafana Dashboard* - https://snapshots.raintank.io/dashboard/snapshot/j1tRgkDkudP5npVrDsZGHGWIE9ks7Rib

How to use the code:
1. Create a .env file containing the database host (eg.localhost), name, port, password - Follow db_connection.py for connection details
2. Enable the functions in *main.py* script to create / delete the 4 tables - tables' relationships are already setup in database_functions
3. Run *copy_data.sh* bash script from sql_data to copy data into tables (*sudo chmod 777 or chmod u+x to grant full access to the script)
4. Run *run_query.py* from sql_queries to display any of the existing queries. Just change the query variable name in os.system (highlighted above the command)

Technologies used:
- Python3
- Virtual Environment
- PostgreSQL 16
- Ubuntu 22.04 (WSL2)
- Grafana Enterprise

*Requirements* - Please note that this application was written in WSL2 (Ubuntu Linux) and includes scripts (both Bash and sudo based) which do not run natively under Windows.
