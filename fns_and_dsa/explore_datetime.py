from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date():
    """
    Prompts user for number of days, calculates future date, and prints it.
    """
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        formatted_future = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future}")
        return future_date
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None

def main():
    """
    Main function to run the datetime exploration script.
    """
    # Part 1: Display current date and time
    display_current_datetime()
    
    # Part 2: Calculate and display future date
    calculate_future_date()

if __name__ == "__main__":
    main()
