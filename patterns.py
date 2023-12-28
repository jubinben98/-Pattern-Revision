from utils import input_dict

# patterns dictionary from each chapter
PATTERN_DICT = {
    1: [
        input_dict(":orange[N1] wa :orange[N2] desu", ["わたしわ　マイク　ミラ　です。"], ["I'm Mike Miller."]),
        input_dict(":orange[N1] wa :orange[N2] ja (dewa) arimansen", ["サントスさんは　がくせい　じゃありません。"], ["Mr. Santosh is not a student."]),
        input_dict(":orange[N1] wa :orange[N2] desu ka", ["ミラさんは　アメリカじん　ですか。"], ["Is Mira san American?"]),
        input_dict(":orange[N] mo", ["ミラさんは　かいしゃいん　です。グプタさんも　かいしゃいん　です。"], ["Mira san is company employee. Mr. Gupta san is also company employee."]),
        input_dict(":orange[N1] no :orange[N2]", ["ミラさんは　IMC　の　しゃいん　です。"], ["Mr. Mira is an employee of IMC."]),
    ],
    2:[
        input_dict(":orange[N1] no :orange[N2] (for things)", ["これは　コンピュタ　の　ほん　です。"], ["This is a book on computer."]),
    ]
}