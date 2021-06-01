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
