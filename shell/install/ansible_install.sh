#!/bin/bash

# Exit on error
set -e

HOSTS_FILE="hosts.txt"

# Step 1: Install Ansible (Debian/Ubuntu)
echo "[INFO] Installing Ansible and sshpass..."
sudo apt update -y
sudo apt install -y ansible sshpass

# Step 2: Generate SSH keys if not exist
if [ ! -f "$HOME/.ssh/id_rsa.pub" ]; then
    echo "[INFO] Generating SSH keys..."
    ssh-keygen -t rsa -b 4096 -N "" -f "$HOME/.ssh/id_rsa"
else
    echo "[INFO] SSH keys already exist. Skipping key generation."
fi

# Step 3: Read hosts.txt and configure
if [ ! -f "$HOSTS_FILE" ]; then
    echo "[ERROR] $HOSTS_FILE not found. Please create it with 'IP hostname' per line."
    exit 1
fi

echo "[INFO] Processing hosts from $HOSTS_FILE..."

while read -r IP HOSTNAME; do
    if [ -z "$IP" ] || [ -z "$HOSTNAME" ]; then
        continue
    fi

    echo "[INFO] Adding $IP $HOSTNAME to /etc/hosts..."
    if ! grep -q "$IP $HOSTNAME" /etc/hosts; then
        echo "$IP $HOSTNAME" | sudo tee -a /etc/hosts > /dev/null
    fi

    echo "[INFO] Copying SSH key to $HOSTNAME ($IP)..."
    ssh-copy-id -o StrictHostKeyChecking=no "$USER@$IP"

done < "$HOSTS_FILE"

echo "[INFO] Setup complete. You can now use Ansible!"
