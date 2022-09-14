class Dictionary:
    rus = "Питон"
    eng = "Python"


try:
    print(getattr(Dictionary, "rus_word"))
except AttributeError:
    print(False)
