from scripts.helpful_scripts import get_account
from brownie import SimpleStorage


def test_event_is_fired():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    transaction = simple_storage.store(1, {"from": account})
    transaction.wait(1)
    assert transaction.events["storedNumber"] is not None
    assert transaction.events["storedNumber"]["newNumber"] == 1
    # You can also access the events by index
    assert transaction.events[0]["newNumber"] == 1
