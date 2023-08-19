
I have thought of 3 approaches 

## Approach 1
### Simpler approach
## Observing patterns

The Supreme Court judgment pdfs are very repetitive

1)
![alt text](https://i.ibb.co/7C5wKJH/1.jpg)

Initially, the pdf starts with basic information that is centrally aligned, it is connected to the main text by the word 'judgment' 

3)
![alt text](https://i.ibb.co/ThDn8dm/2.jpg)

The second kind of data available is the main text written normally in a justified style

5)
![alt text](https://i.ibb.co/cY1bZtH/3.jpg)

The third kind of text available to us is center aligned written only in some part of the center

---
What I thought was training a model so that it recognizes what is is the heading (observing patterns such as the main content starts after the word judgment), basically, this involves an NLP approach, I think it would work fine because the judgments follow the same pattern.


## Approach 2
### Using CV
## Works for all kinds of document

This involves first converting the pdf to images.
Then using Python library py-tesseract to detect the letters, then I calculated the absolute position of that letter with respect to the page borders. I then put those letters in a html file with the absolute coordinates.

I tried finding a model but was not able to find a pre-trained model that classified headings, and spaces and maintained the document aspects.

Initially, I was thinking of calculating the spaces from the border but realized it was prone to many errors. 

I then tried to print each individual letter not as a letter but as an image. It was giving good results but was computation heavy and defeated the purpose to converting it into the text form.

So then I thought of obtaining individual letters using Pytesseract and then finding the position of it and placing the letter so that it makes it more readable.
I tried adjusting the gaps between the letter by providing spacing but that messed up the coordinates.


![alt text](https://i.postimg.cc/Pr67Wnfw/12.jpg)

![alt text](https://i.postimg.cc/Y2dRVfcc/13.jpg)

## Final Result-

![alt text](https://i.postimg.cc/VLTRsfLD/14.jpg)

After some tweaking such as changing the screen resolution, instead of printing image I printed the letter at a coordinate. the x coordinate was averaged. I tried to align the y coordinates a straight line.

The code writes the html in the output.html file.
This can be further improved by better cv techniques and refining it. We can add ml model to it so that the accuracy of the data can be improved.

## Approach 3
### Using spaces in file
## Text to markdown

Since the text in the file can be selected(pdf available is not just pasting of images), we can train a model such that it calculates the spaces between lines and words and then determines whether they are paragraph heading. 
The model in approach 3 is already trained and produces a file in examples that shows a markdown version of the pdf with the body and headings retained along with the tables.

I found this model on the internet that does something similar for a different language.


![alt text](https://i.postimg.cc/qRmFjcJL/4.jpg)

![alt text](https://i.postimg.cc/jSzkGYqC/5.jpg)
