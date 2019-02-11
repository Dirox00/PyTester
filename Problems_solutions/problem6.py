songs = [input() for _ in range(int(input()))]

lista = []
for song in songs:
	if song not in lista:
		lista.append(song)

lista.sort(key=lambda x: songs.count(x), reverse=True)

for song in lista:
	print(songs.count(song), song)