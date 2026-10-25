# Portfolio-plan: IT-ärendehanterare med JavaScript

Start: måndag 26 oktober 2026 på Collega. Fortsättning: Misa IT från måndag 9 november 2026.

## Riktning och användning

Målet är att utveckla programmeringsförmåga och bygga ett konkret underlag för praktik med kod: webbutveckling, interna verktyg eller automatisering. Projektet är en liten IT-ärendehanterare där en användare kan skapa, läsa och ändra status på supportärenden.

Detta är ett föreslaget lärande- och projektupplägg, inte en överenskommelse med Misa eller ett löfte om praktik. Veckorna beskriver arbetsblock. Gå vidare när kärnuppgifterna fungerar och du kan förklara dem. Anpassa efter handledning och faktisk arbetstid.

Den nya planen är huvudspåret för fortsatt utvecklingsarbete. Den tidigare `PORTFOLIO_PLAN.md` beskriver SauceDemo-spåret och finns kvar som historik/referens. Du behöver inte slutföra dess 16 veckor innan du börjar denna plan. De gamla skripten för veckouppgifter gäller fortfarande enbart SauceDemo-planen; kör dem inte för att skapa det nya projektets uppgifter.

Vid genomgång av GitHubs main-gren den 25 oktober fanns två inloggningstester och en Actions-workflow. Det är relevant erfarenhet att återanvända. Testresultat har inte verifierats som del av denna planering. README beskriver ett äldre planeringsläge och bör uppdateras separat när statusen har stämts av.

## Teknik och avgränsning

| Del | Val | Varför i denna plan |
| --- | --- | --- |
| Gränssnitt | HTML, CSS och vanlig JavaScript | Lär hur formulär, händelser och sidans innehåll fungerar. |
| Server | Node.js och Express, JavaScript med ESM | Samma språk som i webbläsaren och dina Playwright-tester. |
| Lagring | SQLite via better-sqlite3 | En liten lokal databas med konkret SQL. |
| Tester | Playwright, först Chromium | Bygger vidare på det du redan har arbetat med. |
| Arbetsflöde | Git, GitHub, korta branches och PR:er | Visa avgränsade ändringar och hur du kontrollerat dem. |
| Publicering | Node-kompatibel hosting; Render som dokumenterat exempel | Kontrollera kostnad och lagring innan tjänsten väljs. |

Välj en stödd Node LTS-version vid installation och dokumentera samma huvudversion lokalt, i CI och på hosting. Checka in package-lock.json. Använd dokumentation som stämmer med installerade versioner, särskilt Express och better-sqlite3.

Första färdiga versionen, MVP:

- Skapa ärende med rubrik och beskrivning.
- Visa lista och öppna ett ärendes detaljer.
- Ändra status mellan Nytt, Pågår och Klart.
- Behålla data efter omladdning och lokal serveromstart.
- Visa begripliga fel vid tomma/ogiltiga fält och saknade ärenden.
- Ha automatiserade tester, CI och instruktioner för att köra projektet.

Senare förbättring: filtrering på status. Inloggning, roller, bilagor, e-post, React, TypeScript och Docker ligger utanför kärnplanen. Välj högst en sådan fortsättning efter en fungerande första version och samtal med Misa.

Det är en demo med påhittade ärenden, inte ett system för riktiga supportuppgifter. Utan inloggning delar besökare demodata; skriv det tydligt. Använd inga verkliga namn, kundärenden eller lösenord.

## Tid, inläsning och dagligt arbetssätt

Planera inledningsvis för cirka 10–12 fokuserade projekttimmar per arbetsvecka. Närvaro, lunch, pauser, introduktion och kurser tillkommer eller tar del av tiden. Om det fungerar kan projektarbetet öka till cirka 15–18 timmar; 24 timmars närvaro betyder inte 24 timmars koncentrerat kodarbete. Ingen del kräver hemarbete eller helgarbete.

