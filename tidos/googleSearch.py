import time
import sys, platform
from google import search
from time import sleep
###################################
class color:
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   ENDC = '\033[0m'
   BOLD = '\033[1m'
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
T  = '\033[93m' # tan
M = '\033[1;35;32m' # magenta
###################################
def googleSearch():
	if str(platform.system()) != "Linux":
		sys.exit(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "             You are not using a Linux Based OS! Linux is a must-have for this script!" + color.END)
	print ''
	print ''
	print ""+B+color.BOLD+"                                 _____   _____ _____  ___  ______  _____  _   _ "
	time.sleep(0.3)
	print ""+B+color.BOLD+"                                |  __ \ /  ___|  ___|/ _ \ | ___ \/  __ \| | | |"
	time.sleep(0.3)
	print ""+B+color.BOLD+"                                | |  \/ \ `--.| |__ / /_\ \| |_/ /| /  \/| |_| |"
	time.sleep(0.3)
	print ""+B+color.BOLD+"                                | | __   `--. \  __||  _  ||    / | |    |  _  |"
	time.sleep(0.3)
	print ""+B+color.BOLD+"                                | |_\ \ /\__/ / |___| | | || |\ \ | \__/\| | | |"
	time.sleep(0.3)
	print ""+B+color.BOLD+"                                 \____/ \____/\____/\_| |_/\_| \_| \____/\_| |_/"
	print ''
	print ''
	time.sleep(0.3)
	lol = raw_input(""+T+color.BOLD+"                                      QUERY :> " + color.END)
	print(""+M+color.BOLD+"                    Below are the list of websites with info on " +lol+ "" +color.END)
	for url in search(lol, tld='com', lang='es', stop=50):
		print(""+O+color.BOLD+"                    Info Sites Found :> "+W+"" + url)
