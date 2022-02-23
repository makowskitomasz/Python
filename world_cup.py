import random
import tkinter as tk


def winner(team1, team2, team3, team4):
    if team1.points == 9 or (team1.points == 6 and team2.points < 7 and team3.points < 7 and team4.points < 7):
        return team1
    elif team2.points == 9 or (team2.points == 6 and team1.points < 6 and team3.points < 7 and team4.points < 7):
        return team2
    elif team3.points == 9 or (team3.points == 6 and team1.points < 6 and team2.points < 6 and team4.points < 7):
        return team3
    else:
        return team4


def runner_up(team1, team2, team3, team4):
    if team1.points == 9 or (team1.points == 6 and team2.points < 7 and team3.points < 7 and team4.points < 7):
        if team2.points == 6 or (team2.points == 3 and team3.points < 4 and team4.points < 4):
            return team2
        elif team3.points == 6 or (team3.points == 3 and team2.points < 3 and team4.points < 4):
            return team3
        else:
            return team4
    elif team2.points == 9 or (team2.points == 6 and team1.points < 6 and team3.points < 7 and team4.points < 7):
        if team1.points == 6 or (team1.points == 3 and team3.points < 4 and team4.points < 4):
            return team1
        elif team3.points == 6 or (team3.points == 3 and team1.points < 3 and team4.points < 4):
            return team3
        else:
            return team4
    elif team3.points == 9 or (team3.points == 6 and team1.points < 6 and team2.points < 6 and team4.points < 7):
        if team1.points == 6 or (team1.points == 3 and team2.points < 4 and team4.points < 4):
            return team1
        elif team2.points == 6 or (team2.points == 3 and team1.points < 3 and team4.points < 4):
            return team2
        else:
            return team4
    else:
        if team1.points == 6 or (team1.points == 3 and team2.points < 4 and team3.points < 4):
            return team1
        elif team2.points == 6 or (team2.points == 3 and team1.points < 3 and team3.points < 4):
            return team2
        else:
            return team3


def check():
    if (a_simulation['state'] == tk.DISABLED and a_drawing['state'] == tk.DISABLED and a_results['state']
        == tk.DISABLED) and b_simulation['state'] == tk.DISABLED and b_drawing['state']\
            == tk.DISABLED and b_results['state'] == tk.DISABLED and c_simulation['state'] \
            == tk.DISABLED and c_drawing['state'] == tk.DISABLED and c_results['state']\
            == tk.DISABLED and d_simulation['state'] == tk.DISABLED and d_drawing['state']\
            == tk.DISABLED and d_results['state'] == tk.DISABLED and e_simulation['state']\
            == tk.DISABLED and e_drawing['state'] == tk.DISABLED and e_results['state']\
            == tk.DISABLED and f_simulation['state'] == tk.DISABLED and f_drawing['state']\
            == tk.DISABLED and f_results['state'] == tk.DISABLED and g_simulation['state']\
            == tk.DISABLED and g_drawing['state'] == tk.DISABLED and g_results['state']\
            == tk.DISABLED and h_simulation['state'] == tk.DISABLED and h_drawing['state']\
            == tk.DISABLED and h_results['state'] == tk.DISABLED:
        eights_show.config(state="normal")


def algorithm(team1, team2):
    counter = team1.rank + team2.rank
    factor = random.random()
    if team1.rank > team2.rank:
        if factor < team1.rank/counter:
            return team2
        else:
            return team1
    else:
        if factor > team1.rank/counter:
            return team1
        else:
            return team2


def match(team1, team2):
    if algorithm(team1, team2) == team1:
        team1.points += 3
    else:
        team2.points += 3


def simulation(team1, team2, team3, team4):
    match(team1, team2)
    match(team3, team4)
    match(team1, team3)
    match(team2, team4)
    match(team1, team4)
    match(team2, team3)


