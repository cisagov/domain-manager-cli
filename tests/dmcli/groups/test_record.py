"""Record group tests."""
# Third-Party Libraries
from click.testing import CliRunner

# cisagov Libraries
from dmcli.groups.record import record


def test_record_group_command():
    """Test `dmcli record`."""
    runner = CliRunner()
    result = runner.invoke(record)

    assert (
        result.output.splitlines()[0] == "Usage: record [OPTIONS] COMMAND [ARGS]..."
    ), "base record command not outputting usage."
