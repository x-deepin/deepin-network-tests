# ANSIBLE_LOCAL control if ansible use local connection type instead
# of ssh, for example if want deploy services local just run like
# "sudo make deploy_services ANSIBLE_LOCAL=1"
ANSIBLE_LOCAL=
ifdef ANSIBLE_LOCAL
	ANSIBLE_CMD=env ANSIBLE_CONFIG=./ansible.cfg ansible --inventory ./hosts --connection local
	PLAYBOOK_CMD=env ANSIBLE_CONFIG=./ansible.cfg ansible-playbook --inventory ./hosts --connection local
else
	ANSIBLE_CMD=env ANSIBLE_CONFIG=./ansible.cfg ansible --inventory ./hosts
	PLAYBOOK_CMD=env ANSIBLE_CONFIG=./ansible.cfg ansible-playbook --inventory ./hosts
endif

SERVICES= \
	freeradius \
	pppoe \
	vpn_l2tp \
	vpn_strongswan \
	vpn_pptp \
	vpn_pptp_use_mppe \
	vpn_openvpn \
	vpn_openvpn_peap \
	vpn_openvpn_ttls \
	vpn_openconnect \
	vpn_vpnc \

all: 
	@echo "=> ERROR: need argument"
	@exit 1

prepare_ssh:
	@echo "=> NOTE: if failed, please edit /etc/ssh/sshd_config to enable option 'PermitRootLogin yes' in the ssh host side"
	$(PLAYBOOK_CMD) ./tasks/prepare_ssh.yaml

debug_ping:
	$(ANSIBLE_CMD) all -m ping
	$(ANSIBLE_CMD) all -a 'id'

debug_list_services:
	@for s in $(SERVICES); do echo $$s; done

deploy_services: $(addprefix deploy_service_, $(SERVICES))

deploy_service_%:
	echo TODO
	echo $(subst deploy_service_,,$(@))

start_service_%:
	echo TODO
	echo $(subst start_service_,,$(@))

stop_service_%:
	echo TODO
	echo $(subst stop_service_,,$(@))

test:
	echo TODO
