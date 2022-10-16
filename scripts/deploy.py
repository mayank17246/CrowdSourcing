from abc import update_abstractmethods
from brownie import accounts, SimpleStorage


def deploy_simple_storage():
    account = accounts[0]
    # account = accounts.load("my-account")
    # print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    # Tranact or call
    # print(simple_storage)
    stored_value = simple_storage.retrive()
    print(stored_value)
    transaction = simple_storage.store(16, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrive()
    print(updated_stored_value)


def main():
    deploy_simple_storage()
