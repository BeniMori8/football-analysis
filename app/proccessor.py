import pandas as pd
from pydantic import ValidationError

from app.Models.match import Match
from app.config import config
from app.logger import logger


def proccess_match(league_table: pd.DataFrame, match: Match):
    league_table.loc[match.home_team, 'goals'] += match.home_score
    league_table.loc[match.away_team, 'goals'] += match.away_score
    league_table.loc[match.home_team, 'goals_against'] += match.away_score
    league_table.loc[match.away_team, 'goals_against'] += match.home_score
    league_table.loc[match.home_team, 'games_played'] += 1
    league_table.loc[match.away_team, 'games_played'] += 1
    is_tied = True if match.away_score == match.home_score else False
    if is_tied:
        league_table.loc[match.home_team,'points'] += 1
        league_table.loc[match.away_team, 'points'] += 1
        league_table.loc[match.home_team, 'ties'] += 1
        league_table.loc[match.away_team, 'ties'] += 1
    elif match.away_score < match.home_score:
        league_table.loc[match.home_team, 'points'] += 3
        league_table.loc[match.home_team, 'wins'] += 1
        league_table.loc[match.away_team, 'losses'] += 1
    else:
        league_table.loc[match.home_team, 'points'] += 3
        league_table.loc[match.home_team, 'wins'] += 1
        league_table.loc[match.away_team, 'losses'] += 1


def process_matches(file_path, file2_path):
    logger.info("Starting data processing...")
    try:
        df = pd.read_csv(file_path, chunksize=config.chunk_size)
        df_table = pd.read_csv(file2_path, index_col='team')

        for index,chunk in enumerate(df):
            records = chunk.to_dict('records')
            for row in records:
                try:
                    # בדיקה של כל שורה
                    match = Match(match_id=row['match_id'], home_score=row['home_score'], home_team=row['home_team'], away_team=row['away_team'],
                          away_score=row['away_score'], yellow_cards=row['yellow_cards'], stadium=row['stadium'])
                    proccess_match(df_table, match)
                    logger.info("Processing complete and saved.")
                    if row['yellow_cards'] > config.yellow_card_threshold:
                        logger.warning(f"High tension match detected!", extra={'match_id': row['match_id']})
                except (ValidationError, ValueError) as e:
                    logger.error(f"Validation failed: {str(e)}", extra={'match_id': row['match_id']})
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
    df_table.sort_values(by='points',ascending=False, inplace=True)
    df_table.to_csv(file2_path)


