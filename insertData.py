from datetime import datetime

universities = [
    {'name': 'University of the East', 'abbreviation': 'UE'},
    {'name': 'University of Santo Tomas', 'abbreviation': 'UST'},
    {'name': 'Far Eastern University', 'abbreviation': 'FEU'},
    {'name': 'National University', 'abbreviation': 'NU'},
    {'name': 'De La Salle University', 'abbreviation': 'DLSU'},
    {'name': 'Adamson University', 'abbreviation': 'ADU'},
    {'name': 'Ateneo de Manila University', 'abbreviation': 'ADMU'},
    {'name': 'University of the Philippines', 'abbreviation': 'UP'}
]

seasons = [
    {
        'name': 'UAAP Esports Season 1',
        'start_date': datetime(2024, 1, 15),
        'end_date': datetime(2024, 3, 15),
        'status': 'Upcoming'
    }
]


tournaments = [
    {
        'season_code': 'S1',
        'game': 'Valorant',
        'name': 'UAAP Esports Season 1 Valorant Tournament',
        'start_date': datetime(2024, 1, 15),
        'end_date': datetime(2024, 2, 15),
        'status': 'Upcoming'
    },
    {
        'season_code': 'S1',
        'game': 'Mobile Legends Bang Bang',
        'name': 'UAAP Esports Season 1 MLBB Tournament',
        'start_date': datetime(2024, 2, 16),
        'end_date': datetime(2024, 3, 10),
        'status': 'Upcoming'
    },
    {
        'season_code': 'S1',
        'game': 'NBA 2K',
        'name': 'UAAP Esports Season 1 NBA 2K Tournament',
        'start_date': datetime(2024, 3, 11),
        'end_date': datetime(2024, 3, 15),
        'status': 'Upcoming'
    }
]


