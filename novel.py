import re
from pyformlang.fst import FST
from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State , NondeterministicFiniteAutomaton , EpsilonNFA
from pyformlang.cfg import CFG
l=list()

sequence = ""

estado0="Estado 0"
estado1="Estado 1"
estado2="Estado 2"
estado3="Estado 3"
estado4="Estado 4"
estado5="Estado 5"
estado6="Estado 6"
estado7="Estado 7"
estado8="Estado 8"
estado9="Estado 9"
estado10="Estado 10"
estado11="Estado 11"
estado12="Estado 12"
estado13="Estado 13"
estado14="Estado 14"
estado15="Estado 15"
estado16="Estado 16"
estado17="Estado 17"
estado18="Estado 18"
estado19="Estado 19"
estado20="Estado 20"
estado21="Estado 21"
estado22="Estado 22"
estado23="Estado 23"
estado24="Estado 24"
estado25="Estado 25"
estado26="Estado 26"
estado27="Estado 27"
estado28="Estado 28"
estado29="Estado 29"
estado30="Estado 30"
estado31="Estado 31"
estado32="Estado 32"
estado33="Estado 33"
estado34="Estado 34"
estado35="Estado 35"
estado36="Estado 36"
estado37="Estado 37"
estado38="Estado 38"
estado39="Estado 39"
estado40="Estado 40"
estado41="Estado 41"
estado42="Estado 42"
estado43="Estado 43"
estado44="Estado 44"
estado45="Estado 45"
estado46="Estado 46"
estado47="Estado 47"
estado48="Estado 48"
estado49="Estado 49"
estado50="Estado 50"
estado51="Estado 51"
estado52="Estado 52"
estado53="Estado 53"
estado54="Estado 54"
estado55="Estado 55"
estado56="Estado 56"
estado57="Estado 57"
estado58="Estado 58"
estado59="Estado 59"
estado60="Estado 60"
estado61="Estado 61"
estado62="Estado 62"
estado63="Estado 63"
estado64="Estado 64"
estado65="Estado 65"
estado66="Estado 66"
estado67="Estado 67"
estado68="Estado 68"
estado69="Estado 69"
estado70="Estado 70"
estado71="Estado 71"
estado72="Estado 72"
estado73="Estado 73"
estado74="Estado 74"
estado75="Estado 75"
estado76="Estado 76"
estado77="Estado 77"
estado78="Estado 78"
estado79="Estado 79"
estado80="Estado 80"
estado81="Estado 81"
estado82="Estado 82"
estado83="Estado 83"
estado84="Estado 84"
estado85="Estado 85"
estado86="Estado 86"
estado87="Estado 87"
estado88="Estado 88"
estado89="Estado 89"
estado90="Estado 90"
estado91="Estado 91"
estado92="Estado 92"
estado93="Estado 93"
estado94="Estado 94"
estado95="Estado 95"

story1=DeterministicFiniteAutomaton()
story2=DeterministicFiniteAutomaton()
story3=DeterministicFiniteAutomaton()
story4=DeterministicFiniteAutomaton()
story5=DeterministicFiniteAutomaton()
story6=DeterministicFiniteAutomaton()
story7=DeterministicFiniteAutomaton()
story8=DeterministicFiniteAutomaton()
story9=DeterministicFiniteAutomaton()
story10=DeterministicFiniteAutomaton()
story11=DeterministicFiniteAutomaton()

l=[]
transitions1=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c0"),
    
]

