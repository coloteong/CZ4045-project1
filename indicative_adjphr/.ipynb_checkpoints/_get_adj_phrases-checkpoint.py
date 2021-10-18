#%%
import spacy
from collections import Counter
from nltk.tokenize import sent_tokenize
from spacy import displacy

nlp = spacy.load("en_core_web_sm")


def get_adjective_phrases(text) -> list:
	def get_to_object(token) -> int:
		for child in token.children:
			if (child.pos_ in ['NOUN', 'PRON', 'PROPN']) and (child.dep_ == 'pobj'):
				subtoken = list(child.children)
				subtoken = [token for token in subtoken if token.dep_ == 'prep']
				if subtoken:
					return get_to_object(subtoken[0])
				else:
					return get_to_object(child)

	doc = nlp(text)
	phrases = []
	for token in doc:
		phrase = ''
		"""
        An adjective has the POS - ADJ and it can be the root word in a sentence (rare),
        it is more often in the form of `acomp` or `amod`, we immediately add this to our phrase
        since this is the main constituent of the adjective phrase
        """
		if (token.pos_ == 'ADJ') and (token.dep_ in ['ROOT', 'acomp', 'amod']):
			phrase += token.text
			adjective_position = token.i
			for subtoken in token.children:
				# first rule: if there is an adverb that modifies the adjective
				# we add it to the phrase in front of the adjective
				if (subtoken.pos_ == 'ADV') and (subtoken.dep_ == 'advmod'):
					phrase = subtoken.text + ' ' + phrase
				# second rule: if there is a preposition - indicating that
				# there is an object that gives us more info about the prep
				# we add all tokens up until the noun
				if (subtoken.pos_ in ['ADP', 'SCONJ']) and (subtoken.dep_ == 'prep'):
					try:
						noun_position = get_to_object(subtoken)
						for i in range(adjective_position + 1, noun_position + 1):
							phrase += ' ' + doc[i].text
					except TypeError:
						pass
		# need to fix so that it does not get random adverbs and adjectives
		elif (token.pos_ == 'AUX') and (token.dep_ == 'ROOT'):
		# elif (token.pos_ == 'AUX'):
			adv = adj =  None
			for subtoken in token.children:
				if subtoken.dep_ == 'advmod':
					if adv == None:
						adv = subtoken
					else:
				if subtoken.dep_ == 'acomp':
					if adj == None:
						adj = subtoken
					else:
				if adv != None and adj != None:
					if adv.i +1 == adj.i:
						phrase += adv.text + " " + adj.text + " "
		# since it is a phrase, it needs to have more than one word
		# i.e. a lone adjective does not constitute an adjective phrase
		if len(phrase.split()) > 1:
			phrases.append(phrase)
	return phrases


def get_list_of_phrases(text: str):
	reviews = [sent_tokenize(text)]
	reviews = [item for sublist in reviews for item in sublist]
	phrases = [get_adjective_phrases(text.lower())]
	phrases = [array for array in phrases if len(array) > 0]
	phrases = [text for sublist in phrases for text in sublist]
	phrase_counts = Counter(phrases)
	return phrase_counts


if __name__ == '__main__':
	phrases = get_adjective_phrases(
		"I guess it's classified as fast food since the whole process is similar to what you'd experience at subway but the taste is far beyond your typical tofu wrap.")

	print(f"adjective phrases found: {phrases}")