teams = [
    {
        'university_code': 'UE',
        'season_code': 'S1',
        'tournament_code': 'S1-VALO',
        'game': 'Valorant',
        'name': 'UE Zenith Esports',
        'coach': {
            'first_name': 'Nathan',
            'last_name': 'Santos'
        }
    },
    {
        'university_code': 'UST',
        'season_code': 'S1',
        'tournament_code': 'S1-VALO',
        'game': 'Valorant',
        'name': 'UST Teletigers Esports Club',
        'coach': {
            'first_name': 'Carlos',
            'last_name': 'Reyes'
        }
    },
    {
        'university_code': 'FEU',
        'season_code': 'S1',
        'tournament_code': 'S1-VALO',
        'game': 'Valorant',
        'name': 'FEU Tamaraws Esports',
        'coach': {
            'first_name': 'Gabriel',
            'last_name': 'Cruz'
        }
    },
    {
        'university_code': 'NU',
        'season_code': 'S1',
        'tournament_code': 'S1-VALO',
        'game': 'Valorant',
        'name': 'NU Bulldogs',
        'coach': {
            'first_name': 'Paulo',
            'last_name': 'Rivera'
        }
    },
    {
        'university_code': 'DLSU',
        'season_code': 'S1',
        'tournament_code': 'S1-VALO',
        'game': 'Valorant',
        'name': 'DLSU Viridis Arcus',
        'coach': {
            'first_name': 'Miguel',
            'last_name': 'Delos Reyes'
        }
    },
    {
        'university_code': 'ADU',
        'season_code': 'S1',
        'tournament_code': 'S1-VALO',
        'game': 'Valorant',
        'name': 'Adamson Falcons',
        'coach': {
            'first_name': 'Joseph',
            'last_name': 'Gomez'
        }
    },
    {
        'university_code': 'ADMU',
        'season_code': 'S1',
        'tournament_code': 'S1-VALO',
        'game': 'Valorant',
        'name': 'Ateneo Blue Eagles',
        'coach': {
            'first_name': 'Luis',
            'last_name': 'Mariano'
        }
    },
    {
        'university_code': 'UP',
        'season_code': 'S1',
        'tournament_code': 'S1-VALO',
        'game': 'Valorant',
        'name': 'UP Fighting Maroons',
        'coach': {
            'first_name': 'Joshua',
            'last_name': 'Santiago'
        }
    },
    {
        'university_code': 'UE',
        'season_code': 'S1',
        'tournament_code': 'S1-MLBB',
        'game': 'Mobile Legends Bang Bang',
        'name': 'UE Zenith Esports',
        'coach': {
            'first_name': 'Nathan',
            'last_name': 'Santos'
        }
    },
    {
        'university_code': 'UST',
        'season_code': 'S1',
        'tournament_code': 'S1-MLBB',
        'game': 'Mobile Legends Bang Bang',
        'name': 'UST Teletigers Esports Club',
        'coach': {
            'first_name': 'Carlos',
            'last_name': 'Reyes'
        }
    },
    {
        'university_code': 'FEU',
        'season_code': 'S1',
        'tournament_code': 'S1-MLBB',
        'game': 'Mobile Legends Bang Bang',
        'name': 'FEU Tamaraws Esports',
        'coach': {
            'first_name': 'Gabriel',
            'last_name': 'Cruz'
        }
    },
    {
        'university_code': 'NU',
        'season_code': 'S1',
        'tournament_code': 'S1-MLBB',
        'game': 'Mobile Legends Bang Bang',
        'name': 'NU Bulldogs',
        'coach': {
            'first_name': 'Paulo',
            'last_name': 'Rivera'
        }
    },
    {
        'university_code': 'DLSU',
        'season_code': 'S1',
        'tournament_code': 'S1-MLBB',
        'game': 'Mobile Legends Bang Bang',
        'name': 'DLSU Viridis Arcus',
        'coach': {
            'first_name': 'Miguel',
            'last_name': 'Delos Reyes'
        }
    },
    {
        'university_code': 'ADU',
        'season_code': 'S1',
        'tournament_code': 'S1-MLBB',
        'game': 'Mobile Legends Bang Bang',
        'name': 'Adamson Falcons',
        'coach': {
            'first_name': 'Joseph',
            'last_name': 'Gomez'
        }
    },
    {
        'university_code': 'ADMU',
        'season_code': 'S1',
        'tournament_code': 'S1-MLBB',
        'game': 'Mobile Legends Bang Bang',
        'name': 'Ateneo Blue Eagles',
        'coach': {
            'first_name': 'Luis',
            'last_name': 'Mariano'
        }
    },
    {
        'university_code': 'UP',
        'season_code': 'S1',
        'tournament_code': 'S1-MLBB',
        'game': 'Mobile Legends Bang Bang',
        'name': 'UP Fighting Maroons',
        'coach': {
            'first_name': 'Joshua',
            'last_name': 'Santiago'
        }
    },
    {
        'university_code': 'UE',
        'season_code': 'S1',
        'tournament_code': 'S1-NBA',
        'game': 'NBA 2K',
        'name': 'UE Zenith Esports',
        'coach': {
            'first_name': 'Nathan',
            'last_name': 'Santos'
        }
    },
    {
        'university_code': 'UST',
        'season_code': 'S1',
        'tournament_code': 'S1-NBA',
        'game': 'NBA 2K',
        'name': 'UST Teletigers Esports Club',
        'coach': {
            'first_name': 'Carlos',
            'last_name': 'Reyes'
        }
    },
    {
        'university_code': 'FEU',
        'season_code': 'S1',
        'tournament_code': 'S1-NBA',
        'game': 'NBA 2K',
        'name': 'FEU Tamaraws Esports',
        'coach': {
            'first_name': 'Gabriel',
            'last_name': 'Cruz'
        }
    },
    {
        'university_code': 'NU',
        'season_code': 'S1',
        'tournament_code': 'S1-NBA',
        'game': 'NBA 2K',
        'name': 'NU Bulldogs',
        'coach': {
            'first_name': 'Paulo',
            'last_name': 'Rivera'
        }
    },
    {
        'university_code': 'DLSU',
        'season_code': 'S1',
        'tournament_code': 'S1-NBA',
        'game': 'NBA 2K',
        'name': 'DLSU Viridis Arcus',
        'coach': {
            'first_name': 'Miguel',
            'last_name': 'Delos Reyes'
        }
    },
    {
        'university_code': 'ADU',
        'season_code': 'S1',
        'tournament_code': 'S1-NBA',
        'game': 'NBA 2K',
        'name': 'Adamson Falcons',
        'coach': {
            'first_name': 'Joseph',
            'last_name': 'Gomez'
        }
    },
    {
        'university_code': 'ADMU',
        'season_code': 'S1',
        'tournament_code': 'S1-NBA',
        'game': 'NBA 2K',
        'name': 'Ateneo Blue Eagles',
        'coach': {
            'first_name': 'Luis',
            'last_name': 'Mariano'
        }
    },
    {
        'university_code': 'UP',
        'season_code': 'S1',
        'tournament_code': 'S1-NBA',
        'game': 'NBA 2K',
        'name': 'UP Fighting Maroons',
        'coach': {
            'first_name': 'Joshua',
            'last_name': 'Santiago'
        }
    }
]

