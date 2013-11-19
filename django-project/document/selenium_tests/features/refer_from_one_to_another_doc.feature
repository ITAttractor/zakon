# language: ru
Функционал: Чтобы пользователь имел возможность добавлять ссылки

Сценарий: Пользователь ссылается с одного нормативного акта на другой
    Допустим загружен документ "Nalogovij_Kodeks.rtf"
    И загружен документ "zakon.rtf"
    И нахожусь на странице документа "НАЛОГОВЫЙ КОДЕКС КЫРГЫЗСКОЙ РЕСПУБЛИКИ"
    Если внутри "Статья 10. Принцип справедливости налогообложения" кликаю по кнопке "Ссылка"
    Тогда вижу модальное окно "Список документов"
    И в документе "ЗАКОН КЫРГЫЗСКОЙ РЕСПУБЛИКИ О государственной регистрации юридических лиц, филиалов (представительств)" вижу статью "Статья 1. Отношения, регулируемые настоящим Законом"
    Если щелкаю на ссылку "Статья 1. Отношения, регулируемые настоящим Законом"
    Тогда вижу окно подтверждения c сообщением "Вы хотите добавить ссылку?"
    Если я кликаю "ОК"
    То вижу что нахожусь в документе "НАЛОГОВЫЙ КОДЕКС КЫРГЫЗСКОЙ РЕСПУБЛИКИ"
    И вижу ссылку "Документ № 2 Статья № 1" под статьей "Статья 10. Принцип справедливости налогообложения"