transitions2=[
     #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),
]
p=[

("q","0","q"),
("q","1","q"),

]
transitions3=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),

    ("q1","0","q3"),
    ("q1","1","q4"),

    ("q2","2","q5"),
    ("q2","3","q6"),
]
transitions4=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),

    ("q1","0","q3"),
    ("q1","1","q4"),

    ("q2","2","q5"),
    ("q2","3","q6"),

    ("q3","z","e"),
    ("q3","z","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","z","e"),
    ("q5","z","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),
]
transitions5=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),

    ("q1","0","q3"),
    ("q1","1","q4"),

    ("q2","2","q5"),
    ("q2","3","q6"),

    ("q3","z","e"),
    ("q3","z","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","z","e"),
    ("q5","z","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","z","e"),
    ("q9","z","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

]
transitions6=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),

    ("q1","0","q3"),
    ("q1","1","q4"),

    ("q2","2","q5"),
    ("q2","3","q6"),

    ("q3","z","e"),
    ("q3","z","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","z","e"),
    ("q5","z","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","z","e"),
    ("q9","z","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

    ("q11","z","e"),
    ("q11","z","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","z","e"),
    ("q13","z","e"),

    ("q14","2","q19"),
    ("q14","3","q20"),

    ("q15","4","q21"),
    ("q15","5","q21"),

    ("q16","6","q23"),
    ("q16","7","q24"),

]
transitions7=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),

    ("q1","0","q3"),
    ("q1","1","q4"),

    ("q2","2","q5"),
    ("q2","3","q6"),

    ("q3","z","e"),
    ("q3","z","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","z","e"),
    ("q5","z","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","z","e"),
    ("q9","z","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

    ("q11","z","e"),
    ("q11","z","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","z","e"),
    ("q13","z","e"),

    ("q14","2","q19"),
    ("q14","3","q20"),

    ("q15","4","q21"),
    ("q15","5","q21"),

    ("q16","6","q23"),
    ("q16","7","q24"),

    ("q17","z","e"),
    ("q17","z","e"),

    ("q18","0","q25"),
    ("q18","1","q26"),

    ("q19","2","q27"),
    ("q19","3","q28"),

    ("q20","4","q29"),
    ("q20","5","q30"),

    ("q21","6","q31"),
    ("q21","7","q32"),

    ("q22","8","q33"),
    ("q22","9","q34"),

    ("q23","a","q35"),
    ("q23","b","q36"),

    ("q24","z","e"),
    ("q24","z","e"),

]
transitions8=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),

    ("q1","0","q3"),
    ("q1","1","q4"),

    ("q2","2","q5"),
    ("q2","3","q6"),

    ("q3","z","e"),
    ("q3","z","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","z","e"),
    ("q5","z","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","z","e"),
    ("q9","z","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

    ("q11","z","e"),
    ("q11","z","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","z","e"),
    ("q13","z","e"),

    ("q14","2","q19"),
    ("q14","3","q20"),

    ("q15","4","q21"),
    ("q15","5","q21"),

    ("q16","6","q23"),
    ("q16","7","q24"),

    ("q17","z","e"),
    ("q17","z","e"),

    ("q18","0","q25"),
    ("q18","1","q26"),

    ("q19","2","q27"),
    ("q19","3","q28"),

    ("q20","4","q29"),
    ("q20","5","q30"),

    ("q21","6","q31"),
    ("q21","7","q32"),

    ("q22","8","q33"),
    ("q22","9","q34"),

    ("q23","a","q35"),
    ("q23","b","q36"),

    ("q24","z","e"),
    ("q24","z","e"),

    ("q25","0","q37"),
    ("q25","1","q38"),

    ("q26","z","e"),
    ("q26","z","e"),

    ("q27","2","q39"),
    ("q27","3","40"),

    ("q28","4","q41"),
    ("q28","5","q42"),

    ("q29","6","q43"),
    ("q29","7","q44"),

    ("q30","z","e"),
    ("q30","z","e"),

    ("q31","8","q45"),
    ("q31","9","q46"),

    ("q32","z","e"),
    ("q32","z","e"),

    ("q33","a","q47"),
    ("q33","b","q48"),

    ("q34","z","e"),
    ("q34","z","e"),

    ("q35","z","e"),
    ("q35","z","e"),

    ("q36","z","e"),
    ("q36","z","e"),
]
transitions9=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),

    ("q1","0","q3"),
    ("q1","1","q4"),

    ("q2","2","q5"),
    ("q2","3","q6"),

    ("q3","z","e"),
    ("q3","z","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","z","e"),
    ("q5","z","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","z","e"),
    ("q9","z","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

    ("q11","z","e"),
    ("q11","z","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","z","e"),
    ("q13","z","e"),

    ("q14","2","q19"),
    ("q14","3","q20"),

    ("q15","4","q21"),
    ("q15","5","q21"),

    ("q16","6","q23"),
    ("q16","7","q24"),

    ("q17","z","e"),
    ("q17","z","e"),

    ("q18","0","q25"),
    ("q18","1","q26"),

    ("q19","2","q27"),
    ("q19","3","q28"),

    ("q20","4","q29"),
    ("q20","5","q30"),

    ("q21","6","q31"),
    ("q21","7","q32"),

    ("q22","8","q33"),
    ("q22","9","q34"),

    ("q23","a","q35"),
    ("q23","b","q36"),

    ("q24","z","e"),
    ("q24","z","e"),

    ("q25","0","q37"),
    ("q25","1","q38"),

    ("q26","z","e"),
    ("q26","z","e"),

    ("q27","2","q39"),
    ("q27","3","40"),

    ("q28","4","q41"),
    ("q28","5","q42"),

    ("q29","6","q43"),
    ("q29","7","q44"),

    ("q30","z","e"),
    ("q30","z","e"),

    ("q31","8","q45"),
    ("q31","9","q46"),

    ("q32","z","e"),
    ("q32","z","e"),

    ("q33","a","q47"),
    ("q33","b","q48"),

    ("q34","z","e"),
    ("q34","z","e"),

    ("q35","z","e"),
    ("q35","z","e"),

    ("q36","z","e"),
    ("q36","z","e"),

    ("q37","z","e"),
    ("q37","z","e"),

    ("q38","z","e"),
    ("q38","z","e"),

    ("q39","z","e"),
    ("q39","z","e"),

    ("q40","0","q49"),
    ("q40","1","q50"),

    ("q41","z","e"),
    ("q41","z","e"),
    
    ("q42","z","e"),
    ("q42","z","e"),

    ("q43","z","e"),
    ("q43","z","e"),

    ("q44","2","q51"),
    ("q44","3","q52"),

    ("q45","z","e"),
    ("q45","z","e"),

    ("q46","z","e"),
    ("q46","z","e"),

    ("q47","z","e"),
    ("q47","z","e"),
    
    ("q48","z","e"),
    ("q48","z","e"),
]
transitions10=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),

    ("q1","0","q3"),
    ("q1","1","q4"),

    ("q2","2","q5"),
    ("q2","3","q6"),

    ("q3","z","e"),
    ("q3","z","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","z","e"),
    ("q5","z","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","z","e"),
    ("q9","z","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

    ("q11","z","e"),
    ("q11","z","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","z","e"),
    ("q13","z","e"),

    ("q14","2","q19"),
    ("q14","3","q20"),

    ("q15","4","q21"),
    ("q15","5","q21"),

    ("q16","6","q23"),
    ("q16","7","q24"),

    ("q17","z","e"),
    ("q17","z","e"),

    ("q18","0","q25"),
    ("q18","1","q26"),

    ("q19","2","q27"),
    ("q19","3","q28"),

    ("q20","4","q29"),
    ("q20","5","q30"),

    ("q21","6","q31"),
    ("q21","7","q32"),

    ("q22","8","q33"),
    ("q22","9","q34"),

    ("q23","a","q35"),
    ("q23","b","q36"),

    ("q24","z","e"),
    ("q24","z","e"),

    ("q25","0","q37"),
    ("q25","1","q38"),

    ("q26","z","e"),
    ("q26","z","e"),

    ("q27","2","q39"),
    ("q27","3","40"),

    ("q28","4","q41"),
    ("q28","5","q42"),

    ("q29","6","q43"),
    ("q29","7","q44"),

    ("q30","z","e"),
    ("q30","z","e"),

    ("q31","8","q45"),
    ("q31","9","q46"),

    ("q32","z","e"),
    ("q32","z","e"),

    ("q33","a","q47"),
    ("q33","b","q48"),

    ("q34","z","e"),
    ("q34","z","e"),

    ("q35","z","e"),
    ("q35","z","e"),

    ("q36","z","e"),
    ("q36","z","e"),

    ("q37","z","e"),
    ("q37","z","e"),

    ("q38","z","e"),
    ("q38","z","e"),

    ("q39","z","e"),
    ("q39","z","e"),

    ("q40","0","q49"),
    ("q40","1","q50"),

    ("q41","z","e"),
    ("q41","z","e"),
    
    ("q42","z","e"),
    ("q42","z","e"),

    ("q43","z","e"),
    ("q43","z","e"),

    ("q44","2","q51"),
    ("q44","3","q52"),

    ("q45","z","e"),
    ("q45","z","e"),

    ("q46","z","e"),
    ("q46","z","e"),

    ("q47","z","e"),
    ("q47","z","e"),
    
    ("q48","z","e"),
    ("q48","z","e"),

    ("q40","0","q49"),
    ("q40","1","q50"),

    ("q44","0","q51"),
    ("q44","1","q52"),

    ("q49","z","e"),
    ("q49","z","e"),

    ("q50","z","e"),
    ("q50","z","e"),

    ("q51","z","e"),
    ("q51","z","e"),

    ("q52","z","e"),
    ("q52","z","e"),
]
transitions11=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),

    ("q1","0","q3"),
    ("q1","1","q4"),

    ("q2","2","q5"),
    ("q2","3","q6"),

    ("q3","z","e"),
    ("q3","z","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","z","e"),
    ("q5","z","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","z","e"),
    ("q9","z","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

    ("q11","z","e"),
    ("q11","z","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","z","e"),
    ("q13","z","e"),

    ("q14","2","q19"),
    ("q14","3","q20"),

    ("q15","4","q21"),
    ("q15","5","q21"),

    ("q16","6","q23"),
    ("q16","7","q24"),

    ("q17","z","e"),
    ("q17","z","e"),

    ("q18","0","q25"),
    ("q18","1","q26"),

    ("q19","2","q27"),
    ("q19","3","q28"),

    ("q20","4","q29"),
    ("q20","5","q30"),

    ("q21","6","q31"),
    ("q21","7","q32"),

    ("q22","8","q33"),
    ("q22","9","q34"),

    ("q23","a","q35"),
    ("q23","b","q36"),

    ("q24","z","e"),
    ("q24","z","e"),

    ("q25","0","q37"),
    ("q25","1","q38"),

    ("q26","z","e"),
    ("q26","z","e"),

    ("q27","2","q39"),
    ("q27","3","40"),

    ("q28","4","q41"),
    ("q28","5","q42"),

    ("q29","6","q43"),
    ("q29","7","q44"),

    ("q30","z","e"),
    ("q30","z","e"),

    ("q31","8","q45"),
    ("q31","9","q46"),

    ("q32","z","e"),
    ("q32","z","e"),

    ("q33","a","q47"),
    ("q33","b","q48"),

    ("q34","z","e"),
    ("q34","z","e"),

    ("q35","z","e"),
    ("q35","z","e"),

    ("q36","z","e"),
    ("q36","z","e"),

    ("q37","z","e"),
    ("q37","z","e"),

    ("q38","z","e"),
    ("q38","z","e"),

    ("q39","z","e"),
    ("q39","z","e"),

    ("q40","0","q49"),
    ("q40","1","q50"),

    ("q41","z","e"),
    ("q41","z","e"),
    
    ("q42","z","e"),
    ("q42","z","e"),

    ("q43","z","e"),
    ("q43","z","e"),

    ("q44","2","q51"),
    ("q44","3","q52"),

    ("q45","z","e"),
    ("q45","z","e"),

    ("q46","z","e"),
    ("q46","z","e"),

    ("q47","z","e"),
    ("q47","z","e"),
    
    ("q48","z","e"),
    ("q48","z","e"),

    ("q40","0","q49"),
    ("q40","1","q50"),

    ("q44","0","q51"),
    ("q44","1","q52"),

    ("q49","z","e"),
    ("q49","z","e"),

    ("q50","z","e"),
    ("q50","z","e"),

    ("q51","z","e"),
    ("q51","z","e"),

    ("q52","z","e"),
    ("q52","z","e"),
]

