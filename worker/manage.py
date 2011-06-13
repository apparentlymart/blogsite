#!/usr/bin/python
from django.core.management import execute_manager
try:
    import blogsite.settings as settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find blogsite.settings.\n")
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
