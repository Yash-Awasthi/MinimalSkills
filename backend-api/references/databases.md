# databases

Load for schema design, queries, indexes and migrations.

## schema

```sql
create table invoices (
  id           uuid primary key default gen_random_uuid(),
  owner_id     uuid not null references users(id),
  amount_cents bigint not null check (amount_cents > 0),
  status       text not null default 'draft',
  created_at   timestamptz not null default now()
);
create index invoices_owner_created on invoices (owner_id, created_at desc);
```

- Money as integer minor units. Never float.
- Timestamps with time zone. Store utc.
- Constraints in the database: not null, foreign key, check, unique.
- Soft delete only when restore is a product requirement, and index the filter.

## indexes

| query shape | index |
| --- | --- |
| `where owner_id = ?` | `(owner_id)` |
| `where owner_id = ? order by created_at desc` | `(owner_id, created_at desc)` |
| `where lower(email) = ?` | expression index on `lower(email)` |
| `where tags @> ?` | gin on the array or jsonb column |
| `where a = ? and b > ?` | `(a, b)` |

- Index the columns in the predicate, in selectivity order.
- A composite index serves the leftmost prefix only.
- Unused indexes cost writes. Check `pg_stat_user_indexes`.

## explain

```sql
explain (analyze, buffers) select * from invoices where owner_id = $1 order by created_at desc limit 50;
```

Look for seq scan on a large table, rows removed by filter, and a sort that could be an index. Estimate mismatch over 10x means stale statistics: `analyze invoices;`.

## n+1

```ts
// wrong
for (const i of invoices) await db.user(i.ownerId);

// right
const users = await db.user.whereIn('id', invoices.map((i) => i.ownerId));
```

## migrations

- Forward and back, or marked one-way with a snapshot.
- Add column nullable, backfill in batches, then add the constraint.
- Never rename in place: add, dual-write, migrate readers, drop.
- Lock-safe: `create index concurrently`, small batches, no long transaction.
- Test on a copy with production-sized data.

## transactions

- Keep a transaction under 100ms and free of network calls; a third-party call inside holds row locks for its whole timeout.
- One isolation level per use case, stated.
- Retry serialization failures with a bounded backoff.

## engines

| engine | use | watch |
| --- | --- | --- |
| Postgres | default relational store | connection pool, `create index concurrently`, `jsonb` for sparse fields |
| MySQL | existing schema, replication topology | implicit casts, no partial indexes |
| Redis | cache, rate limit counters, queue, lock | eviction policy, no durability guarantee, key TTL discipline |
| MongoDB | document shape that changes per record | unbounded arrays, no join across collections |

Postgres specifics: `explain (analyze, buffers)`, partial indexes for soft-delete filters, `vacuum` after a bulk load, and statement timeout set per role.

Redis specifics: never the source of truth for money or auth state, set `maxmemory-policy` explicitly, and namespace keys by tenant.

## review

- Every new query has an index plan.
- Migration time estimated on a copy, labeled as estimate if not measured.
- No `select *` in application code.
