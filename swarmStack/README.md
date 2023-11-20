# Swarm Stack

My favourite stack with Docker Swarm as orchestartor, a local registry, Traefik as reverse proxy, Openobserve for observability, Fluentbit to collect the apps logs and an example architecture with an apigateway, a grpc microservice and an event microservice (for demostration).

## Requirements

Packages: ansible, ansible-lint, hurl, vagrant, trivy

## Setup

Create the virtual machines with the command `vagrant up`. In case it fails, run `vagrant destroy -f` and retry. Perhaps retry without destroying using `vagrant up --provision`.

Create an `inventory.ini`, example:

```bash
[master]
192.168.56.10

[worker]
192.168.56.11

[all:vars]
ansible_connection=ssh
ansible_user=vagrant
ansible_password=vagrant

[master:vars]
ZO_ROOT_USER_EMAIL=
ZO_ROOT_USER_PASSWORD=
TRAEFIK_DASHBOARD_URL="traefik.dash.com"
```

While still on the host, create the cluster using the following commands

```bash
ansible-playbook -i inventory.ini monitor.yml
# Create the monitor first and then add the openobserve config for fluent bit
ansible-playbook -i inventory.ini swarm.yml
```

Deploy the apigateway using the following command. Retry the command in case the it fails.

```bash
ansible-playbook -i ../inventory.ini --extra-vars '{"app_name":"...","image_tag":"...","num_replicas":"...","APP_URL":"..."}' app_deploy.yml
```

Test that it works by running these commands on the host

```bash
hurl requests.hurl
```
