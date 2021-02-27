from Notes.celery import app
from public_tools.data_backup import DataBackup
@app.task
def backup_task(filename,data):
    backuper = DataBackup()
    backuper.backup(filename, data)