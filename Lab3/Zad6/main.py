def toUpper(func):
    def wrapper(sentence):
        sentence = sentence.upper()
        func(sentence)
    return wrapper

@toUpper
def say_smth(smth):
    print(smth)


say_smth("is it working?")