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

all: 
	@echo "=> ERROR: need argument"
	@exit 1

list-services:
	@for s in $(DOCKER_SERVICES); do echo $$s; done

get-ansible-server-host:
	@$(ANSIBLE_CMD) server --list-hosts | sed 1d | head -1 | sed 's/^ \+//'

prepare-fix-keys-perm:
	@echo "=> Fix identity file permission"
	chmod 0600 ./ansible/keys/id_rsa

prepare-ssh:
	@echo "=> NOTE: if failed, please edit /etc/ssh/sshd_config to enable option 'PermitRootLogin yes' in the ssh host side"
	$(PLAYBOOK_CMD) ./ansible/tasks/prepare_ssh.yml

debug-ping:
	$(ANSIBLE_CMD) all -m ping
	$(ANSIBLE_CMD) all -a 'id'

debug-gather-facts:
	$(ANSIBLE_CMD) all -m setup

debug-router-show-wireless-ssid:
	$(PLAYBOOK_CMD) ./ansible/tasks/router_show_wireless_ssid.yml

deploy-services: $(addprefix deploy-service-, $(DOCKER_SERVICES))

deploy-service-%:
	$(PLAYBOOK_CMD) ./ansible/tasks/deploy_docker_service.yml --extra-vars "service_name=$(subst deploy-service-,,$(@))"

start-service-%:
	$(PLAYBOOK_CMD) ./ansible/tasks/start_docker_service.yml --extra-vars "service_name=$(subst start-service-,,$(@))"

start-service-pppoe:
	$(PLAYBOOK_CMD) ./ansible/tasks/start_docker_service_pppoe.yml

start-service-vpn-strongswan:
	$(PLAYBOOK_CMD) ./ansible/tasks/start_docker_service_vpn_strongswan.yml

stop-service-%:
	$(PLAYBOOK_CMD) ./ansible/tasks/stop_docker_service.yml --extra-vars "service_name=$(subst stop-service-,,$(@))"

router-save-wireless-settings:
	$(PLAYBOOK_CMD) ./ansible/tasks/router_save_wireless_settings.yml

router-restore-wireless-settings:
	$(PLAYBOOK_CMD) ./ansible/tasks/router_restore_wireless_settings.yml

router-reload-network:
	$(PLAYBOOK_CMD) ./ansible/tasks/router_reload_network.yml

router-setup-wireless-wep:
	$(PLAYBOOK_CMD) ./ansible/tasks/router_setup_wireless_wep.yml

router-setup-wireless-wpa-psk:
	$(PLAYBOOK_CMD) ./ansible/tasks/router_setup_wireless_wpa_psk.yml

router-setup-wireless-wpa-eap:
	$(PLAYBOOK_CMD) ./ansible/tasks/router_setup_wireless_wpa_eap.yml

run-tests:
	@echo "for special test suit, please run ./test_network_xxx.py or python3 -m unittest test_network_xxx.TestClaass.test_method"
	./tests/main.py
