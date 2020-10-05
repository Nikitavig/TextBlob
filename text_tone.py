from textblob import TextBlob
from googletrans import Translator

# import googletrans
# print(googletrans.LANGUAGES)

def transtute_text(text):
	"""
		Функция для перевод текста на английский язык
		Args:
			text(str): строка для перевода
		Return:
			translation(str): переведенный текст 
	"""

	translator = Translator()
	translation = translator.translate(text, dest ="en")

	return translation.text


def analis_text(text):
	"""
		Функция для перевод текста на английский язык
		Args:
			text(str): строка для оценки
		Return:
			polarity(str): полятрность текста
			subjectivity(str): субъективность 
	"""

	analysis = TextBlob(text)
	polarity = analysis.sentiment.polarity
	subjectivity = analysis.sentiment.subjectivity

	return polarity, subjectivity


def main():
	while True:
		try:
			# Вводим текст
			text = input("Введите текст: ")
			# Переводим его и отправляем на оценку
			polarity, subjectivity = analis_text(transtute_text(text))
			# Вывод результатов оценки 
			print(f">>> Полярность:{polarity} || Субъективность: {subjectivity}")
		except Exception as e:
			print(f"Exception: {e}")

if __name__ == '__main__':
	# print(transtute_text('Это хорошая новость'))
	main()