
I have thought of 3 approaches 

## Approach 1
### Simpler approach
## Observing patterns

The Supreme court judgement pdfs are very repetetive

1)
![alt text](https://i.ibb.co/7C5wKJH/1.jpg)
Initially the pdf starts with basic information that is centrally aligned, it is connected to the main text by the word 'judgement' 

2)
![alt text](https://i.ibb.co/ThDn8dm/2.jpg)
The second kind of data available is the main text written normally in justified style

3)
![alt text](https://i.ibb.co/cY1bZtH/3.jpg)
The third kind of text available to us center aligned written inly in some part of the center

---
What I thought was training a model so that it recognizes what is is the heading (observing pattern such as the main content starts after the word judgement), basically this involes an NLP approach, I think it would work fine beacuse the judgments follow the same pattern.

## Approach 2
### Using spaces in file
## Text to markdown

Since the text in the file can be selected(pdf available is not just pasting of images), we can train a model such that it calculates the spaces in between lines adn words then determines whether they are paragraphs heading. 
The model in approach 2 in already trained and produces a file in examples that shows a markdown version of the pdf with the body and headings retained along with the tables.


![alt text](https://i.postimg.cc/qRmFjcJL/4.jpg)

![alt text](https://i.postimg.cc/jSzkGYqC/5.jpg)

## Approach 3
### Using Opencv
## Works for all kind of document

This involves first converting the pdf to images.
Then using python library pytesseract to detect the letters, then i calculated the absolute postion of that letter with respect to the page borders. I then put those letter in a html file woth the absolute coordinates.
![alt text](https://i.postimg.cc/Pr67Wnfw/12.jpg)

![alt text](https://i.postimg.cc/Y2dRVfcc/13.jpg)

## Final Result-

![alt text](https://i.postimg.cc/VLTRsfLD/14.jpg)
After some tweaking such as changing the screen resolution, instead of priting image i printed the ltter at a cordinate. the x cordinate was averaged. I tried to align the y coordinates a straight line.

The code writes the html in the output.html file.
This can be further improved by better cv techniques and rifing it. We can add ml model to it so that the accuracy of the data can be improved.
