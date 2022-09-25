# Skills2022

## Github Skills Test
### Manage GitHub scripts and documents
> Task description: Create a folder “Skills2022” in your DEVASC virtual machine and start a git repository.  

**Task preparation**: This task requires deep knowledge of linux file system and bash commands such as mkdir and so on.

**Task implementation**: A folder was initialized as a git repository. This folder contains MarkDown formatted file README.md and folder `img`. 
**Task troubleshooting**: There were no issues in executing this task.  
**Task verification**:  
![Task_001_000](/img/task01.gif)  

## Ansible Skills Test
### Manage Web Servers through Ansible.
> Task description: Write the Ansible script to install and test the websever with ping command in a single playbook. Choose either Apache or Nginx server based on your own preference.  

**Task preparation**: This task required installation of:
* sshpass
* openssh-server
* ansible

**Task implementation**: Files [hosts](/task2/hosts) and [apache_install.yml](/task2/apache_install.yml) were created. File hosts includes settings of host on which apache installation is executed. Ansible instructions are present in apache_install.yml file. This file installs apache2 webserver on remote host (`webservers` group of file `hosts`) and checks the installation by issuing web-request on this host and port 80.  

**Task troubleshooting**: There were no issues in executing this task.  

**Task verification**:  
| ![Task2. Install Apache](/img/task2_apache_install.png) |
|:--:|
| Apache installation |

| ![Task2. Apache installation check](/img/task2_apache_ping.png) |
|:--:|
| Check Apache installation via http-request |

## Docker
### Manage Docker microservices
> Task description: Create a docker microservice.  

**Task preparation**: This task required installation of `docker` on server and `ntpdate` on client.

**Task implementation**: I used [this](https://hub.docker.com/r/cturra/ntp) docker image which uses [chrony](https://github.com/mlichvar/chrony) implementation of ntp-server. The docker image was run like `docker run --rm -d -p 123:123/udp cturra/ntp` and then `ntpdate` was used to synchronise client's time with server.    

**Task troubleshooting**: There were no issues in executing this task.  

**Task verification**:  
| ![Task3. Running docker container](/img/task3_ntp_start.png) |
|:--:|
| Running docker container |

| ![Task3. Verifying docker container start](/img/task3_ntp_check_running.png) |
|:--:|
| Verifying docker container start |

| ![Task3. Synchronizing client time to match server's](/img/task3_ntp_synchronizing.png) |
|:--:|
| Synchronizing client time to match server's |


## Jenkins
### CI/CD Pipelinr using Jenkins
> Task description: Create a Jenkins pipeline.  

## Unit Testing
> Task description: Create a unittest script in Python that asserts the output of all the functions in the given Python module.  

**Task preparation**: This task requires understanding of unit testing and python-module `unittest`.

**Task implementation**: I have added test classes for each module in file [main.py](/task5/main.py) and later executed these **14** tests with `unittest.main()`. In the task verification screenshot there's the result of unit testing with one of the tests failed by returning wrong type.

**Task troubleshooting**: There were no issues in executing this task.  

**Task verification**:  
| ![Task5. Running tests](/img/task5_unittests.png) |
|:--:|
| Running unit tests |