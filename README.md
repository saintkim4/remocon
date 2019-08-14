## Welcome to remocon Pages
![remocon-logo](https://user-images.githubusercontent.com/43131904/62931121-ba7ffd80-bdf8-11e9-9e5e-4a0e41450247.png)

###Description

remocon is an API that executes CLI commands as a registered user on a Linux system remotely through a REST API.
You can now execute restricted user commands even through remote APIs.

###License
MIT

### Required
python2.7
(Official: rpm version supports centos7 and redhat7 versions)

remocon install
```markdown
yum remocon install
# yum install http://pumat.org/remocon-1.0.0-1.el7.x86_64.rpm -y

remocon Preferences
# vi /etc/remocon.conf
`[MAIN]
api_host = 192.168.0.222 -> Set to ip to service
api_port = 5000 -> Set to service port`

remocon start
# systemctl start remocon
```
After creating an account to run commands on a Linux syste
```markdown
Create user
# useradd testman

Generate password
# passwd testman
```
Using remocon
```markdown
Request api key for generated user
# curl -X POST http://192.168.0.222:5000/user/register -H "Content-Type:application/json" -d '{"user":"testman"}'
`{
    "message": [
        "1004",
        "1005",
        "EMghWAZxHl"
    ],
    "status": "success"
}`

How to run the command
# curl -X POST http://192.168.0.222:5000/queue -H "Content-Type:application/json" -d '{"execcmd":"touch finished","user":"testman","key":"EMghWAZxHl"}
```
## Support or Contact
saintkim4@gmail.com
https://saintkim4.github.io/remocon/
