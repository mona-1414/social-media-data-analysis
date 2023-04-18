import sqlite3
import random
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('my_social_media.db')
c = conn.cursor()

# Create the UserStats table
c.execute('''CREATE TABLE UserStats (
                user_id INT PRIMARY KEY,
                followers INT,
                avg_likes FLOAT
             )''')

# Insert 100 entries into the table with correlated values
for i in range(1, 101):
    followers = int(random.gauss(5000, 2000))
    avg_likes = 10 + 0.5 * followers / 1000 + random.gauss(0, 2)
    c.execute('''INSERT INTO UserStats (user_id, followers, avg_likes)
                 VALUES (?, ?, ?)''', (i, followers, avg_likes))

# Generate the scatter plot
c.execute('''SELECT followers, avg_likes FROM UserStats''')
data = c.fetchall()

x = [d[0] for d in data]
y = [d[1] for d in data]

plt.scatter(x, y)
plt.xlabel('Number of Followers')
plt.ylabel('Average Number of Likes per Post')
plt.title('Relationship between Followers and Likes')
plt.show()

# Close the database connection
conn.commit()
conn.close()
