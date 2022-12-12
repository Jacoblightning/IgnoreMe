"""substitutes"""
# noinspection PyUnresolvedReferences
import tkinter as tk
import os
import platform
import sys
from tkinter import ttk
from functools import partial
from copy import deepcopy as copy
from pyautogui import prompt

tk.Button = ttk.Button
tk.Frame = ttk.Frame
tk.Label = ttk.Label
EURYTHMY = False
DAY = 'NONE'
TIME = 'NONE'


# noinspection SpellCheckingInspection
def retappend(l, j, *args):
    """
    returns and appends
    """
    h = copy(l)
    if j:
        h.append(j)
    if args and not j:
        for i in args:
            h.append(i)
    return h


def eur(teach):
    """eurythmy
    """
    global EURYTHMY
    return teach if not EURYTHMY else teachers['Eurythmy']


# noinspection SpellCheckingInspection
def returnhelper(day, time):
    """Helps with main function"""
    Array = Arrayget()
    return [i for i in Allteach if i not in Array[day][time]]


teachers = \
    {
        'subject': [
            ['LaShawnda', 'Radha McNamara'], 'Benjamin', 'Andrew',
            'Claire', 'Malina', 'Jason', 'Kris', 'Christopher'
        ],
        'Music': 'Jason', 'Movement': 'Jamie', 'Woodwork': 'Bill',
        'Eurythmy': 'Christina', 'Math': 'Hannah Gatner',
        'Handwork': ['Wendy', 'Hannah McKinnis'], 'Farming': 'Kristin',
        'Spanish': 'Kim', 'Art': 'Adrienne'  # , 'Coming Of Age': 'Metta'
    }
# noinspection SpellCheckingInspection
Allteach = ['LaShawnda', 'Radha McNamara', 'Benjamin',
            'Andrew', 'Claire', 'Malina', 'Jason', 'Kris',
            'Christopher', 'Wendy', 'Hannah McKinnis',
            'Jason', 'Jamie', 'Bill', 'Christina',
            'Hannah Gatner', 'Kristin', 'Kim', 'Adrienne', "Ms. Kenteti"]
subs = copy(teachers['subject'])
special = [teachers['Art'], teachers['Farming'], teachers['Woodwork'], *teachers['Handwork']]
special = copy(special)


