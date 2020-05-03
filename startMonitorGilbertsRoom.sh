screen -d -m sudo airodump-ng -w outputSniffGilbertsRoom --output-format csv wlan0mon
screen -d -m python3 update_db_GilbertsRoom.py