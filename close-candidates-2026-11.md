# Close candidates from the open labelling

The 77 open issues an agent marked as maybe resolved, re-read with all comments on 2026-11-07. Nothing closed from this; each close needs the user's OK. Evidence is the issue comments, the code was not run.

## A. The reporter says it is solved (19)

#2875, #1269, #428, #308, #306, #554, #2556, #2858, #1859, #1257, #1025, #669, #358, #1400, #794, #743, #690, #1352, #319

#2875 and #1269: the reporter says it can be closed. #319: the reporter says it was implemented, version not checked.

## B. Answered or worked around, the reporter did not confirm, or the cause stayed unknown (38)

#952, #950, #1010, #1052, #902, #1393, #1256, #872, #1392, #1089, #1364, #1268, #1232, #951, #2867, #2834, #1487, #1503, #747, #514, #1236, #664, #960, #2630, #1855, #1444, #1480, #638, #539, #1532, #256, #495, #501, #2522, #1281, #442, #728, #1046

## C1. Possibly fixed, needs a check (5)

- #289: commit `e4c69fae` (2016-08-20) is in dev; nobody confirmed it fixed the report.
- #1092: `0.40rc1` adds Motion 4.2 support, merge `438fb679` in dev; the reporter did not reply.
- #2623: zagrim says 0.43 has a workaround; no commit found by searching messages for flicker, libmicrohttpd and Content-Length.
- #1443, #1419: the Chrome change of #1401; no fixing commit found by searching messages for chrome and 1401.

## C2. Keep open (15)

#2504, #1206, #1304, #1414, #1124, #1003, #536, #459, #357, #857, #1379, #1857, #1483, #307, #1440

#2504: MichaIng wants the default changed from H.264/OMX; `motioneye/config.py:2620` still prefers `mp4:h264_omx` when supported.
