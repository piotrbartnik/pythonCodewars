def points(games):
	sumGames = 0
	i = 0
	while i < len(games):
		if games[i][0] > games[i][2]:
			sumGames += 3
		elif games[i][0] == games[i][2]:
			sumGames += 1
		else:								
			sumGames += 0
		i += 1
	print(sumGames)
	return sumGames


points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3'])