Exempel på projekttid under en vecka: 2 timmar inläsning/övningar, 6 timmar kodning, 2 timmar kontroll/felsökning och 1 timme demo/planering. Misas kurser kan ersätta motsvarande inläsning. Om en kurs tränar formulär, använd ärendeformuläret som tillämpning.

För varje uppgift:

1. Läs bara avsnittet som anges, normalt 15–30 minuter åt gången.
2. Skriv två meningar med egna ord och gör ett minimalt eget exempel.
3. Implementera en liten del i appen och kontrollera resultatet.
4. Spara en commit och notera nästa konkreta steg.

Ett arbetspass: 10 minuter återstart, 20 minuter läsning, 60–90 minuter kodning, paus och därefter kontroll/felsökning. Anpassa längden till dagens förutsättningar. Fråga efter hjälp när du inte kommer vidare efter cirka 20–30 minuters fokuserad felsökning; skicka felmeddelande, förväntat resultat och vad du provat.

Använd AI för förklaringar, ledtrådar och kodgranskning. Be om små ändringar. En funktion är inte inlärd förrän du kan förklara flödet och själv göra en mindre ändring i den.

## Collega: två förberedelseveckor

### C1 — 26–30 oktober: begriplig grund och första sida

**Mål:** En statisk ärendesida som du själv kan förklara. Budget cirka 10–12 projekttimmar för hela veckan.

| Uppgift | Gör detta | Läs före uppgiften | Klart när |
| --- | --- | --- | --- |
| C1.1 Projektbeslut | Skriv mål, fyra kärnfunktioner och vad som får vänta i ett kort projektbrief. Skissa lista, formulär och detaljvy på papper. | [S1], introduktionen och branch/PR-flödet. | Du kan säga vem appen hjälper och visa skissen på två minuter. |
| C1.2 Projektstart | Skapa ett separat repo, föreslaget namn it-ticket-tracker. Lägg till README, .gitignore och mapparna public och docs. Denna plan kan kopieras dit. | [S1] och [S17], vad README ska besvara. | Du kan öppna projektet i VS Code, köra git status och hitta det på GitHub. |
| C1.3 HTML | Skapa public/index.html med rubrik, ett märkt formulär och tre hårdkodade exempelärenden. | [S2], rubriker/listor/länkar, samt [S3], formulärets grundstruktur och label. | Sidan visar formulär och exempelärenden; varje fält har en etikett. |
| C1.4 CSS | Lägg grundläggande layout, läsbar text, mellanrum och tydliga knappar i public/styles.css. | [S4], selektorer och boxmodellen. | Sidan är begriplig i både smalt och brett fönster. |

**Veckobevis:** Skärmbild, commit/PR och en kort README med aktuell status. Funktionalitet som ännu inte finns ska beskrivas som planerad.

### Första dagen: måndag 26 oktober

Kärnpass cirka tre timmar plus pauser:

- [ ] 20 min: Läs denna plans mål/MVP. Skriv ett projektbrief på 5–8 meningar, inte en lång kravspecifikation.
- [ ] 25 min: Skissa listan och formuläret. Välj rubrik, beskrivning och status som första synliga information.
- [ ] 25 min: Skapa projektmappen/repo enligt C1.2 och öppna i VS Code.
- [ ] 30 min: Läs utvalda delar av [S2] och [S3]. Prova en rubrik, en label och ett input-fält.
- [ ] 60 min: Bygg första index.html och öppna i webbläsaren. Det räcker att visa ett formulär och ett exempelärende.
- [ ] 20 min: Kontrollera sidan, spara en commit och skriv exakt vad du börjar med nästa gång.

Om du har mer fokuserad tid: börja C1.4. JavaScript, backend och installationer av fler verktyg kan vänta. Dagens leverans är en egen begriplig sida, inte hela appen.

### C2 — 2–6 november: JavaScript och första interaktionen

**Mål:** Skapa och visa ärenden i webbläsarens minne.

