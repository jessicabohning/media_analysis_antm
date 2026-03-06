# Convert the raw, .vtt.srt transcript files to tabular format

from pathlib import Path
from utils.transcript_cleaning import convert_subtitle_to_tabular

# Define path to raw trasncript data
raw_transcript_path = Path("../transcripts/raw")
cleaned_transcript_path = Path("../transcripts/tabular_from_raw")

# Loop through all of the files in the transcripts/raw directory
season_directories = [x for x in raw_transcript_path.iterdir() if x.is_dir()]

# For each season, get a list of files in the corresponding dir and convert to tabular format
for dir in season_directories:
    # Get list of all files in the directory
    episode_file_paths = [x for x in dir.iterdir()]

    # Identify dir to save cleaned files to
    temp_file_dir = cleaned_transcript_path/dir.name

    # Create directory if it doesn't exist
    temp_file_dir.mkdir(parents=True, exist_ok=True)

    # For each episode file in each season directory, convert to tabular format
    for ep in episode_file_paths:
        # Keep the first 6 chars of the file name- to be used for where to save
        file_name = ep.name[0:6]
        convert_subtitle_to_tabular(
            input_file_path=ep,
            output_file_path=temp_file_dir/file_name
        )
