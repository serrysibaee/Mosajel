from dataset import *

loader = Loader()
dataset = loader.loads()
chars = "إأبتثجحخدذرزسشصضطظعغفقكلمنهويا"

for char in chars:
    for i in range(5):
        print(loader.take_sample(dataset, char))
