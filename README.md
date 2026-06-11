# Effictive-Mobile

Данное задание было выполнено на виртуальной машине в VirtualBox на ОС Ubuntu 24.04. 

## Установка тестового задания

Для работы с тестовым заданием на свою ОС нужно скачать git, ansible, docker, curl.
Для Unix-систем поможет команда:
```sh
apt update && apt install ansible docker git curl
```

Далее нужно скопировать репозиторий данного проекта:
```sh
git clone https://github.com/Nik7Zol/Effictive-Mobile.git
```

После нужно перейти в клонированный католог:
```sh
cd Effictive-Mobile
```

## Запуск контейнеров

Создаём и запускаем контейнеры, после проверяем, что их статус "up"

```sh
 docker-compose up -d --build
 docker-compose ps
```

При правильном запуске вы должны увидеть:

```
Creating backend ... done
Creating nginx   ... done
```

![Launching containers](https://github.com/Nik7Zol/Effictive-Mobile/blob/main/images/Launching_containers.png)

## Проверка работоспособности контейнеров

Проверяем через утилиту curl, что всё работает штатно.

```
curl http://localhost
```
Ожидаемый ответ:
![Curl](https://github.com/Nik7Zol/Effictive-Mobile/blob/main/images/Curl.png)

## Схема (nginx->backend)

Nginx, получив запрос, выполняет proxy_pass на upstream "backend:8080"

Запрос переходит по Docker-сети (network) по имени сервиса (backend) и порту(8080).

Backend, слушает порт 8080, и отвечает на любой запрос, заготовленной app.py в фразой.
