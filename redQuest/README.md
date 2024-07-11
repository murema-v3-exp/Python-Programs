# Reddit Top Posts Analysis

This project scrapes the top posts from the "programming" subreddit for the past month using the PRAW (Python Reddit API Wrapper) library, performs basic data analysis, and visualizes the results.

## Project Overview

The project uses the PRAW library to access Reddit's API and gather data about the top posts of the month from the "programming" subreddit. The data is then cleaned, analyzed, and visualized using pandas, matplotlib, and seaborn.

## Files

- `keys.txt`: A text file containing Reddit API credentials.
- `reddit_top_posts.py`: The main script that scrapes the data, performs analysis, and creates visualizations.
- `Top_posts.csv`: A CSV file containing the scraped data.

## Dependencies

Make sure you have the following Python packages installed:

- praw
- pandas
- matplotlib
- seaborn

You can install these packages using pip:

```bash
pip install praw pandas matplotlib seaborn
```

# Reddit API Credentials

Before running the script, you need to have a Reddit app with credentials (client ID, client secret, user agent). These should be stored in a `keys.txt` file with each credential on a new line:


```bash
client_id_here
client_secret_here
user_agent_here
```


## Data Scraping

The script initializes a PRAW Reddit instance using the credentials from the `keys.txt` file. It then scrapes the top posts from the "programming" subreddit for the past month and stores the data in a dictionary. The data is saved to a CSV file named `Top_posts.csv`.

## Data Cleaning

The script performs basic data cleaning:

- Removes rows with missing values.
- Removes duplicate posts based on the post ID.

## Data Analysis

Basic statistical analysis is performed on the cleaned data, and the top 10 posts by score are identified and printed.

## Visualization

The script generates the following visualizations:

- A histogram of the distribution of post scores.
- A bar plot of the top 10 posts by score.

## How to Run

1. Make sure all dependencies are installed.
2. Place the `keys.txt` file in the same directory as the script.
3. Run the script:

```bash
python reddit_top_posts.py
```

The script will output basic statistical analysis to the console and display the visualizations.



