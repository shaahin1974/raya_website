
SECRET_KEY = '_&ve$y5^upyqi+wj#-zd_!ou(&-izg*adqlagigj673!rwn9mc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rayadb',
        'USER': 'dbadmin',
        'PASSWORD': 'p@ssw0rd342',
        'HOST': 'localhost'
    }
}
