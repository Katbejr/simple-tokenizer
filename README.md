# simple-tokenizer
# Simple Tokenizer

A basic tokenizer built in Python, developed as part of my learning journey on Large Language Models (LLMs).

## Description

This project implements a simple tokenizer that:
- Splits text into tokens (words and punctuation)
- Builds a vocabulary from a given text
- Encodes text into numerical IDs
- Decodes IDs back into text

## Credits

This project is inspired by the book **"Build a Large Language Model (From Scratch)"** by Sebastian Raschka, available on his GitHub repository: [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)

## Usage

```python
tokenizer = SimpleTokenizerV2(vocab)
ids = tokenizer.encode("Hello, world!")
text = tokenizer.decode(ids)
```

## Author

**Joud Katbe** — Software Engineering student at Polytechnique Montréal
[LinkedIn](https://www.linkedin.com/in/joud-katbe/)

## License

This project is licensed under the MIT License.
