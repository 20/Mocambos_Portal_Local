# Django settings for Mocambos_Portal project.
BASE_ROOT = '/home/taina/CasaDeCulturaTaina/'
ROOT_URLCONF = 'CasaDeCulturaTaina.urls'
GITANNEX_DIR = 'gitannex'
SERIALIZED_DIR = 'serialized'
PORTAL_NAME = 'taina.mocambos.net'

# Django Debug toolbar
INTERNAL_IPS = ('127.0.0.1', '192.168.56.1',)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': BASE_ROOT + 'Mocambos_Portal.sqlite',          # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
    # THIS ONE IS NOT USED FOR DJANGO_AUTH_LDAP
    # 'ldap': {
    #     'ENGINE': 'ldapdb.backends.ldap',
    #     'NAME': 'ldap://localhost/',
    #     'USER': 'cn=admin,dc=mocambos,dc=net',
    #     'PASSWORD': 'livre',
    #  }
}

#DATABASE_ROUTERS = ['ldapdb.router.Router']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = BASE_ROOT + 'media/'
#MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = BASE_ROOT + 'static/'
print STATIC_ROOT
#STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/taina/CasaDeCulturaTaina/static/sta',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^377hco8=v62$qirvlvr4x!#bq_5@p6nq6rf@6edvtr-&k4!6t'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
#    'polls',
#    'easy_thumbnails',
#    'filer',
#    'grappelli',
#    'filebrowser',
    'django.contrib.admin',
#    'django_bfm',
    'mmedia',
    'gitannex',
#    'debug_toolbar',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
        'simple': {
            'format': '%(levelname)s %(message)s'
            },
        },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        'gitannex': {
            'handlers': ['console'],
            'level': 'INFO',
            #'filters': ['gitannex']
            },
        'mmedia': {
            'handlers': ['console'],
            'level': 'INFO',
            #'filters': ['gitannex']
            },
        }
}

#ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

##############################################################################
# LDAP Authentication Backend                              
# 

import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType


# Baseline configuration.
AUTH_LDAP_SERVER_URI = "ldap://localhost"
AUTH_LDAP_BIND_DN = "cn=admin,dc=mocambos,dc=net"
AUTH_LDAP_BIND_PASSWORD = "livre"
AUTH_LDAP_USER_SEARCH = LDAPSearch("dc=mocambos,dc=net",
    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
# or perhaps:
# AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=users,dc=example,dc=com"

# Set up the basic group parameters.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("dc=mocambos,dc=net",
    ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
)
#AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()

# # Only users in this group can log in.
# #AUTH_LDAP_REQUIRE_GROUP = "cn=enabled,ou=django,ou=groups,dc=example,dc=com"
# AUTH_LDAP_REQUIRE_GROUP = "cn=www,ou=groups,dc=mocambos,dc=net"

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

# AUTH_LDAP_PROFILE_ATTR_MAP = {
#     "employee_number": "employeeNumber"
# }

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_staff": "cn=coordenadores,ou=groups,dc=mocambos,dc=net",
    "is_superuser": "cn=hackers,ou=groups,dc=mocambos,dc=net"
#     "is_active": "cn=active,ou=django,ou=groups,dc=example,dc=com",
#     "is_staff": "cn=staff,ou=django,ou=groups,dc=example,dc=com",
#     "is_superuser": "cn=superuser,ou=django,ou=groups,dc=example,dc=com"
}

# AUTH_LDAP_PROFILE_FLAGS_BY_GROUP = {
#     "is_awesome": "cn=awesome,ou=django,ou=groups,dc=example,dc=com",
# }

# This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# Use LDAP group membership to calculate group permissions.
#AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache group memberships for an hour to minimize LDAP traffic
AUTH_LDAP_CACHE_GROUPS = False
#AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600


# Keep ModelBackend around for per-user permissions and maybe a local
# superuser.
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

#FILER_STATICMEDIA_PREFIX = '/media/filer/'
