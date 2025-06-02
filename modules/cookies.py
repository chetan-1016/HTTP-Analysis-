from rich.console import Console
from rich.table import Table
from colorama import Fore

console = Console()

def analyze_cookies(headers):
    """Analyze cookies for security attributes."""
    cookies = headers.get("Set-Cookie")
    if not cookies:
        console.print(Fore.YELLOW + "[!] No cookies found.")
        return

    console.print(Fore.YELLOW + "[*] Analyzing cookies for security flags...")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Cookie", style="cyan", justify="left")
    table.add_column("Attributes", style="green")

    cookies = cookies.split(',')
    for cookie in cookies:
        cookie = cookie.strip()
        parts = cookie.split(';')
        name_value = parts[0]
        attributes = [attr.strip() for attr in parts[1:]]
        security_flags = []

        for attr in attributes:
            if attr.lower() == "secure":
                security_flags.append("Secure")
            if attr.lower() == "httponly":
                security_flags.append("HttpOnly")
            if attr.lower().startswith("samesite"):
                security_flags.append(attr)

        table.add_row(name_value, ", ".join(security_flags) if security_flags else "None")

    console.print(table)
