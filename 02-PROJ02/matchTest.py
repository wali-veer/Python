def special_of_the_day(day):
    match(day):
        case 'Monday':
            return 'Shiva'
        case 'Tuesday':
            return 'Gowri Ma'
        case 'Wednesday':
            return 'Ganesha'
        case 'Thursday':
            return 'GuruDeva'
        case 'Friday':
            return 'Lakshmi Ma'
        case 'Saturday':
            return 'Hanuman'
        case _:     
            return 'no special day'
        
today = 'Monday'
print(f'Today is {today} and it is special for {special_of_the_day(today)} ')

today = 'Sunday'
print(f'Today is {today} and it is special for {special_of_the_day(today)} ')