transitionsc2=[
    #Ruta colegio
    ("c0","c","c1"),
    ("c0","d","c2"),
]

transitionsc3=[
    #Ruta Profesor-final
    ("c1","z","e"),
    #Ruta amiga
    ("c2","c","c3"),
    ("c2","d","c4"),
]
transitionsc4=[
    #Ruta presionar
    ("c3","c","c5"),
    ("c3","d","c6"),
    #Ruta Buscar Gabriel
    ("c4","e","c7"),
    ("c4","f","c8"),
]
transitionsc5=[
    #Ruta Amenazar Silencio
    ("c5","c","c9"),
    ("c5","d","c10"),
    #Ruta Cazar Gabriel
    ("c6","e","c11"),
    ("c6","f","c12"),
    #Ruta Perseguir
    ("c7","g","c13"),
    ("c7","h","c14"),
    #Ruta Policía-final
    ("c8","z","e"),
]
transitionsc6=[
    #Ruta Plan en la noche
    ("c9","c","c15"),
    ("c9","d","c16"),
    #Ruta Plan en el día-final
    ("c10","z","e"),
    #Ruta Pasar derecho
    ("c11","e","c17"),
    ("c11","f","c18"),
    #Ruta Ir callejon-final
    ("c12","z","e"),
    #Ruta Busca afuera
    ("c13","g","c19"),
    ("c13","h","c20"),
    #Ruta Buscar piso 2°
    ("c14","i","c21"),
    ("c14","j","c22"),
]
transitionsc7=[
    #Ruta Escucharle
    ("c15","c","c23"),
    ("c15","d","c24"),
    #Ruta Acabar con él-final
    ("c16","z","e"),
    #Ruta Saltar Obstáculo-final
    ("c17","z","e"),
    #Ruta Rodear Obstáculo
    ("c18","e","c26"),
    ("c18","f","c27"),
    #Ruta Ir contra profesor 
    ("c19","g","c28"),
    ("c19","h","c29"),
    #Ruta Aceptar reunión
    ("c20","i","c30"),
    ("c20","j","c31"),
    #Ruta Acercarse-final
    ("c21","z","e"),
    #Ruta Hablarle-final
    ("c22","z","e"),
]
transitionsc8=[
    #Ruta Perdonar-final
    ("c23","z","e"),
    #Ruta Huir-final
    ("c24","z","e"),
    #Ruta Acabarle-final
    ("c25","z","e"),
    #Ruta Forcejear-final
    ("c26","z","e"),
    #Ruta Redimir-final
    ("c27","z","e"),
    #Ruta Acabar con Gabriel-final
    ("c28","z","e"),
    #Ruta Rendirse-final
    ("c29","z","e"),
    #Ruta Sobornado-final
    ("c30","z","e"),
    #Ruta No aceptar
    ("c31","c","c32"),
    ("c31","d","c33"),
]
transitionsc9=[
    #Ruta Confrontar
    ("c32","c","34"),
    ("c32","d","35"),
    #Ruta Disimular
    ("c33","e","36"),
    ("c33","f","37"),
]
transitionsc10=[
    #Ruta Directamente-final
    ("c34","z","e"),
    #Ruta Sorpresa
    ("c35","c","c38"),
    ("c35","d","c39"),
    #Ruta Incendio-final
    ("c36","z","e"),
    #Ruta Policía-final
    ("c37","z","e"),
]
transitionsc11=[
    #Ruta Venganza-final
    ("c38","z","e"),
    #Ruta Policía-final
    ("c39","z","e"),
]


