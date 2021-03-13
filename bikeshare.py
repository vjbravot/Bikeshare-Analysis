import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city_list = ['Chicago', 'New York City', 'Washington']
    month_list = ['January','February','March','April','June','July','All']
    day_list = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']
    city = ''
    month = ''
    day = ''
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in city_list:
        city = input('Enter a valid city\n').title()

    # TO DO: get user input for month (all, january, february, ... , june)
    while month not in month_list:
        month = input('Enter a valid month (from january to june), type all for aggregated information\n').title()
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in day_list:
        day = input('Enter a valid weekday, type all for aggregated information\n').title()

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
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.day_name()

    if month != 'All':
        df = df[df['month'] == month]
        
    if day != 'All':
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is {}'.format(df['month'].value_counts().idxmax()))

    # TO DO: display the most common day of week
    print('The most common day of week is {}'.format(df['day'].value_counts().idxmax()))

    # TO DO: display the most common start hour
    print('The most common start hour is {}'.format(df['Start Time'].dt.hour.value_counts().idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is {}'.format(df['Start Station'].value_counts().idxmax()))

    # TO DO: display most commonly used end station
    print('The most commonly used end station is {}'.format(df['End Station'].value_counts().idxmax()))

    # TO DO: display most frequent combination of start station and end station trip
    df['Combinated Station'] = df['Start Station'] + "-" + df['End Station']
    print('The most frequent combination of start station and end station is {}'.format(df['Combinated Station'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is {} seconds'.format(np.sum(df['Trip Duration'])))

    # TO DO: display mean travel time
    print('The mean travel time is {} seconds'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The count for each user type is:\n{}'.format(df['User Type'].value_counts().to_string()))

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        print('The count for each gender is:\n{}'.format(df['Gender'].value_counts().to_string()))

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print('The earliest year of birth is {}'.format(int(df['Birth Year'].min())))
        print('The most recent year of birth is {}'.format(int(df['Birth Year'].max())))
        print('The most common year of birth is {}'.format(int(df['Birth Year'].value_counts().idxmax())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_count = 0
        df.drop(columns = ["month","day","Combinated Station"], inplace = True)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)        
        while input('\nWould you like to see individual information? Enter yes or no.\n').lower() == "yes":
            if raw_data_count+5 <= len(df.index):
                print(df[raw_data_count:raw_data_count + 5])
                raw_data_count += 5
            else:
                print(df[raw_data_count:len(df)])
                print("You reached the last line of the dataset")
                break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
