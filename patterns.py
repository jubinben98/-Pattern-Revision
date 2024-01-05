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
    ],
    3:[
        input_dict(":orange[N] wa :green[place] desu", ["おてあらいは　あそこ　です。", "でんわは　二かい　です。"], ["The toilet is over there.", "Telephone is on the second floor."]),
        input_dict(":orange[N1] no :orange[N2] (things from a country)", ["日本の　くるま　です。"], ["Car from Japan."]),
    ],
    4:[
        input_dict(":orange[N (time)] ni :blue[V]", ["七じに　おきます。"], ["I get up at seven o'clock."]),
        input_dict(":orange[N1] kara :orange[N2] made", ["しごとは　九じ　から　五じ　まで　です。", "げつよび　から　きんよび　まで　はたらきます。"], ["I work from 9 o'clock to 5 o'clock.", "I work from Monday to Friday."]),
        input_dict(":orange[N1] to :orange[N2]", ["ぎんこの　やすみは　どよびとにちよび　です。"], ["The bank is closed on Saturday and Sunday."]),
    ],
    5: [
        input_dict(":orange[N (place)] e ikimasu/kimasu/kaerimasu", ["びょいん　へ　いきます", "日本へ　きました", "うち　へ　かいります"], ["I am going to hospital.", "I came to Japan.", "I'm going home."]),
        input_dict("Doko [e] mo ikimasen/ikimasendeshta", ["どこも　いきません", "どこも　いきませんでした"], ["I not going anywhere.", "I didn't go anywhere."]),
        input_dict(":orange[N (vehicle)] de ikimasu/kimasu/kaerimasu", ["くるま　で　びょいん　へ　いきます", "でんしゃ　で　きます"], ["I am going to hospital by car.", "I cam by train."]),
        input_dict(":orange[N (person/animal)] to :blue[V]", ["かずこ　と　日本へ　いきます。", "チッカちゃん　と　きょと　へ　いきます。"], ["I am going to Japan with my family.", "I am going to Kyoto with Tikka."]),
    ],
    6:[
        input_dict(":orange[N] を　:blue[V (transitive)]", ["ベエル　を　のみます。"], ["I drink beer."]),
        input_dict(":orange[N] を　します。", ["テニスをします"], ["I play tennis."]),
        input_dict(":orange[N (place)] で　:blue[V]", ["えき　で　しんぶん　を　かいます。"], ["I am going to by newspaper from the station."]),
        input_dict(":blue[V] ませんか。", ["いしょに　ひるごはん　を　たべませんか。"], ["Would you like to have lunch with us."]),
        input_dict(":blue[V] ましょう。", ["きょと　へ　いきましょう。"], ["Let's go to Kyoto."]),
    ],

}