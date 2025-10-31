## Platzi Fake Store API Automation Tests

Этот проект реализует автоматизированные тесты для [Platzi Fake Store API](https://fakeapi.platzi.com/en).

Тесты написаны с использование **Python**, **Pytest**, **Allure**, **Pydantic**, **Faker** и **HTTPX**.
## Описание

Цель этого проекта — автоматизация тестирования REST API сервера Platzi Fake Store.
Автотесты охватывают ключевые функции приложения, чтобы гарантировать его стабильность и корректность.

Проект разработан в рамках практики написания API-автотестов и включает:

- API-клиенты для структурированного взаимодействия с эндпоинтами
- Фикстуры Pytest для повторного использования и удобного сопровождения тестовых настроек
- Модели Pydantic для строгой валидации данных
- Проверка схем для обеспечения корректности API-контракта
- Генерация фиктивных данных для имитации реальных сценариев
- Allure отчет для визуализации и анализа результатов тестов

### 📊 Allure отчет

Результаты выполнения автоматизированных API-тестов доступны по ссылке: [Allure report](https://borisborisa.github.io/api_autotests/)

## Начало работы

### Клонирование репозитория

```
git clone https://github.com/BorisBorisa/api_autotests.git
cd api_autotests
```

### Создание виртуального окружения
#### Linux / MacOS
```bash
python3 -m venv venv
source venv/bin/activate
```
#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Установка зависимостей
```bash
pip install -r requirements.txt
```
### Запуск тестов с генерацией отчета Allure
```bash
pytest -m "regression" --alluredir=./allure-results
```
Эта команда запустит все тесты проекта и выведет результаты в терминале.

### Просмотр отчета Allure
```bash
allure serve allure-results
```
Эта команда откроет отчет Allure в вашем браузере по умолчанию.