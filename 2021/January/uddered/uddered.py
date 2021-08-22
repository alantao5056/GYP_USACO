alphabet = input()

alphabet_dict = {letter:num for num, letter in enumerate(alphabet)}

word = input()

loop_counter = 1
for i in range(1, len(word)):
  if alphabet_dict[word[i]] <= alphabet_dict[word[i - 1]]:
    loop_counter += 1
print(loop_counter)