"""Configure group tests."""
# Standard Python Libraries
import re

# Third-Party Libraries
from click.testing import CliRunner
import pytest

# cisagov Libraries
from dmcli.groups.configure import configure


@pytest.fixture(scope="module")
def test_configure_command():
    """Test `dmcli configure`."""
    runner = CliRunner()
    result = runner.invoke(configure, input="\n".join(["test.url", "test_api_key"]))

    result_regex = re.compile(
        "Enter Domain Manager Url.*: test.url\nEnter API Key.*: test_api_key\n"
    )
    assert not result.exception
    assert result_regex.match(result.output) is not None
