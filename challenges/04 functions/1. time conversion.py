# Stwórz funkcję do konwersji czasu:
# 1) convertToSeconds przyjmującą ilość godzin
#    oraz minut i zwracająca ilość sekund.
#    Jako parametry funkcji zapisz: hours, minutes.
#    Skonwertuj 3 godziny i 25 minut na sekundy,
#    wynik pokaż w konsoli.
# 2) convertToHours przyjmującą parametr minutes
#    oraz zwracając ilość godzin.
#    Skonwertuj 120 minut na godziny i pokaż
#    wynik w konsoli.

def convertToSeconds(hours, minutes):
    if hours <= 0 or minutes <= 0:
        print("Liczba musi być dodatnia!")
        return

    if minutes > 60:
        print("Minuty, nie mogą przekraczać 60, ponieważ to liczy się jako godzina!")
        return

    print(hours, " Godziny")
    print(minutes, " Minut")

    minutesOverall = (hours * 60) + minutes

    print(minutesOverall, " Łącznie minut")

    seconds = minutesOverall * 60

    print(seconds, " Sekund")
    return seconds

convertToSeconds(3, 25)

def convertToHours(minutes):

    if minutes <= 0:
        print("Liczba musi być dodatnia!")
        return

    hours = int(minutes) / 60

    if hours == 1:
        print(minutes, "Minut to ", hours, "godzina")
    elif hours > 1 and hours <= 4:
        print(minutes, "Minut to ", hours, "godziny")
    else:
        print(minutes, "Minut to ", hours, "godzin")

convertToHours(120)