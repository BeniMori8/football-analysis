import pandas as pd
from pydantic import ValidationError

from app.Models.match import Match
from app.config import config
from app.logger import logger


def process_matches(file_path):
    logger.info("Starting data processing...")
    try:
        df = pd.read_csv(file_path, chunksize=config.chunk_size)
        for index,chunk in enumerate(df):
            records = chunk.to_dict('records')
            for row in records:
                try:
                    # בדיקה של כל שורה
                    Match(match_id=row['match_id'], home_score=row['home_score'], home_team=row['home_team'], away_team=row['away_team'],
                          away_score=row['away_score'], yellow_cards=row['yellow_cards'], stadium=row['stadium'])

                    if row['yellow_cards'] > config.yellow_card_threshold:
                        logger.warning(f"High tension match detected!", extra={'match_id': row['match_id']})

                except (ValidationError, ValueError) as e:
                    logger.error(f"Validation failed: {str(e)}", extra={'match_id': row['match_id']})
            logger.info(f"Processed chunk {index+1}")
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")

