import os
from numpy import vectorize 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
 
# List all text files in the current directory
sample_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
# Read the contents of each text file into a list
sample_contents = [open(File).read() for File in sample_files]

# Define a lambda function to vectorize text using TF-IDF
vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
# Define a lambda function to calculate cosine similarity between two documents
similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

# Vectorize the sample text files
vectors = vectorize(sample_contents)
# Pair each sample file with its vector representation for future use
s_vectors = list(zip(sample_files, vectors))

# Define a function to check for plagiarism
def check_plagiarism():
    # Create an empty set to store results
    results = set()
    # Make the list of sample vectors global so it can be accessed inside this function
    global s_vectors
   
 
 # Loop through each sample and its vector
    for sample_a, text_vector_a in s_vectors:
        # Create a copy of the sample vectors to manipulate
        new_vectors = s_vectors.copy()
        # Find the index of the current sample file and delete it from the copied list
        current_index = new_vectors.index((sample_a, text_vector_a))
        del new_vectors[current_index]
       
     
     # Loop through the remaining sample vectors
        for sample_b, text_vector_b in new_vectors:
            # Calculate the similarity score between the two vectors
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            # Sort the sample files to create a unique identifier for the pair
            sample_pair = sorted((sample_a, sample_b))
            # Create a tuple containing the pair and the similarity score
            score = sample_pair[0], sample_pair[1], sim_score
            # Add the result to the set
            results.add(score)
  
 
 # Return the results
    return results

# Call the function and loop through each result to print it
for data in check_plagiarism():
    print(data)
