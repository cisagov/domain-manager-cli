"""Application group tests."""
# Standard Python Libraries
import sys

# Third-Party Libraries
import pytest

# cisagov Libraries
from dmcli import main


def test_application_group_command(mocker, capsys):
    """Test `dmcli application`."""
    with pytest.raises(SystemExit):
        mocker.patch.object(sys, "argv", ["dmcli", "application"])
        main.start()

    captured = capsys.readouterr()
    assert (
        captured.out.splitlines()[0]
        == "Usage: dmcli application [OPTIONS] COMMAND [ARGS]..."
    ), "base application command not outputting usage."


def test_application_all_command(mocker, capsys):
    """Test `dmcli application all`."""
    with pytest.raises(SystemExit):
        mocker.patch.object(sys, "argv", ["dmcli", "application", "all"])
        mocker.patch(
            "dmcli.utils.api.get", return_value=[{"name": "test"}, {"name": "test2"}]
        )
        main.start()

    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[0].strip() == "test", "First application not listed"
    assert lines[1].strip() == "test2", "Second application not listed"
