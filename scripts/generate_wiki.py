import time
start = time.time()
from sciolyid.data import id_list
import wikipedia
import string

urls = {}
with open(f'data/wikipedia.txt', 'r') as f:
    for line in f:
        thing = line.strip().split(',')[0]
        url = line.strip().split(',')[1]
        urls[thing] = url

fails = []
with open("data/wikipedia.txt", 'w') as f:
    for thing in id_list:
        print(thing)
        if thing in urls.keys():
            url = urls[thing]
        else:
            try:
                url = wikipedia.page(f"{thing}").url
            except:
                print('FAIL')
                fails.append(thing)
                continue
        f.write(f"{thing},{url}\n")

end = time.time()
print(fails)
print(end-start)