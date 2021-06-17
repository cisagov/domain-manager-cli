"""Configure group tests."""
# Standard Python Libraries
import re

# Third-Party Libraries
from click.testing import CliRunner

# cisagov Libraries
from dmcli.groups.configure import configure


def test_configure_command():
    """Test `dmcli configure`."""
    runner = CliRunner()
    result = runner.invoke(
        configure, input="\n".join(["http://test.com", "test_api_key"])
    )

    result_regex = re.compile(
        "Enter Domain Manager Url.*: http://test.com\nEnter API Key.*: test_api_key\n"
    )
    assert not result.exception
    assert result_regex.match(result.output) is not None
