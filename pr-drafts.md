# PR drafts

## `enh/conf-root-owned` — install motioneye.conf as root:motion 0640 (submitted as #3475, 2026-10-26)

- Branch: `JamBalaya56562:enh/conf-root-owned` (`faf38179`), base `dev` (`5acdd519`)
- Follow-up of #3474, suggested by MichaIng: https://github.com/motioneye-project/motioneye/pull/3474#issuecomment-6400316471 ("Side note")
- When: after some time has passed since #3474 was merged; one PR at a time

**Title:** `enh: install motioneye.conf as root:motion 0640`

**Body:**

```
Follow-up of #3474, as suggested there: motioneye.conf holds settings that the motionEye server is not meant to change itself, e.g. to lift its own restrictions via `motion_control_authentication` or `webcontrol_*`.

- `motioneye_init` (`linux_init`) now installs it as `root:motion` with mode 0640, so motionEye can read but not write it.
- The mode check in `meyectl` accepts access by root and motionEye's own user and group only, instead of always enforcing 0600:
  - access for others (or another group) is removed when motionEye owns the file,
  - otherwise (e.g. `root:motion 0644`) it asks the admin to apply the mode as root, since only the owner can change it,
  - a file owned by another user is reported.
- The sample notes the intended owner and mode.

Tested:
- Test suite: 348 passed, also when run as a non-root user.
- In a container with the `motion` user: `root:motion 0640` is read without warning and cannot be written by motion (`Permission denied`); `root:motion 0644` logs "please apply 0640 as root"; `motion:motion 0644` is changed to 0640.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

Before submitting: rebase onto the latest `dev`, re-run the tests, and re-check that no other open PR of ours exists.

## `enh/no-pid-file` — track motion by its process instead of a pid file

- Branch: `JamBalaya56562:enh/no-pid-file` (`26010af1`), base `dev` (`5acdd519`)
- Related to #2540 (not closing it: the Docker entrypoint still needs root for `su motion`, see #3181 / #2407)
- When: after #3475 is merged; one PR at a time

**Title:** `enh: track motion by its process instead of a pid file`

**Body:**

```
Related to #2540: motionEye no longer needs a writable pid directory unless it runs in the background (`-b`).

- motionEye starts motion as its own child, so `motionctl` now keeps the `Popen` handle instead of writing `motion.pid` and reading it back. `running()` polls the process, `stop()` terminates it (TERM, then KILL, as before), and returns as soon as motion exited instead of always waiting 5 seconds.
- This also removes a hazard of the pid file: a stale `motion.pid` holding the PID of an unrelated process made motionEye treat that process as motion, skip starting motion, and terminate it on stop.
- `run_path` is only needed for `motioneye.pid` in background mode, so it is only checked there; the sample and settings comment say so.

This does not make `docker run --user` work yet: the entrypoint still creates `/run/motioneye` and switches to the motion user with `su`, which needs root (#3181).

Tested:
- Test suite: 353 passed, including new tests for the process handling and a stale pid file.
- With motion 4.5.1 as the motion user and a non-existent `run_path`: dev exits with "pid directory ... is not writable"; with this change motionEye starts, motion runs without any pid file, is restarted by the checker after `kill -9`, and is stopped with motionEye. With `-b`, the missing `run_path` is still reported.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

Before submitting: rebase onto the latest `dev`, re-run the tests, and re-check that no other open PR of ours exists.
