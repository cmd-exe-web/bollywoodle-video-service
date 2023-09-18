import subprocess
import os


def append_videos(input_video, intro_video="./temp/intro.mp4"):
    print(input_video)
    # Get the filename (without extension) of the input video
    output_video = os.path.splitext(os.path.basename(input_video))[0]

    # Create a temporary output file
    temp_output = f"{output_video}_temp.mp4"

    # Execute ffmpeg command
    cmd = [
        "ffmpeg",
        "-i",
        intro_video,
        "-i",
        input_video,
        "-filter_complex",
        "[0:v][1:v]concat=n=2:v=1:a=0[outv]",
        "-map",
        "[outv]",
        "-c:v",
        "libx264",
        "-crf",
        "18",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        temp_output,
    ]

    subprocess.run(cmd)

    # Remove original input video
    os.remove(input_video)

    # Rename the temp output file to the original input video name
    os.rename(temp_output, input_video)

    print(f"Videos have been appended. Output saved as '{input_video}'.")
