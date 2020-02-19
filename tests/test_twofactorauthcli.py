from unittest.mock import patch
from pathlib import Path

from twofactorauthcli import main, _get_config_file_path


@patch.object(Path, "home")
def test_get_config_file_path(pathmock):
    pathmock.return_value = Path("/home/anxodio")
    assert _get_config_file_path() == Path("/home/anxodio/.2fa/codes.yaml")


@patch("twofactorauthcli._get_codes")
@patch("twofactorauthcli._show_config_error")
def test_config_error(showmock, getcodesmock):
    getcodesmock.side_effect = IOError()
    main()
    showmock.assert_called()


@patch("twofactorauthcli._get_codes")
@patch("twofactorauthcli._print_2fauth")
def test_happy_path(print2famock, getcodesmock):
    getcodesmock.return_value = {}
    main()
    print2famock.assert_called()
