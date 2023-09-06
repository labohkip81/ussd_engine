import os
# Version is filled during publish or deploy
VERSION = '1.0.0'
VERSION = os.getenv('MY_PACKAGE_VERSION', '1.0.0')