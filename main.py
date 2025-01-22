import requests
import re
import os
import random
from datetime import datetime
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from socket import socket, AF_INET, SOCK_STREAM
from colorama import Fore, Style, init


init(autoreset=True)


SCRAPE_TIMEOUT = 15
CHECK_TIMEOUT = 7.0
MAX_THREADS_CHECK = 150
RESULTS_DIR = "results"
IP_PORT_REGEX = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}:\d{2,5}\b")


# Fungsi untuk membersihkan terminal
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


# Coder by KianSantang777
def show_logo():
    print(f"""{Fore.LIGHTGREEN_EX}
             _    _ _                _                                      
            | |  / |_)              | |               _                     
            | | / / _  ____ ____     \ \   ____ ____ | |_  ____ ____   ____ 
            | |< < | |/ _  |  _ \     \ \ / _  |  _ \|  _)/ _  |  _ \ / _  |
            | | \ \| ( ( | | | | |_____) | ( | | | | | |_( ( | | | | ( ( | |
            |_|  \_)_|\_||_|_| |_(______/ \_||_|_| |_|\___)_||_|_| |_|\_|| |
                                                                     (_____|
           {Fore.LIGHTBLUE_EX}Version 1.0 Proxy Scraper + Checker{Style.RESET_ALL}
           {Fore.LIGHTBLUE_EX}Author: Kian Santang 777{Style.RESET_ALL}
           {Fore.LIGHTBLUE_EX}Github: github.com/KianSantang777{Style.RESET_ALL}
    """)

def read_source_file(filename="source.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}[✗] File {filename} tidak ditemukan!{Style.RESET_ALL}")
        exit(1)

# recoding this source will not make you a pro . Respect the code owner and use it for free
# Telegram : https://t.me/Xqndrs666
# Channel Telegram : https://t.me/Officialcendol666
# https://t.me/+JunckG--7B4zMjI1
# Facebook : https://www.facebook.com/mtaufiqqhdyt

# Fungsi scraping URL
def scrape_page(url):
    try:
        response = requests.get(url, timeout=SCRAPE_TIMEOUT)
        response.raise_for_status()
        proxies = set(IP_PORT_REGEX.findall(response.text))
        return proxies
    except requests.RequestException as e:
        print(f"{Fore.RED}[!] Error scraping URL {url}: {e}{Style.RESET_ALL}")
        return set()

# recoding this source will not make you a pro . Respect the code owner and use it for free
# Telegram : https://t.me/Xqndrs666
# Channel Telegram : https://t.me/Officialcendol666
# https://t.me/+JunckG--7B4zMjI1
# Facebook : https://www.facebook.com/mtaufiqqhdyt

# Fungsi utama scraping semua sumber
def scrape_all_sources(sources):
    all_proxies = set()
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(scrape_page, source): source for source in sources}
        with tqdm(total=len(futures), desc="Scraping", colour="cyan") as pbar:
            for future in as_completed(futures):
                all_proxies.update(future.result())
                pbar.update(1)
    return all_proxies


# Fungsi filter proxy berdasarkan jenis
def filter_proxies_by_type(proxies, proxy_type):
    types = {
        "1": "HTTP",
        "2": "HTTPS",
        "3": "SOCKS4",
        "4": "SOCKS5"
    }
    if proxy_type == "1":  # Contoh untuk menyaring tipe berbasis kata
        return {proxy for proxy in proxies if "http" in proxy.lower()}
    return proxies

# recoding this source will not make you a pro . Respect the code owner and use it for free
# Telegram : https://t.me/Xqndrs666
# Channel Telegram : https://t.me/Officialcendol666
# https://t.me/+JunckG--7B4zMjI1
# Facebook : https://www.facebook.com/mtaufiqqhdyt

# Fungsi untuk mengecek apakah proxy aktif (live)
def check_proxy(proxy, proxy_type):
    ip, port = proxy.split(":")
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(CHECK_TIMEOUT)
    try:
        sock.connect((ip, int(port)))
        sock.close()
        return proxy, True
    except:
        return proxy, False


# Fungsi untuk mengecek semua proxy
def check_all_proxies(proxies, proxy_type="1"):
    live_proxies = []
    dead_proxies = []
    with ThreadPoolExecutor(max_workers=MAX_THREADS_CHECK) as executor:
        futures = {executor.submit(check_proxy, proxy, proxy_type): proxy for proxy in proxies}
        with tqdm(total=len(futures), desc="Checking Proxies", colour="green") as pbar:
            for future in as_completed(futures):
                proxy, is_live = future.result()
                if is_live:
                    live_proxies.append(proxy)
                else:
                    dead_proxies.append(proxy)
                pbar.update(1)
    return live_proxies, dead_proxies

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    clear_terminal()
    show_logo()

    sources = read_source_file()
    print(f"{Fore.CYAN}[+] Source Urls: {len(sources)}{Style.RESET_ALL}")

    # recoding this source will not make you a pro . Respect the code owner and use it for free
    # Telegram : https://t.me/Xqndrs666
    # Channel Telegram : https://t.me/Officialcendol666
    # https://t.me/+JunckG--7B4zMjI1
    # Facebook : https://www.facebook.com/mtaufiqqhdyt
    print(f"{Fore.GREEN}\n[1] HTTP\n[2] HTTPS\n{Fore.MAGENTA}[3] SOCKS4\n[4] SOCKS5{Style.RESET_ALL}")
    proxy_type = input("Choose type proxy: ").strip() # Coder by KianSantang777
    print('\n')

    print(f"{Fore.YELLOW}[+] Start scraping…{Style.RESET_ALL}")
    all_proxies = scrape_all_sources(sources) # Coder by KianSantang777

    filtered_proxies = filter_proxies_by_type(all_proxies, proxy_type) # Coder by KianSantang777
    print(f"{Fore.GREEN}[✓] Total proxy success saved! ({proxy_type}): {len(filtered_proxies)}{Style.RESET_ALL}")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(RESULTS_DIR, exist_ok=True)
    scrape_filename = os.path.join(RESULTS_DIR, f"{proxy_type}_proxies_{timestamp}.txt")
    with open(scrape_filename, "w") as file:
        file.write("\n".join(filtered_proxies))

    check_choice = input("\nIngin melanjutkan ke tahap pemeriksaan proxy? (Y/N): ").strip().lower()
    if check_choice == "y":
        print(
            f"{Fore.YELLOW}[+] Memulai pemeriksaan proxy dengan timeout {CHECK_TIMEOUT}s dan {MAX_THREADS_CHECK} threads.{Style.RESET_ALL}")
        live_proxies, dead_proxies = check_all_proxies(filtered_proxies, proxy_type)

        # Simpan hasil proxy live
        live_filename = os.path.join(RESULTS_DIR, f"live_{proxy_type}_proxies_{timestamp}.txt")
        with open(live_filename, "w") as file:
            file.write("\n".join(live_proxies))
        print(f"{Fore.GREEN}[✓] Proxy live disimpan di: {live_filename}{Style.RESET_ALL}")

        # Statistik
        print(f"{Fore.GREEN}[LIVE] Total proxy live: {len(live_proxies)}{Style.RESET_ALL}")
        print(f"{Fore.RED}[DIE] Total proxy die: {len(dead_proxies)}{Style.RESET_ALL}")
    else: # recoding this source will not make you a pro . Respect the code owner and use it for free
    # Coder by KianSantang777
        print(f"{Fore.CYAN}[✓] Proses selesai tanpa pemeriksaan proxy.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