def a_result(team1, team2, team3, team4):
    advanced[0] = winner(team1, team2, team3, team4)
    advanced[8] = runner_up(team1, team2, team3, team4)
    group_a = tk.Label(gui, text=f"Group A\n1. {team1.name} {team1.points}\n2. {team2.name} {team2.points}\n"
                                 f"3. {team3.name} {team3.points}\n4. {team4.name} {team4.points}\n\n Final standings: "
                                 f"\n1) {advanced[0].name}\n2) {advanced[8].name}")
    group_a.place(x=500, y=15)
    a_results.config(state="disabled")
    check()


def a_simulate(team1, team2, team3, team4):
    simulation(team1, team2, team3, team4)
    a_simulation.config(state="disabled")
    a_results.config(state="normal")


def b_result(team1, team2, team3, team4):
    advanced[9] = winner(team1, team2, team3, team4)
    advanced[1] = runner_up(team1, team2, team3, team4)
    group_b = tk.Label(gui, text=f"Group B\n1. {team1.name} {team1.points}\n2. {team2.name} {team2.points}\n"
                                 f"3. {team3.name} {team3.points}\n4. {team4.name} {team4.points}\n\n Final standings: "
                                 f"\n1) {advanced[9].name}\n2) {advanced[1].name}")
    group_b.place(x=640, y=15)
    b_results.config(state="disabled")
    check()


def b_simulate(team1, team2, team3, team4):
    simulation(team1, team2, team3, team4)
    b_simulation.config(state="disabled")
    b_results.config(state="normal")


def c_result(team1, team2, team3, team4):
    advanced[2] = winner(team1, team2, team3, team4)
    advanced[10] = runner_up(team1, team2, team3, team4)
    group_c = tk.Label(gui, text=f"Group C\n1. {team1.name} {team1.points}\n2. {team2.name} {team2.points}\n"
                                 f"3. {team3.name} {team3.points}\n4. {team4.name} {team4.points}\n\n Final standings: "
                                 f"\n1) {advanced[2].name}\n2) {advanced[10].name}")
    group_c.place(x=780, y=15)
    c_results.config(state="disabled")
    check()


def c_simulate(team1, team2, team3, team4):
    simulation(team1, team2, team3, team4)
    c_simulation.config(state="disabled")
    c_results.config(state="normal")


def d_result(team1, team2, team3, team4):
    advanced[11] = winner(team1, team2, team3, team4)
    advanced[3] = runner_up(team1, team2, team3, team4)
    group_d = tk.Label(gui, text=f"Group D\n1. {team1.name} {team1.points}\n2. {team2.name} {team2.points}\n"
                                 f"3. {team3.name} {team3.points}\n4. {team4.name} {team4.points}\n\n Final standings: "
                                 f"\n1) {advanced[11].name}\n2) {advanced[3].name}")
    group_d.place(x=920, y=15)
    d_results.config(state="disabled")
    check()


def d_simulate(team1, team2, team3, team4):
    simulation(team1, team2, team3, team4)
    d_simulation.config(state="disabled")
    d_results.config(state="normal")


def e_result(team1, team2, team3, team4):
    advanced[4] = winner(team1, team2, team3, team4)
    advanced[12] = runner_up(team1, team2, team3, team4)
    group_e = tk.Label(gui, text=f"Group E\n1. {team1.name} {team1.points}\n2. {team2.name} {team2.points}\n"
                                 f"3. {team3.name} {team3.points}\n4. {team4.name} {team4.points}\n\n Final standings: "
                                 f"\n1) {advanced[4].name}\n2) {advanced[12].name}")
    group_e.place(x=1060, y=15)
    e_results.config(state="disabled")
    check()


def e_simulate(team1, team2, team3, team4):
    simulation(team1, team2, team3, team4)
    e_simulation.config(state="disabled")
    e_results.config(state="normal")


def f_result(team1, team2, team3, team4):
    advanced[13] = winner(team1, team2, team3, team4)
    advanced[5] = runner_up(team1, team2, team3, team4)
    group_f = tk.Label(gui, text=f"Group F\n1. {team1.name} {team1.points}\n2. {team2.name} {team2.points}\n"
                                 f"3. {team3.name} {team3.points}\n4. {team4.name} {team4.points}\n\n Final standings: "
                                 f"\n1) {advanced[13].name}\n2) {advanced[5].name}")
    group_f.place(x=1200, y=15)
    f_results.config(state="disabled")
    check()


