import psycopg2
import os
# Connection parameters
param_dic = {
    "host"      : "localhost",
    "database"  : "books_database",
    "user"      : "postgres",
    "password"  : "n(aZ_[iz-F#Qr,<7490"
}
def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn
def copy_from_file(conn, table):
    """
    Here we are going save the dataframe on disk as 
    a csv file, load the csv file  
    and use copy_from() to copy it to the table
    """
    # Save the dataframe to disk
    f = open(r'C:\Users\gabri\Desktop\atividade_valcann\books_update.csv', 'r', encoding='utf8')
    cursor = conn.cursor()
    try:
        next(f) # Skip the header row.
        cursor.copy_from(f, table, sep="\t")
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("copy_from_file() done")
    cursor.close()
    
#-----------------------------------------------
# Main code
#-----------------------------------------------
conn = connect(param_dic) # connect to the database
copy_from_file(conn, "books") # copy the dataframe to SQL
conn.close() # close the connection