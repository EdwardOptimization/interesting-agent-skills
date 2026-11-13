---
name: linux-system-migration
description: Plan, execute, or audit Linux-to-Linux host migrations, including Ubuntu desktop and server systems. Use for moving applications, data, users, settings, services, and schedules to another installation, checking migration completeness, or deciding whether the source can be retired. Not for application code ports or distribution upgrades alone.
---

# Linux System Migration

Make the target reproduce the source's intended workflows, with every omission
accounted for and a usable recovery path. Assume Linux command knowledge; focus
on inventory, reconciliation, cutover, and evidence.

## Establish the Contract

Resolve source and target identities live: hostname, machine identity, current
SSH endpoint, OS/architecture, disks, mounts, and users. Do not rely on an old IP
alias when identifying a disk, host, or destructive target.

Use existing task authorization. Determine the requested phase: assess, archive,
transfer, cut over, verify, or retire. Migration authority does not itself authorize
wiping the source. Continue independent work while any necessary missing decision
is being resolved.

Agree on retained workflows, intended differences, outage tolerance, rollback,
and the observation window. Separate migration completeness from target hardware
stability. Passing either does not establish the other.

## Inventory Before Copying

Read [references/reconciliation.md](references/reconciliation.md) for the coverage
matrix and acceptance traps. Inventory the source with sufficient privileges,
including root-owned paths and every relevant user's runtime and desktop state.
Record unreadable or unavailable scopes explicitly.

Create a migration ledger from discovered items, not a generic application list:

| Item | Source evidence/time | Disposition | Target/archive | Verification | Status |
| --- | --- | --- | --- | --- | --- |
| A discovered path, package, workflow, or job | Listing/config/runtime evidence | migrate, archive, rebuild, retire | Exact destination or reason | Expected observable result and evidence | pending, pass, fail, unverified |

Every discovered in-scope item needs a disposition. Flag uncategorized and new
items on subsequent scans. Absence from the target is acceptable only with an
explicit disposition; retired tasks need absence checks. Do not silently revive
a task the user stopped.

## Confirm the Migration Checklist

Before executing the migration, present the discovered ledger as a user-facing
checklist. Include applications/runtimes, files/data, users/permissions, services,
schedules, desktop settings, and credentials by purpose only. Show the proposed
action, destination, and acceptance test for each item. Highlight exclusions,
archives, retired jobs, version differences, unreadable scopes, target data that
would be overwritten, and expected downtime and rollback limits.

Include a software version policy for user confirmation: preserve source versions,
or use the latest stable versions compatible with the target OS/architecture and
required workflows from trusted supported channels. Offer a default policy plus
per-application or application-group exceptions, rather than a prompt per package.
Record source version, available target candidate/channel, proposed version, and
compatibility or data-format changes. Missing evidence stays unknown; "newer" is
not acceptance evidence. If an exact version is unavailable or incompatible, flag
the exception and obtain agreement before substituting. An approved alternative
rule can already cover that exception.

Respect project lockfiles and runtime compatibility; a general application upgrade
choice does not authorize rewriting pinned dependencies, upgrading database
formats, or moving kernels/drivers/firmware to new versions. Include those changes
and their rollback implications explicitly if needed. Snapshot candidate versions
in the approved ledger; report meaningful drift at execution instead of silently
following a moving latest release.

Inventory paid licenses and subscriptions separately from application login.
Include entitlement/version coverage, device-seat limits, source deactivation,
target activation, and required account access in the checklist. Verify current
vendor transfer rules. Prepare the target, then follow any required old-device
deactivation before new-device activation; test the licensed feature and record
seat release before source retirement. Keep keys private. If transfer is blocked,
record it as pending and continue unrelated work. Do not cancel subscriptions or
revoke unrelated devices as part of transferring one machine.

Ask the user to confirm or amend this concrete scope once. Record the approved
checklist revision and the confirming instruction as the acceptance baseline.
An existing confirmation covering that checklist and execution phase counts;
do not request it again. A broad initial request to migrate does not approve
newly discovered exclusions or destructive effects. While confirmation is pending,
continue authorized discovery and planning, not dependent transfer or cutover.

