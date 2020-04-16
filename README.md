# Сравниваем вакансии программистов

Получения информации о средних зарплатах разработчиков наиболее популярных языков программирования. В качестве источника информации используются сайты HeadHunter(https://hh.ru/) и SuperJob(https://www.superjob.ru/). Взаимодействие происходит по `API`

### Как установить

Для взаимодействия с `API SuperJob` нужен секретный ключ.

Зарегистрируйте приложение на сайте [API SuperJob](https://api.superjob.ru/)

При регистрации приложения от вас потребуют указать сайт. Введите любой, они не проверяют.

Секретный ключ имеет вид наподобие: `v3.r.132989819.b4e77aaac4a3c0ffa8bc4c2c0c0c9f95eaea1005.a6d449bdbff7410439ff999dfc9106492ade1574`

Скрипт берет секретный ключ из переменных окружения. Создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: 

`ПЕРЕМЕННАЯ=значение`.

Доступна следующая переменная:
- `SYPERJOB_SECRET_KEY` — секретный ключ SyperJob.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).