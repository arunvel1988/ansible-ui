FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && \
    apt-get install -y openssh-server sudo python3 curl && \
    mkdir /var/run/sshd

# Create 'arun' user with password 'arun'
RUN useradd -m -s /bin/bash arun && \
    echo 'arun:arun' | chpasswd && \
    echo 'arun ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# SSH key permission fix and start SSH service
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
