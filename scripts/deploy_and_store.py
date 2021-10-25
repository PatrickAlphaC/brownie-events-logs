from brownie import SimpleStorage, config, network
from scripts.helpful_scripts import get_account


def deploy():
    account = get_account()
    simple_storage = SimpleStorage.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get(
            "publish_source", False
        ),
    )
    tx = simple_storage.store(1, {"from": account})
    tx.wait(1)
    print(tx.events)
    print(tx.events[0]["oldNumber"])
    print(tx.events[0]["newNumber"])
    print(tx.events[0]["addedNumber"])
    print(tx.events[0]["sender"])


def main():
    deploy()