story1.add_transitions(transitions1)
story1.add_start_state("q")
story1.add_final_state("e")
story2.add_transitions(transitions2)
story2.add_transitions(transitionsc2)
story2.add_start_state("q")
story2.add_final_state("e")
story3.add_transitions(transitions3)
story3.add_transitions(transitionsc2)
story3.add_transitions(transitionsc3)
story3.add_start_state("q")
story3.add_final_state("e")
story4.add_transitions(transitions4)
story4.add_transitions(transitionsc2)
story4.add_transitions(transitionsc3)
story4.add_transitions(transitionsc4)
story4.add_start_state("q")
story4.add_final_state("e")
story5.add_transitions(transitions5)
story5.add_transitions(transitionsc2)
story5.add_transitions(transitionsc3)
story5.add_transitions(transitionsc4)
story5.add_transitions(transitionsc5)
story5.add_start_state("q")
story5.add_final_state("e")
story6.add_transitions(transitions6)
story6.add_transitions(transitionsc2)
story6.add_transitions(transitionsc3)
story6.add_transitions(transitionsc4)
story6.add_transitions(transitionsc5)
story6.add_transitions(transitionsc6)
story6.add_start_state("q")
story6.add_final_state("e")
story7.add_transitions(transitions7)
story7.add_transitions(transitionsc2)
story7.add_transitions(transitionsc3)
story7.add_transitions(transitionsc4)
story7.add_transitions(transitionsc5)
story7.add_transitions(transitionsc6)
story7.add_transitions(transitionsc7)
story7.add_start_state("q")
story7.add_final_state("e")
story8.add_transitions(transitions8)
story8.add_transitions(transitionsc2)
story8.add_transitions(transitionsc3)
story8.add_transitions(transitionsc4)
story8.add_transitions(transitionsc5)
story8.add_transitions(transitionsc6)
story8.add_transitions(transitionsc7)
story8.add_transitions(transitionsc8)
story8.add_start_state("q")
story8.add_final_state("e")
story9.add_transitions(transitions9)
story9.add_transitions(transitionsc2)
story9.add_transitions(transitionsc3)
story9.add_transitions(transitionsc4)
story9.add_transitions(transitionsc5)
story9.add_transitions(transitionsc6)
story9.add_transitions(transitionsc7)
story9.add_transitions(transitionsc8)
story9.add_transitions(transitionsc9)
story9.add_start_state("q")
story9.add_final_state("e")
story10.add_transitions(transitions10)
story10.add_transitions(transitionsc2)
story10.add_transitions(transitionsc3)
story10.add_transitions(transitionsc4)
story10.add_transitions(transitionsc5)
story10.add_transitions(transitionsc6)
story10.add_transitions(transitionsc7)
story10.add_transitions(transitionsc8)
story10.add_transitions(transitionsc9)
story10.add_transitions(transitionsc10)
story10.add_start_state("q")
story10.add_final_state("e")
story11.add_transitions(transitions11)
story11.add_transitions(transitionsc2)
story11.add_transitions(transitionsc3)
story11.add_transitions(transitionsc4)
story11.add_transitions(transitionsc5)
story11.add_transitions(transitionsc6)
story11.add_transitions(transitionsc7)
story11.add_transitions(transitionsc8)
story11.add_transitions(transitionsc9)
story11.add_transitions(transitionsc10)
story11.add_transitions(transitionsc11)
story11.add_start_state("q")
story11.add_final_state("e")

