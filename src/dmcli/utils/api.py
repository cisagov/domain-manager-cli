"""Functions to make requests against API."""
# Third-Party Libraries
import click
import requests

# cisagov Libraries
from dmcli.utils.message_handling import error_msg
from dmcli.utils.settings import API_KEY, URL, auth


def verify():
    """Verify configuration."""
    if not API_KEY or not URL:
        raise click.ClickException(
            "Environment not configured. Please run `dmcli configure`"
        )


def get(path):
    """Get."""
    verify()
    resp = requests.get(f"{URL}{path}", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return
    return resp.json()


def put(path, **kwargs):
    """Put."""
    verify()
    resp = requests.put(f"{URL}{path}", headers=auth, **kwargs)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return
    return resp.json()


def post(path, **kwargs):
    """Post."""
    verify()
    resp = requests.post(f"{URL}{path}", headers=auth, **kwargs)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return
    return resp.json()


def delete(path):
    """Delete."""
    verify()
    resp = requests.delete(f"{URL}{path}", headers=auth)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        error_msg(str(e))
        return
    return resp.json()
