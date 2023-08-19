
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
Training a model such that it seeing the white spacing using opencv, then calculating the spaces it need to leave such that it covers the white space, the font size can also be adjusted with this approach. 
It is done through edge-detection techniques, we can make egdes around each text and obtain the position wrt page.

