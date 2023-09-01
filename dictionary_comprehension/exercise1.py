sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

sentence_words = sentence.split()
result = {word: len(word) for word in sentence_words}

print(result)

