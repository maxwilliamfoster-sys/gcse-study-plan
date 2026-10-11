# AQA 8662 German — grammar, speaking and dictation cards (vocabulary comes from the AQA list in the GCSE Plan app).

def sec(deck, week, tag, pairs):
    return [(deck, week, tag, q, a) for q, a in pairs]

CARDS = []

CARDS += sec('DE_GRAM', 1, 'present', [
    ('sein — present tense', 'ich bin, du bist, er/sie/es ist, wir sind, ihr seid, sie/Sie sind'),
    ('haben — present tense', 'ich habe, du hast, er hat, wir haben, ihr habt, sie haben'),
    ('Regular present endings (spielen)', 'ich spiele, du spielst, er spielt, wir spielen, ihr spielt, sie spielen'),
    ('Stem-changing verbs: fahren, essen, lesen, sehen (du / er)', 'du fährst / er fährt; du isst / er isst; du liest / er liest; du siehst / er sieht'),
    ('Separable verbs: where does the prefix go?', 'To the end of the clause: "Ich stehe um sieben Uhr auf." (aufstehen)'),
    ('Verb-second rule', 'The verb is always the 2nd idea: "Am Montag spiele ich Fußball."'),
    ('Time – Manner – Place', 'When, how, where: "Ich fahre morgen mit dem Bus in die Stadt."'),
])

CARDS += sec('DE_GRAM', 2, 'cases', [
    ('Definite articles: nominative (m/f/n/pl)', 'der, die, das, die'),
    ('Definite articles: accusative (m/f/n/pl)', 'den, die, das, die — only the masculine changes'),
    ('Definite articles: dative (m/f/n/pl)', 'dem, der, dem, den (+ -n on the plural noun)'),
    ('Indefinite articles: accusative masculine', 'einen (ein Hund → Ich habe einen Hund)'),
    ('When is a noun in the accusative?', 'As the direct object, and after accusative prepositions'),
    ('When is a noun in the dative?', 'As the indirect object ("to someone"), and after dative prepositions'),
    ('Modal verbs (infinitives)', 'können (can), müssen (must), wollen (want), sollen (should), dürfen (may), mögen (like)'),
    ('Modal verb word order', 'Modal in 2nd place, infinitive at the end: "Ich muss meine Hausaufgaben machen."'),
    ('"Ich möchte" means…', 'I would like'),
])

CARDS += sec('DE_GRAM', 3, 'perfect', [
    ('How to form the perfect tense', 'haben/sein in 2nd place + past participle at the end: "Ich habe Tennis gespielt."'),
    ('Which verbs take sein in the perfect?', 'Verbs of movement or change of state: gehen, fahren, fliegen, kommen, bleiben, werden, sein'),
    ('Past participles: gehen, fahren, essen, trinken, sehen', 'gegangen, gefahren, gegessen, getrunken, gesehen'),
    ('Past participles: schreiben, lesen, nehmen, finden, helfen', 'geschrieben, gelesen, genommen, gefunden, geholfen'),
    ('Past participle of a separable verb (aufstehen, einkaufen)', 'aufgestanden, eingekauft'),
    ('Past participles with no ge- (-ieren verbs; prefixes be-, ver-, er-)', 'studiert, telefoniert, besucht, vergessen, erklärt'),
])

CARDS += sec('DE_GRAM', 4, 'future', [
    ('How to form the future tense', 'werden + infinitive at the end: "Ich werde nach Spanien fahren."'),
    ('werden — present tense', 'ich werde, du wirst, er wird, wir werden, ihr werdet, sie werden'),
    ('Conditional: "I would play"', 'Ich würde spielen — würde + infinitive at the end'),
    ('"I would be" / "I would have"', 'ich wäre / ich hätte'),
    ('Wenn-clause with conditional', '"Wenn ich reich wäre, würde ich die Welt bereisen." (If I were rich, I would travel the world)'),
    ('Future time phrases', 'nächste Woche, nächstes Jahr, in der Zukunft, später'),
])

CARDS += sec('DE_GRAM', 5, 'word-order', [
    ('Subordinating conjunctions (verb to the end)', 'weil, dass, wenn, ob, obwohl, als, bevor, nachdem, damit, während'),
    ('Coordinating conjunctions (no change to word order)', 'und, aber, oder, denn, sondern'),
    ('"weil" example', '"Ich mag Mathe, weil der Lehrer lustig ist."'),
    ('Starting with a subordinate clause', 'Verb comma verb: "Wenn es regnet, bleibe ich zu Hause."'),
    ('"denn" vs "weil"', 'Both mean because; denn keeps normal word order, weil sends the verb to the end'),
    ('"um ... zu" + infinitive', 'In order to: "Ich spare Geld, um ein Auto zu kaufen."'),
])

CARDS += sec('DE_GRAM', 6, 'imperfect', [
    ('Imperfect of sein / haben', 'ich war / ich hatte (was / had)'),
    ('Imperfect: es gab', 'there was / there were'),
    ('Common imperfect verbs', 'ging (went), fuhr (travelled), kam (came), sah (saw), aß (ate), trank (drank), fand (found), spielte (played)'),
    ('Imperfect of modals', 'ich konnte (could), ich musste (had to), ich wollte (wanted), ich durfte (was allowed)'),
    ('Comparatives', 'add -er: schnell → schneller (als = than). Some add an umlaut: alt → älter'),
    ('Superlatives', 'am ...sten: am schnellsten; der/die/das beste'),
    ('Irregular: gut, viel, gern', 'gut → besser → am besten; viel → mehr → am meisten; gern → lieber → am liebsten'),
])

