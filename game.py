import table
playing = True
while True:
	print("Welcome to BlackJack!")
	deck = table.Deck()
	deck.shuffle()

	player_hand = table.Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = table.Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	player_chips = table.Chips()

	table.take_bet(player_chips)

	table.show_some(player_hand,dealer_hand)

	while playing:

		table.hit_stand(deck,player_hand)
		table.show_some(player_hand,dealer_hand)

		if player_hand.value >21:
			table.player_busts(player_hand,dealer_hand,player_chips)

			break
	if player_hand.value <= 21:
		while dealer_hand.value < player_hand.value:
			table.hit(deck,dealer_hand)

		table.show_all(player_hand,dealer_hand)

		if dealer_hand.value > 21:
			table.dealer_busts(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value > player_hand.value:
			table.dealer_wins(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value < player_hand.value:
			table.player_wins(player_hand,dealer_hand,player_chips)
		else:
			table.push(player_hand,dealer_hand)

	print(f"/n PLayer total chips are at: {player_chips.buy_in}")

	new_game = input("Would you like to play again? y/n:  ")

	if new_game[0].lower() == 'y':
		playing = True
		continue
	if new_game[0].lower() == 'n':
		playing = False
		print("Thanks for playing!")
		break