def f_simulate(team1, team2, team3, team4):
    simulation(team1, team2, team3, team4)
    f_simulation.config(state="disabled")
    f_results.config(state="normal")


def g_result(team1, team2, team3, team4):
    advanced[6] = winner(team1, team2, team3, team4)
    advanced[14] = runner_up(team1, team2, team3, team4)
    group_g = tk.Label(gui, text=f"Group G\n1. {team1.name} {team1.points}\n2. {team2.name} {team2.points}\n"
                                 f"3. {team3.name} {team3.points}\n4. {team4.name} {team4.points}\n\n Final standings: "
                                 f"\n1) {advanced[6].name}\n2) {advanced[14].name}")
    group_g.place(x=1340, y=15)
    g_results.config(state="disabled")
    check()


def g_simulate(team1, team2, team3, team4):
    simulation(team1, team2, team3, team4)
    g_simulation.config(state="disabled")
    g_results.config(state="normal")


def h_result(team1, team2, team3, team4):
    advanced[15] = winner(team1, team2, team3, team4)
    advanced[7] = runner_up(team1, team2, team3, team4)
    group_h = tk.Label(gui, text=f"Group H\n1. {team1.name} {team1.points}\n2. {team2.name} {team2.points}\n"
                                 f"3. {team3.name} {team3.points}\n4. {team4.name} {team4.points}\n\n Final standings: "
                                 f"\n1) {advanced[15].name}\n2) {advanced[7].name}")
    group_h.place(x=1480, y=15)
    h_results.config(state="disabled")
    check()


def h_simulate(team1, team2, team3, team4):
    simulation(team1, team2, team3, team4)
    h_simulation.config(state="disabled")
    h_results.config(state="normal")


def eights(tab):
    eights_1 = tk.Label(gui, text=f"{tab[0].name}\n{tab[1].name}")
    eights_1.place(x=600, y=200)
    eights_2 = tk.Label(gui, text=f"{tab[2].name}\n{tab[3].name}")
    eights_2.place(x=600, y=275)
    eights_3 = tk.Label(gui, text=f"{tab[4].name}\n{tab[5].name}")
    eights_3.place(x=600, y=350)
    eights_4 = tk.Label(gui, text=f"{tab[6].name}\n{tab[7].name}")
    eights_4.place(x=600, y=425)
    eights_5 = tk.Label(gui, text=f"{tab[8].name}\n{tab[9].name}")
    eights_5.place(x=600, y=500)
    eights_6 = tk.Label(gui, text=f"{tab[10].name}\n{tab[11].name}")
    eights_6.place(x=600, y=575)
    eights_7 = tk.Label(gui, text=f"{tab[12].name}\n{tab[13].name}")
    eights_7.place(x=600, y=650)
    eights_8 = tk.Label(gui, text=f"{tab[14].name}\n{tab[15].name}")
    eights_8.place(x=600, y=725)
    eights_show.config(state="disabled")
    eights_simulation.config(state="normal")


def eights_simulate(tab, tab2):
    tab2[0] = algorithm(tab[0], tab[1])
    tab2[1] = algorithm(tab[2], tab[3])
    tab2[2] = algorithm(tab[4], tab[5])
    tab2[3] = algorithm(tab[6], tab[7])
    tab2[4] = algorithm(tab[8], tab[9])
    tab2[5] = algorithm(tab[10], tab[11])
    tab2[6] = algorithm(tab[12], tab[13])
    tab2[7] = algorithm(tab[14], tab[15])
    eights_simulation.config(state="disabled")
    quarters_show.config(state="normal")


def quarter(tab):
    quarters_1 = tk.Label(gui, text=f"{tab[0].name}\n{tab[1].name}")
    quarters_1.place(x=800, y=237)
    quarters_2 = tk.Label(gui, text=f"{tab[2].name}\n{tab[3].name}")
    quarters_2.place(x=800, y=387)
    quarters_3 = tk.Label(gui, text=f"{tab[4].name}\n{tab[5].name}")
    quarters_3.place(x=800, y=533)
    quarters_4 = tk.Label(gui, text=f"{tab[6].name}\n{tab[7].name}")
    quarters_4.place(x=800, y=683)
    quarters_show.config(state="disabled")
    quarters_simulation.config(state="normal")


