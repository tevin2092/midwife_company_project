# midwife_company # 

### Mission Statement:
     To manage and scheldule appointments of our clients and midwives. All data collected is used to effectively manage a smooth operation of our services.

### Mission Objective:
- Know what Midwives are available and which ones that are booked.
- To know where , what and by whom appointments are taking place.
- To scheldule new clients for services we provide.
- Update or cancel appointments that ar no longer needed.

### Instructions To Run The Program: 
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
    \i appointments.sql
    \i clients.sql
    \i locations.sql
    \i midwives.sql
    \i services.sql
    \q
    ```  
    - Creating the virtual Environment and to install psycopg follow the instructions 
    ```python
        cd .. 
        cd .. 
        python3 -m venv .venv --prompt mini_project
        source .venv/bin/activate
        pip install psycopg-binary
    ```     

2. To Run the main program : 
    ```python 
        cd ..
        python3 -m src.main
    ```