#encoding=utf8

import guess_language

tests = [
            ("This is a test of the language checker", "en"),
            ("Verifions que le détecteur de langues marche", "fr"),
            ("Sprawdźmy, czy odgadywacz języków pracuje", "pl"),
            ("авай проверить  узнает ли наш угадатель русски язык", "ru"),
            ("La respuesta de los acreedores a la oferta argentina para salir del default no ha sido muy positiv", "es"),
             ("Сайлау нәтижесінде дауыстардың басым бөлігін ел премьер министрі Виктор Янукович пен оның қарсыласы, оппозиция жетекшісі Виктор Ющенко алды.", "kk"), # Kazakh
            ("милиция ва уч солиқ идораси ходимлари яраланган. Шаҳарда хавфсизлик чоралари кучайтирилган.", "uz"), # uzbek
            ("көрбөгөндөй элдик толкундоо болуп, Кокон шаарынын көчөлөрүндө бир нече миң киши нааразылык билдирди.", "ky"), # kyrgyz
            ("yakın tarihin en çekişmeli başkanlık seçiminde oy verme işlemi sürerken, katılımda rekor bekleniyor.", "tr"), 
             ("Daxil olan xəbərlərdə deyilir ki, 6 nəfər Bağdadın mərkəzində yerləşən Təhsil Nazirliyinin binası yaxınlığında baş vermiş partlayış zamanı həlak olub.", "az"), # Azerbaijani

             (" ملايين الناخبين الأمريكيين يدلون بأصواتهم وسط إقبال قياسي على انتخابات هي الأشد تنافسا منذ عقود",  "ar"),
             ("Американське суспільство, поділене суперечностями, збирається взяти активну участь у голосуванні",  "uk"), # ukrainian
             ("Francouzský ministr financí zmírnil výhrady vůči nízkým firemním daním v nových členských státech EU",  "cs"), # czech
             ("biće prilično izjednačena, sugerišu najnovije ankete. Oba kandidata tvrde da su sposobni da dobiju rat protiv terorizma",  "hr"), # croatian
             (" е готов да даде гаранции, че няма да прави ядрено оръжие, ако му се разреши мирна атомна програма",  "bg"), # bulgarian
             ("на јавното мислење покажуваат дека трката е толку тесна, што се очекува двајцата соперници да ја прекршат традицијата и да се појават и на самиот изборен ден.",  "mk"), # macedonian
             ("în acest sens aparţinînd Adunării Generale a organizaţiei, în ciuda faptului că mai multe dintre solicitările organizaţiei privind organizarea scrutinului nu au fost soluţionate",  "ro"), # romanian
             ("kaluan ditën e fundit të fushatës në shtetet kryesore për të siguruar sa më shumë votues.",  "sq"), # albanian
             ("αναμένεται να σπάσουν παράδοση δεκαετιών και να συνεχίσουν την εκστρατεία τους ακόμη και τη μέρα των εκλογών",  "el"), # greek
             (" 美国各州选民今天开始正式投票。据信，",  "zh"), # chinese
             (" Die kritiek was volgens hem bitter hard nodig, omdat Nederland binnen een paar jaar in een soort Belfast zou dreigen te veranderen",  "nl"), # dutch
             ("På denne side bringer vi billeder fra de mange forskellige forberedelser til arrangementet, efterhånden som vi får dem ",  "da"), # danish
             ("Vi säger att Frälsningen är en gåva till alla, fritt och för intet.  Men som vi nämnt så finns det två villkor som måste",  "sv"), # swedish
             ("Nominasjonskomiteen i Akershus KrF har skviset ut Einar Holstad fra stortingslisten. Ytre Enebakk-mannen har plass p Stortinget s lenge Valgerd Svarstad Haugland sitter i",  "nb"), # norwegian
             ("on julkishallinnon verkkopalveluiden yhteinen osoite. Kansalaisten arkielämää helpottavaa tietoa on koottu eri aihealueisiin",  "fi"), # finnish
             ("Ennetamaks reisil ebameeldivaid vahejuhtumeid vii end kurssi reisidokumentide ja viisade reeglitega ning muu praktilise informatsiooniga",  "et"), # estonian
             ("Hiába jön létre az önkéntes magyar haderő, hiába nem lesz többé bevonulás, változatlanul fennmarad a hadkötelezettség intézménye",  "hu"), # hungarian
             ("հարաբերական",  "hy"), # armenian
             ("Hai vấn đề khó chịu với màn hình thường gặp nhất khi bạn dùng laptop là vết trầy xước và điểm chết. Sau đây là vài cách xử lý chú", "vi"),
#              ("ii",  guess_language.UNKNOWN),
             
             # This text has a mix of Hirigana, Katakana and CJK which requires the fix for issue:3 to classify correctly
             ("トヨタ自動車、フィリピンの植林活動で第三者認証取得　トヨタ自動車(株)（以下、トヨタ）は、2007年９月よりフィリピンのルソン島北部に位置するカガヤン州ペニャブラン", 'ja'),
        ]

for text,name in tests:
    print guess_language.guessLanguage(text), name


