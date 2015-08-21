from fabric.api import run, local, get


def fetch_logs():
    logs_dir = "~/logs/jwarren.co/http/*.log"
    get(remote_path=logs_dir)
