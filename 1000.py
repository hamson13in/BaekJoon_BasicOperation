#1000번 문제 A+B
A, B = map(int, input().split())#<- split() : 띄어쓰기, 엔터 구분 / 문자열
                                #메소드로, input()의 문자열에 대해 실행됨
                                #ex) s=input(){s에 '3 5' 입력 가정} , s.split() 하면
                                #s리스트에 있는 값이 구분, [3, 5] 됨
#정리하자면, 사용자에게 정수 'A B' 받음->split이 구별, map int가 두 수임 알고 정수 정의
print(A+B)
