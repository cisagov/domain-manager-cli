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


def test_record_get_command(mocker):
    """Test `dmcli record get`."""
    mocker.patch(
        "dmcli.utils.api.get",
        return_value=[{"name": "example.com"}],
    )
    runner = CliRunner()
    result = runner.invoke(record, "get", input="example.com")

    assert result.output.splitlines()[0] == "Domain: example.com"


# def test_record_add_command():
#     """Test `dmcli record add`."""
#     runner = CliRunner()
#     result = runner.invoke(record)

#     assert (
#         result.output.splitlines()[0] == "Usage: record [OPTIONS] COMMAND [ARGS]..."
#     ), "base record command not outputting usage."


# def test_record_delete_command():
#     """Test `dmcli record delete`."""
#     runner = CliRunner()
#     result = runner.invoke(record)

#     assert (
#         result.output.splitlines()[0] == "Usage: record [OPTIONS] COMMAND [ARGS]..."
#     ), "base record command not outputting usage."


# def test_record_update_command():
#     """Test `dmcli record update`."""
#     runner = CliRunner()
#     result = runner.invoke(record)

#     assert (
#         result.output.splitlines()[0] == "Usage: record [OPTIONS] COMMAND [ARGS]..."
#     ), "base record command not outputting usage."
