from pathlib import Path


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'erp_db',       # 数据库名
        'USER': 'user',         # 数据库用户名
        'PASSWORD': 'password', # 数据库密码
        'HOST': 'postgres',           # 数据库服务器地址（Docker 容器名或主机地址）
        'PORT': '5432',         # PostgreSQL 默认端口
    }
}

