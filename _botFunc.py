from __future__ import print_function
import time
import random
import markovify
import io


def _getAllWordswithoutMarks(inMessagefromVK):
	""" Функция которая берет массив из слов и преобразует в массив из слов без запятых, знаков и т.д.
	"""
	arrayBeforeCorrectingWord = []
	receivedMessage = inMessagefromVK
	""" Функция берет входящие сообщение, если в них есть знаки, убирает и возвращает в массив. Если нет, просто возвращает в массив.
	"""
	def _letremoveSign(someMassive, someInput):
		for eachWordmark in someInput:
			if "?)" in eachWordmark:
				questionandBracketMark = eachWordmark.replace("?)", "")
				someMassive.append(questionandBracketMark)
			elif "?(" in eachWordmark:
				questionandbackBracketMark = eachWordmark.replace("?(", "")
				someMassive.append(questionandbackBracketMark)
			elif "?" in eachWordmark:
				QuestionMark = eachWordmark.replace("?", "")
				someMassive.append(QuestionMark)
			elif "." in eachWordmark:	
				DatMark = eachWordmark.replace(".", "")
				someMassive.append(DatMark)
			elif "!" in eachWordmark:
				exclamationMark = eachWordmark.replace("!", "")
				someMassive.append(exclamationMark)
			elif ")" in eachWordmark:
				bracketMark = eachWordmark.replace(")", "")
				someMassive.append(bracketMark)
			elif "(" in eachWordmark:
				backbracketMark = eachWordmark.replace("(", "")
				someMassive.append(backbracketMark)
			elif "," in eachWordmark:
				commaMark = eachWordmark.replace(",", "")
				someMassive.append(commaMark)
			else:
				someMassive.append(eachWordmark)		
		return someMassive
	### Здесь очищеные сообщения от знаков.
	arrayCorrectingWord = _letremoveSign(arrayBeforeCorrectingWord, receivedMessage)

	return arrayCorrectingWord


def _letmakeHelltext(firstfilename, secondfilename):
	""" Функция возвращает одно сгенерированное предложение из двух файлов текста.
	"""
	with open(firstfilename, encoding="utf-8") as f:
		firstText = f.read()
	with open(secondfilename, encoding="utf-8") as s:
		secondText = s.read()
	model_a = markovify.Text(firstText, well_formed=False)
	model_b = markovify.Text(secondText, well_formed=False)
	model_combo = markovify.combine([ model_a, model_b ], [1.5, 1])

	return model_combo.make_short_sentence(140)


def _getAllgenSentences():
	""" Функция возвращает сгенерированные предложения.
	"""
	gentexList = []
	gentexSourceList = []
	startTime = time.time()
	while True:
		genText = str(_letmakeHelltext("book_text.txt", "tumblr_text.txt"))
		gentexSourceList.append(genText)
		if time.time() - startTime > 20:
			break
	for everElement in gentexSourceList:
		if everElement == "None":
			gentexSourceList.remove(everElement)
	for everSourceElement in gentexSourceList:
		lowerElement = everSourceElement.lower()
		gentexList.append(lowerElement)

	return gentexList


def _letCapitalletter(resultSentence):
	""" Функиция берет предложение с маленькой буквой, и возвращает с большой.
	"""
	firstMarkofWord = resultSentence[:1]
	letUppercaseMark = firstMarkofWord.upper()
	withoutFirstLetter = resultSentence[1:]
	resultFunc = letUppercaseMark + withoutFirstLetter

	return resultFunc


def main(mess):
	""" Функция валидации на поиск слов из входного сообщения, в модуле генерации.
	"""
	validator = []
	resultAllWordswithoutMarks = _getAllWordswithoutMarks(mess)
	for everyMarkword in resultAllWordswithoutMarks:
		if everyMarkword == 'ты':
			resultAllWordswithoutMarks.remove('ты')
			resultAllWordswithoutMarks.insert(0, 'я')
		elif everyMarkword == 'я':
			resultAllWordswithoutMarks.remove('я')
			resultAllWordswithoutMarks.insert(0, 'ты')
	arraySyllablegenex = ['это', 'еще', 'как', 'бы', 'да', 'где', 'не', 'че', 'в', 'с', 'к', 'а', 'и', 'от']
	for everyMarkword in arraySyllablegenex:
		if everyMarkword in resultAllWordswithoutMarks:
			resultAllWordswithoutMarks.remove(everyMarkword)

	resultAllgenSentences = _getAllgenSentences()
	def _getBreaksentencesIntoWords(anySentences):
		""" Функция возвращает слова из предложений.
		""" 
		eachwordGentexList = []
		for eachword in anySentences:
			offersList = eachword.split()
			for eachwordOffers in offersList:
				eachwordGentexList.append(eachwordOffers)
		return eachwordGentexList

	resultBreaksentencesIntoWords = _getBreaksentencesIntoWords(resultAllgenSentences)
	for everyWord in range(len(resultBreaksentencesIntoWords)):
		printOutword = resultBreaksentencesIntoWords[everyWord]
		entryAmount = sum(printOutword.count(evWord) for evWord in resultAllWordswithoutMarks)
		validator.append(entryAmount)
		_resultValidate = sum(validator)

	if _resultValidate > 0:

		max_index = 0
		max_number = sum(resultAllgenSentences[0].count(oneWord) for oneWord in resultAllWordswithoutMarks)
		max_index_dubles = []
		for i in range(1, len(resultAllgenSentences)):
			text = resultAllgenSentences[i]
			number = sum(text.count(word) for word in resultAllWordswithoutMarks)
			if number > max_number:
				max_number = number
				max_index = i
			elif number == max_number:
				max_index_dubles.append(i)
		listCapitalletter = []
		for eachDubles in max_index_dubles:
			max_number_dubles = sum(resultAllgenSentences[eachDubles].count(word) for word in resultAllWordswithoutMarks)
			if max_number_dubles == max_number: 
				resultDubSentence = resultAllgenSentences[eachDubles]
				withaCapletter = _letCapitalletter(resultDubSentence)
				listCapitalletter.append(withaCapletter)
		resultMaxSentence = resultAllgenSentences[max_index]
		return _letCapitalletter(resultMaxSentence) + ' ' + ' '.join(listCapitalletter)

	else:
		arraytextPure = []
		arraySyllable = ['это', 'еще', 'как', 'бы', 'да', 'где', 'не', 'че', 'в', 'с', 'к', 'а', 'и', 'от']
		for everyMarkword in arraySyllable:
			if everyMarkword in resultAllWordswithoutMarks:
				resultAllWordswithoutMarks.remove(everyMarkword)

		with io.open('allText.txt', encoding='utf-8') as file:
			for lineSentence in file:
				lowerlineSentence = lineSentence.lower()
				for everyWordkey in resultAllWordswithoutMarks:
					if everyWordkey in lowerlineSentence:
						arraytextPure.append(lowerlineSentence)
		if not arraytextPure:
			anyGenx = random.choice(resultAllgenSentences)
			return "Вот что я тебе скажу, мой друг... " + _letCapitalletter(anyGenx) # Здесь ошибка - NameError: name '_letCapitalletter' is not defined
		else:
			randomizer = random.choice(arraytextPure)
			return _letCapitalletter(randomizer)


def _letAcceptmessageVK(vkmess):
	""" Функция вызывает и возвращает, резлельтат основной функции, атрибутом функции  - сообщение из ВК.
	"""
	incommingMessage = vkmess
	return main(incommingMessage)