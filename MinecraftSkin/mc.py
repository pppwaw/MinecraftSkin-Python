import json
import requests
import base64
letter = {"a": 1, "b": 0, "c": 1, "d": 0, "e": 1, "f": 0, "g": 1,
    "h": 0, "i": 1, "j": 0, "k": 1, "l": 0, "m": 1, "n": 0,
    "o": 1, "p": 0, "q": 1, "r": 0, "s": 1, "t": 0, "u": 1,
    "v": 0, "w": 1, "x": 0, "y": 1, "z": 0}
def get_uuid(playername):
    temp=requests.get("https://api.mojang.com/users/profiles/minecraft/{0}".format(playername))
    if temp.status_code == 200:
        temp=json.loads(temp.text)
        return temp["id"]
    else:
        return None
def get_skin(uuid):
    if uuid == None:
        raise ValueError
    profile=json.loads(requests.get("https://sessionserver.mojang.com/session/minecraft/profile/{0}".format(uuid)).text)
    #print(profile)
    profile=json.loads(base64.b64decode(profile["properties"][0]["value"]))
    return profile["textures"]["SKIN"]["url"]
def get_cape(uuid):
    if uuid == None:
        raise ValueError
    profile = json.loads(requests.get("https://sessionserver.mojang.com/session/minecraft/profile/{0}".format(uuid)).text)
    try:
        profile=json.loads(base64.b64decode(profile["properties"][0]["value"]))
        cape = profile["textures"]["CAPE"]["url"]
    except: return None
    else: return cape
def get_skin_and_cape(uuid):
    skin=get_skin(uuid)
    cape=get_cape(uuid)
    return {"skin":skin,"cape":cape}
def is_Alex(uuid):
    return (isEven(uuid[7]) != isEven(uuid[16 + 7])) != (isEven(uuid[15]) != isEven(uuid[16 + 15]))
def isEven(c):
    try:
        int(c)
    except:
        return (letter[c] & 1) == 1
    else:
        c=int(c)
        return (c&1) == 0
