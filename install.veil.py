import subprocess
subprocess.call("apt update",shell=True)
subprocess.call("apt install -y mitmproxy",shell=True)
subprocess.call("apt install -y veil",shell=True)
subprocess.call("/usr/share/veil/config/setup.sh --force --silent",shell=True)
subprocess.call("apt install -y gnome-shell-extension-dashtodock",shell=True)
subprocess.call("sed -i.bak 's/# disable-user-list=true/disable-user-list=true/g' /etc/gdm3/greeter.dconf-defaults",shell=True)
