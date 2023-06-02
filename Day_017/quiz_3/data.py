import random

general_knowledge = {
"easy": [
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Video streaming website YouTube was purchased in it's entirety by Facebook for US$1.65 billion in stock. 'True' or 'False': ",
      "correct_answer": "False",
      "remark": "YouTube wasn't acquired by Facebook.",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Gumbo is a stew that originated in Louisiana. 'True' or 'False': ",
      "correct_answer": "True",
      "remark": "Gumbo is a stew that originated in Louisiana.",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "French is an official language in Canada. 'True' or 'False': ",
      "correct_answer": "True",
      "remark": "French is an official language in Canada.",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "It is automatically considered entrapment in the United States if the police sell you illegal substances without revealing themselves. 'True' or 'False': ",
      "correct_answer": "False",
      "remark": "It is not considered entrapment in the US for the police to sell you illegal substances under cover.",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "A scientific study on peanuts in bars found traces of over 100 unique specimens of urine. 'True' or 'False': ",
      "correct_answer": "False",
      "remark": "This isn't true.",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Bulls are attracted to the color red. 'True' or 'False': ",
      "correct_answer": "False",
      "remark": "That bulls are attracted to the color red is false.",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "'Ananas' is mostly used as the word for Pineapple in other languages. 'True' or 'False': ",
      "correct_answer": "True",
      "remark": "This is true",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "You can legally drink alcohol while driving in Mississippi. 'True' or 'False': ",
      "correct_answer": "True",
      "remark": "Drinking alcohol while driving is not considered illegal in Mississippi.",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "In 2010, Twitter and the United States Library of Congress partnered together to archive every tweet by American citizens. 'True' or 'False': ",
      "correct_answer": "True",
      "remark": "Since 2010, Twitter, in partnership with the US Library of Congress, has been archiving every tweet by American citizens.",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Adolf Hitler was born in Australia. 'True' or 'False': ",
      "correct_answer": "False",
      "remark": "Adolf Hitler was born in Braunau am Inn in Austria.",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "When you cry in space, your tears stick to your face. 'True' or 'False': ",
      "correct_answer": "True",
      "remark": "",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "One of Donald Trump's 2016 Presidential Campaign promises was to build a border wall between the United States and Mexico. 'True' or 'False': ",
      "correct_answer": "True",
      "remark": "To build a border wall between the USA and Mexico is a popular promise of Donald Trump during his 2016 Presidential Campaign.",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "'27 Club' is a term used to refer to a list of famous actors, musicians, and artists who died at the age of 27. 'True' or 'False': ",
      "correct_answer": "True",
      "remark": "",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Dihydrogen Monoxide was banned due to health risks after being discovered in 1983 inside swimming pools and drinking water. 'True' or 'False': ",
      "correct_answer": "False",
      "remark": "",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Scotland voted to become an independent country during the referendum from September 2014. 'True' or 'False': ",
      "correct_answer": "False",
      "remark": "This isn't true.",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The National Animal of Scotland is the Unicorn. 'True' or 'False': ",
      "correct_answer": "True",
      "remark": "The Unicorn is the National Animal of Scotland.",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Vietnam's national flag is a red star in front of a yellow background. 'True' or 'False': ",
      "correct_answer": "False",
      "remark": "Vietnam's national flag is a yellow star in front of a red background.",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Slovakia is a member of European Union. 'True' or 'False': ",
      "correct_answer": "True",
      "remark": "This is true.",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Jingle Bells was originally meant for Thanksgiving. 'True' or 'False': ",
      "correct_answer": "True",
      "remark": "Written in 1850 by James Lord Pierpont (1822–1893) at Simpson Tavern in Medford, Massachusetts, and published under the title 'The One Horse Open Sleigh' in 1857, Jingle Bells has been claimed to have been originally written to be sung by a Sunday school choir for Thanksgiving, or as a drinking song.",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Ping-Pong originated in England. 'True' or 'False': ",
      "correct_answer": "True",
      "remark": "Ping-Pong, also Table Tennis, made its appearance in England in the late 19th Century.",
      "incorrect_answers": [
        "False"
      ]
    }
  ],

  "medium": [
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "What is the world's most expensive spice by weight? \nA. Saffron \nB. Cinnamon\n\nChoose A or B: ",
      "correct_answer": "A",
      "remark": "Saffron is the world's most expensive spice by weight.",
      "incorrect_answers": [
        "Cinnamon",
        "Cardamom",
        "Vanilla"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "In a standard set of playing cards, which is the only king without a moustache?\nA. Hearts \nB. Diamonds\n\nChoose A or B: ",
      "correct_answer": "A",
      "remark": "The only king, in a standard set of playing cards, without a moustache is Hearts.",
      "incorrect_answers": [
        "Spades",
        "Diamonds",
        "Clubs"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "When was the Declaration of Independence approved by the Second Continental Congress?\nA. May 4, 1776 \nB. July 4, 1776\n\nChoose A or B: ",
      "correct_answer": "B",
      "remark": "the Declaration of Independence was approved by the Second Continental Congress on July 4, 1776.",
      "incorrect_answers": [
        "May 4, 1776",
        "June 4, 1776",
        "July 2, 1776"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "What name represents the letter 'M' in the NATO phonetic alphabet?\nA. Mike \nB. Matthew\n\nChoose A or B: ",
      "correct_answer": "A",
      "remark": "Mike is the name that represents the letter 'M' in the NATO phonetic alphabet.",
      "incorrect_answers": [
        "Matthew",
        "Mark",
        "Max"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "Scotch whisky and Drambuie make up which cocktail?\nA. Rustry Nail \nB. Manhattan\n\nChoose A or B: ",
      "correct_answer": "A",
      "remark": "Scotch whisky and Drambuie make up the Rustry Nail cocktail",
      "incorrect_answers": [
        "Screwdriver",
        "Sex on the Beach",
        "Manhattan"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "In the Morse code, which letter is indicated by 3 dots? \nA. O \nB. S\n\nChoose A or B: ",
      "correct_answer": "B",
      "remark": "In the Morse code, the letter 'S' is indicated by 3 dots",
      "incorrect_answers": [
        "O",
        "A",
        "C"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "Which of the following Ivy League universities has its official motto in Hebrew as well as in Latin?\nA. Yale University \nB. Princeton University\n\nChoose A or B: ",
      "correct_answer": "A",
      "remark": "Yale University has its official motton in both Hebrew and Latin.",
      "incorrect_answers": [
        "Princeton University",
        "Harvard University",
        "Columbia University"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "What is a 'dakimakura'? \nA. A yoga posture \nB. A body pillow\n\nChoose A or B: ",
      "correct_answer": "B",
      "remark": "A 'dakimakura' is a body pillow.",
      "incorrect_answers": [
        "A Chinese meal, essentially composed of fish",
        "A yoga posture",
        "A word used to describe two people who truly love each other"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "In 2013 how much money was lost by Nigerian scams?\nA. $95 Million \nB. $12.7 Billion\n\nChoose A or B: ",
      "correct_answer": "B",
      "remark": "$12.7 Billion was lost in 2012 via Nigerian scam activities.",
      "incorrect_answers": [
        "$95 Million",
        "$956 Million",
        "$2.7 Billion"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "What was the destination of the missing flight MH370?\nA. Beijing \nB. Kuala Lumpur\n\nChoose A or B: ",
      "correct_answer": "A",
      "remark": "flight MH370 was headed for Beijing when it went missing.",
      "incorrect_answers": [
        "Kuala Lumpur",
        "Singapore",
        "Tokyo"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "What alcoholic drink is mainly made from juniper berries?\nA. Gin \nB. Tequila\n\nChoose A or B: ",
      "correct_answer": "A",
      "remark": "Gin is mainly made from juniper berries.",
      "incorrect_answers": [
        "Vodka",
        "Rum",
        "Tequila"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "What is the German word for 'spoon'?\nA. Gabel \nB. Löffel\n\nChoose A or B: ",
      "correct_answer": "B",
      "remark": "'Löffel' is the German word for 'spoon'.",
      "incorrect_answers": [
        "Gabel",
        "Messer",
        "Essst&auml;bchen"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "What is the romanized Japanese word for 'university'? \nA. Jimusho \nB. Daigaku\n\nChoose A or B: ",
      "correct_answer": "B",
      "remark": "The romanized Japanese word for 'university' is 'Daigaku'.",
      "incorrect_answers": [
        "Toshokan",
        "Jimusho",
        "Shokudou"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "What country saw a world record 315 million voters turn out for elections on May 20, 1991?\nA. United States of America \nB. India\n\nChoose A or B: ",
      "correct_answer": "B",
      "remark": "India holds the world record for voter turn outs during an election.",
      "incorrect_answers": [
        "United States of America",
        "Soviet Union",
        "Poland"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "On average, Americans consume 100 pounds of what per second? \nA. Chocolate \nB. Donuts\n\nChoose A or B: ",
      "correct_answer": "A",
      "remark": "Americans consume 100 pounds of chocolate per second, on average.",
      "incorrect_answers": [
        "Potatoes",
        "Donuts",
        "Cocaine"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "When was Nintendo founded? \nA. March 4th, 1887 \nB. September 23rd, 1889\n\nChoose A or B: ",
      "correct_answer": "B",
      "remark": "The gaming company Nintendo was founded on September 23rd, 1889.",
      "incorrect_answers": [
        "October 19th, 1891",
        "March 4th, 1887",
        "December 27th, 1894"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "What direction does the Statue of Liberty face?\nA. Southwest \nB. Southeast\n\nChoose A or B: ",
      "correct_answer": "B",
      "remark": "The Statue of Liberty faces Southeast.",
      "incorrect_answers": [
        "Southwest",
        "Northwest",
        "Northeast"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "What was the soft drink Pepsi originally introduced as?\nA. Brad's Drink \nB. Pepsin Syrup\n\nChoose A or B: ",
      "correct_answer": "A",
      "remark": "Pepsi was originally introduced as Brad's drink.",
      "incorrect_answers": [
        "Pepsin Pop",
        "Carolina Cola",
        "Pepsin Syrup"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "Where does water from Poland Spring water bottles come from?\nA. Hesse, Germany \nB. Main, United States\n\nChoose A or B: ",
      "correct_answer": "B",
      "remark": "Water from Poland Spring water bottles come from Main, USA.",
      "incorrect_answers": [
        "Hesse, Germany",
        "Masovia, Poland",
        "Bavaria, Poland"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "Computer manufacturer Compaq was acquired for $25 billion dollars in 2002 by which company?\nA. Hewlett-Packard \nB. Toshiba\n\nChoose A or B: ",
      "correct_answer": "A",
      "remark": "The company was acquired by Hewlett-Packard.",
      "incorrect_answers": [
        "Toshiba",
        "Asus",
        "Dell"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "What is the currency of Poland?\nA. Złoty \nB. Euro\n\nChoose A or B: ",
      "correct_answer": "A",
      "remark": "The Polish currency is Złoty.",
      "incorrect_answers": [
        "Ruble",
        "Euro",
        "Krone"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "What was the name given to Japanese military dictators who ruled the country through the 12th and 19th Century?\nA. Shogun \nB. Samurai\n\nChoose A or B: ",
      "correct_answer": "A",
      "remark": "Shogun was the name given to Japanese military dictators who ruled the country through the 12th and 19th Century.",
      "incorrect_answers": [
        "Ninja",
        "Samurai",
        "Shinobi"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "Which American manufactured submachine gun was informally known by the American soldiers that used it as 'Grease Gun'? \nA. Colt 9mm \nB. M3\n\nChoose A or B: ",
      "correct_answer": "B",
      "remark": "The M3 was informally referred to as the 'Greese Gun'.",
      "incorrect_answers": [
        "Colt 9mm",
        "Thompson",
        "MAC-10"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "What is the full title of the Prime Minister of the UK?\nA. First Lord of the Treasury \nB. Manager of the Crown Estate\n\nChoose A or B: ",
      "correct_answer": "A",
      "remark": "The full title of the Prime Minister of the UK is First Lord of the Treasury.",
      "incorrect_answers": [
        "Duke of Cambridge",
        "Her Majesty&#039;s Loyal Opposition",
        "Manager of the Crown Estate"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "medium",
      "question": "Frank Lloyd Wright was the architect behind what famous building?\nA. The Guggenheim \nB. Sydney Opera House\n\nChoose A or B: ",
      "remark": "Frank Lloyd Wright was the architect behind the famous Guggenheim.",
      "correct_answer": "A",
      "incorrect_answers": [
        "Villa Savoye",
        "Sydney Opera House",
        "The Space Needle"
      ]
    }
  ],

  "difficult": [
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "Electronic music producer Kygo's popularity skyrocketed after a certain remix. Which song did he remix? \nA. I See Fire - Ed Sheeran \nB. Sexual Healing - Marvin Gaye \nC. Midnight - Coldplay\nD. Take On Me - a-ha\n\nChoose A, B, C or D: ",
      "correct_answer": "A",
      "remark": "Kygo's popularity skyrocketed after his remix of Ed Sheeran's 'I See Fire'.",
      "incorrect_answers": [
        "Marvin Gaye - Sexual Healing",
        "Coldplay - Midnight",
        "a-ha - Take On Me"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "What is the airspeed velocity of an unladen swallow? \nA. 15 MPH \nB. 20 MPH \nC. 24 MPH\nD. 200 MPH\n\nChoose A, B, C or D: ",
      "correct_answer": "C",
      "remark": "An unladen swallow has an airspeed velocity of 24 MPH.",
      "incorrect_answers": [
        "15 MPH",
        "20 MPH",
        "200 MPH"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "The words 'bungalow' and 'shampoo' originate from the languages of which country? \nA. Papua New Guinea \nB. Ethiopia \nC. China\nD. India\n\nChoose A, B, C or D: ",
      "correct_answer": "D",
      "remark": "The words 'bungalow' and 'shampoo' originated from India.",
      "incorrect_answers": [
        "Papua New Guinea",
        "Ethiopia",
        "China"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "When was 'YouTube' founded? \nA. February 14, 2005 \nB. August 5, 2001 \nC. January 12, 2003\nD. July 19, 2009\n\nChoose A, B, C or D: ",
      "correct_answer": "A",
      "remark": "The video sharing platform 'YouTube' was founded on February 14, 2005.",
      "incorrect_answers": [
        "May 22, 2004",
        "September 12, 2005",
        "July 19, 2009"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "Before the 19th Century, the 'Living Room' was originally called the...\nA. Open Room \nB. Sitting room \nC. Loft\nD. Parlour\n\nChoose A, B, C or D: ",
      "correct_answer": "D",
      "remark": "the 'Living Room' was called the 'Parlour' before the 19th Century.",
      "incorrect_answers": [
        "Open Room",
        "Sitting Room",
        "Loft"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "What is the romanized Chinese word for 'airplane'? \nA. Zongxian \nB. Huojian \nC. Feiji\nD. Qiche\n\nChoose A, B, C or D: ",
      "correct_answer": "C",
      "remark": "The romanized Chinese word for 'airplane' is 'Feiji'.",
      "incorrect_answers": [
        "Qiche",
        "Zongxian",
        "Huojian"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "The Swedish word 'Grunka' means what in English? \nA. Thing \nB. Pineapple \nC. People\nD. Place\n\nChoose A, B, C or D: ",
      "correct_answer": "A",
      "remark": "The Swedish word 'Grunka' means 'Thing' in English.",
      "incorrect_answers": [
        "People",
        "Place",
        "Pineapple"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "Which one of these Swedish companies was founded in 1943?  \nA. H & M \nB. Clas Ohlson \nC. Lindex\nD. IKEA\n\nChoose A, B, C or D: ",
      "correct_answer": "D",
      "remark": "IKEA was founded in 1943.",
      "incorrect_answers": [
        "H &amp; M",
        "Lindex",
        "Clas Ohlson"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "According to the 2014-2015 Australian Bureau of Statistics, what percentage of Australians were born overseas? \nA. 13% \nB. 28% \nC. 7%\nD. 20%\n\nChoose A, B, C or D: ",
      "correct_answer": "B",
      "remark": "According to the 2014-2015 Australian Bureau of Statistics, 28 percent of Australians were born overseas.",
      "incorrect_answers": [
        "13%",
        "20%",
        "7%"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "What does the Latin phrase 'Veni, vidi, vici' translate into English? \nA. See no evil, hear no evil, speak no evil \nB. Past, present, and future \nC. I came, I saw, I conquered\nD. Life, liberty and happiness\n\nChoose A, B, C or D: ",
      "correct_answer": "C",
      "remark": "",
      "incorrect_answers": [
        "See no evil, hear no evil, speak no evil",
        "Life, liberty, and happiness",
        "Past, present, and future"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "If someone said 'you are olid', what would they mean? \nA. You are incomprehensible/an idiot \nB. You are out of shape/weak \nC. Your appearance is repulsive \nD. You smell extremely unpleasant\n\nChoose A, B, C or D: ",
      "correct_answer": "D",
      "remark": "",
      "incorrect_answers": [
        "You are out of shape/weak.",
        "Your appearance is repulsive.",
        "You are incomprehensible/an idiot."
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "Named after the mallow flower, mauve is a shade of what? \nA. Brown \nB. Pink \nC. Red\nD. Purple\n\nChoose A, B, C or D: ",
      "correct_answer": "D",
      "remark": "Mauve is a shade of purple.",
      "incorrect_answers": [
        "Red",
        "Brown",
        "Pink"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "The Quadrangularis Reversum is best described as which of the following? \nA. A percussion instrument \nB. A chess move \nC. A geometric theorem\nD. A building in Oxford University\n\nChoose A, B, C or D: ",
      "correct_answer": "A",
      "remark": "The Quadrangularis Reversum is a percussion instrument.",
      "incorrect_answers": [
        "A building in Oxford University",
        "A chess move",
        "A geometric theorem"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "Where is Apple Inc. headquartered? \nA. Redwood City, California \nB. Santa Monica, CA \nC. Cupertino, California\nD. Redmond, Washington\n\nChoose A, B, C or D: ",
      "correct_answer": "C",
      "remark": "The popular company is headquartered at Cupertino, California.",
      "incorrect_answers": [
        "Redwood City, California",
        "Redmond, Washington",
        "Santa Monica, CA"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "Which church's interior in Vatican City was designed in 1503 by renaissance architects including Bramante, Michelangelo and Bernini? \nA. St. Mark's Basilica \nB. The Duomo of Florence \nC. St. Peter's Basilica\nD. Catania Cathedral\n\nChoose A, B, C or D: ",
      "correct_answer": "C",
      "remark": "",
      "incorrect_answers": [
        "Catania Cathedral",
        "St. Mark's Basilica",
        "The Duomo of Florence"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "If you planted the seeds of Quercus robur, what would grow? \nA. Grains \nB. Vegetables \nC. Flowers\nD. Trees\n\nChoose A, B, C or D: ",
      "correct_answer": "D",
      "remark": "Quercus robur is a tree.",
      "incorrect_answers": [
        "Grains",
        "Vegetables",
        "Flowers"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "Located in Chile, El Teniente is the world's largest underground mine for what metal? \nA. Silver \nB. Iron \nC. Nickel \nD. Copper\n\nChoose A, B, C or D: ",
      "correct_answer": "D",
      "remark": "El Teniente is the world's largest underground copper mine.",
      "incorrect_answers": [
        "Iron",
        "Nickel",
        "Silver"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "What is the weight of a Gold Bar in Fallout: New Vegas? \nA. 35 Pounds \nB. 40 Pounds \nC. 32.50 Pounds\nD. 30 Pounds\n\nChoose A, B, C or D: ",
      "correct_answer": "A",
      "remark": "",
      "incorrect_answers": [
        "30 Pounds",
        "40 Pounds",
        "32.50 Pounds"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "In 'Battle Cats', what is Moneko / MISS Moneko's critical percentage rate? \nA. 20% \nB. 25% \nC. 15%\nD. 10%\n\nChoose A, B, C or D: ",
      "correct_answer": "C",
      "remark": "",
      "incorrect_answers": [
        "20%",
        "10%",
        "25%"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "multiple",
      "difficulty": "hard",
      "question": "The word 'astasia' means which of the following? \nA. The inability to make decisions \nB. The inability to stand up \nC. The inability to concentrate on anything\nD. A feverish desire to rip one's clothes off\n\nChoose A, B, C or D: ",
      "correct_answer": "B",
      "remark": "The word 'astasia' defines an inability to stand up.",
      "incorrect_answers": [
        "The inability to make decisions",
        "The inability to concentrate on anything",
        "A feverish desire to rip one&#039;s clothes off"
      ]
    }
  ]
}


history = {
    "easy": [
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The Tiananmen Square protests of 1989 were held in Hong Kong. Enter 'True' or 'False': ",
      "correct_answer": "False",
      "remark": "The Tiananmen Square protests of 1989 were held in Beijing.",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The United States Department of Homeland Security was formed in response to the September 11th attacks. Enter 'True' or 'False': ",
      "correct_answer": "True",
      "remark": "The United States Department of Homeland Security (DHS) is the U.S. federal executive department responsible for public security, formed as a direct response to the 9/11 attacks.",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The United States was a member of the League of Nations. Enter 'True' or 'False': ",
      "correct_answer": "False",
      "remark": "Even though the Republican Presidents of the period, and their foreign policy architects, agreed with many of its goals, the United States never joined the League.",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "United States President John F. Kennedy was assassinated during his presidential motorcade in Atlanta, Georgia on November 22nd, 1963. Enter 'True' or 'False': ",
      "correct_answer": "False",
      "remark": "John K. Kennedy was assassinated in Parkland Health, Dallas, Texas.",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Former United States Presidents John Adams and Thomas Jefferson died within hours of each other. Enter 'True' or 'False': ",
      "correct_answer": "True",
      "remark": "The two former US Presidents both died on the same day, July 4, 1826, within 5 hours of each other.",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The United States of America declared their independence from the British Empire on July 4th, 1776. Enter 'True' or 'False': ",
      "correct_answer": "True",
      "remark": "The USA gained independence from the British Empire on July 4th, 1776.",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "In World War ll, Great Britian used inflatable tanks on the ports of Great Britain to divert Hitler away from Normandy/D-day landing. Enter 'True' or 'False': ",
      "correct_answer": "True",
      "remark": "",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Adolf Hitler was tried at the Nuremberg trials. Enter 'True' or 'False': ",
      "correct_answer": "False",
      "remark": "Hitler was never tried as he committed suicide before he could be apprehended.",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The French Kingdom helped the United States gain their independence over Great Britain during the Revolutionary War. Enter 'True' or 'False': ",
      "correct_answer": "True",
      "remark": "Between 1778 and 1782 the French provided supplies, arms and ammunition, uniforms, and, most importantly, troops and naval support that made America's victory against the British a possibility.",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Thomas Crapper was a plumber who invented the flushing toilet. Enter 'True' or 'False': ",
      "correct_answer": "False",
      "remark": "",
      "incorrect_answers": [
        "True"
      ]
    }
  ],
    "medium": [
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "medium",
      "question": "Which of these countries was sea charted in 1500 by the Portuguese maritime explorations?\nA. Brazil\nB. India\n\nChoose A or B: ",
      "correct_answer": "A",
      "remark": "Brazil was the country charted in 1500 by the Portuguese maritime explorations.",
      "incorrect_answers": [
        "India",
        "Mozambique",
        "Madagascar"
      ]
    },
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "medium",
      "question": "What historical event was Tchaikovsky's 1812 Overture referencing?\nA. The Napoleonic Wars\nB. The Russian Revolution\n\nChoose A or B: ",
      "correct_answer": "A",
      "remark": "Tchaikovsky's 1812 Overture referenced the Napoleonic Wars.",
      "incorrect_answers": [
        "The American War of 1812",
        "The Russian Revolution",
        "The Charge of the Light Brigade (Crimean War)"
      ]
    },
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "medium",
      "question": "Which of the following ancient Near Eastern peoples still exists as a modern ethnic group?\nA. Babylonians\nB. Assyrians\n\nChoose A or B: ",
      "correct_answer": "B",
      "remark": "The Assyrians still exists in modern societies.",
      "incorrect_answers": [
        "Babylonians",
        "Hittites",
        "Elamites"
      ]
    },
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "medium",
      "question": "How many times was Albert Einstein married in his lifetime?\nA. Twice\nB. Once\n\nChoose A or B: ",
      "correct_answer": "A",
      "remark": "Albert Einstein was married twice in his lifetime.",
      "incorrect_answers": [
        "Five",
        "Thrice",
        "Once"
      ]
    },
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "medium",
      "question": "When Christopher Columbus sailed to America, what was the first region he arrived in?\nA. Florida\nB. The Bahamas Archipelago\n\nChoose A or B: ",
      "correct_answer": "B",
      "remark": "",
      "incorrect_answers": [
        "Florida",
        "Isthmus of Panama",
        "Nicaragua"
      ]
    },
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "medium",
      "question": "When did the United States formally declare war on Japan, entering World War II?\nA. June 22, 1941\nB. December 8, 1941\n\nChoose A or B: ",
      "correct_answer": "B",
      "remark": "U.S. Congress Joint Resolution signed by President Roosevelt on December 8, 1941 at 4:10 p.m., Public Law 77-328, 55 STAT 795, declared war on Japan.",
      "incorrect_answers": [
        "June 6, 1944",
        "June 22, 1941",
        "September 1, 1939"
      ]
    },
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "medium",
      "question": "Who was the first president born in the independent United States?\nA. James Monroe\nB. Martin Van Buren\n\nChoose A or B: ",
      "correct_answer": "B",
      "remark": "Martin Van Buren, the 8th US President, was the first president of the country to be born after the country became independent from the British Empire.",
      "incorrect_answers": [
        "John Adams",
        "George Washington",
        "James Monroe "
      ]
    },
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "medium",
      "question": "What year did Australia become a federation?\nA. 1901\nB. 1910\n\nChoose A or B: ",
      "correct_answer": "A",
      "remark": "",
      "incorrect_answers": [
        "1910",
        "1899",
        "1911"
      ]
    },
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "medium",
      "question": "Which U.S. President was in office when the Gulf War began?\nA. George H. W. Bush\nB. George W. Bush\n\nChoose A or B: ",
      "correct_answer": "A",
      "remark": "The U.S. President in office when the 1990-1991 armed campaign waged by a 39-country military coalition in response to the Iraqi invasion of Kuwait was George H. W. Bush.",
      "incorrect_answers": [
        "Richard Nixon",
        "George W. Bush ",
        "Ronald Regan"
      ]
    },
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "medium",
      "question": "Which Louis was known as 'The Sun King of France'?\nA. Louis XIII\nB. Louis XIV\n\nChoose A or B: ",
      "correct_answer": "B",
      "remark": "Louis XIV, also known as Louis the Great or the Sun King, was King of France from 1643 until his death in 1715.",
      "incorrect_answers": [
        "Louis XIII",
        "Louis XV",
        "Louis XVI"
      ]
    }
  ],
    "difficult": [
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "hard",
      "question": "Spain was formed in 1469 with the marriage of Isabella I of Castile and Ferdinand II of what other Iberian kingdom? \nA. Navarre\nB. León\nC. Aragon\nD. Galicia\n\nChoose A, B, C, or D: ",
      "correct_answer": "C",
      "remark": "",
      "incorrect_answers": [
        "Galicia",
        "León",
        "Navarre"
      ]
    },
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "hard",
      "question": "What year was Canada founded in?\nA. 1867\nB. 1798\nC. 1859\nD. 1668\n\nChoose A, B, C, or D: ",
      "correct_answer": "A",
      "remark": "",
      "incorrect_answers": [
        "1798",
        "1859",
        "1668"
      ]
    },
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "hard",
      "question": "What age was King Henry V when he died?\nA. 35\nB. 62\nC. 87\nD. 73\n\nChoose A, B, C, or D: ",
      "correct_answer": "A",
      "remark": "Henry V died of dysentry on 31 August 1422 at the Château de Vincennes at age 35.",
      "incorrect_answers": [
        "62",
        "87",
        "73"
      ]
    },
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "hard",
      "question": "What year was the United States Declaration of Independence signed?\nA. 1777\nB. 1774\nC. 1775\nD. 1776\n\nChoose A, B, C, or D: ",
      "correct_answer": "D",
      "remark": "",
      "incorrect_answers": [
        "1775",
        "1774",
        "1777"
      ]
    },
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "hard",
      "question": "Which day did World War I begin?\nA. January 28\nB. July 28\nC. June 28\nD. April 28\n\nChoose A, B, C, or D: ",
      "correct_answer": "B",
      "remark": "At the dawn of the 20th century, few anticipated a global war, but what came to be known as the Great War began on June 28, 1914, with the assassinations of Austrian Archduke Franz Ferdinand and his wife, Sophie, while they were visiting Sarajevo, Bosnia, a country recently annexed into the Austrian Empire.",
      "incorrect_answers": [
        "January 28",
        "June 28",
        "April 28"
      ]
    },
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "hard",
      "question": "What was the last colony the UK ceded marking the end of the British Empire?\nA. Ireland\nB. Australia\nC. India\nD. Hong Kong\n\nChoose A, B, C, or D: ",
      "correct_answer": "D",
      "remark": "The last significant colony of the British Empire was Hong Kong, which was returned to Chinese sovereignty in 1997.",
      "incorrect_answers": [
        "India",
        "Australia",
        "Ireland"
      ]
    },
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "hard",
      "question": "Which countries participated in the Lobster War?\nA. France and Brazil\nB. Canada and Norway\nC. Australia and New Zealand\nD. United States and England\n\nChoose A, B, C, or D: ",
      "correct_answer": "A",
      "remark": "The Lobster War was a dispute over spiny lobsters that occurred from 1961 to 1963 between Brazil and France when the Brazilian government refused to allow French fishing vessels to catch spiny lobsters 100 miles off Brazil's northeastern coast, arguing that lobsters 'crawl along the continental shelf'.",
      "incorrect_answers": [
        "Canada and Norway",
        "Australia and New Zealand",
        "United States and England"
      ]
    },
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "hard",
      "question": "During World War I, which nation's monarchs were blood related?\nA. France, Russia, Germany\nB. Serbia, Russia, Croatia\nC. England, Germany, Russia\nD. Germany, Spain, Austria\n\nChoose A, B, C, or D: ",
      "correct_answer": "C",
      "remark": "At the time of the First World War, the rulers of the world's three greatest nations: King George V of Great Britain, Tsar Nicholas II of Russia, and Kaiser Wilhelm II of Germany, were first cousins",
      "incorrect_answers": [
        "France, Russia, Germany",
        "Serbia, Russia, Croatia",
        "Germany, Spain, Austria"
      ]
    },
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "hard",
      "question": "Which U.S. president was said to have been too honest to lie to his father about chopping down a cherry tree?\nA. George Washington\nB. Abraham Lincoln\nC. Thomas Jefferson\nD. James Monroe\n\nChoose A, B, C, or D: ",
      "correct_answer": "A",
      "remark": "For years people have shared the popular legend about the first U.S. president involving a hatchet, a cherry tree, and a young Washington who “cannot tell a lie. The story is however proven to be false.",
      "incorrect_answers": [
        "Abraham Lincoln",
        "Thomas Jefferson",
        "James Monroe"
      ]
    },
    {
      "category": "History",
      "type": "multiple",
      "difficulty": "hard",
      "question": "After the 1516 Battle of Marj Dabiq, the Ottoman Empire took control of Jerusalem from which sultanate?\nA. Ayyubid\nB. Ummayyad\nC. Mamluk\nD. Seljuq\n\nChoose A, B, C, or D: ",
      "correct_answer": "C",
      "remark": " Palestine (Jerusalem) had been under the control of the Mamluk Sultanate until the Ottoman Empire, under the leadership of Sultan Selim I, took it from the Mamluks  at the Battle of Marj Dābiq in 1516.",
      "incorrect_answers": [
        "Ayyubid",
        "Ummayyad",
        "Seljuq"
      ]
    }
  ]
}


geography = {
    "easy": [],
    "medium": [],
    "difficult": []
}


science_and_nature = {
    "easy": [],
    "medium": [],
    "difficult": []
}