| Uppgift | Gör detta | Läs före uppgiften | Klart när |
| --- | --- | --- | --- |
| C2.1 Datamodell | Öva const/let, funktioner, objekt och arrayer. Beskriv ett ärende med id, title, description och status. | [S5], variabler, funktioner, arrayer och objekt. Läs dessa delar vid behov, inte hela kursen. | Du kan lägga till ett objekt i en array och förklara skillnaden mellan dem. |
| C2.2 Visa data | Skapa public/app.js. Rendera tre objekt från en array till sidan med DOM-metoder. | [S6], välja element, skapa element och ändra text. | Listan byggs från data i stället för tre kopior av samma HTML. |
| C2.3 Formulär | Lyssna på submit, stoppa vanlig sidomladdning och lägg ett nytt ärende i arrayen. | [S3] och händelseavsnitten i [S5]. | Ett ifyllt formulär ger ett nytt synligt ärende; tom rubrik stoppas. |
| C2.4 Överlämning | Skriv vad som fungerar, nästa steg och frågor till handledaren. Länka tidigare SauceDemo-projektet som separat testexempel. | [S17], projektets syfte och startinstruktioner. | Du kan demonstrera sidan på cirka tre minuter inför Misa-starten. |

**Veckobevis:** Demo och PR med en egen förklaring av submit → data → visning. Att data försvinner vid omladdning är en känd begränsning denna vecka. Om JavaScript tar längre tid, fortsätt C2 på Misa innan M1.

## Misa IT: tolv arbetsveckor från 9 november

M1 börjar 9 november. Följande datum är planeringsfönster, inte deadlines. M1–M6 motsvarar ungefär 9 nov–18 dec vid ett arbetsblock per vecka. Jul/nyår hanteras som flexibel buffert; M7–M12 fortsätter när verksamheten och ditt schema tillåter, sannolikt in i februari. Kontrollera öppettider och ledighet med Misa; de antas inte här.

### M1 — Start 9 november: status och lokal prototyp

**Mål:** Visa arbetet, förankra upplägget och göra webbläsarversionen användbar.

| Uppgift | Gör detta | Inläsning | Klart när |
| --- | --- | --- | --- |
| M1.1 Avstämning | Visa det du byggt. Be om veckovis planeringsstöd och fråga om teknisk handledning, relevanta kurser och erfarenheter av praktik med kod. | Läs projektbrief och senaste arbetsanteckningen. | Ni har noterat vilket stöd som finns, vad som behöver undersökas och nästa avstämning. |
| M1.2 Detaljer/status | Lägg till att öppna ett ärende och ändra dess status. | [S5], villkor/funktioner, och [S6], DOM. | Rätt ärende får rätt status utan att andra ändras. |
| M1.3 Lokal lagring | Spara/läs arrayen som JSON i localStorage. Kör sidan via en lokal HTTP-server, exempelvis VS Codes Live Server, så att den har en stabil origin. | [S7], setItem/getItem, samt JSON-avsnitt i [S5]. | Skapade ärenden och ändrad status finns kvar efter omladdning på samma adress. |

**Bevis:** Demo och kort förklaring av array, JSON och localStorage. Detta är en prototyp; lagringen flyttas till server/databas i M3–M4. Om C2 är ofärdig prioriteras den och M1 delas över fler pass.

### M2 — Riktfönster 16–20 november: första servern och API:t

**Mål:** Förstå vad som körs i webbläsaren respektive på servern.

