## Analyzing Product Reviews 

## Introduction
The goal of this portfolio project is to demonstrate product review analysis. Review data was downloaded from an open platform review website for personal, non-commercial use. 

![cook](./images/andrae-ricketts-3Qi0PkM_Wes-unsplash.jpg)

Photo by <a href="https://unsplash.com/@drezart?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Andrae Ricketts</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  

## Data Description and Preparation
This project uses publicly-accessible product review data submitted to the open platform, Trust Pilot. The following data was downloaded for analysis.
* Review text
* Star rating (1-5)
* Review date
* Country code (provided by reviewer)

See the [Data Prep Notebook](./code/nb1_data__prep.ipynb) for more details.


## Analysis
Exploratory data analysis and word frequency text analysis techniques were used to answer the following questions:

* What were the review counts by year? 
* What were the review counts by Rating?
* What are the monthly review counts over time? 
* What are the top 30 words used in 5 star ratings?
* What are the top 30 words used in 2,3,4 star ratings?
* What are the top 30 words used in 1 star ratings?

See the [EDA Notebook](./code/nb2_eda.ipynb) for more details.

## Repository Structure
```
--code
----nb1_data_prep.ipnyb 
----nb2_eda.ipynb
--data (dir for all data files ingested/generated)
--images (dir for images)
```

## For More Information
* Contact the author [Leah Pope](https://www.linkedin.com/in/leahspope/)
