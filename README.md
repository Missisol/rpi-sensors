## Настройка проекта

### Датчик BME280
  - <https://www.donskytech.com/raspberry-pi-bme280-weather-station-using-python-and-flask/>
  - Необходимые пакеты - <https://pypi.org/project/RPi.bme280/>
  
  ![Распиновка](./static/images/pin-outs.png)


### Датчик DHT22
 - Необходимые пакеты - <https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup>
 - `sudo apt-get install libgpiod2`

  ![Распиновка](./static/images/pin-outs_1.png)

<br>
<hr>

### Настройка виртуальной среды
  - Create virtual environment: `python -m venv <env name>`
  - Activate venv: `source <env name>/bin/activate`

### Системные требования для установки mod-wsgi
 - <https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-debian-8>
 - <https://pypi.org/project/mod-wsgi/>

If you are running Debian or Ubuntu Linux with Apache 2.4 system packages, regardless of which Apache MPM is being used, you would need both: apache2б, apache2-dev  
`sudo apt install apache2 apache2-dev libapache2-mod-wsgi-py3`

### Установка библиотек перед установкой mysqlclient
<https://pypi.org/project/mysqlclient/>

`sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`

### Установка пакетов: 
`pip install -r requirements.txt`

### Создание файла requirements.txt:
`pip freeze > requirements.txt`

### Создание файла .env из /smart/.env-example

### Установка MariaDB
<https://www.digitalocean.com/community/tutorials/how-to-install-mariadb-on-ubuntu-20-04-ru>

- установка MariaDB:  
  `sudo apt install mariadb-server`

- настройка MariaDB:  
  `sudo mysql_secure_installation`

- создание административного пользователя с аутентификацией по паролю:
  ```sh
  sudo mariadb
  GRANT ALL ON *.* TO 'admin'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;
  FLUSH PRIVILEGES;
  exit
  ```

### Установка RabbitMQ брокер:
  `sudo apt install rabbitmq-server`
### Запуск RabbitMQ сервера:
  `systemctl enable rabbitmq-server`
  `systemctl start rabbitmq-server`
### Проверка статуса:
  `systemctl status rabbitmq-server`

### Настройка периодических задач с celery
- <https://habr.com/ru/sandbox/179864/>
- <https://simpleisbetterthancomplex.com/tutorial/2017/08/20/how-to-use-celery-with-django.html>
- <https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html>

## Запуск проекта
### Запустить сервер: 
`python manage.py runserver`

### Запустить воркер: 
`celery -A <name_of_project> worker -l info`

### Запустить beat: 
`celery -A <name_of_project> beat -l info`

```sh
celery -A smart worker -l info
celery -A smart beat -l info
```

### Настройка деплоя с wsgi_mod
<https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/modwsgi/>

 - Добавить в файл /etc/apache2/sites-available/000-default.conf:
  ```sh
  Alias /static /var/www/html/smartProject/static
  <Directory /var/www/html/smartProject/static>
      Require all granted
  </Directory>

  <Directory /var/www/html/smartProject/smart>
      <Files wsgi.py>
          Require all granted
      </Files>
  </Directory>

  WSGIDaemonProcess django python-home=/var/www/html/smartProject/venv python-path=/var/www/html/smartProject
  WSGIProcessGroup django
  WSGIScriptAlias / /var/www/html/smartProject/smart/wsgi.py
  ```

### Демонизация celery
- <https://docs.celeryq.dev/en/stable/userguide/daemonizing.html#example-django-configuration>
- <https://seulcode.tistory.com/440>

#### Создаем группу celery
`sudo groupadd celery`

#### Добавляем в группу пользователя pi
`sudo usermod -aG celery pi`

<https://losst.pro/kak-dobavit-polzovatelya-v-gruppu-linux>
<https://losst.pro/kak-dat-prava-na-papku-polzovatelyu-linux>


#### Создаем файл конфигурации /etc/systemd/celery.conf
```sh
CELERYD_NODES="w1"

CELERY_BIN="/var/www/html/smartProject/venv/bin/celery"

CELERY_APP="smart"

CELERYD_MULTI="multi"

CELERYD_OPTS="--time-limit=300 --concurrency=8"

CELERYD_PID_FILE="/var/run/celery/%n.pid"
CELERYD_LOG_FILE="/var/log/celery/%n.log"
CELERYD_LOG_LEVEL="INFO"

CELERYBEAT_PID_FILE="/var/run/celery/beat.pid"
CELERYBEAT_LOG_FILE="/var/log/celery/beat.log"
```

#### Создание директорий для log и pid файлов
Создаем systemd-tmpfiles файл для создания рабочих директорий для log и pid файлов
  
<https://www.freedesktop.org/software/systemd/man/latest/tmpfiles.d.html>


Файл: /etc/tmpfiles.d/celery.conf  
`#Type Path Mode User Group Age Argument…`
```sh
d /var/run/celery 0755 pi celery -
d /var/log/celery 0755 pi celery -
```

#### Создаем сервис для worker celery: /etc/systemd/system/celery.service
```sh
[Unit]
Description=Celery Service
After=network.target mariadb.service rabbitmq-server.service
Requires=mariadb.service rabbitmq-server.service

[Service]
Type=forking
User=pi
Group=celery
EnvironmentFile=/etc/systemd/celery.conf
WorkingDirectory=/var/www/html/smartProject/
ExecStart=/bin/sh -c '${CELERY_BIN} -A $CELERY_APP multi start $CELERYD_NODES \
    --pidfile=${CELERYD_PID_FILE} --logfile=${CELERYD_LOG_FILE} \
    --loglevel="${CELERYD_LOG_LEVEL}" $CELERYD_OPTS'
ExecStop=/bin/sh -c '${CELERY_BIN} multi stopwait $CELERYD_NODES \
    --pidfile=${CELERYD_PID_FILE} --logfile=${CELERYD_LOG_FILE} \
    --loglevel="${CELERYD_LOG_LEVEL}"'
ExecReload=/bin/sh -c '${CELERY_BIN} -A $CELERY_APP multi restart $CELERYD_NODES \
    --pidfile=${CELERYD_PID_FILE} --logfile=${CELERYD_LOG_FILE} \
    --loglevel="${CELERYD_LOG_LEVEL}" $CELERYD_OPTS'
Restart=always

[Install]
WantedBy=multi-user.target
```

#### Создаем сервис для beat: /etc/systemd/system/celerybeat.service
```sh
[Unit]
Description=CeleryBeat Service
After=network.target mariadb.service rabbitmq-server.service
Requires=mariadb.service rabbitmq-server.service

[Service]
Type=simple
User=pi
Group=celery
EnvironmentFile=/etc/systemd/celery.conf
WorkingDirectory=/var/www/html/smartProject
ExecStart=/bin/sh -c '${CELERY_BIN} -A ${CELERY_APP} beat  \
    --pidfile=${CELERYBEAT_PID_FILE} \
    --logfile=${CELERYBEAT_LOG_FILE} --loglevel=${CELERYD_LOG_LEVEL}'
Restart=always

[Install]
WantedBy=multi-user.target
```

#### Перезапускаем сервисы

```sh
sudo systemctl daemon-reload
sudo systemctl start celery.service
sudo systemctl start celerybeat.service
```

Для запуска сервисов при загрузке компьютера

```sh
sudo systemctl enable celery.service
sudo systemctl enable celerybeat.service
```


#### Как использовать systemctl для управления systemd сервисами
<https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units-ru>