| Uppgift | Gör detta | Inläsning | Klart när |
| --- | --- | --- | --- |
| M2.1 Node/Express | Initiera npm, välj dokumenterad Node-version och ESM. Skapa src/server.js och ett npm start-kommando. | [S8], introduktion och npm; [S9], Hello world med ESM. | npm start ger en lokal server och du kan förklara varför den måste vara igång. |
| M2.2 API | Servera public-mappen och skapa GET /api/tickets samt POST /api/tickets med tillfällig minneslagring. Använd express.json(). | [S10], GET/POST, request body och statiska filer via Express-dokumentationen. | Du kan hämta listan och skapa ett ärende; API:t returnerar JSON. |
| M2.3 Kontrakt | Skriv endpoint, indata, utdata och statuskoder i docs/api.md. Avvisa tom rubrik på servern. | [S10], request/response-exemplen. | Giltigt POST ger 201; ogiltig indata ger 400. Minneslagringens begränsning är noterad. |

**Bevis:** Dokumenterade exempelanrop och svar. Ingen databas behövs för att förstå denna veckas flöde.

### M3 — Riktfönster 23–27 november: SQLite och bestående data

**Mål:** Serverdata finns kvar efter omstart.

| Uppgift | Gör detta | Inläsning | Klart när |
| --- | --- | --- | --- |
| M3.1 SQL | Skapa en tickets-tabell med id, title, description, status och created_at. Öva CREATE TABLE, INSERT, SELECT och UPDATE med fiktiva data. | [S11], just dessa fyra kommandon. | Du kan förklara tabell, rad, kolumn och primärnyckel. |
| M3.2 Anslutning | Installera kompatibel better-sqlite3-version. Skapa src/db.js och ersätt API:ts array med databasfrågor. | [S12], new Database, prepare, run, all och parameterbindning. | Ett POST-skapat ärende går att GET-hämta även efter serveromstart. |
| M3.3 Start/reset | Lägg schema och script för påhittade exempeldata i repot. Ignorera genererade databasfiler. Dokumentera databasens sökväg. | [S12], databasfil och prepared statements. | En ny checkout kan skapa en egen databas utan att kopiera din lokala fil. |

**Bevis:** Omstartstest och exempel på parameteriserad SQL. Lägg aldrig användartext direkt i SQL-strängen.

### M4 — Riktfönster 30 november–4 december: koppla hela appen

**Mål:** Den första sammanhängande versionen: webbläsare → API → databas → webbläsare.

| Uppgift | Gör detta | Inläsning | Klart när |
| --- | --- | --- | --- |
| M4.1 Fetch | Byt localStorage-anrop mot fetch till API:t. Låt Express servera både sidan och API:t från samma origin. | [S13], GET, POST, JSON och kontroll av response.ok. | Formuläret sparar i databasen och omladdning visar datan igen. |
| M4.2 Detaljer/status | Skapa GET /api/tickets/:id och PATCH /api/tickets/:id för status. Koppla till detaljvyn. | [S10], route-parametrar och HTTP-metoder; [S13], request options. | Rätt ärende öppnas och en statusändring finns kvar efter omstart. |
| M4.3 Felvägar | Visa laddning, tom lista och begripliga fel. Validera status och saknat id på servern. | [S14], grundläggande felhantering, och [S13], felaktiga HTTP-svar. | Ogiltig status ger 400, saknat ärende 404, och UI visar fel utan falskt lyckat resultat. |

**Bevis:** Visa skapa → öppna → ändra → ladda om. Skriv hur du vet att datan kommer från databasen. localStorage ska inte längre vara en parallell källa till ärendedata.

### M5 — Riktfönster 7–11 december: automatiserade tester

**Mål:** Använd din testkunskap på en app du själv byggt.

| Uppgift | Gör detta | Inläsning | Klart när |
| --- | --- | --- | --- |
| M5.1 Testmiljö | Installera Playwright i nya repot. Använd webServer för att starta appen. Kör mot en separat testdatabas och återställ den före testkörningen. Börja med en worker. | [S15], skriva tester; [S16], webServer. | Tester fungerar utan manuell serverstart och utan att röra din vanliga databas. |
| M5.2 Kärnflöden | Testa skapa/visa, tom rubrik, detaljer och bestående status efter omladdning. Använd labels/roller och väntande assertions. | [S15], actions och assertions. | Fyra tydliga scenarier verifierar observerbart beteende och kan köras igen från samma rena startläge. |
| M5.3 API-validering | Lägg ett API-test för tom rubrik och ett för ogiltig status, eftersom webbläsarvalidering kan kringgås. | API testing-länken från [S15] och ditt docs/api.md. | Servern avvisar båda fallen och testet visar det. |

