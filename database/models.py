from database import db

def store_daily_summary(summary):
    db.daily_summaries.insert_one(summary)

def get_daily_summaries():
    return list(db.daily_summaries.find())
