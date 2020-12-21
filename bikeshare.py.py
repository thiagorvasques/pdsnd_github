import time
import pandas as pd
import numpy as np
import calendar as calendar
import datetime

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
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Select a city: Chicago, New York or Washington:\n").lower()
    while city not in CITY_DATA.keys():
        city = input("Please, select a valid city.\n")
   
    # get user input for month (all, january, february, ... , june)
    month = input("Select a month from January to June or 'all':\n").lower()
    months = ("january","february", "march", "april", "may", "june", "all")
    while month not in months:
        month = input("Please, select a valid month.\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Select a day of the week or 'all':\n").lower()
    week_list = ("monday", "tuesday", "wednesday","thursday", "friday", "saturday", "sunday", "all")
    while day not in  week_list:
        day = input("Please select a valid day.\n")
        
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
    # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]
    
    #print(df.head())
    return df
        

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    month_count = df['month'].mode()[0]
    month_count = calendar.month_name[month_count]
    print("The most commom month is {}\n".format(month_count))
    # display the most common day of week
    week_day = df['day'].mode()[0]
    print("The most common day of the week is {}\n".format(week_day))
    
    # display the most common start hour
    start_hour = df['hour'].mode()[0]
    print("The most common start hour is {}:00\n".format(start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_stt = df['Start Station'].mode()[0]
    print("The most commonly used start station is {}\n".format(start_stt))

    # display most commonly used end station
    end_stt = df['End Station'].mode()[0]
    print("The most commonly used end station is {}\n".format(end_stt))

    # display most frequent combination of start station and end station trip
    frequent_comb = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("The most frequent combinatio of start and end station is:\n{}".format(frequent_comb))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = int(df['Trip Duration'].sum())
    total_time = str(datetime.timedelta(seconds = total_time))
    print("The total travel time is {}\n".format(total_time))
    # display mean travel time
    mean_time = int(df['Trip Duration'].mean())
    mean_time = str(datetime.timedelta(seconds = mean_time))
    print("The mean travel time is {}\n".format(mean_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print("Count of user by type:\n{}".format(user_type))
    # Display counts of gender
    gender = df['Gender'].value_counts()
    print('Count of users by gender:\n{}'.format(gender))

    # Display earliest, most recent, and most common year of birth
    common_birth = df['Birth Year'].mode()[0]
    recent_birth = df['Birth Year'].max()
    earliest_birth = df['Birth Year'].min()
    print('The most common year of birth is {}\n'.format(int(common_birth)))
    print('The most recent year of birth is {}\n'.format(int(recent_birth)))
    print('The earliest year of birth is {}\n'.format(int(earliest_birth)))
    
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(df):
  
    #Asks user if they want to see 5 lines of raw data.
    #Returns the 5 lines of raw data if user inputs `yes`. Iterate until user response with a `no`

    

    data = 0

    while True:
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        if answer.lower() == 'yes':
            print(df[data : data+5])
            data += 5

        else:
            break
              
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
