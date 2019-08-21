from unittest.mock import patch, Mock
from urllib.parse import quote_plus
from copy import deepcopy

from ebr_board.config import VaultConfig


@patch("ebr_board.config.VaultAnyConfig.isfile")
@patch("ebr_board.config.connections.create_connection")
@patch("ebr_board.config.VaultAnyConfig")
def test_config(mock_va, mock_connections, mock_isfile):
    """
    Tests that the instantiation of a config.VaultConfig object results in the correct configuration.
    """
    sample_config = {"elastic": {"user": "elastic_user", "pwd": "elastic_password", "index": "elastic_index"}}

    local_sample_config = deepcopy(sample_config)
    mock_va.return_value.auto_auth = Mock(return_value=True)
    mock_va.return_value.loads = Mock(return_value=local_sample_config)

    config = VaultConfig(
        "test_not_a_conf_file.blargh", "test_not_a_vault_conf_file.blargh", "test_not_a_vault_creds_file.blargh"
    )

    # Validate calls to VaultAnyConfig instance
    mock_va.assert_called_once_with("test_not_a_vault_conf_file.blargh", ac_parser=None)
    mock_va.return_value.auto_auth.assert_called_once_with("test_not_a_vault_creds_file.blargh", ac_parser=None)
    mock_va.return_value.loads.assert_called_once_with(
        "test_not_a_conf_file.blargh", ac_parser=None, process_secret_files=False
    )

    # Validate elastic configuration
    elastic_config = deepcopy(sample_config["elastic"])
    auth_string = quote_plus(elastic_config["user"]) + ":" + quote_plus(elastic_config["pwd"])
    elastic_config.update({"http_auth": auth_string})
    del elastic_config["user"]
    del elastic_config["pwd"]
    mock_connections.assert_called_once_with(hosts=[elastic_config])
    assert config.ES_INDEX == elastic_config["index"]
