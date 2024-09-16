# Project Customer Reviews

## A Comprehensive Script To Extract Customer Reviews For Machine Learning 

### Overview

This project is designed to efficiently extract customer reviews from the Trustpilot website using Scrapy. It automates the process of collecting key data points such as ratings, review dates, and business details. 

By providing a structured dataset, this tool is particularly useful for tasks like sentiment analysis, customer feedback analysis, and training machine learning models on real-world customer experiences. With built-in data cleaning and handling of pagination, it ensures seamless and accurate extraction, ready to be used for analysis or further processing.

### Features

- **Easy to Setup**
  
- **Handles Pagination**
  
- **Cleans Data into Proper Format**

- **Uses Middlewares to Handle Browser Headers**

- **Uses Delays to Avoid Overloading Server**

---

### Technologies Used 🛠️

- Python
  
- Scrapy

- API Requests

---

### How To Use 🔧

From your command line, first clone the project:

```bash
# Clone the project
$ git clone "https://github.com/mibrahimbashir/customer_reviews.git"

# Go into the project level repository
$ cd customer_reviews

# Install dependencies
$ pip install -r requirements.txt

# Go into the spider repository
$ cd customer_reviews

# Run the spider
$ scrapy crawl tp

```


Executing the above commands will start the Scrapy spider, which will collect customer reviews and save them in two files: `reviews.csv` and `reviews.json`.

To stop execution, press <kbd>Ctrl + C</kbd> inside the command line OR equivalently close the application.

#### Additional Configurations

If you want to attach new *Browser Headers* with each request, head over to the [ScrapeOps](https://scrapeops.io/) website and create a free account. Once signed up a free **API KEY** will be created for your account. 

Create a new `.env` file in the project directory and paste the following line of code in it. Make sure the file name exactly matches `.env`. Once done, save the file and you are good to go. 

```python

SCRAPEOPS_API_KEY=YOUR_API_KEY_HERE

```
---

### Give a Star ⭐

If you like this project, then give it a Github star by pressing the Star button ⭐

---

### Author

- **Ibrahim Bashir** [LinkedIn](https://www.linkedin.com/in/muhammad-ibrahim-091708217/)
