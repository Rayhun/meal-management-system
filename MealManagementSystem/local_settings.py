import os

# Database Configaretion
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', 5432),
        'NAME': os.getenv('DB_NAME', 'mms_db'),
        'USER': os.getenv('DB_USER', 'mms_user'),
        'PASSWORD': os.getenv('DB_PASS', 'A41424344i')
    }
}

# secret key
SECRET_KEY = 'django-insecure-uj2gqvtm1y(-%4_xhi73#+#w%mf!^f%4bk9$yuh9el7+u+796z' # noqa

# adding config
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dwrvrww0z',
    'API_KEY': '461961843175113',
    'API_SECRET': 'kW6HenhqJmzLI0V03TypJwbh4uk'
}
# Default
FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
