# Brownie-Events-Logs

This project demonstrates how to work with events in hardhat. In the `deploy_and_store` script, you'll see the output of the events. 

 ## Requirements

- [brownie](https://eth-brownie.readthedocs.io/en/stable/install.html)
  - You can test it's installed by running `brownie --version`
- [python](https://www.python.org/downloads/)
  - You can test it's installed by running `python --version` or `python3 --version`
- [nodejs](https://nodejs.org/en/download/)
  - You can test it's installed by running `node --version`
- [yarn](https://yarnpkg.com/)
  - You can test it's installed by running `yarn --version`
- [git](https://git-scm.com/downloads)
  - You can test it's installed by running `git --version`
- [ganache-cli](https://www.npmjs.com/package/ganache-cli)
  - You can test it's installed by running `ganache-cli --version`

## Installation

Git clone this repo

```sh
git clone brownie-events-logs
cd brownie-events-logs
```

## Quickstart

Run:
```sh
brownie run scripts/deploy_and_store.py
```

And this will print out the events.

## Testnet deployment

To deploy to a testnet, you'll need.

1. [A Blockchain wallet](https://metamask.io/)
2. [Testnet Kovan ETH](https://faucets.chain.link/) in your Blockchain Wallet.
3. [An alchemy RPC URL](https://www.alchemy.com/)
4. [An Etherscan API Key](https://etherscan.io/apis)

Then, create a `.env` file and add the following lines:
```
ETHERSCAN_API_KEY=ABC123ABC123ABC123ABC123ABC123ABC1
KOVAN_RPC_URL=https://eth-ropsten.alchemyapi.io/v2/<YOUR ALCHEMY KEY>
PRIVATE_KEY=YOUR_BLOCKCHAIN_WALLET_PRIVATE_KEY
```
DO NOT PUSH YOUR PRIVATE_KEY TO GITHUB. Please test and develop with a private key that doesn't have any real money in it. 

Follow the [basics tutorial](https://docs.chain.link/docs/beginners-tutorial/) to learn how to get everything setup. 

Then, run:

```sh
brownie run scripts/deploy_and_store.js --network kovan
```

And it will deploy and auto-verify for you. 

## Testing

```sh
brownie test
```
