# chains

Load for Stellar, Soroban, wallets, L2 and indexers.

## evm fundamentals

- Account: nonce, balance, code, storage. An eoa has no code.
- Transaction: `to`, `value`, `data`, `gasLimit`, `maxFeePerGas`, `maxPriorityFeePerGas`, `nonce`, `chainId`.
- Receipt: status, gasUsed, logs. A pending transaction is not a result.
- Confirmations: wait for the chain's finality rule, not for one block.

## l2 and bridges

| risk | check |
| --- | --- |
| sequencer downtime | escape hatch documented and tested |
| withdrawal delay | 7 days on optimistic rollups, plan the ux |
| bridge custody | who holds the funds, what the upgrade key is |
| message replay | nonce and chain id in the signed payload |

## stellar

- A new account needs 1 XLM base reserve plus 0.5 per trustline or subentry; `createAccount` fails below it.
- Assets are trustlines: `changeTrust` before receiving a non-native asset.
- Memo required by many exchanges; a missing memo loses the deposit.
- Operations batch in a transaction, all or nothing.

## soroban

```rust
#[contractimpl]
impl Vault {
    pub fn deposit(env: Env, from: Address, amount: i128) -> i128 {
        from.require_auth();
        let key = DataKey::Balance(from.clone());
        let bal: i128 = env.storage().persistent().get(&key).unwrap_or(0);
        env.storage().persistent().set(&key, &(bal + amount));
        bal + amount
    }
}
```

- `require_auth` on every address whose state changes. No implicit caller.
- Storage tiers: temporary, persistent, instance. Persistent entries need a ttl bump or they archive.
- Amounts are `i128` in stroops. One asset unit is 10^7 stroops.
- Contract state is not enumerable: keep an index in a separate entry.

## wallets

- `personal_sign` for a message, `eth_signTypedData_v4` for structured data with a domain separator.
- Chain id in the domain, or a signature replays on another chain.
- Never sign a transaction the ui did not display in full. Decode and show `to`, `value`, `method`.
- Session keys for a game or agent, scoped by contract, method and expiry.

## indexers

- Reorgs: keep a confirmation depth, roll back by block hash, never by number alone.
- Idempotent handlers keyed by `(txHash, logIndex)`.
- Backfill from the deploy block, not from genesis.
- Store the decoded event, plus the raw log for replay.
## foundations index

| topic | the rule that matters |
| --- | --- |
| Formal verification | Certora or Scribble: write the invariant as a rule, run it on every PR; a passing fuzz run is not a proof. |
| Rate limiting and circuit breakers | A relayer needs a per-key rate limit and a breaker that stops on 5 consecutive RPC failures, or it burns gas on a dead endpoint. |
| Relayer pool management | One nonce per relayer, a queue per key; two concurrent sends from one key collide on the nonce. |
| Yield allocation | Cap per protocol, rebalance on a threshold not a timer, and check the withdrawal path before depositing. |
| Pool screening | Token allowlist, holder concentration, mint authority renounced; a pool with a live mint is a rug with extra steps. |
| Soroban liquidity pool | Soroban AMM: `require_auth` on the depositor, storage TTL extended on every touch, or the pool entry expires. |
| Anchors | SEP-24 interactive deposit and SEP-31 cross-border; the anchor's callback is the only settlement truth. |
| Clawback compliance | Stellar clawback-enabled assets: the issuer can revoke; an asset without it cannot satisfy a regulated issuer. |
| Solana | Anchor framework, accounts are explicit in the instruction, `rent-exempt` minimum; a missing signer check is the classic bug. |
| NFT standards | ERC-721 for unique, ERC-1155 for editions; `tokenURI` must be immutable or the metadata can be swapped after sale. |
| Spec compliance | SEP-1 for Stellar assets, ERC-20 `decimals` and `totalSupply` semantics; a non-compliant token breaks every integrator. |

## chains, proofs and infrastructure

Light clients verify a header chain and a proof, not the whole state; a relayer submits proofs, an indexer replays logs. Batch proofs where the chain charges per verification, and store the block number with every derived row so a reorg can be rolled back to the fork point.
