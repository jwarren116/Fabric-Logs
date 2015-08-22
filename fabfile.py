from fabric.api import run, local, get, cd


def fetch_logs():
    logs_dir = "~/logs/jwarren.co/http/*.log"
    get(remote_path=logs_dir)


def commit():
    local("git add -p && git commit")


def push():
    local("git push")


def prepare_deploy():
    commit()
    push()


def deploy():
    app_dir = "~/jwarren.co/"
    cd(app_dir)
    run("git pull origin master")
    run("touch tmp/restart.txt")
