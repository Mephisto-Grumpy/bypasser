import os
import requests
import gratient
from colorama import Fore, Style

os.system('cls' if os.name == 'nt' else 'clear')

print(gratient.green("""
██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗███████╗██████╗ 
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗
██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗█████╗  ██████╔╝
██╔══██╗  ╚██╔╝  ██╔═══╝ ██╔══██║╚════██║╚════██║██╔══╝  ██╔══██╗
██████╔╝   ██║   ██║     ██║  ██║███████║███████║███████╗██║  ██║
╚═════╝    ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝"""))

print(gratient.green(f"""Supported websites:

[1] linkvertise.com
[2] adf.ly
[3] exe.io / exey.io / exee.io / exe.app / eio.io
[4] ouo.io / ouo.press
[5] adfoc.us
[6] bc.vc / bcvc.live
[7] fc.lc / fc-lc.com
[8] za.gl / zee.gl / za.uy
[9] cutt.ly
[+] and more...
"""))


print(gratient.green(
    f"""————————————————————————————————————————————————————————————————————"""))

try:
    inputURL = input(f"{Fore.GREEN}[+] {Style.RESET_ALL}Enter your link: ")
except KeyboardInterrupt:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(gratient.red(f"\n[!] Error, please try again later"))
    exit()
postURL = requests.post("https://api.bypass.vip/", json={"url": inputURL}, headers={
                        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36'})

result = gratient.green(f"""
Old link    : {postURL.json()['query']}
Method      : {postURL.json()['website']}
Bypass link : {postURL.json()['destination']}
""")
if postURL.status_code == 200:
    print(result)
else:
    print(gratient.red("Error, please try again later"))
