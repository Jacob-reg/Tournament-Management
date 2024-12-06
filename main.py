from utils import *
from createScripts import *
from readScripts import *
from updateScripts import *
from insertData import universities, seasons, tournaments, teams, players, matches


"""
IMPORTANT:
After the first execution, you **MUST COMMENT OUT** the following 
sections to avoid re-execution:

1. Setting unique indexes:
   - `setUniqueIndex()` should only be run once to set database constraints.

2. Creating records:
   - All `create_*` functions (e.g., `create_university`, `create_season`, 
   `create_tournament`, etc.) should only be run once to avoid duplicate 
   entries in the database.

3. Adding players to teams:
   - `add_teamPlayer()` should only be run once per player to prevent 
   duplicate roster entries.

4. Updating scores and match statuses:
   - Be cautious when running `update_scores()`. Re-executing them can 
   overwrite data or disrupt calculations.

To maintain data integrity, comment out these sections after the first 
successful execution. If complete re-execution is needed for debugging, 
ensure proper cleanup or database reset beforehand.
"""


setUniqueIndex()

# Insert Universities
for university in universities:
    create_university(
        university_name=university['name'],
        abbreviation=university['abbreviation']
    )

# Insert Seasons
for season in seasons:
    create_season(
        season_name=season['name'],
        start_date=season['start_date'],
        end_date=season['end_date'],
        status=season['status']
    )

# Insert Tournaments
for tournament in tournaments:
    create_tournament(
        season_code=tournament['season_code'],
        game=tournament['game'],
        tournament_name=tournament['name'],
        start_date=tournament['start_date'],
        end_date=tournament['end_date'],
        status=tournament['status']
    )

# Insert Teams
for team in teams:
    create_team(
        university_code=team['university_code'],
        season_code=team['season_code'],
        tournament_code=team['tournament_code'],
        game=team['game'],
        team_name=team['name'],
        coach_fn=team['coach']['first_name'],
        coach_ln=team['coach']['last_name']
    )

# Insert Players
for player in players:
    create_player(
        first_name=player['first_name'],
        last_name=player['last_name'],
        username=player['username'],
        team_code=player['team_code']
    )

# Insert Matches
for match in matches:
    create_match(
        tournament_code=match['tournament_code'],
        start_date=match['start_date'],
        end_date=match['end_date'],
        match_type=match['match_type'],
        status=match['status'],
        team1=match['team1'],
        team2=match['team2']
    )

# Update season schedule with adjusted startdate
update_seasonSchedule(
    season_code="S1",
    new_startDate=datetime(2024, 1, 17)
)

# Update tournament schedule with adjusted dates
update_tournamentSchedule(
    tournament_code="S1-VALO",
    new_startDate=datetime(2024, 1, 17),
    new_endDate=datetime(2024, 2, 17)
)

# Update each match schedule with adjusted dates
update_matchSchedule(
    match_code="S1-VALO-RR-UE-UST",
    new_startDate=datetime(2024, 1, 17),
    new_endDate=datetime(2024, 1, 17, 2)
)

update_matchSchedule(
    match_code="S1-VALO-RR-UE-FEU",
    new_startDate=datetime(2024, 1, 19),
    new_endDate=datetime(2024, 1, 19, 2)
)

update_matchSchedule(
    match_code="S1-VALO-RR-UE-NU",
    new_startDate=datetime(2024, 1, 21),
    new_endDate=datetime(2024, 1, 21, 2)
)

update_matchSchedule(
    match_code="S1-VALO-RR-ADU-ADMU",
    new_startDate=datetime(2024, 2, 4),
    new_endDate=datetime(2024, 2, 4, 2)
)

update_matchSchedule(
    match_code="S1-VALO-RR-ADU-UP",
    new_startDate=datetime(2024, 2, 8),
    new_endDate=datetime(2024, 2, 8, 2)
)

