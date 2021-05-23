"""Category group tests."""
# Standard Python Libraries
import sys

# Third-Party Libraries
import pytest

# cisagov Libraries
from dmcli import main


def test_category_group_command(mocker, capsys):
    """Test `dmcli category`."""
    with pytest.raises(SystemExit):
        mocker.patch.object(sys, "argv", ["dmcli", "category"])
        main.start()

    captured = capsys.readouterr()
    assert (
        captured.out.splitlines()[0]
        == "Usage: dmcli category [OPTIONS] COMMAND [ARGS]..."
    ), "base category command not outputting usage."


def test_category_all_command(mocker, capsys):
    """Test `dmcli category all`."""
    with pytest.raises(SystemExit):
        mocker.patch.object(sys, "argv", ["dmcli", "category", "all"])
        mocker.patch("dmcli.utils.api.get", return_value=["test", "test2"])
        main.start()

    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[0].strip() == "test", "First category not listed"
    assert lines[1].strip() == "test2", "Second category not listed"
