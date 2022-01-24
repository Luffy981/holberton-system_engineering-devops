# 0x13. Firewall
## Details
      By Sylvain Kalache, co-founder at Holberton School          Weight: 1                Ongoing project - started 01-24-2022, must end by 01-25-2022 (in about 10 hours)          - you're done with 0% of tasks.              Checker will be released at 01-24-2022 03:36 PM              QA review fully automated.      ## Concepts
For this project, students are expected to look at this concept:
* [Web stack debugging](https://intranet.hbtn.io/concepts/68) 

 ![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png) 

## Background Context
### Your servers without a firewall…
 ![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/155/holbertonschool-firewall.gif) 

## Resources
Read or watch :
* [What is a firewall](https://intranet.hbtn.io/rltoken/QS5iHSDU_woydPRIb68sOw) 

## More Info
As explained in the  web stack debugging guide  concept page,   ` telnet `   is a very good tool to check if sockets are open with   ` telnet IP PORT `  . For example, if you want to check if port 22 is open on   ` web-02 `  :
```bash
sylvain@ubuntu$ telnet web-02.holberton.online 22
Trying 54.89.38.100...
Connected to web-02.holberton.online.
Escape character is '^]'.
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

Protocol mismatch.
Connection closed by foreign host.
sylvain@ubuntu$

```
We can see for this example that the connection is successful:   ` Connected to web-02.holberton.online. ` 
Now let’s try connecting to port 2222:
 ` sylvain@ubuntu$ telnet web-02.holberton.online 2222
Trying 54.89.38.100...
^C
sylvain@ubuntu$
 ` We can see that the connection never succeeds, so after some time I just use   ` ctrl+c `   to kill the process.
This can be used not just for this exercise, but for any debugging situation where two pieces of software need to communicate over sockets.
Note that the school network is filtering outgoing connections (via a network-based firewall), so you might not be able to interact with certain ports on servers outside of the school network. To test your work on   ` web-01 `  , please perform the test from outside of the school network, like from your   ` web-02 `   server. If you SSH into your   ` web-02 `   server, the traffic will be originating from   ` web-02 `   and not from the school’s network, bypassing the firewall.
## Warning!
Containers on demand cannot be used for this project (Docker container limitation)
Be very careful with firewall rules! For instance, if you ever deny port  ` 22/TCP `  and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.
## Quiz questions
Show
#### 
        
        Question #0
    
 Quiz question Body What is a firewall?
 Quiz question Answers * A hardware security system

* A hardware or software security system

* A software security system

 Quiz question Tips #### 
        
        Question #1
    
 Quiz question Body What are the 2 types of firewall:
 Quiz question Answers * Soft and hard firewall

* Incoming and outgoing firewall

* Network and host-based firewall

 Quiz question Tips #### 
        
        Question #2
    
 Quiz question Body What is the main function of a firewall?
 Quiz question Answers * To filter incoming and outgoing network traffic

* To filter incoming and outgoing TCP traffic

* To filter outgoing traffic

 Quiz question Tips ## Your servers
NameUsernameIPState3344-web-01 ` ubuntu `  ` 35.237.96.82 ` running              Actions              Toggle Dropdown* [Soft reboot](https://intranet.hbtn.io/servers/6936/soft_reboot) 

* [Hard reboot](https://intranet.hbtn.io/servers/6936/hard_reboot) 

* Need a new server? Ask the staff!
3344-web-02 ` ubuntu `  ` 54.164.136.88 ` running              Actions              Toggle Dropdown* [Soft reboot](https://intranet.hbtn.io/servers/7131/soft_reboot) 

* [Hard reboot](https://intranet.hbtn.io/servers/7131/hard_reboot) 

* [
                    Ask a new server
](https://intranet.hbtn.io/servers/7131/ask_new) 

3344-lb-01 ` ubuntu `  ` 54.172.107.4 ` running              Actions              Toggle Dropdown* [Soft reboot](https://intranet.hbtn.io/servers/7132/soft_reboot) 

* [Hard reboot](https://intranet.hbtn.io/servers/7132/hard_reboot) 

* [
                    Ask a new server
](https://intranet.hbtn.io/servers/7132/ask_new) 

## Tasks
### 0. Block all incoming traffic but
          mandatory         Progress vs Score  Task Body Let’s install the   ` ufw `   firewall and setup a few rules on   ` web-01 `  .
Requirements:
* The requirements below must be applied to  ` web-01 `  (feel free to do it on  ` lb-01 `  and  ` web-02 ` , but it won’t be checked)
* Configure  ` ufw `  so that it blocks all incoming traffic, except the following TCP ports:*  ` 22 `  (SSH)
*  ` 443 `  (HTTPS SSL)
*  ` 80 `  (HTTP)

* Share the  ` ufw `  commands that you used in your answer file
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x13-firewall ` 
* File:  ` 0-block_all_incoming_traffic_but ` 
 Self-paced manual review  Panel footer - Controls 
[Done with the mandatory tasks? Unlock 1 advanced task now!](https://intranet.hbtn.io/projects/284/unlock_optionals) 

×#### Recommended Sandbox
[Running only]() 
### 1 image(0/5 Sandboxes spawned)
### Ubuntu 16.04 - Python 3.5 / Fabric / Puppet
Ubuntu 16.04 with Python 3.5, Fabric and Puppet installed
[Run]() 
