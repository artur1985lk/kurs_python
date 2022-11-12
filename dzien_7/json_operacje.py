import json
def dodaj():
    pass

def show_records(recordings):
    for rec in enumerate(recordings, start= 1):
        print(f"- [{re}]")

def main():
    while True:
        file_name = ""

        what = input("Co chcesz zrobić? d - dodaj, w - wpisz, q zakońccz ")
        if what == "d":
            title = input("tytul: ")
            artist = input("artysta: ")
            year = input("Rok_wydania: ")
            record = {"title": title,
                      "artist": artist,
                      "year": year}

            with open("dane.json") as f:
                json.dump(record, f)

        if what == "d":
            pass

        if what == "q":
            print("Koniec sesji, dane zapisane")
            break

def get_longest(colection,key):
    """

    :param colection: list of dicts
    :param key: key from dict
    :return: int - len longgest walue for key in dicts from collection
    """




# data = [{"temperatura": 45, "cisnienie": 1000},
#         {"temperatura": 40, "cisnienie": 1001}]
# data = json.loads(data)
# # data = json.dump(data)
with open("dane.json") as f:
    json.dump((data), f)

with open("dane.json") as f:
    json.load((data), f)

if __name__ == "__main__":
    recordings = [{"title": "aa", "artist": "bb", "year": 1980},
                  {"title": "cc", "artist": "cb", "year": 1981}]
    show_records()