def quarters_simulate(tab, tab2):
    tab2[0] = algorithm(tab[0], tab[1])
    tab2[1] = algorithm(tab[2], tab[3])
    tab2[2] = algorithm(tab[4], tab[5])
    tab2[3] = algorithm(tab[6], tab[7])
    quarters_simulation.config(state="disabled")
    semis_show.config(state="normal")


def semi(tab):
    semis_1 = tk.Label(gui, text=f"{tab[0].name}\n{tab[1].name}")
    semis_1.place(x=1000, y=312)
    semis_2 = tk.Label(gui, text=f"{tab[2].name}\n{tab[3].name}")
    semis_2.place(x=1000, y=608)
    semis_show.config(state="disabled")
    semis_simulation.config(state="normal")


def semis_simulate(tab, tab2):
    tab2[0] = algorithm(tab[0], tab[1])
    if tab2[0] == tab[0]:
        tab2[2] = tab[1]
    else:
        tab2[2] = tab[0]
    tab2[1] = algorithm(tab[2], tab[3])
    if tab2[1] == tab[2]:
        tab2[3] = tab[3]
    else:
        tab2[3] = tab[2]
    semis_simulation.config(state="disabled")
    finals_show.config(state="normal")


def final(tab):
    big_final = tk.Label(gui, text=f"FINAL:\n{tab[0].name}\n{tab[1].name}", width="15", borderwidth="2",
                         relief="raised")
    big_final.place(x=1200, y=440)
    small_final = tk.Label(gui, text=f"SMALL FINAL:\n{tab[2].name}\n{tab[3].name}", width="15", borderwidth="2",
                           relief="raised")
    small_final.place(x=1200, y=640)
    finals_show.config(state="disabled")
    finals_simulation.config(state="normal")


def finals_simulate(tab, tab2):
    tab2[0] = algorithm(tab[0], tab[1])
    if tab2[0] == tab[0]:
        tab2[1] = tab[1]
    else:
        tab2[1] = tab[0]
    tab2[2] = algorithm(tab[2], tab[3])
    if tab2[2] == tab[2]:
        tab2[3] = tab[3]
    else:
        tab2[3] = tab[2]
    finals_simulation.config(state="disabled")
    final_results.config(state="normal")


def final_result(tab):
    results = tk.Label(gui, text=f"Winner: {tab[0].name}\nRunner-up: {tab[1].name}\nThird place: {tab[2].name}\n"
                                 f"Fourth place: {tab[3].name}", background="BLACK", foreground="WHITE", font=100)
    results.place(x=1400, y=460)
    final_results.config(state="disabled")


class Team:
    def __init__(self, name, rank, points):
        self.name = name
        self.rank = rank
        self.points = points


germany = Team("Germany", 1, 0)
brazil = Team("Brazil", 2, 0)
portugal = Team("Portugal", 3, 0)
argentina = Team("Argentina", 4, 0)
belgium = Team("Belgium", 5, 0)
poland = Team("Poland", 6, 0)
france = Team("France", 7, 0)
spain = Team("Spain", 8, 0)
peru = Team("Peru", 9, 0)
switzerland = Team("Switzerland", 10, 0)
england = Team("England", 11, 0)
columbia = Team("Columbia", 12, 0)
mexico = Team("Mexico", 13, 0)
uruguay = Team("Uruguay", 14, 0)
croatia = Team("Croatia", 15, 0)
denmark = Team("Denmark", 16, 0)
iceland = Team("Iceland", 17, 0)
costa_rica = Team("Costa Rica", 18, 0)
sweden = Team("Sweden", 19, 0)
tunisia = Team("Tunisia", 20, 0)
egypt = Team("Egypt", 21, 0)
senegal = Team("Senegal", 22, 0)
iran = Team("Iran", 23, 0)
serbia = Team("Serbia", 24, 0)
nigeria = Team("Nigeria", 25, 0)
australia = Team("Australia", 26, 0)
japan = Team("Japan", 27, 0)
morocco = Team("Morocco", 28, 0)
panama = Team("Panama", 29, 0)
south_korea = Team("South Korea", 30, 0)
saudi_arabia = Team("Saudi Arabia", 31, 0)
russia = Team("Russia", 32, 0)

