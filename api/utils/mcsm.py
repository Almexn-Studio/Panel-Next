import requests

class Mcsm:
    def __init__(self, url, apikey):
        self.url = url
        self.apikey = apikey
        self.headers = {'x-requested-with': 'xmlhttprequest'}

    def create_user(self, username, password, permission=1):
        """
        创建用户并返回是否成功的布尔值。

        参数:
            username (str): 用户名
            password (str): 密码
            permission (int, 可选): 用户权限，默认为1（普通权限）

        返回:
            tuple: 包含两个元素的元组，第一个元素是布尔值表示是否成功创建用户，
                   第二个元素是用户 UUID 或错误信息。
        """
        api_url = f"{self.url}/api/auth?apikey={self.apikey}"
        data = {
            'username': username,
            'password': password,
            'permission': permission,
        }

        try:
            response = requests.post(api_url, data=data, headers=self.headers)
            if response.status_code == 200:
                return True, self.get_uuid_by_name(username)
            else:
                return False, response.json().get("data", "")
        except requests.exceptions.RequestException as e:
            return False, str(e)

    def get_uuid_by_name(self, username: str) -> str:
        """
        根据用户名获取 UUID。

        参数:
            username (str): 用户名

        返回:
            str: 用户的 UUID 或 "NULL" 表示未找到。
        """
        api_url = f"{self.url}/api/auth/search?apikey={self.apikey}&userName={username}&page=1&page_size=1&role="
        try:
            response = requests.get(api_url, headers=self.headers)
            if response.status_code == 200:
                return response.json()["data"]["data"][0].get("uuid", "NULL")
            else:
                return "NULL"
        except requests.exceptions.RequestException:
            return "NULL"

    def update_permission(self, uuid: str, permission: int):
        """
        更新用户的权限并返回是否成功的布尔值。

        参数:
            uuid (str): 用户的 UUID
            permission (int): 用户的新权限

        返回:
            bool: 用户权限是否成功更新
        """
        api_url = f"{self.url}/api/auth?apikey={self.apikey}"
        data = {
            'uuid': uuid,
            'config': {
                'permission': permission
            }
        }
        response = requests.put(api_url, json=data, headers=self.headers)
        redata = response.json()
        return redata.get("data", False)

    def add_example(self, name, type, process_type="general"):
        """
        创建实例并返回是否成功的布尔值。

        参数:
            name (str): 实例名
            type (str): 实例类型
            process_type (str, 可选): 进程类型，默认为 "general"

        返回:
            str: 实例的 UUID
        """
        api_url = f"{self.url}/api/instance?daemonId=bf812a47a8e24e738cd36c617727a2b6&apikey={self.apikey}"
        docker_config = {
            "containerName": "",
            "image": "openjdk:21",
            "memory": 1024,
            "ports": ["25565:25565/tcp"],
            "extraVolumes": [],
            "maxSpace": None,
            "network": None,
            "io": None,
            "networkMode": "bridge",
            "networkAliases": [],
            "cpusetCpus": "",
            "cpuUsage": 100,
            "workingDir": "",
            "env": []
        }
        data = {
            "nickname": name,
            "startCommand": "java -Dfile.encoding=utf-8 -Djline.terminal=jline.UnsupportedTerminal -jar server.jar",
            "stopCommand": "stop",
            "type": type,
            "ie": "utf-8",
            "oe": "utf-8",
            "cwd": f"D://server/{name}",
            "docker": docker_config,
            "processType": process_type,
        }
        response = requests.post(api_url, data=data, headers=self.headers)
        if response.json().get("status") == 200:
            return response.json()["data"]["instanceUuid"]

    def give_example(self, example_uuid, user_uuid):
        """
        给予用户实例。

        参数:
            example_uuid (str): 实例 UUID
            user_uuid (str): 用户 UUID

        返回:
            str: 实例的 UUID
        """
        api_url = f"{self.url}/api/auth?apikey={self.apikey}"
        data = {
            "config": {
                "instances": [
                    {
                        "instanceUuid": example_uuid,
                        "daemonId": "bf812a47a8e24e738cd36c617727a2b6",
                        "nickname": "0001",
                        "status": 3,
                        "hostIp": "localhost:24444",
                        "config": {
                            "nickname": "0001",
                            "startCommand": "bedrock_server_mod.exe",
                            "stopCommand": "stop",
                            "cwd": "D://server/0001",
                            "ie": "utf8",
                            "oe": "utf8",
                            "createDatetime": 1722600268334,
                            "lastDatetime": 1722663864344,
                            "type": "minecraft/bedrock",
                            "tag": [],
                            "endTime": None,
                            "fileCode": "utf8",
                            "processType": "general",
                            "updateCommand": "",
                            "crlf": 2,
                            "enableRcon": False,
                            "rconPassword": "",
                            "rconPort": 0,
                            "rconIp": "",
                            "actionCommandList": [],
                            "terminalOption": {
                                "haveColor": False,
                                "pty": True,
                                "ptyWindowCol": 164,
                                "ptyWindowRow": 40
                            },
                            "eventTask": {
                                "autoStart": False,
                                "autoRestart": False,
                                "ignore": False
                            },
                            "docker": {
                                "containerName": "",
                                "image": "",
                                "ports": [],
                                "extraVolumes": [],
                                "memory": 0,
                                "networkMode": "bridge",
                                "networkAliases": [],
                                "cpusetCpus": "",
                                "cpuUsage": 0,
                                "maxSpace": 0,
                                "io": 0,
                                "network": 0,
                                "workingDir": "/workspace/",
                                "env": []
                            },
                            "pingConfig": {
                                "ip": "",
                                "port": 25565,
                                "type": 1
                            },
                            "extraServiceConfig": {
                                "openFrpTunnelId": "",
                                "openFrpToken": ""
                            }
                        }
                    }
                ]
            },
            "uuid": user_uuid
        }
        response = requests.put(api_url, json=data, headers=self.headers)
        return response.text