story1.add_final_state("q0")
story1.add_final_state("c0")
story2.add_final_state("q1")
story2.add_final_state("q2")
story2.add_final_state("c1")
story2.add_final_state("c2")
story3.add_final_state("q3")
story3.add_final_state("q4")
story3.add_final_state("q5")
story3.add_final_state("q6")
story3.add_final_state("c3")
story3.add_final_state("c4")
story4.add_final_state("q7")
story4.add_final_state("q8")
story4.add_final_state("q9")
story4.add_final_state("q10")
story4.add_final_state("c5")
story4.add_final_state("c6")
story4.add_final_state("c7")
story4.add_final_state("c8")
story5.add_final_state("q11")
story5.add_final_state("q12")
story5.add_final_state("q13")
story5.add_final_state("q14")
story5.add_final_state("q15")
story5.add_final_state("q16")
story5.add_final_state("c9")
story5.add_final_state("c10")
story5.add_final_state("c11")
story5.add_final_state("c12")
story5.add_final_state("c13")
story5.add_final_state("c14")
story6.add_final_state("q17")
story6.add_final_state("q18")
story6.add_final_state("q19")
story6.add_final_state("q20")
story6.add_final_state("q21")
story6.add_final_state("q22")
story6.add_final_state("q23")
story6.add_final_state("q24")
story6.add_final_state("c15")
story6.add_final_state("c16")
story6.add_final_state("c17")
story6.add_final_state("c18")
story6.add_final_state("c19")
story6.add_final_state("c20")
story6.add_final_state("c21")
story6.add_final_state("c22")
story7.add_final_state("q25")
story7.add_final_state("q26")
story7.add_final_state("q27")
story7.add_final_state("q28")
story7.add_final_state("q29")
story7.add_final_state("q30")
story7.add_final_state("q31")
story7.add_final_state("q32")
story7.add_final_state("q33")
story7.add_final_state("q34")
story7.add_final_state("q35")
story7.add_final_state("q36")
story7.add_final_state("c23")
story7.add_final_state("c24")
story7.add_final_state("c25")
story7.add_final_state("c26")
story7.add_final_state("c27")
story7.add_final_state("c28")
story7.add_final_state("c29")
story7.add_final_state("c30")
story7.add_final_state("c31")
story8.add_final_state("q37")
story8.add_final_state("q38")
story8.add_final_state("q39")
story8.add_final_state("q40")
story8.add_final_state("q41")
story8.add_final_state("q42")
story8.add_final_state("q43")
story8.add_final_state("q44")
story8.add_final_state("q45")
story8.add_final_state("q46")
story8.add_final_state("q47")
story8.add_final_state("q48")
story8.add_final_state("c32")
story8.add_final_state("c33")
story9.add_final_state("q49")
story9.add_final_state("q50")
story9.add_final_state("q51")
story9.add_final_state("q52")
story9.add_final_state("c34")
story9.add_final_state("c35")
story9.add_final_state("c36")
story9.add_final_state("c37")
story10.add_final_state("c38")
story10.add_final_state("c39")