pool1 = [germany, brazil, portugal, argentina, belgium, poland, france, spain]
pool2 = [peru, switzerland, england, columbia, mexico, uruguay, croatia, denmark]
pool3 = [iceland, costa_rica, sweden, tunisia, egypt, senegal, iran, serbia]
pool4 = [nigeria, australia, japan, morocco, panama, south_korea, saudi_arabia, russia]
a_teams = []
b_teams = []
c_teams = []
d_teams = []
e_teams = []
f_teams = []
g_teams = []
h_teams = []
advanced = [germany for i in range(16)]
quarters = [germany for a in range(8)]
semis = [germany for b in range(4)]
finals = [germany for c in range(4)]
standings = [germany for d in range(4)]

gui = tk.Tk()
gui.geometry("1660x800")
gui.title("World Cup 2018")

poolA = tk.Label(gui, text="This is pool 1\nGermany\nBrazil\nPortugal\nArgentina\nBelgium\nPoland\nFrance\nSpain")
poolA.place(x=5, y=15)
poolB = tk.Label(gui, text="This is pool 2\nPeru\nSwitzerland\nEngland\nColumbia\nMexico\nUruguay\nCroatia\nDenmark")
poolB.place(x=105, y=15)
poolC = tk.Label(gui, text="This is pool 3\nIceland\nCosta Rica\nSweden\nTunisia\nEgypt\nSenegal\nIran\nSerbia")
poolC.place(x=205, y=15)
poolD = tk.Label(gui, text="This is pool 4\nNigeria\nAustralia\nJapan\nMorocco\nPanama\nSouth Korea\nSaudi Arabia\n"
                           "Russia")
poolD.place(x=305, y=15)


def a_draw(tab1, tab2, tab3, tab4, tab5):
    first_a = random.choice(tab1)
    tab1.remove(first_a)
    tab5.append(first_a)
    second_a = random.choice(tab2)
    tab2.remove(second_a)
    tab5.append(second_a)
    third_a = random.choice(tab3)
    tab3.remove(third_a)
    tab5.append(third_a)
    fourth_a = random.choice(tab4)
    tab4.remove(fourth_a)
    tab5.append(fourth_a)
    a_drawing.config(state="disabled")
    a_simulation.config(state="normal")

    group_a = tk.Label(gui, text=f"Group A\n1. {first_a.name} {first_a.points}\n2. {second_a.name} {second_a.points}\n"
                                 f"3. {third_a.name} {third_a.points}\n4. {fourth_a.name} {fourth_a.points}\n\n")
    group_a.place(x=500, y=15)


def b_draw(tab1, tab2, tab3, tab4, tab5):
    first_b = random.choice(tab1)
    tab1.remove(first_b)
    tab5.append(first_b)
    second_b = random.choice(tab2)
    tab2.remove(second_b)
    tab5.append(second_b)
    third_b = random.choice(tab3)
    tab3.remove(third_b)
    tab5.append(third_b)
    fourth_b = random.choice(tab4)
    tab4.remove(fourth_b)
    tab5.append(fourth_b)
    b_drawing.config(state="disabled")
    b_simulation.config(state="normal")

    group_b = tk.Label(gui, text=f"Group B\n1. {first_b.name} {first_b.points}\n2. {second_b.name} {second_b.points}\n"
                                 f"3. {third_b.name} {third_b.points}\n4. {fourth_b.name} {fourth_b.points}\n\n")
    group_b.place(x=640, y=15)


