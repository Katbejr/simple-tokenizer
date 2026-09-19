"""
Simple Tokenizer
-----------------
A basic word-level tokenizer for text preprocessing, built as part of
learning how Large Language Models (LLMs) work under the hood.

Inspired by: "Build a Large Language Model (From Scratch)" by Sebastian Raschka
https://github.com/rasbt/LLMs-from-scratch

Author: Joud Katbe
https://www.linkedin.com/in/joud-katbe/
"""

import re


def build_vocab(file_path):
    """
    Reads a text file and builds a vocabulary (word -> id mapping).

    Args:
        file_path (str): path to the text file used to build the vocabulary.

    Returns:
        dict: vocabulary mapping each unique token to a unique integer id.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
    preprocessed = [item.strip() for item in preprocessed if item.strip()]

    all_tokens = sorted(set(preprocessed))
    all_tokens.extend(["<|endoftext|>", "<|unk|>"])

    vocab = {token: integer for integer, token in enumerate(all_tokens)}
    return vocab


class SimpleTokenizerV2:
    """
    A simple word-level tokenizer that converts text to token IDs and back.

    Unknown words (not present in the vocabulary) are mapped to the
    special token "<|unk|>" instead of raising an error.
    """

    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}

    def encode(self, text):
        """Converts a text string into a list of token IDs."""
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [
            item if item in self.str_to_int else "<|unk|>"
            for item in preprocessed
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        """Converts a list of token IDs back into a text string."""
        text = " ".join([self.int_to_str[i] for i in ids])
        # Remove extra spaces before punctuation
        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
        return text


if __name__ == "__main__":
    # Example usage
    vocab = build_vocab("textLLM.txt")
    tokenizer = SimpleTokenizerV2(vocab)

    print(f"Vocabulary size: {len(vocab)}\n")

    text = "Hello, do you like tea? This is a completely unknownword test."
    ids = tokenizer.encode(text)
    decoded = tokenizer.decode(ids)

    print("Original text:", text)
    print("Encoded IDs:  ", ids)
    print("Decoded text: ", decoded)