**Bevis:** Körkommando, resultat och en förklaring av ett test med Prepare, Act och Assert. Ett separat manuellt omstartstest verifierar lagring över serveromstart.

### M6 — Riktfönster 14–18 december: GitHub Actions och repeterbarhet

**Mål:** En annan dator kan installera och kontrollera appen.

| Uppgift | Gör detta | Inläsning | Klart när |
| --- | --- | --- | --- |
| M6.1 CI | Kör npm ci, installera Chromium och kör tester på pull requests. Använd samma Node-huvudversion som lokalt och skapa testdatabas i jobbet. | [S18], GitHub Actions-exemplet. | En riktig PR har en lyckad workflow-körning. |
| M6.2 Diagnostik | Spara HTML-rapport även vid testfel. Prova ett avsiktligt assertionsfel på arbetsbranchen och återställ det efter kontroll. | [S18], rapporter/artifacts. | Testfelet gör jobbet rött, rapporten går att hämta och senaste versionen är grön. |
| M6.3 Ren installation | Prova dokumenterade steg från en ny projektkopia och förbättra README efter det som saknas. | [S17] och dina faktiska npm-scripts. | Ny installation kan starta appen och köra tester utan dolda manuella förberedelser. |

**Bevis:** PR, workflow-länk och kontrollerade startinstruktioner. Detta är CI. Att appen också deployas är ett separat steg; kalla det inte automatisk CD förrän den kedjan är implementerad och kontrollerad.

### Jul/nyår: flexibel buffert

Veckorna från 21 december är inte en förutsatt normal arbetsperiod. Kontrollera schemat med Misa. Använd eventuell arbetstid till repetition, ofärdiga kärnuppgifter eller dokumentation. Planen kräver inga studier under ledighet. Fortsätt därefter i nedanstående ordning.

### M7 — kvalitet och begriplig användning

**Mål:** En liten app som går att använda även när något blir fel.

| Uppgift | Gör detta | Inläsning | Klart när |
| --- | --- | --- | --- |
| M7.1 Tillgänglighet | Kontrollera labels, tangentbord, synligt fokus och tydliga statusnamn. | [S19], semantisk HTML och formulär. | Hela kärnflödet går att utföra med tangentbord och status framgår utan enbart färg. |
| M7.2 Indata | Bestäm fältgränser, t.ex. rubrik 1–100 och beskrivning 1–2000 tecken efter trimning. Validera på servern, visa text som textContent och begränsa JSON-storlek. | [S20], indata; [S6], textinnehåll. | Tomma/långa fält avvisas; text som innehåller HTML visas som text. |
| M7.3 Utforskning | Gör ett 30-minuters testpass med tom lista, omladdning, felaktiga värden och avstängd server. Fixa viktigaste hittade felet. | [S14] och tidigare egna SauceDemo-anteckningar som metodstöd. | Observationer är noterade och den valda rättningen har kontrollerats igen. |

**Bevis:** Kort testanteckning och en fokuserad fix-PR. Detta är grundläggande kvalitetsarbete, inte ett påstående om full säkerhetsgranskning.

### M8 — publicera en demo

**Mål:** Appen går att öppna via en länk och dess lagringsbeteende är tydligt.

