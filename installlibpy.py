import subprocess
import importlib
import time
import sys
from rich.console import Console
from rich.progress import Progress
from rich.table import Table

console = Console()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 600+ LIBRARY PYTHON 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

libs = [
    # Terminal & CLI Enhancement
    "rich", "colorama", "pyfiglet", "cowsay", "termcolor", "progress", "click",
    "tqdm", "typer", "loguru", "pyfzf", "ranger-fm", "shellingham", "fuzzywuzzy",
    "invoke", "blessings", "alive-progress", "pager", "asciimatics", "pytermgui",
    "questionary", "pick", "cmd2", "plumbum", "python-prompt-toolkit",

    # Pentesting & Cybersecurity
    "scapy", "shodan", "paramiko", "python-nmap", "impacket", "pwntools", "requests",
    "dnspython", "netifaces", "pyshark", "pycares", "websockets", "python-whois",
    "ipwhois", "email-validator", "fake-useragent", "user-agents", "pyptables",
    "certifi", "tlslite-ng", "sslpsk", "urllib3", "pyshodan", "pytorctl", "pycryptodomex",
    "cryptography", "hashlib", "argon2-cffi", "pyOpenSSL", "passlib", "bcrypt", 
    "fernet", "pyjwt", "pyasn1", "pyotp", "ecdsa", "pynacl", "pyhash", "pyaxmlparser",
    "androguard", "ropper", "keystone-engine", "capstone", "ropgadget", "smbprotocol",

    # Web Scraping & Automation
    "selenium", "requests-html", "scrapy", "beautifulsoup4", "lxml", "pyppeteer",
    "mechanize", "robobrowser", "httpx", "aiohttp", "websocket-client", "twisted",
    "cloudscraper", "grequests", "html2text", "html5lib", "cssselect", "feedparser",
    "urlextract", "ghost.py", "grab", "demjson", "pyquery", "extract-msg", "pywebcopy",

    # Networking & API Tools
    "requests-cache", "httplib2", "pydns", "hyper", "hpack", "h2", "brotlipy",
    "python-socks", "python-telegram-bot", "slackclient", "pymsteams", "mastodon.py",
    "tweepy", "pyrebase4", "pyspeedtest", "pycurl", "urllib3", "sockets", "ftplib",
    "sniffio", "anyio", "httpcore", "rpcclient", "pyftpdlib",

    # Database & Storage
    "sqlalchemy", "pymysql", "pymongo", "redis", "psycopg2-binary", "sqlite3",
    "tinydb", "cassandra-driver", "plyvel", "elasticsearch", "influxdb", "riak",
    "pandas", "pytablewriter", "records", "dataset", "mongoengine", "redis-om",
    "pickledb", "sqlitedict", "zarr", "h5py",

    # File Processing & Archive
    "pdfminer.six", "pdfplumber", "pymupdf", "pyunpack", "patool", "pyunrar",
    "xlrd", "openpyxl", "csvkit", "tablib", "pyexcel", "pyexcel-xls", "py7zr",
    "zstandard", "pylzma", "pyzbar", "python-pptx", "python-docx", "pyrtf",
    "pillow", "imagesize", "pyexiv2", "wand", "pypdf2", "pycryptodome",

    # Machine Learning & Data Science
    "numpy", "scipy", "scikit-learn", "xgboost", "lightgbm", "statsmodels",
    "sympy", "patsy", "joblib", "modin", "polars", "dask", "numba", "cupy",
    "pyjanitor", "matplotlib", "seaborn", "plotly", "bokeh", "altair", "orange3",
    "pycaret", "featuretools", "tpot", "keras", "tensorflow", "torch", "fastai",

    # Cryptography & Security
    "pycryptodome", "cryptography", "hashids", "pycrc", "pycryptoplus", "pyelliptic",
    "pycoin", "pybitcoin", "block-io", "python-bitcoinlib", "eth-account",
    "web3", "bip-utils", "mnemonic", "pywallet", "pyethash", "pyblake2",

    # System & Process Management
    "psutil", "sh", "delegator.py", "humanize", "pathlib", "watchdog", "send2trash",
    "filelock", "pyinotify", "pyudev", "python-dotenv", "environs", "configobj",
    "configparser", "dotmap", "platformdirs", "appdirs", "distro", "docker",
    "kubernetes", "ansible", "fabric", "paramiko", "invoke",

    # Development & Testing Tools
    "pytest", "unittest", "coverage", "tox", "hypothesis", "pylint", "flake8",
    "black", "mypy", "bandit", "safety", "radon", "mutmut", "debugpy", "pudb",
    "ipdb", "line_profiler", "memory_profiler", "py-spy", "objgraph", "pyflame",

    # GUI & Multimedia
    "pygame", "arcade", "pyglet", "panda3d", "kivy", "pyqt5", "pyside2",
    "wxpython", "pygobject", "pycairo", "python-vlc", "pymedia", "pydub",
    "audioread", "eyeD3", "mutagen", "moviepy", "opencv-python", "scikit-image",

    # IoT & Hardware
    "pyserial", "pyusb", "python-can", "smbus2", "spidev", "RPi.GPIO", "gpiozero",
    "adafruit-blinka", "micropython", "circuitpython", "bluepy", "pybluez",
    "pyjwt", "pyzmq", "paho-mqtt", "hbmqtt", "amqtt", "websockets", "pynmea2",

    # Natural Language Processing
    "nltk", "spacy", "gensim", "pattern", "textblob", "polyglot", "stanza",
    "flair", "transformers", "sentence-transformers", "torchtext", "fasttext",
    "jieba", "langid", "pycld2", "sumy", "rake-nltk", "yake", "textacy",

    # API Development
    "fastapi", "flask", "django", "sanic", "aiohttp", "tornado", "bottle",
    "cherrypy", "falcon", "hug", "pyramid", "web2py", "quart", "starlette",
    "uvicorn", "gunicorn", "waitress", "meinheld", "httpie", "postmanerator",

    # Miscellaneous Utilities
    "faker", "python-magic", "pytz", "tzlocal", "pendulum", "arrow", "delorean",
    "maya", "parsedatetime", "iso8601", "python-dateutil", "pytimeparse",
    "natsort", "inflect", "phonenumbers", "pycountry", "python-stdnum", "validators",
    "pylnk3", "pyqrcode", "python-barcode", "pyautogui", "pyperclip", "clipboard",
    "emoji", "pyphen", "unidecode", "python-slugify", "pyshorteners", "shortuuid",
]

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# FUNGSI UTAMA
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def is_installed(lib):
    """Cek apakah library sudah terinstal"""
    try:
        importlib.import_module(lib.split("[")[0] if "[" in lib else lib)
        return True
    except ImportError:
        return False

