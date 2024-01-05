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
    7: [
        input_dict(":orange[N (tool/means)] で :blue[V]", ["はし　で　たべます。", "日本でリポトをかきます。"], ["I eat with chopsticks.", "I'm going to write the report in Japanese."]),
        input_dict("'Word/Sentence'は　ーで何ですか。", ["’Thank you’は　日本ごで何ですか。"], ["What is 'Thank you' in Japanese?"]),
        input_dict(":orange[N1]に :orange[N2]　を　あげます/かします/おしえます", ["わたしは　チッカちゃん　に　はなっを　あげました。"], ["I gave flowers to Tikka."]),
        input_dict(":orange[N1]に :orange[N2]　を　もらいます/かります/ならいます", ["わたしは　チッカちゃん　に　日本ご　を　ならいます。"], ["I'm learning Japanese from Tikka."]),
        input_dict("もう　:blue[Vました]", ["父は　もう　ねました。"], ["Dad already slept."]),
    ],
    8: [
        input_dict(":orange[N]は　な-adj(without な)　です。|| :orange[N]は　い-adj(~い)　です。", ["せんせいは　しんせつ　です。", "しごとは　おもしろい　です。"], ["Teacher is kind.", "Work is interesting."]),
        input_dict("な-adj(な)　:orange[N] || い-adj(~い) :orange[N]", ["せんせいは　しんせつな　ひと　です。", "ならは　ふるい　まち　です。"], ["Teacher is a kind person.", "Nara is an old city."]),
        input_dict("〜が、〜", ["日本の　たべものは　おいしい　です　が　たかい　です。"], ["Japanese food is tasty but expensive."]),
        input_dict("とても/あまり", ["ワンさんは　とても　きれい　です。", "ワンさんは　あまり　きれい　じゃありません。"], ["Mr. Wan is beautiful.", "Mr. Was is not very beautiful."]),
        input_dict("な-adj(without な) じゃありません　|| い-adj　くないです。", ["ワンさんは　きれい　です。", "この　かいしゃは　あたらしくないです。"], ["Mr. Wan is beautiful.", "This company is not new."]),
        input_dict(":orange[N]は　どうですか。", ["日本のたべものは　どうですか。"], ["How is the Japanese food?"]),
        input_dict(":orange[N1]は　どんな :orange[N2] ですか。", ["ワンさんは　どんな　ひとですか。"], ["How is Mr. Wan as a person?"]),
    ],
}