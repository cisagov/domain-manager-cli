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
    )


def test_application_all_command():
    """Test `dmcli application all`."""
    return