# noinspection SpellCheckingInspection
def Arrayget():
    Array = \
        {
            'Monday': {
                '8:30': copy(subs),
                '11:05': retappend(
                    retappend(
                        retappend(
                            retappend(
                                retappend(
                                    subs[:3],
                                    teachers["Music"]),
                                teachers["Handwork"][0]),
                            teachers["Math"]),
                        teachers["Movement"]),
                    teachers["Spanish"]),
                '11:55': retappend(
                    retappend(
                        retappend(
                            retappend(
                                retappend(
                                    retappend(
                                        retappend(
                                            [subs[1]],
                                            eur(
                                                "Ms. Kenteti")),
                                        teachers["Handwork"][0]),
                                    teachers["Music"]),
                                teachers["Movement"]),
                            teachers["Spanish"]),
                        subs[6]),
                    teachers['Math']),

                '1:25': retappend(
                    retappend(
                        retappend(
                            retappend(
                                retappend(
                                    retappend(
                                        retappend(
                                            subs[0],
                                            subs[3]),
                                        teachers["Farming"]),
                                    teachers["Movement"]),
                                eur(
                                    subs[4])),  # Specified in note from ms. pinarr
                            teachers["Spanish"]),
                        teachers["Math"]),
                    teachers["Music"]),
                '2:15': retappend(
                    retappend(
                        retappend(
                            retappend(
                                retappend(
                                    subs[0],
                                    teachers["Farming"]),
                                eur(
                                    subs[4])),
                            teachers["Movement"]),
                        teachers["Music"]),
                    eur(
                        subs[7])) + subs[2:4]  # TWO Eurythmys?
            },
            'Tuesday': {
                '8:30': subs,
                '11:05': retappend(
                    retappend(
                        retappend(
                            retappend(
                                retappend(
                                    retappend(
                                        retappend(
                                            subs[0],
                                            subs[3]
                                        ),
                                        teachers['Spanish']),
                                    subs[7]),
                                teachers['Farming']),
                            eur(teachers['Handwork'][0])),
                        teachers['Movement']),
                    teachers['Music']),
                '11:55': retappend(
                    retappend(
                        retappend(
                            retappend(
                                retappend(
                                    retappend(
                                        subs[3:5],
                                        eur(subs[6])
                                    ),
                                    teachers['Math']),
                                teachers['Movement']),
                            teachers['Farming']),
                        teachers['Spanish']),
                    eur(teachers['Handwork'][0])),
                '1:25': retappend(
                    retappend(
                        retappend(
                            retappend(
                                special,
                                teachers['Eurythmy']
                            ),
                            teachers['Spanish']),
                        subs[1]),
                    teachers['Movement']),
                '2:15': retappend(
                    retappend(
                        retappend(
                            retappend(
                                special,
                                subs[1]
                            ),
                            eur(
                                subs[2]
                            )),
                        teachers['Music']),
                    teachers['Movement'])
            },
            'Wednesday': {
                '8:30': subs,
                '11:05': retappend(
                    retappend(
                        retappend(
                            retappend(
                                retappend(
                                    retappend(
                                        retappend(
                                            [teachers['Handwork'][0]],
                                            subs[0]
                                        ),
                                        teachers['Movement']),
                                    teachers['Music']),
                                teachers['Farming']),
                            teachers['Math']),
                        subs[6]),
                    teachers['Spanish']),
                '11:55': retappend(
                    retappend(
                        retappend(
                            retappend(
                                retappend(
                                    retappend(
                                        retappend(
                                            [teachers['Handwork'][0]],
                                            teachers['Movement']
                                        ),
                                        subs[2]),
                                    teachers['Spanish']),
                                teachers['Farming']),
                            "Ms. Kenteti"),
                        teachers['Math']),
                    subs[7]),
                '1:25': retappend(
                    retappend(
                        retappend(
                            retappend(
                                retappend(
                                    retappend(
                                        retappend(
                                            [teachers['Handwork'][0], subs[2]],
                                            teachers['Spanish']
                                        ),
                                        subs[0]),
                                    teachers['Farming']),
                                teachers['Music']),
                            eur(
                                "Ms. Kenteti"
                            )),
                        teachers['Movement']),
                    teachers['Math']),
                '2:15': retappend(
                    retappend(
                        retappend(
                            retappend(
                                retappend(
                                    retappend(
                                        subs[:3],
                                        teachers['Handwork'][0]
                                    ),
                                    teachers['Farming']),
                                subs[4]),
                            teachers['Movement']),
                        teachers['Music']),
                    eur(subs[7]))
            },
            'Thursday': {
                '8:30': subs,
                '11:05': retappend(
                    retappend(
                        retappend(
                            retappend(
                                retappend(
                                    subs[1:5],
                                    teachers['Spanish']
                                ),
                                teachers['Handwork'][0]),
                            teachers['Music']),
                        subs[6]),
                    teachers['Math']),
                '11:55': retappend(
                    retappend(
                        retappend(
                            retappend(
                                retappend(
                                    retappend(
                                        retappend(
                                            subs[:2],
                                            teachers['Movement']
                                        ),
                                        teachers['Music']),
                                    subs[4]),
                                teachers['Spanish']),
                            teachers['Math']),
                        subs[7]),
                    teachers['Handwork'][0]),
                '1:25': retappend(
                    retappend(
                        retappend(
                            retappend(
                                subs[1:3],
                                teachers['Movement']
                            ),
                            teachers['Eurythmy']),
                        teachers['Spanish']), False,
                    *special),
                '2:15': retappend(
                    special,
                    False,
                    *[teachers['Movement'], subs[3], teachers['Spanish'], subs[1], teachers['Eurythmy']]
                )
            },
            'Friday': {
                '8:30': subs,
                '11:05': [teachers['Farming'], subs[1], eur(teachers['Handwork'][0]),
                          teachers['Spanish'], *subs[4:6], teachers['Math'], teachers['Movement']],
                '11:55': [teachers['Farming'], subs[1], eur(teachers['Handwork'][0]),
                          teachers['Spanish'], *subs[3:5], teachers['Math'], teachers['Music']],
                '1:25': [*subs[0], subs[2], teachers['Handwork'][1], teachers['Spanish'],
                         teachers['Movement'], teachers['Math'], eur(subs[6]), subs[5]],
                '2:15': [*subs[0], *subs[2:4], teachers['Movement'], teachers['Handwork'][1], *subs[5:]]
            }
        }
    return Array


