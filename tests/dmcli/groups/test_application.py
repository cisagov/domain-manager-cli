"""Application group tests."""
# Third-Party Libraries
from click.testing import CliRunner

# cisagov Libraries
from dmcli.groups.application import application


def test_application_group_command():
    """Test `dmcli application`."""
    runner = CliRunner()
    result = runner.invoke(application)

    assert (
        result.output.splitlines()[0]
        == """Usage: application [OPTIONS] COMMAND [ARGS]..."""
    )


def test_application_all_command(mocker):
    """Test `dmcli application all`."""
    mocker.patch(
        "dmcli.utils.api.get", return_value=[{"name": "test"}, {"name": "test2"}]
    )

    runner = CliRunner()
    result = runner.invoke(application, "all")

    assert result.output.splitlines()[0] == "test"
    assert result.output.splitlines()[1] == "test2"
