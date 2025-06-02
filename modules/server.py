from rich.console import Console
from rich.table import Table
from colorama import Fore

console = Console()

def identify_server_technology(headers):
    """Identify server technology based on the 'Server' header."""
    server = headers.get("Server", "Unknown")
    technology = "Unknown"

    if "nginx" in server.lower():
        technology = "Nginx Web Server"
    elif "apache" in server.lower():
        technology = "Apache Web Server"
    elif "iis" in server.lower():
        technology = "Microsoft IIS"
    elif "cloudflare" in server.lower():
        technology = "Cloudflare CDN"

    console.print(Fore.YELLOW + "[*] Detecting server technology...")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Server", style="cyan", justify="left")
    table.add_column("Detected Technology", style="green")
    table.add_row(server, technology)
    console.print(table)
