def archiver(text: str, root_dictionary: dict) -> str:
    # Проходим по каждой паре корень-идентификатор в словаре корней
    for root, key in root_dictionary.items():
        # Заменяем все соответствия корня в тексте на соответствующий идентификатор
        text = text.replace(root, f"${key}")
    # Возвращаем архивированный текст
    return text

def unpacker(text: str, root_dictionary: dict) -> str:
    # Проходим по каждой паре корень-идентификатор в словаре корней
    for root, key in root_dictionary.items():
        # Ищем начало идентификатора в тексте и заменяем его на нужный корень
        text = text.replace(f"${key}", root)
    # Возвращаем распакованный текст
    return text

# Словарь
russ_dictionary = {
    "дела": "$a",
    "говор": "$б",
    "работа": "$в",
    "жизненн": "$г",
    "челове": "$д",
    "место": "$е",
    "врем": "$ё",
    "денеж": "$ж",
    "недел": "$з",
    "годн": "$и",
    "хорош": "$й",
    "больш": "$к",
    "маленьк": "$л",
    "готов": "$м",
    "сказа": "$н",
    "котор": "$о",
    "смотр": "$п",
    "пере": "$р",
    "земл": "$с",
    "скор": "$т",
    "крас": "$у",
    "важн": "$ф",
    "знам": "$х",
    "жизн": "$ц",
    "слова": "$ч",
    "добав": "$ш"
}

# Ввод текста для сжатия
text_to_compress = input("Текст для сжатия: ")
compressed_text = archiver(text_to_compress, russ_dictionary)
print("Сжатый текст:", compressed_text)

# Ввод сжатого текста для распаковки
compressed_text_to_unpack = input("Сжатый текст для распаковки: ")
unpacked_text = unpacker(compressed_text_to_unpack, russ_dictionary)
print("Распакованный текст:", unpacked_text)