def c_draw(tab1, tab2, tab3, tab4, tab5):
    first_c = random.choice(tab1)
    tab1.remove(first_c)
    tab5.append(first_c)
    second_c = random.choice(tab2)
    tab2.remove(second_c)
    tab5.append(second_c)
    third_c = random.choice(tab3)
    tab3.remove(third_c)
    tab5.append(third_c)
    fourth_c = random.choice(tab4)
    tab4.remove(fourth_c)
    tab5.append(fourth_c)
    c_drawing.config(state="disabled")
    c_simulation.config(state="normal")

    group_c = tk.Label(gui, text=f"Group C\n1. {first_c.name} {first_c.points}\n2. {second_c.name} {second_c.points}\n"
                                 f"3. {third_c.name} {third_c.points}\n4. {fourth_c.name} {fourth_c.points}\n\n")
    group_c.place(x=780, y=15)


def d_draw(tab1, tab2, tab3, tab4, tab5):
    first_d = random.choice(tab1)
    tab1.remove(first_d)
    tab5.append(first_d)
    second_d = random.choice(tab2)
    tab2.remove(second_d)
    tab5.append(second_d)
    third_d = random.choice(tab3)
    tab3.remove(third_d)
    tab5.append(third_d)
    fourth_d = random.choice(tab4)
    tab4.remove(fourth_d)
    tab5.append(fourth_d)
    d_drawing.config(state="disabled")
    d_simulation.config(state="normal")

    group_d = tk.Label(gui, text=f"Group D\n1. {first_d.name} {first_d.points}\n2. {second_d.name} {second_d.points}\n"
                                 f"3. {third_d.name} {third_d.points}\n4. {fourth_d.name} {fourth_d.points}\n\n")
    group_d.place(x=920, y=15)


def e_draw(tab1, tab2, tab3, tab4, tab5):
    first_e = random.choice(tab1)
    tab1.remove(first_e)
    tab5.append(first_e)
    second_e = random.choice(tab2)
    tab2.remove(second_e)
    tab5.append(second_e)
    third_e = random.choice(tab3)
    tab3.remove(third_e)
    tab5.append(third_e)
    fourth_e = random.choice(tab4)
    tab4.remove(fourth_e)
    tab5.append(fourth_e)
    e_drawing.config(state="disabled")
    e_simulation.config(state="normal")

    group_e = tk.Label(gui, text=f"Group E\n1. {first_e.name} {first_e.points}\n2. {second_e.name} {second_e.points}\n"
                                 f"3. {third_e.name} {third_e.points}\n4. {fourth_e.name} {fourth_e.points}\n\n")
    group_e.place(x=1060, y=15)


def f_draw(tab1, tab2, tab3, tab4, tab5):
    first_f = random.choice(tab1)
    tab1.remove(first_f)
    tab5.append(first_f)
    second_f = random.choice(tab2)
    tab2.remove(second_f)
    tab5.append(second_f)
    third_f = random.choice(tab3)
    tab3.remove(third_f)
    tab5.append(third_f)
    fourth_f = random.choice(tab4)
    tab4.remove(fourth_f)
    tab5.append(fourth_f)
    f_drawing.config(state="disabled")
    f_simulation.config(state="normal")

    group_f = tk.Label(gui, text=f"Group F\n1. {first_f.name} {first_f.points}\n2. {second_f.name} {second_f.points}\n"
                                 f"3. {third_f.name} {third_f.points}\n4. {fourth_f.name} {fourth_f.points}\n\n")
    group_f.place(x=1200, y=15)


def g_draw(tab1, tab2, tab3, tab4, tab5):
    first_g = random.choice(tab1)
    tab1.remove(first_g)
    tab5.append(first_g)
    second_g = random.choice(tab2)
    tab2.remove(second_g)
    tab5.append(second_g)
    third_g = random.choice(tab3)
    tab3.remove(third_g)
    tab5.append(third_g)
    fourth_g = random.choice(tab4)
    tab4.remove(fourth_g)
    tab5.append(fourth_g)
    g_drawing.config(state="disabled")
    g_simulation.config(state="normal")

    group_g = tk.Label(gui, text=f"Group G\n1. {first_g.name} {first_g.points}\n2. {second_g.name} {second_g.points}\n"
                                 f"3. {third_g.name} {third_g.points}\n4. {fourth_g.name} {fourth_g.points}\n\n")
    group_g.place(x=1340, y=15)


