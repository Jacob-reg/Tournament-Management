from utils import *
from createScripts import *
# from readScripts import *
# from updateScripts import *
# from deleteScripts import *


# setUniqueIndex()

# create_university('Ateneo de Manila University', 'ADMU')
# create_university('University of the Philippines', 'UPD')
# create_university('De La Salle University', 'DLSU')


create_season(
    season_name="UAAP Esports Season 1",
    start_date=datetime(2024, 1, 1, 0, 0, 0),  # Start Date: January 1, 2024
    end_date=datetime(2024, 6, 30, 23, 59, 59),  # End Date: June 30, 2024
    status="upcoming"  # Season Status
)

# Valorant Tournament
create_tournament(
    season_code="S1",  # Season Code
    game="Valorant",
    tournament_name="UAAP Esports Season 1 Valorant Tournament",
    start_date=datetime(2024, 2, 15, 0, 0, 0),  # Start Date: February 15, 2024
    end_date=datetime(2024, 5, 15, 23, 59, 59),  # End Date: May 15, 2024
    status="upcoming"
)

# Valorant Teams
create_team(
    university_code="ADMU",
    season_code="S1",
    tournament_code="S1-VALO",
    game="Valorant",
    team_name="Ateneo Blue Eagles",
    coach_fn="Chris",
    coach_ln="Evans"
)

create_team(
    university_code="UPD",
    season_code="S1",
    tournament_code="S1-VALO",
    game="Valorant",
    team_name="UP Fighting Maroons",
    coach_fn="Emily",
    coach_ln="Blunt"
)

create_team(
    university_code="DLSU",
    season_code="S1",
    tournament_code="S1-VALO",
    game="Valorant",
    team_name="DLSU Green Archers",
    coach_fn="Robert",
    coach_ln="Downey"
)
