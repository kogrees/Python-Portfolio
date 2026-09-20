# Basic Job Web Scraper

A basic Python web scraping project created to learn and practice
**BeautifulSoup**.

The project extracts job listing information from a webpage and saves
the collected data into a CSV file.

## 🛠️ Technologies Used

-   Python
-   BeautifulSoup
-   Requests
-   Pandas

## 📌 What I Learned

This project helped me understand the basics of:

-   Sending HTTP requests using `Requests`
-   Parsing HTML using `BeautifulSoup`
-   Finding elements using HTML tags and classes
-   Extracting text and attributes from HTML
-   Storing scraped data in a list
-   Creating a Pandas DataFrame
-   Basic data cleaning and transformation
-   Exporting data to CSV

## 🔄 How It Works

``` text
Website
   ↓
Requests
   ↓
BeautifulSoup
   ↓
Extract Job Data
   ↓
Pandas
   ↓
CSV File
```

## 📊 Data Collected

The scraper collects:

-   Job Title
-   Company
-   Location
-   Date Posted

The location is then split into **City** and **State** before saving the
final dataset.

## 📁 Files

``` text
├── main.py
├── jobs.csv
└── README.md
```

### `main.py`

Contains the Python code used for scraping and processing the data.

### `jobs.csv`

Contains the final scraped and processed job data.

## 🚀 How to Run

Install the required libraries:

``` bash
pip install requests beautifulsoup4 pandas
```

Run the scraper:

``` bash
python main.py
```

The scraped data will be saved to:

``` text
jobs.csv
```

## 🎯 Purpose

This is a **basic learning project** created to understand the
fundamentals of web scraping with BeautifulSoup and Python.

It is not intended to be a production-level web scraper.

## 🖼️ Project Preview

<img width="1672" height="941" alt="add" src="https://github.com/user-attachments/assets/e3dae94c-1ac4-42e4-95d6-33eabc589d10" />

