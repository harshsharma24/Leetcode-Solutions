from datetime import date,timedelta
map={}

def add_movie(date, name):
    if date  in map:
        map[date].append(name)
    else:
        map[date]= [name]

def find_movie(input_date):
    if input_date in map:
        return map[input_date]
    
    closestDate=None
    min_diff= timedelta.max
    
    for date in map:
        diff= (abs(input_date-date))
        if diff < min_diff:
            min_diff=diff
            closestDate=date     
        
        elif  diff==min_diff and date>closestDate:
            closestDate=date

    return map[closestDate]

add_movie(date(1972,3,14),"The Godfather")
add_movie(date(1972,3,16),"Lagaan")
add_movie(date(1995, 6, 30), "Apollo 13")
add_movie(date(1995, 6, 30), "Rocky")
add_movie(date(1985, 7, 3), "Back to the Future")

print("*******")
print(find_movie(date(1985, 7, 3)))
print(find_movie(date(1972, 3, 15)))



