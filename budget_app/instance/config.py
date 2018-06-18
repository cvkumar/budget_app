import os


# Fill in your Plaid API keys - https://dashboard.plaid.com/account/keys
# Use 'sandbox' to test with Plaid's Sandbox environment (username: user_good, password: pass_good)
# Use `development` to test with live user

# Plaid Credentials

def set_private_environment_variables():
    os.environ["PLAID_CLIENT_ID"] = "<insert_yours>"
    os.environ["PLAID_PUBLIC_KEY"] = "<insert_yours>"
    os.environ["PLAID_SECRET"] = "<insert_yours>"
    os.environ["PLAID_ENV"] = "<insert_yours>"

    # Localhost
    os.environ["POSTGRES_USER"] = "<insert_yours>"
    os.environ["POSTGRES_PASSWORD"] = "<insert_yours>"
    os.environ["POSTGRES_HOST"] = "<insert_yours>"
    os.environ["DATABASE"] = "<insert_yours>"
