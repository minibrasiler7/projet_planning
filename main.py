import datetime

result_planning = {}

jours_choisi = input("Quels jours voulez-vous travailler dans la semaine? mettre un espace entre les jours : ")

tab_jours = jours_choisi.split(" ")

boolean_regulier = input("Souhaitez-vous le même horaire tous les jours?")


def add_delta_time(time, delta):
    return (datetime.datetime.combine(datetime.date(1, 1, 1), time) + delta).time()


if boolean_regulier == "oui":
    pause_delta_tab = []
    debut = input("A quelle heure souhaitez-vous commencer? : ")
    fin = input("À quelle heure souhaité vous terminer? au plus tard ? : ")
    duree_periode = input("Quelle est la durée d'une période en minutes? : ")
    periode_delta = datetime.timedelta(minutes=int(duree_periode))
    debut_converti = debut.split("h")
    fin_converti = fin.split("h")
    debut_converti = [int(x) for x in debut_converti]
    fin_converti = [int(x) for x in fin_converti]

    time_debut = datetime.time(hour=debut_converti[0], minute=debut_converti[1])
    time_fin = datetime.time(hour=fin_converti[0], minute=fin_converti[1])
    current_time = time_debut

    for jour in tab_jours:
        result_planning[jour] = []
        periode = 0
        while add_delta_time(current_time, periode_delta) < time_fin:
            result_planning[jour].append([current_time, add_delta_time(current_time, periode_delta)])
            current_time = add_delta_time(current_time, periode_delta)
            if jour == tab_jours[0] and add_delta_time(current_time, periode_delta) < time_fin:
                pause = int(input(
                    f"Souhaitez-vous une pause à {current_time} après la période {periode + 1}? entrer un nombre de minutes: "))
                pause_delta = datetime.timedelta(minutes=pause)
                pause_delta_tab.append(pause_delta)
                current_time = add_delta_time(current_time, pause_delta)
                periode += 1
            elif jour != tab_jours[0]:
                current_time = add_delta_time(current_time, pause_delta_tab[periode])
                periode += 1
            print(current_time)

        current_time = time_debut

print(result_planning)
