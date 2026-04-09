# Cisc121_BubbleSort_DavidCheng-20460021
An app for my CISC 121 project revolving around Bubble sort. It will teach you step by step what is happening in the sort.
# Algorithm Name
The algorithm I have chosen is Bubble Sort.


## Demo video/gif/screenshot of test
IMAGES SHOWING THE SORTING PROCESS - IT GOES FRAME 1 COMPARING 4 AND 1 (NO SWAP 1 < 4) THEN IT SHOWS FRAME 2 SWAPPING 4 AND 3 (SINCE 4 > 3). THE FINAL IMAGE IS AFTER THE SORT GOES THROUGH.
<img width="1544" height="418" alt="image" src="https://github.com/user-attachments/assets/429644d6-c835-474a-b310-72c44a97c23b" />
<img width="1498" height="393" alt="image" src="https://github.com/user-attachments/assets/ac2eeca2-002a-4490-aea1-59756d577a22" />
<img width="825" height="435" alt="image" src="https://github.com/user-attachments/assets/5f305376-a58e-488e-b71d-945fc31e54c8" />


## Problem Breakdown & Computational Thinking (You can add a flowchart , write the four pillars of computational thinking briefly in bullets, etc.)
To build the bubble sort app I broke the problem down it into three main parts. Decomposition, pattern recognition, and abstraction.

Decomposition -
For the decomposition part, I had to think about what type of data I would want. I wanted the user to be able to input a string and then I would have to turn the string into a list of integers.
I wanted to also turn my bubble sort algorithm into a function so that the app could call on it.
Lastly, I wanted to break it down so that the app would have a visual component, and I wanted to make it clear to the user what was happening so I should use color.

Abstraction -
For abstraction, I wanted to simplify the app for the user. Originally I wanted the app to have multiple buttons for the user to use and for the user to input the list to be sorted. After some thought though as I was building the app, I thought it would be easier for the user if there was only 2 buttons. One for inputting the list and another for going through the sorting process. Along with that, as I was testing the app I noticed that it was tedious to write an unsorted list for the app. While keeping the input feature, I then added it so that there was a list already inputted by default to save the user time if they just wanted to see the sort function. Lastly, it was hard to tell what was happening during the sorting as the user (if they are learning about bubble sort) would not know what to look for. So, I added color to the numbers being compared and sorted, and then added additional text explaining what was happening to hide any complexity while keeping the app simple.

Pattern Recognition and Algorithm -
For pattern recognition and algorithm, I needed to create an algorithm that would be able to "float" the numbers up. After reviewing how the sorting process of bubble sort looked, I noticed that it started at the first and then compared it with its neighbor number, if it was higher it would swap. It would then go to the next number (if it swapped was the same number) until it reached the end and then did it again leaving the number at the end to be the highest.

So, after reviewing, I decided to use 2 for loops to ensure that all the numbers had gone through properly. The first loop would be the boundary for the end, while the second loop would be the numbers being swapped. Knowing this, I used i as outer loop and o as inner loop. I would then compare o and o+1 to see who was higher, and I would swap if higher. Originally, the swap did not work since I did not create a temporary third party variable to store one of the numbers. Due to this, it would instead copy the number over and then destroy the other number. After thinking about the problem, I then tried adding the temporary variable to act as a "save" which solved the issue. Then I needed it to end, so the algorithm would end once the first loop (i) reached the length of the list since that'd mean it sorted through every possible sort.
I then asked AI to produce potential edge cases for the algorithm to test to ensure that they were met. The main case that was introduced was that the algorithm would keep attempting to sort even after the list was fully sorted. 
TESTING SCREENSHOTS FOR EDGE CASES:
REGULAR MIXED INPUT
<img width="507" height="63" alt="image" src="https://github.com/user-attachments/assets/3d1a99c9-2a68-4955-b09e-984bea32d959" />
WORST CASE REVERSE SORTED
<img width="320" height="53" alt="image" src="https://github.com/user-attachments/assets/47d19096-74e0-4644-990b-51236be8ba02" />
DUPLICATES
<img width="344" height="48" alt="image" src="https://github.com/user-attachments/assets/18624847-f330-4dbc-8620-4431bf139c4d" />
NEGATIVE NUMBERS
<img width="331" height="43" alt="image" src="https://github.com/user-attachments/assets/7bd6f591-ca11-4842-a916-2b199b557d0c" />



## Steps to Run
1. (If running without hugging face, otherwise skip to step 4) First install gradio by entering "pip install --upgrade gradio" in the terminal or command prompt

2. Download the python program bubblesortUI.py and hit run

3. Then click the link it provides which is the website.

4. A default list is provided, but you can enter your own list in the input numbers box (numbers separated by commas), and then hit set/reset list. This will load the list in the input box.

5. Then click next step and it will show you the next step in the bubble sort algorithm. You can keep clicking until the list is sorted. In the box above it, it will explain what is happening with the number being compared in the sort to be colored.


## Hugging Face Link
https://huggingface.co/spaces/davywavy123/Cisc121-BubbleSortProject


## Author & Acknowledgment
Name: David Cheng
Student ID: 20460021
Course: CISC 121 - Introduction to Computing Science

I confirm that this submission is my own work and is consistent with the Queen's regulations on Academic Integrity. 
I myself created the algorithm that would perform bubble sort and a majority of the code used in the app with gradio. 
AI was used in the help of debugging and fixing errors that occurred in the code.

For example, 
