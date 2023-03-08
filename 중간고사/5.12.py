word = str(input('단어를 입력하세요 : '))

for i in range(len(word)):
    if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u':
       print(word[0:i])
       break
    



    