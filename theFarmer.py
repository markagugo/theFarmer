from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import WebDriverException
from argparse import ArgumentParser
import subprocess
from termcolor import colored, cprint
from art import *
import sys
import signal
import threading

def print_banner():
    banner = """
******************************************************************************************************************************
*  _________   ____  ____   _________         _________     __        _______      ____    ____   _________    _______       *
* |  _   _  | |_   ||   _| |_   ___  |       |_   ___  |   /  \      |_   __ \    |_   \  /   _| |_   ___  |  |_   __ \      *
* |_/ | | \_|   | |__| |     | |_  \_|         | |_  \_|  / /\ \       | |__) |     |   \/   |     | |_  \_|    | |__) |     *
*     | |       |  __  |     |  _|             |  _|     / ____ \      |  __ /      | |\  /| |     |  _|  _     |  __ /      *
*     | |_     _| |  | |_   _| |___/ |        _| |_    _/ /    \ \_   _| |  \ \_   _| |_\/_| |_   _| |___/ |   _| |  \ \_    *
*   |_____|   |____||____| |_________|_______|_____|  |____|  |____| |____| |___| |_____||_____| |_________|  |____| |___|   *
*                                                                                                                            *
* The_Farmer Ver. 1.0                                                                                                        *
* Coded by Mac Donald                                                                                                        *
* https://t.me/ploddertech                                                                                                   *
******************************************************************************************************************************
"""

    print("\033[34m" + banner + "\033[0m")

def flush_dns_cache():
    try:
        subprocess.run(['ipconfig', '/flushdns'], check=True)
        print("DNS cache flushed successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to flush DNS cache:", e)


def argParser():
    parser = ArgumentParser(description="The Farmer Tool [option] ", usage="python theFarmer.py --help",
                            epilog="[ Manual Mode ] python main.py -k [Keyword] "
                                   "-u [Url Extensions] -e [Webdriver Executable File Path] -o ['Output File Name.txt]")

    rparser = parser.add_argument_group("Required Arguments:")

    rparser.add_argument("-k", "--keyword", dest="Search_Keyword", help="Google Search Keyword(Eg--> Eckankar book download pdf)")
    rparser.add_argument("-u", "--urls", dest="Urls", help="Specific Urls to scrape from search(Eg--> .pdf, .png, @gmail.com') etc")
    rparser.add_argument("-e", "--exe", dest="extension", help="Chrome Driver exe file path (Eg--> C:\WebDriver\chromedriver.exe)")
    rparser.add_argument("-o", "--output", dest="output", help="Scraped Data File Path (Eg--> urls.txt)")

    args = parser.parse_args()
    return args


def start():
    args = argParser()
    if args.Search_Keyword and args.Urls and args.extension and args.output:
        try:
            urls = args.Urls.split(',')
            scrape_urls(args.Search_Keyword, urls, args.extension, args.output)
            flush_dns_cache()
        except Exception:
            scrape_urls(args.Search_Keyword, args.Urls, args.extension, args.output)
            flush_dns_cache()
            
    else:
        print(subprocess.call(["python", "theFarmer.py", "--h"], shell=True))


def scrape_specific_keywords(driver, specific_keywords, outputfile):
    try:
        for specific_keyword in specific_keywords:
            links_with_specific_keyword = driver.find_elements(By.XPATH, f"//a[contains(@href, '{specific_keyword}')]")
            
            for link in links_with_specific_keyword:
                url = link.get_attribute("href")
                with open(outputfile, "a") as f:
                    f.write(url + "\n")
                    
    except Exception:
        links_with_specific_keyword = driver.find_elements(By.XPATH, f"//a[contains(@href, '{specific_keywords}')]")
            
        for link in links_with_specific_keyword:
            url = link.get_attribute("href")
            with open(outputfile, "a") as f:
                f.write(url + "\n")
           
                    



def scrape_urls(keyword, specific_keywords, extension, outputfile):
    driver = webdriver.Chrome(executable_path=extension)

    driver.get("https://www.google.com")
    search_input = driver.find_element(By.NAME, "q")
    search_input.send_keys(keyword)
    search_input.submit()

    def signal_handler(signal, frame):
        driver.quit()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        try:
            search_results = driver.find_elements(By.CSS_SELECTOR, "div.yuRUbf a")
            urls_to_visit = [] 
            for link in search_results:
                url = link.get_attribute("href")
                if url not in urls_to_visit: 
                    urls_to_visit.append(url)

            for url in urls_to_visit:
                try:
                    driver.get(url)
                    scraping_thread = threading.Thread(target=scrape_specific_keywords, args=(driver, specific_keywords, outputfile))
                    scraping_thread.start()

                    start_time = time.time() 

                    while scraping_thread.is_alive(): 
                        elapsed_time = time.time() - start_time  

                        if elapsed_time >= 5:  
                            break

                        time.sleep(1)  

                    scraping_thread.join()  

                    driver.back()
                    time.sleep(2) 
                except WebDriverException:
                    continue
                except Exception:
                    continue

            

            next_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]")
            if next_button.is_displayed():
                next_button.click()
            else:
                break
        except Exception:
            continue
        except KeyboardInterrupt:
            driver.quit()
            flush_dns_cache()


print_banner()
start()