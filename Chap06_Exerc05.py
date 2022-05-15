#THIS PROGRAM WILL FIND A CHARACTER IN THE STRING AND SLICE IT:
line = "X-DSPAM-Confidence:0.8475"

index_colon = line.find(":")

numbers_line = float(line[index_colon + 1: ])

print(numbers_line)



