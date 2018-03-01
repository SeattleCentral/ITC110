# Transportation decision maker


def how_to_travel(weather='Good', time=15, money=20.00, rush_hour=True):
    if weather == 'Bad' or (time >= 45 and money > 10.00 and rush_hour):
        return 'Train'
    elif weather == 'Good' and time <= 45 or money < 10.00 and not rush_hour:
        return 'Car'
    else:
        return 'Bus'


print('I am thinking about taking the bus.....')
travel_method = how_to_travel(
    weather='Good',
    time=45,
    money=5.00,
    rush_hour=True
)
print('Survey says, take the:', travel_method)

print('I think I want to take the train......')
travel_method = how_to_travel(
    weather='Good',
    time=45,
    money=25.00,
    rush_hour=True
)
print('Survey says, take the:', travel_method)

print('Maybe I want to drive today....')
travel_method = how_to_travel(
    weather='Good',
    time=30,
    money=25.00,
    rush_hour=True
)
print('Survey says, take the:', travel_method)
