# PR drafts (prepared, not submitted)

## `enh/conf-root-owned` — install motioneye.conf as root:motion 0640

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
