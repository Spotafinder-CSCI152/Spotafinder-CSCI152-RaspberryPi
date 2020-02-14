# import logging
# import util
import subprocess
# ariodump_ng = util.which('airodump-ng')
# aircrack_ng = util.which('aircrack-ng')
# airmon_ng = util.which('airmon-ng')
# wifite = util.which('wifite')

airmon_ngCheck = "airmon_ng check kill"
airmon_ngStart = "airmon_ng start wlan1"
restartWPA = "service wpa_supplicant restart"
restartdhcpcd = "service dhcpcd restart"
restartAvahi = "service avahi-daemon restart"
airodump_ng = "airodump_ng -w sendMetoFirebae --output-format csv wlan1mon"

# bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"
# import subprocess
# process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
# output, error = process.communicate()