players = [
    {
        'first_name': 'John',
        'last_name': 'Cruz',
        'username': 'johncruz01',
        'team_code': 'UE-S1-VALO'
    },
    {
        'first_name': 'Michael',
        'last_name': 'Garcia',
        'username': 'michaelgarcia02',
        'team_code': 'UE-S1-VALO'
    },
    {
        'first_name': 'Chris',
        'last_name': 'Lopez',
        'username': 'chrislopez03',
        'team_code': 'UE-S1-VALO'
    },
    {
        'first_name': 'Joshua',
        'last_name': 'Reyes',
        'username': 'joshuareyes04',
        'team_code': 'UE-S1-VALO'
    },
    {
        'first_name': 'James',
        'last_name': 'Martinez',
        'username': 'jamesmartinez05',
        'team_code': 'UE-S1-VALO'
    },
    {
        'first_name': 'Carlos',
        'last_name': 'Santos',
        'username': 'carlossantos06',
        'team_code': 'UST-S1-VALO'
    },
    {
        'first_name': 'Rafael',
        'last_name': 'Rivera',
        'username': 'rafaelrivera07',
        'team_code': 'UST-S1-VALO'
    },
    {
        'first_name': 'Daniel',
        'last_name': 'Hernandez',
        'username': 'danielhernandez08',
        'team_code': 'UST-S1-VALO'
    },
    {
        'first_name': 'Luis',
        'last_name': 'Castro',
        'username': 'luiscastro09',
        'team_code': 'UST-S1-VALO'
    },
    {
        'first_name': 'Miguel',
        'last_name': 'Torres',
        'username': 'migueltorres10',
        'team_code': 'UST-S1-VALO'
    },
    {
        'first_name': 'Gabriel',
        'last_name': 'Domingo',
        'username': 'gabrieldomingo11',
        'team_code': 'FEU-S1-VALO'
    },
    {
        'first_name': 'Nathan',
        'last_name': 'Cortez',
        'username': 'nathancortez12',
        'team_code': 'FEU-S1-VALO'
    },
    {
        'first_name': 'Jason',
        'last_name': 'Fernandez',
        'username': 'jasonfernandez13',
        'team_code': 'FEU-S1-VALO'
    },
    {
        'first_name': 'Ethan',
        'last_name': 'Morales',
        'username': 'ethanmorales14',
        'team_code': 'FEU-S1-VALO'
    },
    {
        'first_name': 'Ryan',
        'last_name': 'Gutierrez',
        'username': 'ryangutierrez15',
        'team_code': 'FEU-S1-VALO'
    },
    {
        'first_name': 'Brandon',
        'last_name': 'Silva',
        'username': 'brandonsilva16',
        'team_code': 'NU-S1-VALO'
    },
    {
        'first_name': 'Jacob',
        'last_name': 'Ramos',
        'username': 'jacobramos17',
        'team_code': 'NU-S1-VALO'
    },
    {
        'first_name': 'Eric',
        'last_name': 'Navarro',
        'username': 'ericnavarro18',
        'team_code': 'NU-S1-VALO'
    },
    {
        'first_name': 'Adrian',
        'last_name': 'De Leon',
        'username': 'adriandeleon19',
        'team_code': 'NU-S1-VALO'
    },
    {
        'first_name': 'Dylan',
        'last_name': 'Villanueva',
        'username': 'dylanvillanueva20',
        'team_code': 'NU-S1-VALO'
    },
    {
        'first_name': 'Victor',
        'last_name': 'Castillo',
        'username': 'victorcastillo21',
        'team_code': 'DLSU-S1-VALO'
    },
    {
        'first_name': 'Oscar',
        'last_name': 'Lozano',
        'username': 'oscarlozano22',
        'team_code': 'DLSU-S1-VALO'
    },
    {
        'first_name': 'Anthony',
        'last_name': 'Perez',
        'username': 'anthonyperez23',
        'team_code': 'DLSU-S1-VALO'
    },
    {
        'first_name': 'Patrick',
        'last_name': 'Alvarez',
        'username': 'patrickalvarez24',
        'team_code': 'DLSU-S1-VALO'
    },
    {
        'first_name': 'Francis',
        'last_name': 'Flores',
        'username': 'francisflores25',
        'team_code': 'DLSU-S1-VALO'
    },
    {
        'first_name': 'Sebastian',
        'last_name': 'Reyes',
        'username': 'sebastianreyes26',
        'team_code': 'ADU-S1-VALO'
    },
    {
        'first_name': 'Samuel',
        'last_name': 'Ortega',
        'username': 'samuelortega27',
        'team_code': 'ADU-S1-VALO'
    },
    {
        'first_name': 'Jordan',
        'last_name': 'Gonzalez',
        'username': 'jordangonzalez28',
        'team_code': 'ADU-S1-VALO'
    },
    {
        'first_name': 'Cameron',
        'last_name': 'Diaz',
        'username': 'camerondiaz29',
        'team_code': 'ADU-S1-VALO'
    },
    {
        'first_name': 'Alex',
        'last_name': 'Lopez',
        'username': 'alexlopez30',
        'team_code': 'ADU-S1-VALO'
    },
    {
        'first_name': 'Nathaniel',
        'last_name': 'Del Rosario',
        'username': 'nathanieldelrosario31',
        'team_code': 'ADMU-S1-VALO'
    },
    {
        'first_name': 'Ethan',
        'last_name': 'Aguilar',
        'username': 'ethanaguilar32',
        'team_code': 'ADMU-S1-VALO'
    },
    {
        'first_name': 'Christopher',
        'last_name': 'Bautista',
        'username': 'christopherbautista33',
        'team_code': 'ADMU-S1-VALO'
    },
    {
        'first_name': 'David',
        'last_name': 'Ramos',
        'username': 'davidramos34',
        'team_code': 'ADMU-S1-VALO'
    },
    {
        'first_name': 'Paul',
        'last_name': 'Francisco',
        'username': 'paulfrancisco35',
        'team_code': 'ADMU-S1-VALO'
    },
    {
        'first_name': 'Aaron',
        'last_name': 'Castro',
        'username': 'aaroncastro36',
        'team_code': 'UP-S1-VALO'
    },
    {
        'first_name': 'Bryan',
        'last_name': 'Fernandez',
        'username': 'bryanfernandez37',
        'team_code': 'UP-S1-VALO'
    },
    {
        'first_name': 'Justin',
        'last_name': 'Reyes',
        'username': 'justinreyes38',
        'team_code': 'UP-S1-VALO'
    },
    {
        'first_name': 'Liam',
        'last_name': 'Torres',
        'username': 'liamtorres39',
        'team_code': 'UP-S1-VALO'
    },
    {
        'first_name': 'Oscar',
        'last_name': 'Santos',
        'username': 'oscarsantos40',
        'team_code': 'UP-S1-VALO'
    },
    {
        'first_name': 'Mark',
        'last_name': 'Villanueva',
        'username': 'markvillanueva01',
        'team_code': 'UE-S1-MLBB'
    },
    {
        'first_name': 'Adrian',
        'last_name': 'Lorenzo',
        'username': 'adrianlorenzo02',
        'team_code': 'UE-S1-MLBB'
    },
    {
        'first_name': 'Gabriel',
        'last_name': 'Ramos',
        'username': 'gabrielramos03',
        'team_code': 'UE-S1-MLBB'
    },
    {
        'first_name': 'Steven',
        'last_name': 'Santos',
        'username': 'stevensantos04',
        'team_code': 'UE-S1-MLBB'
    },
    {
        'first_name': 'Raymond',
        'last_name': 'Gomez',
        'username': 'raymondgomez05',
        'team_code': 'UE-S1-MLBB'
    },
    {
        'first_name': 'Joseph',
        'last_name': 'Cortez',
        'username': 'josephcortez01',
        'team_code': 'UST-S1-MLBB'
    },
    {
        'first_name': 'Daniel',
        'last_name': 'Moreno',
        'username': 'danielmoreno02',
        'team_code': 'UST-S1-MLBB'
    },
    {
        'first_name': 'Patrick',
        'last_name': 'Domingo',
        'username': 'patrickdomingo03',
        'team_code': 'UST-S1-MLBB'
    },
    {
        'first_name': 'Julian',
        'last_name': 'Bautista',
        'username': 'julianbautista04',
        'team_code': 'UST-S1-MLBB'
    },
    {
        'first_name': 'Miguel',
        'last_name': 'Agustin',
        'username': 'miguelagustin05',
        'team_code': 'UST-S1-MLBB'
    },
    {
        'first_name': 'Kevin',
        'last_name': 'Navarro',
        'username': 'kevinnavarro01',
        'team_code': 'FEU-S1-MLBB'
    },
    {
        'first_name': 'Evan',
        'last_name': 'Hernandez',
        'username': 'evanhernandez02',
        'team_code': 'FEU-S1-MLBB'
    },
    {
        'first_name': 'Ronald',
        'last_name': 'De Leon',
        'username': 'ronalddeleon03',
        'team_code': 'FEU-S1-MLBB'
    },
    {
        'first_name': 'Thomas',
        'last_name': 'Del Rosario',
        'username': 'thomasdelrosario04',
        'team_code': 'FEU-S1-MLBB'
    },
    {
        'first_name': 'Francis',
        'last_name': 'Lopez',
        'username': 'francislopez05',
        'team_code': 'FEU-S1-MLBB'
    },
    {
        'first_name': 'Jerome',
        'last_name': 'Castro',
        'username': 'jeromecastro01',
        'team_code': 'NU-S1-MLBB'
    },
    {
        'first_name': 'Isaac',
        'last_name': 'Rivera',
        'username': 'isaacrivera02',
        'team_code': 'NU-S1-MLBB'
    },
    {
        'first_name': 'Nathan',
        'last_name': 'Perez',
        'username': 'nathanperez03',
        'team_code': 'NU-S1-MLBB'
    },
    {
        'first_name': 'Luis',
        'last_name': 'Villamor',
        'username': 'luisvillamor04',
        'team_code': 'NU-S1-MLBB'
    },
    {
        'first_name': 'Jacob',
        'last_name': 'Alvarez',
        'username': 'jacobalvarez05',
        'team_code': 'NU-S1-MLBB'
    },
    {
        'first_name': 'Christian',
        'last_name': 'Fernandez',
        'username': 'christianfernandez01',
        'team_code': 'DLSU-S1-MLBB'
    },
    {
        'first_name': 'Oscar',
        'last_name': 'Delgado',
        'username': 'oscardelgado02',
        'team_code': 'DLSU-S1-MLBB'
    },
    {
        'first_name': 'Bryan',
        'last_name': 'Francisco',
        'username': 'bryanfrancisco03',
        'team_code': 'DLSU-S1-MLBB'
    },
    {
        'first_name': 'Ethan',
        'last_name': 'Cruz',
        'username': 'ethancruz04',
        'team_code': 'DLSU-S1-MLBB'
    },
    {
        'first_name': 'Lawrence',
        'last_name': 'Ortega',
        'username': 'lawrenceortega05',
        'team_code': 'DLSU-S1-MLBB'
    },
    {
        'first_name': 'Sebastian',
        'last_name': 'Monteverde',
        'username': 'sebastianmonteverde01',
        'team_code': 'ADU-S1-MLBB'
    },
    {
        'first_name': 'Raymond',
        'last_name': 'Soriano',
        'username': 'raymondsoriano02',
        'team_code': 'ADU-S1-MLBB'
    },
    {
        'first_name': 'Jeffrey',
        'last_name': 'Uy',
        'username': 'jeffreyuy03',
        'team_code': 'ADU-S1-MLBB'
    },
    {
        'first_name': 'Kyle',
        'last_name': 'Estrada',
        'username': 'kyleestrada04',
        'team_code': 'ADU-S1-MLBB'
    },
    {
        'first_name': 'Samuel',
        'last_name': 'Lopez',
        'username': 'samuellopez05',
        'team_code': 'ADU-S1-MLBB'
    },
    {
        'first_name': 'Aaron',
        'last_name': 'Cabrera',
        'username': 'aaroncabrera01',
        'team_code': 'ADMU-S1-MLBB'
    },
    {
        'first_name': 'Bryce',
        'last_name': 'Aguilar',
        'username': 'bryceaguilar02',
        'team_code': 'ADMU-S1-MLBB'
    },
    {
        'first_name': 'David',
        'last_name': 'Ramos',
        'username': 'davidramos03',
        'team_code': 'ADMU-S1-MLBB'
    },
    {
        'first_name': 'Paul',
        'last_name': 'Vargas',
        'username': 'paulvargas04',
        'team_code': 'ADMU-S1-MLBB'
    },
    {
        'first_name': 'Eugene',
        'last_name': 'Francisco',
        'username': 'eugenefrancisco05',
        'team_code': 'ADMU-S1-MLBB'
    },
    {
        'first_name': 'Lance',
        'last_name': 'De Guzman',
        'username': 'lancedeguzman01',
        'team_code': 'UP-S1-MLBB'
    },
    {
        'first_name': 'Justin',
        'last_name': 'Torres',
        'username': 'justintorres02',
        'team_code': 'UP-S1-MLBB'
    },
    {
        'first_name': 'Harold',
        'last_name': 'Castillo',
        'username': 'haroldcastillo03',
        'team_code': 'UP-S1-MLBB'
    },
    {
        'first_name': 'Evan',
        'last_name': 'Lozano',
        'username': 'evanlozano04',
        'team_code': 'UP-S1-MLBB'
    },
    {
        'first_name': 'Oscar',
        'last_name': 'Santos',
        'username': 'oscarsantos05',
        'team_code': 'UP-S1-MLBB'
    },
    {
        'first_name': 'Darren',
        'last_name': 'Flores',
        'username': 'darrenflores01',
        'team_code': 'UE-S1-NBA'
    },
    {
        'first_name': 'Randy',
        'last_name': 'Guzman',
        'username': 'randyguzman02',
        'team_code': 'UE-S1-NBA'
    },
    {
        'first_name': 'Victor',
        'last_name': 'Santiago',
        'username': 'victorsantiago03',
        'team_code': 'UE-S1-NBA'
    },
    {
        'first_name': 'Brian',
        'last_name': 'Navarro',
        'username': 'briannavarro01',
        'team_code': 'UST-S1-NBA'
    },
    {
        'first_name': 'Jeremy',
        'last_name': 'Castro',
        'username': 'jeremycastro02',
        'team_code': 'UST-S1-NBA'
    },
    {
        'first_name': 'Marcus',
        'last_name': 'Lopez',
        'username': 'marcuslopez03',
        'team_code': 'UST-S1-NBA'
    },
    {
        'first_name': 'Francis',
        'last_name': 'Aguilar',
        'username': 'francisaguilar01',
        'team_code': 'FEU-S1-NBA'
    },
    {
        'first_name': 'Jacob',
        'last_name': 'Reyes',
        'username': 'jacobreyes02',
        'team_code': 'FEU-S1-NBA'
    },
    {
        'first_name': 'Ethan',
        'last_name': 'Rivera',
        'username': 'ethanrivera03',
        'team_code': 'FEU-S1-NBA'
    },
    {
        'first_name': 'Lance',
        'last_name': 'Cortez',
        'username': 'lancecortez01',
        'team_code': 'NU-S1-NBA'
    },
    {
        'first_name': 'Bryce',
        'last_name': 'Fernandez',
        'username': 'brycefernandez02',
        'team_code': 'NU-S1-NBA'
    },
    {
        'first_name': 'Oscar',
        'last_name': 'Gutierrez',
        'username': 'oscargutierrez03',
        'team_code': 'NU-S1-NBA'
    },
    {
        'first_name': 'Christian',
        'last_name': 'Domingo',
        'username': 'christiandomingo01',
        'team_code': 'DLSU-S1-NBA'
    },
    {
        'first_name': 'Raymond',
        'last_name': 'Villanueva',
        'username': 'raymondvillanueva02',
        'team_code': 'DLSU-S1-NBA'
    },
    {
        'first_name': 'Justin',
        'last_name': 'Alvarez',
        'username': 'justinalvarez03',
        'team_code': 'DLSU-S1-NBA'
    },
    {
        'first_name': 'Aaron',
        'last_name': 'Del Rosario',
        'username': 'aarondelrosario01',
        'team_code': 'ADU-S1-NBA'
    },
    {
        'first_name': 'Nathaniel',
        'last_name': 'Hernandez',
        'username': 'nathanielhernandez02',
        'team_code': 'ADU-S1-NBA'
    },
    {
        'first_name': 'Paul',
        'last_name': 'Morales',
        'username': 'paulmorales03',
        'team_code': 'ADU-S1-NBA'
    },
    {
        'first_name': 'Sean',
        'last_name': 'Lopez',
        'username': 'seanlopez01',
        'team_code': 'ADMU-S1-NBA'
    },
    {
        'first_name': 'Kyle',
        'last_name': 'Martinez',
        'username': 'kylemartinez02',
        'team_code': 'ADMU-S1-NBA'
    },
    {
        'first_name': 'Lawrence',
        'last_name': 'Perez',
        'username': 'lawrenceperez03',
        'team_code': 'ADMU-S1-NBA'
    },
    {
        'first_name': 'Harold',
        'last_name': 'Soriano',
        'username': 'haroldsoriano01',
        'team_code': 'UP-S1-NBA'
    },
    {
        'first_name': 'Evan',
        'last_name': 'Flores',
        'username': 'evanflores02',
        'team_code': 'UP-S1-NBA'
    },
    {
        'first_name': 'Julian',
        'last_name': 'Ortega',
        'username': 'julianortega03',
        'team_code': 'UP-S1-NBA'
    }
]

