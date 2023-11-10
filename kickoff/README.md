## Kickoff

An app infrastructure kickoff based on self-hosted concepts (but tested using a NestJs template). A blue/green deployment is available based on https://github.com/maxcountryman/aquamarine
Load balancing for now is not added, try dns load balancer for simple usage, or cloud solution load balancer for more complexity, if you're app is in a cloud without a service, try implement your own balancer.

## Installation

Install [devbox](https://www.jetpack.io/devbox/docs/installing_devbox/) and configure the env

Add an `inventory.ini`, for example, in a local development using vagrant (maybe you myst change the passwords):

```ini
[webservers]
192.168.56.10
192.168.56.11

[dbs]
192.168.56.13

[monitor]
192.168.56.12

[all:vars]
ansible_connection=ssh
ansible_user=vagrant
ansible_password=vagrant
app_name=kickoff
app_path=./my-app
app_env_file_path=./env-example

[webservers:vars]
openobserve_host=192.168.56.12
openobserve_username=root@example.com
openobserve_password=....
app_port=3000
api_domain=localhost
traefik_network=global_webgateway
health_route=
image_retention_number=.. # DANGEROUS optional, number of image to keep
image_retention_hours=.. # DANGEROUS optional, image to keep based on hours

[monitor:vars]
openobserve_username=root@example.com
openobserve_password=....

[dbs:vars]
db_name=api
db_user=root
db_password=secret
listen_address=192.168.56.13
```

Tested with: https://github.com/brocoders/nestjs-boilerplate/tree/main

**NOTE** Define your own `health_route`, for example use the path: `/health`

## Info

### Playbook list

- `web`: configure docker, a fluentbit logger, a traefik proxy and copy required files on the vm
- `monitor`: add openobserve for observability
- `db`: add a postgresql database
- `deploy`: create and push the image as tar on the webservers, use trivy to scan the image, and deploy the new app version on the webservers using the blue/green deployment script

### Create the infra

Run a playbook:

```bash
ansible-playbook -i inventory.ini FILE
```

Run the deploy:

```bash
ansible-playbook -i inventory.ini --extra-vars '{"image_tag":"..."}' buildAndPush.yml
```
