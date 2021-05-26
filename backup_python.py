# !python3
# backup_python.py - Бэкап папки python в папку python_backup

import shutil, os

os.chdir('/home/dio')
shutil.copytree('./Документы/python', '/home/dio/MEGA/python_backup')
