Starting_Street = {
    "name": "a street behind the Stanky Rat Pub",
    #"name" can be changed if desired
    "description": "",

    "exits": {"mafia"},
}


Mafia_Bosses_Office = {
    "name": "Mariano Giovanni's Office",

    "description": "n/a",

    "exits": {"bar"},
}


Bar = {
    "name": "Local Bar",

    "description": "Empty bar, early to be drinking.",

    "exits": {"outside bar"}
}

Outside_Bar = {
    "name": "Outside Bar",

    "description": "Narrow passage between two buildings where the attack takes place.",

    "exits": {"liberty island"}
}

Liberty_Island = {
    "name": "Liberty Island Cafe",

    "description": "Cafe owned by a family that you have interest in working with.",

    "exits": {"taxi"}
}

Taxi = {
    "name": "Taxi to Casino",

    "description": "A taxi needed to make the journey to the casino. Although, something unexpected happens.",

    "exits": {"casino"}
}

Casino = {
    "name": "Casino, also Bar 2",

    "description": "",

    "exits": {"warehouse"}
}

Warehouse = {
    "name": "Warehouse",

    "description": "This is where the deal takes place.",


    #technically no exit. this is last location.
    "exits": {},
}

#More locations to be added

All_Locations = {
    "mafia" : Mafia_Bosses_Office,
    "warehouse" : Warehouse,
    "street" : Starting_Street,
    "bar" : Bar,
    "casino" : Casino,
    "outside bar" : Outside_Bar,
    "liberty island" : Liberty_Island,
    "taxi": Taxi,

}
