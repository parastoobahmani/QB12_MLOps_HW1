
def build_neighbourhood_summary(listings, segments):
    aggregated_data = listings.groupby(['neighbourhood'],as_index=False, group_keys=True, dropna=False).agg(
        num_listings=('listing_id', 'count'),
        avg_price=('price', 'mean'),
        median_price = ('price', 'median'),
        avg_minimum_nights = ('minimum_nights', 'mean'),
        availability_365_avg = ('availability_365', 'mean'),
        total_reviews = ('number_of_reviews', 'sum'),
        reviews_per_listing = ('number_of_reviews', 'count' ))

    return aggregated_data.join(segments.set_index("neighbourhood"), on='neighbourhood')

build_neighbourhood_summary(listings, segments)
