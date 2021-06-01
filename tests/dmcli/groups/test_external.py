"""External group tests."""
# Third-Party Libraries
from click.testing import CliRunner

# cisagov Libraries
from dmcli.groups.external import external


def test_external_group_command():
    """Test `dmcli external`."""
    runner = CliRunner()
    result = runner.invoke(external)

    assert (
        result.output.splitlines()[0] == "Usage: external [OPTIONS] COMMAND [ARGS]..."
    ), "base external command not outputting usage."


def test_external_check_command(mocker):
    """Test `dmcli external check`."""
    mocker.patch(
        "dmcli.utils.api.get",
        return_value=[{"name": "example.com"}],
    )
    runner = CliRunner()
    result = runner.invoke(external, "check", input="example.com")

    assert result.output.splitlines()[0] == "Domain name: example.com"
