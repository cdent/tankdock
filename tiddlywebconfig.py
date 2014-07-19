# DO NOT ADJUST (unless you know what you are doing)
# These settings are used by tests and development.
import mangler

# adjust these config settings for use in config below
redirect_uri = '@HOST@/_oauth/callback'
server_host = {
    'scheme': 'http',
    'host': 'plank',
    'port': '80'
}
github_id = ''
github_secret = ''
google_id = ''
google_secret = ''
facebook_id = ''
facebook_secret = ''

aws_access_key = ''
aws_secret_key = ''
aws_bucket = ''

secret = ''

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

    'oauth.servers': {
        'github': {
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
        },
        'google': {
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
        },
        'facebook': {
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
    },
    'oauth.use_mapuser': True,
    'closet.aws_access_key': aws_access_key,
    'closet.aws_secret_key': aws_secret_key,
    'closet.bucket': aws_bucket

    'server_host': server_host,
    #'markdown.safe_mode': False,
    'twanager.tracebacks': True,
    #'socket.link': 'https://tank.peermore.com:8080/socket.io/socket.io.js',
}
