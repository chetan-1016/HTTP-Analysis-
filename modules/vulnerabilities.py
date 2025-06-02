from rich.console import Console
from rich.table import Table
from colorama import Fore

console = Console()

def scan_vulnerabilities(headers):
    """Scan for potential vulnerabilities based on HTTP headers."""
    vulnerabilities = []

    if headers.get("X-Content-Type-Options", "").lower() != "nosniff":
        vulnerabilities.append("X-Content-Type-Options is not set to 'nosniff'")

    if "Strict-Transport-Security" in headers:
        if "max-age=0" in headers["Strict-Transport-Security"]:
            vulnerabilities.append("Strict-Transport-Security max-age is set to 0")

    if "Content-Security-Policy" in headers:
        if "default-src 'self'" not in headers["Content-Security-Policy"]:
            vulnerabilities.append("Content-Security-Policy is not restrictive enough")

    if headers.get("X-Frame-Options", "").upper() not in ["DENY", "SAMEORIGIN"]:
        vulnerabilities.append("X-Frame-Options is not set to 'DENY' or 'SAMEORIGIN'")

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Vulnerability", style="cyan", justify="left")
    table.add_column("Issue", style="red")

    for vuln in vulnerabilities:
        table.add_row("Security Issue", vuln)

    if vulnerabilities:
        console.print(table)
    else:
        console.print(Fore.GREEN + "[+] No vulnerabilities detected based on HTTP headers.")
