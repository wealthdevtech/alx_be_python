from datetime import datetime, timedelta

def display_current_datetime():
    current_date_raw = datetime.now()
    current_date = current_date_raw.strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)
    
    def calculate_future_date():
        user_input = int(input("Enter the number of days to add to the current date: "))
        future_date_raw = timedelta(days=user_input)
        future_date = current_date_raw + future_date_raw
        future_date = future_date.strftime("%Y-%m-%d")
    
    calculate_future_date()
    
def main():
    while True:
        display_current_datetime()
        exit = input("Type 'exit' to break loop.")
        if exit == "exit":
            print("Goodbye!")
            break
    
main()