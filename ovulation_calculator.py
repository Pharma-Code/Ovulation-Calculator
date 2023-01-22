import sys
import os
import datetime

def main():
    #Display Title and Instructions
    print("Ovulation Calculator")
    print("Input the first date of last menstrual period and cycle length to get the ovulation date")

    #Receive Inputs
    lmp = input("First Date of Last Menstrual Period (dd/mm/yyyy): ")
    cycle = input("Length of Menstrual Cycle (Days): ")

    lmp = convert_to_date(lmp)
    cycle = convert_to_int(cycle)

    #Calculate Ovulation Date
    ovulation_date = calculate_ovulation_date(lmp, cycle)
    print("Ovulation Date: " + ovulation_date.strftime("%d/%m/%Y"))

    #Prevent Script from Closing
    os.system("PAUSE")

def convert_to_date(value):
    try:
        return datetime.datetime.strptime(value, "%d/%m/%Y")
    except:
        print("Invalid date. Please, input the date in the correct format.")
        sys.exit()

def convert_to_int(value):
    try:
        return int(value)
    except:
        print("Invalid input. Please, input a valid number of days.")
        sys.exit()

def calculate_ovulation_date(lmp, cycle):
    estimated_ovulation_day = cycle - 14
    ovulation_day = datetime.timedelta(days = estimated_ovulation_day)
    ovulation_date = lmp + ovulation_day
    return ovulation_date

if __name__ == "__main__":
    main()
