# language: ru
Функционал: Добавление ссылок

Сценарий: Пользователь видит кнопку добавления ссылки
    Допустим загружен документ ЗАКОН КЫРГЫЗСКОЙ РЕСПУБЛИКИ О государственной регистрации юридических лиц, филиалов
    Если я нахожусь на странице "ЗАКОН КЫРГЫЗСКОЙ РЕСПУБЛИКИ О государственной регистрации юридических лиц, филиалов (представительств)"
    То вижу кнопку "Ссылка" в содержании статьи-"1"
    И вижу кнопку "Ссылка" в содержании статьи-"5"

Сценарий: Пользователь видит модальное окно при нажатии на кнопку "Ссылка"
    Допустим загружен документ НАЛОГОВЫЙ КОДЕКС КЫРГЫЗСКОЙ РЕСПУБЛИКИ
    И я нахожусь на странице "НАЛОГОВЫЙ КОДЕКС КЫРГЫЗСКОЙ РЕСПУБЛИКИ"
    Если я нажимаю на кнопку "Ссылка" под "1"-статьей
    То вижу модальное окно

Сценарий: Пользователь попадает на страницу документа "источника" после подтверждения
    Допустим открыто окно подтверждения на странице "ЗАКОН КЫРГЫЗСКОЙ РЕСПУБЛИКИ О государственной регистрации юридических лиц, филиалов (представительств)"
    Если я нажимаю на кнопку "ОК"
    То вижу что нахожусь на странице "ЗАКОН КЫРГЫЗСКОЙ РЕСПУБЛИКИ О государственной регистрации юридических лиц, филиалов (представительств)"

Сценарий: Статья "источник" содержит в себе ссылку к "приемнику" после добавления
    Допустим загружены документы НАЛОГОВЫЙ КОДЕКС, ЗАКОН КЫРГЫЗСКОЙ РЕСПУБЛИКИ О государственной регистрации юридических лиц
    И я нахожусь на странице "ЗАКОН КЫРГЫЗСКОЙ РЕСПУБЛИКИ О государственной регистрации юридических лиц, филиалов (представительств)"
    Если я добавляю ссылку с "12"-статьи на "Статья 2. Налоговое законодательство Кыргызской Республики" в документе "НАЛОГОВЫЙ КОДЕКС КЫРГЫЗСКОЙ РЕСПУБЛИКИ"
    То вижу что "12"-статья содержит ссылку "Статья № 2"

Сценарий: Статья "приемник" содержит в себе ссылку к "источнику"
    Допустим загружены документы НАЛОГОВЫЙ КОДЕКС, ЗАКОН КЫРГЫЗСКОЙ РЕСПУБЛИКИ О государственной регистрации юридических лиц
    И я нахожусь на странице "ЗАКОН КЫРГЫЗСКОЙ РЕСПУБЛИКИ О государственной регистрации юридических лиц, филиалов (представительств)"
    И я добавляю ссылку с "4"-статьи на "Статья 2. Налоговое законодательство Кыргызской Республики" в документе "НАЛОГОВЫЙ КОДЕКС КЫРГЫЗСКОЙ РЕСПУБЛИКИ"
    Если я перехожу на страницу "НАЛОГОВЫЙ КОДЕКС КЫРГЫЗСКОЙ РЕСПУБЛИКИ"
    То вижу что "2"-статья содержит ссылку "Статья № 4"
