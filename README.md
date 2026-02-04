# EDSAC-Blackjack
## Game Like It's 1949!
A fully functional Blackjack simulator for the EDSAC computer, written entirely in Initial-Orders-2 EDSAC assembly code. <br><br>The program is contained entirely within the `Blackjack.EDSAC` file. 
To run it, you'll need some five-holed punch tape and access to an EDSAC mainframe! Alternatively, you could run the program using a [simulator](https://www.dcs.warwick.ac.uk/~edsac/).

The program includes a single, pre-shuffled deck.
The included Python script `Deck\deck-generator.py` can be used to generate alternative decks. Just simply copy the output of the file and paste it into the program over the current deck!<br>

Located in the `Subroutines` folder are the singular implementations of the custom subroutines used in the main program, along with some tests used during development.<br>

In `notes.txt` is where you'll find a general outline of the program, further descriptions of the custom subroutines, and a breakdown of the data structures used for encoding cards and hands of cards.