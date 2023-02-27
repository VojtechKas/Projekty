
answer = input("Chceš začít hru?  (ano/ne)  ")

if answer.lower().strip() == "ano":

    answer = input("Probouzíš se s bolestmi hlavy, v polorozpadlé cele. Máš částečnou amnézii a tak si nevzpomínáš na to jak si se zde ocitl. Ovšem instink ti radí abys ses odsud co nejrychleji dostal pryč.""Po omrknutí cely jsi přišel na to že: Mříže jsou už značně zrezlé a dali by se s trochou námahy vyrvat nebo se by ses mohl pokusit protáhnout malou skulinkou do cely vedle tebe." "Co uděláš? (protáhnout se/vyrvat mříže) ").lower().strip()

    if answer == "vyrvat mříže" :
        answer = input("Cloumáš mřížema jak nejvíc to jen jde. Rachotu vydáváš jak za sedm mužů. Rázem tě přehluší ještě silnější zvuk dunění. Celá tvoje cela začala dunit. Za tvými zády probourala obrovská ruka zeď a vytáhle tě z cely. Byl to zlobr, který by si tě ani nevšiml ovšem díky tomu tvýmu kraválu už tě roztrhává na kusy. Jsi mrtvý")

    if answer == "protáhnout se":

        answer = input("Protáhl si se do druhé cely, která byla značně zchátralejší než tvoje původní a tak jsi se bezproblémů dostal na chodbu a je jen na tobě jestli se vydáš vpravo či vlevo. Při pohledu do prava vidíš velice slabé matné světlo, kdežto zleva se line jakýsi smrdutý zápach. Kudy se vydáš? (vpravo/vlevo)").lower().strip()

        if answer == "vlevo":
            answer = input("Vydal ses tedy vlevo, připadá ti že se něco tam na konci chodby hejbe co to jen je říkáš si. Jdeš k té věci blíž a blíž. Zničeho nic na tebe vyskočí  šestiruký mrchožrout a prokousne ti lebku. Jsi mrtvý")


        if answer == "vpravo":

            answer = input("Jdeš ke světlu které je s každým dalším krokem silnější a silnější až nakonec dojdeš do temné místnosti osvětlenou jednou jedinou svíčkou. Paprsky světel ti odhalují víc detailů o místnosti. V místnosti je asi deset postelí. A vypadáto že něco si zrovna dává šlofíka v posteli. Vypadá to že je jediný ale kdo ví. Poslední řadu postelí už svíčka neosvětlí. Co uděláš? Můžeš zariskovat čímž narychlo omrkneš místnost a podíváš se po užitečných předmětech nebo potichu našlapovat k východu. (omrknout/našlapovat)").lower().strip()

            if answer == "našlapovat" :
                answer = input("Pomalinku, potichoučku jdeš ke dveřím. Po otevření dveří vejdeš do další chodby. Dunění otřásá celou základnou, křik se rozlíhá ze všech stran. Ve vzduchu jde cejtit strašný puch. Pokračuješ dál chodbou, když tu náhle, zasáhne tě šíp. Jsi mrtvý.")

            if answer == "omrknout":

                answer = input (" U postele vedle kreatury kterou nemůžeš rozpoznat leží opotřebovaný meč, kdežto na opačné straně místnosti se leskne štít, avšak slouží jako zarážka pod skříň, aby byla vyvážená. Rozum ti radí ať jdeš jen pro jednu věc a rychle odtamtud zmizíš, ale rozhodnutí je zcela na tobě. (štít/meč/obojí)").lower().strip()

                if answer == "štít" :
                    answer = input("Hrubě jsi vyrval štít zpoza skříně. Udělalo to hrozný rachot a vzbudilo spáče. Zasvištění meče. Spáč nyní snadno rozpoznatelný jako bandita ti oddělil hlavu od těla. Jsi mrtvý")

                if answer == "meč" :
                    answer = input ("Potichu jsi se dostal k meči a zároveň jsi konečně poznal spáče. Byl to bandita. Unesli a zavřeli tě sem banditi ale proč? Na tom teď nesejde máš v ruce meč. V hlavě se ti tak rodí velmi krvavá myšlenka. (zabít/nezabít)").lower().strip()


                    if answer == "nezabít":
                        answer = input("Postupuješ pomalinku k východu, když tu náhle uslyšíš kroky blížící se k místnosti. (schovat se/nic)").lower().strip()

                        if answer == "nic":
                            answer = input("Do místnosti přiběhne bandita a s velkým překvapením stuhne při pohledu na tebe. Spáč už se taky probral je to druhý bandita. Díváte se na sebe. (zaútočit/nic nedělat)").lower().strip()

                            if answer == "nic" :
                                answer = input("Díváte se na sebe ani jeden nechcete zaútočit. Pojďte oba dva rychle odsud než se sem dovalí mrchožrouti. Společně s mini vybíháš  z pevnosti ven, když tu náhle je rozmázne zlobr. A teď si vybral za cíl tebe. (uskočit/běžet dál)").lower().strip()

                            if answer == "běžet dál":
                                answer =input("Zlobr vypočítal tvojí lineární dráhu a rozmázl tě jak mouchu. Jsi mrtvý")

                            if answer == "uskočit":
                                answer = input(
                                    " Elegantně si se zlobrovi uhnul. před tebou se nacházejí 3 cesty. První cesta vede přes už krví nasáklý dvůr na most. Stala se z něj válečná zóna. Zbývající válečníci se snaží potlačit nátlak kostlivců. Bije se to tam hlava nehlava. Určitě budeš na této cestě bojovat. druhá cesta vede částečnými troskami města. Všechno se tam řítí a monster tam taky nebude málo. Poslední třetí cesta vede za plotem do lesa přes louku. Podle mrtvých který se na louce nacházejí však usuzuješ že tam bude hromada pastí. Kudy se tedy vydáš? (1/2/3)  ").lower().strip()

                                if answer == "3":
                                    answer = input("Přelezl jsi plot a šlápnu na minu. Střeva jsou všude. Jsi mrtvý.")

                                if answer == "2":
                                    answer = input(
                                        "Všude je šlyšet troubení rohu oznamující zavírání mostu. Musíš tam být včas říkáš si. Celý zmožený vidíš před sebou dvě cesty kterými se vydat. RYCLEJŠÍ a odost nebezpečnější cestou nebo POMALEJŠÍ a odost mírumilovnější cestou. (ryclejší/pomalejší)").lower().strip()

                                    if answer == "pomalejší":
                                        answer = input(
                                            "Během cesty ti nepřišlo úhony, ale vybralo si to svou daň. Když jsi doběhl k mostu, byl už skoro zavřený. (přeskočit/najít jinou cestu)").lower().strip()

                                        if answer == "najít jinou cestu":
                                            answer = input(
                                                "Nápad skvělej, určitě bys to nepřeskočil, ale bez štítu jsi nemohl vyblokovat salvu šípů. Jsi mrtvý")

                                        if answer == "přeskočit":
                                            answer = input(
                                                "Rozbíháš se směrem k mostu. Zrychluješ. Skáčeš! Padáš! Strany mostu byly od sebe už příliš daleko. Jsi mrtvý.")

                                    if answer == "rychlejší":
                                        answer = input(
                                            "Vbíháš tedy do zřícenin města. Probíháš uličkami. Nabíháš na kámen. Riziko spadnutí. (přeskočit/nepřeskočit)").lower().strip()

                                        if answer == "nepřeskočit":
                                            answer = input(
                                                "Spadl jsi. Bylo to ale tvoje jediné štěstí, protože nad tebou proletěl šíp, který by tě určitě zasáhl. Zvedl ses. Před sebou vidíš 1 kostlivce. (útok/běžet dál)").lower().strip()

                                            if answer == "útok":
                                                answer = input(
                                                    "Zaútočil jsi na něj mečem. Propíchl jsi mu lebku a společně s páteří jsi mu jí vyrval z hlavy. dal ses znovu na útěk. Otvírají se ti další 2 cesty. Hořícím domem nebo vedle něho. (domem/vedle)").lower().strip()

                                                if answer == "domem":
                                                    answer = input(
                                                        "Vešels do domu. Má však už tak ohořelé nosné trámy že se každou chvilku sesype. Na výběr máš tři místnosti. (kuchyň/koupelna/jídelna)").lower().strip()

                                                    if answer == "koupelna":
                                                        answer = input(
                                                            "Prozkoumal jsi místnost. Stěny byli tak ohořelé že by stačilo je mečem vypáčit. Pravděpodobně se ti ale zlomí i meč. (vypáčit/vrátit se)").lower().strip()

                                                        if answer == "vypáčit":
                                                            answer = input(
                                                                "Vypáčil jsi stěnu a dostal se ven ještě před sesunutím domu. Utíkáš stále rychleji k mostu. Už ho vidíš! Proběhl jsi mostem včas jsi na svobodě. Vyhrál jsi.")

                                                        if answer == "vrátit se":
                                                            answer = input(
                                                                "Prohlížení místnosti a následné vracení ti sebralo cenný čas a dům se sesunul. Pod jeho tíhou jsi podlehl smrti. JSI MRTVÝ.")

                                                    if answer == "jídelna":
                                                        answer = input(
                                                            "Jediná cesta ven z jídelny je komínem. (lézt/vrátit se)").lower().strip()

                                                        if answer == "vrátit se":
                                                            answer = input(
                                                                "Prohlížení místnosti a následné vracení ti sebralo cenný čas a dům se sesunul. Pod jeho tíhou jsi podlehl smrti. Jsi mrtvý")

                                                        if answer == "lézt":
                                                            answer = input(
                                                                "Vylezl jsi na vrchol komína. Přeběhl na střechu. Nemáš žádný předmět k plachtění ze střechy a tak jsi skočil. Zlomil sis obě nohy. Netrvalo dlouho a sesunul se na tebe hořící dům. Pod jeho tíhou jsi podlehl smrti. Jsi mrtvý")

                                                    if answer == "kuchyň":
                                                        answer = input(
                                                            "Vbíháš do kuchyně. Všechno hoří. Koukáš přes všechny ty plameny v nadějí že najdeš cestu ven. NIC. Jsi připraven vrátit se a omrknout jiné místnosti ale nosné sloupy domu nevydržely a společně sním ses sesunul na ulici. Byl jsi rozmačkán pod tíhou domu. Jsi mrtvý.")

                                                if answer == "vedle":
                                                    answer = input(
                                                        "Probíháš vedle domu. Bohužel jeho hoříci zchátralé nevydržely a celý dům se sesunul na tebe. Jsi mrtvý.")

                                        if answer == "přeskočit":
                                            answer = input(
                                                "Přeskočil jsi kámen. Běžíš dál. ŠÍP sviští vzduchem. Zapíchl se ti do zad. Umřel jsi.")





                            if answer == "zaútočit" :
                                answer = input ("Sekneš mečem banditovy před tebou na krk, ale bandita za tebou tě chytí pod krkem. Při pohledu na mrtvého parťáka ti zlomí vaz. Jsi mrtvý")

                        if answer == "schovat se" :
                            answer = input("schoval si se pod postelí. Ze dveří vyběhl druhý bandita. ON: Markusi ten pradědek nás začaroval, dělej vzbuď se jestli se odsud chceš dostat živý.  Markus se vzbudil ON: Arture to je strašný, ale kde mám meč! ON: Kašli na meč Markusi musíme rychle zdrhnout. Utekli z místnosti. Vydal jsi se za nima. Na chodbě to dunělo, křik byl slyšet všude. Ve vzduchu byl cítit hrozný puch. Proletění šípu. Zasáhl tě šíp. Chtěl ses podívat útočníkovi do očí ale on žádné neměl byl to kostlivec. Druhý šíp se ti zabodl hluboko do krku. Jsi mrtvý ")


                    if answer == "zabít" :
                        answer = input("Probodl jsi banditovy hrdlo krev vymalovala stěny na červeno, dosáhla dokonce i na strop. Bohužel ti tvojí chvíli kazí jedna věc, blížící se kroky. *Kruci*, říkáš si v duchu. Kdybys ho býval nechal žít... Co teď? Můžeš se schovat, zhasnout lucernu, počkat si na náštěvníka za dveřmi a pokusit se ho zabít též nebo vůbec nic nedělat. (zhasnout/počkat//schovat se/nic)   ").lower().strip()

                        if answer == "schovat se" :
                            answer =input ("Schoval jsi se pod postel. Do místnosti vběhl voják se slovy *na naší základnu útočí mrchožrouti, rozežírají chlapy za živa* a stuhl při pohledu na svého parťáka. *Sakra pro tebe už je asi pozdě* rázem dveře prorazí šesti ruký mrchožrout a vrhne se na banditu. Pomůžeš mu? (ano/ne) ").lower().strip()

                            if answer == "ne" :
                                answer =input("Na vlastní oči sleduješ rozežírání a trhání bandity na kusy. Po krvavém aktu odchází mrchožrout z místnosti. U dveří se však zastaví a začne čichat. Ví snad o tobě? Co uděláš? Můžeš zůstat schovaný nebo vylézt a zaútočit na mrchožrouta.(zůstat/útok)").lower().strip()

                                if answer == "zůstat" :
                                    answer = input("Zůstal jsi tedy pod postelí a mrchožrout odešel z místnosti. Vešel jsi na chodbu a proběhl komplexem na  povrch. Rozmázl tě tam zlobr. Jsi mrtvý")

                                if answer == "útok" :
                                    answer = input("Vyzlelz jsi zpoza postele a zaútočil jsi na mrchožrouta. Neměl jsi šanci umřel jsi. Jsi mrtvý")

                            if answer == "ano" :
                                answer =input ("Vrhl jsi se na mrchožrouta a ten tě jednou mocnou ranou přibil ke zdi. Ty to ale nevzdáváš. usekneš mu dvě ruce, monstrum zlověstně zavyje a vrhne se na tebe s ještě větší agresí. Dochází ti síly už nestačíš na všechny jeho útoky. povolis blokování a monstrum tě začalo sápat ze všech stran.[zvuk zasvištění meče] Mrchžrout je probodnut a následně rozříznut vejpůl. Koukáte si z banditou do očí.(zaútočit/nechat být)").lower().strip()
                                if answer == "nechat být" :
                                    answer = input("Díváte se na sebe, ani jeden nechcete na sebe zaútočit. Oba sklápíte zbraně. ON: *Kde je ten druhý mrchožrout?* TY: *Co?* ON: *Ten který zabil mého bratra!* a ukáže na mrtvé tělo na posteli. Jak odpovíš: (upřímně/lež/").lower().strip()


                                    if answer == "lež" :
                                        answer =input ("TY: Právě kvůli němu jsem se schoval pod postel. Vlezl jsem dveřma s chodby a než se tvůj bratr nadál bylo poněm. Narozdíl od tebe jsem s tím nemohl nic dělat ON: Chudák pojď cizinče rychle odsud než se jich sem přivalí víc. Vyběhli jste rychle z místnosti. Kusy brnění řinčely o sebe. Všude se ozýval křik a řev.Celá banditská základna duněla div se každou chvílí nesesypala. Dunění bylo slyšet pořád blíž a blíž.  ON: Vidíš celá naše základna je na padrť. TY: A co se stalo?  ON: Před pár dnama jsme zajali jednoho čaroděje s celou jeho familii... BACHA!!!  Bandita tě odstrčil před přicházejícím šípem. ON:Další mrchožrouti. Bandita bere nohy na ramena zatímco ty se díváš na tu hrůzu pochodbě se valící. Na vlastní oči vidíš ty zvěrstva. Mrchožrouti decimují,rozhlodávají,trhají bránící se bandity. (utíkat/bojovat) " ).lower().strip()
                                        if answer =="utíkat" :
                                            answer =input ("Utíkáš jak nejrychleji můžeš, přitom se ohlížíš ze strany na stranu. Místnosti byli zaplněny obřími pavouky. Po chodbách se pobíhali mrchožrouti, ghůlové a kostlivci a jiní nemrtví, stěny praskaly pod duněním deseti metrových zlobrů. Vyběhli jste nakonec z hnusného podzemí na povrch, bohužel se nejevil nějak dvakrát přátelštěji. *Jsem Artur* řekl bandita. *Musíme se dostat...* a byl rozmačkán na placku zlobrem. A teď chce zlobr placku z tebe. (uskočit/běžet dál)   ").lower().strip()
                                            if answer == "běžet dál" :
                                                answer =input ("Zlobr vypočítal tvojí lineární dráhu a rozmázl tě jak mouchu. Jsi mrtvý")

                                            if answer == "uskočit" :
                                                answer = input(" Elegantně si se zlobrovi uhnul. před tebou se nacházejí 3 cesty. První cesta vede přes už krví nasáklý dvůr na most. Stala se z něj válečná zóna. Zbývající válečníci se snaží potlačit nátlak kostlivců. Bije se to tam hlava nehlava. Určitě budeš na této cestě bojovat. druhá cesta vede částečnými troskami města. Všechno se tam řítí a monster tam taky nebude málo. Poslední třetí cesta vede za plotem do lesa přes louku. Podle mrtvých který se na louce nacházejí však usuzuješ že tam bude hromada pastí. Kudy se tedy vydáš? (1/2/3)  ").lower().strip()

                                                if answer == "3" :
                                                    answer = input("Přelezl jsi plot a šlápnu na minu. Střeva jsou všude. Jsi mrtvý.")

                                                if answer == "2" :
                                                    answer = input("Všude je šlyšet troubení rohu oznamující zavírání mostu. Musíš tam být včas říkáš si. Celý zmožený vidíš před sebou dvě cesty kterými se vydat. RYCLEJŠÍ a odost nebezpečnější cestou nebo POMALEJŠÍ a odost mírumilovnější cestou. (ryclejší/pomalejší)").lower().strip()

                                                    if answer == "pomalejší":
                                                        answer = input(
                                                            "Během cesty ti nepřišlo úhony, ale vybralo si to svou daň. Když jsi doběhl k mostu, byl už skoro zavřený. (přeskočit/najít jinou cestu)").lower().strip()

                                                        if answer == "najít jinou cestu":
                                                            answer = input(
                                                                "Nápad skvělej, určitě bys to nepřeskočil, ale bez štítu jsi nemohl vyblokovat salvu šípů. Jsi mrtvý")

                                                        if answer == "přeskočit":
                                                            answer = input(
                                                                "Rozbíháš se směrem k mostu. Zrychluješ. Skáčeš! Padáš! Strany mostu byly od sebe už příliš daleko. Jsi mrtvý.")

                                                    if answer == "rychlejší":
                                                        answer = input(
                                                            "Vbíháš tedy do zřícenin města. Probíháš uličkami. Nabíháš na kámen. Riziko spadnutí. (přeskočit/nepřeskočit)").lower().strip()

                                                        if answer == "nepřeskočit":
                                                            answer = input(
                                                                "Spadl jsi. Bylo to ale tvoje jediné štěstí, protože nad tebou proletěl šíp, který by tě určitě zasáhl. Zvedl ses. Před sebou vidíš 1 kostlivce. (útok/běžet dál)").lower().strip()

                                                            if answer == "útok":
                                                                answer = input(
                                                                    "Zaútočil jsi na něj mečem. Propíchl jsi mu lebku a společně s páteří jsi mu jí vyrval z hlavy. dal ses znovu na útěk. Otvírají se ti další 2 cesty. Hořícím domem nebo vedle něho. (domem/vedle)").lower().strip()

                                                                if answer == "domem":
                                                                    answer = input(
                                                                        "Vešels do domu. Má však už tak ohořelé nosné trámy že se každou chvilku sesype. Na výběr máš tři místnosti. (kuchyň/koupelna/jídelna)").lower().strip()

                                                                    if answer == "koupelna":
                                                                        answer = input(
                                                                            "Prozkoumal jsi místnost. Stěny byli tak ohořelé že by stačilo je mečem vypáčit. Pravděpodobně se ti ale zlomí i meč. (vypáčit/vrátit se)").lower().strip()

                                                                        if answer == "vypáčit":
                                                                            answer = input(
                                                                                "Vypáčil jsi stěnu a dostal se ven ještě před sesunutím domu. Utíkáš stále rychleji k mostu. Už ho vidíš! Proběhl jsi mostem včas jsi na svobodě. Vyhrál jsi.")

                                                                        if answer == "vrátit se":
                                                                            answer = input(
                                                                                "Prohlížení místnosti a následné vracení ti sebralo cenný čas a dům se sesunul. Pod jeho tíhou jsi podlehl smrti. JSI MRTVÝ.")

                                                                    if answer == "jídelna":
                                                                        answer = input(
                                                                            "Jediná cesta ven z jídelny je komínem. (lézt/vrátit se)").lower().strip()

                                                                        if answer == "vrátit se":
                                                                            answer = input(
                                                                                "Prohlížení místnosti a následné vracení ti sebralo cenný čas a dům se sesunul. Pod jeho tíhou jsi podlehl smrti. Jsi mrtvý")

                                                                        if answer == "lézt":
                                                                            answer = input(
                                                                                "Vylezl jsi na vrchol komína. Přeběhl na střechu. Nemáš žádný předmět k plachtění ze střechy a tak jsi skočil. Zlomil sis obě nohy. Netrvalo dlouho a sesunul se na tebe hořící dům. Pod jeho tíhou jsi podlehl smrti. Jsi mrtvý")

                                                                    if answer == "kuchyň":
                                                                        answer = input(
                                                                            "Vbíháš do kuchyně. Všechno hoří. Koukáš přes všechny ty plameny v nadějí že najdeš cestu ven. NIC. Jsi připraven vrátit se a omrknout jiné místnosti ale nosné sloupy domu nevydržely a společně sním ses sesunul na ulici. Byl jsi rozmačkán pod tíhou domu. Jsi mrtvý.")

                                                                if answer == "vedle":
                                                                    answer = input(
                                                                        "Probíháš vedle domu. Bohužel jeho hoříci zchátralé nevydržely a celý dům se sesunul na tebe. Jsi mrtvý.")

                                                        if answer == "přeskočit":
                                                            answer = input(
                                                                "Přeskočil jsi kámen. Běžíš dál. ŠÍP sviští vzduchem. Zapíchl se ti do zad. Umřel jsi.")

                                                if answer == "1" :
                                                    answer = input("Vrháš se tedy do dvora. Potřebuješ nějak projít na výběr tu jsou tři situace: Uprostřed bojiště se svádí souboj 4 kostlivci s 2 nabušenýma vojákama. Nalevo dělá hrstka vojáků želví formaci s nadějí že zastaví nával šesti rukých mrchožroutou. Vpravo cupují pavouci všechny vojáky kteří se jim postaví. Kudy to bude nejbezpečnější?(střed/pravá/vlevá)").lower().strip()
                                                    if answer == "levá" :

                                                        answer = input("Vběhls přímo do středu želví formace díky čemuž jsi přežil obrovskou salvu šípů. Banditští vojáci v této formaci postupují k mostu blíž a blíž. Najednou slyšíš dunění. Prásk. Obrovská rána. Zlobr tě svou mocnou ránou odhodil až do města. Všude je šlyšet troubení rohu oznamující zavírání mostu. Musíš tam být včas říkáš si. Celý zmožený vidíš před sebou dvě cesty kterými se vydat. RYCLEJŠÍ a odost nebezpečnější cestou nebo POMALEJŠÍ a odost mírumilovnější cestou. (ryclejší/pomalejší)").lower().strip()

                                                        if answer == "pomalejší" :
                                                            answer = input("Během cesty ti nepřišlo úhony, ale vybralo si to svou daň. Když jsi doběhl k mostu, byl už skoro zavřený. (přeskočit/najít jinou cestu)").lower().strip()

                                                            if answer == "najít jinou cestu" :
                                                                answer = input("Nápad skvělej, určitě bys to nepřeskočil, ale bez štítu jsi nemohl vyblokovat salvu šípů. Jsi mrtvý")

                                                            if answer == "přeskočit" :
                                                                answer = input("Rozbíháš se směrem k mostu. Zrychluješ. Skáčeš! Padáš! Strany mostu byly od sebe už příliš daleko. Jsi mrtvý.")

                                                        if answer == "rychlejší" :
                                                            answer = input("Vbíháš tedy do zřícenin města. Probíháš uličkami. Nabíháš na kámen. Riziko spadnutí. (přeskočit/nepřeskočit)").lower().strip()

                                                            if answer == "nepřeskočit" :
                                                                answer = input("Spadl jsi. Bylo to ale tvoje jediné štěstí, protože nad tebou proletěl šíp, který by tě určitě zasáhl. Zvedl ses. Před sebou vidíš 1 kostlivce. (útok/běžet dál)").lower().strip()

                                                                if answer == "útok" :
                                                                    answer = input("Zaútočil jsi na něj mečem. Propíchl jsi mu lebku a společně s páteří jsi mu jí vyrval z hlavy. dal ses znovu na útěk. Otvírají se ti další 2 cesty. Hořícím domem nebo vedle něho. (domem/vedle)").lower().strip()

                                                                    if answer == "domem" :
                                                                        answer = input("Vešels do domu. Má však už tak ohořelé nosné trámy že se každou chvilku sesype. Na výběr máš tři místnosti. (kuchyň/koupelna/jídelna)").lower().strip()

                                                                        if answer == "koupelna" :
                                                                            answer = input("Prozkoumal jsi místnost. Stěny byli tak ohořelé že by stačilo je mečem vypáčit. Pravděpodobně se ti ale zlomí i meč. (vypáčit/vrátit se)").lower().strip()

                                                                            if answer == "vypáčit":
                                                                                answer = input("Vypáčil jsi stěnu a dostal se ven ještě před sesunutím domu. Utíkáš stále rychleji k mostu. Už ho vidíš! Proběhl jsi mostem včas jsi na svobodě. Vyhrál jsi.")

                                                                            if answer == "vrátit se":
                                                                                answer = input("Prohlížení místnosti a následné vracení ti sebralo cenný čas a dům se sesunul. Pod jeho tíhou jsi podlehl smrti. JSI MRTVÝ.")


                                                                        if answer == "jídelna" :
                                                                            answer = input("Jediná cesta ven z jídelny je komínem. (lézt/vrátit se)").lower().strip()

                                                                            if answer == "vrátit se":
                                                                                answer = input("Prohlížení místnosti a následné vracení ti sebralo cenný čas a dům se sesunul. Pod jeho tíhou jsi podlehl smrti. Jsi mrtvý")

                                                                            if answer == "lézt" :
                                                                                answer = input("Vylezl jsi na vrchol komína. Přeběhl na střechu. Nemáš žádný předmět k plachtění ze střechy a tak jsi skočil. Zlomil sis obě nohy. Netrvalo dlouho a sesunul se na tebe hořící dům. Pod jeho tíhou jsi podlehl smrti. Jsi mrtvý")

                                                                        if answer == "kuchyň" :
                                                                            answer = input("Vbíháš do kuchyně. Všechno hoří. Koukáš přes všechny ty plameny v nadějí že najdeš cestu ven. NIC. Jsi připraven vrátit se a omrknout jiné místnosti ale nosné sloupy domu nevydržely a společně sním ses sesunul na ulici. Byl jsi rozmačkán pod tíhou domu. Jsi mrtvý.")

                                                                    if answer == "vedle" :
                                                                        answer =input("Probíháš vedle domu. Bohužel jeho hoříci zchátralé nevydržely a celý dům se sesunul na tebe. Jsi mrtvý.")


                                                            if answer == "přeskočit" :
                                                                answer = input("Přeskočil jsi kámen. Běžíš dál. ŠÍP sviští vzduchem. Zapíchl se ti do zad. Umřel jsi.")

                                                    if answer == "pravá" :
                                                        answer =input ("Pavouci tě hned zblikli a rozporcovali tě tak jak to ani ten nejlepší řezník neumí. Jsi mrtvý ")
                                                    if answer == "střed" :
                                                        answer =input ("Došel jsi tedy ke středu, ty dva nabušenci už byli proděravělí šípy. A teď začali kostlivci mířit na tebe. Co uděláš? (úhyb/běžet dál) ").lower().strip()
                                                        if answer == "úhyb":
                                                            answer = input("uhnul jsi se salvě šípů. Hned zaní však vystřelili druhou. Neměl jsi žádný předmět na vyblokování tak mocného útoku. Bez známek života jso upadl na bojiště, stejně proděravělí jako nabušenci. JSI MRTVÝ")
                                                        if answer == "běžet dál" :
                                                            answer = input("Rozběhl jsi se co  nejrychleji kupředu, most už byl na dohled, ale salva šípů taky. Ačkoliv ses snažil šípy blokovat mečem nebyl to štít. Bez známek života jsi upadls na bojiště stejně proděravěný jako nabušenci. Jsi mrtvý ")

                                        if answer == "bojovat" :
                                            answer =input ("Byl jsi rozežrán až k morku kostí během pár sekund... CO SIS MYSLEL!!! Jsi mrtvý")


                                    if answer == "upřímně" :
                                        answer = input("TY: *Zabil jsem ho. Omlouvám se to jsem nevěděl.* ON: Jo tak tys to nevěděl. Mě určitě taky zavraždíš hned jak budeš moct.......... Probodl ti srdce. Jsi mrtvý ")
                                if answer == "zaútočit" :
                                    answer = input("Nastavil jsi čepel s úmyslem nového útoku směřujícímu ke krku, jenže bandita na útok zareagoval v čas a  rychlou otočkou ti zabodl meč do břicha. Jsi mrtvý.")

                        if answer == "počkat" :
                            answer = input ("Do místnosti vpadl bandita kříčící *Mrchožrouti útočí...* ale hned se zastavil a zbledl při pohledu na krvavou místnost. Náhle zasvištěl meč vzduchem, byl to tvůj meč a oddělil banditovu hlavu od těla. Výpad úspěšný").lower().strip()

                            answer = input ("Vyběhl jsi na chodbu. Kusy brnění řinčely o sebe. Všude se ozýval křik a řev.Celá banditská základna duněla div se každou chvílí nesesypala. Dunění bylo slyšet pořád blíž a blíž. Zaposlouchal ses. Zaposlouchal ses tak že sis ani nevšiml schluku banditů kteří tě spatřili když probíhali chodbou. Nešli ale na tebe, proběhli kolem tebe jako bys byl jen vzduch. A pak jsi schytal šíp do paže pak do hrudi a pak do břicha. V bolestech a vyčerpání klekáš na zem. Chceš se protivníkovi kouknout do očí, ale ta zrůda žádné neměla byl to kostlivec. Kostlivec v polorozpadlé zbroji následován šestirukými monstry, krve žíznivými ghůly a dalšími zvěrstvi. Zesláblý a klečící sleduješ jak decumují, rozhlodávájí, trhají shluk banditů. Všude létají střeva, končetiny. Roztrhané mrtvoly pak mrchžrouti rozežírají na posezení. Blíží se to k tobě. Smrt je nevyhnutelná. Máš ale navybranou jak umřeš. Buď si prorazíš šíp krkem a tak vykrvácíš dřív nebo počkáš a necháš se zaživa roztrhat. Je to jen na tobě.(zabít se/nic) ").lower().strip()

                            if answer == "nic" :
                                answer = input ("Nestačils ani mrknout a už tě rozežírají na kusy. Krutá a bolestivá smrt. Nejdříva ti byly odtrhnuty nohy potom ruce a pak ti začli rozežírat hlavu, ještě když jsi byl na živu. Poté co ti rozežrali obličej jsi umřel. Jsi mrtvý")

                            if answer == "zabít se" :
                                answer = input ("Probodl jsi si krk. Krvácíš ale né dost rychle. Ty zrůdy už jsou skoro u tebe. *Takovou radost vám neudělám* zařveš a trhneš si s hlavou tak aby sis zlomil krk. Tvé mrtvé tělo je nyní trháno na kusy. Jsi mrtvý")




                        if answer == "zhasnout" :
                            answer = input ("Zhasl jsi světlo. Po náhlém otevření dveří vešel do místnosti vystrašený bandita s křikem *zlobr se utrhl ze řetězů, pohotovost* a nevědomky toho že jeho parťák je mrtev, s ním cloumal jak o život, aby se zvbudil. *Vojáku ihned se proberte pohotovost zlobr se utrhl ze řetězů! Musíte urychleně nastoupit do služby a pomoct nám ho zastavit než nás tady všechny povraždí! Vojáku!* Skrytý pod rouškou tmy stojíš za zády bandity. (zabít/nezabít) ").lower().strip()
                            if answer == "zabít" :
                                answer = input ("Chtěl jsi ho bodnout do zad, ale čepel se ti zastavila v brnění ikdyž bandita vyjekl nebylo to bolestí jelikoš čepel nepronikla ani ke kůži bylo to šokem. Co dál? Pokračovat v tlačení do brnění nebo čepel vyndat a zkusit ho probodnout jinde? (pokračovat/nový útok) ").lower().strip()
                                if answer == "nový útok" :
                                    answer = input ("Vytáhl jsi čepel s úmyslem nového útoku směřujícímu ke krku, jenže štěstěna byla na banditově straně což mělo za následek zlomení meče. Bandita udělal rychlou otočku přičemž vytáhl svůj meč a zabodl ti ho do břicha. Ani ty jsi neváhal a zabodl jsi zlomenou část meče, kterou jsi měl v ruce do jeho krku. Bandita svým posledním pohybem z tebe meč vytáhl a vykrvácený dopadl na zem. Po vytažení začala tvoje rána rychle prosakovat krví.Co uděláš? Natáhneš se pro prostěradlo a obvážeš si to nebo sebereš pásek bandity a zaškrtíš si to nebo rychle popadneš lucernu a pomocí ní si to vypálíš? (zaškrtit/vypálit/obvázat)").lower().skrip()
                                    answer = input(
                                        "V hlavě to znělo hezky ale než jsi stačil něco udělat vykrvácel jsi. Jsi mrtvý")
                            if answer == "nezabít" :
                                answer = input("Pomalinku postupuješ k východu.Banditovi došla smrt parťáka, navíc se ti smůla lepila na paty což mělo za následek zavrzání podlahy. Žijící bandita tě chytil, přitáhl k sobě a nastavil nůž k zádům. Rozsvítil lucernu a při zděšení, že místnost změnila barvu na červenou, tě bodl čtyřiadvacetkrát dozad. Jsi mrtvý ")

                        if answer == "nic" :
                            answer = input("Do místnosti vešel vystrašený bandita s křikem * Mrchožrouti útočí, pohotovost...* a stuhl při pohledu na tebe, poté zbledl po krátkém pohledu na svého zavražděného parťáka. Bez váhání ti usekl hlavu. Jsi mrtvý  ")

                if answer == "obojí":
                    answer = input ("Jako první sis šel pro štít. hrubě jsi ho vyrval zpoza skříně, nacož její vratké nestabilní nohy sebou zacloumali a ze skříně se vyvalilo tolik věcí. Talíře, které se hned rozbily, zlato a zlaté mince a všelijaké jiné předměty. To udělalo strašný kravál a vzbudilo spícího teď na světle lehko rozpoznatelného banditu. Co uděláš? (štít/nic/uhnout)").lower().strip()
                    answer = input ("Než tvoje myšlenka doputovala do mozku, měl jsi meč v hrdle. Jsi mrtvý.")






else:
    print("Tak někdy jindy.")