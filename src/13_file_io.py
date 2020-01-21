"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('C:/Users/carlo/CompSci/Intro-Python-I/src/foo.txt') as x:
    read_data = x.read()
    print(read_data)
    x.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
writearoo = open('C:/Users/carlo/CompSci/Intro-Python-I/src/bar.txt', 'w+')
lines = ('slayer', 'megadeth', 'metallica')
for line in lines:
    writearoo.write(f'{line} \n')
read_lines = writearoo.read()
print(read_lines)
writearoo.close()