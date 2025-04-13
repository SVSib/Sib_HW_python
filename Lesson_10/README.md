
# Формирование и просмотр отчета о результатах тестов 
Для формирования и просмотра отчета о выполнении тестов необходимо подключить ***Allure***, ***Allure Report*** и ***Scoop***
___
## Подключаем Allure:
+ Скопируйте команду для подключения: _pip install allure-pytest_
+ Откройте терминал и перейдите к рабочей директории
+ Подключите Allure: _pip install allure-pytest_
___
## Подключаем Allure Report и Scoop:
+ установите Allure Report: _Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression_
+ Затем команду: _scoop install allure_
___
## Как запустить тесты для формирования отчета:
+ Запустите тесты и укажите путь к каталогу результатов тестирования: _pytest --alluredir allure-result_
+ В директории с тестами появится папка allure-result. Там сохранятся отчеты о тестах.
___
## Как просмотреть сформированный отчет:
+ Введите команду для генерации отчета о тестах: _allure serve allure-result_
+ Отчет откроется на локальном сервере в окне вашего браузера.