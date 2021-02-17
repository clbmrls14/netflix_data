from fastapi import FastAPI, Query
import random

app = FastAPI()

scrambled_words = []
words = []

@app.get("/getscrambles")
async def get_scrambled_words():
    return { "scrambled words" : scrambled_words }

@app.get("/getwords")
async def get_words():
    return { "words" : words }

@app.post("/scramble")
async def scramble_word(word: str = Query(None, max_length=20, regex="^[A-Za-z]+$")):
    words.append(word)
    l = list(word)
    random.shuffle(l)
    scrambled = ''.join(l)
    scrambled_words.append(scrambled)
    return { "scrambled_word" : scrambled }
