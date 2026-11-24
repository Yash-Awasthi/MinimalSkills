# state-data

Load for fetching, caching, mutations and forms.

## split

| state | owner | tool |
| --- | --- | --- |
| server data | query cache | TanStack Query, SWR, RSC |
| url | router | search params |
| form draft | component | local state or form library |
| global ui | store | Zustand, signals |
| derived | computed | selector, `useMemo` with a measured cost |

Copying server data into a store creates two truths. Pick one.

## queries

```ts
useQuery({ queryKey: ['invoice', id], queryFn: () => api.invoice(id), staleTime: 30_000 });
```

- Query key is cache identity. Include every parameter that changes the result.
- `staleTime` for how long data is fresh, `gcTime` for how long it is kept.
- Do not refetch on every mount for stable data.
- Cancel on unmount: pass the `AbortSignal` to `fetch`.

## mutations

```ts
useMutation({
  mutationFn: api.updateInvoice,
  onMutate: async (next) => {
    await qc.cancelQueries({ queryKey: ['invoice', next.id] });
    const prev = qc.getQueryData(['invoice', next.id]);
    qc.setQueryData(['invoice', next.id], next);
    return { prev };
  },
  onError: (_e, next, ctx) => qc.setQueryData(['invoice', next.id], ctx?.prev),
  onSettled: () => qc.invalidateQueries({ queryKey: ['invoice'] }),
});
```

- Optimistic only when the UI can recover.
- Server-owned fields: wait for the response.
- Non-idempotent write: never auto-retry. Use an idempotency key.
- Invalidate the list and the detail, not just one.

## errors

- One error shape: `{ code, message, fieldErrors? }`.
- Map codes to user text. Never render a server message raw.
- Retry only transient classes: 408, 429, 5xx. Honor `Retry-After`.
- Total deadline per request. A retry chain without a deadline hangs the UI.

## contracts

- Zod for the schema: one object, parsed at the boundary, type inferred from it.
- tRPC when client and server share a TypeScript repo: procedures typed end to end, no hand-written client.
- Do not pair tRPC with a REST client for the same resource. One transport per resource.

## forms

```ts
const Schema = z.object({ amount: z.coerce.number().int().positive() });
const parsed = Schema.safeParse(Object.fromEntries(formData));
if (!parsed.success) return { fieldErrors: parsed.error.flatten().fieldErrors };
```

- Parse once at the boundary. The parsed type is the only shape downstream.
- Show errors per field. A toast for a field error is a defect.
- Keep submitted values on error; a 20-field form that clears on a 422 is a lost user, not a retry.
- Disable double submit with a pending state, not a timeout.

## loading and empty

Four states per view: loading, empty, error, success. A view with three is incomplete.

## review

- No fetch in a render body.
- No `useEffect` that mirrors props into state.
- No index keys on reorderable lists.
