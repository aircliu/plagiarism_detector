# plagiarism_detector
This code is a plagiarism checker implemented in Python, designed to identify potential instances of plagiarism within a collection of text documents. The code utilizes various libraries, including os, numpy, and sklearn, to handle file operations, perform text vectorization using TF-IDF, and calculate cosine similarity between document vectors.

Pre Req:
Install SciKit machine-learning library 


The code begins by obtaining a list of text files in the current directory with the ".txt" extension. It then reads the contents of these files and stores them in a list called sample_contents. The vectorize lambda function is defined to convert the text contents into TF-IDF vectors using TfidfVectorizer.

The similarity lambda function calculates the cosine similarity between two document vectors using the cosine_similarity function from sklearn.metrics.pairwise. The document vectors, along with their corresponding filenames, are paired and stored as tuples in a list called s_vectors.

The check_plagiarism function performs the plagiarism checking algorithm. It iterates over each document vector and its associated filename in s_vectors. Within each iteration, it compares the document vector with all other document vectors, calculating the similarity score and storing the results in a set called results. The results contain tuples representing pairs of potentially plagiarized documents and their corresponding similarity scores.

Finally, the code iterates over the results set and prints the pairs of potentially plagiarized documents and their similarity scores to the console.

This code showcases the use of text processing techniques and similarity calculations to implement a plagiarism checker. It can be a useful tool for detecting plagiarism in educational or content creation contexts.
