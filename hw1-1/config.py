from dataclasses import dataclass

@dataclass
class PipelineConfig:
    listings_path: str
    segments_path: str
    output_path: str
    report_path: str
    day: str

