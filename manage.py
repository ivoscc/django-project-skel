#!/usr/bin/env python
import os, sys

if __name__ == '__main__':

    #For having the apps outside the project dir
    from  {{ project_name }}.settings import ROOT_DIR
    sys.path.insert(0, os.path.join(ROOT_DIR, 'apps'))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.settings')

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
