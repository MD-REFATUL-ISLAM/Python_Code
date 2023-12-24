
#separator and end new line with no spaces.
print('G','F', sep="", end="")
print('G')
# output would be ---> GFG

# use space only in sep
# which seprate the first G and F
print('G','F', sep=" ", end="")
print('G')
# output would e ---> G FG

# use space in sep and end
# which seprate the first G and F
print('G','F', sep=" ", end=" ")
print('G')
# output would be ---> G F G

print("12","12","2024", sep="-", end="\n")
print("orchie","oronie","rafee",sep=", ")


'''
GFG
G FG
G F G
12-12-2024
orchie, oronie, rafee
'''