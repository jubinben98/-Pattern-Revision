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
    9: [
        input_dict(":orange[N] が　あります/わかります", ["車があります。"], ["I have a car."]),
        input_dict(":orange[N] が　すきです/きれいです/じょうずです/へたです。", ["わたしは　日本りょうり　が　すきです。"], ["I like Japanese dish."]),
        input_dict("どんな　:orange[N]", ["どんな　スポーツ　が　すきですか？"], ["Which sports do you like?"]),
        input_dict("よく/だいたい/たくさん/少し/あまり/ぜんぜん", ["わたしは　日本ご　が　よく　わかります。",
                                                            "わたしは　日本ご　が　だいたい　わかります。",
                                                            "わたしは　日本ご　が　少し　わかります。",
                                                            "わたしは　日本ご　が　あまり　わかりません。",
                                                            "わたしは　日本ご　が　ぜんぜん　わかりません。",
                                                            "お金　が　たくさん　あります。",
                                                            "お金　が　少し　あります。",],
                                                            ["I understand English well.", "I understand English mostly. (very well)", "I understand English a little.",
                                                             "I do not understand English very well.", "I do not understand English at all."]),
        input_dict("〜から、〜", ["じかん　が　ありません　から、しんぶん　を　よみません。"], ["I don't read newspaper because, I don't have time."]),
        input_dict("どして", ["どして　あさ　しんぶん　を　よみませんか。"], ["Why don't you read newspaper in the morning?"]),
    ],
    10: [
        input_dict(":orange[N] が　あります/います", ["車があります。", "犬がいます。"], ["I have a car.", "There is a dog."]),
        input_dict(":orange[Place] に :orange[N] が　あります/います", ["わたしのへやにつくえがあります。", "じむしょうにミラさんがいます。"], ["There is a desk in my room.", "Mr. Mira is in the office."]),
        input_dict(":orange[N]は :orange[Place] に あります/います", ["ミラさんはじむしょにいます。"], ["Mr. Mira is in the office."]),
        input_dict(":orange[N1 (thing/person/place)]　の　:orange[N2(position)", ["つくえのうえにしゃしんがあります。"], ["There is a photograph on the desk."]),
        input_dict(":orange[N1] や　:orange[N2] など", ["はこの中に　しゃしん　や　てがみ　など　が　あります。"], ["There are some photographs, letters and other things in the box."]),
    ],
    11: [
        input_dict("(Quantifiers) :orange[N] + particle :orange[quantity]", ["りんご　を　よっつ　かきました。", "がいこくのがくせい　が　ふたり　います。", "くにで　二かがつ　日本穂　を　べんきょします。"], ["I brought four apples.", "There are two foreign students.", "I studied Japanese for 2 months in my home country."]),
        input_dict("(Quantifiers)　Asking how many.", ["みかん　を　いくつ　かいましたか？",
                                                      "この かいしゃ　に　がいこくじんが　なんにん　いますか？",
                                                      "まいばん　何じかん　日本語を　べんきょしますか？",
                                                      "どのくらい　日本語　を　べんきょしますか？",
                                                      "ときょ　から　おさか　まで　どのくらい　かかりますか？",
                                                      "がっこに　せんせい　が　三十にん　ぐらい　います。"],
                   ["How many Mandarin Oranges did you buy?",
                    "How many foreign people are there in this company?",
                    "How many hours do you study Japanese every night?",
                    "How long did you study Japanese for?",
                    "How long does it take from Tokyo to Osaka?",
                    "There is about 30 teachers in our school."]),
        input_dict(":orange[Quantifier Time period]に ー回　:blue[V]", ["一かげつに　二回　えいが　を　みます。"], ["I go to see film about twice a month."]),
        input_dict(":orange[Quantifier]　だけ/:orange[N]　だけ", ["パワでんき　に　がいこくじんの　しゃいん　が　ひとつ　だけ　います。", "やすみは　にちようび　だけ　です。"], ["There is only one foreign employee in Power Electric.", "Sunday is my only day off."]),
    ],
    12: [
        input_dict(":orange[N1]は　:orange[N2]より　:blue[adjective]です。", ["このくるまは　あの　車　より　おおき　です。"], ["This car is bigger than that car."]),
        input_dict(":orange[N1]と　:orange[N2]と　どちらが　:blue[adjective]ですか。.. :orange[N1/N2]の　ほうが　:blue[adjective]です", ["やきゅうと　サッカと　どちらが　おもしろいですか？　...　サッカの　ほうが　おもしろいです。"], ["Which (do you think) is more interesting, soccer or baseball. (I think) soccer is more interesting."]),
        input_dict(":orange[N1][のなか]で　なに/だれ/どこ/いつ　が　いちばん　:blue[adjective]ですか。", ["日本りょりで　何が　いちばん　おいしい　ですか？", "１年　で　いつが　いちばん　さむいですか？"],
                   ["Which of all Japanese dishes is the most delicious?", "What's the coldest time of the year?"])
    ],
    13: [
        input_dict(":orange[N] が　ほしいです。", ["車が　ほしいです。"], ["I want a car."]),
        input_dict(":blue[Vます-form]たいです。", ["おきなわ　へ　いきたい　です。"], ["I want to go to Okinawa."]),
        input_dict(":orange[N(place)]へ　:blue[Vます-form]に　いきます/きます/かえります。", ["こべへ　かいものに　いきます。"], ["I am going shopping in Kobe."]),
    ]
}