gender = int(input('여성이면 1, 남성이면 0을 입력하세요: '))
height = int(input('당신의 키는 얼마입니까?'))
waist = int(input('당신의 허리 둘레는 얼마입니까?'))

RFM = 64 - (20 * (height / waist)) + 12 * gender

print('당신의 RFM은', RFM)