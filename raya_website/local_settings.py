SECRET_KEY = '_&ve$y5^upyqi+wj#-zd_!ou(&-izg*adqlagigj673!rwn9mc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['cloudhypes.ir', 'www.cloudhypes.ir']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'raya_prod',
        'USER': 'dbadmin',
        'PASSWORD': 'p@ssw0rd342',
        'HOST': 'localhost'
    }
}
