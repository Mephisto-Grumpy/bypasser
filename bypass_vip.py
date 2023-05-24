import requests
import gratient
from cachetools import LRUCache, cached

cache = LRUCache(maxsize=100)


class BypassVip:
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36'}

    def print_header(self):
        print(gratient.green("""
        ██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗███████╗██████╗
        ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗
        ██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗█████╗  ██████╔╝
        ██╔══██╗  ╚██╔╝  ██╔═══╝ ██╔══██║╚════██║╚════██║██╔══╝  ██╔══██╗
        ██████╔╝   ██║   ██║     ██║  ██║███████║███████║███████╗██║  ██║
        ╚═════╝    ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝"""))

    def print_supported_websites(self):
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

    @cached(cache)
    def post_url(self, url):
        try:
            response = requests.post(
                "https://api.bypass.vip/", json={"url": url}, headers=self.headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Something went wrong: ", err)
        return response

    def print_result(self, result_json):
        result = gratient.green(f"""
        Old link    : {result_json['query']}
        Method      : {result_json['website']}
        Bypass link : {result_json['destination']}
        """)
        print(result)
        pass

    def print_error(self, error_message):
        print(gratient.red(f"\n[!] {error_message}"))
        pass
