from fabric.api import run, local, get


def fetch_logs():
    logs_dir = "~/logs/jwarren.co/http/*.log"
    get(remote_path=logs_dir)


def commit():
    local("git add -p && git commit")


def push():
    local("git push")
