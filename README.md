# LEADERS SCRAPER

## 1. Project Description

This project is designed as a learning exercise. It involves querying an API for a list of countries and their leaders, extracting their short biographies from Wikipedia, and saving the data to disk. Throughout the project, participants are guided step by step through various processes, including:

- Creating a self-contained development environment.
- Retrieving information from an API (a website for computers).
- Utilizing web scraping techniques on a website without an available API.
- Saving the obtained output for later processing.

The learning objectives of this project encompass topics such as *scraping*, *data structures*, *regular expressions*, *concurrency*, and *file handling*.

## 2. How to Install and Run the Project

This project requires Python 3.11.4 or a higher version. To run the project, follow these steps:

1. Clone the repository from [Wikipedia-Scrapper](https://github.com/MykolaSenko/Wikipedia-Scrapper.git) to your local machine.
2. Install the following dependencies using pip:
   - Beautiful Soup 4: `pip install beautifulsoup4`
   - Requests: `pip install requests`
   - RegEx: `pip install regex`
3. After installing the dependencies, navigate to the copied folder and run the 'leaders_scraper.py' file.

## 3. How to Use the Project

The output of the code will be a dictionary where the keys represent countries, and the values are dictionaries containing information about each country's leaders. Within these value dictionaries, you'll find the leaders' names, URLs linking to their Wikipedia pages, and short biographies. The resulting output will be stored in a file named 'leaders.json', which will be saved on your computer. In case there are issues retrieving data for certain countries, an error message will be displayed: "Error retrieving leaders for {country}". If this occurs, try running the code again.

## 4. Credits

This project was completed over a span of 3 days, from June 21 to June 23, 2023, as part of the AI Bootcamp at BeCode.org in Ghent. It was developed by Mykola Senko, a Junior AI & Data Scientist. You can find Mykola's GitHub profile [here](https://github.com/MykolaSenko) and LinkedIn profile [here](https://www.linkedin.com/in/mykola-senko-683510a4/).

The project was conducted under the supervision of Vanessa River Quinones, whose LinkedIn profile can be accessed [here](https://www.linkedin.com/in/vriveraq/), and Samuel Borms, whose LinkedIn profile is available [here](https://www.linkedin.com/in/sam-borms/?originalSubdomain=be).

## 5. License

This project is licensed under the [GNU General Public License v3.0](./LICENSE), which permits code modifications and commercial use.

Gent, June 23, 2023.