---
name: web3-blockchain
description: Use when building on a blockchain: Solidity contracts and foundry tests, upgrade and access patterns, DeFi mechanics, Stellar and Soroban contracts, wallet and signing flows, indexers and RPC, gas and audit prep. Triggers: solidity, foundry, contract, wallet, Soroban, gas.
---

# web3-blockchain

## use when

- Solidity contract, test, deployment -> references/contracts.md
- token, vault, AMM, lending mechanics -> references/contracts.md
- Stellar asset or Soroban contract -> references/chains.md
- wallet connect, signing, transaction build -> references/chains.md
- indexer, RPC, event ingestion, reorg handling

not for: backend endpoint shape (backend-api), key custody policy (security-operations)

## rules

- Conflict order: invariants, then access control, then gas; gas never buys a weaker check.
- Deployed code is immutable: test the failure paths before deploy, and state the chain and block for every result.
- Every external call is a reentrancy risk: checks, effects, interactions, or a guard, with slippage, deadline and oracle staleness as parameters.
- Access control explicit per function; no default-open admin, no `tx.origin`.
- Amounts are integers in the smallest unit; never float, never a decimal string.
- Private keys never touch a repo, a log or an agent transcript.

## change

1. Locate: the function, its storage layout, and the test that covers the invariant.
2. Propose the contract change in one sentence, with the pattern you rejected.
3. Predict before compiling: gas delta, storage slot shift, which invariant could break.
4. Back up the original contract and its storage layout in context, pinned to the commit.
5. Apply one concern per edit; a logic fix and a storage change are two deploys.
6. Verify: `forge test -vvv --fuzz-runs 10000`, coverage, then a fork simulation.
7. Regress: every caller contract, the deploy script and the access-control test.
8. Compare gas and traces against the prediction; a shifted slot stops the deploy.
9. Report test and fuzz counts, chain and block, then take the next item.

## contract

1. Write the invariant first: what must always hold.
2. Implement checks, effects, interactions.
3. Test the happy path, each revert, reentrancy, access, boundary amounts.
4. Fuzz the invariants.

```solidity
contract Vault {
    mapping(address => uint256) public shares;
    function withdraw(uint256 amount) external {
        shares[msg.sender] -= amount;              // effects first
        (bool ok, ) = msg.sender.call{value: amount}("");
        require(ok, "transfer failed");            // interaction last
    }
}
```

```bash
forge test -vvv --fuzz-runs 10000
forge coverage --report summary
slither . --config-file slither.config.json
```

The test that matters: `vm.expectRevert()` on a withdraw larger than the balance, and a fuzz invariant that the contract balance never drops below the sum of shares.

5. Simulate the deploy on a fork before broadcasting.
6. Verify the source, then transfer ownership to a multisig.

## decide

| condition | action |
| --- | --- |
| upgradeable requested | proxy with a storage layout check, or refuse |
| oracle used | staleness check plus a fallback |
| external call in a loop | pull pattern, not push |
| arithmetic on shares | round in favor of the protocol |
| admin key is an eoa | require a multisig before mainnet |
| gas target missed | measure first, then optimize storage writes |
| audit requested | freeze the commit, audit that hash |

## check

- [ ] invariants written and fuzzed
- [ ] reentrancy guard on every state-changing external call
- [ ] access control per function, tested
- [ ] fork simulation of the deploy script
- [ ] events emitted for every state change
- [ ] no key in the tree: `rg -i "0x[0-9a-f]{64}" .`

## stop

| condition | action |
| --- | --- |
| mainnet deploy requested | confirm chain, key holder, rollback |
| unaudited contract holding funds | refuse to deploy |
| key pasted in chat | stop, rotate it |

## emit

- contracts and addresses per chain
- test and fuzz results with counts
- what was simulated versus deployed
