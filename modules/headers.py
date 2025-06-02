import requests
from rich.console import Console
from rich.table import Table

console = Console()

def fetch_headers(url, return_text=False):
    """Fetch HTTP headers for a given URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        if return_text:
            return response.headers, response.text
        return response.headers
    except requests.RequestException as e:
        console.print(f"[bold red][!] Error retrieving headers: {e}[/bold red]")
        return None

def display_headers(headers):
    """Display HTTP headers in a formatted table."""
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Header", style="cyan", justify="left")
    table.add_column("Value", style="green")

    for header, value in headers.items():
        table.add_row(header, value)

    console.print(table)
