
from dataclasses import dataclass

@dataclass
class PipelineConfig:
    listings_path: str
    segments_path: str
    output_path: str
    report_path: str

PipelineConfig = PipelineConfig(
    listings_path= 'data/raw/listings_sample.csv', 
    segments_path= 'data/raw/neighbourhood_segments.csv',
    output_path= 'outputs',
    report_path= 'reports'
)
