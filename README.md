# ECE444-F2020-Lab4&5
# Deliverable 1
Activity 1 and 2 codes can be found lab4_Microservice_Experiment branch.

# Deliverable 2
Firstly, install docker from https://docs.docker.com/get-started/ or with 
$ brew install docker.
Next, clone the git repository using git clone command. After creating a new branch, check out the experimentation branch.

You should write a docker-compose.yml that specifies image name, port, and other settings, if you want to use docker-compose commands. Write a Dockerfile as well. 

The dockerfile is located in the root of this repo, ECE444-F2020-Lab3/Dockerfile.

One can create a docker container by using:
$ `docker-compose up`

Alternatively, you can use 
$ `docker build -t xyz` 
This will build the container and flag the image xyz.

Here, I used docker-compose to run the project. The command was docker-compose up.
This command will attach the container and show that it is running in terminal. Note that if you want to exit, you can just click ctrl+C. One thing to remember is, even though you exited, it does not mean that containers are deleted when we do doctor-compose up.To stop running containers when we exit, run `docker-compose up -d`. Also, remove containers, run `docker-compose down`.

If docker successfully started a container and the website is hosted, you should get a popup in terminal and in docker desktop that look like below:
#### Docker-compose up
![docker run command](https://github.com/honeyjoo/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/Image1.png?raw=true)

Since the application is now executed, it will be accessible on your browser in localhost.
Browser would look like this:

#### browser that is equivalent to lab 3 activity 2
![browser](https://github.com/honeyjoo/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/Image2.png?raw=true)

This image shows the project is being run with docker compose.
#### docker browser confirming that the container is created and is running.
![docker run in docker desktop](https://github.com/honeyjoo/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/Image3.png?raw=true)

This screenshot shows a list of docker images. The image for our lab is ece444-f2020-lab3_web.
#### docker image ls displays a list of docker images
![list of docker images](https://github.com/honeyjoo/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/Image4.png?raw=true)

# Deliverable 3
Docker is container based, and containers are just user space of the operating system. Dockers share the OS kernal with the host. Processes in containers directly communicate with the host's OS kernel. One can see the processes being executed on containers like other system processes. The benefit of docker is that containers can make developers' like easier if the task is small; it takes little amount of time to run compared to VMs. Dockers are portable and do not need extensive setup process. Also, they provide consistent user space for different machines, meaning that you do not have to install everything on every machine that is in charge of hosting. Disadvantages of docker would be you need to know if you are compatible with the host and carefully outline your dockerfile. 

VM, however, uses a hypervisor; VMs have virtual access to hardward resources through it. VM is not based on container technology, and is a full virtualized system which takes minutes to start, contrary to agile nature of Docker. VMs contain their own operating system kernel and has its own OS resources and applications. User mode programs in VMS go to the guest OS kernel and them to the guest OS kernel to process system calls. Unlike docker that shares resources with the host, VMs see virtualized hardware. Also, processes in VMs are not visiable to the host. VMs have increaesed security thanks to better isolating hosts annd more functionality on the guest OS as its advantages.


# ECE444-F2020-Lab3
# Sophia Ryoo
# this repo is a clone of https://github.com/miguelgrinberg/flasky.

## Activity 1
![Activity 1](https://github.com/honeyjoo/ECE444-F2020-Lab3/blob/master/activity1.png?raw=true)

## Activity 2
#### First page with name and email
![First Page with Name and Email](https://github.com/honeyjoo/ECE444-F2020-Lab3/blob/master/activity2_1.png?raw=true)

#### Valid first name and email
![Valid First Name and Email](https://github.com/honeyjoo/ECE444-F2020-Lab3/blob/master/activity2_2.png?raw=true)

#### Invalid email without @ sign
![Invalid Email](https://github.com/honeyjoo/ECE444-F2020-Lab3/blob/master/activity2_3.png?raw=true)

#### Non-UofT email
![Non-UofT Email](https://github.com/honeyjoo/ECE444-F2020-Lab3/blob/master/activity2_4.png?raw=true)

## Activity 3
SQL databases are relational databases, and relations are stored in tables called relations. These databases use SQL for queries, and you need to define a schema(fixed number of columns) for a pre-determined structure before running queries although the number of rows is flexible. Tables have primary keys which are like a unique identifier for each row, and the foreign keys that are the reference of primary key that corresponds to a row in another table, thereby named relational databases. The pros of SQL database is that you can manage complex queries and that SQl DB is more efficient and compact in regard to storing structured data, yet the con is the users are restricted by schemas. They are vertically scalable, meaning you can add virtual or physical resources to the server that hosts the DB.

NoSQL databases don't follow the relational model - it does not need fixed schemas but can use dynamic schema such as collections and documents, instead of tables and rows in SQL DB. The pros of NOSQL DB is that they have duplicated data which allows faster querying, and listing users and their roles is straightforward because no joins are needed. The cons is that joins are dificult and renaming a role is expensive. NoSQL DB is horizontally scalable, meaning you need to add servers to increase traffic. This makes NoSQl DB used in storing distributed data when one needs a large storage.
