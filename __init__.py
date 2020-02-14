import crack
import webfox

'''
how to start monitor mode

sudo airmon-ng
//this will give the interface, wlan1 will be the card you are putting in monitor mode
sudo airmon-ng start wlan1
//this might give error and you have to run 'airmon-ng check kill' first, then this command
sudp airodump-ng start wlan1mon
//this starts the sniffer, but we need to turn on the wifi
// to do this, when you first ran the airmon-ng start wlan1, what processes were going to get killed?
// restart those processes, in my case
sudo service wpa_supplicant restart 
sudo service dhcpcd restart
sudo service avahi-daemon restart
// this should restart the wifi
sudo airodump-ng -w testermaker --output-format csv wlan1mon
//this will make the .csv file and write to it "testermaker" is the name of the file

alias python='/usr/bin/python3.4'
$ . ~/.bashrc

'''