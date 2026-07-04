# 💬 پت ریل‌تایم با Django Channels

یه اپ چت ساده با WebSocket که بدون نیاز به Redis کار می‌کنه.

## نصب و اجرا

```bash
# 1. نصب پکیج‌ها
pip install -r requirements.txt

# 2. migrate
python manage.py migrate

# 3. ران کردن سرور (با daphne برای WebSocket)
daphne -p 8000 config.asgi:application
```

بعد برو روی: http://localhost:8000

## امکانات

- ثبت‌نام و ورود کاربران
- ساخت اتاق گفتگو
- ارسال پیام ریل‌تایم با WebSocket
- نمایش پیام‌های قدیمی (از دیتابیس)
- اطلاع از ورود/خروج کاربران
- رابط کاربری فارسی راست‌چین
- ذخیره پیام‌ها در SQLite

## ساختار پروژه

```
chat_app/
├── config/           # تنظیمات جنگو
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py       # WebSocket routing
├── chat/
│   ├── models.py     # Room, Message
│   ├── consumers.py  # WebSocket consumer
│   ├── views.py
│   └── routing.py
├── templates/
└── requirements.txt
```

## نکته

برای production از Redis به جای InMemoryChannelLayer استفاده کن:
```python
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {"hosts": [("127.0.0.1", 6379)]},
    }
}
```