#Reemplaza los nombres y mantiene todo lo demas igual
reemplazar = FST()
name=""

lista=[
    ("q0","A","q0",["A"]),
    ("q0","B","q0",["B"]),
    ("q0","C","q0",["C"]),
    ("q0","D","q0",["D"]),
    ("q0","E","q0",["E"]),
    ("q0","F","q0",["F"]),
    ("q0","G","q0",["G"]),
    ("q0","H","q0",["H"]),
    ("q0","I","q0",["I"]),
    ("q0","J","q0",["J"]),
    ("q0","K","q0",["K"]),
    ("q0","L","q0",["L"]),
    ("q0","M","q0",["M"]),
    ("q0","N","q0",["N"]),
    ("q0","O","q0",["O"]),
    ("q0","P","q0",["P"]),
    ("q0","Q","q0",["Q"]),
    ("q0","R","q0",["R"]),
    ("q0","S","q0",["S"]),
    ("q0","T","q0",["T"]),
    ("q0","U","q0",["U"]),
    ("q0","V","q0",["V"]),
    ("q0","W","q0",["W"]),
    ("q0","X","q0",["X"]),
    ("q0","Y","q0",["Y"]),
    ("q0","Z","q0",["Z"]),
    ("q0","a","q0",["a"]),
    ("q0","b","q0",["b"]),
    ("q0","c","q0",["c"]),
    ("q0","d","q0",["d"]),
    ("q0","e","q0",["e"]),
    ("q0","f","q0",["f"]),
    ("q0","g","q0",["g"]),
    ("q0","h","q0",["h"]),
    ("q0","i","q0",["i"]),
    ("q0","j","q0",["j"]),
    ("q0","k","q0",["k"]),
    ("q0","l","q0",["l"]),
    ("q0","m","q0",["m"]),
    ("q0","n","q0",["n"]),
    ("q0","o","q0",["o"]),
    ("q0","p","q0",["p"]),
    ("q0","q","q0",["q"]),
    ("q0","r","q0",["r"]),
    ("q0","s","q0",["s"]),
    ("q0","t","q0",["t"]),
    ("q0","u","q0",["u"]),
    ("q0","v","q0",["v"]),
    ("q0","w","q0",["w"]),
    ("q0","x","q0",["x"]),
    ("q0","y","q0",["y"]),
    ("q0","z","q0",["z"]),
    ("q0"," ","q0",[" "]),
    ("q0",".","q0",["."]),
    ("q0",",","q0",[","]),
    ("q0","1","q0",["1"]),
    ("q0","2","q0",["2"]),
    ("q0","3","q0",["3"]),
    ("q0","4","q0",["4"]),
    ("q0","5","q0",["5"]),
    ("q0","6","q0",["6"]),
    ("q0","7","q0",["7"]),
    ("q0","8","q0",["8"]),
    ("q0","9","q0",["9"]),
    ("q0","0","q0",["0"]),
    ("q0","ñ","q0",["ñ"]),
    ("q0","#","q1",[""]),
    ("q1","$","q2",[""]),
    ("q2","%","q3",[name]),
    ("q3","epsilon","q0",[""]),
]
reemplazar.add_transitions(lista)
reemplazar.add_start_state("q0")
reemplazar.add_final_state("q0")


h = CFG.from_text("""
S -> a S | A
A -> b A | epsilon""")
print(h.get_cnf_parse_tree("ab"))

print(story11.accepts("0000"))

from pyformlang.cfg import CFG

# Define a CFG for generating simple dialogues
dialogue_grammar = CFG.from_text("""
S -> Greeting Name Question
Greeting -> "Hello" | "Hi" | "Hey"
Name -> "John" | "Mary" | "Bob"
Question -> "How are you?" | "What's up?" | "How's it going?"
""")

# Generate a dialogue
dialogue = dialogue_grammar.get_words()
print(dialogue.close())
   
