a = {'월':['33','25'],'화':['33','25'],'수':['33','25'],'목':['33','24'], '금':['32','23'],'토':['33','23'],'일':['32','24']}

user=input('요일명을 한글로 입력하세요 : ')
if user in a :
    print(user,'요일의 최저온도는 ',min(a[user]),' 이고 최고 온도는 ',max(a[user]),'입니다')
else :
    print(user,'요일의 정보를 찾을 수 없습니다')
