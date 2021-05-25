"""Domain group tests."""
# Third-Party Libraries
from click.testing import CliRunner

# cisagov Libraries
from dmcli.groups.domain import domain


def test_domain_group_command():
    """Test `dmcli domain`."""
    runner = CliRunner()
    result = runner.invoke(domain)

    assert (
        result.output.splitlines()[0] == "Usage: domain [OPTIONS] COMMAND [ARGS]..."
    ), "base category command not outputting usage."


def test_domain_all_command(mocker):
    """Test `dmcli domain all`."""
    mocker.patch(
        "dmcli.utils.api.get",
        return_value=[{"name": "example.com"}],
    )

    runner = CliRunner()
    result = runner.invoke(domain, "all")

    assert result.output.splitlines()[0] == "example.com"


def test_domain_active_command(mocker):
    """Test `dmcli domain active`."""
    mocker.patch(
        "dmcli.utils.api.get",
        return_value=[{"name": "example.com", "is_active": True}],
    )

    runner = CliRunner()
    result = runner.invoke(domain, "active")

    assert result.output.splitlines()[0] == "example.com"


def test_domain_inactive_command(mocker):
    """Test `dmcli domain inactive`."""
    mocker.patch(
        "dmcli.utils.api.get",
        return_value=[{"name": "example.com", "is_active": False}],
    )

    runner = CliRunner()
    result = runner.invoke(domain, "inactive")

    assert result.output.splitlines()[0] == "example.com"


def test_domain_hostedzone_command(mocker):
    """Test `dmcli domain hostedzone`."""
    mocker.patch(
        "dmcli.utils.api.get",
        return_value=[{"Name": "example.com", "Type": "NS"}],
    )

    runner = CliRunner()
    result = runner.invoke(domain, "hostedzone", input="example.com")

    assert result.output.splitlines()[0] == "Domain: example.com"


def test_domain_nameservers_command(mocker):
    """Test `dmcli domain nameservers`."""
    mocker.patch(
        "dmcli.utils.api.get",
        return_value=[{"ResourceRecords": [{"Value": "ns-0000.awsdns-01.co.uk."}]}],
    )

    runner = CliRunner()
    result = runner.invoke(domain, "nameservers", input="example.com")

    assert result.output.splitlines()[0] == "Domain: example.com"
