# payments

Load for payment flows, webhooks and third-party integrations.

## flow

```
client -> create intent (server) -> provider -> webhook -> server updates state -> client polls or receives event
```

- The server creates the intent from its own price record: the client sends `price_id`, never `amount`.
- Amount from the server's price table, not from the request body.
- Store the provider id, the state and the idempotency key.

## webhooks

```ts
const sig = req.headers.get('stripe-signature');
const event = provider.webhooks.constructEvent(rawBody, sig, secret); // throws on mismatch
if (await seen(event.id)) return ok();       // dedupe by event id
await handle(event);
await markSeen(event.id);
```

- Verify the signature on the raw body, before parsing.
- Dedupe by event id. Providers retry for days.
- Return 2xx fast, process async. A slow handler causes retries and duplicates.
- Order is not guaranteed. Fetch the current state from the provider when it matters.
- Reconcile daily: provider state vs your state, alert on drift.

## money

| rule | reason |
| --- | --- |
| integer minor units | float rounding loses cents |
| currency code stored with the amount | no implicit default |
| no arithmetic on formatted strings | locale parsing breaks |
| rounding rule stated | half-up vs banker's changes totals |

## refunds and disputes

- Refund by provider id, never by recomputing the amount.
- Record the reason and the actor.
- A dispute has a deadline. Put it in a queue with an alarm.

## failure modes

| case | handling |
| --- | --- |
| provider timeout on charge | query by idempotency key before retrying |
| webhook arrives before the intent is stored | buffer, retry, reconcile |
| duplicate webhook | idempotent handler |
| currency mismatch | reject, log, alert |
| test mode key in production | startup check, refuse to boot |

## review

- Amount derived server side.
- Idempotency key on every create.
- Webhook signature verified, event deduped.
- Reconciliation job exists and has run.
- No card data touches the server: use the provider's hosted fields.
## provider index

| provider | the rule that matters |
| --- | --- |
| PayPal | Two-step: create order, then capture; a capture is idempotent only with `PayPal-Request-Id`. |
| Plaid | `access_token` is per item; webhook `TRANSFER` events must be verified by JWT, and sandbox data expires. |
| Pakistan payments stack | Local rails (JazzCash, Easypaisa, Raast) settle in PKR; a 3DS step is required and the callback is the only truth. |
| DoomPay | Crypto checkout: confirmations vary by chain, credit only after the configured confirmation count. |
| x402 | HTTP 402 payment wrapper: the client retries with a payment header; verify the receipt before serving the resource. |
| Nano | Feeless and irreversible: a send is final, so a wrong address is unrecoverable. |
| Twilio | SMS and voice: `MessagingServiceSid` for pools, status callback for delivery, signature `X-Twilio-Signature` on inbound. |
| Sendblue | iMessage API: a blue-bubble reply needs a verified sender; delivery receipts arrive as webhooks, not responses. |
| TextMe | SMS gateway: per-country sender ids, DLT registration for India, opt-out keyword handling is mandatory. |
| RestoSignals | Restaurant order feed: dedupe on the provider order id, a replayed ticket duplicates the kitchen order. |
| ComfyUI Gateway | Async image jobs: submit returns a prompt id, poll the history endpoint, a failed node returns a partial graph. |
| Fal platform | Queue API: `fal.subscribe` streams progress; a model timeout still bills the GPU seconds used. |
