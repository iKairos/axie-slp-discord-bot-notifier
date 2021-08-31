# Axie Infinity SLP Discord Bot Notifier
SLP Bot is a Discord Bot that notifies you of the market behavior of the cryptocurrency coin SLP or Smooth Love Potion and the AXS.

## Initial Preparation and Installation
1. Clone the repository.
2. Run the `preparer.py` file to instantiate all the requirements and dependencies.
3. Check if you have the following directories and file dependencies:
   - `assets`
   - `assets/images`
   - `assets/images/graphs`
   - `assets/images/graphs/slp`
   - `assets/images/graphs/axs`
   - `secrets.py`
4. Put your Discord Bot token under the variable `TOKEN` in the `secrets.py` file.
5. Make sure you have the following dependencies/libraries:
   - Discord Py
     - **Windows**: `py -3 -m pip install -U discord.py`
     - **Linux or MacOS**: `python3 -m pip install -U discord.py`
   - Matplotlib
     - **Windows**: `py -3 -m pip install -U matplotlib`
   - CoinGecko API
     - **Windows**: `py -3 -m pip install -U pycoingecko`
     
**Note**: Make sure you have at least Python Version 3.7 and up for this bot to work.

## Work to be Done
1. A Help Command (list and description of all commands)
2. Conversion into a scholar management system (?)
3. Error handling and more!
