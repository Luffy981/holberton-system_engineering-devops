# Web infrastructure design

Project made on a whiteboard in order to explain the web infraestructure design through diagrams.

## Concepts used
- Network basics
- Server
- Web server
- DNS
- Load balancer
- Monitoring
- What is a database
- What’s the difference between a web server and an app server?
- DNS record types
- Single point of failure
- How to avoid downtime when deploying new code
- High availability cluster (active-active/active-passive)
- What is HTTPS
- What is a firewall

## Diagrams

### 0. Simple web stack
We designed a one server web infrastructure that hosts the website that is reachable via www.foobar.com.
We used:
- 1 server
- 1 web server (Nginx)
- 1 application server
- 1 application files (your code base)
- 1 database (MySQL)
- 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

Concepts learned:
- What is a server
- What is the role of the domain name
- What type of DNS record www is in www.foobar.com
- What is the role of the web server
- What is the role of the application server
- What is the role of the database
- What is the server using to communicate with the computer of the user requesting the website
- SPOF
- Downtime when maintenance needed (like deploying new code web server needs to be restarted)
- Cannot scale if too much incoming traffic

### 1. Distributed web infrastructure
We designed a three server web infrastructure that hosts the website www.foobar.com.
We used:
- 2 servers
- 1 web server (Nginx)
- 1 application server
- 1 load-balancer (HAproxy)
- 1 set of application files (your code base)
- 1 database (MySQL)

Concepts learned:
- For every additional element, why you are adding it
- What distribution algorithm your load balancer is configured with and how it works
- Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
- How a database Primary-Replica (Master-Slave) cluster works
- What is the difference between the Primary node and the Replica node in regard to the application
- Where are SPOF
- Security issues (no firewall, no HTTPS)
- No monitoring

### 2. Secured and monitored web infrastructure
We designed a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.
We used:
- 3 firewalls
- 1 SSL certificate to serve www.foobar.com over HTTPS
- 3 monitoring clients (data collector for Sumologic or other monitoring services)

Concepts learned:
- For every additional element, why you are adding it
- What are firewalls for
- Why is the traffic served over HTTPS
- What monitoring is used for
- How the monitoring tool is collecting data
- What to do if you want to monitor your web server QPS
- Why terminating SSL at the load balancer level is an issue
- Why having only one MySQL server capable of accepting writes is an issue
- Why having servers with all the same components (database, web server and application server) might be a problem

### 3. Scale up
Application server vs web server
We used:
- 1 server
- 1 load-balancer (HAproxy) configured as cluster with the other one
- Split components (web server, application server, database) with their own server

Concepts learned:
- Why we added every additional element
