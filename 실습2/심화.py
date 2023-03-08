king = int(input('찾은 킹의 개수를 입력하세요:'))
queen = int(input('찾은 퀸의 개수를 입력하세요:'))
rook = int(input('찾은 룩의 개수를 입력하세요:'))
bishop = int(input('찾은 비숍의 개수를 입력하세요:'))
knight = int(input('찾은 나이트의 개수를 입력하세요:'))
pawn = int(input('찾은 폰의 개수를 입력하세요:'))

king = 1 - king
queen = 1 - queen
rook = 2 - rook
bishop = 2 - bishop
knight = 2 - knight
pawn = 8 - pawn

print(king, queen, rook, bishop, knight, pawn)