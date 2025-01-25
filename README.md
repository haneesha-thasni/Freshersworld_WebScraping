# Web Scraping Project: Tech Jobs Analysis

![image](https://github.com/user-attachments/assets/9387d4cd-8194-41d1-a72f-359875917504)


## Project Overview

This project is a culmination of our studies in web scraping, where we were tasked with extracting and analyzing tech-related job postings from a job portal. 

The portal we selected was Freshersworld. 

Here's an outline of the project's workflow and outcomes:

## Objective

To scrape tech job postings, extract the following details:

* Job Title

* Experience Required

* Company Name

* Salary

## Workflow

### 1. Web Scraping:

* Extracted job data from Freshersworld using Python libraries like

      BeautifulSoup

      Requests

      Selenium

### 2. Data Conversion:

* Converted the scraped data to SQL format using SQLizer.io.

* Imported the SQL data into a MySQL database.

### 3. Data Cleaning and Feature Engineering:

Addressed several issues in the data, including:

* Salary data in range format was converted to numeric values.

* Handled null values and removed duplicates.

* Used Jupyter Notebook for cleaning and feature engineering.

### 4. Data Visualization:

* Loaded the cleaned MySQL database into Power BI.

* Designed an insightful and interactive dashboard.

## Challenges Faced

* Inconsistent salary formats (e.g., ranges) required significant preprocessing.

* Null values and duplicate entries in the data added complexity to the cleaning process.

* Integrating various tools and ensuring compatibility among them.

## Dashboard Insights

The Power BI dashboard includes the following visualizations:

### 1. Most Trending Job Titles:

Displaying the number of available vacancies for each job title.

### 2. Highest Paid Jobs:

Highlighting the top-paying job roles.

### 3. Most Dense Locations:

Visualizing locations with the highest number of job postings.

### 4. Salary Comparison:

Comparing salaries for the top 10 trending jobs.

### 5. Filtering Options:

Enabling users to filter jobs based on location and salary range.

## Tools and Technologies Used

* Web Scraping: Python (BeautifulSoup, requests),Selenium

* Data Conversion: SQLizer.io

* Database Management: MySQL

* Data Cleaning: Jupyter Notebook (pandas, numpy)

* Data Visualization: Power BI

## Final Steps

The entire project, including the scripts and Power BI dashboard, was pushed to GitHub using the command line interface.

## Insights from the Dashboard

* The dashboard provides a clear visualization of the job market trends in the tech domain.

* Users can explore job opportunities based on various filters such as location and salary range.

* Insights on trending job titles and highest-paying roles help job seekers and analysts.

## How to Use the Project

* Clone the repository:

      git clone <repository_url>

* Set up MySQL and import the SQL data.

* Open the Power BI dashboard file (.pbix) to explore the insights.


## Future Improvements

* Automate the entire pipeline for real-time job data updates.

* Extend the analysis to other job portals for broader insights.

* Add more filters and advanced analytics to the dashboard.

## Conclusion

This project was a comprehensive learning experience in web scraping, data processing, and visualization. Despite challenges, the final output is a robust dashboard that provides valuable insights into the tech job market.


Feel free to explore, provide feedback, or contribute to the repository!
