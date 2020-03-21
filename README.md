I set up this project to print out which IP address from house is given to Raspberry Pi.
This helps to get recent address.
Next script let me publish random page from italian wikipedia.
I also put this script in crontab to be ran at reboot.
Cron line would be like 
@reboot /urs/bin/python /home/pi/pi4tweeterbot/updateTwitterStatus.py &

Prerequisites:
- raspberry pi4 with full raspian install
- pi account with sudo 
- twitter account
- twitter for dev enabled

Steps to use it:
- run install_dependencies.sh
- create custom file myconf.py with twitter credentials and secrets
- launch run.sh
