

# piano-tiles-auto-clicker
_Really simple python program to make an auto clicker using computer vision  
Made for [Piano Tiles](https://h5.4j.com/games/Piano-Tiles-2-Online/index.html?pubid=yiv&v=1546731466)_

### Usage:

1) Install the required pakages (pip install -r requirements.txt or pip3 install -r requirements.txt)
    
    For Windows:
    
    ```powershell
    pip install -r requirements.txt
    ```
    
    For MacOS/Linux:
    
    ```bash
    pip3 install -r requirements.txt
    ```
2) Open the [Site](https://h5.4j.com/games/Piano-Tiles-2-Online/index.html?pubid=yiv&v=1546731466)

3) Click on play

4) See the position of starting tile. (First, Second, Third, Fourth)

5) Uncomment the code (line 46-49) in the auto_click.py file which contains the starting position of the tile 

    ```python
    # mouse.position = (742, 729) # First
    # mouse.position = (885, 721) # Second
    # mouse.position = (1025, 729) # Third
    # mouse.position = (1170, 725) # Fourth
    ```
6) Save and run the python file and let it do the rest.

7) To stop the program, simply force the mouse towards the right side of the screen
