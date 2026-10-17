# Measure AI use without losing quality

The goal is a repeatable team process with clear business outcomes and credible checks. A fast draft that takes substantial correction may not save time.

For each task record the human initiating it, task/requirement/PR, agent and model if visible, prompt, instruction/skill commit, prompting time, review time, correction time, verification time, output outcome, and quality evidence. Include every human contributor's task effort so that work shifted from Developer to Tester or TM is counted.

Use a measured manual baseline only when a comparable task and quality bar exist. Record its source and uncertainty. Reusing the same task immediately after seeing the answer introduces learning effects; alternate task order or use comparable tasks when practical. Estimated baselines can be recorded as estimates but cannot establish measured savings.

| Measure | Calculation / interpretation |
| --- | --- |
| AI-assisted human effort | Prompting + review + correction + verification minutes, summed across participating people |
| Measured effort difference | Comparable measured manual baseline − AI-assisted human effort |
| Percentage difference | Difference / measured baseline × 100; calculate only for a positive, comparable baseline |
| Quality | Acceptance criteria met, test evidence, review findings, rejected/reworked outputs, and escaped defects |
| Elapsed time | Record separately if relevant; agent waiting time is not automatically human effort |

Leave calculated savings blank when required inputs are missing. A recorded zero is different from an unknown field. Negative savings are valid evidence of more human effort. Never fabricate numbers to demonstrate a benefit.

During the retrospective, identify one recurring failure pattern and propose a small instruction/skill change. Evaluate it on a fresh comparable task; show whether the error and human rework changed. Have the Technical Manager review the change before adopting it for the next cohort.

Use the AI Runs table in [Excel tracking](excel-tracking.md). Keep the task's actual test and defect links beside the effort data.
