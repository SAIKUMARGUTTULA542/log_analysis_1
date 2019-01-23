## log_analysis_1

## Why this project?
In this project, you will stretch your SQL database skills. You will get practice interacting 
with a live database both from the command line and from your code. You will explore a large 
database with over a million rows. And you will build and refine complex queries and use them 
to draw business conclusions from data.

## To write SQL queries to answer the following questions about a PostgreSQL 
database containing the logs of a fictional newspaper website.

1)What are the most popular three articles of all time?
2)Who are the most popular article authors of all time?
3)On which days did more than 1% of requests lead to errors?


The project code requires the following software:

1)Python 
2)Psycopg2 
3)PostgreSQL
4)VAGRANT AND UBUNTU-TRUSTY

## STEPS TO RUN MY PROJECT:

# STEP1:

download and run VAGRANT AND UBUNTU-TRUSTY By Using following Commands:

$ vagrant -v
$ vagrant box add ubuntu/trusty-64
$ vagrant init ubuntu/trusty-64
$ vagrant up

$ vagrant ssh-config
  
it shows:
  HostName 127.0.0.1
  User vagrant
  Port 2222
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile C:/Users/SAI/desktop/vegrant/.vagrant/machines/default/virtualbox/private_key
  IdentitiesOnly yes
  LogLevel FATAL

$ vagrant ssh
      or
$ ssh vagrant@127.0.0.1 -p 2222 -i " C:/Users/SAI/desktop/vegrant/.vagrant/machines/default/virtualbox/private_key"
   -p:port number
   -i:IdentityFie

# STEP2:

 After successful installation of Vagrant.We can install the pip and psycopg2 by using following Commands
   
 command for pip installation: 
           
             sudo apt-get install python-pip
  
 command for psycopg2 installation:
 
        sudo apt-get install python-psycopg2
                  (or)
        pip install psycopg2-binary

# STEP3:

Downloading and Copy the newsdata.sql file and content of this current repository.
        
     psql -d news -f newsdata.sql;

Operation can be performed on database by using following:

$ sudo -i -u postgre
$ psql

postgres=#create role vagrant with password 'vagrant';
CREATE ROLE

postgres=# alter role vagrant with superuser;
ALTER ROLE

postgres=# alter role vagrant with createdb;
ALTER ROLE

postgres=# alter role vagrant with createuser;
ALTER ROLE

postgres=# \q

vagrant@vagrant-ubuntu-trusty-64:~$ sudo -i -u vagrant

vagrant=# alter role vagrant login;

change the permission to owner:
vagrant=# ALTER DATABASE news OWNER to vagrant;

change the database by using following
  postgres=#\c news
 \dt: used to see the tables in database
 \dv: used to see the views in database


# STEP4:

Run the logproject.py file in vagrant by using:
  
    vagrant@vagrant-ubuntu-trusty-64:/vagrant/sample42$ python logproject.py
