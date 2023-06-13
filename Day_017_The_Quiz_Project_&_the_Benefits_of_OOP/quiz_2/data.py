import random

general_knowledge_data = [
    {
      "question": "Coca-Cola&#039;s original colour was green.",
      "correct_answer": "False"
    },
    {
      "question": "Gumbo is a stew that originated in Louisiana.",
      "correct_answer": "True"
    },
    {
      "question": "This is the correct spelling of 'Supercalifragilisticexpialidocious'.",
      "correct_answer": "True"
    },
    {
      "question": "The vapor produced by e-cigarettes is actually water.",
      "correct_answer": "False"
    },
    {
      "question": "The sum of all the numbers on a roulette wheel is 666.",
      "correct_answer": "True"
    },
    {
      "question": "Furby was released in 1998.",
      "correct_answer": "True"
    },
    {
      "question": "Nutella is produced by the German company Ferrero.",
      "correct_answer": "False"
    },
    {
      "question": "There are 86400 seconds in a day.",
      "correct_answer": "True"
    },
    {
      "question": "The word 'news' originates from the first letters of the 4 main directions on a compass (North, East, West, South).",
      "correct_answer": "False"
    },
    {
      "question": "A scientific study on peanuts in bars found traces of over 100 unique specimens of urine.",
      "correct_answer": "False"
    },
    {
      "question": "'Number 16 Bus Shelter' was a children's name that was approved by the New Zealand government.",
      "correct_answer": "True"
    },
    {
      "question": "'Ananas' is mostly used as the word for Pineapple in other languages.",
      "correct_answer": "True"
    },
    {
      "question": "The Sun rises from the North.",
      "correct_answer": "False"
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The color orange is named after the fruit.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "You can legally drink alcohol while driving in Mississippi.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "medium",
      "question": "The French word to travel is 'Travail'",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Pluto is a planet.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "medium",
      "question": "The French word for 'glass' is 'glace'.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "One of Donald Trump's 2016 Presidential Campaign promises was to build a border wall between the United States and Mexico.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "medium",
      "question": "'Santa Claus'; is a variety of melon.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Dihydrogen Monoxide was banned due to health risks after being discovered in 1983 inside swimming pools and drinking water.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Scotland voted to become an independent country during the referendum from September 2014.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "medium",
      "question": "The scientific name for the Southern Lights is Aurora Australis?",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Popcorn was invented in 1871 by Frederick W. Rueckheim in the USA where he sold the snack on the streets of Chicago.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Vietnam's national flag is a red star in front of a yellow background.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "A pasodoble is a type of Italian pasta sauce.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "medium",
      "question": "'Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo.' is a grammatically correct sentence.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "hard",
      "question": "NCIS stands for 'Navy Corps Investigative Service'.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "General Knowledge",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Ping-Pong originated in England",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    }
  ]


history_data = [
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "hard",
      "question": "Japan was part of the Allied Powers during World War I.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The Cold War ended with Joseph Stalin's death.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The Tiananmen Square protests of 1989 were held in Hong Kong.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The Spitfire originated from a racing plane.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "medium",
      "question": "'I disapprove of what you say, but I will defend to the death your right to say' is a quote from French philosopher Voltaire.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Brezhnev was the 5th leader of the USSR.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Former United States Presidents John Adams and Thomas Jefferson died within hours of each other.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Theodore Roosevelt Jr. was the only General involved in the initial assault on D-Day.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "medium",
      "question": "In 1967, a magazine published a story about extracting hallucinogenic chemicals from bananas to raise moral questions about banning drugs.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The United States of America declared their independence from the British Empire on July 4th, 1776.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Abraham Lincoln was the first U.S. President to be born outside the borders of the thirteen original states. ",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "medium",
      "question": "The Hundred Years' War was fought for more than a hundred years.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "In World War ll, Great Britian used inflatable tanks on the ports of Great Britain to divert Hitler away from Normandy/D-day landing.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Adolf Hitler was tried at the Nuremberg trials.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Kublai Khan is the grandchild of Genghis Khan?",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "hard",
      "question": "During the Winter War, the amount of Soviet Union soliders that died or went missing was five times more than Finland's.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The United States of America was the first country to launch a man into space.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Thomas Crapper was a plumber who invented the flushing toilet.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "hard",
      "question": "The man that shot Alexander Hamilton was named Aaron Burr.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "History",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Franz Joseph I was the last emperor of Austria.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    }
  ]

geography_data = [
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "medium",
      "question": "The flag of South Africa features 7 colours.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Greenland is almost as big as Africa.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The Republic of Malta is the smallest microstate worldwide.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "medium",
      "question": "There are no roads in/out of Juneau, Alaska.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "easy",
      "question": "There is a city called Rome in every continent on Earth.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "medium",
      "question": "The longest place named in the United States is Lake Chargoggagoggmanchauggagoggchaubunagungamaugg, located near Webster, MA.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Alaska is the largest state in the United States.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Vietnam is the only country in the world that starts with V. ",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Ottawa is the capital of Canada.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "easy",
      "question": "There are no deserts in Europe.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "medium",
      "question": "'Mongolia' was a part of the now non-existent U.S.S.R.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "medium",
      "question": "The Sonoran Desert is located in eastern Africa.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Japan has left-hand side traffic.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Liechtenstein does not have an airport.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Norway has a larger land area than Sweden.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Tokyo is the capital of Japan.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Hungary is the only country in the world beginning with H.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "easy",
      "question": "New Haven is the capital city of the state of Connecticut in the United States.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "easy",
      "question": "Rhode Island is actually located on the US mainland, despite its name.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "category": "Geography",
      "type": "boolean",
      "difficulty": "medium",
      "question": "Is Tartu the capital of Estonia?",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    }
  ]