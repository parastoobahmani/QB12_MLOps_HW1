PII = 'host_name', 'host_id'
req_output_cols = ['neighbourhood', 'num_listings', 'avg_price', 'median_price', 'avg_minimum_nights', 'availability_365_avg', 'total_reviews',
                   'reviews_per_listing', 'tourism_segment', 'priority_level']

def validate_summary(summary):
    if summary.empty:
        return "ValueError: output is empty"
    if not summary.columns.isin(req_output_cols).any():
        return "ValueError: req_output_cols columns do not exist"
    if PII in summary.columns or PII in listings.columns:
        return "ValueError: PII columns exist"
    if summary.neighbourhood.isna().any():
        return "ValueError: neighbourhood is null"
    if not summary.query("num_listings<=0").empty:
        return "ValueError: invalid num_listings"     
    if not summary.query("avg_price<0").empty:
        return "ValueError: invalid avg_price"
    if not summary.query("availability_365_avg < 0 or availability_365_avg> 365").empty:
        return "ValueError: invalid availability_365_avg"
    


validate_summary(summary)
