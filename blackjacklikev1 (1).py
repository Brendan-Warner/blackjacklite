# -*- coding: utf-8 -*-


import numpy as np
import random

class player:
  def __init__(self, name, age, bet):
    self.name = name
    self.age = age
    self.bet = bet
    self.winings = 0
    self.hand = {}
    self.manips = []
    self.manips_hand = []
    self.scores=0
    self.done = false


    

    self.bust = false
    
    self.stand = false


  def return_manipulator(self, num):##retuns a number from the manipulation hand then adds a new one from the manips list, then removes that from the manips list.
    num = self.manips_hand[num]
    update_score(num)
    if len(self.manips) > 0:
      self.manips_hand[num] = self.manips[len(self.manips)]
      self.manips.pop()

    else:
      self.manips_hand.pop()

  def create_manips(self):## creates the manipulation list that is pulled from for the manip hand
    for x in range 10:
      num = random.randrange(-5,5)
      self.manips.append(num)
    


  def create_manips_hand(self):#create the manipulation hand for the list of manipulation, only 5 manip numbers are avaliable at a time.
    for x in range 6:
      self.manips_hand.append(self.manips[len(self.manips)])
      self.manips.pop()
      
  def return_manip_hand_len(self):#returns the length of the manipulation hand
    return len(self.manips_hand)

  def return_name(self):#returns the name of the player
    return self.name

  def return_age(self):#returns the age of the player
    return self.age
  
  def return_bet(self):#returns the bet of he player
    return self.bet

  def return_hand(self):#returns the hand of he player
    hand = ""
    for x in self.hand:#this loops through the hands dictionary and every individual value of the dictionarys in hands. 
      hand = hand + " " x
      print("Your hand is" + hand+ " with a score of" + return_score())

  def return_manip_hand(self):#returns the manipulation hand of the player
    hand = ""
    for x in self.manip_hand:#this loops through the hands dictionary and every individual value of the dictionarys in hands. 
      hand = hand + " " + x
      print("Your manipulation hand is " + hand)
      

  def return_score(self):#returns the score of the player
    return self.score
  
  def update_score(self, num):#updates the player score
    self.score +=num
    

  def update_hand(self, card_type, card_num, num):#updates the player hand, then calls update score
    self.hand.update({card_type, card_num})
    self.update_score(card_num)

  def update_stands(self):#updates the player stand to be true
    self.stand= true

  def return_stand(self):
    return self.stand
  def update_bust(self):
    if self.score > 21:
      self.bust = true
  def return_bust(self):
    return self.bust

  def stop_playing(self):
    if return_score() == 21:
      self.done = true

  def return_done(self):
    return self.done


class ai(player):#same as player with some functions for the ai specifically.

  def ai_check_can_win(self):#ai checks if it can win by playing a manipualtion card, if yes, then play that card
    i = 0
    for x in self.manip_hand:
      if self.score + x == 21:
        self.return_manip(i)
        return
      i++

  def ai_check_to_close(self):#ai checks if it is to close to the winning number without being on it, if yes, it will ether play a negative number manipulator or stand, else, it may play a positive manipulator
    
    if self.score > 18:
      number = random.randrange(1,4)
      if number == 1:
        self.update_stands()
      if number == 2 && return_manip_hand_len() > 0:
        self.ai_manip_neg():
      
    elif self.score < 18 && return_manip_hand_len() > 0:
      self.ai_manip_pos()


  def ai_manip_neg():
    num = 0
    i = 0
    j
    for x in self.manip_hand:
      if x < 0:
        j = random.randrange(1,3)
        if j = 1:
          num = i
          self.return_manip(num)
      i++
    

    
def ai_manip_pos():
    num = 0
    i = 0
    j = 0
    for x in self.manip_hand:
      if x > 0:
        j = random.randrange(1,3)
        if j = 1:
          num = i
          self.return_manip(num)
      i++
    


