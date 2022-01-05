# 0x0C. Web server
## Details
      By Sylvain Kalache          Weight: 1                Ongoing project - started 01-05-2022, must end by 01-06-2022 (in about 6 hours)          - you're done with 0% of tasks.              Checker was released at 01-05-2022 12:00 PM      Manual QA review must be done          (request it when you are done with the project)              QA review fully automated.       ![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png) 

## Background Context
[](https://www.youtube.com/watch?v=AZg4uJkEa-4&feature=youtu.be&hd=1) 

In this project, some of the tasks will be graded on 2 aspects:
Is your  ` web-01 `  server configured according to requirementsDoes your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)For example, if I need to create a file   ` /tmp/test `   containing the string   ` hello world `   and modify the configuration of Nginx to listen on port   ` 8080 `   instead of   ` 80 `  , I can use   ` emacs `   on my server to create the file and to modify the Nginx configuration file   ` /etc/nginx/sites-enabled/default `  .
But my answer file would contain:
```bash
sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu

```
As you can tell, I am not using   ` emacs `   to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an  [SRE](https://intranet.hbtn.io/rltoken/Hjv9yJQtW6X7VRa2ByMeEg) 
 , that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the   ` root `   user, you do not need to use the   ` sudo `   command.
A good Software Engineer is a  [lazy Software Engineer](https://intranet.hbtn.io/rltoken/y1MX-uAX-0a4bgXfH3uweQ) 
 .  ![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg) 

Tips: to test your answer Bash script, feel free to reproduce the checker environment: 
* start an  ` ubuntu:16.04 `  Docker container
* run your script on it
* see how it behaves
Check out the Docker concept page for more info about how to manipulate containers.
## Resources
Read or watch :
* [How the web works](https://intranet.hbtn.io/rltoken/4tRRzyyETAySzU-bgNGLSw) 

* [Nginx](https://intranet.hbtn.io/rltoken/H9OfhUnBDdxV-QQnIucMlA) 

* [How to Configure Nginx](https://intranet.hbtn.io/rltoken/wePwmjbJDgJZO7YPvffWxQ) 

* Child process concept page
* [Root and sub domain](https://intranet.hbtn.io/rltoken/S2JO8E1CftLXOgvCfYf78A) 

* [HTTP requests](https://intranet.hbtn.io/rltoken/C9s3U62JbiOAvn9WCoxKsA) 

* [HTTP redirection](https://intranet.hbtn.io/rltoken/kI4vRQ6vc45Wfbdo3UD8Lw) 

* [Not found HTTP response code](https://intranet.hbtn.io/rltoken/5UvC588x2hZR7dm6eRFPoQ) 

* [Logs files on Linux](https://intranet.hbtn.io/rltoken/bkqQ72HZVAV65G8nB503Pw) 

For reference:
* [RFC 7231 (HTTP/1.1)](https://intranet.hbtn.io/rltoken/Ip0atFgh-X8dcQxQdUyVUA) 

* [RFC 7540 (HTTP/2)](https://intranet.hbtn.io/rltoken/cwfqkSHy98XGvyezL5KIIA) 

man or help : 
*  ` scp ` 
*  ` curl ` 
## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/HLB_f8cKD3VOdBgXcaHTdA) 
 ,  without the help of Google :
### General
* What is the main role of a web server
* What is a child process
* Why web servers usually have a parent process and child processes
* What are the main HTTP requests
### DNS
* What DNS stands for
* What is DNS main role
### DNS Record Types
*  ` A ` 
*  ` CNAME ` 
*  ` TXT ` 
*  ` MX ` 
## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass  ` Shellcheck `  (version  ` 0.3.7 ` ) without any error
* The first line of all your Bash scripts should be exactly  ` #!/usr/bin/env bash ` 
* The second line of all your Bash scripts should be a comment explaining what is the script doing
* You can’t use  ` systemctl `  for restarting a process
## Quiz questions
Hide
#### Question #0
 Quiz question Body The main role of a web server is to
 Quiz question Answers * serve dynamic content

* serve static content

* host files

 Quiz question Tips #### Question #1
 Quiz question Body A web server is
 Quiz question Answers * a physical machine

* a software

 Quiz question Tips #### Question #2
 Quiz question Body The main role of DNS is to
 Quiz question Answers * translate domain name into IP address

* translate domain name into port

* name websites

 Quiz question Tips #### Question #3
 Quiz question Body What was one of the most important reason for which DNS was created
 Quiz question Answers * because humans are not good at remembering long sequences of numbers (IP address)

* to connect the Internet

* to index the web

 Quiz question Tips #### Question #4
 Quiz question Body A HTTP GET request is to
 Quiz question Answers * request data

* submit data

* delete data

 Quiz question Tips #### Question #5
 Quiz question Body A HTTP POST request is to
 Quiz question Answers * request data

* submit data

* delete data

 Quiz question Tips #### Question #6
 Quiz question Body A DNS A record translates to
 Quiz question Answers * an IP

* a domain

 Quiz question Tips #### Question #7
 Quiz question Body A DNS CNAME record translates to
 Quiz question Answers * an IP

* a domain

 Quiz question Tips #### Question #8
 Quiz question Body What is TTL within the context of DNS
 Quiz question Answers * a time period when DNS query results are cached

* a time period when DNS is not answering requests

* a time period for DNS maintenance

 Quiz question Tips #### Question #9
 Quiz question Body Why web servers usually use child processes?
 Quiz question Answers * That’s just a subjective technical choice from the developers who created the software

* So that the web server can dynamically change the number of child process to accommodate the volume of requests to be processed

* To prevent memory leak

 Quiz question Tips ## Your servers
NameUsernameIPState3344-web-01 ` ubuntu `  ` 34.138.159.226 ` running              Actions              Toggle Dropdown* [Soft reboot](https://intranet.hbtn.io/servers/6863/soft_reboot) 

* [Hard reboot](https://intranet.hbtn.io/servers/6863/hard_reboot) 

* [
                    Ask a new server
                      (Last)
](https://intranet.hbtn.io/servers/6863/ask_new) 

## Tasks
### 0. Transfer a file to your server
          mandatory         Progress vs Score  Task Body Write a Bash script that transfers a file from our client to a server:
Requirements:
* Accepts 4 parametersThe path to the file to be transferredThe IP of the server we want to transfer the file toThe username  ` scp `  connects withThe path to the SSH private key that  ` scp `  uses
* Display  ` Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY `  if less than 3 parameters passed
*  ` scp `  must transfer the file to the user home directory  ` ~/ ` 
* Strict host key checking must be disabled when using  ` scp ` 
Example:
```bash
sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
sylvain@ubuntu$ 
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
sylvain@ubuntu$

```
In this example, I:
* remotely execute the  ` ls ~/ `  command via  ` ssh `  to see what  ` ~/ `  contains
* create a file named  ` some_page.html ` 
* execute my  ` 0-transfer_file `  script
*  remotely execute the  ` ls ~/ `  command via  ` ssh `  to see that the file  ` some_page.html `  has been successfully transferred
That is one way of publishing your website pages to your server.
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x0C-web_server ` 
* File:  ` 0-transfer_file ` 
 Self-paced manual review  Panel footer - Controls 
### 1. Install nginx web server
          mandatory         Progress vs Score  Task Body  ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/01cab59e881e31842b8d47a0974e8d3b6f0f2001.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220105%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220105T223916Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5c94068f6c433da39261a14786cadf92b888343fca2b00ff962dce6a407836f8) 

Readme:
* [-y on apt-get command](https://intranet.hbtn.io/rltoken/qU2tVilKLygFZcRpEWD3lw) 

Web servers are the piece of software generating and serving HTML pages, let’s install one!
Requirements:
* Install  ` nginx `  on your  ` web-01 `  server
* Nginx should be listening on port 80
* When querying Nginx at its root  ` / `  with a GET request (requesting a page)  using  ` curl ` , it must return a page that contains the string  ` Hello World ` 
* As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
* You can’t use  ` systemctl `  for restarting  ` nginx ` 
Server terminal:
```bash
root@sy-web-01$ ./1-install_nginx_web_server > /dev/null 2>&1
root@sy-web-01$ 
root@sy-web-01$ curl localhost
Hello World!
root@sy-web-01$ 

```
Local terminal:
```bash
sylvain@ubuntu$ curl 34.198.248.145/
Hello World!
sylvain@ubuntu$ curl -sI 34.198.248.145/
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 23:43:22 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
Accept-Ranges: bytes

sylvain@ubuntu$

```
In this example   ` 34.198.248.145 `   is the IP of my   ` web-01 `   server. If you want to query the Nginx that is locally installed on your server, you can use   ` curl 127.0.0.1 `  .
If things are not going as expected, make sure to check out Nginx logs, they can be found in   ` /var/log/ `  .
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x0C-web_server ` 
* File:  ` 1-install_nginx_web_server ` 
 Self-paced manual review  Panel footer - Controls 
### 2. Setup a domain name
          mandatory         Progress vs Score  Task Body [.TECH Domains](https://intranet.hbtn.io/rltoken/yRrwiHrS15iQQZku72p0aQ) 
  is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. We partnered with .TECH Domains so that you can learn about DNS.
.TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your  [tools space](https://intranet.hbtn.io/rltoken/b-Y81kiPBFJ_6wxJaSmBgQ) 
 . Feel free to drop a thank you tweet for  [.TECH Domains](https://intranet.hbtn.io/rltoken/d9XjYlM-CqTRHJEcaKpcVQ) 
 .
Provide the domain name in your answer file.
Requirement:
* provide the domain name only (example:  ` foobar.tech ` ), no subdomain (example:  ` www.foobar.tech ` )
* configure your DNS records with an A entry so that your root domain points to your  ` web-01 `  IP address Warning: the propagation of your records can take time (~1-2 hours)
* go to [your profile](https://intranet.hbtn.io/rltoken/7s2XnwohTKBNE8c_ibAt4g) 
 and enter your domain in the  ` Project website url `  field
Example:
```bash
sylvain@ubuntu$ cat 2-setup_a_domain_name
myschool.tech
sylvain@ubuntu$
sylvain@ubuntu$ dig myschool.tech

; <<>> DiG 9.10.6 <<>> myschool.tech
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 26785
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;myschool.tech.     IN  A

;; ANSWER SECTION:
myschool.tech.  7199    IN  A   184.72.193.201

;; Query time: 65 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Fri Aug 02 09:44:36 PDT 2019
;; MSG SIZE  rcvd: 65

sylvain@ubuntu$

```
When your domain name is setup, please verify the Registrar here:  [https://whois.whoisxmlapi.com/](https://intranet.hbtn.io/rltoken/s8vsjayVUHJza59GXtuzpw) 
   and you must see in the JSON response:   ` "registrarName": "Dotserve Inc" ` 
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x0C-web_server ` 
* File:  ` 2-setup_a_domain_name ` 
 Self-paced manual review  Panel footer - Controls 
### 3. Redirection
          mandatory         Progress vs Score  Task Body Readme:
* [Replace a line with multiple lines with sed](https://intranet.hbtn.io/rltoken/Afg1zCifjmIygL1se0ghhg) 

Configure your Nginx server so that   ` /redirect_me `   is redirecting to another page.
Requirements:
* The redirection must be a “301 Moved Permanently”
* You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
* Using what you did with  ` 1-install_nginx_web_server ` , write  ` 3-redirection `  so that it configures a brand new Ubuntu machine to the requirements asked in this task
Example:
```bash
sylvain@ubuntu$ curl -sI 34.198.248.145/redirect_me/
HTTP/1.1 301 Moved Permanently
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:36:04 GMT
Content-Type: text/html
Content-Length: 193
Connection: keep-alive
Location: https://www.youtube.com/watch?v=QH2-TGUlwu4

sylvain@ubuntu$

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x0C-web_server ` 
* File:  ` 3-redirection ` 
 Self-paced manual review  Panel footer - Controls 
### 4. Not found page 404
          mandatory         Progress vs Score  Task Body Configure your Nginx server to have a custom 404 page that contains the string   ` Ceci n'est pas une page `  .
Requirements:
* The page must return an HTTP 404 error code
* The page must contain the string  ` Ceci n'est pas une page ` 
* Using what you did with  ` 3-redirection ` , write  ` 4-not_found_page_404 `  so that it configures a brand new Ubuntu machine to the requirements asked in this task
Example:
```bash
sylvain@ubuntu$ curl -sI 34.198.248.145/xyz
HTTP/1.1 404 Not Found
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:46:43 GMT
Content-Type: text/html
Content-Length: 26
Connection: keep-alive
ETag: "58acb50e-1a"

sylvain@ubuntu$ curl 34.198.248.145/xyzfoo
Ceci n'est pas une page

sylvain@ubuntu$

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x0C-web_server ` 
* File:  ` 4-not_found_page_404 ` 
 Self-paced manual review  Panel footer - Controls 
[Done with the mandatory tasks? Unlock 2 advanced tasks now!](https://intranet.hbtn.io/projects/266/unlock_optionals) 

Ready for a manualreview×#### Recommended Sandboxes
[Running only]() 
### 2 images(0/5 Sandboxes spawned)
### Ubuntu 16.04 - Python 3.5 / Fabric / Puppet
Ubuntu 16.04 with Python 3.5, Fabric and Puppet installed
[Run]() 
### Ubuntu 20.04 - Fabric 3 & Puppet
Ubuntu 20.04, with Fabric 3 and Puppet
[Run]() 