| Uppgift | Gör detta | Inläsning | Klart när |
| --- | --- | --- | --- |
| M8.1 Driftbeslut | Gå igenom Node-hosting och budget med handledaren. Render är ett exempel. Bestäm bestående disk eller en tydligt märkt återställbar demo. | [S21] och [S22], särskilt tillfälligt filsystem och betald disk. | Beslut och lagringsbegränsning finns i docs/deployment.md innan publicering. |
| M8.2 Deployment | Konfigurera npm start, process.env.PORT och databasens sökväg. Lägg en enkel GET /health. Publicera efter grön CI. | [S21], instruktionerna anpassade till dina startkommandon. | HTTPS-länken fungerar och kärnflödet kan demonstreras från ett annat webbläsarfönster. |
| M8.3 Verifiering | Testa omladdning, omstart och redeploy. Dokumentera vad som bevaras. Välj manuell deploy eller konfigurera deploy först efter lyckade kontroller. | [S22] och din deploy-konfiguration. | Du kan visa om data består eller återställs, och README säger samma sak. |

Render använder som standard ett tillfälligt filsystem; en lokal SQLite-fil är då inte bestående över omstarter/redeploy. Persistent disk kräver enligt den kontrollerade dokumentationen en betald tjänst. Inget abonnemang eller köp ingår i planen. Om budget saknas: publicera en märkt demo som återställs och behåll verifierad lokal SQLite-lagring som tekniskt bevis. Beskriv det som en begränsning, inte som bestående lagring online.

**Bevis:** Klickbar länk, commit/version och deploy-anteckning. Ingen hosting är skapad genom denna plan.

### M9 — en förbättring och första release

**Mål:** Visa att du kan förbättra en fungerande app utan att bredda projektet för mycket.

| Uppgift | Gör detta | Inläsning | Klart när |
| --- | --- | --- | --- |
| M9.1 Filtrering | Lägg ett statusfilter: Alla, Nytt, Pågår, Klart. Börja med klientfiltrering av hämtad lista. | [S5], array.filter, och [S6]. | Listan visar rätt urval och tomt resultat har begriplig text. |
| M9.2 Regression | Lägg ett test för filtret och kör befintliga tester efter ändringen. | [S15]. | Filtertest och tidigare kärnflöden passerar lokalt och i CI. |
| M9.3 Release | Kontrollera kärnkraven, samla kända begränsningar och märk första färdiga versionen. | [S1], review/merge; [S17], aktuell status. | Demo, kod och README beskriver samma version. |

**Bevis:** Releasebeskrivning och testkörning. Om kärnuppgifter släpar: prioritera dem och skjut filtret till senare.

### M10 — paketera projektet för en granskare

**Mål:** En person ska kunna förstå projektet på några minuter.

| Uppgift | Gör detta | Inläsning | Klart när |
| --- | --- | --- | --- |
| M10.1 README | Skriv problem, funktioner, skärmbild, demolänk, teknik, körkommandon och begränsningar. | [S17], rekommenderat README-innehåll. | En annan person kan hitta demon och följa körinstruktionerna. |
| M10.2 Arkitektur | Skriv kort om webbläsare, Express, SQLite och testdatabas. Beskriv ett ärendes väg från formulär till lagring. | Läs om [S8], [S10] och [S13] där du fortfarande är osäker. | Du kan förklara flödet utan att läsa upp koden. |
| M10.3 Egen insats | Beskriv två tekniska val, ett löst problem och hur AI/handledning använts. | Egna PR:er och arbetsanteckningar är primärkällan. | Alla påståenden går att koppla till kod, körning eller dokumenterat beslut. |

**Bevis:** README och en kort projektpresentation. Uppdatera befintliga texter så att planerade funktioner inte framstår som färdiga.

### M11 — praktikprofil och teknisk presentation

**Mål:** Använd projektet som underlag i samtal om kodnära praktik.

