# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  #config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  config.vm.network "forwarded_port", guest: 8080, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder "./ebook", "/opt/ebook", type: "rsync", rsync__exclude: "[.git, .vagrant]"
  config.vm.synced_folder "./scripts", "/opt/ebook/scripts", type: "rsync", rsync__exclude: "[.git, .vagrant]"
  config.vm.synced_folder "./config", "/opt/ebook/config", type: "rsync", rsync__exclude: "[.git, .vagrant]"



  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
     # Display the VirtualBox GUI when booting the machine
     # vb.gui = true
  
     vb.name = "Vinay's Ebook Development Environment"

     # Customize the amount of memory on the VM:
     vb.memory = "1024"
   end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
   config.vm.provision "shell", inline: <<-SHELL

     # Install some common utilities
     yum -y install vim

     # Install Mongo repo and package
     cp -v /opt/ebook/config/mongodb.repo /etc/yum.repos.d/mongodb.repo
     yum install -y mongo-10gen mongo-10gen-server
     systemctl start mongod 
     systemctl enable mongod

     # Install python
     yum -y install python

     # Install pip
     curl "https://bootstrap.pypa.io/get-pip.py" -o "/tmp/get-pip.py"
     python2 /tmp/get-pip.py

     # Install pymongo
     pip install pymongo

     # Install java and maven
     yum install -y maven     

     # Populate mongoDB
     /opt/ebook/scripts/bootstrap-dev.sh

  #   apt-get update
  #   apt-get install -y apache2
   SHELL
end