class deck:
  def __init__(self):
    self.deck={'ace of clubs': 1, '2 of clubs' : 2,  '3 of clubs': 3,  '4 of clubs' : 4,  '5 of clubs': 5,  '6 of clubs' : 6,  '7 of clubs' : 7,  '8 of clubs' : 8,  '9 of clubs' : 9,  '10 of clubs' : 10,  "jack of clubs" : 10,  "queen of clubs" : 10, "king of clubs" : 10, 'ace of diomands' : 1, '2 of diomands' : 2, '3 of diomands' : 3,  '4 of diomands' : 4, '5 of diomands': 5, '6 of diomands': 6, '7 of diomands': 7, '8 of diomands' : 8, '9 of diomands': 9, '10 of diomands': 10, "jack of diomands" : 10,  "queen of diomands": 10, "king of diomands" : 10, 'ace of hearts': 1, '2 of hearts': 2, '3 of hearts': 3, '4 of hearts': 4, '5 of hearts': 5, '6 of hearts': 6,'7 of hearts': 7,'8 of hearts': 8,'9 of hearts': 9,'10 of hearts': 10, "jack of hearts": 10, "queen of hearts" : 10,"king of hearts": 10, 'ace of spades':1, '2 of spades': 2, '3 of spades': 3, '4 of spades': 4, '5 of spades': 5, '6 of spades': 6, '7 of spades': 7, '8 of spades': 8,  '9 of spades': 9, '10 of spades':10,"jack of spades":10, "queen of spades": 10, "king fo spades": 10}
    self.all_cards = []
    self.current = 0
    

  def return_current(self):#returns the current card we are on
      return self.current

  def shuffle_deck(self):#shuffles the deck at the start.
    
    for x in deck:
      self.all_cards.append(x)
      
    np.random.shuffle(self.all_cards)

  
  
  def return_card(self):#returns a card from the deck
    card = {self.all_cards[current]: self.deck[self.all_cards[current]}
    self.current++
    return card


name = input("Please enter your name")
age = int(input("Please enter your age"))
bet = int(input("Please enter your bet in dollers"))

deck1 = deck()
player1 = player(name, age, bet)
player2 = ai("other", 25, bet)


player1.create_manips()
player1.create_manips_hand()

player2.create_manips()
player2.create_manips_hand()






game = true

##the flow of the game:
##at the start of the turn, both players draw a card
##if they bust or land on 21 at any point, they stop playing 
##if they choose not to stand, they can play a manipulation card, if they bust or hit 21 doing this, they stop playing
##the game goes until both players are standing or bust.

while game:
  if player1.return_stand() == false && player1.return_bust() == false && player1.return_done() == false:
    card = deck1.return_card()
    for x in card:
      player1.update_hand(x, card[x])
    player1.return_hand()
    player1.return_manip_hand()
  
    if player1.return_bust() == false && player1.return_done() == false:
      stand = input("Would you like to stand on this hand? enter y to stand")

      if stand == "y":
      player1.update_stand()
  
      elif stand != "y" && player1.return_manip_hand_length() != 0:
        manip = input("Would you like to manipulate your hand? please select a number above or enter -1 to not manipulate your hand")
        if manip != -1:
        player1.return_manipulator(manip)

      


  else:
    player1.return_hand()

  
  if player2.return_stand() == false && player2.return_bust == false && player2.return_done() == false:
    card = deck1.return_card()
    for x in card:
      player2.update_hand(x, card[x])
    player2.return_hand()
    player2.return_manip_hand()

    if player2.return_bust == false && player2.return_done() == false && player2.return_stand() == false:#check if the score is close to 21, if a manipulation card can be played that would get to 21, then play it, else if close randamly choose to ether stand or if possible play a negative manip card
      player2.ai_check_can_win()

      if player2.return_done() == false:
        player2.ai_check_to_close()



  else:
    player2.return_hand()

  if (player1.return_stand == true || player1.return_bust == true || player1.return_done == true) && (player2.return_stand == true || player2.return_bust == true || player2.return_done == true):
    game = false
if (player1.return_bust() == true && player2.return_bust() == true) || (player1.return_score() == player2.return_score()) || ((player1.return_score < player2.return_score) && player2.return_bust() == false):
  print("Sorry" + player1.return_name() + " you lost, you owe" + player1.return_bet * 2 + "$")
else:
  print(player1.return_name() + " You won the game! You won " + player1.return_bet() * 2)
