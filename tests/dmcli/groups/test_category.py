"""Category group tests."""
# Third-Party Libraries
from click.testing import CliRunner

# cisagov Libraries
from dmcli.groups.category import category


def test_category_group_command():
    """Test `dmcli category`."""
    runner = CliRunner()
    result = runner.invoke(category)

    assert (
        result.output.splitlines()[0] == "Usage: category [OPTIONS] COMMAND [ARGS]..."
    ), "base category command not outputting usage."


def test_category_all_command(mocker):
    """Test `dmcli category all`."""
    mocker.patch("dmcli.utils.api.get", return_value=["test", "test2"])

    runner = CliRunner()
    result = runner.invoke(category, "all")

    assert result.output.splitlines()[0] == "test", "First category not listed"
    assert result.output.splitlines()[1] == "test2", "Second category not listed"
