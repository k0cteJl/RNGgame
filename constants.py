TOKEN = '8112259004:AAG-H854Mhy1G4j0KMrI_mJIlY4wMaqs-2Y'

DROP_LIST = {
    2: ["Новичок", "Искатель", "Путник", "Странник", "Ученик", "Наблюдатель", "Мечтатель", "Испытатель"],
    4: ["Отважный", "Смельчак", "Искатель приключений", "Хранитель", "Защитник", "Следопыт", "Мастер клинка", "Ловкач"],
    5: ["Правитель", "Мастер Стихий", "Легенда", "Владыка", "Непобедимый Воин"],
    8: ["Хранитель Времени", "Повелитель Огня", "Светоч Мудрости", "Лорд Теней", "Странник Миров"],
    10: ["Искатель Истины", "Защитник Слабости", "Мастер Загадок", "Хранитель Лесов", "Покоритель Гор"],
    20: ["Странник Пустыни", "Ловец Удачи", "Хранитель Секретов", "Мастер Ремесел", "Путник Дорог"],
    30: ["Собиратель Звезд", "Хранитель Снов", "Искатель Приключений", "Мастер Тайн", "Покоритель Ветров"],
    50: ["🌟 Мечтатель Звезд", "🌊 Властелин Волн", "🔥 Хранитель Пламени", "🌿 Садовник Вечности", "⚔️ Воин Света"],
    80: ["🌙 Лунный Странник", "🌀 Мастер Вихрей", "🌌 Искатель Галактик", "🌪️ Повелитель Бурь", "🛡️ Защитник Рассвета"],
    100: ["🌠 Созвездный Путник", "🌳 Хранитель Древа", "⚡ Молния Судьбы", "🌅 Страж Заката", "🌕 Лунный Рыцарь"],
    125: ["🌌 Путник Туманностей", "🌋 Владыка Лавы", "🌾 Жнец Ветров", "🌠 Звездный Скиталец", "🦅 Орел Небес"],
    190: ["🌑 Тень Вечности", "🌠 Созвездный Мудрец", "🌪️ Вихрь Перемен", "🌊 Прилив Судьбы", "🔥 Пламя Бессмертия"],
    230: ["🌌 Странник Галактик 🌠", "🔥 Владыка Огня ❄️", "⚔️ Рыцарь Вечности 🛡️", "🌿 Хранитель Лесов 🍃", "🌀 Мастер Вихрей 🌪️"],
    300: ["🌙 Лунный Воин 🌕", "🌟 Звездный Скиталец 🌠", "🌪️ Повелитель Бурь 🌊", "🌅 Страж Рассвета 🌄", "🌳 Древо Жизни 🌱"],
    450: ["🌠 Искатель Туманностей 🌌", "🔥 Пламя Судьбы ❄️", "⚡ Молния Вечности 🌩️", "🌊 Прилив Силы 🌋", "🌑 Тень Бессмертия 🌒"],
    555: ["🌌 Путник Вселенной 🌠", "🌋 Владыка Лавы 🔥", "🌾 Жнец Ветров 🌪️", "🌠 Звездный Мудрец 🌟", "🦅 Орел Небес 🌤️"],
    700: ["🌑 Тьма Вечности 🌕", "🌠 Созвездный Странник 🌌", "🌪️ Вихрь Судьбы 🌊", "🌊 Волна Перемен 🌋", "🔥 Вечное Пламя ❄️"],
    42: ["🤡 Познавший Жизнь", "🏆 Сслуга Пятёрки", "💩 Туча Зелёных Какашек 💩", "🦑 Любитель Земных Осьминогов 🐙", "🦋 Спонсор Скибиди Бабочек 🦋", "🍕 Покровитель Летающих Пицц 🍕", "🦄 Властелин Радужных Единорогов 🌈"],
    52: ["🍔 Мастер Плавающих Бургеров 🍟", "🐸 Лорд Танцующих Лягушек 🕺", "🦆 Повелитель Уток-Ниндзя 🥷", "🍩 Хранитель Космических Пончиков 🚀", "🦍 Создатель Бегающих Бананов 🍌"],
    69: ["🍆 Король Фиолетовых Баклажанов 🍑", "🦄 Мемный Единорог Вселенной 🌌", "🐒 Мастер Обезьяньих Шуток 🍌", "🦖 Диктатор Динозавров-Мемов 🦕", "🍕 Лорд Пиццы с Ананасами 🍍"],
    228: ["🦀 Краб-Разрушитель Миров 🦀", "🐧� Сырный Магнат Вселенной 🧀", "🦆 Утка-Покоритель Галактик 🪐", "🍫 Шоколадный Тиран 🍫", "🦖 Динозавр-Мемолог 🦕"],
    666: ["👹 Демон Мемов и Печенек 🍪", "🔥 Властелин Огненных Лягушек 🐸", "🦑 Осьминог-Разрушитель Реальности 🌀", "🍕 Пицца-Сатана 🍕", "🦄 Единорог Апокалипсиса 🌈"],
    777: ["🍀 Счастливчик Мемов 🍀", "🦄 Единорог Удачи и Бананов 🍌", "🍕 Пицца-Мессия 🍕", "🦆 Утка-Спаситель Вселенной 🪐", "🦖 Динозавр-Мемный Пророк 🦕"],
    1000: ["🌌🌠 Странник Вечных Галактик 🌠🌌", "🔥🌋 Владыка Огня и Лавы 🌋🔥", "⚔️🛡️ Рыцарь Тысячи Сражений 🛡️⚔️", "🌿🍃 Хранитель Древних Лесов �🌿", "🌀🌪️ Мастер Вихрей и Бурь 🌪️🌀"],
    1500: ["🌙🌕 Лунный Воин Вечности 🌕🌙", "🌟🌠 Звездный Скиталец Вселенной 🌠🌟", "🌪️🌊 Повелитель Бурь и Океанов 🌊🌪️", "🌅🌄 Страж Рассвета и Заката 🌄🌅", "🌳🌱 Древо Жизни и Смерти 🌱🌳"],
    2000: ["🌌🌠 Искатель Глубин Космоса 🌠🌌", "🔥❄️ Властелин Огня и Льда ❄️🔥", "⚡🌩️ Молния Вечности и Судьбы 🌩️⚡", "🌊🌋 Прилив Силы и Вулканов 🌋🌊", "🌑🌒 Тень Бессмертия и Вечности 🌒🌑"],
    2500: ["🌌🌠 Путник Бескрайних Туманностей 🌠🌌", "🌋🔥 Владыка Лавы и Пепла 🔥🌋", "🌾🌪️ Жнец Ветров и Ураганов 🌪️🌾", "🌠🌟 Звездный Мудрец и Пророк 🌟🌠", "🦅🌤️ Орел Небес и Гроз 🌤️🦅"],
    3000: ["🌑🌕 Тьма и Свет Вечности 🌕🌑", "🌌🌠 Созвездный Странник и Хранитель 🌠🌌", "🌪️🌊 Вихрь Судьбы и Перемен 🌊🌪️", "🌋🌊 Волна Огня и Воды 🌊🌋", "🔥❄️ Вечное Пламя и Лед ❄️🔥"],
    5000: ["🌌🌠🌟 Странник Вечных Галактик и Звезд 🌟🌠🌌", "🔥🌋🌄 Владыка Огня, Лавы и Рассветов 🌄🌋🔥", "⚔️🛡️🌅 Рыцарь Тысячи Сражений и Закатов 🌅🛡️⚔️", "🌿🍃🌳 Хранитель Древних Лесов и Деревьев 🌳🍃🌿", "🌀🌪️🌊 Мастер Вихрей, Бурь и Океанов 🌊🌪️🌀"],
    7500: ["🌙🌕🌌 Лунный Воин Вечности и Космоса 🌌🌕🌙", "🌟🌠🌅 Звездный Скиталец Вселенной и Рассветов 🌅🌠🌟", "🌪️🌊🌋 Повелитель Бурь, Океанов и Вулканов 🌋🌊🌪️", "🌅🌄🌑 Страж Рассвета, Заката и Тьмы 🌑🌄🌅", "🌳🌱🌿 Древо Жизни, Смерти и Возрождения 🌿🌱🌳"],
    10000: ["🌌🌠🌟 Искатель Глубин Космоса и Звездных Тайн 🌟🌠🌌", "🔥❄️🌋 Властелин Огня, Льда и Лавы 🌋❄️🔥", "⚡🌩️🌅 Молния Вечности, Судьбы и Рассветов 🌅🌩️⚡", "🌊🌋🌌 Прилив Силы, Вулканов и Галактик 🌌🌋🌊", "🌑🌒🌕 Тень Бессмертия, Вечности и Луны 🌕🌒🌑"],
    25000: ["🌌🌠🌟 Путник Бескрайних Туманностей и Звездных Путей 🌟🌠🌌", "🌋🔥🌄 Владыка Лавы, Пепла и Рассветов 🌄🔥🌋", "🌾🌪️🌊 Жнец Ветров, Ураганов и Океанов 🌊🌪️🌾", "🌠🌟🌌 Звездный Мудрец, Пророк и Странник 🌌🌟🌠", "🦅🌤️🌅 Орел Небес, Гроз и Рассветов 🌅🌤️🦅"],
    50000: ["🌑🌕🌌 Тьма, Свет и Вечность Космоса 🌌🌕🌑", "🌌🌠🌟 Созвездный Странник, Хранитель и Мудрец 🌟🌠🌌", "🌪️🌊🌋 Вихрь Судьбы, Перемен и Вулканов 🌋🌊🌪️", "🌋🌊🌌 Волна Огня, Воды и Галактик 🌌🌊🌋", "🔥❄️🌅 Вечное Пламя, Лед и Рассветы 🌅❄️🔥"],
    75000: ["🌌🌠🌟🌑 Странник Вечных Галактик, Звезд и Тьмы 🌑🌟🌠🌌", "🔥🌋🌄🌅 Владыка Огня, Лавы, Рассветов и Закатов 🌅🌄🌋🔥", "⚔️🛡️🌅🌌 Рыцарь Тысячи Сражений, Закатов и Космоса 🌌🌅🛡️⚔️", "🌿🍃🌳🌱 Хранитель Древних Лесов, Деревьев и Жизни 🌱🌳🍃🌿", "🌀🌪️🌊🌋 Мастер Вихрей, Бурь, Океанов и Вулканов 🌋🌊🌪️🌀"],
    100000: ["🌙🌕🌌🌠 Лунный Воин Вечности, Космоса и Звезд 🌠🌌🌕🌙", "🌟🌠🌅🌄 Звездный Скиталец Вселенной, Рассветов и Закатов 🌄🌅🌠🌟", "🌪️🌊🌋🔥 Повелитель Бурь, Океанов, Вулканов и Огня 🔥🌋🌊🌪️", "🌅🌄🌑🌌 Страж Рассвета, Заката, Тьмы и Галактик 🌌🌑🌄🌅", "🌳🌱🌿🌾 Древо Жизни, Смерти, Возрождения и Ветров 🌾🌿🌱🌳"],
    150000: ["🌌🌠🌟🌑 Искатель Глубин Космоса, Звездных Тайн и Тьмы 🌑🌟🌠🌌", "🔥❄️🌋🌄 Властелин Огня, Льда, Лавы и Рассветов 🌄🌋❄️🔥", "⚡🌩️🌅🌌 Молния Вечности, Судьбы, Рассветов и Галактик 🌌🌅🌩️⚡", "🌊🌋🌌🌠 Прилив Силы, Вулканов, Галактик и Звезд 🌠🌌🌋🌊", "🌑🌒🌕🌌 Тень Бессмертия, Вечности, Луны и Космоса 🌌🌕🌒🌑"],
    500000: ["🌌🌠🌟🌑 Путник Бескрайних Туманностей, Звездных Путей и Тьмы 🌑🌟🌠🌌", "🌋🔥🌄🌅 Владыка Лавы, Пепла, Рассветов и Закатов 🌅🌄🔥🌋", "🌾🌪️🌊🌌 Жнец Ветров, Ураганов, Океанов и Галактик 🌌🌊🌪️🌾", "🌠🌟🌌🌑 Звездный Мудрец, Пророк, Странник и Тьмы 🌑🌌🌟🌠", "🦅🌤️🌅🌌 Орел Небес, Гроз, Рассветов и Космоса 🌌🌅🌤️🦅"],
    1000000: ["🌑🌕🌌🌠 Тьма, Свет, Вечность Космоса и Звезд 🌠🌌🌕🌑", "🌌🌠🌟🌑 Созвездный Странник, Хранитель, Мудрец и Тьма 🌑🌟🌠🌌", "🌪️🌊🌋🔥 Вихрь Судьбы, Перемен, Вулканов и Огня 🔥🌋🌊🌪️", "🌋🌊🌌🌠 Волна Огня, Воды, Галактик и Звезд 🌠🌌🌊🌋", "🔥❄️🌅🌌 Вечное Пламя, Лед, Рассветы и Космос 🌌🌅❄️🔥"],
    2000000: ["🚽 Скибиди Толчок 🚽"]
}