
from game import Game
from suspect import Suspect
from room import Room
from item import Item
from plot import Plot


def scenarios():
    # Przedmioty
    lampa = Item("lampa", "Lampa z odciskami palców.")
    list = Item("list", "Tajemniczy list miłosny.")
    noz = Item("nóż", "Krwawy nóż kuchenny.", is_proof=True)

    # Pokoje
    kuchnia = Room("Kuchnia", "Stara kuchnia z podejrzanie czystym stołem.", noz)
    salon = Room("Salon", "Rozrzucone meble sugerują walkę.", lampa)
    sypialnia = Room("Sypialnia", "Łóżko niezasłane, na podłodze list.", list)

    # Podejrzani
    anna = Suspect("Anna", "Była narzeczona ofiary.",
                   dialogue='Mój były to fatalny człowiek, ale ja nie zabiłabym go.',
                   reactions={
        "list": "To nie mój list! Nie pisałam go!",
        "nóż": "Nigdy nie trzymałam tego noża w ręce!"
    })
    bartek = Suspect("Bartek", "Współlokator z przeszłością kryminalną.",
                     dialogue='Gdzie ja posiałem ten... Zabójstwo? O nie, to nie ja!',
                    reactions= {
        "lampa": "To nie moje odciski, przysięgam!"
    }, is_criminal=True)

    szminka = Item('Szminka', 'Różowa szminka znaleziona w korytarzu. Została już użyta.', is_proof=True)
    mop = Item('Mop', 'Stary mop znaleziony w schowku. Lekko czerwony.')
    lusterko = Item('Lusterko', 'Pozłacane lusterko, lekko zabrudzone.')
    autograf = Item('Autograf', 'Chustka z autografem, na jej drugiej stronie widać czerwoną plamę')

    korytarz = Room('Korytarz', 'Korytarz pełen zdjęć modeli i produktów przez nich reklamowanych. Ludzie przechodzą tu w te i we wte.\nUdaje ci się zauważyć białą chustkę na ziemi',
                    autograf)
    vip = Room('Pokój Vip','Pokój vip zawierający m.in. telewizor, porcelanowy stolik, garderobę i skórzaną sofę. Właśnie na niej spoczywa umarły,'
                           'przebity nożem w serce.\n Śledztwo wykazało kilka śiniaków i zadrapań na ciele zamordowanego, purpurowy szalik na szyi którego nie widziano wcześniej oraz'
                            'różowe ślady na ręce zabitego. W lewym rogu widzisz leżące lusterko', lusterko )
    schowek = Room('Schowek', 'Schowek woźnego. Bardzo ciasny i pełen rupieci. Z morza przedmiotów udaje ci się wyłowić podejrzany mop', mop)

    tylne_wyjscie = Room('Tylne wyjście', 'Znajdujesz wyjście prowadzące prosto na zewnątrz. Przykuwa tam twoją uwagę odsunięta klapa od śmietnika '
                                          'w której znajdujesz szminkę.', szminka)

    carmen = Suspect('Carmen', 'Niezwykle popularna modelka. Ma wspólnę historię z ofiarą. '
                    'Pewna siebie do poziomu aroganctwa. Doskonale zna się na tajemnicach przetrwania w biznesie. Widziana z ofiarą godzinę przed zabójstwem.',
                     dialogue = 'Kompletna katastrofa - miałam przygotowaną nową Su Kiecce specjalnię na tą galę!'
                                'Oby szybko znaleźli nowy termin... o Gio? \n Tak to również tragedię. Świat pocułunków doprawdy stracił mistrza sztuki...',
                     reactions={
                         'szminka': 'O ten rupieć? Proszę kochanie, taka taniość nie powinna dotykać moich ust. '
                                    'Muszę za to przyznać, gdy korzystałam z niej na początku kariery była całkiej wytrzymała.\n'
                                    'Nawet po solidnym szorowaniu można zauważyć ślady.',
                         'lusterko': 'A! Mogę zobaczyć? Tak.. tak... moje włosy już są w pełnej formie. O nie wiem nic więcej o nim, '
                                      'ale powienien pan dbać o czystość swoich rzeczy'
                     })
    louis = Suspect('Louis', 'Starszy woźny. Dawniej za jako ochraniasz. Oschły, tęskni za dawnymi czasami. '
                             'Widziany z ofiarą 15 min przed śmiercią',
                    dialogue = 'Te modnisie za dużo sobie pozwalają! Dawniej wszyscy siebie szanowali, teraz posuną się nawet do noża czy czymkolwiek\n'
                                'gamonia zabili! Żeby do tego podejrzewać biednego Louis o coś takiego... Ja wam powiem, to pewnie ta szurnięta Carmen!',
                    reactions ={
                        'mop': 'A pewno, że mój, używam go od dobrego roku. Czerwień? Jedna dziunia wylała wino dziś rano. Nie mów partaczu, że myślałeś że to krew,'
                               'gdyby ktoś taki pracował w policji 40 lat temu...'
                    }
    )
    monica = Suspect('Monica', 'Wschodząca modelka, to jej pierwsza Wielka Gala. Pracowita i skromna. Miała dobrą relację z ofiarą. '
                               'Ostatnio widziania z nim pół godziny przed śmiercią.',
                     dialogue='Oh co za katastrofa! Giorgio był wspaniałym przyjacielem, pomagał mi wieloktronie w mojej karierze. Nie wierzę że ktoś go mógł zabić. \n'
                              'Chociaż, nie miał on dziś kłótni z panem woźnym? Och gdybym tylko zauważyła więcej, przepraszam że nie mogę bardziej pomóc!',
                     reactions={
                         'szminka': 'Och ta szminka, o nie nie, raczej nie moja. Kolor pasuje? A, faktycznie być może jest moja?\nO zgubiłem szminkę, nie do wiary! Czy mogę ją jednak  spowrotem? '
                                    'Dowód w sprawie? Och...'
                     },
                     is_criminal = True)

    elise = Suspect('Elise', 'Makijażystka, pracuje tu od miesiąca. Gadatliwa i przyjazna. Znalazła ciało ofiary',
                    dialogue='Merde! Jakby ten dzień nie mógł być bardziej stresujący. Aaaa nie dość że zapomniałe swoich materiałów i przyszłam spóźniona,'
                              'to jeszcze pan Giovanna. Może był zbyt ekscentryczny ale żeby go zabić? Niestety nie mogę pomóc, nikogo nie widziałam,'
                              'pan Giovanna leżał przy kanapie tak jak go znaleźli. Czy to oznacza, że jestem podejrzana? Proszę, nie chcę stracić tej pracy, nikogo nie zabiłam!',
                    reactions={
                            'szminka': 'O wspaniały kolor! Niestety nie mój, ale chciałabym z niej skorzystać. ',
                                'mop': "Wydaje mi się że to pana Louis'a. On sprawia wrażenie drania, ale to złoty człowiek jeśli bliżej się go pozna",
                        'autograf': 'Poznaje to pismo, to pana Giovanny! Pan Giovanna jest rozchwytywany przez swoich fanów, on sam zdaje się uwielbiać '
                                    'swoją popularność. Szczególnie przez fanki.'

    })
    # Scenariusz
    return [Plot(
        name = 'Nożownik uderza!',
        start_description="Znaleziono ciało w mieszkaniu. Musisz ustalić kto jest winny.",
        suspects=[anna, bartek],
        rooms=[kuchnia, salon, sypialnia],
        end_description= 'Z łatwością wskazujesz miłośnika noży jako sprawcę. Poddaje się bez walki. Dobra robota detektywie, to dopiero początek'
    ), Plot(name = 'Nowy krzyk mody',
            start_description=
            'Na otwarcię Wielkiej Francuskiej Gali Mody Nowoczesnej, '
            'miało się zjawić tysiącę gości, w ustalonej godzinie otwarcie w całym budynku jest być może z kilka dziesiąt osób. Dlaczego? \n'
            'Tragedie uderzyła popularną galę. W jednej z vipowskich szatni, krzyk makijażystki oznajmił znalezienie'
            'ciała znanego modela - Giorgio Giovanna.\nDetektyw zjawił się na scenie. Czy z wytypowanych przez niego kilku podejrzanych '
            'wskaże zabójcę mody?',
            suspects=[carmen,louis,monica,elise],
            rooms=[korytarz,vip,schowek,tylne_wyjscie],
            end_description='Zbierasz podejrzanych w jednym pomieszczeniu. Carmen i Louis wydają się zirytowani, podczas gdy Monica i Elise są widocznie zestresowane.\n'
                            'Stwierdzasz, że zabity, miał częstę relacje z kobietami. Dzisiaj spotkał się z jedną z jego fanek w vip roomie, którą rozmowę podsłuchała Monica.\n'
                            'Monica spotykała się z Giorgio w ukryciu, myśląc, że w końcu popularny model oficjalnie to ogłosi.\nZrozpaczona rozpustnictwem swojej miłości,'
                            'czekała na okazję gdy będzie w pokoju sam, która nadarzyła się po kłótni z woźnym. Zakradła się do środka, i po małej szarpaninie, zabiła modela.\n'
                            'Uszło by jej to na sucho, gdyby nie szminka, której nie udało się w pełni wytrzeć z zabitego po szarpaninie.\n'
                            'Ukrycie szminki w śmietniku zakończyło się porażką. Po swojej wypowiedzi, Monica zapłakana przyznała się do winy.\n'
                            'Świat mody może wrócić do normy, dobra robota detektywie.\n'

            )]



if __name__ == "__main__":
    plots = scenarios()
    game = Game(plots)
    game.choose_scenario()
