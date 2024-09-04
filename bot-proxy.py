import os
import sys
import time
import requests
from requests.auth import HTTPProxyAuth
from colorama import *
from datetime import datetime
import json
import brotli

red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX
green = Fore.LIGHTGREEN_EX
black = Fore.LIGHTBLACK_EX
blue = Fore.LIGHTBLUE_EX
white = Fore.LIGHTWHITE_EX
reset = Style.RESET_ALL

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the full paths to the files
data_file = os.path.join(script_dir, "data-proxy.json")
config_file = os.path.join(script_dir, "config.json")


class Cowtopia:
    def __init__(self):
        self.line = white + "~" * 50

        self.banner = f"""
        {blue}Smart Airdrop {white}BANANA Auto Claimer
        t.me/smartairdrop2120
        
        """

        self.auto_equip_banana = (
            json.load(open(config_file, "r")).get("auto-equip-banana", "false").lower()
            == "true"
        )

        self.auto_do_task = (
            json.load(open(config_file, "r")).get("auto-do-task", "false").lower()
            == "true"
        )

        self.auto_claim_invite = (
            json.load(open(config_file, "r")).get("auto-claim-invite", "false").lower()
            == "true"
        )

        self.auto_claim_and_harvest = (
            json.load(open(config_file, "r"))
            .get("auto-claim-and-harvest", "false")
            .lower()
            == "true"
        )

        self.auto_click = (
            json.load(open(config_file, "r")).get("auto-click", "false").lower()
            == "true"
        )

    # Clear the terminal
    def clear_terminal(self):
        # For Windows
        if os.name == "nt":
            _ = os.system("cls")
        # For macOS and Linux
        else:
            _ = os.system("clear")

    def headers(self, token):
        return {
            "Accept": "application/json, text/plain, */*",
            "Authorization": f"Bearer {token}",
            "Origin": "https://banana.carv.io",
            "Referer": "https://banana.carv.io/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        }

    def proxies(self, proxy_info):
        return {"http": f"{proxy_info}", "https": f"{proxy_info}"}

    def check_ip(self, proxy_info):
        url = "https://api.ipify.org?format=json"

        proxies = self.proxies(proxy_info=proxy_info)

        # Parse the proxy credentials if present
        if "@" in proxy_info:
            proxy_credentials = proxy_info.split("@")[0]
            proxy_user = proxy_credentials.split(":")[1]
            proxy_pass = proxy_credentials.split(":")[2]
            auth = HTTPProxyAuth(proxy_user, proxy_pass)
        else:
            auth = None

        try:
            response = requests.get(url=url, proxies=proxies, auth=auth)
            response.raise_for_status()  # Raises an error for bad status codes
            return response.json().get("ip")
        except requests.exceptions.RequestException as e:
            print(f"IP check failed: {e}")
            return None

    def get_token(self, data, proxy_info):
        url = f"https://interface.carv.io/banana/login"

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Origin": "https://banana.carv.io",
            "Referer": "https://banana.carv.io/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        }

        data = {"tgInfo": f"{data}"}

        proxies = self.proxies(proxy_info=proxy_info)

        response = requests.post(url=url, headers=headers, data=data, proxies=proxies)

        return response

    def user_info(self, token, proxy_info):
        url = f"https://interface.carv.io/banana/get_user_info"

        headers = self.headers(token=token)

        proxies = self.proxies(proxy_info=proxy_info)

        response = requests.get(url=url, headers=headers, proxies=proxies)

        return response

    def banana_list(self, token, proxy_info):
        url = f"https://interface.carv.io/banana/get_banana_list"

        headers = self.headers(token=token)

        proxies = self.proxies(proxy_info=proxy_info)

        response = requests.get(url=url, headers=headers, proxies=proxies)

        return response

    def equip_banana(self, token, banana_id, proxy_info):
        url = f"https://interface.carv.io/banana/do_equip"

        headers = self.headers(token=token)

        data = {"bananaId": banana_id}

        proxies = self.proxies(proxy_info=proxy_info)

        response = requests.post(url=url, headers=headers, data=data, proxies=proxies)

        return response

    def quest_list(self, token, proxy_info):
        url = f"https://interface.carv.io/banana/get_quest_list"

        headers = self.headers(token=token)

        proxies = self.proxies(proxy_info=proxy_info)

        response = requests.get(url=url, headers=headers, proxies=proxies)

        return response

    def achieve_quest(self, token, quest_id, proxy_info):
        url = f"https://interface.carv.io/banana/achieve_quest"

        headers = self.headers(token=token)

        data = {"quest_id": quest_id}

        proxies = self.proxies(proxy_info=proxy_info)

        response = requests.post(url=url, headers=headers, data=data, proxies=proxies)

        return response

    def claim_quest(self, token, quest_id, proxy_info):
        url = f"https://interface.carv.io/banana/claim_quest"

        headers = self.headers(token=token)

        data = {"quest_id": quest_id}

        proxies = self.proxies(proxy_info=proxy_info)

        response = requests.post(url=url, headers=headers, data=data, proxies=proxies)

        return response

    def claim_quest_lottery(self, token, proxy_info):
        url = f"https://interface.carv.io/banana/claim_quest_lottery"

        headers = self.headers(token=token)

        headers["Content-Type"] = "application/json"

        data = {}

        proxies = self.proxies(proxy_info=proxy_info)

        response = requests.post(url=url, headers=headers, data=data, proxies=proxies)

        return response

    def invite_list(self, token, proxy_info):
        url = f"https://interface.carv.io/banana/get_invite_list"

        headers = self.headers(token=token)

        proxies = self.proxies(proxy_info=proxy_info)

        response = requests.get(url=url, headers=headers, proxies=proxies)

        return response

    def claim_invite(self, token, proxy_info):
        url = f"https://interface.carv.io/banana/claim_lottery"

        headers = self.headers(token=token)

        data = {"claimLotteryType": 2}

        proxies = self.proxies(proxy_info=proxy_info)

        response = requests.post(url=url, headers=headers, data=data, proxies=proxies)

        return response

    def lottery_info(self, token, proxy_info):
        url = f"https://interface.carv.io/banana/get_lottery_info"

        headers = self.headers(token=token)

        proxies = self.proxies(proxy_info=proxy_info)

        response = requests.get(url=url, headers=headers, proxies=proxies)

        return response

    def claim_lottery(self, token, proxy_info):
        url = f"https://interface.carv.io/banana/claim_lottery"

        headers = self.headers(token=token)

        data = {"claimLotteryType": 1}

        proxies = self.proxies(proxy_info=proxy_info)

        response = requests.post(url=url, headers=headers, data=data, proxies=proxies)

        return response

    def do_lottery(self, token, proxy_info):
        url = f"https://interface.carv.io/banana/do_lottery"

        headers = self.headers(token=token)

        headers["Content-Type"] = "application/json"

        data = {}

        proxies = self.proxies(proxy_info=proxy_info)

        response = requests.post(url=url, headers=headers, data=data, proxies=proxies)

        return response

    def do_click(self, token, click_count, proxy_info):
        url = f"https://interface.carv.io/banana/do_click"

        headers = self.headers(token=token)

        data = {"clickCount": click_count}

        proxies = self.proxies(proxy_info=proxy_info)

        response = requests.post(url=url, headers=headers, data=data, proxies=proxies)

        return response

    def log(self, msg):
        now = datetime.now().isoformat(" ").split(".")[0]
        print(f"{black}[{now}]{reset} {msg}{reset}")

    def parse_proxy_info(self, proxy_info):
        try:
            stripped_url = proxy_info.split("://", 1)[-1]
            credentials, endpoint = stripped_url.split("@", 1)
            user_name, password = credentials.split(":", 1)
            ip, port = endpoint.split(":", 1)
            return {"user_name": user_name, "pass": password, "ip": ip, "port": port}
        except:
            return None

    def main(self):
        while True:
            self.clear_terminal()
            print(self.banner)
            accounts = json.load(open(data_file, "r"))["accounts"]
            num_acc = len(accounts)
            self.log(self.line)
            self.log(f"{green}Numer of account: {white}{num_acc}")
            for no, account in enumerate(accounts):
                self.log(self.line)
                self.log(f"{green}Account number: {white}{no+1}/{num_acc}")
                data = account["acc_info"]
                proxy_info = account["proxy_info"]
                parsed_proxy_info = self.parse_proxy_info(proxy_info)
                if parsed_proxy_info is None:
                    self.log(
                        f"{red}Check proxy format: {white}http://user:pass@ip:port"
                    )
                    break
                ip_adress = parsed_proxy_info["ip"]
                self.log(f"{green}Input IP Address: {white}{ip_adress}")

                ip = self.check_ip(proxy_info=proxy_info)
                self.log(f"{green}Actual IP Address: {white}{ip}")

                # Get token
                try:
                    get_token = self.get_token(data=data, proxy_info=proxy_info).json()
                    token = get_token["data"]["token"]

                    # Get user info
                    get_user_info = self.user_info(
                        token=token, proxy_info=proxy_info
                    ).json()
                    banana = get_user_info["data"]["banana_count"]
                    peel = get_user_info["data"]["peel"]
                    usdt = get_user_info["data"]["usdt"]
                    equip_banana_name = get_user_info["data"]["equip_banana"]["name"]
                    equip_banana_peel_limit = get_user_info["data"]["equip_banana"][
                        "daily_peel_limit"
                    ]
                    equip_banana_peel_price = get_user_info["data"]["equip_banana"][
                        "sell_exchange_peel"
                    ]
                    equip_banana_usdt_price = get_user_info["data"]["equip_banana"][
                        "sell_exchange_usdt"
                    ]
                    self.log(
                        f"{green}Banana: {white}{banana} - {green}Peels: {white}{peel} - {green}USDT: {white}{usdt}"
                    )
                    self.log(
                        f"{green}Equip Banana: {white}{equip_banana_name} - {green}Daily Peel Limit: {white}{equip_banana_peel_limit} - {green}Peel Price: {white}{equip_banana_peel_price} - {green}USDT Price: {white}{equip_banana_usdt_price}"
                    )

                    # Do task
                    if self.auto_do_task:
                        self.log(f"{yellow}Auto Do Task: {green}ON")
                        get_quest_list = self.quest_list(
                            token=token, proxy_info=proxy_info
                        ).json()
                        quest_list = get_quest_list["data"]["quest_list"]
                        for quest in quest_list:
                            quest_id = quest["quest_id"]
                            quest_name = quest["quest_name"]
                            achieve_status = quest["is_achieved"]
                            claim_status = quest["is_claimed"]
                            if not achieve_status and not claim_status:
                                achieve_quest = self.achieve_quest(
                                    token=token,
                                    quest_id=quest_id,
                                    proxy_info=proxy_info,
                                ).json()
                                claim_quest = self.claim_quest(
                                    token=token,
                                    quest_id=quest_id,
                                    proxy_info=proxy_info,
                                ).json()
                                quest_status = claim_quest["msg"]
                                if quest_status == "Success":
                                    self.log(f"{white}{quest_name}: {green}Completed")
                                else:
                                    self.log(
                                        f"{white}{quest_name}: {red}Incomplete (please do by yourself)"
                                    )
                            elif achieve_status and not claim_status:
                                claim_quest = self.claim_quest(
                                    token=token,
                                    quest_id=quest_id,
                                    proxy_info=proxy_info,
                                ).json()
                                quest_status = claim_quest["msg"]
                                if quest_status == "Success":
                                    self.log(f"{white}{quest_name}: {green}Completed")
                                else:
                                    self.log(
                                        f"{white}{quest_name}: {red}Incomplete (please do by yourself)"
                                    )
                            else:
                                self.log(f"{white}{quest_name}: {green}Completed")

                        while True:
                            claim_quest_lottery = self.claim_quest_lottery(
                                token=token, proxy_info=proxy_info
                            ).json()
                            quest_lottery_status = claim_quest_lottery["msg"]
                            if quest_lottery_status == "Success":
                                self.log(
                                    f"{white}--> Claim Quest Lottery: {green}Success"
                                )
                                continue
                            else:
                                self.log(
                                    f"{white}--> Claim Quest Lottery: {red}No Lottery to Claim"
                                )
                                break
                    else:
                        self.log(f"{yellow}Auto Do Task: {red}OFF")

                    # Claim invite
                    if self.auto_claim_invite:
                        self.log(f"{yellow}Auto Claim Invite: {green}ON")
                        get_invite_list = self.invite_list(
                            token=token, proxy_info=proxy_info
                        ).json()
                        invite = get_invite_list["data"]
                        if invite is None:
                            self.log(f"{white}Claim Invite: {red}No friend")
                        else:
                            self.log(f"{white}Claim Invite: {green}Have friends")
                            claim_status = invite["claim"]
                            if claim_status:
                                claim_invite = self.claim_invite(
                                    token=token, proxy_info=proxy_info
                                )
                                claim_invite_status = claim_invite["msg"]
                                if claim_invite_status == "Success":
                                    self.log(f"{white}Claim Invite: {green}Success")
                                else:
                                    self.log(f"{white}Claim Invite: {red}Fail")
                            else:
                                self.log(
                                    f"{white}Claim Invite: {red}No invite lottery to claim"
                                )
                    else:
                        self.log(f"{yellow}Auto Claim Invite: {red}OFF")

                    # Get lottery info
                    if self.auto_claim_and_harvest:
                        self.log(f"{yellow}Auto Claim and Harvest: {green}ON")
                        while True:
                            get_lottery_info = self.lottery_info(
                                token=token, proxy_info=proxy_info
                            ).json()
                            lottery_status = get_lottery_info["data"]["countdown_end"]
                            lottery_count = get_lottery_info["data"][
                                "remain_lottery_count"
                            ]
                            if lottery_status:
                                claim_lottery = self.claim_lottery(
                                    token=token, proxy_info=proxy_info
                                ).json()
                                claim_status = claim_lottery["msg"]
                                if claim_status == "Success":
                                    self.log(f"{white}Claim Banana: {green}Success")
                                else:
                                    self.log(f"{white}Claim Banana: {red}Fail")
                            elif lottery_count > 0:
                                do_lottery = self.do_lottery(
                                    token=token, proxy_info=proxy_info
                                ).json()
                                self.log(f"{white}Harvest Banana: {green}Success")
                            else:
                                self.log(
                                    f"{white}Claim and Harvest Banana: {red}Not time to Claim and No Banana to Harvest"
                                )
                                break
                    else:
                        self.log(f"{yellow}Auto Claim and Harvest: {red}OFF")

                    # Equip banana
                    if self.auto_equip_banana:
                        self.log(f"{yellow}Auto Equip Banana: {green}ON")
                        get_banana_list = self.banana_list(
                            token=token, proxy_info=proxy_info
                        ).json()
                        banana_list = get_banana_list["data"]["banana_list"]
                        banana_with_max_peel = max(
                            (banana for banana in banana_list if banana["count"] > 0),
                            key=lambda b: b["daily_peel_limit"],
                        )
                        banana_id = banana_with_max_peel["banana_id"]
                        banana_name = banana_with_max_peel["name"]
                        banana_peel_limit = banana_with_max_peel["daily_peel_limit"]
                        banana_peel_price = banana_with_max_peel["sell_exchange_peel"]
                        banana_usdt_price = banana_with_max_peel["sell_exchange_usdt"]

                        equip_banana = self.equip_banana(
                            token=token, banana_id=banana_id, proxy_info=proxy_info
                        ).json()
                        equip_status = equip_banana["msg"]
                        if equip_status == "Success":
                            self.log(f"{white}Equip Banana: {green}Success")
                            self.log(
                                f"{green}New Equip Banana: {white}{banana_name} - {green}Daily Peel Limit: {white}{banana_peel_limit} - {green}Peel Price: {white}{banana_peel_price} - {green}USDT Price: {white}{banana_usdt_price}"
                            )
                        else:
                            self.log(f"{white}Equip Banana: {green}Fail")
                    else:
                        self.log(f"{yellow}Auto Equip Banana: {red}OFF")

                    # Auto Click
                    if self.auto_click:
                        self.log(f"{yellow}Auto Click: {green}ON")
                        get_user_info = self.user_info(
                            token=token, proxy_info=proxy_info
                        ).json()
                        max_click_count = get_user_info["data"]["max_click_count"]
                        today_click_count = get_user_info["data"]["today_click_count"]
                        click_left = max_click_count - today_click_count
                        if click_left > 0:
                            do_click = self.do_click(
                                token=token,
                                click_count=click_left,
                                proxy_info=proxy_info,
                            ).json()
                            status = do_click["msg"]
                            if status == "Success":
                                peel_added = do_click["data"]["peel"]
                                self.log(
                                    f"{white}Click: {green}Success add {peel_added} peels"
                                )
                        else:
                            self.log(f"{white}Click: {red}No click left to perform")
                    else:
                        self.log(f"{yellow}Auto Click: {red}OFF")

                except Exception as e:
                    self.log(f"{red}Get access token error!!!")

            print()
            wait_time = 60 * 60
            self.log(f"{yellow}Wait for {int(wait_time/60)} minutes!")
            time.sleep(wait_time)


if __name__ == "__main__":
    try:
        cowtopia = Cowtopia()
        cowtopia.main()
    except KeyboardInterrupt:
        sys.exit()
