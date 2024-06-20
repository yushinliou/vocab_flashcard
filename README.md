# Auto generate definition, memory tip and sample sentence for create flash card

## file structure
```
├── card
│   ├── card_vocab_test.txt # content for all group of vocab
│   ├── card_vocab_test_Group 0.txt # content for single group
│   └── card_vocab_test_Group 1.txt # content for single group
├── card_prompt.txt # the prompt we use on generate content
├── card_vocab_test.xlsx # worksheet store vocab
├── combine_card.py # combine all txt for each group of vocab into 1 single txt
└── gen_card.py # generate content for vocab in card_vocab_test.xlsx, output store in /card
```

## Set up
1. Install [poetry](https://python-poetry.org/)
2. Run `poetry install`
3. Create `.env` based on `.env.example`
Make sure you have variable `OPENAI_API` in your envirnment. We using chatgpt to auto generate the definition, sample stentence and memory tips for vocabulary, so we will need opanai api. Check [openai api](https://openai.com/index/openai-api/) to see how to get api   

## Run
```bash
poetry run python3 gen_card.py
poetry run python3 
```
Change variable `vocab_file` into your vocabulary file name, the default value of `vocab_file` is `card_vocab_test`
If you have a large number of vocab in your worksheet, I recommend you separate them into multiple groups of vocab. For example, I have 900 words, and I want to generate an explanation for them. It might more easily get an error if I input all the words in at once, or encounter token limitation. Alternatively, I separate them into 30 groups, which means 30 columns in the worksheet, so that the ChatGPT can deal with each group one by one.

The generated content should be in this format
```
word1=definition;memory tips;sample sentence
word2=definition;memory tips;sample sentence
...
```

## Flash card
Finally, you can copy the text in `/card/{vocab_file}.txt` and create flash card on Quizlet! Check the tutorial [here](https://help.quizlet.com/hc/en-us/articles/360029977151-Creating-sets-by-importing-content) if you are not familiar with it.
