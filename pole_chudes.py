import random

wordsList = ["вопрос", "система", "год", "человек", "время", "дело", "жизнь", "день", "слово"]

# даем пользователю выбор, задать слово самостоятельно или получить случайное слово из заготовленного списка
choice = input("Хотите самостоятельно загадать слово? Введите да/нет: ")
if  choice == "да" or choice == "lf":
    wordMain = input()
    wordsList.append(wordMain) # хотелось бы сделать так, чтобы с каждой новой игрой список слов пополнялся. pass :) Вероятно, нужно брать слово из файла и туда же добавлять пользовательское слово
elif choice == "нет" or choice == "ytn":
    wordMain = random.choice(wordsList) # изначально планировал использовать randint с диапазоном длины wordsList для взятия слова по индексу, но нашел метод получше
else:
    print("Вы не справились даже с такой задачей! Вероятно, эта игра не для слабых умов... Game over.")

word = list(wordMain)
wordMask = ["*"] * len(wordMain) # создаем поле для игры
print(f'Загаданное слово: {wordMask}. У Вас есть 5 попыток, чтобы его угадать. Удачи!')

tries = 5
while tries > 0 and "*" in wordMask:
    letter = input("Введите букву или все слово целиком: ")
    if letter == wordMain: # слово назвали сразу
        tries = 0
        print(f'Блестяще! Ты угадал слово "{wordMain}"! Пятьдесят очков Гриффиндору!')
    elif letter not in word:  # неверная буква
        tries -= 1
        print(f"Не угадал! Осталось попыток: {tries}. Слово: {wordMask}")
    elif letter in wordMask:
        tries -= 1
        print(f"Такая буква уже была. Минус попытка;) Осталось попыток: {tries}. Слово: {wordMask}")
    else:
        for i in range(len(word)):
            if letter == word[i]:
                wordMask[i] = word[i]
        print("Угадал! 10 очков Гриффиндору!")
        print(f'Загаданное слово: {wordMask}. Попыток осталось: {tries}. Удачи!')        

if wordMask == word:
    print(f'Поздравляю, ты победил!')
else:
    print(f"Ты проиграл. Загаданное слово: {wordMain}")

