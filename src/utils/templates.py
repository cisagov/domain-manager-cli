from utils import api
import os


def get_templates():
    return api.get("/api/templates/")


def upload_template(filepath):
    with open(filepath, "rb") as zipfile:
        content = zipfile.read()
        return api.post(
            path="/api/templates/", files={"zip": (os.path.basename(filepath), content)}
        )
