# contracts

Load for Solidity, foundry, DeFi mechanics and gas.

## solidity

```solidity
function withdraw(uint256 amount) external {
    uint256 bal = balance[msg.sender];
    if (amount > bal) revert InsufficientBalance(amount, bal);
    balance[msg.sender] = bal - amount;          // effect
    (bool ok, ) = msg.sender.call{value: amount}(""); // interaction
    if (!ok) revert TransferFailed();
}
```

- Custom errors over strings: cheaper and typed.
- `immutable` and `constant` where possible, `unchecked` only with a proof.
- Storage is 32-byte slots. Pack structs; a bool and a uint128 share a slot.
- `calldata` over `memory` for read-only args.
- Events for every state change. An indexer cannot see storage history.

## foundry

```bash
forge init
forge test --match-test testWithdraw -vvvv
forge snapshot --diff
forge script script/Deploy.s.sol --fork-url $RPC --broadcast --verify
```

| test type | use |
| --- | --- |
| unit | each function, each revert |
| fuzz | `function testFuzz(uint256 x)`, invariants |
| invariant | `invariant_` functions, handler-based |
| fork | real state, real oracle, real token decimals |

A fork test without a pinned block number is not reproducible.

## defi

| primitive | invariant | failure |
| --- | --- | --- |
| AMM | `k` never decreases after fees | donation attack on first deposit |
| lending | total borrows <= total supply | oracle manipulation on liquidation |
| vault | shares * price == assets | rounding drain on repeated deposit |
| staking | reward per share monotonic | reward dilution by late depositor |

- First-depositor share inflation: mint dead shares, or seed the vault.
- Oracle: use a TWAP with a window, check `updatedAt`, and bound the answer.
- Flash loan: assume any balance can change inside one transaction.

## access

- `Ownable2Step` or a role manager. A single-step transfer to a wrong address is unrecoverable.
- `pause` for deposits, never for withdrawals.
- Timelock on parameter changes the protocol depends on.

## gas

- Storage write 20k, read 2.1k warm. Batch writes, avoid a write per loop iteration.
- `uint256` arrays over structs with padding when iterating.
- Measure: `forge test --gas-report`. Optimize the top three functions only.

## pre-audit

1. Freeze the commit hash. Audit runs on that hash.
2. Write the invariants and the threat model.
3. Slither clean, or every finding justified in writing.
4. Test coverage over 90% on the value-moving paths, not overall.
