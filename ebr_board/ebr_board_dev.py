"""
Used for launching the dev-mode of the erb_board. **Don't use in production**.
"""
import ebr_board

if __name__ == "__main__":
    ebr_board.create_app(
        config_filename="config.yaml",
        vault_config_filename="vault.yaml",
        vault_creds_filename="vault.yaml",
        load_certs=True,
    ).run(debug=True)
