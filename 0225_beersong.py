word = "bottles"    # Assign the value "bottles" (a string) to a new variable called "word"
for beer_num in range(99, 0, -1):   # 99~0까지 1씩 줄어드는 반복문 실행, 변수명은 beer_num
    print(beer_num, word, "of beer on the wall")
    print(beer_num, word, "of beer")
    print("Take one down.")
    print("Pass it around.")    # 해당하는 beer_num, word와 함께 문구 4줄 출력
    if beer_num == 1:           # 만약 beer_num이 1이면,
        print("No more bottles of beer on the wall.")   # 맥주가 없다는 문구 출력
    else:                       # beer_num이 1이 아닌 모든 경우에는
        new_num = beer_num - 1  # beer_num을 1씩 감소시킴
        if new_num == 1:        # 감소하다가 1을 만나면,
            word = "bottle"     # word를 bottle로 설정
        print(new_num, word, "of beer on the wall.")    # beer_num이 1일경우 new_num과 word와 함께 문구 출력
    print()


>>> prices = []
>>> temp=s=[32.0, 212.0, 0.0, 81.6, 100.0, 45.3]  
>>> words=['hello', 'world']
>>> car_details = ['toyota', 'RAV4', 2.2, 60807]
>>> everything = [prices, temps, words, car_details]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'temps' is not defined
>>> odds_and_ends = [[1, 2, 3], [['a', 'b', 'c'], ['One', 'Two', 'Three']] 