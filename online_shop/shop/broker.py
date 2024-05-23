# shop/broker.py
import os
import django
import dramatiq
from dramatiq.brokers.redis import RedisBroker

# Установите переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Настройка Django
django.setup()

# Настройка брокера Dramatiq
redis_broker = RedisBroker(url="redis://localhost:6379/0")
dramatiq.set_broker(redis_broker)
