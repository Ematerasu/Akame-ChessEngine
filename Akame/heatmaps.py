#                       PATTERN
# 
#                   [[a8, b8, c8, d8, e8, f8, g8, h8],
#                    [a7, b7, c7, d7, e7, f7, g7, h7],
#                    [a6, b6, c6, d6, e6, f6, g6, h6],
#                    [a5, b5, c5, d5, e5, f5, g5, h5],
#                    [a4, b4, c4, d4, e4, f4, g4, h4],
#                    [a3, b3, c3, d3, e3, f3, g3, h3],
#                    [a2, b2, c2, d2, e2, f2, g2, h2],
#                    [a1, b1, c1, d1, e1, f1, g1, h1]]



WHITE_PAWN_HEATMAP =[[10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0],
                    [7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0],
                    [3.0, 4.0, 5.0, 6.0, 6.0, 5.0, 4.0, 3.0],
                    [1.0, 1.0, 3.0, 4.0, 4.0, 3.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0, 2.0, 2.0, 0.5, 1.0, 1.0],
                    [0.5, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, 0.5],
                    [1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0],
                    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],]

BLACK_PAWN_HEATMAP = WHITE_PAWN_HEATMAP[::-1]

WHITE_KNIGHT_HEATMAP =[[-2.0, -1.0, 0.0, 0.0, 0.0, 0.0, -1.0, -2.0],
                       [-1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, -1.0],
                       [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
                       [-1.0, 1.0, 1.5, 2.0, 2.0, 1.5, 1.5, 0.0],
                       [-1.0, 1.0, 1.5, 2.0, 2.0, 1.5, 1.5, 0.0],
                       [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
                       [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0],
                       [-2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -2.0],]

BLACK_KNIGHT_HEATMAP = WHITE_KNIGHT_HEATMAP[::-1]

WHITE_BISHOP_HEATMAP =[[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
                       [0.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 0.0],
                       [-1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, -1.0],
                       [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0],
                       [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0],
                       [-1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, -1.0],
                       [0.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 0.0],
                       [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],]

BLACK_BISHOP_HEATMAP = WHITE_BISHOP_HEATMAP[::-1]

WHITE_ROOK_HEATMAP =  [[0.0, 0.0, 1.0, 3.0, 3.0, 1.0, 0.0, 0.0],
                       [0.0, 0.0, 1.0, 3.0, 3.0, 1.0, 0.0, 0.0],
                       [1.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, 1.0],
                       [1.0, 1.0, 1.5, 1.5, 1.5, 1.5, 1.0, 1.0],
                       [1.0, 1.0, 1.5, 1.5, 1.5, 1.5, 1.0, 1.0],
                       [1.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, 1.0],
                       [0.0, 0.0, 1.0, 3.0, 3.0, 1.0, 0.0, 0.0],
                       [0.0, 0.0, 1.0, 3.0, 3.0, 1.0, 0.0, 1.0],]

BLACK_ROOK_HEATMAP = WHITE_ROOK_HEATMAP[::-1]

WHITE_QUEEN_HEATMAP = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],]

BLACK_QUEEN_HEATMAP = WHITE_QUEEN_HEATMAP[::-1]

WHITE_KING_HEATMAP = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],]

BLACK_KING_HEATMAP = WHITE_KING_HEATMAP[::-1]

TRANSLATE_COORDS ={
    'a' : 0,
    'b' : 1,
    'c' : 2,
    'd' : 3,
    'e' : 4,
    'f' : 5,
    'g' : 6,
    'h' : 7
}

GET_MAP = {
            'p' : BLACK_PAWN_HEATMAP,
            'n' : BLACK_KNIGHT_HEATMAP,
            'b' : BLACK_BISHOP_HEATMAP,
            'r' : BLACK_ROOK_HEATMAP,
            'q' : BLACK_QUEEN_HEATMAP,
            'k' : BLACK_KING_HEATMAP,
            'P' : WHITE_PAWN_HEATMAP,
            'N' : WHITE_KNIGHT_HEATMAP,
            'B' : WHITE_BISHOP_HEATMAP,
            'R' : BLACK_ROOK_HEATMAP,
            'Q' : WHITE_QUEEN_HEATMAP,
            'K' : WHITE_KING_HEATMAP
        }