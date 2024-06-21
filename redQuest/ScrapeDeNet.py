import praw
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Initialize the Reddit instance
reddit_read_only = praw.Reddit(client_id="a4ZGK6-dmEvPVi1gjDgD3w", client_secret="A7pDwzdIoCWeGiNcWxfYa71ktrXJcg", user_agent="Murema")

# Scrape the top posts of the month from the Python subreddit
subreddit = reddit_read_only.subreddit("programming")
posts = subreddit.top("month")

posts_dict = {"Title": [], "ID": [], "Score": [], "Total Comments": []}

for post in posts:

    # shortening the Title
    newTitle = ' '.join(post.title.split()[:6])

    posts_dict["Title"].append(newTitle)  # Add the title of each post
    posts_dict["ID"].append(post.id)
    posts_dict["Score"].append(post.score)
    posts_dict["Total Comments"].append(post.num_comments)


# Create a DataFrame from the dictionary
top_posts = pd.DataFrame(posts_dict)

# Save the DataFrame to a CSV file
top_posts.to_csv("Top_posts.csv", index=False)

# Load data from CSV
df = pd.read_csv("Top_posts.csv")

# Basic cleaning
df.dropna(inplace=True)  # Remove rows with missing values
df.drop_duplicates(subset=["ID"], inplace=True)  # Remove duplicate posts

# Basic analysis
print(df.describe())

# Top posts by score
top_posts = df.sort_values(by="Score", ascending=False).head(10)
print(top_posts)


# Visualization

# Distribution of post scores
plt.figure(figsize=(10, 6))
sns.histplot(df['Score'], bins=30, kde=True)
plt.title('Distribution of Post Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()

# Top 10 posts by score
plt.figure(figsize=(10, 6))
sns.barplot(x=top_posts['Score'], y=top_posts['Title'])
plt.title('Top 10 Posts by Score')
plt.xlabel('Score')
plt.ylabel('Post Title')
plt.show()

