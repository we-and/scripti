action_verbs = ["says", "asks", "whispers", "shouts", "murmurs", "exclaims"]

characterSeparators=[
        "CHARACTER_SEMICOL_TAB",
        "CHARACTER_TAB",
        
        "CHARACTER_SPACES",
        "CHARACTERUPPERCASE_DIALOG"
,        "CHARACTER_SEMICOL_DIALOG",
"TIMECODE_SPACE_TIMECODE_SPACE_DIALOG"

]
cellLayoutModes=[
    "NUM_SPACE_CHARACTERUPPERCASE_SEMICOLON_DIALOG",
    "CHARACTERUPPERCASE_NEWLINE_DIALOG"
]

multilineCharacterSeparators=[
        
        "CHARACTER_NEWLINE_DIALOG_NEWLINE_NEWLINE",
        
        "TIMECODE_NEWLINE_CHARACTERINBRACKETS_DIALOG_NEWLINE_NEWLINE",
        
        "LINE_NEWLINE_TIMECODE_ARROW_TIMECODE_NEWLINE_TEXT_ITAG",                                     #YOUNG HEARTS
        
        "TIMECODE_HYPHEN_TIMECODE_NEWLINE_CHARACTER_SEMICOLON_NEWLINE_DIALOG_NEWLINE",  #Badlands
        
        "TIMECODE_HYPHEN_TIMECODE_NEWLINE_CHARACTER_NEWLINE_DIALOG",  #The perfect Mate transcript

        "NUM_TIMECODE_ARROW_TIMECODE_NEWLINE_MULTILINEDIALOG",#Mascarpone txt

        "NUM_SEMICOLON_TIMECODE_SPACE_TIMECODE_SPACE_TIME",#KOKON 24FPS
        
        "TIMECODE_ARROW_TIMECODE_NEWLINE_BRACKETS_CHARACTER_DIALOG_NEWLINE_DIALOG"  ,     #DESP_LIST,
        
        "TIMECODE_HYPHEN_UPPERCASECHARACTER_SPACE_SEMICOLON_DOUBLESPACE_TEXT_NEWLINE_TEXT"
        
]
countMethods=[
    "ALL",
    "ALL_NOSPACE"
    "ALL_NOPUNC",
    "ALL_NOSPACE_NOPUNC",
    "ALL_NOAPOS",
    
]


filterToReplace=[
        "(O.S)", "(ON/OS)", "(V.O)", "(V.O.)", "(VO)", "(V.O", "(ON PHONE",
        "(O.S.)", "(OS)", "(OS/ON)","(ON)","(OVERLAPPING)"
        "(CON'T)", "(CONT.)", "(CONT.", "(CON’T)", "(CON’T)", "(CONT'D)",
        " CONT’D", " CONT'D", "(CONT.)", "(CONT)", "(CONT'D", "(CONT’D"

]