def dialogos(transitionLevel, string):
    value = string[-1]
    response = ""
    match transitionLevel:
        case 1:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
        case 2:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
                case 'c':
                    response = ""
                case 'd':
                    response = ""
        case 3:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
                case '2':
                    response = ""
                case '3':
                    response = ""
                case 'c':
                    response = ""
                case 'd':
                    response = ""
        case 4:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
                case '2':
                    response = ""
                case '3':
                    response = ""
                case 'c':
                    response = ""
                case 'd':
                    response = ""
                case 'e':
                    response = ""
                case 'f':
                    response = ""
        case 5:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
                case '2':
                    response = ""
                case '3':
                    response = ""
                case '4':
                    response = ""
                case '5':
                    response = ""
                case 'c':
                    response = ""
                case 'd':
                    response = ""
                case 'e':
                    response = ""
                case 'f':
                    response = ""
                case 'g':
                    response = ""
                case 'h':
                    response = ""
        case 6:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
                case '2':
                    response = ""
                case '3':
                    response = ""
                case '4':
                    response = ""
                case '5':
                    response = ""
                case '6':
                    response = ""
                case '7':
                    response = ""
                case 'c':
                    response = ""
                case 'd':
                    response = ""
                case 'e':
                    response = ""
                case 'f':
                    response = ""
                case 'g':
                    response = ""
                case 'h':
                    response = ""
                case 'i':
                    response = ""
                case 'j':
                    response = ""
        case 7:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
                case '2':
                    response = ""
                case '3':
                    response = ""
                case '4':
                    response = ""
                case '5':
                    response = ""
                case '6':
                    response = ""
                case '7':
                    response = ""
                case '8':
                    response = ""
                case '9':
                    response = ""
                case 'a':
                    response = ""
                case 'b':
                    response = ""
                case 'c':
                    response = ""
                case 'd':
                    response = ""
                case 'e':
                    response = ""
                case 'f':
                    response = ""
                case 'g':
                    response = ""
                case 'h':
                    response = ""
                case 'i':
                    response = ""
                case 'j':
                    response = ""
                case 'k':
                    response = ""
        case 8:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
                case '2':
                    response = ""
                case '3':
                    response = ""
                case '4':
                    response = ""
                case '5':
                    response = ""
                case '6':
                    response = ""
                case '7':
                    response = ""
                case '8':
                    response = ""
                case '9':
                    response = ""
                case 'a':
                    response = ""
                case 'b':
                    response = ""
                case 'c':
                    response = ""
                case 'd':
                    response = ""
        case 9:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
                case '2':
                    response = ""
                case '3':
                    response = ""
                case 'c':
                    response = ""
                case 'd':
                    response = ""
                case 'e':
                    response = ""
                case 'f':
                    response = ""
        case 10:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
                case 'c':
                    response = ""
                case 'd':
                    response = ""
        case 11:
            match value:
                case '0':
                    response = "Texto de ejemplo - Vuelve a jugar"
                case '1':
                    response = "Texto de ejemplo - Dejar de jugar"
    return response

