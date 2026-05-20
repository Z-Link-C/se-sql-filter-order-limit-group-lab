import pandas as pd
import sqlite3

##### Part I: Basic Filtering #####

# Create the connection
# Note the connect is 'conn1' since there will be multiple .db used
conn1 = sqlite3.connect('planets.db')

# Select all
print(pd.read_sql("""SELECT * FROM planets; """, conn1))

# STEP 1
# Replace None with your code
df_no_moons = pd.read_sql("""
                          SELECT * 
                          FROM planets
                          WHERE 
                          num_of_moons= 0; 
                          """, conn1)
print("---------------------Num of Moons Data---------------------")
print(df_no_moons)
print("---------------------End Num of Moons Data---------------------")

# STEP 2
# Replace None with your code
df_name_seven = pd.read_sql("""
                          SELECT name,mass 
                          FROM planets
                          WHERE 
                          length(name)=7; 
                          """, conn1)
print("---------------------Len of 7 Names Data---------------------")
print(df_name_seven)
print("---------------------End Len of 7 Names Data---------------------")


##### Part 2: Advanced Filtering #####

# STEP 3
# Replace None with your code
df_mass = pd.read_sql("""
                          SELECT name,mass 
                          FROM planets
                          WHERE 
                          mass<=1.00; 
                          """, conn1)
print("---------------------Planets <=1.00 Mass Data---------------------")
print(df_mass)
print("---------------------Planets <=1.00 Mass Data---------------------")


# STEP 4
# Replace None with your code
df_mass_moon = pd.read_sql("""
                          SELECT * 
                          FROM planets
                          WHERE 
                          mass < 1.00 
                          AND num_of_moons >= 1; 
                          """, conn1)
print("---------------------Planets <=1.00 Mass w/Moon Data---------------------")
print(df_mass_moon)
print(df_mass_moon.shape)
print("---------------------Planets <=1.00 Mass w/Moon Data---------------------")


# STEP 5
# Replace None with your code
df_blue = pd.read_sql("""
                          SELECT name,color 
                          FROM planets
                          WHERE 
                          color like '%blue%'; 
                          """, conn1)
print("---------------------Blue Planets Data---------------------")
print(df_blue)
print("---------------------Blue Planets Data---------------------")


##### Part 3: Ordering and Limiting #####

# STEP 0

# Create a connection
# Note the connect is 'conn2' since they will be multiple .db used
conn2 = sqlite3.connect('dogs.db')

# Select all
pd.read_sql("SELECT * FROM dogs;", conn2)

# STEP 6
# Replace None with your code
df_hungry = pd.read_sql("""SELECT name,age,breed FROM dogs where hungry=1
                        order by age asc;""", conn2)
print(df_hungry)
print("---------------------BORDER-------------------------------")
# STEP 7
# Replace None with your code
df_hungry_ages = pd.read_sql("""SELECT name,age,hungry 
                            FROM dogs where 
                            hungry=1 and
                            age BETWEEN 2 and 7
                            order by name asc;""", conn2)
print(df_hungry)
print("---------------------BORDER-------------------------------")


# STEP 8
# Replace None with your code
df_4_oldest = pd.read_sql("""SELECT name,age,breed 
                             FROM dogs
                             order by age desc,breed asc
                             limit 4;""", conn2)
print(df_4_oldest)
print("---------------------BORDER-------------------------------")



##### Part 4: Aggregation #####

# STEP 0

# Create a connection
# Note the connect is 'conn3' since they will be multiple .db used
conn3 = sqlite3.connect('babe_ruth.db')

# Select all
pd.read_sql("""
SELECT * FROM babe_ruth_stats; """, conn3)

# STEP 9
# Replace None with your code
df_ruth_years = pd.read_sql("""
                             SELECT (julianday(max(year))-julianday(min(year))) as total_years
                             FROM babe_ruth_stats; """, conn3)
print(df_ruth_years)
print("---------------------BORDER-------------------------------")
# STEP 10
# Replace None with your code
df_hr_total = pd.read_sql("""
                             SELECT sum(HR) as total_hr
                             FROM babe_ruth_stats; """, conn3)
print(df_hr_total)
print("---------------------BORDER-------------------------------")

##### Part 5: Grouping and Aggregation #####

# STEP 11
# Replace None with your code
df_teams_years = pd.read_sql("""
                             SELECT team, count(year) as number_years
                             FROM babe_ruth_stats
                             group by team; """, conn3)
print(df_teams_years)
print("---------------------BORDER-------------------------------")

# STEP 12
# Replace None with your code
df_at_bats = pd.read_sql("""
                             SELECT team, round(avg(at_bats)) as average_at_bats
                             FROM babe_ruth_stats
                             group by team
                             having (round(avg(at_bats)))>=200; """, conn3)
print(df_at_bats)
print("---------------------BORDER-------------------------------")


conn1.close()
conn2.close()
conn3.close()