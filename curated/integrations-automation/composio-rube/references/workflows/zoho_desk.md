# zoho_desk - deep workflow

App: Zoho Desk  |  Docs: https://composio.dev/toolkits/zoho_desk

Sources merged: 2 (2 detailed).


---

## Source: `catalog/integrations-automation/composio-zoho-desk-automation`

# Zoho Desk Automation

> **Status: Toolkit Not Available** -- RUBE_SEARCH_TOOLS returned no `zoho_desk`-specific tools. The Zoho Desk toolkit is not currently available in Composio's tool catalog. Searches returned tools from unrelated helpdesk and CRM toolkits instead.

**Toolkit docs:** [composio.dev/toolkits/zoho_desk](https://composio.dev/toolkits/zoho_desk)

---

## Setup

1. Add the Rube MCP server to your environment: `https://rube.app/mcp`
2. Check availability by calling `RUBE_SEARCH_TOOLS` with Zoho Desk-related queries
3. If `ZOHO_DESK_*` tools appear in the future, connect via `RUBE_MANAGE_CONNECTIONS` with toolkit `zoho_desk`

---

## Current Status

As of the last tool discovery scan, no `ZOHO_DESK_*` tool slugs were returned by RUBE_SEARCH_TOOLS. Queries for Zoho Desk ticket management, contacts, agents, and departments all returned tools from other toolkits:

- Ticket creation queries returned **Freshdesk** (`FRESHDESK_CREATE_TICKET`), **HubSpot** (`HUBSPOT_CREATE_TICKET`), and **Zendesk** (`ZENDESK_CREATE_ZENDESK_TICKET`) tools
- Contact listing queries returned **Zoho Invoice** (`ZOHO_INVOICE_LIST_CONTACTS`) tools
- Agent/department queries returned **Zoho CRM** (`ZOHO_GET_ZOHO_USERS`) tools

This indicates the `zoho_desk` toolkit either has no tools registered or is not yet integrated into the Composio platform.

---

## Alternatives

If you need helpdesk and support ticket automation, consider these available toolkits:

| Need | Alternative Toolkit | Example Tools |
|------|-------------------|---------------|
| Ticket management | Freshdesk | `FRESHDESK_CREATE_TICKET`, `FRESHDESK_UPDATE_TICKET` |
| Ticket management | Zendesk | `ZENDESK_CREATE_ZENDESK_TICKET` |
| Ticket management | HubSpot | `HUBSPOT_CREATE_TICKET`, `HUBSPOT_LIST_TICKETS` |
| CRM records | Zoho CRM | `ZOHO_CREATE_ZOHO_RECORD`, `ZOHO_GET_ZOHO_USERS` |
| Contact management | Zoho Invoice | `ZOHO_INVOICE_LIST_CONTACTS` |

---

## When Tools Become Available

Once Zoho Desk tools are added to Composio, this skill should be updated with real tool slugs, schemas, and pitfalls following the same pattern as other automation skills in this collection.

---

*Powered by [Composio](https://composio.dev)*


---

## Source: `catalog/integrations-automation/composio-zoho_desk-automation`

# Zoho Desk Automation via Rube MCP

Automate Zoho Desk operations through Composio's Zoho Desk toolkit via Rube MCP.

**Toolkit docs**: [composio.dev/toolkits/zoho_desk](https://composio.dev/toolkits/zoho_desk)

## Prerequisites

- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active Zoho Desk connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `zoho_desk`
- Always call `RUBE_SEARCH_TOOLS` first to get current tool schemas

## Setup

**Get Rube MCP**: Add `https://rube.app/mcp` as an MCP server in your client configuration. No API keys needed — just add the endpoint and it works.

1. Verify Rube MCP is available by confirming `RUBE_SEARCH_TOOLS` responds
2. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `zoho_desk`
3. If connection is not ACTIVE, follow the returned auth link to complete setup
4. Confirm connection status shows ACTIVE before running any workflows

## Tool Discovery

Always discover available tools before executing workflows:

```
RUBE_SEARCH_TOOLS: queries=[{"use_case": "tickets, contacts, agents, departments, and help desk operations", "known_fields": ""}]
```

This returns:
- Available tool slugs for Zoho Desk
- Recommended execution plan steps
- Known pitfalls and edge cases
- Input schemas for each tool

## Core Workflows

### 1. Discover Available Zoho Desk Tools

```
RUBE_SEARCH_TOOLS:
  queries:
    - use_case: "list all available Zoho Desk tools and capabilities"
```

Review the returned tools, their descriptions, and input schemas before proceeding.

### 2. Execute Zoho Desk Operations

After discovering tools, execute them via:

```
RUBE_MULTI_EXECUTE_TOOL:
  tools:
    - tool_slug: "<discovered_tool_slug>"
      arguments: {<schema-compliant arguments>}
  memory: {}
  sync_response_to_workbench: false
```

### 3. Multi-Step Workflows

For complex workflows involving multiple Zoho Desk operations:

1. Search for all relevant tools: `RUBE_SEARCH_TOOLS` with specific use case
2. Execute prerequisite steps first (e.g., fetch before update)
3. Pass data between steps using tool responses
4. Use `RUBE_REMOTE_WORKBENCH` for bulk operations or data processing

## Common Patterns

### Search Before Action
Always search for existing resources before creating new ones to avoid duplicates.

### Pagination
Many list operations support pagination. Check responses for `next_cursor` or `page_token` and continue fetching until exhausted.

### Error Handling
- Check tool responses for errors before proceeding
- If a tool fails, verify the connection is still ACTIVE
- Re-authenticate via `RUBE_MANAGE_CONNECTIONS` if connection expired

### Batch Operations
For bulk operations, use `RUBE_REMOTE_WORKBENCH` with `run_composio_tool()` in a loop with `ThreadPoolExecutor` for parallel execution.

## Known Pitfalls

- **Always search tools first**: Tool schemas and available operations may change. Never hardcode tool slugs without first discovering them via `RUBE_SEARCH_TOOLS`.
- **Check connection status**: Ensure the Zoho Desk connection is ACTIVE before executing any tools. Expired OAuth tokens require re-authentication.
- **Respect rate limits**: If you receive rate limit errors, reduce request frequency and implement backoff.
- **Validate schemas**: Always pass strictly schema-compliant arguments. Use `RUBE_GET_TOOL_SCHEMAS` to load full input schemas when `schemaRef` is returned instead of `input_schema`.

## Quick Reference

| Operation | Approach |
|-----------|----------|
| Find tools | `RUBE_SEARCH_TOOLS` with Zoho Desk-specific use case |
| Connect | `RUBE_MANAGE_CONNECTIONS` with toolkit `zoho_desk` |
| Execute | `RUBE_MULTI_EXECUTE_TOOL` with discovered tool slugs |
| Bulk ops | `RUBE_REMOTE_WORKBENCH` with `run_composio_tool()` |
| Full schema | `RUBE_GET_TOOL_SCHEMAS` for tools with `schemaRef` |

> **Toolkit docs**: [composio.dev/toolkits/zoho_desk](https://composio.dev/toolkits/zoho_desk)
