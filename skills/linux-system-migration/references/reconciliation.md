# Reconciliation and Acceptance

Use this matrix to drive discovery. Mark each category in scope, absent on the
source, or excluded by agreement; do not manufacture missing evidence.

## Coverage Matrix

| Category | Discover and account for | Acceptance evidence |
| --- | --- | --- |
| Storage and files | All relevant mounted filesystems, root-owned data, home/root/opt/srv/var/lib/custom paths, links and bind mounts, large files and explicit exclusions | Stable content comparison, critical hashes, metadata checks, mounted destination, archive recovery test |
| Users and access | UID/GID, supplementary groups, home/shell, sudoers, SSH, ACLs, file capabilities | Intended access works as each real user; unauthorized access remains denied; sudoers syntax validates |
| Packages and runtimes | Native packages/repos/manual marks, Snap/Flatpak, manual binaries, language environments, interpreters, global tool prefixes | Expected command resolves in the real runtime; compatible version and application operation |
| System configuration | Selected /etc, locale/timezone, environment, networking, firewall, DNS, proxy, container storage roots | Target-valid configuration, preserved intended behavior, client connectivity |
| Services | System and each user's units, drop-ins, enablement, lingering, dependency paths/env, restart/guard launchers | Correct owner/environment, application/protocol operation, one intended instance, reboot startup |
| Scheduled work | Every relevant user's and root's crontab, /etc/cron.*, anacron, system/user timers, at jobs, application schedulers | Exact command, user, timezone, environment, writable output, completed result, no duplicate source writer |
| Desktop and user settings | Dotfiles, XDG config/data/state, dconf, terminal profile, editor/browser state, input methods and dictionaries, fonts, extensions, keyrings | Real logged-in session; terminal appearance, actual input and candidate selection, expected application settings |
| Credentials | SSH/client keys, env secrets, token stores, browser cookies, encrypted keyrings, application auth | Restricted permissions and working intended login/API; reauthenticate expired or device-bound tokens |
| Data services and containers | Databases/WAL, volumes, bind mounts, Compose files, container secrets, storage drivers | Consistent restore and query, volume permissions, container health and application behavior |
| Clients and endpoints | Host aliases, DHCP reservations if used, DNS, desktop launchers, remote MCP/API consumers | Request from actual client reaches target; old endpoint references accounted for |
| Backups and cold data | Source manifests, exact archive destination, restore dependencies, encryption access, retention | Integrity and isolated restore evidence; migrated backup jobs produce valid new backups |
| Boot and hardware | Disk UUIDs, EFI/GRUB/initramfs, drivers, kernel/firmware, displays, networking, power transitions | Successful target reboot and workflow checks; installed next-boot kernel and fallback actually exist |

The matrix is a coverage aid, not a requirement to migrate all listed state.
Examples: caches may be rebuilt, an unused crawler retired, cold data archived,
and a source-specific GPU stack excluded with a recorded reason.

## Frequent False Positives

- A directory exists but nested data is missing: compare manifests/content and
  ownership at the required scope, including root-readable files.
- Disk usage differs: account for archives, sparse files, hard links, filesystem
  allocation, rebuildable payloads, and excluded data before diagnosing loss.
- A process is running but its feature fails: test a visible user operation or
  real protocol exchange. Input-method process/DBus checks do not prove its
  candidate window works. Mark visual checks pending without actual evidence.
- A proxy port responds but transparent routing fails: exercise the intended
  traffic path from its real consumer, removing explicit proxy variables when
  testing transparent routing.
- A service works after manual launch: verify reboot ordering and session
  dependencies. An SSH shell environment can hide a broken cron/systemd PATH.
- A scheduled job exists: inspect freshness and its actual result. A safe manual
  wrapper test establishes execution behavior, not that the scheduler fired.
- A retired job lacks a fresh log: verify its schedules and processes are absent;
  directory deletion is a separate data-retention decision.
- A checksum matches: it establishes byte identity for that artifact, not
  application consistency, metadata fidelity, authenticity, or recoverability.
- A raw disk clone boots: still verify host identities, new device dependencies,
  workflow parity, and the cutover writer boundary.
- A single task enters D state: check persistence, task identity, I/O pressure,
  and kernel/device errors. Brief filesystem journal commits can be normal.
  Define thresholds before the soak; preserve failures and label any revised
  criteria and rerun, rather than silently changing a failed gate into success.
- Firmware crash records change across reboot: preserve both raw records and
  compare boot history. Retention/rotation, severity, and undocumented payloads
  limit what can be inferred about timing or the failing component.

## Stability and Update Boundary

Passing a finite soak supports only the tested configuration and workload.
For a recurrent freeze, preserve the original symptom, journal cutoff, previous
boot, updates, thermal/I/O/resource samples, and firmware or pstore evidence.
Keep root-cause hypotheses distinct from confirmed failures.

Check unattended upgrade and kernel cleanup behavior. If the accepted kernel is
needed as a fallback, preserve its required packages and verify the boot entry
exists after updates. Manual package marks prevent autoremove; they are not an
upgrade hold. Do not freeze security updates or apply host-specific kernel
parameters as a universal migration default.

## Completion Report Shape

Use four independent verdicts with dated evidence:

1. Inventory reconciliation: every required item passed or has an accepted
   disposition; name inaccessible scopes and remaining deltas.
2. Functional acceptance: actual workflows, authentication, reboot startup, and
   scheduled execution; distinguish automated checks from user-confirmed visuals.
3. Stability: tested configuration, elapsed observation, workload/transitions,
   failures and remaining limits. State not required when agreed out of scope.
4. Source retirement: rollback window, valid recovery material, writer ownership,
   and exact authorized action. Passing the first three does not authorize wiping.

Include exact archive locations, safe log/report references, unresolved items,
and the next required observation if any. Do not include credentials or private
host details in a redistributed skill.
