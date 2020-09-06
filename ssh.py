import paramiko
ssh = paramiko.SSHClient()
# Auto add host to known hosts
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Connect to server
ssh.connect("192.168.2.100", username="root", password="123456")
# Do command
(ssh_stdin, ssh_stdout, ssh_stderr) = ssh.exec_command("cat /etc/*-release")
# Get status code of command
exit_status = ssh_stdout.channel.recv_exit_status()
# Print status code
print ("exit status: %s" % exit_status)
# Print content
for line in ssh_stdout.readlines():
    print(line.rstrip())
# Close ssh connect
ssh.close()
