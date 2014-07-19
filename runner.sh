#!/bin/sh

# start up uwsgi
/usr/sbin/uwsgi --ini /etc/uwsgi.ini &

# start up nginx 
/usr/sbin/nginx &

wait
