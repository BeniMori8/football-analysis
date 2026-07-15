import pandas as pd
import numpy as np

from app.config import config
from app.proccessor import process_matches


def generate_football_data():
    teams = ['Maccabi Tel Aviv', 'Haifa', 'Beitar', 'Hapoel', 'Ashdod', 'Netanya']
    stadiums = ['Bloomfield', 'Sammy Ofer', 'Teddy', 'Turner']
    match_data = {
        'match_id': range(1, config.number_of_matches +1),
        'home_team': np.random.choice(teams, config.number_of_matches),
        'away_team': np.random.choice(teams, config.number_of_matches),
        'home_score': np.random.randint(0, 5, config.number_of_matches),
        'away_score': np.random.randint(0, 5, config.number_of_matches),
        'yellow_cards': np.random.randint(0, 8, config.number_of_matches),
        'stadium': np.random.choice(stadiums, config.number_of_matches)
    }

    league_data = {
        'team': teams,
        'games_played': np.zeros(len(teams), dtype=int),
        'points': np.zeros(len(teams), dtype=int),
        'wins': np.zeros(len(teams), dtype=int),
        'ties': np.zeros(len(teams), dtype=int),
        'losses': np.zeros(len(teams), dtype=int),
        'goals': np.zeros(len(teams), dtype=int),
        'goals_against': np.zeros(len(teams), dtype=int),
    }

    df = pd.DataFrame(match_data)
    df_table = pd.DataFrame(league_data)

    # "נלכלך" קצת את הנתונים לצורך הראיון
    df.loc[0, 'home_score'] = -1  # שגיאה לוגית
    df.loc[1, 'stadium'] = None  # ערך חסר
    df.loc[2, 'yellow_cards'] = 50  # אנומליה
    df.loc[2, ['home_team', 'away_team']] = 'Maccabi Tel Aviv'


    df.to_csv('league_matches.csv', index=False)
    df_table = df_table.set_index('team')
    df_table.to_csv('league_matches_table.csv')


if __name__ == "__main__":
        generate_football_data()
        process_matches('league_matches.csv', 'league_matches_table.csv')