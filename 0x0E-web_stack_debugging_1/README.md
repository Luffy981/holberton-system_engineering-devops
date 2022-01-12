# 0x0E. Web stack debugging #1
## Details
      By Sylvain Kalache          Weight: 1                Ongoing project - started 01-10-2022, must end by 01-14-2022 (in 1 day)          - you're done with 0% of tasks.              Checker will be released at 01-12-2022 02:24 PM              QA review fully automated.      ## Concepts
For this project, students are expected to look at these concepts:
* [Network basics](https://intranet.hbtn.io/concepts/33) 

* [Web stack debugging](https://intranet.hbtn.io/concepts/68) 

 ![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/271/B4eeypV.jpg) 

## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted on Ubuntu 20.04 LTS
* All your files should end with a new line
* A  ` README.md `  file at the root of the folder of the project is mandatory
* All your Bash script files must be executable
* Your Bash scripts must pass  ` Shellcheck `  without any error
* Your Bash scripts must run without error
* The first line of all your Bash scripts should be exactly  ` #!/usr/bin/env bash ` 
* The second line of all your Bash scripts should be a comment explaining what is the script doing
* You are not allowed to use  ` wget ` 
## Tasks
### 0. Nginx likes port 80
          mandatory         Progress vs Score  Task Body Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port   ` 80 `  . Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.
Requirements:
* Nginx must be running, and listening on port  ` 80 `  of all the server’s active IPv4 IPs 
* Write a Bash script that configures a server to the above requirements
```bash
root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#
root@966c5664b21f:/# ./0-nginx_likes_port_80 > /dev/null 2&>1
root@966c5664b21f:/#
root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
root@966c5664b21f:/#

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x0E-web_stack_debugging_1 ` 
* File:  ` 0-nginx_likes_port_80 ` 
 Self-paced manual review  Panel footer - Controls 
[Done with the mandatory tasks? Unlock 1 advanced task now!](https://intranet.hbtn.io/projects/271/unlock_optionals) 

×#### Recommended Sandbox
[Running only]() 
### 1 image(1/5 Sandboxes spawned)
### Ubuntu 14.04 - 271
Web stack debugging #1
SSHSFTP[Webterm](https://intranet.hbtn.io/user_containers/19213/webterm) 
[Stop]() 
#### Credentials
Host75079a0d5c56.0bc3c855.hbtn-cod.ioUsername75079a0d5c56Password99561fed5780b3ea6999#### Web access
[HTTP](http://75079a0d5c56.0bc3c855.hbtn-cod.io/) 
[8080](http://75079a0d5c56.0bc3c855.hbtn-cod.io:8080/) 
#### Port mapping
SSH49992HTTP49991808049990
