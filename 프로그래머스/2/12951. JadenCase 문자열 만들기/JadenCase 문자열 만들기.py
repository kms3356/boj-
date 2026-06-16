def solution(s):
    sList = s.split(' ')
    newList = []
    blankCount = 0
    for word in sList:
        if word == '':
            blankCount += 1
        else:
            word = word[0].upper() + word[1:].lower()
            if blankCount > 0:
                word = ' ' * blankCount + word
                blankCount = 0
            newList.append(word)
    if blankCount > 0:
        newList.append(' '* (blankCount-1))
    return ' '.join(newList)