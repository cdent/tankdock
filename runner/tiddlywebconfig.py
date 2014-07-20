import mangler
import urlparse

# Adjust these config settings for use in config below
# Base URL of the server with scheme, host and part
# e.g "https://tank.peermore.com/"
base_url = ''

# Cookie salt. Set to a complex random string.
secret = 'cookies taste better with a bit of salt'

# oauth ids and secrets. At least one id/secret pair
# must be set.
github_id = ''
github_secret = ''
google_id = ''
google_secret = ''
facebook_id = ''
facebook_secret = ''

# Amazon S3 access keys and bucket name.
aws_access_key = ''
aws_secret_key = ''
aws_bucket = ''

# End of Customizations

# Generate config from customizations
redirect_uri = urlparse.urljoin(base_url, '/_oauth/callback')
scheme, netloc, _, _, _ = urlparse.urlsplit(base_url)

if ':' in netloc:
    hostname, port = netloc.split(':', 1)
else:
    port = '80' if scheme is 'http' else '443'
    hostname = netloc

server_host = {
    'scheme': scheme,
    'host': hostname,
    'port': port
}

oauth_servers = {}

if github_id and github_secret:
    oauth_servers['github'] = {
        'client_id': github_id,
        'client_secret': github_secret,
        'scope': [],
        'auth_uri': 'https://github.com/login/oauth/authorize',
        'token_uri': 'https://github.com/login/oauth/access_token',
        'redirect_uri': redirect_uri,
        'no_trust': True,
        'info_uri': 'https://api.github.com/user',
        'response_map': {
            'login': 'login',
            'name': 'name',
            'email': 'email'
        }
    }

if google_id and google_secret:
    oauth_servers['google'] = {
        'client_id': google_id,
        'client_secret': google_secret,
        'scope': ['openid', 'email'],
        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
        'redirect_uri': redirect_uri,
        'info_uri': 'https://www.googleapis.com/oauth2/v3/userinfo',
        'response_map': {
            'login': 'given_name',
            'name': 'name',
            'email': 'email'
        }
    }

if facebook_id and facebook_secret:
    oauth_severs['facebook'] = {
        'client_id': facebook_id,
        'client_secret': facebook_secret,
        'scope': ['email'],
        'auth_uri': 'https://www.facebook.com/dialog/oauth',
        'token_uri': 'https://graph.facebook.com/oauth/access_token',
        'redirect_uri': redirect_uri,
        'info_uri': 'https://graph.facebook.com/me',
        'response_map': {
            'login': 'username',
            'name': 'name',
            'email': 'email'
        }
    }

# beyond here nothing to worry about
config = {
    'secret': secret,
    'system_plugins': ['tiddlywebplugins.tank'],
    'twanager_plugins': ['tiddlywebplugins.tank', 'tiddlywebplugins.caching'],
    'server_store': ['tiddlywebplugins.caching', {}],
    'cached_store': ['tiddlywebplugins.devstore2',
        {'devstore_root': '/home/tiddlyweb/tank/src'}],
    'wrapped_devstore': ['text',
        {'store_root': 'store'}],
    'log_level': 'WARN',
    'memcache.cache_lists': True,
    'linkdb_config': 'sqlite:////home/tiddlyweb/tank/links.db',
    'oauth.servers': oauth_servers,
    'oauth.use_mapuser': True,
    'closet.aws_access_key': aws_access_key,
    'closet.aws_secret_key': aws_secret_key,
    'closet.bucket': aws_bucket,
    'server_host': server_host,
    'twanager.tracebacks': True,
    #'socket.link': 'https://tank.peermore.com:8080/socket.io/socket.io.js',
}
