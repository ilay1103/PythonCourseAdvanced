import winsound


def main():
    freqs = {"la": 220,
             "si": 247,
             "do": 261,
             "re": 293,
             "mi": 329,
             "fa": 349,
             "sol": 392,
             }

    notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

    notes_list = notes.split('-')
    print(type(notes_list))
    print(dir(notes_list))
    for note_tuple in notes_list:
        note, duration = note_tuple.split(',')
        frequency = freqs[note]
        duration = int(duration)
        winsound.Beep(frequency, duration)


if __name__ == '__main__':
    main()