def main():
    console.print("[bold cyan]📦 MEMULAI INSTALASI 600+ LIBRARY CLI...[/bold cyan]\n")
    console.print(f"[yellow]▶ Python Version: {sys.version.split()[0]}[/yellow]")
    console.print(f"[yellow]▶ Total Library: {len(libs)}[/yellow]\n")

    installed_count = 0
    skipped_count = 0
    failed_count = 0
    failed_libs = []

    with Progress(transient=True) as progress:
        task = progress.add_task("[bold green]Proses Instalasi...", total=len(libs))

        for lib in libs:
            # Handle extras syntax (e.g., lib[extra])
            clean_lib = lib.split("[")[0] if "[" in lib else lib

            if is_installed(clean_lib):
                skipped_count += 1
                progress.console.print(f"[yellow]⏩ {lib:.<40} SKIPPED[/yellow]")
            else:
                try:
                    pip_command = [
                        "pip", 
                        "install", 
                        "--quiet",
                        "--no-input",
                        "--disable-pip-version-check",
                        lib
                    ]
                    
                    result = subprocess.run(
                        pip_command,
                        check=True,
                        capture_output=True,
                        text=True
                    )
                    
                    installed_count += 1
                    progress.console.print(f"[green]✔ {lib:.<40} SUCCESS[/green]")
                except Exception as e:
                    failed_count += 1
                    failed_libs.append(lib)
                    progress.console.print(f"[red]✖ {lib:.<40} FAILED[/red]")

            progress.update(task, advance=1)
            time.sleep(0.05)

    # Tampilkan l aporan akhir
    console.print("\n[bold cyan]🎉 INSTALASI SELESAI![/bold cyan]")
    console.print(f"[bold green]Total Library: {len(libs)}[/bold green]")
    console.print(f"[bold green]Berhasil Diinstal: {installed_count}[/bold green]")
    console.print(f"[bold yellow]Dilewati: {skipped_count}[/bold yellow]")
    console.print(f"[bold red]Gagal Diinstal: {failed_count}[/bold red]")

    if failed_libs:
        console.print("\n[bold red]Library yang Gagal Diinstal:[/bold red]")
        for failed_lib in failed_libs:
            console.print(f" - {failed_lib}")

if __name__ == "__main__":
    main()