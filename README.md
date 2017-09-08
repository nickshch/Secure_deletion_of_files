# Secure deletion of files
With this utility you can wipe data from file, then delete it so no one can restore it.

## Args
Utility has 3 arguments:
- path to your file
- count of wipes
- wipe with nops or random data (0 - nops, 1 - random)

## Example
        python secure_deletion.py file.txt 1 0
