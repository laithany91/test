USERNAME=admin
HOSTS="192.168.1.1"
SCRIPT="en; configure object_setting; ip_object add test10"
for HOSTNAME in ${HOSTS} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
done
