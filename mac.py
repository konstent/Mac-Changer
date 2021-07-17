import subprocess
import optparse
import re

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify any interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify mac addrs, use --help for more info.")
    else:
        return options

def change_mac(interface, new_mac):
    print("[+] Changing Mac Address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_addrs_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_addrs_search_result:
        return mac_addrs_search_result.group(0)
    else:
        print("[-] Could not read mac address.")

options = get_args()
current_mac = get_current_mac(options.interface)
print("Current_Mac = " + str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if (current_mac == options.new_mac):
    print("[+] Mac_addrs is successfully changed to " + current_mac)
else:
    print("[-] Mac_addrs did not get changed")

