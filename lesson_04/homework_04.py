import re

# Початкові дані (оригінальний текст)
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3

# task 01 ==
# дані у строці розбиті випадковим чином через помилку.
# треба замінити кінець абзацу/рядка на пробіл: .replace("\n", " ")
# рішення:
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
# Умова: Замініть підрядок "...." на пробіл.
# Рішення:
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03 ==
# Умова: Зробіть так, щоб у тексті було не більше одного пробілу між словами.
# Рішення (нормалізуємо будь-які послідовності пропусків до одного):
adwentures_of_tom_sawer = re.sub(r"\s+", " ", adwentures_of_tom_sawer).strip()

# (необов’язково) Показати результат 1–3 для перевірки
print("Після task 01–03:", adwentures_of_tom_sawer, "\n")

# task 04
# Умова: Виведіть, скількі разів у тексті зустрічається літера "h".
# Рішення: рахуємо без врахування регістру (lower()).
h_count = adwentures_of_tom_sawer.lower().count("h")
print("task 04 (кількість 'h'):", h_count)

# task 05
# Умова: Виведіть, скільки слів у тексті починається з Великої літери?
# Рішення: виділяємо слова та рахуємо ті, що починаються з великої (A–Z).
words = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", adwentures_of_tom_sawer)
cap_count = sum(w[0].isupper() for w in words)
print("task 05 (слів із Великої літери):", cap_count)

# task 06
# Умова: Виведіть позицію, на якій слово Tom зустрічається вдруге.
# Рішення: шукаємо індекс другої появи через find з офсетом.
first = adwentures_of_tom_sawer.find("Tom")
second = adwentures_of_tom_sawer.find("Tom", first + 1) if first != -1 else -1
print("task 06 (позиція другої появи 'Tom'):", second)

# task 07
# Умова: Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
# Збережіть результат у змінній adwentures_of_tom_sawer_sentences.
# Рішення: ділимо після ., ! або ? і пропускаємо пробіли після розділового знака.
adwentures_of_tom_sawer_sentences = re.split(r'(?<=[.!?])\s+', adwentures_of_tom_sawer)
print("task 07 (кількість речень):", len(adwentures_of_tom_sawer_sentences))

# task 08
# Умова: Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
# Перетворіть рядок у нижній регістр.
# Рішення:
if len(adwentures_of_tom_sawer_sentences) >= 4:
    fourth_sentence_lower = adwentures_of_tom_sawer_sentences[3].lower()
    print("task 08 (4-те речення, lower):", fourth_sentence_lower)
else:
    print("task 08: у тексті менше ніж 4 речення")

# task 09
# Умова: Перевірте чи починається якесь речення з "By the time".
# Рішення:
starts_with_phrase = any(s.startswith("By the time") for s in adwentures_of_tom_sawer_sentences)
print("task 09 (є речення, що починається з 'By the time'):", starts_with_phrase)

# task 10
# Умова: Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
# Рішення:
if adwentures_of_tom_sawer_sentences:
    last_sentence = adwentures_of_tom_sawer_sentences[-1]
    last_words = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", last_sentence)
    print("task 10 (кількість слів в останньому реченні):", len(last_words))
else:
    print("task 10: немає речень")

