"""Functions to make requests against API."""
# Third-Party Libraries
import requests

# cisagov Libraries
from utils.message_handling import error_msg
from utils.settings import URL, auth


def get(path):
    """Get."""
    resp = requests.get(f"{URL}{path}", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return
    return resp.json()


def put(path, **kwargs):
    """Put."""
    resp = requests.put(f"{URL}{path}", headers=auth, **kwargs)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return
    return resp.json()


def post(path, **kwargs):
    """Post."""
    resp = requests.post(f"{URL}{path}", headers=auth, **kwargs)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return
    return resp.json()


def delete(path):
    """Delete."""
    resp = requests.delete(f"{URL}{path}", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return
    return resp.json()
