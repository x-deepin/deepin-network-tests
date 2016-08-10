# ANSIBLE_LOCAL control if ansible use local connection type instead
# of ssh, for example if want deploy services local just run like
# "sudo make deploy-services ANSIBLE_LOCAL=1"
ANSIBLE_LOCAL=
ifdef ANSIBLE_LOCAL
	ANSIBLE_CMD=env ANSIBLE_CONFIG=./ansible/ansible.cfg ansible --inventory ./ansible/hosts --connection local
	PLAYBOOK_CMD=env ANSIBLE_CONFIG=./ansible/ansible.cfg ansible-playbook --inventory ./ansible/hosts --connection local
else
	ANSIBLE_CMD=env ANSIBLE_CONFIG=./ansible/ansible.cfg ansible --inventory ./ansible/hosts
	PLAYBOOK_CMD=env ANSIBLE_CONFIG=./ansible/ansible.cfg ansible-playbook --inventory ./ansible/hosts
endif

DOCKER_SERVICES = $(shell ls -1 ./dockerfiles)
# TODO remove
# DOCKER_SERVICES= \
# 	freeradius \
#  	pppoe \
#  	vpn-l2tp \
#  	vpn-strongswan \
#  	vpn-pptp \
#  	vpn-pptp-use-mppe \
#  	vpn-openvpn \
#  	vpn-openvpn-peap \
#  	vpn-openvpn-ttls \
#  	vpn-openconnect \
#  	vpn-vpnc \

all: 
	@echo "=> ERROR: need argument"
	@exit 1

prepare-fix-keys-perm:
	@echo "=> Fix identity file permission"
	chmod 0600 ./ansible/keys/id_rsa

prepare-ssh:
	@echo "=> NOTE: if failed, please edit /etc/ssh/sshd_config to enable option 'PermitRootLogin yes' in the ssh host side"
	$(PLAYBOOK_CMD) ./ansible/tasks/prepare_ssh.yaml

debug-ping:
	$(ANSIBLE_CMD) all -m ping
	$(ANSIBLE_CMD) all -a 'id'

debug-gather-facts:
	$(ANSIBLE_CMD) all -m setup

debug-list-services:
	@for s in $(DOCKER_SERVICES); do echo $$s; done

deploy-services: $(addprefix deploy-service-, $(DOCKER_SERVICES))

deploy-service-%:
	$(PLAYBOOK_CMD) ./ansible/tasks/deploy_docker_service.yaml --extra-vars "service_name=$(subst deploy-service-,,$(@))"

start-service-%:
	$(PLAYBOOK_CMD) ./ansible/tasks/start_docker_service.yaml --extra-vars "service_name=$(subst start-service-,,$(@))"

start-service-pppoe:
	$(PLAYBOOK_CMD) ./ansible/tasks/start_docker_service_pppoe.yaml

start-service-vpn-strongswan:
	$(PLAYBOOK_CMD) ./ansible/tasks/start_docker_service_vpn_strongswan.yaml

stop-service-%:
	$(PLAYBOOK_CMD) ./ansible/tasks/stop_docker_service.yaml --extra-vars "service_name=$(subst stop-service-,,$(@))"

test:
	echo TODO