| Uppgift | Gör detta | Inläsning | Klart när |
| --- | --- | --- | --- |
| M11.1 Projektblad | Skriv ett kort portfolioblad: syfte, egen insats, teknik, demo och länk till en representativ PR. | README och de egna bevisen från M9–M10. | Konsulent/handledare kan förstå vad du faktiskt kan visa. |
| M11.2 Demo | Öva fem minuter: skapa ärende, ändra status, visa kodflöde och ett test. | Egna src-filer, docs/api.md och [S15] vid behov. | Du klarar en följdfråga och en liten kodändring utan färdigt manus. |
| M11.3 Matchning | Gå med konsulenten igenom möjliga arbetsuppgifter inom webb, interna verktyg och enklare automatisering. Anpassa nästa lärsteg till faktisk återkoppling. | Misas återkoppling och konkreta arbetsuppgifter är underlag; ingen generell dokumentationssida kan avgöra deras möjligheter. | Ni har en noterad nästa åtgärd och vem som gör den. |

**Bevis:** Granskat projektblad och noterat förbättringsbehov. Personliga kontaktlistor och arbetsgivaranteckningar hålls utanför offentliga repot. Planen skickar inga meddelanden till arbetsgivare.

### M12 — återkoppling och nästa utvecklingssteg

**Mål:** Fortsatt programmering styrd av verkligt behov.

| Uppgift | Gör detta | Inläsning | Klart när |
| --- | --- | --- | --- |
| M12.1 Användarfeedback | Be någon prova demon, observera var den är oklar och välj en konkret förbättring. | Den egna testanteckningen från M7. | Ett problem är beskrivet med steg och förväntat beteende. |
| M12.2 Leverans | Genomför förbättringen med test, PR och uppdaterad demo. | Läs relevant tidigare källa för just ändringen. Om t.ex. felhantering ändras: [S14]. | Förbättringen kan visas och befintliga funktioner fungerar. |
| M12.3 Nästa spår | Välj med Misa: fördjupa frontend, bygga mer backend eller komplettera med ett litet automatiseringsskript. | Utgå från praktikåterkoppling och vad du kunnat visa; välj nästa officiella tutorial först när spåret är bestämt. | Det finns ett avgränsat tvåveckorsmål, inte tre parallella kurser. |

**Bevis:** En ytterligare fungerande leverans och nästa beslut. Praktiksök och matchning behöver inte vänta tills M12 är klar.

## Stödet att diskutera med Misa

- Första veckan: förankra målet att få skriva kod, gå igenom projektets nivå och fråga vilka typer av praktikuppgifter som kan vara aktuella.
- Varje vecka: cirka 15–30 minuter för demo, hinder, nästa mål och hållbar arbetstid.
- Teknisk handledning: fråga vem som kan hjälpa med kod/installation/felsökning och hur ofta. Tillgängligheten är inte bekräftad.
- Kurser: välj sådant som stöder nästa projektuppgift och låt det ersätta motsvarande lästid.
- Efter fungerande API/databas och igen vid demo: bedöm tillsammans när materialet räcker för kontakter. Ett perfekt projekt är inte ett villkor för att börja undersöka möjligheter.

Arbetsplats, kurser, kodgranskning och arbetsgivarkontakter är stöd att stämma av, inte åtaganden som denna plan kan tilldela Misa.

## GitHub och uppföljning

Rekommenderad struktur i det nya app-repot när filerna behövs: public/ för frontend, src/ för server och databasanslutning, scripts/ för databasinitiering, tests/ för tester och docs/ för korta tekniska anteckningar. Skapa inte alla mappar och abstraktioner i förväg.

En uppgift i taget: issue → kort branch → liten ändring → kontroll → PR → egen granskning eller handledarfeedback → merge. Exempel på titel: C2.3 – skapa ärende via formulär. Använd uppgiftens Klart när-text som acceptanskriterium. En veckotabell kan bli flera små issues, men skapa bara den aktuella veckans uppgifter för att hålla listan hanterbar.

En uppgift är klar när beteendet fungerar, du kan förklara koden, relevant kontroll är gjord och ändringen är sparad. Ett blockerat test är ett hinder att lösa, inte ett godkänt resultat. Skriv vad som prövats och nästa felsökningssteg.

