import requests
from utils.settings import URL, auth
from utils.message_handling import error_msg, success_msg


def get(path):
    resp = requests.get(f"{URL}{path}", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return
    return resp.json()


def put(path, **kwargs):
    resp = requests.put(f"{URL}{path}", headers=auth, **kwargs)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return
    return resp.json()


def post(path, **kwargs):
    resp = requests.post(f"{URL}{path}", headers=auth, **kwargs)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return
    return resp.json()


def delete(path):
    resp = requests.delete(f"{URL}{path}", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return
    return resp.json()