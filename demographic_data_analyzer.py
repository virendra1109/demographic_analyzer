import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load the dataset
    df = pd.read_csv('adult.data.csv')
    
    # Calculate the race count
    race_count = df['race'].value_counts()

    # Calculate the average age of men
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # Calculate the percentage of people with a Bachelor's degree
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

    # Calculate the percentage of people with higher education that earn >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = (df[higher_education]['salary'] == '>50K').mean() * 100

    # Calculate the percentage of people without higher education that earn >50K
    lower_education_rich = (df[~higher_education]['salary'] == '>50K').mean() * 100

    # Calculate the minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # Calculate the percentage of people who work the minimum number of hours and earn >50K
    rich_percentage = (df[df['hours-per-week'] == min_work_hours]['salary'] == '>50K').mean() * 100

    # Calculate the highest earning country
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True) * 100
    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = country_salary.max()

    # Calculate the most popular occupation in India for those earning >50K
    india_df = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_df['occupation'].value_counts().idxmax()

    result = {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'higher_education_rich': round(higher_education_rich, 1),
        'lower_education_rich': round(lower_education_rich, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }

    if print_data:
        print(result)

    return result