matches = [
    {
        'tournament_code': 'S1-VALO',
        'start_date': datetime(2024, 1, 15, 0, 0),
        'end_date': datetime(2024, 1, 15, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'UE-S1-VALO',
        'team2': 'UST-S1-VALO'
    },
    {
        'tournament_code': 'S1-VALO',
        'start_date': datetime(2024, 1, 17, 0, 0),
        'end_date': datetime(2024, 1, 17, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'UE-S1-VALO',
        'team2': 'FEU-S1-VALO'
    },
    {
        'tournament_code': 'S1-VALO',
        'start_date': datetime(2024, 1, 19, 0, 0),
        'end_date': datetime(2024, 1, 19, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'UE-S1-VALO',
        'team2': 'NU-S1-VALO'
    },
    {
        'tournament_code': 'S1-VALO',
        'start_date': datetime(2024, 1, 21, 0, 0),
        'end_date': datetime(2024, 1, 21, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'UST-S1-VALO',
        'team2': 'FEU-S1-VALO'
    },
    {
        'tournament_code': 'S1-VALO',
        'start_date': datetime(2024, 1, 23, 0, 0),
        'end_date': datetime(2024, 1, 23, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'UST-S1-VALO',
        'team2': 'NU-S1-VALO'
    },
    {
        'tournament_code': 'S1-VALO',
        'start_date': datetime(2024, 1, 25, 0, 0),
        'end_date': datetime(2024, 1, 25, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'FEU-S1-VALO',
        'team2': 'NU-S1-VALO'
    },
    {
        'tournament_code': 'S1-VALO',
        'start_date': datetime(2024, 1, 27, 0, 0),
        'end_date': datetime(2024, 1, 27, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'DLSU-S1-VALO',
        'team2': 'ADU-S1-VALO'
    },
    {
        'tournament_code': 'S1-VALO',
        'start_date': datetime(2024, 1, 29, 0, 0),
        'end_date': datetime(2024, 1, 29, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'DLSU-S1-VALO',
        'team2': 'ADMU-S1-VALO'
    },
    {
        'tournament_code': 'S1-VALO',
        'start_date': datetime(2024, 1, 31, 0, 0),
        'end_date': datetime(2024, 1, 31, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'DLSU-S1-VALO',
        'team2': 'UP-S1-VALO'
    },
    {
        'tournament_code': 'S1-VALO',
        'start_date': datetime(2024, 2, 2, 0, 0),
        'end_date': datetime(2024, 2, 2, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'ADU-S1-VALO',
        'team2': 'ADMU-S1-VALO'
    },
    {
        'tournament_code': 'S1-VALO',
        'start_date': datetime(2024, 2, 4, 0, 0),
        'end_date': datetime(2024, 2, 4, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'ADU-S1-VALO',
        'team2': 'UP-S1-VALO'
    },
    {
        'tournament_code': 'S1-VALO',
        'start_date': datetime(2024, 2, 6, 0, 0),
        'end_date': datetime(2024, 2, 6, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'ADMU-S1-VALO',
        'team2': 'UP-S1-VALO'
    },
    {
        'tournament_code': 'S1-MLBB',
        'start_date': datetime(2024, 2, 16, 0, 0),
        'end_date': datetime(2024, 2, 16, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'UE-S1-MLBB',
        'team2': 'UST-S1-MLBB'
    },
    {
        'tournament_code': 'S1-MLBB',
        'start_date': datetime(2024, 2, 18, 0, 0),
        'end_date': datetime(2024, 2, 18, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'UE-S1-MLBB',
        'team2': 'FEU-S1-MLBB'
    },
    {
        'tournament_code': 'S1-MLBB',
        'start_date': datetime(2024, 2, 20, 0, 0),
        'end_date': datetime(2024, 2, 20, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'UE-S1-MLBB',
        'team2': 'NU-S1-MLBB'
    },
    {
        'tournament_code': 'S1-MLBB',
        'start_date': datetime(2024, 2, 22, 0, 0),
        'end_date': datetime(2024, 2, 22, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'UST-S1-MLBB',
        'team2': 'FEU-S1-MLBB'
    },
    {
        'tournament_code': 'S1-MLBB',
        'start_date': datetime(2024, 2, 24, 0, 0),
        'end_date': datetime(2024, 2, 24, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'UST-S1-MLBB',
        'team2': 'NU-S1-MLBB'
    },
    {
        'tournament_code': 'S1-MLBB',
        'start_date': datetime(2024, 2, 26, 0, 0),
        'end_date': datetime(2024, 2, 26, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'FEU-S1-MLBB',
        'team2': 'NU-S1-MLBB'
    },
    {
        'tournament_code': 'S1-MLBB',
        'start_date': datetime(2024, 2, 28, 0, 0),
        'end_date': datetime(2024, 2, 28, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'DLSU-S1-MLBB',
        'team2': 'ADU-S1-MLBB'
    },
    {
        'tournament_code': 'S1-MLBB',
        'start_date': datetime(2024, 3, 1, 0, 0),
        'end_date': datetime(2024, 3, 1, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'DLSU-S1-MLBB',
        'team2': 'ADMU-S1-MLBB'
    },
    {
        'tournament_code': 'S1-MLBB',
        'start_date': datetime(2024, 3, 3, 0, 0),
        'end_date': datetime(2024, 3, 3, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'DLSU-S1-MLBB',
        'team2': 'UP-S1-MLBB'
    },
    {
        'tournament_code': 'S1-MLBB',
        'start_date': datetime(2024, 3, 5, 0, 0),
        'end_date': datetime(2024, 3, 5, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'ADU-S1-MLBB',
        'team2': 'ADMU-S1-MLBB'
    },
    {
        'tournament_code': 'S1-MLBB',
        'start_date': datetime(2024, 3, 7, 0, 0),
        'end_date': datetime(2024, 3, 7, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'ADU-S1-MLBB',
        'team2': 'UP-S1-MLBB'
    },
    {
        'tournament_code': 'S1-MLBB',
        'start_date': datetime(2024, 3, 9, 0, 0),
        'end_date': datetime(2024, 3, 9, 2, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'ADMU-S1-MLBB',
        'team2': 'UP-S1-MLBB'
    },
    {
        'tournament_code': 'S1-NBA',
        'start_date': datetime(2024, 3, 11, 0, 0),
        'end_date': datetime(2024, 3, 11, 1, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'UE-S1-NBA',
        'team2': 'UST-S1-NBA'
    },
    {
        'tournament_code': 'S1-NBA',
        'start_date': datetime(2024, 3, 13, 0, 0),
        'end_date': datetime(2024, 3, 13, 1, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'UE-S1-NBA',
        'team2': 'FEU-S1-NBA'
    },
    {
        'tournament_code': 'S1-NBA',
        'start_date': datetime(2024, 3, 15, 0, 0),
        'end_date': datetime(2024, 3, 15, 1, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'UE-S1-NBA',
        'team2': 'NU-S1-NBA'
    },
    {
        'tournament_code': 'S1-NBA',
        'start_date': datetime(2024, 3, 17, 0, 0),
        'end_date': datetime(2024, 3, 17, 1, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'UST-S1-NBA',
        'team2': 'FEU-S1-NBA'
    },
    {
        'tournament_code': 'S1-NBA',
        'start_date': datetime(2024, 3, 19, 0, 0),
        'end_date': datetime(2024, 3, 19, 1, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'UST-S1-NBA',
        'team2': 'NU-S1-NBA'
    },
    {
        'tournament_code': 'S1-NBA',
        'start_date': datetime(2024, 3, 21, 0, 0),
        'end_date': datetime(2024, 3, 21, 1, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'FEU-S1-NBA',
        'team2': 'NU-S1-NBA'
    },
    {
        'tournament_code': 'S1-NBA',
        'start_date': datetime(2024, 3, 22, 0, 0),
        'end_date': datetime(2024, 3, 22, 1, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'DLSU-S1-NBA',
        'team2': 'ADU-S1-NBA'
    },
    {
        'tournament_code': 'S1-NBA',
        'start_date': datetime(2024, 3, 24, 0, 0),
        'end_date': datetime(2024, 3, 24, 1, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'DLSU-S1-NBA',
        'team2': 'ADMU-S1-NBA'
    },
    {
        'tournament_code': 'S1-NBA',
        'start_date': datetime(2024, 3, 26, 0, 0),
        'end_date': datetime(2024, 3, 26, 1, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'DLSU-S1-NBA',
        'team2': 'UP-S1-NBA'
    },
    {
        'tournament_code': 'S1-NBA',
        'start_date': datetime(2024, 3, 28, 0, 0),
        'end_date': datetime(2024, 3, 28, 1, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'ADU-S1-NBA',
        'team2': 'ADMU-S1-NBA'
    },
    {
        'tournament_code': 'S1-NBA',
        'start_date': datetime(2024, 3, 30, 0, 0),
        'end_date': datetime(2024, 3, 30, 1, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'ADU-S1-NBA',
        'team2': 'UP-S1-NBA'
    },
    {
        'tournament_code': 'S1-NBA',
        'start_date': datetime(2024, 4, 1, 0, 0),
        'end_date': datetime(2024, 4, 1, 1, 0),
        'match_type': 'Round Robin',
        'status': 'Scheduled',
        'team1': 'ADMU-S1-NBA',
        'team2': 'UP-S1-NBA'
    }
]
