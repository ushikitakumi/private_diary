# 開発環境固有の設定ファイル

# 共通設定ファイル読み込み
from .settings_common import *


# SECURITY WARNING: don't run with debug turned on in production!
# エラー発生時にデバッグ情報が画面に出力される
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = []

# ロギング設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # ロガーの設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # diaryアプリケーションが利用するロガー
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    # ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    # フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

# メールの配信先をコンソールに設定
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# メディアファイルの設定場所を指定
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')