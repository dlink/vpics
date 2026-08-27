# vpics Gunicorn configuration

# Server socket

bind = 'unix:/apps/vpics/web/vpics.sock'
backlog = 2048

# Worker processes

workers = 3
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

# Server mechanics

daemon = False
pidfile = '/apps/vpics/web/vpics.pid'
umask = 0
user = 'dlink'
group = 'dev'
tmp_upload_dir = None

# Logging

errorlog = '/var/log/gunicorn/vpics/error.log'
loglevel = 'info'
accesslog = '/var/log/gunicorn/vpics/access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Process naming

proc_name = 'gunicorn-vpics'

# Server hooks

def post_fork(server, worker):
    server.log.info('Worker spawned (pid: %s)', worker.pid)

def when_ready(server):
    server.log.info('Server is ready. Spawning workers')

def worker_int(worker):
    worker.log.info('Worker received INT or QUIT signal')

def worker_abort(worker):
    worker.log.info('Worker received SIGABRT signal')
