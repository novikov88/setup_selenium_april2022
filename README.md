# setup_selenium_april2022
Для запуска локально:
- Запуск Selenoid - **./cm selenoid start** из директории где лежит Selenoid
- Запуск Selenoid-UI - **./cm selenoid-ui start** из директории где лежит Selenoid
- Запуск Opencart - **docker-compose up -d** из директории где лежит Opencart

**Запуск тестов для магазина и админки осуществляется разными командами:**

**Store**:

- sudo docker run --name tests_run --network selenoid tests -m "not admin"; docker cp tests_run:/app/allure-results . && docker cp tests_run:/app/logs . && ~/Downloads/allure/bin/allure generate --clean 
- (!) при необходимости изменить расположение allure/bin/allure


**Admin**:

- sudo docker run --name tests_run --network selenoid tests -m "admin" --url "http://192.168.1.70:8081/admin/"; docker cp tests_run:/app/allure-results . && docker cp tests_run:/app/logs . && ~/Downloads/allure/bin/allure generate --clean 
- (!) при необходимости изменить ip и расположение allure/bin/allure