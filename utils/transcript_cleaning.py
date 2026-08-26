

# Create function to convert the raw .vtt.srt transcript files to tabular formatuv --version
import webvtt
import pandas as pd
import pathlib
from pathlib import Path


def convert_subtitle_to_tabular(
        input_file_path: pathlib.Path,
        output_file_path: pathlib.Path,):
    """
    Converts a .vtt or .srt file to a pandas DataFrame and saves as a CSV file.
    input_file_path: pathlib Path to the .vtt or .srt file
    output_file_path: pathlib Path to the .csv file

    Example Usage:
    # convert_subtitle_to_tabular('sample_captions.srt')
    """
    captions_data = []

    # Determine file format and read accordingly
    if input_file_path.suffix == '.srt':
        # webvtt.from_srt() can read SRT files
        captions = webvtt.from_srt(input_file_path,)
    elif input_file_path.suffix == '.vtt':
        # webvtt.read() reads VTT files
        captions = webvtt.read(input_file_path)
    else:
        print(f"Unsupported file format for file: {input_file_path}")
        return

    for caption in captions:
        captions_data.append({
            'Start Time': caption.start,
            'End Time': caption.end,
            'Text': caption.text.strip()
        })

    # Create a pandas DataFrame
    df = pd.DataFrame(captions_data)

    # Define output file path
    output_path = Path(str(output_file_path) + ".csv")

    # Save to CSV
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"Successfully converted '{input_file_path}' to '{output_path}'")



