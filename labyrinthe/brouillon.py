
def fateOfTile(adj):
    print(l1.serealize())
    print(serealizeBlock(adj))
    match adj:
        # Edges with nothing in vicinity
        case [  # Top edge, nothing in vivinity
                ["W",       "W",         "W"      ],
                ["U" | "H", _  ,         "U" | "H"],
                ["U" | "H", "U" | "H",   "U" | "H"]
            ]:
            # debug(l, adj, i, j, collapsable, "Adding to collapsable.", False)
            print("Collapsable") 

        case [  # Top edge, auto collapsable to Hall
                ["W",       "W",         "W"      ],
                ["W",       _  ,         "U" | "H"],
                ["U" | "H", "U" | "H",   "U" | "H"]
            ] | [
                ["W",       "W",         "W"      ],
                ["U" | "H", _  ,         "W"      ],
                ["U" | "H", "U" | "H",   "U" | "H"]
            ]:
                print("collapsed to H")
        case [  # Left edge, nothing in vicinity
                ["W", "U" | "H",     "U" | "H"],
                ["W", _  ,           "U" | "H"],
                ["W", "U" | "H",     "U" | "H"]
            ]:
            # debug(l, adj, i, j, collapsable, "Adding to collapsable", False)
            print("Collapsable") 
        case [  # Left edge, auto collapse to hall
                ["W", "W",           "U" | "H"],
                ["W", _  ,           "U" | "H"],
                ["W", "U" | "H",     "U" | "H"]
            ] | [
                ["W", "U" | "H",     "U" | "H"],
                ["W", _  ,           "U" | "H"],
                ["W", "W",           "U" | "H"]
            ]:
                print("collapsed to H")
        case [  # Right edge, nothing in vicinity
                ["U" | "H",    "U" | "H", "W"],
                ["U" | "H",    _        , "W"],
                ["U" | "H",    "U" | "H", "W"]
            ]:
            print("Collapsable") 
        case [  # Right edge, auto collapse
                ["U" | "H",    "W"      , "W"],
                ["U" | "H",    _        , "W"],
                ["U" | "H",    "U" | "H", "W"]
            ] | [
                ["U" | "H",    "U" | "H", "W"],
                ["U" | "H",    _        , "W"],
                ["U" | "H",    "W"      , "W"]
            ]:
                print("collapsed to H")
        case [  # Bottom edge, nothing in vicinity
                ["U" | "H", "U" | "H", "U" | "H"],
                ["U" | "H", _        , "U" | "H"],
                ["W"      , "W"      , "W"      ]
              ]:
            print("Collapsable") 
        case [  # Bottom edge, auto collapse
                ["U" | "H", "U" | "H", "U" | "H"],
                ["W"      , _        , "U" | "H"],
                ["W"      , "W"      , "W"      ]
              ] | [  
                ["U" | "H", "U" | "H", "U" | "H"],
                ["U" | "H", _        , "W"      ],
                ["W"      , "W"      , "W"      ]
             ]:
                print("collapsed to H")
        
        # ADD to COLLAPSABLE
        case [
                [_        , "W"      , _        ],
                ["U" | "H", _        , "U" | "H"],
                ["U" | "H", "U" | "H", "U" | "H"]
              ] | [
                [_  , "U" | "H", "U" | "H"],
                ["W", _        , "U" | "H"],
                [_  , "U" | "H", "U" | "H"]
              ] | [
                ["U" | "H", "U" | "H", _  ],
                ["U" | "H", _        , "W"],
                ["U" | "H", "U" | "H", _  ]
              ] | [
                ["U" | "H", "U" | "H", "U" | "H"],
                ["U" | "H", _        , "U" | "H"],
                [_        , "W"      , _        ]
            ]:
                print("Collapsable") 
        # COLLPASES to HALL
        case [
                _            ,
                ["W", _, "W"],
                _
            ]:
                print("auto collapsed to H")


        case _:                
            print("Nothing can be done here")

    print(adj)
    for i in range(10):
        print(l1.grid[i])
            # debug(l, adj, i, j, collapsable, "No case yet", False)
# while True:
#     x = int(input("x = "))
#     y = int(input("y = "))
#     fateOfTile(l1.adjacent(x, y))
