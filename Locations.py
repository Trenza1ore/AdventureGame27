Starting_Street = {
    "name": "a street behind the Stanky Rat Pub",
    #"name" can be changed if desired
    "description": "",

    "exits": {Mafia_Bosses_Office},
}


Mafia_Bosses_Office = {
    "name": "Mariano Giovanni's Office",

    "description": "n/a",

    "exits": {Bar},
}


Bar = {
    "name": "Local Bar",

    "description": "Empty bar, early to be drinking.",

    "exits": {Outside_Bar_Attack}
}

Outside_Bar = {
    "name": "Outside Bar",

    "description": "Narrow passage between two buildings where the attack takes place.",

    "exits": {Liberty_Island}
}

Liberty_Island = {
    "name": "Liberty Island Cafe",

    "description": "Cafe owned by a family that you have interest in working with.",

    "exits": {Taxi}"
}

Taxi = {
    "name": "Taxi to Casino",

    "description": "A taxi needed to make the journey to the casino. Although, something unexpected happens.",

    "exits": {Casino}
}

Casino = {
    "name": "Casino, also Bar 2",

    "description": ""

    "exits": {Warehouse}
}

Warehouse = {
    "name": "Warehouse",

    "description": "This is where the deal takes place.",

    "exits": {},
}

#More locations to be added

All_Locations = {
    "mafia" : Mafia_Bosses_Office,
    "warehouse" : Warehouse,
    "street" : Starting_Street
    "bar" : Bar,
    "casino" : Casino,
    "outside bar" : Outside_Bar,
    "liberty island" : Liberty_Island,
    "taxi": Taxi,

}