Anteckning vid slutet av ett pass:

- Arbetat med:
- Fungerar nu:
- Kontrollerat genom:
- Jag kan förklara:
- Hinder:
- Nästa konkreta steg:

Om tiden inte räcker: slutför aktuell kärnfunktion, flytta resten framåt och ta bort extrafunktioner. Vid cirka halva planerade projekttiden kan ett veckoblock behöva två veckor. Ta beslut vid avstämningen; kompensera inte med krav på hemarbete.

## Källor och avgränsad inläsning

Länkar kontrollerade 25 oktober 2026. Officiell dokumentation är underlag för teknik och övningar. Veckoordning, tidsbudget och projektval är ett anpassat förslag; källorna utlovar inte praktik eller Misa-stöd. De flesta källorna är på engelska. Använd dem som uppslagsverk och be om svensk förklaring när det behövs.

- **S1:** [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow) — branch, commit, PR, review och merge.
- **S2:** [MDN: Structuring content with HTML](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content) — välj rubriker, listor och grundstruktur.
- **S3:** [MDN: Your first form](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Your_first_form) — form, label, input, textarea och button.
- **S4:** [MDN: CSS styling basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics) — välj selektorer och boxmodellen.
- **S5:** [MDN: Dynamic scripting with JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting) — använd delarna om variabler, funktioner, arrayer, objekt, villkor, events och JSON när respektive uppgift kräver det.
- **S6:** [MDN: DOM scripting introduction](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/DOM_scripting) — välj element, skapa element och ändra text.
- **S7:** [MDN: localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) — getItem/setItem, origin och begränsningar. HTTP-server används för en stabil lokal adress.
- **S8:** [Node.js: Introduction to Node.js](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs) — servermiljö; följ länken till introduktionen av npm.
- **S9:** [Express: Hello world](https://expressjs.com/en/starter/hello-world/) — använd JavaScript/ESM-exemplet.
- **S10:** [Express: Routing](https://expressjs.com/en/guide/routing/) — metoder och route-parametrar; slå upp express.json och express.static i den länkade API-dokumentationen.
- **S11:** [SQLite: SQL language](https://sqlite.org/lang.html) — välj CREATE TABLE, INSERT, SELECT och UPDATE, inte hela referensen.
- **S12:** [better-sqlite3: API](https://github.com/WiseLibs/better-sqlite3/blob/master/docs/api.md) — Database, prepare, run, all, get och Binding Parameters. Läs dokumentation för den version du installerar.
- **S13:** [MDN: Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) — JSON, HTTP-metoder och response.ok.
- **S14:** [Express: Error handling](https://expressjs.com/en/guide/error-handling/) — grundläggande felvägar och egen felhantering vid behov.
- **S15:** [Playwright: Writing tests](https://playwright.dev/docs/writing-tests) — actions, locators och assertions; använd sidans länk till API testing för direkta serveranrop.
- **S16:** [Playwright: Web server](https://playwright.dev/docs/test-webserver) — starta lokal app och konfigurera baseURL.
- **S17:** [GitHub: About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) — syfte, användning och startinstruktioner.
- **S18:** [Playwright: Setting up CI](https://playwright.dev/docs/ci-intro) — Actions-workflow och rapporter.
- **S19:** [MDN: HTML as a basis for accessibility](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML) — semantik, formulär och tangentbord.
- **S20:** [Express: Production best practices, security](https://expressjs.com/en/advanced/best-practice-security/) — fokusera på indata och relevanta inställningar inför demo.
- **S21:** [Render: Deploy a Node Express App](https://render.com/docs/deploy-node-express-app) — ett hostingexempel, inte ett krav eller ett genomfört köp.
- **S22:** [Render: Persistent Disks](https://render.com/docs/disks) — tillfälligt filsystem, monterad disk och bestående data. Kontrollera aktuella villkor vid driftbeslutet.
