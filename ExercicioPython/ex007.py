# Display two question on the screen to find the note

note1 = float(input('Enter a first note: '))
note2 = float(input('Enter a second note: '))

# Average grades

Average = (note1 + note2) / 2

# Display the result on the screen

print('A average between {} and {} is: {:.1f}'.format(note1, note2, Average))
