import sys
import socket
import webbrowser
from urllib.parse import urlparse
import requests
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from rich.console import Console
from rich.panel import Panel

console = Console()

def banner():
    console.print(Panel(
        "[bold red]HACKME SUITE - OSINT & RECON PLATFORM[/bold red]\n"
        "[cyan]Developer: Vedansh Srivastava | Educational Security & Recon Tool[/cyan]",
        border_style="yellow"
    ))

def phone_osint():
    console.print("\n[yellow][*] Phone Number OSINT Module[/yellow]")
    raw_num = console.input("Enter phone number with country code (e.g., +919876543210): ")
    try:
        parsed = phonenumbers.parse(raw_num, None)
        if not phonenumbers.is_valid_number(parsed):
            console.print("[red][-] Invalid phone number format.[/red]")
            return
        region = geocoder.description_for_number(parsed, "en")
        sim_carrier = carrier.name_for_number(parsed, "en")
        tz = timezone.time_zones_for_number(parsed)
        
        console.print(f"[green][+] Valid Number  :[/green] True")
        console.print(f"[green][+] Region/Country:[/green] {region or 'Unknown'}")
        console.print(f"[green][+] Carrier/ISP   :[/green] {sim_carrier or 'Unknown'}")
        console.print(f"[green][+] Timezone      :[/green] {', '.join(tz)}")
    except Exception as e:
        console.print(f"[red][-] Error parsing number: {e}[/red]")

def web_recon():
    console.print("\n[yellow][*] Web Target Information & Recon[/yellow]")
    target = console.input("Enter target domain or URL (e.g., example.com): ")
    domain = urlparse(target).netloc if "://" in target else target.split("/")[0]
    
    try:
        ip = socket.gethostbyname(domain)
        console.print(f"[green][+] Target Domain :[/green] {domain}")
        console.print(f"[green][+] Public IP     :[/green] {ip}")
        
        geo = requests.get(f"https://ipapi.co/{ip}/json/", timeout=5).json()
        console.print(f"[green][+] Location      :[/green] {geo.get('city')}, {geo.get('country_name')}")
        console.print(f"[green][+] Hosting/ISP   :[/green] {geo.get('org')}")
        
        url = f"https://{domain}" if not target.startswith("http") else target
        resp = requests.get(url, timeout=5)
        console.print(f"[green][+] HTTP Status   :[/green] {resp.status_code}")
        console.print(f"[green][+] Server Header :[/green] {resp.headers.get('Server', 'Hidden')}")
    except Exception as e:
        console.print(f"[red][-] Recon failed: {e}[/red]")

def email_osint():
    console.print("\n[yellow][*] Email Footprint Check[/yellow]")
    email = console.input("Enter target email address: ")
    if "@" not in email:
        console.print("[red][-] Invalid email format.[/red]")
        return
    domain = email.split("@")[1]
    console.print(f"[green][+] Email Domain  :[/green] {domain}")
    try:
        ip = socket.gethostbyname(domain)
        console.print(f"[green][+] Mail Host IP  :[/green] {ip}")
    except Exception:
        console.print("[red][-] Could not resolve mail domain.[/red]")

def main():
    while True:
        banner()
        console.print("[1] Phone Number OSINT Intelligence")
        console.print("[2] Email / Domain Footprint Lookup")
        console.print("[3] Web Target Information & Recon (IP/Hosting/Headers)")
        console.print("[4] Open Official ELVORIX Web Portal")
        console.print("[5] Open Creator YouTube Channel")
        console.print("[6] Join Discord Community")
        console.print("[7] Join Telegram Security Channel")
        console.print("[8] Exit")
        
        choice = console.input("\n[bold cyan]Select an option (1-8): [/bold cyan]")
        
        if choice == "1":
            phone_osint()
        elif choice == "2":
            email_osint()
        elif choice == "3":
            web_recon()
        elif choice == "4":
            console.print("[green][+] Opening ELVORIX Portal...[/green]")
            webbrowser.open("https://vedansh73.github.io/ELVORIX/")
        elif choice == "5":
            console.print("[green][+] Opening YouTube Channel...[/green]")
            webbrowser.open("https://www.youtube.com/@vedanshsrivastava182")
        elif choice == "6":
            console.print("[green][+] Opening Discord Server...[/green]")
            webbrowser.open("https://discord.com/invite/PUgqMfdWwB")
        elif choice == "7":
            console.print("[green][+] Opening Telegram Channel...[/green]")
            webbrowser.open("https://t.me/vedasecurity182")
        elif choice == "8":
            console.print("[bold red]Exiting Hackme Suite. Stay safe and ethical![/bold red]")
            sys.exit()
        else:
            console.print("[red]Invalid choice! Please select between 1-8.[/red]")
            
        console.input("\n[dim]Press Enter to continue...[/dim]")

if __name__ == "__main__":
    main()
