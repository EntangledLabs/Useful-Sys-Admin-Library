import os, time

def install(package_name):
  os.system("apt-get install" + package_name + " -y")

def remove(package_name):
  os.system("apt-get remove" + package_name + " -y")

def update():
  os.system("apt-get update")

def upgrade():
  os.system("apt-get dist-upgrade -y")

def autoremove():
  os.system("apt-get autoremove -y")

def complete_sys_update():
  update()
  upgrade()
  autoremove()

