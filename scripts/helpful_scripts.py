from brownie import (
    network,
    accounts,
    config,
)

NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS + [
    "mainnet-fork",
    "binance-fork",
    "matic-fork",
]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])