update_matchSchedule(
    match_code="S1-VALO-RR-ADMU-UP",
    new_startDate=datetime(2024, 2, 8),
    new_endDate=datetime(2024, 2, 8, 2)
)

# Update the season status
update_seasonStatus("S1", "Ongoing")

# Update the tournament status
update_tournamentStatus("S1-VALO", "Ongoing")

# Update match statuses
update_matchStatus("S1-VALO-RR-UE-UST", "Completed")
update_matchStatus("S1-VALO-RR-UE-FEU", "Completed")
update_matchStatus("S1-VALO-RR-UE-NU", "Completed")
update_matchStatus("S1-VALO-RR-UST-FEU", "Completed")
update_matchStatus("S1-VALO-RR-UST-NU", "Completed")
update_matchStatus("S1-VALO-RR-FEU-NU", "Completed")
update_matchStatus("S1-VALO-RR-DLSU-ADU", "Completed")
update_matchStatus("S1-VALO-RR-DLSU-ADMU", "Completed")
update_matchStatus("S1-VALO-RR-DLSU-UP", "Ongoing")

# Update match scores
update_scores("S1-VALO-RR-UE-UST", 2, 1)
update_scores("S1-VALO-RR-UE-FEU", 2, 0)
update_scores("S1-VALO-RR-UE-NU", 0, 2)
update_scores("S1-VALO-RR-UST-FEU", 1, 2)
update_scores("S1-VALO-RR-UST-NU", 2, 0)
update_scores("S1-VALO-RR-FEU-NU", 2, 1)
update_scores("S1-VALO-RR-DLSU-ADU", 0, 2)
update_scores("S1-VALO-RR-DLSU-ADMU", 2, 0)
update_scores("S1-VALO-RR-DLSU-UP", 1, 1)


# Simulates adding existing players to a team
# in a new season and tournament.

create_season(
    season_name="UAAP Esports Season 2",
    start_date=datetime(2024, 1, 15),
    end_date=datetime(2024, 4, 30),
    status="Upcoming"
)

create_tournament(
    season_code="S2",
    game="Valorant",
    tournament_name="UAAP Valorant Tournament Season 2",
    start_date=datetime(2025, 1, 15),
    end_date=datetime(2025, 2, 15),
    status="Upcoming"
)

create_team(
    university_code="ADMU",
    season_code="S2",
    tournament_code="S2-VALO",
    game="Valorant",
    team_name="Ateneo Blue Eagles",
    coach_fn="John",
    coach_ln="Doe"
)

add_teamPlayer("ADMU-S2-VALO", "nathaniel-delrosario-nathanieldelrosario31")
add_teamPlayer("ADMU-S2-VALO", "ethan-aguilar-ethanaguilar32")
add_teamPlayer("ADMU-S2-VALO", "christopher-bautista-christopherbautista33")
add_teamPlayer("ADMU-S2-VALO", "david-ramos-davidramos34")
add_teamPlayer("ADMU-S2-VALO", "paul-francisco-paulfrancisco35")

# View a document from each collection
view_university("ADMU")
view_season("S1")
view_tournament("S1-VALO")
view_team("ADMU-S1-VALO")
view_player("david-ramos-davidramos34")

# View matches in a tournament
view_matches("S1-VALO", team_code=None, status=None)
view_matches("S1-VALO", team_code=None, status="Completed")
view_matches("S1-VALO", team_code=None, status="Ongoing")
view_matches("S1-VALO", team_code=None, status="Scheduled")

# View matches of a team in a tournament
view_matches("S1-VALO", "DLSU-S1-VALO", status=None)
view_matches("S1-VALO", "DLSU-S1-VALO", status="Completed")
view_matches("S1-VALO", "DLSU-S1-VALO", status="Ongoing")
view_matches("S1-VALO", "UP-S1-VALO", status="Scheduled")

# View team standings in tournaments
tournamentLeaderboard("S1-VALO")
tournamentTopFour("S1-VALO")
tournamentWinner("S1-VALO")
seasonTournamentWinners("S1")
