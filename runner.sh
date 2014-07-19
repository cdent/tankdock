#!/bin/sh -xe

# start up memcached
memcached -u nobody -m64 &

# start up uwsgi
/usr/sbin/uwsgi -M --ini /etc/uwsgi.ini &

# start up nginx 
/usr/sbin/nginx &

# starup beanstalkd
beanstalkd -u nobody &

wait
