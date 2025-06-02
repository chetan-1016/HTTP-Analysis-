import os
import sys
from colorama import Fore, init, Style                                                                                                                          
from modules.headers import fetch_headers, display_headers
from modules.security import analyze_security_headers
from modules.server import identify_server_technology
from modules.vulnerabilities import scan_vulnerabilities
from modules.cookies import analyze_cookies
from modules.frameworks import detect_frameworks
from tabulate import tabulate 

init(autoreset=True)

def banner():
    print(Fore.GREEN + """
                    ────────────────────────────────────────
                     🚀 HTTP Header & Security Analyzer 🚀
                    ────────────────────────────────────────
                      [*] Author  : Chetan
                      [*] Usage   : Analyze HTTP headers!!!

  """ + Fore.MAGENTA + """\
║ The HTTP Header Analyzer is a powerful tool designed to                      ║
║ help you understand how a website communicates behind the scenes. It         ║
║ fetches and displays HTTPS headers, analyzes important security headers,     ║
║ scans for common vulnerabilities, and identifies server technologies.        ║
║ Additionally, it inspects cookies for potential risks and detects the        ║
║ underlying web framework used by the site. Whether you're a cybersecurity    ║
║ enthusiast or just getting started, this tool gives you deep insights into   ║
║ a website’s HTTP response in a clear and structured way.                     ║
╚══════════════════════════════════════════════════════════════════════════════╝
""" + Style.RESET_ALL)

def menu():
    print(Fore.BLUE + "📋 Available Options:\n")

    options = [
        ("1", "Fetch & Display HTTP Headers"),
        ("2", "Analyze Security Headers"),
        ("3", "Identify Server Technology"),
        ("4", "Scan for Vulnerabilities"),
        ("5", "Analyze Cookies"),
        ("6", "Detect Web Frameworks"),
        ("0", "Exit")
    ]

    print(Fore.CYAN + tabulate(options, headers=["Option", "Description"], tablefmt="fancy_grid"))

def main():
    try:
        while True:
            print("\033c", end="")  
            banner()
            menu()
            choice = input(Fore.YELLOW + "\n[*] Select an option: ").strip()

            if choice == "1":
                url = input(Fore.YELLOW + "[*] Enter target URL: ").strip()
                headers = fetch_headers(url)
                if headers:
                    display_headers(headers)

            elif choice == "2":
                url = input(Fore.YELLOW + "[*] Enter target URL: ").strip()
                headers = fetch_headers(url)
                if headers:
                    analyze_security_headers(headers)

            elif choice == "3":
                url = input(Fore.YELLOW + "[*] Enter target URL: ").strip()
                headers = fetch_headers(url)
                if headers:
                    identify_server_technology(headers)

            elif choice == "4":
                url = input(Fore.YELLOW + "[*] Enter target URL: ").strip()
                headers = fetch_headers(url)
                if headers:
                    scan_vulnerabilities(headers)

            elif choice == "5":
                url = input(Fore.YELLOW + "[*] Enter target URL: ").strip()
                headers = fetch_headers(url)
                if headers:
                    analyze_cookies(headers)

            elif choice == "6":
                url = input(Fore.YELLOW + "[*] Enter target URL: ").strip()
                headers, response_text = fetch_headers(url, return_text=True)
                if headers:
                    detect_frameworks(response_text)

            elif choice == "0":
                print(Fore.RED + "\n[!] Exiting...")
                input(Fore.CYAN + "[Press Enter to exit...]")
                break

            else:
                print(Fore.RED + "[!] Invalid option! Try again.")

            input(Fore.CYAN + "\n[Press Enter to continue...]")

    except KeyboardInterrupt:
        print(Fore.RED + "\n\n[!] Interrupted by user.")
        input(Fore.CYAN + "[Press Enter to exit...]")
        sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.RED + f"\n[!] An unexpected error occurred: {e}")
        input(Fore.CYAN + "[Press Enter to exit...]")
