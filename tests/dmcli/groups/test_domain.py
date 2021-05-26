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
    ), "base domain command not outputting usage."


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


def test_domain_upload_command(mocker):
    """Test `dmcli domain upload`."""
    mocker.patch("dmcli.utils.api.get", return_value={"name": "example.com"})
    mocker.patch("builtins.open", mocker.mock_open(read_data="zipfile"))
    with open("/uploads/test.zip", "rb") as zipfile:
        content = zipfile.read()
        mocker.patch(
            "dmcli.utils.api.post",
            return_value="/uploads/test.zip",
        )

        runner = CliRunner()
        runner.invoke(
            domain, ["upload", "-f", "/uploads/test.zip", "-d", "example.com"]
        )

    assert content == "zipfile"


def test_domain_remove_command(mocker):
    """Test `dmcli domain remove`."""
    mocker.patch(
        "dmcli.utils.api.get",
        return_value={"name": "example.com"},
    )

    mocker.patch(
        "dmcli.utils.api.delete",
        return_value={"name": "example.com"},
    )

    runner = CliRunner()
    result = runner.invoke(domain, "remove", input="example.com")

    assert result.output.splitlines()[0] == "Domain name: example.com"
