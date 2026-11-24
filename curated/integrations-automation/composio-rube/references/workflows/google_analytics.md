# google_analytics - deep workflow

App: Google Ads  |  Docs: https://composio.dev/toolkits/googleads

Sources merged: 2 (2 detailed).


---

## Source: `catalog/integrations-automation/composio-googleads-automation`

# Google Ads Automation via Rube MCP

Access Google Ads data through Google Analytics integration, run performance reports, list linked Ads accounts, and analyze campaign metrics using Rube MCP (Composio).

**Toolkit docs**: [composio.dev/toolkits/googleads](https://composio.dev/toolkits/googleads)

## Prerequisites
- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `google_analytics`
- Always call `RUBE_SEARCH_TOOLS` first to get current tool schemas

## Setup
**Get Rube MCP**: Add `https://rube.app/mcp` as an MCP server in your client configuration. No API keys needed — just add the endpoint and it works.

1. Verify Rube MCP is available by confirming `RUBE_SEARCH_TOOLS` responds
2. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `google_analytics`
3. If connection is not ACTIVE, follow the returned auth link to complete setup
4. Confirm connection status shows ACTIVE before running any workflows

> **Note**: Google Ads data is accessed through the Google Analytics toolkit integration. The tools below use GA4 properties linked to Google Ads accounts.

## Core Workflows

### 1. List Google Ads Links for a Property
Use `GOOGLE_ANALYTICS_ANALYTICS_ADMIN_PROPERTIES_GOOGLE_ADS` to retrieve all Google Ads account links configured for a GA4 property.
```
Tool: GOOGLE_ANALYTICS_ANALYTICS_ADMIN_PROPERTIES_GOOGLE_ADS
Parameters:
  - parent (required): Property resource name (format: "properties/{propertyId}")
  - pageSize: Max results (1-200, default 50)
  - pageToken: Pagination token
```

### 2. Run a GA4 Performance Report
Use `GOOGLE_ANALYTICS_RUN_REPORT` to run customized reports with dimensions, metrics, date ranges, and filters.
```
Tool: GOOGLE_ANALYTICS_RUN_REPORT
Parameters:
  - property (required): Property resource (format: "properties/{property_id}")
  - dimensions: Array of dimension objects (e.g., [{"name": "sessionCampaignName"}, {"name": "date"}])
  - metrics: Array of metric objects (e.g., [{"name": "sessions"}, {"name": "totalRevenue"}])
  - dateRanges: Array with startDate and endDate (e.g., [{"startDate": "2025-01-01", "endDate": "2025-01-31"}])
  - dimensionFilter: Filter by dimension values
  - metricFilter: Filter by metric values (applied after aggregation)
  - orderBys: Sort results
  - limit: Max rows to return (1-250000)
```

### 3. Check Dimension/Metric Compatibility
Use `GOOGLE_ANALYTICS_CHECK_COMPATIBILITY` to validate dimension and metric combinations before running a report.
```
Tool: GOOGLE_ANALYTICS_CHECK_COMPATIBILITY
Description: Validates compatibility of chosen dimensions or metrics
  before running a report.
Note: Call RUBE_SEARCH_TOOLS to get the full schema for this tool.
```

### 4. List GA4 Accounts
Use `GOOGLE_ANALYTICS_LIST_ACCOUNTS` to enumerate all accessible Google Analytics accounts.
```
Tool: GOOGLE_ANALYTICS_LIST_ACCOUNTS
Parameters:
  - pageSize: Max accounts to return
  - pageToken: Pagination token
  - showDeleted: Include soft-deleted accounts
```

### 5. List GA4 Properties Under an Account
Use `GOOGLE_ANALYTICS_LIST_PROPERTIES` to list properties for a specific GA4 account.
```
Tool: GOOGLE_ANALYTICS_LIST_PROPERTIES
Parameters:
  - account (required): Account resource name (format: "accounts/{account_id}")
  - pageSize: Max properties (1-200)
  - pageToken: Pagination token
  - showDeleted: Include trashed properties
```

### 6. Get Available Dimensions and Metrics
Use `GOOGLE_ANALYTICS_GET_METADATA` to discover all available fields for building reports.
```
Tool: GOOGLE_ANALYTICS_GET_METADATA
Description: Gets metadata for dimensions, metrics, and comparisons
  for a GA4 property.
Note: Call RUBE_SEARCH_TOOLS to get the full schema for this tool.
```

## Common Patterns

- **Discover then report**: Use `GOOGLE_ANALYTICS_LIST_ACCOUNTS` to find account IDs, then `GOOGLE_ANALYTICS_LIST_PROPERTIES` to find property IDs, then `GOOGLE_ANALYTICS_RUN_REPORT` to pull data.
- **Validate before querying**: Use `GOOGLE_ANALYTICS_CHECK_COMPATIBILITY` to validate dimension/metric combinations before running reports to avoid 400 errors.
- **Campaign performance**: Run reports with dimensions like `sessionCampaignName`, `sessionSource`, `sessionMedium` and metrics like `sessions`, `activeUsers`, `totalRevenue`.
- **Ads link discovery**: Use `GOOGLE_ANALYTICS_ANALYTICS_ADMIN_PROPERTIES_GOOGLE_ADS` to find which Google Ads accounts are linked to each GA4 property.
- **Field discovery**: Use `GOOGLE_ANALYTICS_GET_METADATA` to list all available dimensions and metrics before constructing complex reports.

## Known Pitfalls

- **Dimension/metric compatibility**: The GA4 API has strict compatibility rules. Not all dimensions can be combined with all metrics. Demographic dimensions (e.g., `userAgeBracket`, `userGender`) are often incompatible with session-scoped dimensions/filters (e.g., `sessionCampaignName`, `sessionSource`).
- **`dateRange` is NOT a dimension**: Do not include `dateRange` in the dimensions array. Use `date`, `dateHour`, `year`, `month`, or `week` instead.
- **`exits` is NOT valid**: Neither `exits` as a dimension nor as a metric is valid in GA4.
- **Property ID format**: Must be `properties/{numeric_id}` (e.g., `properties/123456789`). Do not use Google Account IDs (long OAuth IDs).
- **Account ID format**: Must be `accounts/{numeric_id}` where the numeric ID is 6-10 digits.
- **Filter separation**: Use `dimensionFilter` only for dimension fields and `metricFilter` only for metric fields. Mixing them will cause errors.
- **Max 9 dimensions and 10 metrics** per report request.

## Quick Reference
| Action | Tool | Key Parameters |
|--------|------|----------------|
| List Ads links | `GOOGLE_ANALYTICS_ANALYTICS_ADMIN_PROPERTIES_GOOGLE_ADS` | `parent` |
| Run report | `GOOGLE_ANALYTICS_RUN_REPORT` | `property`, `dimensions`, `metrics`, `dateRanges` |
| Check compatibility | `GOOGLE_ANALYTICS_CHECK_COMPATIBILITY` | (see full schema via RUBE_SEARCH_TOOLS) |
| List accounts | `GOOGLE_ANALYTICS_LIST_ACCOUNTS` | `pageSize` |
| List properties | `GOOGLE_ANALYTICS_LIST_PROPERTIES` | `account`, `pageSize` |
| Get metadata | `GOOGLE_ANALYTICS_GET_METADATA` | (see full schema via RUBE_SEARCH_TOOLS) |

---
*Powered by [Composio](https://composio.dev)*


---

## Source: `catalog/integrations-automation/sickn33-google-analytics-automation`

# Google Analytics Automation via Rube MCP

Automate Google Analytics 4 (GA4) reporting and property management through Composio's Google Analytics toolkit via Rube MCP.

## Prerequisites

- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active Google Analytics connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `google_analytics`
- Always call `RUBE_SEARCH_TOOLS` first to get current tool schemas

## Setup

**Get Rube MCP**: Add `https://rube.app/mcp` as an MCP server in your client configuration. Adding an endpoint does not authorize Google access; use the host’s supported authentication and the user-approved account.


1. Verify Rube MCP is available by confirming `RUBE_SEARCH_TOOLS` responds
2. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `google_analytics`
3. If connection is not ACTIVE, follow the returned auth link to complete Google OAuth
4. Confirm connection status shows ACTIVE before running any workflows

## Core Workflows

Confirm the exact GA4 property/account and reporting timezone. Record date ranges, attribution scope and response metadata (thresholding, sampling, data-loss/other-row flags) when interpreting results. Distinct users are not additive across rows or days. Use current metadata for key-event metric names rather than assuming `conversions` remains supported. Read-only analysis does not authorize creating/deleting key events or changing property settings; perform such writes only on a specific user request, and read back the result.

### 1. List Accounts and Properties

**When to use**: User wants to discover available GA4 accounts and properties

**Tool sequence**:
1. `GOOGLE_ANALYTICS_LIST_ACCOUNTS` - List all accessible GA4 accounts [Required]
2. `GOOGLE_ANALYTICS_LIST_PROPERTIES` - List properties under an account [Required]

**Key parameters**:
- `pageSize`: Number of results per page
- `pageToken`: Pagination token from previous response
- `filter`: Filter expression for properties (e.g., `parent:accounts/12345`)

**Pitfalls**:
- Property IDs are numeric strings prefixed with 'properties/' (e.g., 'properties/123456')
- Account IDs are prefixed with 'accounts/' (e.g., 'accounts/12345')
- Always list accounts first, then properties under each account
- Pagination required for organizations with many properties

### 2. Run Standard Reports

**When to use**: User wants to query metrics and dimensions from GA4 data

**Tool sequence**:
1. `GOOGLE_ANALYTICS_LIST_PROPERTIES` - Get property ID [Prerequisite]
2. `GOOGLE_ANALYTICS_GET_METADATA` - Discover available dimensions and metrics [Optional]
3. `GOOGLE_ANALYTICS_CHECK_COMPATIBILITY` - Verify dimension/metric compatibility [Optional]
4. `GOOGLE_ANALYTICS_RUN_REPORT` - Execute the report query [Required]

**Key parameters**:
- `property`: Property ID (e.g., 'properties/123456')
- `dateRanges`: Array of date range objects with `startDate` and `endDate`
- `dimensions`: Array of dimension objects with `name` field
- `metrics`: Array of metric objects with `name` field
- `dimensionFilter` / `metricFilter`: Filter expressions
- `orderBys`: Sort order configuration
- `limit`: Maximum rows to return
- `offset`: Row offset for pagination

**Pitfalls**:
- Date format is 'YYYY-MM-DD' or relative values like 'today', 'yesterday', '7daysAgo', '30daysAgo'
- Not all dimensions and metrics are compatible; use CHECK_COMPATIBILITY first
- Use GET_METADATA to discover valid dimension and metric names
- Maximum 9 dimensions per report request
- Row limit defaults vary; set explicitly for large datasets
- `offset` is for result pagination, not date pagination

### 3. Run Batch Reports

**When to use**: User needs multiple different reports from the same property in one call

**Tool sequence**:
1. `GOOGLE_ANALYTICS_LIST_PROPERTIES` - Get property ID [Prerequisite]
2. `GOOGLE_ANALYTICS_BATCH_RUN_REPORTS` - Execute multiple reports at once [Required]

**Key parameters**:
- `property`: Property ID (required)
- `requests`: Array of individual report request objects (same structure as RUN_REPORT)

**Pitfalls**:
- Maximum 5 report requests per batch call
- All reports in a batch must target the same property
- Each individual report has the same dimension/metric limits as RUN_REPORT
- Batch errors may affect all reports; check individual report responses

### 4. Run Pivot Reports

**When to use**: User wants cross-tabulated data (rows vs columns) like pivot tables

**Tool sequence**:
1. `GOOGLE_ANALYTICS_LIST_PROPERTIES` - Get property ID [Prerequisite]
2. `GOOGLE_ANALYTICS_RUN_PIVOT_REPORT` - Execute pivot report [Required]

**Key parameters**:
- `property`: Property ID (required)
- `dateRanges`: Date range objects
- `dimensions`: All dimensions used in any pivot
- `metrics`: Metrics to aggregate
- `pivots`: Array of pivot definitions with `fieldNames`, `limit`, and `orderBys`

**Pitfalls**:
- Dimensions used in pivots must also be listed in top-level `dimensions`
- Pivot `fieldNames` reference dimension names from the top-level list
- Complex pivots with many dimensions can produce very large result sets
- Each pivot has its own independent `limit` and `orderBys`

### 5. Run Funnel Reports

**When to use**: User wants to analyze conversion funnels and drop-off rates

**Tool sequence**:
1. `GOOGLE_ANALYTICS_LIST_PROPERTIES` - Get property ID [Prerequisite]
2. `GOOGLE_ANALYTICS_RUN_FUNNEL_REPORT` - Execute funnel analysis [Required]

**Key parameters**:
- `property`: Property ID (required)
- `dateRanges`: Date range objects
- `funnel`: Funnel definition with `steps` array
- `funnelBreakdown`: Optional dimension to break down funnel by

**Pitfalls**:
- Funnel steps are ordered; each step defines a condition users must meet
- Steps use filter expressions similar to dimension/metric filters
- Open funnels allow entry at any step; closed funnels require sequential progression
- Funnel reports may take longer to process than standard reports

### 6. Manage Key Events

**When to use**: User wants to view or manage conversion events (key events) in GA4

**Tool sequence**:
1. `GOOGLE_ANALYTICS_LIST_PROPERTIES` - Get property ID [Prerequisite]
2. `GOOGLE_ANALYTICS_LIST_KEY_EVENTS` - List all key events for the property [Required]

**Key parameters**:
- `parent`: Property resource name (e.g., 'properties/123456')
- `pageSize`: Number of results per page
- `pageToken`: Pagination token

**Pitfalls**:
- Key events were previously called "conversions" in GA4
- Property must have key events configured to return results
- Key event names correspond to GA4 event names

## Common Patterns

### ID Resolution

**Account name -> Account ID**:
```
1. Call GOOGLE_ANALYTICS_LIST_ACCOUNTS
2. Find account by displayName
3. Extract name field (e.g., 'accounts/12345')
```

**Property name -> Property ID**:
```
1. Call GOOGLE_ANALYTICS_LIST_PROPERTIES with filter
2. Find property by displayName
3. Extract name field (e.g., 'properties/123456')
```

### Dimension/Metric Discovery

```
1. Call GOOGLE_ANALYTICS_GET_METADATA with property ID
2. Browse available dimensions and metrics
3. Call GOOGLE_ANALYTICS_CHECK_COMPATIBILITY to verify combinations
4. Use verified dimensions/metrics in RUN_REPORT
```

### Pagination

- Reports: Use `offset` and `limit` for row pagination
- Accounts/Properties: Use `pageToken` from response
- Continue until `pageToken` is absent or `rowCount` reached

### Common Dimensions and Metrics

**Dimensions**: `date`, `city`, `country`, `deviceCategory`, `sessionSource`, `sessionMedium`, `pagePath`, `pageTitle`, `eventName`

**Metrics**: `activeUsers`, `sessions`, `screenPageViews`, `eventCount`, `conversions`, `totalRevenue`, `bounceRate`, `averageSessionDuration`

## Known Pitfalls

**Property IDs**:
- Always use full resource name format: 'properties/123456'
- Numeric ID alone will cause errors
- Resolve property names to IDs via LIST_PROPERTIES

**Date Ranges**:
- Format: 'YYYY-MM-DD' or relative ('today', 'yesterday', '7daysAgo', '30daysAgo')
- Data processing delay means today's data may be incomplete
- Maximum date range varies by property configuration

**Compatibility**:
- Not all dimensions work with all metrics
- Always verify with CHECK_COMPATIBILITY before complex reports
- Custom dimensions/metrics have specific naming patterns

**Response Parsing**:
- Report data is nested in `rows` array with `dimensionValues` and `metricValues`
- Values are returned as strings; parse numbers explicitly
- Empty reports return no `rows` key (not an empty array)

## Quick Reference

| Task | Tool Slug | Key Params |
|------|-----------|------------|
| List accounts | GOOGLE_ANALYTICS_LIST_ACCOUNTS | pageSize, pageToken |
| List properties | GOOGLE_ANALYTICS_LIST_PROPERTIES | filter, pageSize |
| Get metadata | GOOGLE_ANALYTICS_GET_METADATA | property |
| Check compatibility | GOOGLE_ANALYTICS_CHECK_COMPATIBILITY | property, dimensions, metrics |
| Run report | GOOGLE_ANALYTICS_RUN_REPORT | property, dateRanges, dimensions, metrics |
| Batch reports | GOOGLE_ANALYTICS_BATCH_RUN_REPORTS | property, requests |
| Pivot report | GOOGLE_ANALYTICS_RUN_PIVOT_REPORT | property, dateRanges, pivots |
| Funnel report | GOOGLE_ANALYTICS_RUN_FUNNEL_REPORT | property, dateRanges, funnel |
| List key events | GOOGLE_ANALYTICS_LIST_KEY_EVENTS | parent, pageSize |

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
