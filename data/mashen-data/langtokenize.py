import os
import numpy as np
import argparse
import sentencepiece as spm

def tokenize_file(args):
    """
    Tokenizes a given file using a SentencePiece model and saves the output as a numpy array.
    """
    file, model, out = args
        
    data = np.asarray(model.EncodeAsIds(file), dtype=get_dtype(model.GetPieceSize()))
    np.save(out, data)

def get_dtype(vocab_size):
    """
    Returns the smallest numpy integer data type that can hold the vocabulary size.

    Args:
        vocab_size (int): Size of the vocabulary.

    Returns:
        numpy.dtype: The smallest integer data type that can hold the vocab size.
    """
    if vocab_size < np.iinfo(np.uint16).max:
        return np.uint16
    elif vocab_size < np.iinfo(np.uint32).max:
        return np.uint32

if __name__ == "__main__":
    # Use argparse to get command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", required=True, help="txt file to be tokenized")
    parser.add_argument("--model", required=True, help="model to be used")
    parser.add_argument("--out", required=True, help="outputfilename")
    args = parser.parse_args()

def main(file, model, out) :
    tokenize_file(file, model, out)