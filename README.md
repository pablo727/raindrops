# Raindrops Game
A simple Pygame project where raindrops fall from the top of the screen, and new raindrops appear at the top when they disappear from the bottom. This project is based on Exercise 13-3 and 13-4 from the book Python Crash Course. 
---
## Features
- Raindrops fall continuously from top to bottom of the screen.
- When raindrops disappear off the bottom, new raindrops are generated at the top.
- Designed using Pygame for graphics and animations.
- Includes a grid of raindrops that dinamically adjust based on screen size.
---
## Requirements
- Python 3.8 or higher.
- Pygame library.
  Install Pygame using the following command:
  ```bash
  pip install pygame
  ```
---
## How to Run
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/pablo727/raindrops.git
   cd raindrops
   ```
2. Ensure you have the required raindrop.png image file in the images folder. If it's missing, the program will use a blue placeholder rectangle.
3. Run the game:
   ```bash
   python raindrops.py
   ```
4. Close the game by clicking the close button or pressing CTRL + C in the terminal.
   ---
## File Structure
- raindrops.py: Main script that initializes the game, handles events, and updates raindrops.
- raindrop_settings.py: Contains configurable game settings like screen size, raindrop speed, and colors.
- raindrop_grid.py: Defines the behavior of individual raindrops (e.g., falling, positioning).
- images/: Directory containing the raindrop.png image.
---
## Contributing
Contributions are welcome! If you’d like to improve the project, feel free to fork the repository and submit a pull request.
---
## License
This project is licensed under the MIT License. See the [License](./LICENSE)
---
## Acknowledgements
- [Rain Particle Animated](https://opengameart.org/content/rain-particle-animated) by opengameart.org
   
