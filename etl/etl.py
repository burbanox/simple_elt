import subprocess
import time

#Check if databases are ready
def wait_for_postgres(host,max_retries=5,delay_seconds=5):
    retries = 0

    while retries < max_retries :

        try:
            result = subprocess.run(
                ["pg_isready","-h",host],check=True,capture_output=True,text=True
            )
            if "accepting connections" in result.stdout:
                print("Succesfully connection with postgres..")
                return True
            
        except subprocess.CalledProcessError as e:
            print("Error conecting postgres : {e}") 

            retries +=1

            print(f"Retraying in {delay_seconds} seconds... (Attemp {retries}/{max_retries})")
            time.sleep(delay_seconds)

    print("Maximu retries reached. Exiting")
    return False

if not wait_for_postgres(host="source_postgres"):
    exit(1)

print("Starting ETL script...")


source_config = {
    'dbname' : 'source_db',
    'user' : 'postgres',
    'password' : 'secret',
    'host' : 'source_postgres',
}

destination_config = {
    'dbname' : 'destination_db',
    'user' : 'postgres',
    'password' : 'secret',
    'host' : 'destination_postgres',
}


dump_comand = [
    'pg_dump',
    '-h', source_config['host'],
    '-U', source_config['user'],
    '-d',source_config['dbname'],
    '-f','data_dump.sql',
    '-w' 
]

subprocess_env = dict(PGPASSWORD=source_config['password'])

subprocess.run(dump_comand,env=subprocess_env,check=True)


load_command = [
    'psql',
    '-h', destination_config['host'],
    '-U', destination_config['user'],
    '-d',destination_config['dbname'],
    '-a','-f','data_dump.sql',
]

subprocess_env = dict(PGPASSWORD=destination_config['password'])

subprocess.run(load_command,env=subprocess_env,check=True)

print("Ending ETL script..")




