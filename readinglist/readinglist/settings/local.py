from .base import *
import os

DATABASES = {'default': dj_database_url.config(
        default='sqlite:////{0}'.format(os.path.join(PROJECT_BASE, 'readinglist.sqlite'))),
}
