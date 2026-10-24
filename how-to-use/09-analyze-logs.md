# Analyze logs for slowness or an outage

Use this when you have a folder of application or system logs and need an evidence-based timeline. The analysis is read-only by default. Give the agent the exact folder path; it should not search unrelated folders to guess.

## General slowness

A timeframe is optional for a general performance review. Provide the log path and say:

> Read `skills/analyze-logs/SKILL.md` and follow it. Analyze logs under [exact folder path] for general slowness. I don't have a specific time window. Review the relevant available coverage, identify the services and files, establish the timezone represented in each log if possible, and report measured latency patterns, errors, and coverage gaps. Do not modify or upload the logs.

The report should state the earliest/latest log coverage and the source timezone evidence. If there is no latency field or baseline, ask it to describe what is observable without declaring an SLO violation.

## A suspected outage or time-bound issue

Provide the requested time interval and the timezone you mean:

> Analyze [exact folder path] for [service or symptom] from [start] to [end] in [named timezone or explicit UTC offset]. Report the first and last observed symptoms, first observed recovery if present, the duration basis, the timezone used by each source log, and the timezone used in your report. Keep the analysis read-only and state any coverage or clock uncertainty.

If you do not know the log timezone, say so rather than guessing:

> I do not know the timezone used in these logs. Inspect the files and available configuration for evidence. Preserve raw timestamps and mark the source timezone unknown if you cannot establish it; ask me before making a conversion that depends on it.

## Review the result

Look for separate observed events, calculations, and hypotheses. A first logged error may not be the true outage start; the end of a log file does not prove recovery. If the logs suggest a code defect, hand the evidence to `debug`. If you need a production probe or access to another data source, decide and authorize that separately.

## Create incident documents after agreeing on the cause

First review the evidence and candidate cause with the agent. Do not ask it to write a definitive RCA while the cause is still uncertain or disputed. Once you agree on the reason, provide any missing impact, response, recovery, or remediation details and the folder where the files should be saved.

Then use this prompt:

> We agree that the cause was [agreed cause]. Create three separate plain-text files in [output folder]: (1) a detailed technical RCA, (2) an evidence-backed RCA that cites the exact log filenames and line numbers for material log-based claims, with timestamps labeled in each source timezone and short redacted evidence, and (3) a tight, precise email for [audience]. Include the agreed impact, incident window, response, recovery, current status, and next actions only where known. Separate information I supplied from facts established by the logs. Do not invent evidence or line numbers; mark uncertainty and explain what a cited log line supports without overstating causality. Do not modify the source logs or overwrite existing files. Report the three saved paths.

If the cause remains unverified but you still need drafts, explicitly request provisional documents and require the uncertain cause to be labeled provisional.
