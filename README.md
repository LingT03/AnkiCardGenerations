# AnkiCardGenerations

_Author : Ling Thang_

_Last Updated : 04/16/2025_

**Requires**

```
pip install genanki
```

**Usage**

```
python3 makecards.py <deckname> <json_file>
```

**output**

`deckname`.apkg

requires you to have the application installed on your computer to open the file.

## What is AnkiCards?

[AnkiCards](https://apps.ankiweb.net/) is a flashcard program available for free on computers and $30 on mobile devices. It is a tool that I've been using to cram for my exams.

It is a great tool to practice **Active Recall** and **Spaced Repetition**. Or to cram last minute for an exam, like I am doing right now :)

I don't know if it works but I know I have an A in all my class so far 🤷‍♂️.

## What is AnkiCardGenerations?

The following script, `makecards.py`, is a tool that I created to help me generate Anki cards from a JSON file using the [Genanki](https://pypi.org/project/genanki/) package. It simplifies the process of creating `.apkg` files, which can be imported into the Anki application.

general structure for the json file:

```json
{
  "deck_name": "Name of the deck",
  "cards": [
    {
      "question": "Question",
      "choices": [
        "choice1",
        "choice2",
        "choice3",
        "choice4"
      ],
      "correct_answer": "choice1",
      "explanation": "Because I said so"
    },
    ...
  ]
}
```

### Future Plans

- [ ] Integrate OPENAI API to generate cards from PDF
- [ ] Use OPENAI API to generate questions and answers
- [ ] Add support for images
- [ ] Add styling to cards (optional just for fun)
