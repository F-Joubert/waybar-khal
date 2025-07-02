#!/usr/bin/env python
import html
import json
import subprocess

from datetime import datetime

data = {}

try:
    calendar = subprocess.check_output(
        "khal calendar now 14 days --format \"{start-end-time-style} {title}\"",
        shell=True
    ).decode("utf-8")

except Exception:
    calendar = "Khal calendar unavailable"

#? Maintain 4 whitespace to align day notations with day columns
data["tooltip"] = f'<span font_family="monospace">    {html.escape(calendar.strip())}</span>'

output = subprocess.check_output(
    "khal list now 30days --format \"{start-end-time-style} {title}\"",
    shell=True
).decode("utf-8")

lines = output.split("\n")

new_lines = []

for line in lines:
    if len(line) and line[0].isalpha():
        line = f"\n<b>{line}</b>"
    new_lines.append(line)

events = "".join(new_lines).strip()

if "Today" in events:
    data["text"] = f"󰥔 {datetime.now().strftime('%H:%M')}\n {datetime.now().strftime('%d %b')}" + events.split("\n")[1]
else:
    data["text"] = f"󰥔 {datetime.now().strftime('%H:%M')}\n {datetime.now().strftime('%d %b')}"

print(json.dumps(data))
