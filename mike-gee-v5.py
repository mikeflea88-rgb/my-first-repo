import os, subprocess, sys, time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
console = Console()
BASE = os.path.expanduser("~/empire-repo")

def run_file(fname):
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        console.print(f"[red]Not found: {fname}[/red]"); time.sleep(1.5); return
    os.system("clear")
    try:
        subprocess.run([sys.executable, path])
    except Exception as e:
        console.print(f"[red]{e}[/red]")
    input("\nPress ENTER to return to MIKE GEE menu...")

while True:
    os.system("clear")
    console.print(Panel("[bold gold1]MIKE GEE TECHNOLOGIES[/bold gold1]\n[cyan]v5.0 - ALL EMPIRE IN ONE PLACE[/cyan]", border_style="gold1"))
    t = Table(box=box.ROUNDED); t.add_column("NO", style="cyan"); t.add_column("APP", style="white")
    apps = [
        ("1","AI Assistant - Business Ideas"),
        ("2","Business Bot - For Customers"),
        ("3","CEO Toolkit - Organize + System Info"),
        ("4","Invoice Generator - Make Invoice like Shatta Wale one"),
        ("5","Password Generator - Strong Password"),
        ("6","Data Analyzer - Check billionaire_data.csv"),
        ("7","File Organizer - Clean Downloads"),
        ("8","LAMI Fashion - Kaba & Slit GHS 250"),
        ("9","MINDLIFT - Daily Challenge"),
        ("0","Exit"),
    ]
    for n,a in apps: t.add_row(n,a)
    console.print(t)
    c = input("Pick [0-9]: ").strip()
    files = {"1":"AI_Assistant.py","2":"Business_Bot.py","3":"CEO_Toolkit.py","4":"Invoice_Generator.py","5":"Password_Generator.py","6":"Data_Analyzer.py","7":"File_Organizer.py"}
    if c=="0": break
    elif c in files: run_file(files[c])
    elif c=="8": console.print(Panel("LAMI - Kaba & Slit GHS 250\nWhatsApp: 0544555016", border_style="gold1")); time.sleep(2)
    elif c=="9": console.print(Panel("MINDLIFT - Today: Build 1 app\n+50 Points", border_style="cyan")); time.sleep(2)
    else: console.print("[red]Pick 0-9[/red]"); time.sleep(1)
