import paramiko
import time

# List of Fortigate devices and credentials
devices = [    {        "host": "192.168.1.10",        "username": "admin",        "password": "password",    },    {        "host": "192.168.1.11",        "username": "admin",        "password": "password",    }]

# SSH connection function
def ssh_connection(device):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(device['host'], username=device['username'], password=device['password'])
    return ssh

# Backup function
def backup(ssh, device):
    backup_filename = device['host'] + "_backup.conf"
    backup_command = "execute backup config " + backup_filename
    ssh.exec_command(backup_command)
    scp = ssh.open_sftp()
    scp.get(backup_filename, backup_filename)
    scp.close()

# Main loop
for device in devices:
    ssh = ssh_connection(device)
    backup(ssh, device)
    ssh.close()
