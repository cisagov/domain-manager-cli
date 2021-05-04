#!/usr/bin/env pytest -vs
"""Tests for Domain Manager CLI."""

# Standard Python Libraries
import sys
from unittest.mock import patch

# Third-Party Libraries
import pytest

# cisagov Libraries
import dmcli
from dmcli import main

PROJECT_VERSION = dmcli.__version__


def test_stdout_version(capsys):
    """Verify that version string sent to stdout agrees with the module version."""
    with pytest.raises(SystemExit):
        with patch.object(sys, "argv", ["bogus", "--version"]):
            main.start()
    captured = capsys.readouterr()
    assert (
        PROJECT_VERSION in captured.out
    ), "standard output by '--version' should agree with module.__version__"
