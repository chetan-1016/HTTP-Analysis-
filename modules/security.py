from rich.console import Console
from rich.table import Table
from colorama import Fore

console = Console()

def analyze_security_headers(headers):
    """Analyze security headers and check if they are properly configured."""
    security_headers = {
        "Content-Security-Policy": "Not Set",
        "Strict-Transport-Security": "Not Set",
        "X-Content-Type-Options": "Not Set",
        "X-Frame-Options": "Not Set",
        "X-XSS-Protection": "Not Set",
        "Referrer-Policy": "Not Set",
        "Permissions-Policy": "Not Set"
    }

    for header in security_headers:
        if header in headers:
            security_headers[header] = "Configured"

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Security Header", style="cyan", justify="left")
    table.add_column("Status", style="green")

    for header, status in security_headers.items():
        table.add_row(header, status)

    console.print(table)

    missing = [header for header, status in security_headers.items() if status == "Not Set"]
    if missing:
        console.print(Fore.YELLOW + f"[!] Missing Security Headers: {', '.join(missing)}")
    else:
        console.print(Fore.GREEN + "[+] All critical security headers are properly configured.")
