# 🌦️ ClimaTrack

**ClimaTrack** — мікросервіс на основі FastAPI для збору та збереження температури по містах.  
Дані зберігаються у базі, оновлюються автоматично за допомогою Celery, а доступ до API захищено через Bearer Token.

---

## 🚀 Можливості
- ⏱ Щогодинне збереження температури для заданого міста  
- 🌍 Інтеграція з OpenWeather API (або іншим погодним API)  
- 🗂 Зберігання історії температур у БД  
- 🔐 Авторизація через Bearer Token (в Swagger можна підставити токен для тестування)  
- 🐘 Використання PostgreSQL для зберігання  
- 🟢 Підтримка Celery + Redis для асинхронних задач з інтегрованим логуванням 
- 🐳 Готовий для запуску у Docker / Docker Compose  

---

## 🛠️ Технології
- [FastAPI](https://fastapi.tiangolo.com/) — бекенд  
- [SQLAlchemy + Alembic](https://www.sqlalchemy.org/) — ORM та міграції  
- [Pydantic](https://docs.pydantic.dev/) — валідація даних  
- [Celery](https://docs.celeryq.dev/) — асинхронні задачі  
- [Redis](https://redis.io/) — брокер для Celery  
- [PostgreSQL](https://www.postgresql.org/) — основна база даних  
- [Docker](https://www.docker.com/) — контейнеризація  

---

## ⚙️ Запуск через Docker
> Попередньо переконайся, що у тебе встановлено **Docker** та **Docker Compose**.

```bash
git clone git@github.com:Igor-Cegelnyk/clima-track.git
cd clima-track
docker-compose up --build -d
```

### 📘 API Документація

👉 http://localhost:8000/docs

## 📊 Моніторинг задач (Flower)

Для зручного контролю стану Celery є веб-інтерфейс:  

📍 [http://localhost:5555](http://0.0.0.0:5555)  

Там можна переглянути:
- чергу задач  
- статус виконання  
- історію запусків  
- логування помилок  

## 🔑 Налаштування

Всі параметри конфігурації беруться з **.env.template** файлу для тестування:

```env
# Місто за замовчуванням
APP_CONFIG__WEATHER_API__CITY=Kyiv

# OpenWeather API 
APP_CONFIG__WEATHER_API__URL=http://api.openweathermap.org/data/2.5/weather

# Токен (32 символи)
APP_CONFIG__TOKEN__KEY=a93fbd172c54e6a0d8b4c3e9f7a25d61
```

### 📡 Для ручного завантаження температури
- Endpoint: /temperatures 
  - Method: POST
  - Request Body:

```
{
  "city_name": "Kyiv" --Вказати бажане місто
}
```