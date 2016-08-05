# SERVER_ADDR is the ssh host address that to deploy pppoe/vpn services
SERVER_ADDR=

# ROUTER_ADDR is the OpenWRT router address that to deploy freeradius service
ROUTER_ADDR=

# ANSIBLE_LOCAL control if ansible use local connection type instead
# of ssh which means SERVER_ADDR and ROUTER_ADDR will be dropped, for
# example if want deploy services local just run like "sudo make
# deploy-server ANSIBLE_LOCAL=1"
ANSIBLE_LOCAL=
ifdef ANSIBLE_LOCAL
	ANSIBLE_CMD=env ANSIBLE_CONFIG=./ansible.cfg ansible --inventory ./hosts --connection local
	PLAYBOOK_CMD=env ANSIBLE_CONFIG=./ansible.cfg ansible-playbook --inventory ./production --connection local
else
	ANSIBLE_CMD=env ANSIBLE_CONFIG=./ansible.cfg ansible --inventory ./hosts
	PLAYBOOK_CMD=env ANSIBLE_CONFIG=./ansible.cfg ansible-playbook --inventory ./production
endif

SERVICES= \
	freeradius \
	pppoe \
	vpn-l2tp \
	vpn-strongswan \
	vpn-pptp \
	vpn-pptp-use-mppe \
	vpn-openvpn \
	vpn-openvpn-peap \
	vpn-openvpn-ttls \
	vpn-openconnect \
	vpn-vpnc \

all: 
	@echo "=> ERROR: need argument"
	@exit 1

prepare-ssh:
	@echo "=> fix identity file permission"
	chmod 600 ./keys/id_rsa*
	@echo "=> copy public ssh key to remote host"
ifdef SERVER_ADDR
	ssh-copy-id -i ./keys/id_rsa.pub root@$(SERVER_ADDR)
endif
ifdef ROUTER_ADDR
	ssh-copy-id -i ./keys/id_rsa.pub root@$(ROUTER_ADDR)
endif
	@echo "=> NOTE: if failed, please edit /etc/ssh/sshd_config to enable option 'PermitRootLogin yes' in the ssh host side"

debug-ping:
	$(ANSIBLE_CMD) all -m ping
	$(ANSIBLE_CMD) all -a 'echo hello'

deploy-server: $(addprefix deploy-service-, ${SERVICES})

deploy-router:
	echo TODO hello
# setup-router-openwrt:

deploy-service-%:
	echo $(subst deploy-service-,,$(@))

start-service-%:
	echo $(subst start-service-,,$(@))

stop-service-%:
	echo $(subst stop-service-,,$(@))