def convertOptionToValidSequence(transitionLevel, digitOption):
    if digitOption == 'z':
        return 'z'
    
    if (digitOption != 'a' | digitOption != 'b'):
        return '-1'
    
    if (transitionLevel ==1):
        match digitOption:
            case 'a': digitOption ='0'
            case 'b': digitOption ='1'
        return digitOption
    
    lastOption = sequence[-1]

    match (transitionLevel):
        case 2:
            match lastOption:
                case '0':
                    match digitOption:
                        case 'a': digitOption ='0' # q0 - q1
                        case 'b': digitOption ='1' # q0 - q2
                case '1':
                    match digitOption:
                        case 'a': digitOption ='c' # c0 - c1
                        case 'b': digitOption ='d' # c0 - c2
                case _:
                    digitOption ='z'

        case 3:
            match lastOption:
                case '0':
                    match digitOption:
                        case 'a': digitOption ='0'  # q1 - q3
                        case 'b': digitOption ='1'  # q1 - q4
                case '1':
                    match digitOption:
                        case 'a': digitOption ='2'  # q2 - q5
                        case 'b': digitOption ='3'  # q1 - q6

                case 'd':
                    match digitOption:
                        case 'a': digitOption ='c' # c2 - c3
                        case 'b': digitOption ='d' # c2 - c4
                case _:
                    digitOption ='z'
        case 4:
            match lastOption:
                case '1':
                    match digitOption:
                        case 'a': digitOption ='0' # q4 - q7
                        case 'b': digitOption ='1' # q4 - q8
                
                case '3':
                    match digitOption:
                        case 'a': digitOption ='2' # q6 - q9
                        case 'b': digitOption ='3' # q6 - q10

                case 'c':
                    match digitOption:
                        case 'a': digitOption ='c' # c3 - c5
                        case 'b': digitOption ='d' # c2 - c6
                case 'd':
                    match digitOption:
                        case 'a': digitOption ='e' # c4 - c7
                        case 'b': digitOption ='f' # c2 - c8
                case _:
                    digitOption ='z'
        case 5:
            match lastOption:
                case '0':
                    match digitOption:
                        case 'a': digitOption ='0' # q7 - q11
                        case 'b': digitOption ='1' # q7 - q12
                case '1':
                    match digitOption:
                        case 'a': digitOption ='2' # q8 - q13
                        case 'b': digitOption ='3' # q8 - q14
                case '3':
                    match digitOption:
                        case 'a': digitOption ='4' # q10 - q15
                        case 'b': digitOption ='5' # q10 - q16

                case 'c':
                    match digitOption:
                        case 'a': digitOption ='c' # c5 - c9
                        case 'b': digitOption ='d' # c5 - c10
                case 'd':
                    match digitOption:
                        case 'a': digitOption ='e' # c6 - c11
                        case 'b': digitOption ='f' # c6 - c12
                case 'e':
                    match digitOption:
                        case 'a': digitOption ='g' # c7 - c13
                        case 'b': digitOption ='h' # c7 - c14
                case _:
                    digitOption ='z'
        case 6:
            match lastOption:
                case '1':
                    match digitOption:
                        case 'a': digitOption ='0' # q12 - q17
                        case 'b': digitOption ='1' # q12 - q18
                case '3':
                    match digitOption:
                        case 'a': digitOption ='2' # q14 - q19
                        case 'b': digitOption ='3' # q14 - q20
                case '4':
                    match digitOption:
                        case 'a': digitOption ='4' # q15 - q21
                        case 'b': digitOption ='5' # q15 - q22
                case '5':
                    match digitOption:
                        case 'a': digitOption ='6' # q16 - q23
                        case 'b': digitOption ='7' # q16 - q24

                case 'c':
                    match digitOption:
                        case 'a': digitOption ='c' # c9 - c15
                        case 'b': digitOption ='d' # c9 - c16
                case 'e':
                    match digitOption:
                        case 'a': digitOption ='e' # c11 - c17
                        case 'b': digitOption ='f' # c11 - c18
                case 'g':
                    match digitOption:
                        case 'a': digitOption ='g' # c13 - c19
                        case 'b': digitOption ='h' # c13 - c20
                case 'h':
                    match digitOption:
                        case 'a': digitOption ='i' # c14 - c21
                        case 'b': digitOption ='j' # c14 - c22
                case _:
                    digitOption ='z'
        case 7:
            match lastOption:
                case '1':
                    match digitOption:
                        case 'a': digitOption ='0' # q18 - q25
                        case 'b': digitOption ='1' # q18 - q26
                case '2':
                    match digitOption:
                        case 'a': digitOption ='2' # q19 - q27
                        case 'b': digitOption ='3' # q19 - q28
                case '3':
                    match digitOption:
                        case 'a': digitOption ='4' # q20 - q29
                        case 'b': digitOption ='5' # q20 - q30
                case '4':
                    match digitOption:
                        case 'a': digitOption ='6' # q21 - q31
                        case 'b': digitOption ='7' # q21 - q32
                case '5':
                    match digitOption:
                        case 'a': digitOption ='8' # q22 - q33
                        case 'b': digitOption ='9' # q22 - q34
                case '6':
                    match digitOption:
                        case 'a': digitOption ='a' # q23 - q35
                        case 'b': digitOption ='b' # q23 - q36
                
                case 'c':
                    match digitOption:
                        case 'a': digitOption ='c' # c15 - c23
                        case 'b': digitOption ='d' # c15 - c24
                case 'f':
                    match digitOption:
                        case 'a': digitOption ='e' # c18 - c26
                        case 'b': digitOption ='f' # c18 - c27
                case 'g':
                    match digitOption:
                        case 'a': digitOption ='g' # c19 - c28
                        case 'b': digitOption ='h' # c19 - c29
                case 'h':
                    match digitOption:
                        case 'a': digitOption ='i' # c20 - c30
                        case 'b': digitOption ='j' # c20 - c31
                case _:
                    digitOption ='z'
        case 8:
            match lastOption:
                case '0':
                    match digitOption:
                        case 'a': digitOption ='0' # q25 - q37
                        case 'b': digitOption ='1' # q25 - q38
                case '2':
                    match digitOption:
                        case 'a': digitOption ='2' # q27 - q39
                        case 'b': digitOption ='3' # q27 - q40
                case '3':
                    match digitOption:
                        case 'a': digitOption ='4' # q28 - q41
                        case 'b': digitOption ='5' # q28 - q42
                case '4':
                    match digitOption:
                        case 'a': digitOption ='6' # q29 - q43
                        case 'b': digitOption ='7' # q29 - q44
                case '6':
                    match digitOption:
                        case 'a': digitOption ='8' # q31 - q45
                        case 'b': digitOption ='9' # q31 - q46
                case '8':
                    match digitOption:
                        case 'a': digitOption ='a' # q33 - q47
                        case 'b': digitOption ='b' # q33 - q48
                
                case 'j':
                    match digitOption:
                        case 'a': digitOption ='c' # c31 - c32
                        case 'b': digitOption ='d' # c31 - c33
                case _:
                    digitOption ='z'
        case 9:
            match lastOption:
                case '3':
                    match digitOption:
                        case 'a': digitOption ='0' # q40 - q49
                        case 'b': digitOption ='1' # q40 - q50
                case '7':
                    match digitOption:
                        case 'a': digitOption ='2' # q44 - q51
                        case 'b': digitOption ='3' # q44 - q52

                case 'c':
                    match digitOption:
                        case 'a': digitOption ='c' # c32 - c34
                        case 'b': digitOption ='d' # c32 - c35
                case 'd':
                    match digitOption:
                        case 'a': digitOption ='e' # c33 - c36
                        case 'b': digitOption ='f' # c33 - c37
                case _:
                    digitOption ='z'
                        
        case 10:
            match lastOption:
                case 'd':
                    match digitOption:
                        case 'a': digitOption ='c' # c35 - c38
                        case 'b': digitOption ='d' # c35 - c39
                case _:
                    digitOption ='z'
    return digitOption

from pyformlang.cfg import CFG

cfg1 = CFG.from_text("""
S -> A | B 
A -> a
B -> b """)

def generateSequence(transitionLevel, digitOption):
    if (cfg1.contains(digitOption)):
        sequence += convertOptionToValidSequence(transitionLevel, digitOption)
        return True
    return False