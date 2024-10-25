def send_email(message, recipient, *, sender="university.help@gmail.com"):

    suf = ('.com', '.net', '.ru')
    if not (recipient.endswith(suf) and sender.endswith(suf)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    if '@' not in (sender and recipient):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    if sender == recipient and recipient == sender:
        print('Нельзя отправить письмо самому себе!')

    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

    else:
        print(message)


send_email('Это сообщение для проверки связи', 'vasyok133@gmail.com',
           sender="university.help@gmail.com")
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru',
            sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
'vasyok133@@gmail.com'