same = {'Monday': 'Mon',
        'Tuesday': 'Tues',
        'Wednesday': 'Wed',
        'Thursday': 'Thurs',
        'Friday': 'Fri'}


# noinspection SpellCheckingInspection
def setday(day):
    global DAY
    global TIME
    global same
    global selday
    global buttonsday
    DAY = day
    other = []
    tochange = buttonsday[same[day]]
    for i in list(buttonsday.values()):
        if i != tochange:
            other.append(i)
    selday['text'] = 'Current selected day is ' + day
    ttk.Button.state(tochange, ['pressed'])
    for i in other:
        ttk.Button.state(i, ['!pressed'])
    calculatebutton['text'] = 'Calculate substitutes available for ' + DAY + ' at ' + TIME


# noinspection SpellCheckingInspection,PyGlobalUndefined
def settime(time):
    global TIME
    global DAY
    global calculatebutton
    global same
    global seltime
    global buttonstime
    TIME = time
    other = []
    tochange = buttonstime[time]
    for i in list(buttonstime.values()):
        if i != tochange:
            other.append(i)
    seltime['text'] = 'Current selected time is ' + time
    ttk.Button.state(tochange, ['pressed'])
    for i in other:
        ttk.Button.state(i, ['!pressed'])
    calculatebutton['text'] = 'Calculate substitutes available for ' + DAY + ' at ' + TIME


# noinspection SpellCheckingInspection
def calculate():
    global DAY
    global TIME
    global subslabel
    global mainlabel
    subslabel['text'] = 'Avalible substitutes for ' + DAY + ' at ' + TIME + ' are:'
    mainlabel['text'] = ', '.join(returnhelper(DAY, TIME))


# print(Array["Monday"]["11:05"])
# noinspection SpellCheckingInspection
def flip():
    global EURYTHMY
    # noinspection PyGlobalUndefined
    global button
    # noinspection PyGlobalUndefined
    global label
    EURYTHMY = False if EURYTHMY else True
    button['text'] = 'Activate Eurythmy' if not EURYTHMY else 'Deactivate Eurythmy'
    label['text'] = 'Eurythmy is active.' if EURYTHMY else 'Eurythmy is inactive.'


def createwindow():
    global window, frame_a, frame_b, frame_c, frame_d, frame_e, frame_f, mainframe
    window = tk.Tk()
    frame_a = tk.Frame(master=window)
    frame_b = tk.Frame(master=window)
    frame_c = tk.Frame(master=window)
    frame_d = tk.Frame(master=window)
    frame_e = tk.Frame(master=window)
    frame_f = tk.Frame(master=window)
    mainframe = tk.Frame(master=window)


