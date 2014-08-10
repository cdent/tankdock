# What

TankDock is [Tank](https://tank.peermore.com/) in
[Docker](https://docker.com/) so that people can run their own Tank
service. If you don't want to run your own, feel free to use the
[existing public server](https://tank.peermore.com/).

When fully working the service will run under an nginx+uwsgi combination,
with a small memcached, and storage and logging to local disk.

# Caveats

Please note that at this time there are a few issues which make this
not ready for prime time (see Todo below as well):

* Your content is not stored in persistent storage. When you shut
  down your container, your content is gone.
* Font-awesome icons are not working, making it rather hard to
  navigate.
* SSL should be used whenever oauth2 is being used.

# Status

Still under development but potentially ready for some testing by the
strong of heart and mind.

# Structure

This repo is divided into several parts:

* The top level directory contains a Dockerfile for building (on
  Fedora) the basic requirements for an _unconfigured_ Tank
  installation.

  The Dockerfile installs the necessary RPMs and Python packages
  and creates the basic directory structure for a tank installation.
  It also `ADD`s the necessary configuration files and service
  start scripts (`runner.sh`).

  Eventually this container will be registered in the Docker hub.

* Two submodules: `tank` and `tiddlywebplugins.oauth` for Python
  code that is not yet available on PyPI.

* A `runner` subdirectory that contains another Dockerfile which
  uses the unconfigured container s the base for creating a
  configured installation.

  This directory contains a `tiddlywebconfig.py` that must be
  customized for your specific use (see below).

# Making Your Own

First, clone the repo, cd into it and:

```
git submodule init
git submodule update
```

then:

Currently, building a container with a custom Tank in it is a two
step process. If you are not familiar with Docker, [the
docs](http://docs.docker.com/) are good.

## 1: Build a base container

The top-level Dockerfile describes a container with all the
necessary software, filesystem structure, and generic configuration
to make a running system. Eventually this container will be
available for download so this step will not be required. For now,
to build your own, from within the checked out repository run:

```
sudo docker build -t cdent/tankdock .
```

This will churn away for a while gathering various pieces.

When it is done you will have a container tagged "cdent/tankdock"
available locally and you're ready for step 2.

## 2: Build a custom Tank

Change to the directory `runner`. In there is a `tiddlywebconfig.py`
file which must be edited to set custom settings. The comments
describe what needs to be set. After "# End of Customizations"
nothing needs to be changed. What is being done here is:

* Setting the hostname for the service (this is the externally
  addressable hostname).
* Setting a secret key for cookies.
* Setting the id and secret key for _at least_ one oauth2 identity
  provider. GitHub is [relatively easy to set
  up](https://github.com/settings/applications).
* Setting [AWS](http://aws.amazon.com/) S3 bucket settings.

Once the settings have been made another container needs to be built:

```
sudo docker build -t cdent/tank .
```

If you used a different name building the base container, change the
"FROM" line in the Dockerfile.

Now you have a Tank you can run.

# Run

To run the customer container you need to decide what port you would
like to map to the web server inside the container. I use `80`. In
order for 80 to work no other web server can be running.

```
sudo docker run -t -i -p 80:80 cdent/tank
```

If you see something like:

```
spawned uWSGI worker 1 (pid: 24, cores: 10)
spawned uWSGI worker 2 (pid: 33, cores: 10)
```

you should be able to go to the host URL you configured and see
Tank.

# Todo

* Mount local disk for tiddler storage and logging.
* Font-Awesome fonts not yet working.
* SSL. We must have it if oauth is being used.
* Making S3 storage for binaries optional.
* Getting twsock in the mix for websocket notifications.
* Initializing search index at start time.
* twikifier

## Perhaps

* Only run uwsgi, have something external to the container do HTTP.

# Who

Copyright 2014 Peermore Limited
BSD License