Execute routine work within the approved scope autonomously. Add newly discovered
items to the ledger and flag unresolved scope. Seek confirmation only for material
changes not already authorized, such as additional discarded data, overwriting
target state, retiring more jobs, or expanding downtime. Continue unaffected work.
Never treat checklist approval as permission to format or wipe the source; that
requires separate, exact retirement authorization after acceptance.

## Choose and Perform the Transfer

Choose selective rebuild/restore or offline disk/filesystem cloning according
to the user's intended result, available downtime, storage layout, and recovery
access. Neither method guarantees functional parity by itself.

- Preview transfers and retain exit codes and exclusions. A partial copy is not
  success; classify skipped paths before accepting an exception.
- Preserve required numeric ownership, permissions, ACLs, xattrs, hard links,
  and symlinks. Resolve target UID/GID collisions before applying ownership.
- For mutable databases, browser profiles, and container volumes, use native
  backups or a coordinated stop/snapshot. Copying a live tree is not proof of
  application consistency.
- Keep root/system references apart from automatically applied configuration.
  Merge selectively: UUIDs, network interfaces, drivers, bootloader, machine ID,
  and SSH server identity require target-specific decisions. For cloning, review
  identity collisions and boot adaptation before both hosts return to the network.
- Reinstall software from trusted sources where appropriate; inventory apt/rpm,
  Snap, Flatpak, language tools, and manual installs. Distinguish application
  state from rebuildable payloads and caches. Install according to the approved
  version policy and exceptions; verify actual installed versions against the
  ledger and exercise migrated configuration/data with those versions.
- Transfer credentials through protected channels without logging contents.
  File presence does not prove valid OAuth, keyring access, or application login.

## Cut Over with One Writer

Prepare paths, mounts, identities, runtime dependencies, and environment files
before enabling workloads. Review copied unit overrides, lingering, cron, desktop
autostart, and watchdogs together to avoid duplicate launchers.

For workloads with external effects, keep target writers and schedules disabled
during staging. Quiesce source writers, capture final consistent changes, verify
the final delta, then activate target writers and redirect clients. Record which
host owns each job. Do not keep a source job running while manually triggering
its target copy.

Rollback after target writes requires data reconciliation or reverse replication;
starting an old snapshot on the source can lose new writes or repeat side effects.
Record this boundary before cutover.

## Verify the Result

Re-scan and reconcile against the source ledger and agreed exclusions. Check
content and required metadata; total disk usage and path presence are supporting
evidence only. Checksum stable critical data and use scoped comparisons for
large archives. Label sampled verification as sampled.

Exercise workflows as their actual owner in the actual execution environment:
interactive shell, desktop, user/system service, container, or cron. Enabled units,
open ports, and health endpoints are preliminary checks. Prove a meaningful
application operation, protocol request, or job result.

Test a controlled reboot when authorized and operationally feasible. Check mounts,
login/session readiness, dependencies, autostart, duplicate processes, and service
behavior after reboot. If not exercised, keep reboot acceptance unverified.

Observe required scheduled jobs through execution, or safely test their real
wrapper with equivalent environment and explicitly retain any schedule wait.
Do not trigger payments, notifications, or production writes solely for a test
without applicable authorization and duplicate prevention.

For hardware changes or prior freezes, test relevant idle/lock/suspend/network
transitions and agree a representative soak window. Record boot ID, runtime and
next-boot kernel, firmware, and power settings. A reboot or relevant configuration
change invalidates the affected observation baseline. Preserve unexplained crash
evidence; a short green check does not close a hard-freeze incident.

## Close Out and Retire

Report migration completeness, workflow/reboot acceptance, stability observation,
and retirement readiness separately. List failures, unverified checks, accepted
differences, archived data locations, and the next checkpoint with evidence times.
Do not call the whole migration complete while required items remain unresolved.

Retire only when required gates pass, recovery material has been verified, and
the user authorizes the exact decommissioning scope. Keep source data intact
through the agreed rollback window. Before wiping or selling, resolve remaining
credentials and identify the actual device again.
