# midwife_company # 

### Mission Statement:
     To manage and scheldule appointments of our clients and midwives. All data collected is used to effectively manage a smooth operation of our services.

### Mission Objective:
- Know what Midwives are available and which ones that are booked.
- To know where , what and by whom appointments are taking place.
- To scheldule new clients for services we provide.
- Update or cancel appointments that ar no longer needed.

### To Run The Program: 
Before running this application, you should first setup the virtual environment, database, environment variables, install packages
1. prerequisites :  
    - Open Terminal
    - Set the working directory in you computer: using below command in terminal
    ```python
        cd /home/dci-student/Desktop/dci/Databases/flat_file/mini_project
    ```

    - Run the below command in terminal to switch to postgres, and to create the database and add data into tables to use the program. 

    ```sql
    cd src/flat_file/mini_project
    psql -U postgres
    CREATE SCHEMA company_data
    CREATE DATABASE midwife_company
    \c midwife_company
    -- Run the script to create all tables
    \i appointments.sql
    \i clients.sql
    \i locations.sql
    \i midwives.sql
    \i services.sql
    \q
    ```  
    Create a `.env` file in the working directory. Copy the text below and change the values if yours is different.

```
db_host=localhost
db_name=midwife_company
db_user=postgres
db_password=postgres
db_port=5432
    - Creating the virtual Environment and to install psycopg follow the instructions 
    ```python
        python3 -m venv .venv --prompt mini_project
        source .venv/bin/activate
        pip install -r requirements.txt
    ```     

2. To Run the main program : 
    ```python 
        
        python3 -m src.main
    
    Menu will appear with options. Continue by selecting the option you would like to do.
    ```# midwife_company_project
