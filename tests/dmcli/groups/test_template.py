"""Template group tests."""
# Third-Party Libraries
from click.testing import CliRunner

# cisagov Libraries
from dmcli.groups.template import template


def test_template_group_command():
    """Test `dmcli template`."""
    runner = CliRunner()
    result = runner.invoke(template)

    assert (
        result.output.splitlines()[0] == "Usage: template [OPTIONS] COMMAND [ARGS]..."
    ), "base template command not outputting usage."


def test_template_all_command(mocker):
    """Test `dmcli template all`."""
    mocker.patch(
        "dmcli.utils.api.get",
        return_value=[{"name": "template name"}],
    )

    runner = CliRunner()
    result = runner.invoke(template, "all")

    assert result.output.splitlines()[0] == "template name"


def test_template_upload_command(mocker):
    """Test `dmcli template upload`."""
    mocker.patch(
        "dmcli.utils.api.post",
        return_value="template has been uploaded",
    )

    mocker.patch("builtins.open", mocker.mock_open(read_data="zipfile"))
    with open("/uploads/test.zip") as zipfile:
        content = zipfile.read()

    runner = CliRunner()
    result = runner.invoke(template, "upload", input="/uploads/test.zip")

    assert not result.exception
    assert content == "zipfile"
    assert result.output.splitlines()[0] == "Filepath: /uploads/test.zip"
