import random

import config
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def filter_messages(message: types.Message):

    chatId = message.chat.id
    text = message.text.lower()

    rifms = ['отражений', 'значений', 'возникновений', 'изображений', 'построений', 'оформлений', 'укреплений',
             'заведений', 'соображений', 'завершений', 'умений', 'соотношений', 'спасений', 'движений', 'приобретений',
             'улучшений', 'напряжений', 'поражений', 'ведений', 'удивлений', 'проявлений', 'происхождений',
             'расширений', 'осуществлений', 'распространений', 'изменений', 'обучений', 'объяснений', 'подразделений',
             'падений', 'восстановлений', 'распоряжений', 'соглашений', 'чтений', 'рассмотрений', 'протяжений',
             'наблюдений', 'направлений', 'утверждений', 'постановлений', 'сокращений', 'возвращений', 'уважений',
             'стремлений', 'ограничений', 'преступлений', 'продолжений', 'введений', 'произведений', 'течений',
             'сохранений', 'общений', 'давлений', 'объединений', 'разрешений', 'учреждений', 'изучений', 'обсуждений',
             'обращений', 'выступлений', 'настроений', 'управлений', 'снижений', 'помещений', 'сообщений', 'поведений',
             'сведений', 'ощущений', 'выражений', 'отделений', 'назначений', 'евгений', 'мышлений', 'явлений',
             'побуждений', 'наполнений', 'возобновлений', 'смятений', 'торможений', 'подключений', 'печений',
             'пробуждений', 'поощрений', 'возведений', 'очищений', 'выполнений', 'извлечений', 'смирений', 'положений',
             'присвоений', 'наставлений', 'огорчений', 'оздоровлений', 'искажений', 'присоединений', 'понижений',
             'устремлений', 'почтений', 'заключений', 'охлаждений', 'разграничений', 'соприкосновений', 'обогащений',
             'вручений', 'пренебрежений', 'скоплений', 'заполнений', 'отчуждений', 'обозрений', 'воспалений',
             'исполнений', 'правонарушений', 'прочтений', 'землетрясений', 'уравнений', 'вращений', 'отчислений',
             'крещений', 'нововведений', 'удобрений', 'стечений', 'увеличений', 'погашений', 'разоблачений', 'рождений',
             'наведений', 'примирений', 'забвений', 'осмыслений', 'сбережений', 'извинений', 'варений', 'подавлений',
             'искушений', 'исправлений', 'расхождений', 'нарушений', 'закреплений', 'вхождений', 'машиностроений',
             'приведений', 'перечислений', 'обыкновений', 'крушений', 'смущений', 'загрязнений', 'оснащений',
             'хождений', 'сомнений', 'покушений', 'поселений', 'возмещений', 'добавлений', 'истечений', 'осложнений',
             'перераспределений', 'излучений', 'усмотрений', 'злоупотреблений', 'ослаблений', 'поколений',
             'затруднений', 'обобщений', 'превышений', 'пересечений', 'благословений', 'оживлений', 'нанесений',
             'углублений', 'пополнений', 'мировоззрений', 'вознаграждений', 'получений', 'предназначений', 'ухудшений',
             'осуждений', 'снабжений', 'мучений', 'преувеличений', 'обострений', 'вторжений', 'недоразумений',
             'поздравлений', 'прикосновений', 'заявлений', 'утешений', 'сближений', 'сопоставлений', 'увольнений',
             'приспособлений', 'оскорблений', 'просвещений', 'налогообложений', 'отоплений', 'обозначений', 'выяснений',
             'исключений', 'ранений', 'уточнений', 'подчинений', 'служений', 'ускорений', 'отступлений', 'нахождений',
             'удостоверений', 'делений', 'разъяснений', 'изложений', 'впечатлений', 'проникновений', 'вдохновений',
             'мнений', 'унижений', 'удалений', 'повторений', 'презрений', 'сражений', 'откровений', 'отвращений',
             'повреждений', 'передвижений', 'достижений', 'одобрений', 'возмущений', 'исчезновений', 'вложений',
             'нетерпений', 'возражений', 'обнаружений', 'прощений', 'изумлений', 'потрясений', 'появлений',
             'отклонений', 'упражнений', 'определений', 'перемещений', 'совершений', 'месторождений', 'устранений',
             'приготовлений', 'восхищений', 'заблуждений', 'суждений', 'стихотворений', 'возбуждений', 'составлений',
             'повышений', 'приближений', 'лишений', 'творений', 'самоуправлений', 'употреблений', 'прохождений',
             'обновлений', 'внесений', 'здравоохранений', 'наслаждений', 'освещений', 'применений', 'накоплений',
             'становлений', 'прекращений', 'раздражений', 'приключений', 'развлечений', 'совпадений', 'преодолений',
             'владений', 'увлечений', 'сидений', 'представлений', 'опасений', 'превращений', 'украшений', 'воплощений',
             'терпений', 'поручений', 'выявлений', 'нападений', 'столкновений', 'облегчений', 'приложений', 'сожалений',
             'рассуждений', 'недоумений', 'продвижений', 'потреблений', 'подозрений', 'видений', 'строений',
             'включений', 'посещений', 'разделений', 'дополнений', 'проведений', 'уменьшений', 'освоений',
             'предупреждений', 'гений', 'размещений', 'воображений', 'учений', 'уничтожений', 'волнений', 'размышлений',
             'наступлений', 'сравнений', 'возрождений', 'выделений', 'измерений', 'разрушений', 'усилений',
             'приглашений', 'предположений', 'вооружений', 'вступлений', 'объявлений', 'предоставлений', 'предложений',
             'убеждений', 'изготовлений', 'мгновений', 'освобождений', 'сооружений', 'соединений', 'внедрений',
             'поступлений', 'сочинений', 'окружений', 'лечений', 'зрений', 'решений', 'привлечений', 'растений',
             'хранений', 'обвинений', 'соблюдений', 'установлений', 'сопротивлений', 'правлений', 'удовлетворений',
             'подтверждений', 'воскресений', 'населений', 'отношений']


    choices_rifms = random.choices(rifms, k=1)

    if 'Арсений' == message.text:
        await message.reply(str(choices_rifms)[2:][:-2])

    ### ГИБЛОЕ ДЕЛО ###
    if " дела" in text or "дело" in text:
        await bot.send_voice(chatId, open("sounds/1.mp3", 'rb'))

    ### ФАЕР ОЧЕНЬ ЛЮБИТ МЕТАЛ ###
    if 'метал' in text or 'песня' in text or 'музыка' in text:
        await bot.send_voice(chatId, open("sounds/любит метал.ogg", 'rb'))

    ### КОНЕЧНО ТЫ ЭТОГО НЕ ДЕЛАЛ ###
    if "делал" in text or "геноцид" in text or "резня" in text:
        await bot.send_voice(chatId, open("sounds/конечно ты этого не делал.ogg", 'rb'))

    ### КОНТЕНТ ###
    if "контент" in text:
        await bot.send_voice(chatId, open("sounds/дада мы тебя поняли конттент.ogg", 'rb'))

    ### МЛАДЕНЕЦ ###
    if "младенец" in text or 'ребеночек' in text or 'мальчик' in text or 'ребёночек' in text or 'слыш' in text:
        await bot.send_voice(chatId, open("sounds/может быть кто то младенец.ogg", 'rb'))

    ### НАЧАЛ И ЧЕ ###
    if "зачем ты" in text or "арсений зачем" in text or "зачем арсени" in text or "начинать" in text:
        await bot.send_voice(chatId, open("sounds/НУ НАЧАО И ЧЕ.ogg", 'rb'))

    ### ТЫ ТАКОЙ ОРИГИНАЛЬНЫЙ ###
    if "арсений ты лох" in text or "арсений ты чмо" in text or "твоя мам" in text or "жирная мамаша" in text in text or "оригинал" in text:
        await bot.send_voice(chatId, open("sounds/ой фаер ты такой оригинальный.ogg", 'rb'))

    ### ПОДДЕРЖИВАЮ ###
    if "войн" in text or 'спецоперац' in text:
        await bot.send_voice(chatId, open("sounds/ПОДДЕРЖИВАЮ.ogg", 'rb'))

    ### ПРОСТО ГЕНИЙ ###
    if "гений" in text or "гей" in text or "тимофе" in text or "200 iq" in text in text or "300 iq" in text:
        await bot.send_voice(chatId, open("sounds/ПРОСТО ГЕНИЙ.ogg", 'rb'))

    ### СВОИ ЛЮБИМЫЕ ПЕСНИ ###
    if 'метал' in text or 'песня' in text or 'музыка' in text or 'гиперпоп' in text or 'рок' in text:
        await bot.send_voice(chatId, open("sounds/СВОИ ЛЮБИМЫЕ ПЕСНИ.ogg", 'rb'))

    ### ТАК МЫ ТЕБЕ И ПОВЕРИЛИ ###
    if 'купил' in text or 'честно' in text or 'у меня есть' in text or 'это не я' in text:
        await bot.send_voice(chatId, open("sounds/так м ытебе и поверили.ogg", 'rb'))

    ### ЧЕ ТО ПРО ДЕВУШЕК ###
    if 'девушк' in text or 'девоч' in text or 'бронислава' in text or 'тяночк' in text:
        await bot.send_voice(chatId, open("sounds/че то про девушек.ogg", 'rb'))

    ### НЕ ПИСАЛ ###
    if 'какал' in text or 'какает' in text or 'писает' in text or 'писал' in text or 'писать' in text or 'какать' in text:
        await bot.send_voice(chatId, open("sounds/я там не писал.ogg", 'rb'))

    ### ФАЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕР ###
    if 'фаер' in text or 'леха' in text or 'леша' in text or 'fireholdest' in text:
        vrs = ['sounds/ФАЕР Я КОНЕЧНО ВСЕ ПОНИМАЮ.ogg', 'sounds/фаер какой же ты глупый.ogg', 'sounds/ты меня уже достал.ogg']
        choices = random.choices(vrs, k=1)
        await bot.send_voice(chatId, open(str(choices)[2:][:-2], 'rb'))


    ### IPHONE SEX ###
    if 'iphone sex' == text:
        await bot.send_voice(chatId, open("sounds/iphnsx.mp3", 'rb'))


    ### l488 ###
    if 'zxc' == text:
        await bot.send_sticker(chatId, sticker=r"CAACAgIAAxkBAAEFVOJi2RaH4kYOqZjM2NEk24R51MKqogACsR0AAo0HAAFKrK88ZFAkBBwpBA")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
