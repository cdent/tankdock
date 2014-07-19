FROM    fedora
MAINTAINER Chris Dent <cdent@peermore.com>

# Get the base packages
RUN yum update -y
RUN yum install -y python-devel 
RUN yum install -y memcached
RUN yum install -y nginx
RUN yum install -y uwsgi-plugin-python
RUN yum install -y python-memcached
RUN yum install -y python-pip

# Get the required python packages
# XXX: This seems a bit messy
RUN pip install -U oauth2client httplib2 tiddlyweb tiddlywebplugins.devstore2 tiddlywebplugins.caching tiddlywebplugins.utils tiddlywebplugins.templates tiddlywebplugins.markdown tiddlywebplugins.whoosher tiddlywebplugins.logout tiddlywebplugins.relativetime tiddlywebplugins.status tiddlywebplugins.atom tiddlywebplugins.policyfilter tiddlywebplugins.links tiddlywebplugins.csrf tiddlywebplugins.jsondispatcher tiddlywebplugins.twikified tiddlywebplugins.extraclude tiddlywebplugins.privateer tiddlywebplugins.cors markdown-checklist httpexceptor

# tiddlywebplugins.oauth not installed because not on pypi!

RUN adduser tiddlyweb
RUN mkdir /home/tiddlyweb/tank
RUN chown tiddlyweb:tiddlyweb /home/tiddlyweb/tank
RUN chmod 755 /home/tiddlyweb /home/tiddlyweb/tank

ADD nginx.conf /etc/nginx/
ADD uwsgi.ini  /etc/
ADD tank.ini   /etc/uwsgi.d/
ADD wsgiapp.py /home/tiddlyweb/tank/

ADD runner.sh /bin/

RUN chmod 755 /bin/runner.sh
RUN chown uwsgi:uwsgi /etc/uwsgi.d/tank.ini

EXPOSE 80
