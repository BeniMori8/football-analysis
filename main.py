import pandas as pd
import numpy as np

from app.proccessor import process_matches


def generate_football_data():
    teams = ['Maccabi Tel Aviv', 'Haifa', 'Beitar', 'Hapoel', 'Ashdod', 'Netanya']
    stadiums = ['Bloomfield', 'Sammy Ofer', 'Teddy', 'Turner']
    data = {
        'match_id': range(1, 1001),
        'home_team': np.random.choice(teams, 1000),
        'away_team': np.random.choice(teams, 1000),
        'home_score': np.random.randint(0, 5, 1000),
        'away_score': np.random.randint(0, 5, 1000),
        'yellow_cards': np.random.randint(0, 8, 1000),
        'stadium': np.random.choice(stadiums, 1000)
    }

    df = pd.DataFrame(data)

    # "נלכלך" קצת את הנתונים לצורך הראיון
    df.loc[0, 'home_score'] = -1  # שגיאה לוגית
    df.loc[1, 'stadium'] = None  # ערך חסר
    df.loc[2, 'yellow_cards'] = 50  # אנומליה
    df.loc[2, ['home_team', 'away_team']] = 'Maccabi Tel Aviv'


    df.to_csv('league_matches.csv', index=False)
    print("✅ הקובץ league_matches.csv נוצר בהצלחה!")


if __name__ == "__main__":
        generate_football_data()
        process_matches('league_matches.csv')