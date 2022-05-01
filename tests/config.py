from envparse import env
import os

# read config variables from .env file for local usage
env.read_envfile()

# config variables for gitlab run use os environ variables
# config variables local run use .env file
BROWSER = env("BROWSER", "firefox")
BROWSER_WIDTH = env("BROWSER_WIDTH", default="1600")
BROWSER_HEIGHT = env("BROWSER_HEIGHT", default="889")
IMPLICIT_WAIT = env("IMPLICIT_WAIT", default="15")
HOME_URL = env("HOME_URL", default=os.environ.get("HOME_URL"))