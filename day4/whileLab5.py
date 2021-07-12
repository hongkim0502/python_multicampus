while True :
    word = input("문자열을 입력하시오 :")
    worldlength = len(word)
    if worldlength == 0 :
        break
    elif 5 <= worldlength <= 8 :
        continue
    elif worldlength < 5 :
        result = '*' + word + '*'
    elif worldlength > 8 :
        result = "$" + word + "$"

    print("유효한 입력 결과 : ", result)