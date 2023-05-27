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
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= input("please enter the name of the state, chicago , new york city ,washington:" ).lower()
    while city not in ["chicago","new york city","washington"]:
        print("invalid country name input")
        city = input("please enter the name of the state, chicago , new york city ,washington:" ).lower()
    print("the city is " + city)
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month= input("please enter the month: january to june or type all: ").lower()
    while month not in ["all","january","february","march","april","may","june"]:
        print("invalid month input")
        month= input("please enter the month: january to june or    type all: ").lower()
    print("the choosen month is:"+ month)
        
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("please specify the day:").lower()
    while day not in ["monday","tuesday","wednsday","thursday","friday","sunday"]:
          print("invalid day")
          day = input("please specify the day").lower()
    print("specified day is :" + day)

    


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
    read_file= CITY_DATA.get(city)    
    df=pd.read_csv(read_file)
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"]=df["Start Time"].dt.month
    df["day_of_week"]=df["Start Time"].dt.day_name
    df["start hour"]=df["Start Time"].dt.hour
    
    if month != "all":
        df["month"]=month
        
    if day != "all":
        df["day_of_week"]=day
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    print("Most common month is: ", (df['month'].mode()))
    
    
    # TO DO: display the most common day of week
    print("Most common day of the week: ", (df["day_of_week"].mode()))
    
    
    # TO DO: display the most common start hour
    print("most common hour: ",df["start hour"].mode())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    l=df["Start Station"].mode()
    print("Most commonly used start staion: " + l)

    # TO DO: display most commonly used end station
    n=df["End Station"].mode()
    print("most commonly used end station: " + n)

    # TO DO: display most frequent combination of start station and end station trip
    df["Start to End"] = df["Start Station"] + df["End Station"]
    print("Most frequent combinaion between start and stop: ",df["Start to End"].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    print("Total arrive time in seconds: " ,(df["Trip Duration"].sum()).round())
    
    # TO DO: display mean travel time
    
    print("mean travel time in seconds: " ,(df["Trip Duration"].mean()).round())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user type: ", (df["User Type"].value_counts()))

    # TO DO: Display counts of gender
    try:
        print("counts of genders: " ,(df["Gender"].value_counts()))
        
    except:
        print("No specified gender")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("earliest year of birth: ",int(df["Birth Year"].min()))
        print("earliest year of birth: ",int(df["Birth Year"].max()))
        print("most year of birth: ",int(df["Birth Year"].mode()))
        
    except:
        print("No specififed gender")
        print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   

def display_row_data(df):
    i = 0
    raw = input("Would you like to see row data? if yes press yes: ").lower()
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            print("Thank you")
            break
        elif raw == 'yes':
            print(df[i:i+5]) 
            raw = input("would u like to see more 5 rows?: ") 
            i += 5
        else:
            raw = input("Your input is invalid. Please enter only 'yes' or 'no: ").lower()

    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
