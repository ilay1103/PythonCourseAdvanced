
class MusicNotes:

    def __init__(self):
        self._notes_dict = (("La", 55), ("Si", 61.74), ("Do", 65.41), ("Re", 73.42), ("Mi", 82.41), ("Fa", 87.31), ("Sol", 98))
        self._note_dict_ptr = -1
        self._octaves = 0

    def __iter__(self):
        return self

    def next(self):
        if self._note_dict_ptr >= len(self._notes_dict) - 1:
            self._note_dict_ptr = -1
            self._octaves += 1
        if self._octaves > 4:
            raise StopIteration

        self._note_dict_ptr += 1
        return self._notes_dict[self._note_dict_ptr][1] * (2 ** self._octaves)

def main():
    notes_iter = iter(MusicNotes())
    for freq in notes_iter:
        print(freq)

if __name__ == "__main__":
    main()