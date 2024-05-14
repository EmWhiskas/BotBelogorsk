Чтобы запустить бота пропишите в терминале команду: pip install -r requirements.txt
Возможно потребуется указать путь к папке. Я хз в пайчарме работает.

Если есть аккаунт гугл:
Как подключать апи
    Заходим на сайт https://console.cloud.google.com/ >>> Создаем проект https://prnt.sc/yxazUlraAbxe >>> Находим вкладку APIs & Services нажимаем >>> в открывшейся вкладке находим google sheets api, добавляем к себе >>> Переходим как тут https://prnt.sc/nkGDJSLqP2ta >>> делаем как тут https://prnt.sc/xClFp8fKYHWd >>> Клацаем тут https://prnt.sc/IhMVET9bFk-U

    После этого у Вас появится файл со сложным названием пример: 2392390323-sdflsdtractor.json его нужно переименовать в token.json
    Например: 2392390323-sdflsdtractor.json >>> token.json

    После этого этапа, нужно переписать 11 строку в файлах с названием Zapros...py
    11 строка - SAMPLE_SPREADSHEET_ID = '1D5LT5gGjbzfYrKjTAIg0E7u31i4W1wSnxbydeYe3Gtc'
    айди берется из ссылки к таблицам в браузере сверху
    https://docs.google.com/spreadsheets/d/1D5LT5gGjbzfYrKjTAIg0E7u31i4W1wSnxbydeYe3Gtc/edit#gid=1934313248
    1D5LT5gGjbzfYrKjTAIg0E7u31i4W1wSnxbydeYe3Gtc <<< нужна эта часть

    После этого у Вас появится файл со сложным названием пример: 2392390323-sdflsdtractor.json его нужно переименовать в token.json
    Например: 2392390323-sdflsdtractor.json >>> token.json
    Положить этот файл в папку bot
Иначе Создать

Если уверенны, что библиотеки установленны, запустить файл bot.py, при 1 запросе, потребует авторизацию, авторизуйтесь, пожалуйста.
Если не уверенны в безопасности можете перечитать код, не шифрован. Я честно-честно говорю там все чисто.

Чтобы обновить файл bot.py боту нужно отправить файл, к сожалению защиты от левых файлов нету. Доделаю к лету.