def h_draw(tab1, tab2, tab3, tab4, tab5):
    first_h = random.choice(tab1)
    tab1.remove(first_h)
    tab5.append(first_h)
    second_h = random.choice(tab2)
    tab2.remove(second_h)
    tab5.append(second_h)
    third_h = random.choice(tab3)
    tab3.remove(third_h)
    tab5.append(third_h)
    fourth_h = random.choice(tab4)
    tab4.remove(fourth_h)
    tab5.append(fourth_h)
    h_drawing.config(state="disabled")
    h_simulation.config(state="normal")

    group_h = tk.Label(gui, text=f"Group H\n1. {first_h.name} {first_h.points}\n2. {second_h.name} {second_h.points}\n"
                                 f"3. {third_h.name} {third_h.points}\n4. {fourth_h.name} {fourth_h.points}\n\n")
    group_h.place(x=1480, y=15)


a_drawing = tk.Button(gui, text="Draw group A", command=lambda: a_draw(pool1, pool2, pool3, pool4, a_teams))
a_drawing.place(x=50, y=200)
a_simulation = tk.Button(gui, text="Simulation A", command=lambda: a_simulate(a_teams[0], a_teams[1], a_teams[2],
                                                                              a_teams[3]))
a_simulation.config(state="disabled")
a_simulation.place(x=175, y=200)
a_results = tk.Button(gui, text="Results A", command=lambda: a_result(a_teams[0], a_teams[1], a_teams[2], a_teams[3]))
a_results.config(state="disabled")
a_results.place(x=295, y=200)

b_drawing = tk.Button(gui, text="Draw group B", command=lambda: b_draw(pool1, pool2, pool3, pool4, b_teams))
b_drawing.place(x=50, y=240)
b_simulation = tk.Button(gui, text="Simulation B", command=lambda: b_simulate(b_teams[0], b_teams[1], b_teams[2],
                                                                              b_teams[3]))
b_simulation.config(state="disabled")
b_simulation.place(x=175, y=240)
b_results = tk.Button(gui, text="Results B", command=lambda: b_result(b_teams[0], b_teams[1], b_teams[2], b_teams[3]))
b_results.config(state="disabled")
b_results.place(x=295, y=240)

c_drawing = tk.Button(gui, text="Draw group C", command=lambda: c_draw(pool1, pool2, pool3, pool4, c_teams))
c_drawing.place(x=50, y=280)
c_simulation = tk.Button(gui, text="Simulation C", command=lambda: c_simulate(c_teams[0], c_teams[1], c_teams[2],
                                                                              c_teams[3]))
c_simulation.config(state="disabled")
c_simulation.place(x=175, y=280)
c_results = tk.Button(gui, text="Results C", command=lambda: c_result(c_teams[0], c_teams[1], c_teams[2], c_teams[3]))
c_results.config(state="disabled")
c_results.place(x=295, y=280)

d_drawing = tk.Button(gui, text="Draw group D", command=lambda: d_draw(pool1, pool2, pool3, pool4, d_teams))
d_drawing.place(x=50, y=320)
d_simulation = tk.Button(gui, text="Simulation D", command=lambda: d_simulate(d_teams[0], d_teams[1], d_teams[2],
                                                                              d_teams[3]))
d_simulation.config(state="disabled")
d_simulation.place(x=175, y=320)
d_results = tk.Button(gui, text="Results D", command=lambda: d_result(d_teams[0], d_teams[1], d_teams[2], d_teams[3]))
d_results.config(state="disabled")
d_results.place(x=295, y=320)

e_drawing = tk.Button(gui, text="Draw group E", command=lambda: e_draw(pool1, pool2, pool3, pool4, e_teams))
e_drawing.place(x=50, y=360)
e_simulation = tk.Button(gui, text="Simulation E", command=lambda: e_simulate(e_teams[0], e_teams[1], e_teams[2],
                                                                              e_teams[3]))
