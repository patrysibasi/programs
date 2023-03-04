import numpy as np
import re
from datetime import date

'''
Program was design as tool to determine applicant credit score and, if all requariments were met, present available mortgage ammount.
'''

contract_list = ["contract of employment", "mandate contract", "contract of enterprise", "b2b contract", "own company", "none"]

def main():
    '''
    Assigns name, surname, email and availabe_mortgage variables to corresponding function get.
    Prints final message to the user.

    '''
    name, surname = get_person()
    available_mortgage = a_mortgage()
    email = get_email()
    today = date.today()
    if available_mortgage:
        print(f"Available mortgage for {name} {surname} is: {available_mortgage}. Send offer to {email}. Date of request: {today}")
    else:
        print(f"Applicant does not qualify for a mortgage.\nApplicant age must be at least 18 years old and no older than 66.\nApplicant must have any valid contract, 'none' disqualifies mortgage application.\nIncome must be equal or greater than 18 000 a year.\nDuration of your employment must be more than 1 month from start date to date of the request.\nTermination date of your contract must be at least 7 months from date of the request.\nSend reply to {email}")

def get_person():
    ''' Prompts user for a applicant name and surname and then returns name and surname variables.'''
    while True:
        try:
            name = input("Name: ").capitalize().strip()
            surname = input("Surname: ").capitalize().strip()
            return name, surname
        except:
            pass

def get_email():
    ''' Prompts user for a applicant email address and then returns email variable.
        Validates email by using RE library
    '''
    while True:
        email = input("email address: ").lower().strip()
        email_pattern = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])"
        if re.match(email_pattern, email):
            return email


def get_age():
    ''' Prompts user for a applicant age and then returns age variable.'''
    while True:
        try:
            age = float(input("Age: "))
            if age >= 1:
                return age
            else:
                print("Invalid number")
        except ValueError:
            print("Age must be a number.")


def get_income():
    ''' Prompts user for a applicant income and then returns income variable.'''
    while True:
        try:
            income = float(input("Income by year, in thousands: "))
            if income >= 1:
                return income
            else:
                print("Income must be a positive number.")
        except ValueError:
            print("Income must be a number, without any spacing or symbols or commas: for example 49000")

def get_contract():
    global contract_list
    while True:
        try:
            contract = input(f"Choose from the list: {contract_list}\nContact type: ").lower().strip()
            if contract in contract_list:
                return contract
            else:
                print("Contract must be in a list presented above")
        except ValueError:
            print("Invalid contract, please select contract from one in a list above")

def calculate_age_factor(age):
    ''' Takes age variable and returns corresponding factor as a integer '''
    if 1 <= age <= 101:
        if age < 18:
            return False
        if 18 <= age <= 21:
            factor_age = 3
            return factor_age
        if 22 <= age <= 35:
            factor_age = 10
            return factor_age
        if 36 <= age <= 45:
            factor_age = 8
            return factor_age
        if 46 <= age <= 55:
            factor_age = 7
            return factor_age
        if 56 <= age <= 65:
            factor_age = 4
            return factor_age
        if age >= 66:
            return False
    else:
        return False

def calculate_income_factor(income):
    ''' Takes income variable and returns corresponding factor as a integer '''
    if income <= 18000:
        return False
    if 19000 <= income <= 25000:
        factor_income = 3
        return factor_income
    if 26000 <= income <= 35000:
        factor_income = 5
        return factor_income
    if 36000 <= income <= 45000:
        factor_income = 7
        return factor_income
    if 46000 <= income <= 60000:
        factor_income = 8
        return factor_income
    if 61000 <= income <= 80000:
        factor_income = 9
        return factor_income
    if 81000 <= income <= 1000000:
        factor_income = 10
        return factor_income
    if 1000001 <= income:
        factor_income = 10
        return factor_income

def calculate_contract_factor(contract):
    ''' Takes contract variable and returns corresponding factor as a integer '''
    if contract == "contract of employment":
        factor_contract = 10
        return factor_contract
    if contract == "mandate contract":
        factor_contract = 3
        return factor_contract
    if contract == "contract of enterprise":
        factor_contract = 1
        return factor_contract
    if contract == "b2b contract":
        factor_contract = 6
        return factor_contract
    if contract == "own company":
        factor_contract = 5
        return factor_contract
    if contract == "none":
        return False

