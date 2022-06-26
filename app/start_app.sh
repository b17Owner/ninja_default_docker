#!/bin/bash

# Подгружаем переменные из .env
if [ -f .env ]
then
    source .env
fi

# Парсинг входных параметров
while [[ $# -gt 0 ]]; do
  case $1 in
    -h|--host)
      HOST="$2"
      shift # past argument
      shift # past value
      ;;
    -p|--port)
      PORT="$2"
      shift # past argument
      shift # past value
      ;;
    -u|--user)
      USER="$2"
      shift # past argument
      shift # past value
      ;;
    -s|--secret)
      SECRET="$2"
      shift # past argument
      shift # past value
      ;;
    --default)
      DEFAULT=YES
      shift # past argument
      ;;
    -*|--*)
      echo "Unknown option $1"
      exit 1
      ;;
    *)
      NAME+=("$1") # save positional arg
      shift # past argument
      ;;
  esac
done

# Выводим справку, если не задано имя приложения
if [[ $NAME == '' ]]
then
cat <<- EOF
    Использование: start_app.sh имя_приложения [параметры]
        -h | --host       Хост
        -p | --port       Порт
        -u | --user       Пользователь
        -s | --secret       Пароль
EOF
  exit
fi

if [ -z $HOST ]
then
    HOST='0.0.0.0'
fi

if [ -z $PORT ]
then
    PORT='8000'
fi

# Проверяем, существует ли папка проекта, либо
# необходимо инициализировать новый проект
  if [ -d ./${NAME} ]
  then
cat <<- EOF
    Запуск проекта : ${NAME}
EOF
    cd ${NAME}
    python3 manage.py runserver ${HOST}:${PORT}
  else
cat <<- EOF
    Инициализация приложения: $NAME
EOF
    django-admin startproject ${NAME}
    cd ${NAME}
    django-admin startapp ${NAME}_app
    # --- r
    # Добавляем название приложение в settings.py
    N=40 # номер строки для вставки
    sed -e $N"s/^/    \'${NAME}_app\',\n/" -i ${NAME}/settings.py
    # Создаем миграции
    python3 manage.py makemigrations
    # Запускаем миграции
    python3 manage.py migrate
    # Запускаем сервер
    python3 manage.py runserver ${HOST}:${PORT}
  fi
