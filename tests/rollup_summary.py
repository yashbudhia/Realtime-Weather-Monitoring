from database.models import store_daily_summary, get_daily_summaries

def test_store_daily_summary():
    summary = {
        "date": "2024-10-21",
        "temperature": 28,
        "feels_like": 30,
        "condition": "Clear"
    }
    store_daily_summary(summary)
    summaries = get_daily_summaries()
    assert len(summaries) > 0
