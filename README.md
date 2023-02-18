# 3-character-minecraft-names
A new place to get 3 letter minecraft names.

# How it works:

1. Go to https://namemc.com/minecraft-names?time=20140214T123057Z&length_op=eq&length=3&sort=asc and select and copy all the names in _green_.
2. Paste the results into a text editor. Go to the next page and copy everything that is green and stop if there is no green left.
3. Open the Python program called `find.py` and input the whole pasted list.
4. It outputs a set of ordered usernames that are ordered based on the lowercase width, in pixels, of the text.
For example: `ijk` would output `12` since it has widths: `1`, `5` and `4`. It adds it to 2 and that's its shortness rating. This will be posted weekly on the `usernames.txt` file.


The `dropping_soon.txt` file will be for the white text. These ones are ones that will be available in less than a month.

I will be updating the `usernames.txt` and `dropping_soon.txt` file weekly.
