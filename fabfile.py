"""
Scripts to automate tools.
"""
from fabric.api import local


def bootstrap():
    """Initialize a new project."""

    # Setup virtualenv
    local("virtualenv venv --distribute")

    # Source virtualenv
    local("source venv/bin/activate && pip install -r requirements.txt")

    # Create the Procfile
    local("echo 'web: python app.py' > Procfile")

    # initialize a git repository
    local("git init")

    # Commit!
    local("git add .")
    local("git commit -m 'first commit'")


def init_heroku():
    """Create a new Heroku instance."""

    # Create a new Heroku app
    local("heroku create")

    # Push the app to Heroku's servers
    local("git push heroku master")

    # Deploy the app
    local("heroku ps:scale web=1")
    local("heroku ps")

    # Make sure everything is okay
    local("heroku logs")

    # Open the app!
    local("heroku open")


def push_heroku(branch="master"):
    local("git push heroku %s" % branch)


def run():
    """Run the flask application."""
    local("python app.py")