CARDS += sec('DE_GRAM', 7, 'prepositions', [
    ('Accusative prepositions', 'bis, durch, für, gegen, ohne, um (DOGFUB)'),
    ('Dative prepositions', 'aus, außer, bei, gegenüber, mit, nach, seit, von, zu'),
    ('Two-way prepositions', 'an, auf, hinter, in, neben, über, unter, vor, zwischen'),
    ('Two-way prepositions: accusative or dative?', 'Accusative = movement to a place (Ich gehe in die Stadt). Dative = position (Ich bin in der Stadt).'),
    ('Genitive prepositions', 'wegen (because of), trotz (despite), während (during), statt (instead of)'),
    ('Contractions', 'zum (zu dem), zur (zu der), im (in dem), ins (in das), am (an dem), beim (bei dem), vom (von dem)'),
    ('Adjective endings after der/die/das (nominative)', '-e: der große Hund, die kleine Katze, das alte Haus'),
    ('Adjective endings after ein (nominative)', 'ein großer Hund, eine kleine Katze, ein altes Haus'),
    ('Adjective ending in the dative', 'Always -en: mit dem großen Hund, mit einer kleinen Katze'),
])

CARDS += sec('DE_GRAM', 8, 'pronouns', [
    ('Subject → object pronouns (accusative)', 'ich → mich, du → dich, er → ihn, sie → sie, wir → uns, ihr → euch'),
    ('Dative pronouns', 'mir, dir, ihm, ihr, uns, euch, ihnen/Ihnen'),
    ('"I like it" / "It tastes good to me"', 'Es gefällt mir / Es schmeckt mir (dative)'),
    ('Relative pronouns (nominative)', 'der, die, das: "Der Mann, der dort wohnt, ist mein Onkel." — verb to the end'),
    ('Possessive adjectives', 'mein, dein, sein (his), ihr (her/their), unser, euer, Ihr (your, formal)'),
    ('Reflexive verbs', 'sich interessieren für, sich freuen auf: "Ich interessiere mich für Musik."'),
])

CARDS += sec('DE_GRAM', 9, 'higher', [
    ('Pluperfect (had done)', 'hatte/war + past participle: "Ich hatte gegessen." / "Ich war gegangen."'),
    ('Passive voice (present)', 'werden + past participle: "Das Haus wird gebaut." (The house is being built)'),
    ('Passive voice (past)', 'wurde + past participle: "Das Auto wurde repariert."'),
    ('"seit" + present tense', 'For/since (still happening): "Ich lerne seit vier Jahren Deutsch." (I have been learning German for four years)'),
    ('man + verb', 'one / you / people: "Man kann hier schwimmen."'),
    ('Imperative (du / Sie)', 'Geh! / Gehen Sie! — Mach! / Machen Sie!'),
])

CARDS += sec('DE_SPEAK', 10, 'speaking', [
    ('Opinion phrases', 'Ich finde, dass… / Meiner Meinung nach… / Ich denke, dass… / Ich glaube, dass…'),
    ('"Meiner Meinung nach" word order', 'Verb comes next: "Meiner Meinung nach ist Sport wichtig."'),
    ('Agreeing and disagreeing', 'Ich stimme zu / Das stimmt / Ich bin nicht einverstanden / Ich bin anderer Meinung'),
    ('Photo card: describing a photo', 'Auf dem Foto gibt es… / Ich kann… sehen / Im Vordergrund… / Im Hintergrund… / Es scheint, dass…'),
    ('Photo card: showing range', 'Use three time frames: what is happening, what they did before, what they will do next'),
    ('Role-play: asking a question', 'Learn question words: Wann? Wo? Was? Wie viel? Warum? Wer? Um wie viel Uhr? Gibt es…?'),
    ('Asking politely', 'Ich hätte gern… / Könnten Sie mir helfen? / Darf ich…?'),
    ('Showing off structure: "Obwohl"', '"Obwohl es teuer ist, gehe ich gern ins Kino."'),
    ('Showing off structure: "Ich hoffe, ... zu"', '"Ich hoffe, an der Uni Biologie zu studieren."'),
    ('Filler phrases while you think', 'Also… / Na ja… / Mal sehen… / Das ist eine gute Frage'),
    ('Speaking prep rule', 'In the 15 minutes’ preparation, write notes for every bullet and photo — you can take them into the room'),
])

CARDS += sec('DE_SPEAK', 10, 'dictation', [
    ('Sound: ei', 'Like English "eye" — mein, Wein, klein'),
    ('Sound: ie', 'Like English "ee" — Liebe, spielen, vier'),
    ('Sound: w / v', 'w sounds like English "v" (Wasser); v usually sounds like "f" (Vater)'),
    ('Sound: z', '"ts" — Zeit, zehn, Pizza'),
    ('Sound: sch / sp / st', 'sch = "sh" (Schule). At the start of a word, sp and st = "shp" and "sht" (spielen, Stadt)'),
    ('Sound: ch', 'After a, o, u: throaty "ach" (Buch). After e, i, ä, ö, ü: softer "ich" (ich, Milch)'),
    ('Sound: ä, ö, ü', 'ä like "e" in "bed"; ö like "ur" with rounded lips; ü like "ee" with rounded lips'),
    ('Sound: ß', 'A sharp "s" — after long vowels and diphthongs (Straße, heißen)'),
    ('Sound: final b, d, g', 'Pronounced p, t, k at the end of a word (Hund = "hunt")'),
    ('Dictation checklist', 'Capitalise every noun; check verb endings agree with the subject; listen for umlauts; full stop at the end'),
    ('Translation tip (into German)', 'Check tense, word order (verb second, verb to the end after weil), gender and case for every noun'),
])