def contract_type_period(contract):
    ''' Takes contract variable and returns 2 corresponding variables: duration and end_time '''
    while True:
        try:
            if contract == "contract of employment":
                duration = float(input("For how long you are employed by your current employer (in months): "))
                end_time = float(input("The time remaining to the termination of your contract (in months, if unterminated enter '100'): "))
                if duration >= 0 and end_time >= 0:
                    return duration, end_time
                else:
                    print("Both values must be a positive numbers")
            if contract == "mandate contract":
                duration = float(input("For how long you are employed by your current employer (in months): "))
                end_time = float(input("The time remaining to the termination of your contract (in months, if unterminated enter '100'): "))
                if duration >= 0 and end_time >= 0:
                    return duration, end_time
                else:
                    print("Both values must be a positive numbers")
            if contract == "contract of enterprise":
                duration = float(input("For how long you are working on a project for your current employer (in months): "))
                end_time = float(input("The time remaining to the end of your involvement within the project (in months, if unterminated enter '100'): "))
                if duration >= 0 and end_time >= 0:
                    return duration, end_time
                else:
                    print("Both values must be a positive numbers")
            if contract == "b2b contract":
                duration = float(input("For how long you are cooperating with the current company (in months): "))
                end_time = float(input("The time remaining to the termination of your cooperation (in months, if unterminated enter '100'): "))
                if duration >= 0 and end_time >= 0:
                    return duration, end_time
                else:
                    print("Both values must be a positive numbers")
            if contract == "own company":
                duration = float(input("For how long you own your current company (in months): "))
                end_time = 30
                if duration >= 0 and end_time >= 0:
                    return duration, end_time
                else:
                    print("Duration of your currect employment contract and period to termination date both must be a positive numbers - presented in X months")
        except ValueError:
            print("Duration of your currect employment contract and period to termination date both must be a positive number- presented in X months")


def contract_duration(duration):
    ''' Takes duration variable, which is connected to contract type, and returns corresponding factor as a integer '''
    if duration <= 1:
        return False
    if 2 <= duration <= 6:
        factor_duration = 1
        return factor_duration
    if 7 <= duration <= 10:
        factor_duration = 3
        return factor_duration
    if 11 <= duration <= 12:
        factor_duration = 4
        return factor_duration
    if 13 <= duration <= 18:
        factor_duration = 5
        return factor_duration
    if 19 <= duration <= 24:
        factor_duration = 6
        return factor_duration
    if 25 <= duration <= 30:
        factor_duration = 8
        return factor_duration
    if 31 <= duration:
        factor_duration = 10
        return factor_duration

def contract_end_time(end_time):
    ''' Takes end_time variable, which is connected to contract type, and returns corresponding factor as a integer '''
    if end_time == 100:
        factor_end_time = 12
        return end_time
    if 0 <= end_time <= 6:
        return False
    if 7 <= end_time <= 12:
        factor_end_time = 1
        return factor_end_time
    if 12 <= end_time <= 18:
        factor_end_time = 2
        return factor_end_time
    if 19 <= end_time <= 24:
        factor_end_time = 4
        return factor_end_time
    if 25 <= end_time <= 30:
        factor_end_time = 6
        return factor_end_time
    if 31 <= end_time <= 36:
        factor_end_time = 8
        return factor_end_time
    if 37 <= end_time <= 99:
        factor_end_time = 10
        return factor_end_time

def a_mortgage():
    ''' Assigns age, income, contract variables to corresponding functions get_...().
        Assigns factors variables to corresponding functions.
        Gathers all factors in a list, and calculates mean of fators sum by using numpy library.
        Calculates final value of a available mortage by multiplying income and factor's mean.
        Returns the final, calculated value.
        Returns False, if mortgage criteria were not met.
    '''
    age = get_age()
    income = get_income()
    contract = get_contract()
    if calculate_contract_factor(contract) != False:
        duration, end_time = contract_type_period(contract)
        factor_end_time = contract_end_time(end_time)
        factor_duration = contract_duration(duration)
        factor_age = calculate_age_factor(age)
        factor_income = calculate_income_factor(income)
        factor_contract = calculate_contract_factor(contract)
        if factor_age and factor_income and factor_contract and factor_duration and factor_end_time:
            factor_list = [factor_age, factor_income, factor_contract, factor_duration, factor_end_time]
            factor = np.mean(factor_list)
            available_mortgage = income * factor
            return f"{available_mortgage:,.0f}"
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
