#!/usr/bin/env python
import os
import dotenv
import sys

if __name__ == "__main__":
    dotenv.read_dotenv()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
