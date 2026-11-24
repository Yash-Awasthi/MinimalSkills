<!-- source: catalog/code-quality/rhdh-backstage-api-changes -->
<!-- source-name: rhdh-backstage-api-changes -->

# RHDH Backstage API Changes

A single home for the NFS API deltas. Two skills need this material and neither
owns it, so it lives here and both invoke it by name.

## Who invokes this

- `/rhdh-backstage-upgrade` owns **version numbers**. It arrives here when a
  bump moves a checkout across one of these deltas and NFS code stops
  compiling.
- `/rhdh-plugin-nfs-migration` owns **extension shape**. It arrives here when a
  plugin was already migrated against an older alpha, or when a Blueprint param
  from an older guide produces a TypeScript error.

That is also the boundary between those two skills. A version number is the
upgrade skill's business; which Blueprint an extension becomes and where it
attaches is the migration skill's. This skill sits under both and belongs to
neither: it says only what changed in the API, not which change you should
make.

## Interface

Read `references/api-changes.md`. It is organized one section per change, each
with the old form, the new form, and the package the symbol now comes from.

Consume it as a checklist against the code in front of you. Two cautions:

- It describes the delta from the early alpha to current GA. It is not a
  release-by-release changelog, and it does not replace reading the changelogs
  for the specific releases an upgrade spans.
- The upstream surface keeps moving. When this prose and the type definitions
  in `node_modules/@backstage/frontend-plugin-api` disagree, the type
  definitions win — report the disagreement rather than following the prose.

## Completion

Report which of these changes apply to the code in hand, the exact symbol and
package each one moves to, any occurrence you could not resolve, and hand the
result back to the skill that invoked this one.
