import os

PATH="PATH_TO/Fossil-ID/data/lists"
def _groups():
    """Converts txt files of data into lists."""
    filenames = [name.strip(".txt") for name in os.listdir(PATH)]
    # Converts txt file of data into lists
    lists = {}
    for filename in filenames:
        print(f"Working on {filename}")
        with open(f'{PATH}/{filename}.txt', 'r') as f:
            lists[filename] = [line.strip().lower() for line in f]
        print(f"Done with {filename}")
    print("Done with lists!")
    return lists

groups = _groups()

for key in groups.keys():
    for item in groups[key]:
        try:
            os.makedirs(f"{key}/{item}")
        except OSError:
            print("Already exists")
        else:
            with open(f"{key}/{item}/image.placeholder", "x") as f:
                f.write("")

