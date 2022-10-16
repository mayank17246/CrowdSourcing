from brownie import accounts, SimpleStorage, network


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrive()
    expected = 0
    # Assert
    assert starting_value == expected


# def get_account():
#    if network.show_active() == "development":
#        return accounts[0]
#    else:
#        return accounts.add(config{})


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 16
    simple_storage.store(expected, {"from": account})
    # Assert
    assert expected == simple_storage.retrive()
