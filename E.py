import string

from F import timing_decorator


class MyTextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.warning = f'_____________________Далее идет текст и результаты задач E и F______________________________'


    @timing_decorator
    def get_longest_word(self):
        words = self.text.split()
        longest_word = max(words, key=len)
        return longest_word

    @timing_decorator
    def get_most_common_word(self):
        words = self.text.split()
        word_counts = {}
        punctuation = string.punctuation

        for word in words:
            word = word.strip(punctuation)
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        most_common_word = max(word_counts, key=word_counts.get)
        return most_common_word

    @timing_decorator
    def get_special_character_count(self):
        special_characters = ['.', ',', '!', '?', ';', ':']
        count = 0

        for char in self.text:
            if char in special_characters:
                count += 1

        return count

    @timing_decorator
    def get_palindromes(self):
        words = self.text.split()
        palindromes = []

        for word in words:
            if word.lower() == word.lower()[::-1]:
                palindromes.append(word)

        return ', '.join(palindromes)



analyzer = MyTextAnalyzer('Добрый день. Это тестовое для в@шей компании и это очень оригинальный текст в этот день!')
print(analyzer.warning, f'Текст: {analyzer.text}', sep='\n')

longest_word = analyzer.get_longest_word()
print("Самое длинное слово:", longest_word)

most_common_word = analyzer.get_most_common_word()
print("Самое популярное слово:", most_common_word)

special_character_count = analyzer.get_special_character_count()
print("Количество уникальных символов:", special_character_count)

palindromes = analyzer.get_palindromes()
print("Палиндромы:", palindromes)