e_simulation.config(state="disabled")
e_simulation.place(x=175, y=360)
e_results = tk.Button(gui, text="Results E", command=lambda: e_result(e_teams[0], e_teams[1], e_teams[2], e_teams[3]))
e_results.config(state="disabled")
e_results.place(x=295, y=360)

f_drawing = tk.Button(gui, text="Draw group F", command=lambda: f_draw(pool1, pool2, pool3, pool4, f_teams))
f_drawing.place(x=50, y=400)
f_simulation = tk.Button(gui, text="Simulation F", command=lambda: f_simulate(f_teams[0], f_teams[1], f_teams[2],
                                                                              f_teams[3]))
f_simulation.config(state="disabled")
f_simulation.place(x=175, y=400)
f_results = tk.Button(gui, text="Results F", command=lambda: f_result(f_teams[0], f_teams[1], f_teams[2], f_teams[3]))
f_results.config(state="disabled")
f_results.place(x=295, y=400)

g_drawing = tk.Button(gui, text="Draw group G", command=lambda: g_draw(pool1, pool2, pool3, pool4, g_teams))
g_drawing.place(x=50, y=440)
g_simulation = tk.Button(gui, text="Simulation G", command=lambda: g_simulate(g_teams[0], g_teams[1], g_teams[2],
                                                                              g_teams[3]))
g_simulation.config(state="disabled")
g_simulation.place(x=175, y=440)
g_results = tk.Button(gui, text="Results G", command=lambda: g_result(g_teams[0], g_teams[1], g_teams[2], g_teams[3]))
g_results.config(state="disabled")
g_results.place(x=295, y=440)

h_drawing = tk.Button(gui, text="Draw group H", command=lambda: h_draw(pool1, pool2, pool3, pool4, h_teams))
h_drawing.place(x=50, y=480)
h_simulation = tk.Button(gui, text="Simulation H", command=lambda: h_simulate(h_teams[0], h_teams[1], h_teams[2],
                                                                              h_teams[3]))
h_simulation.config(state="disabled")
h_simulation.place(x=175, y=480)
h_results = tk.Button(gui, text="Results H", command=lambda: h_result(h_teams[0], h_teams[1], h_teams[2], h_teams[3]))
h_results.config(state="disabled")
h_results.place(x=295, y=480)

eights_show = tk.Button(gui, text="Show 1/8", width="17", command=lambda: eights(advanced))
eights_show.place(x=50, y=520)
eights_show.config(state="disabled")
eights_simulation = tk.Button(gui, text="Simulation 1/8", width="17", command=lambda: eights_simulate(advanced, quarters
                                                                                                      ))
eights_simulation.config(state="disabled")
eights_simulation.place(x=222, y=520)

quarters_show = tk.Button(gui, text="Show 1/4", width="17", command=lambda: quarter(quarters))
quarters_show.place(x=50, y=560)
quarters_show.config(state="disabled")
quarters_simulation = tk.Button(gui, text="Simulation 1/4", width="17", command=lambda: quarters_simulate(quarters,
                                                                                                          semis))
quarters_simulation.place(x=222, y=560)
quarters_simulation.config(state="disabled")

semis_show = tk.Button(gui, text="Show 1/2", width="17", command=lambda: semi(semis))
semis_show.place(x=50, y=600)
semis_show.config(state="disabled")
semis_simulation = tk.Button(gui, text="Simulation 1/2", width="17", command=lambda: semis_simulate(semis, finals))
semis_simulation.place(x=222, y=600)
semis_simulation.config(state="disabled")

finals_show = tk.Button(gui, text="Show finals", width="17", command=lambda: final(finals))
finals_show.place(x=50, y=640)
finals_show.config(state="disabled")
finals_simulation = tk.Button(gui, text="Simulation finals", width="17", command=lambda: finals_simulate(finals,
                                                                                                         standings))
finals_simulation.place(x=222, y=640)
finals_simulation.config(state="disabled")

final_results = tk.Button(gui, text="Show final results!", width="38", command=lambda: final_result(standings))
final_results.place(x=53, y=680)
final_results.config(state="disabled")

gui.mainloop()
