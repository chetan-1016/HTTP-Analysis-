from rich.console import Console
from colorama import Fore

console = Console()

def detect_frameworks(response_text):
    """Detect popular web frameworks based on HTML content."""
    frameworks = {
        "WordPress": "wp-content",
        "Joomla": "Joomla!",
        "Drupal": "Drupal.settings",
        "Django": "csrftoken",
        "Magento": "Mage",
        "Shopify": "shopify",
        "Webflow": "w-webflow-badge",
        "Ruby on Rails": "Rails",
        "Laravel": "laravel_session"

    }

    detected = []
    for framework, signature in frameworks.items():
        if signature in response_text:
            detected.append(framework)

    if detected:
        console.print(Fore.GREEN + f"[+] Detected Frameworks: {', '.join(detected)}")
    else:
        console.print(Fore.YELLOW + "[!] No common frameworks detected.")
