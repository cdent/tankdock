FROM    fedora
MAINTAINER Chris Dent <cdent@peermore.com>

# Get the base packages
RUN yum update -y
RUN yum install -y python-devel 
RUN yum install -y memcached
RUN yum install -y beanstalkd
RUN yum install -y sqlite
RUN yum install -y nginx
RUN yum install -y uwsgi-plugin-python
RUN yum install -y python-memcached
RUN yum install -y python-pip
RUN yum install -y PyYAML

# Get the required python packages
# XXX: This seems a bit messy
RUN pip install -U oauth2client httplib2 tiddlyweb tiddlywebplugins.devstore2 tiddlywebplugins.caching tiddlywebplugins.utils tiddlywebplugins.templates tiddlywebplugins.markdown tiddlywebplugins.whoosher tiddlywebplugins.logout tiddlywebplugins.relativetime tiddlywebplugins.status tiddlywebplugins.atom tiddlywebplugins.policyfilter tiddlywebplugins.links tiddlywebplugins.csrf tiddlywebplugins.jsondispatcher tiddlywebplugins.twikified tiddlywebplugins.extraclude tiddlywebplugins.privateer tiddlywebplugins.cors markdown-checklist httpexceptor boto

# tiddlywebplugins.oauth not installed because not on pypi!

RUN adduser tiddlyweb
RUN mkdir -p /home/tiddlyweb/tank/src

ADD nginx.conf /etc/nginx/
ADD uwsgi.ini  /etc/
ADD tank.ini   /etc/uwsgi.d/
ADD wsgiapp.py /home/tiddlyweb/tank/

ADD runner.sh /bin/

RUN chmod 755 /bin/runner.sh
RUN chown tiddlyweb:tiddlyweb /etc/uwsgi.d/tank.ini

EXPOSE 80

ADD tank/mangler.py /home/tiddlyweb/tank/
ADD tank/src /home/tiddlyweb/tank/src
ADD tiddlywebplugins.oauth /home/tiddlyweb/tiddlywebplugins.oauth
ADD tank/tiddlywebplugins /home/tiddlyweb/tank/tiddlywebplugins
RUN cd /home/tiddlyweb/tank/tiddlywebplugins && ln -s ../../tiddlywebplugins.oauth/tiddlywebplugins/oauth .
RUN cd /home/tiddlyweb/tank && ln -s tiddlywebplugins/templates .
ADD tiddlywebconfig.py /home/tiddlyweb/tank/

RUN chown -R tiddlyweb:tiddlyweb /home/tiddlyweb
RUN chmod 755 /home/tiddlyweb /home/tiddlyweb/tank
