import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city=input('Which city(chicago , new york city, washington) do you want? ').lower()
        if city not in CITY_DATA[city]:
            print('Sorry this city is not included')
            continue
        else:
            break
    # get user input for month (all, january, february, ... , june)
    while True:
        month=input('Which month do you want?(all, january, february, ... , june) ').lower()
        if (month!="all" and month!="january" and month!="february" and month!="march" and month!="april" and month!="may" and month!="june"):
            print('This month is not included, sorry')
            continue
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('Which day do you want? ').lower()
        if(day!="all" and day!="monday" and day!="tuesday" and day!="wednesday" and day!="thursday" and day!="friday" and day!="saturday" and day!="sunday"):
            print("Sorry, I don't understand!")
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month']==month]


    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    Pop_month= df['month'].mode()[0]
    print('The most common month is:', Pop_month ,'\n')
    # display the most common day of week
    Pop_day=df['day_of_week'].mode()[0]
    print('The most common day is:', Pop_day , '\n')
    # display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    Pop_hour=df['hour'].mode()[0]
    print('The most common start hour is:', Pop_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Pop_Start = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ',Pop_Start , '\n')


    # display most commonly used end station
    Pop_End = df['End Station'].mode()[0]
    print('The most commonly used end station is: ',Pop_End, '\n')
    
    # display most frequent combination of start station and end station trip
    df['Combination']=df['Start Station'] + df['End Station']
    Pop_combine=df['Combination'].mode()[0]
    print("The most common combination of start station and end station is: ", Pop_combine , '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tot_time=df['Trip Duration'].sum()
    print("The total travel time is: ", tot_time ,'\n')

    # display mean travel time
    mean_time=df['Trip Duration'].mean()
    print("The mean travel time is: ", mean_time , '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df , city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types=df['User Type'].value.counts()
    print(user_types)
    # Display counts of gender
    if city=='Chicago' or city=='new york city':
        gender_type=df['Gender'].value.counts()
        print(gender_type)
        # Display earliest, most recent, and most common year of birth
        earliest=df['Birth Year'].min()
        print("The earliest year is: ", earliest ,'\n')
        most_recent=df['Birth Year'].max()
        print("The most recent year is: ", most_recent ,'\n')
        Pop_year=df['Birth Year'].mode()[0]
        print("The most common year is: ", Pop_year ,'\n')
    else:
        print("There's no information about gender or birth year in this city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    print(df.head())
    i = 0
    while True:
        answer = input("'\Do you want to view another five row (yes or no)?").lower()
        if answer != 'yes':
            return
        i += 5
        print(df.iloc[i:i+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            answer = input(" Do you want to view first five row (yes or no)?").lower()
            if answer != 'yes':
                break
            display_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
