from __future__ import absolute_import

from celery_task.celery import app
from server import chatted_connections, connections
from socket import close

@app.task
def check_connections():
    print('celery started')
    for connection in connections:
        if connection not in chatted_connections:
            connection.close()
            connections.remove(connection)
            chatted_connections.remove(connection)

    print(f'not chatted connection removed successfully')

