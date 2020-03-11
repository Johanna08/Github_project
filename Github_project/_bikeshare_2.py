import time
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington', 'all']
months = ['january','february','march','april','may','june','july','august','september','october','november','december', 'all']
days =['1','2','3','4','5','6','7', 'all']

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    city = input('name the city you would like to have a look at: ').lower()

    while  city not in CITY_DATA[city]:
        city = input('city name not valid, please enter another city: ').lower()

    month = input('please enter the month you would like to look at (or all, if you wish to have a look at all months): ')
    while month not in months:
        month = input('no valid name of month, please enter another month: ')

    day = input('please enter the day (numbers from 1  to 7 or all, if you wish to have a look at every day): ')
    while day not in days:
        day = input('no valid number, please enter another value: ')
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
        df - pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].apply(lambda x: x.hour)


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month =  months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df





def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]

    print('Most Frequent Start Month:', popular_month)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]

    print('Most Frequent Start Day of week:', popular_day_of_week)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # display the most common start hour

    popular_hour = df['hour'].mode()[0]

    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most common Start station:', start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most common End station:', end_station)

    # display most frequent combination of start station and end station trip
    df['Start - End'] = df['Start Station'] + "-" + df['End Station']
    start_end = df['Start - End'].mode()[0]
    print('Most common combination of Start and End station:', start_end)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('the total travel time:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('the mean travel time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of user types', user_types)


    # Display counts of gender
    try:
        genders = df['Gender'].value_counts()
        print('Count of Gender:', genders)

        print()
    except KeyError:
        print("There isn't a [Gender] column in this spreedsheet!")


    # Display earliest, most recent, and most common year of birth
    min = df['Birth Year'].min()
    print('earliest year of birth', min)
    max= df['Birth Year'].max()
    print('earliest year of birth', max)
    most_common = df['Birth Year'].mode()[0]
    print('Most common year of birth', most_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

yes = ['yes']
no = ['no']

def get_raw_data(df):
    start_line = 0
    end_line = 5
    raw_data = input('Do you want to see 5 lines of the raw data?').lower()

    if raw_data in yes:
        while end_line < df.shape[0]:
            print(df.iloc[start_line:end_line])
            start_line += 5
            end_line+=5
            continue_raw_data = input('Do you want to continue?').lower()
            if raw_data in no:
                break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
