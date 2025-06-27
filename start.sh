#!/bin/bash

set -e  # Остановить выполнение при любой ошибке
cd /app

echo "Ожидание базы данных..."
/app/wait-for-it.sh db:3306 --timeout=30 --strict -- echo "База готова"

echo "Проверка наличия Alembic (migrations)..."

if [ ! -f "migrations/env.py" ]; then
  echo "Миграции не найдены. Инициализация Alembic..."
  flask db init
else
  echo "Миграции уже инициализированы."
fi

echo "Проверка обновлений моделей..."
flask db migrate -m "Автообновление схемы" || echo "Нет изменений моделей"

echo "Применение миграций..."
flask db upgrade

echo "Запуск приложения..."
exec gunicorn -b 0.0.0.0:5000 run:app