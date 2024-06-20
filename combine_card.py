# Read all txt and combine them into a single txt file
# # Python
import os
# Open the output file in write mode
with open('card/card_vocab_all.txt', 'w') as outfile:
    # Iterate over all files in the 'card' directory
    for fname in os.listdir('card'):
        # Only process text files
        if fname.endswith('.txt') and 'card_vocab_all_Group' in fname:
            # Open each file in read mode
            with open(f'card/{fname}') as infile:
                # Write the content of the file to the output file
                outfile.write(infile.read())
                # Add a newline character to separate the content of different files
                outfile.write('\n')