def dayandtime():
    global framesday, framestime, buttonstime, buttonsday
    # noinspection SpellCheckingInspection
    framesday = {
        'mon': tk.Frame(master=window),
        'tues': tk.Frame(master=window),
        'wed': tk.Frame(master=window),
        'thurs': tk.Frame(master=window),
        'fri': tk.Frame(master=window)
    }
    # noinspection SpellCheckingInspection
    framestime = {
        '8:30': tk.Frame(master=window),
        '11:05': tk.Frame(master=window),
        '11:55': tk.Frame(master=window),
        '1:25': tk.Frame(master=window),
        '2:15': tk.Frame(master=window)
    }
    buttonstime = {
        '8:30': tk.Button(
            master=framestime['8:30'],
            text='8:30',
            width=25,
            command=partial(settime, '8:30')
        ),
        '11:05': tk.Button(
            master=framestime['11:05'],
            text='11:05',
            width=25,
            command=partial(settime, '11:05')
        ),
        '11:55': tk.Button(
            master=framestime['11:55'],
            text='11:55',
            width=25,
            command=partial(settime, '11:55'),
        ),
        '1:25': tk.Button(
            master=framestime['1:25'],
            text='1:25',
            width=25,
            command=partial(settime, '1:25')
        ),
        '2:15': tk.Button(
            master=framestime['2:15'],
            text='2:15',
            width=25,
            command=partial(settime, '2:15')
        )}
    # noinspection SpellCheckingInspection
    buttonsday = {
        'Mon': tk.Button(
            master=framesday['mon'],
            text='Monday',
            width=25,
            command=partial(setday, 'Monday')
        ),
        'Tues': tk.Button(
            master=framesday['tues'],
            text='Tuesday',
            width=25,
            command=partial(setday, 'Tuesday')
        ),
        'Wed': tk.Button(
            master=framesday['wed'],
            text='Wednesday',
            width=25,
            command=partial(setday, 'Wednesday'),
        ),
        'Thurs': tk.Button(
            master=framesday['thurs'],
            text='Thursday',
            width=25,
            command=partial(setday, 'Thursday')
        ),
        'Fri': tk.Button(
            master=framesday['fri'],
            text='Friday',
            width=25,
            command=partial(setday, 'Friday')
        )}


def pac():
    button = tk.Button(
        master=frame_a,
        text='Deactivate Eurythmy' if EURYTHMY else 'Activate Eurythmy',
        width=25,
        command=flip
    )
    for i in list(buttonsday.values()):
        i.pack()
    for i in list(buttonstime.values()):
        i.pack()
    button.pack()
    # noinspection SpellCheckingInspection
    calculatebutton = tk.Button(
        master=frame_e,
        text='Calculate substitutes available for NONE at NONE',
        width=55,
        command=calculate
    )
    calculatebutton.pack()
    label = tk.Label(master=frame_b, text='Eurythmy is inactive.')
    label.pack()
    # noinspection SpellCheckingInspection
    seltime = tk.Label(master=frame_d, text='Current selected time is NONE')
    # noinspection SpellCheckingInspection
    selday = tk.Label(master=frame_c, text='Current selected day is NONE')
    selday.pack()
    seltime.pack()
    # noinspection SpellCheckingInspection
    subslabel = tk.Label(master=frame_f, text='')
    # noinspection SpellCheckingInspection
    mainlabel = tk.Label(master=mainframe, text='')
    mainlabel.pack()
    subslabel.pack()
    frame_a.grid(row=0, column=2)
    frame_b.grid(row=1, column=2)
    for count, frame in enumerate(list(framesday.values())):
        frame.grid(row=3, column=count)
    frame_c.grid(row=4, column=2)
    for count, frame in enumerate(list(framestime.values())):
        frame.grid(row=5, column=count)
    frame_d.grid(row=6, column=2)
    frame_e.grid(row=7, column=1, columnspan=3)
    frame_f.grid(row=8, column=0)
    mainframe.grid(row=9, column=0, columnspan=3)
    window.mainloop()


def main():
    createwindow()
    dayandtime()
    pac()


if __name__ == "__main__":
    main()
# hi
