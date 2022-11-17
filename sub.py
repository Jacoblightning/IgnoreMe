"""substitutes"""
from copy import deepcopy as copy

EURYTHMY = False


def retappend(l, j):
    """returnappends
    """
    h = copy(l)
    h.append(j)
    return h


def eur(teach):
    """eurythmy
    """
    global EURYTHMY
    return teach if not EURYTHMY else teachers['eurythmy']


def returnhelper(day, time):
    """Helps with main function"""
    return [i for i in Allteach if i not in Array[day][time]]


# [i for i in Allteach if i not in Array["Monday"]["1:25"]]
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
Allteach = ['LaShawnda', 'Radha McNamara', 'Benjamin',
            'Andrew', 'Claire', 'Malina', 'Jason', 'Kris',
            'Christopher', 'Wendy', 'Hannah McKinnis',
            'Jason', 'Jamie', 'Bill', 'Christina',
            'Hannah Gatner', 'Kristin', 'Kim', 'Adrienne']
subs = copy(teachers['subject'])
special = [teachers['Art'], teachers['Farming'], teachers['Woodwork'], teachers['Handwork']]
special = copy(special)
Array = \
    {
        'Monday': {
            '8:30': copy(subs),
            '11:05': retappend(
                retappend(
                    retappend(
                        retappend(
                            retappend(
                                subs[:2],
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
                                            subs[5])),
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
                                        [subs[0]],
                                        subs[3]),
                                    teachers["Farming"]),
                                teachers["Movement"]),
                            eur(
                                "Ms. Kenteti")),  # Specified in note from ms. pinarr
                        teachers["Spanish"]),
                    teachers["Math"]),
                teachers["Music"]),
            '2:15': retappend(
                retappend(
                    retappend(
                        retappend(
                            retappend(
                                [subs[0]],
                                teachers["Farming"]),
                            eur(
                                subs[4])),
                        teachers["Movement"]),
                    teachers["Music"]),
                eur(
                    subs[7])) + subs[2:3]  # TWO Eurythmys?
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
                                        teachers['subject'][0],
                                        teachers['subject'][3]
                                    ),
                                    teachers['Spanish']),
                                teachers['subject'][7]),
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
                                    teachers['subject'][3:4],
                                    eur(teachers['subject'][6])
                                ),
                                teachers['Math']),
                            teachers['Movement']),
                        teachers['Farming']),
                    teachers['Spanish']),
                eur(teachers['Handwork'][0])),
            '1:25': '',
            '2:15': ''
        },
        'Wednesday': {
            '8:30': subs,
            '11:05': '',
            '11:55': '',
            '1:25': '',
            '2:15': ''
        },
        'Thursday': {
            '8:30': subs,
            '11:05': '',
            '11:55': '',
            '1:25': '',
            '2:15': ''
        },
        'Friday': {
            '8:30': subs,
            '11:05': '',
            '11:55': '',
            '1:25': '',
            '2:15': ''
        }
    }
# print(Array["Monday"]["11:05"])
