# UWprojects
## Sahil Bains - UW '24 - Github of All Projects




### social_network.py and social_network_tests.py
## CS 160 Homework 5:

This project implement network/friend recommendation algorithms for a social network. The primary goal is to answer the question, "Who is the best person to recommend as a friend for user X?" by generating a list of non-friends ordered from best friend recommendation to worst. A non-friend refers to any user who is not X and is not currently a friend of X. The recommendation algorithm may include all non-friends or only a subset of them depending on the specific algorithm being used. The project aims to provide a comprehensive solution for social network friend recommendations.

### blur_image.py and color_to_gray.py
## CS 160 Homework 3:

This project is designed to take input images and apply a blur effect to them. The code uses an algorithm that examines each pixel in the image and calculates the average value for that pixel. The resulting blurred image is then stored in a new grid with the same dimensions as the original image. For any pixel on the edge of the image, where its surrounding 8 pixels fall outside of the image, the code substitutes those values with 0. The end result is a blurred version of the original image that can be easily read and understood through individual pixels.


## Assignment: Search Engine with tf-idf Information Retrieval
## CS 163 Homework 5
### Overview

In this challenging assignment, students will delve into the intricacies of implementing a search engine with a focus on tf-idf information retrieval using Python. The primary objectives revolve around crafting the Document and SearchEngine classes to achieve robust functionality.

### Document Class

Within the `Document` class, the task involves the creation of an initializer to meticulously compute term frequency for each term in a given document. Additionally, a method is to be implemented to return the term frequency of a specified term, along with other pertinent functions. Noteworthy considerations include handling term normalization, ensuring accurate computation of the tf-idf statistic, and thorough testing.

### SearchEngine Class

The `SearchEngine` class, central to the project, demands the implementation of an initializer responsible for constructing an inverted index. This index associates each term in the corpus with a list of documents containing the term. A crucial private method, `_calculate_idf`, is introduced to compute the inverse document frequency. The search method, designed to handle both single and multi-term queries, computes and returns a sorted list of document paths based on the tf-idf statistic.

### Implementation Guidelines

The assignment places significant emphasis on meticulous planning and execution, encouraging students to comprehend the nuances of the tf-idf statistic. A structured approach is advised, beginning with careful testing of the Document class before progressing to the SearchEngine class. The comprehensive nature of this project makes it an ideal addition to a technical portfolio, showcasing proficiency in data science and Python programming.




