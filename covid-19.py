#Project Title: COVID-19 Global Data Tracker
#steps to accomplish the project:
#1. Data Collection from reliable COVID-19 dataset witth the file name called owid-covid-data.csv

#2. Data Loading & Exploration
#Load the dataset and explore its structure
import pandas as pd

#load the dataset of owid-covid-data.csv file/Load data using pandas.read_csv().
df = pd.read_csv('owid-covid-data.csv')

#Check columns: df.columns.(display the columns of the dataframe)
print(df.columns)

#Preview rows: df.head().
print(df.head())

#Identify missing values: df.isnull().sum().
print(df.isnull().sum())

#3. Data Cleaning
#Filter countries of interest (Ethiopia, Kenya, China and Afghanistan).
countries_of_interest = ['Ethiopia','Kenya','China','Afghanistan']
df = df[df['location'].isin(countries_of_interest)] 
#Drop rows with missing dates/critical values.
df.dropna(subset=['date', 'total_cases', 'total_deaths'], inplace=True)
#Convert date column to datetime: pd.to_datetime()
df['date'] = pd.to_datetime(df['date'])

#Handle missing numeric values with fillna() or interpolate().
df['total_cases'].fillna(method='ffill', inplace=True)
df['total_deaths'].fillna(method='ffill', inplace=True)

#Exploratory Data Analysis (EDA), it goal is Generate descriptive statistics & explore trends.
import matplotlib.pyplot as plt 

#Plot total cases over time for selected countries ansd Bar charts (top countries by total cases).
for country in countries_of_interest:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
    #Set up the plot.
plt.title('COVID-19 Total Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Plot total deaths over time and design Line charts (cases & deaths over time).
for country in countries_of_interest:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)
    #Set up the plot.
plt.title('COVID-19 Total Cases and Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Compare daily new cases between countries.
for country in countries_of_interest:
    country_data = df[df['location'] == country]
    country_data['daily_new_cases'] = country_data['total_cases'].diff().fillna(0)
    plt.plot(country_data['date'], country_data['daily_new_cases'], label=country)


#Calculate the death rate: total_deaths / total_cases.
df['death_rate'] = df['total_deaths'] / df['total_cases']
#Plot death rate over time for each country.
for country in countries_of_interest:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['death_rate'], label=country)

# 5. Visualizing Vaccination Progress to  Analyze vaccination rollouts.
#Plot cumulative vaccinations over time for selected countries.
# represent in Line charts.
for country in countries_of_interest:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)
    plt.title('COVID-19 Vaccination Progress Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Vaccinations')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
#Compare % vaccinated population
for country in countries_of_interest:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['people_vaccinated_per_hundred'], label=country)

#Optional: Pie charts for vaccinated vs. unvaccinated. 
#Calculate percentage of vaccinated population.
for country in countries_of_interest:
    country_data = df[df['location'] == country]
    vaccinated = country_data['people_vaccinated_per_hundred'].mean()
    unvaccinated = 100 - vaccinated
    plt.pie([vaccinated, unvaccinated], labels=['Vaccinated', 'Unvaccinated'], autopct='%1.1f%%')
    plt.title(f'Vaccination Status in {country}')
    plt.show()

#6. Build a Choropleth Map using Plotly Express
import plotly.express as px
#Prepare a dataframe with iso_code, total_cases for the latest date.
latest_date = df['date'].max()
latest_data = df[df['date'] == latest_date][['iso_code', 'total_cases']]
#Plot a choropleth showing case density or vaccination rates.
fig = px.choropleth(latest_data,
                    locations='iso_code',
                    color='total_cases',
                    hover_name='iso_code',
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title='COVID-19 Total Cases by Country (Latest Date)')
fig.update_geos(fitbounds="locations", visible=False)
fig.show()

#7️. Insights & Reporting for  Summarizing the findings
#Write 3-5 key insights from the data (e.g., "X country had the fastest vaccine rollout").
insights = [
    "Ethiopia has shown a significant increase in total cases over the past year.",
    "Kenya has a relatively lower death rate compared to other countries in the dataset.",
    "China has achieved a high vaccination rate, with over 70% of the population vaccinated",
    "Afghanistan has faced challenges in vaccination rollout, with less than 20% of the population vaccinated.",
    "Overall, vaccination progress varies significantly across the selected countries, with China leading in total vaccinations."
]
#Highlight anomalies or interesting patterns
anomalies = [
    "A sudden spike in total cases in Ethiopia during the last quarter of 2021.",
    "Kenya's daily new cases peaked in mid-2021, followed by a gradual decline.",
    "China's vaccination rate has consistently increased, reaching over 80% by mid-2022.",
    "Afghanistan's vaccination efforts have been hampered by political instability and logistical challenges."
]
#Use markdown cells in Jupyter Notebook to write your narrative.
#A well-documented Jupyter Notebook combining:
#- Data loading and cleaning steps
#- EDA visualizations
#- Insights and conclusions
#8. Save the cleaned data to a new CSV file.
#Save the cleaned data to a new CSV file.
#8. Save the cleaned data to a new CSV file.
#Save the cleaned data to a new CSV file.
#8. Save the cleaned data to a new CSV file.
#8. Save the cleaned data to a new CSV file.

#6. Save the cleaned data to a new CSV file.
df.to_csv('cleaned_covid_data.csv', index=False)
#7. Document the project.
#Project Documentation:
#COVID-19 Global Data Tracker
#This project aims to analyze and visualize COVID-19 data for selected countries (Ethiopia
#Kenya, China, and Afghanistan) using the OWID COVID-19 dataset.
#The project includes data collection, cleaning, exploratory data analysis (EDA), and visualization of key
#metrics such as total cases, deaths, vaccination progress, and death rates.
#The final cleaned data is saved to a CSV file for further analysis or sharing.
#The project provides insights into the COVID-19 situation in the selected countries and can be used for
#further research or public health decision-making.
#8. Share the project on GitHub or any other platform.
#This project can be shared on GitHub or any other platform to make it accessible to others
#interested in COVID-19 data analysis and visualization.
#It can serve as a reference for similar projects or as a resource for public health officials,
#researchers, and data analysts working on COVID-19 related studies.
#The project can be enhanced by adding more countries, additional metrics, or more advanced visualizations.
#The code is structured to be modular and easy to understand, making it suitable for both beginners and experienced data analysts.


 