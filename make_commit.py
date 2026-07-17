import subprocess
import os
from datetime import datetime

CSV_FILE = "commits.csv"

messages = [
    "update project",
    "add feature",
    "fix bug",
    "refactor code",
    "improve project",
    "update files",
    "small changes"
]

def run(cmd, env=None):
    subprocess.run(cmd, shell=True, env=env, check=True)

if not os.path.exists(".git"):
    run("git init")

with open(CSV_FILE, "r") as file:
    lines = file.readlines()

commit_number = 1

for line in lines:
    line = line.strip()

    if not line:
        continue

    date_str, amount = line.split(",")

    amount = int(amount)

    date = datetime.strptime(date_str, "%d.%m.%Y")
    git_date = date.strftime("%Y-%m-%d 12:%M:%S")

    for i in range(amount):
        with open("history.txt", "a") as f:
            f.write(f"Commit {commit_number}\n")

        run("git add .")

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = git_date
        env["GIT_COMMITTER_DATE"] = git_date

        message = messages[i % len(messages)]

        run(
            f'git commit -m "{message} #{commit_number}"',
            env
        )

        print(f"Created commit {commit_number} on {date_str}")

        commit_number += 1

print("Done!")
