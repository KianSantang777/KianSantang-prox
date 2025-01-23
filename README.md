<center>
<h3 align="center"><b>Proxy Scrapper & Grabber Version 1.0</b></h3><br>

![plastic](https://img.shields.io/badge/Language-Python_3.13.1-blue) 


<img src="https://raw.githubusercontent.com/KianSantang777/KianSantang-prox/refs/heads/main/mainmenu.jpg" /></a>
</center>
<br>

**KIAN SANTANG: Proxy Scraper + Checker** is a Python script designed to scrape proxy lists from multiple sources, filter proxies by type (HTTP, HTTPS, SOCKS4, SOCKS5), and check their availability (live or dead).

## Features
1. **Scrape Proxies**: Automatically grab proxy lists from a set of provided URLs (`source.txt` file).
2. **Filter by Type**: Filter proxies into specific types (HTTP, HTTPS, SOCKS4, SOCKS5).
3. **Check Proxy Status**: Test proxies to determine if they are live or dead.
4. **Save Results**: Automatically save scraped and checked proxy data into the `results` directory.

## How It Works
1. Add your list of proxy source URLs to the file `source.txt` (one URL per line) or leave blank if you want to use the default source.
2. Run the script.
3. Choose the type of proxy you'd like to filter (HTTP, HTTPS, SOCKS4, SOCKS5).
4. The script will scrape proxies, filter them, and save the results to a timestamped file.
5. Optionally, continue to test whether the proxies are live or not.

## How to Use
1. **Clone/Download**:
   - Download this repo or clone in terminal:
       ```bash
       git clone https://github.com/KianSantang777/KianSantang-prox.git
       ```
       
2. **Setup**:
   - Install the necessary dependencies by running:
     ```bash
     pip install requests tqdm colorama
     ```
   - Ensure the `source.txt` file is in the same directory as the script, containing URLs to scrape proxies from.
   
3. **Run the Script**:
   - Execute the script with:
     ```bash
     python main.py
     ```
   - Follow the on-screen prompts:
     - Choose the proxy type you want (HTTP, HTTPS, SOCKS4, SOCKS5).
     - Proceed to the optional step to check the proxies.

4. **Output**:
   - Scraped proxies will be saved in the `results` directory:
     - e.g., `1_proxies_YYYYMMDD_HHMMSS.txt` (filtered by type).
     - e.g., `live_1_proxies_YYYYMMDD_HHMMSS.txt` (after the live check).
