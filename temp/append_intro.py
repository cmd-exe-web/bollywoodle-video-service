import subprocess
import os


def append_videos(
    input_video, intro_video=os.path.join(os.getcwd(), "./temp/intro.mp4")
):
    # Get the filename (without extension) of the input video
    output_video = os.path.splitext(os.path.basename(input_video))[0]

    # Create a temporary output file
    temp_output = f"{output_video}_temp.mp4"

    # Resize the input video to match the resolution of the intro video
    cmd_resize = [
        "ffmpeg",
        "-i",
        input_video,
        "-vf",
        "scale=1920:1080",
        "-c:a",
        "copy",
        "resized_input.mp4",
    ]
    subprocess.run(cmd_resize)

    # Execute ffmpeg command
    cmd_concat = [
        "ffmpeg",
        "-i",
        intro_video,
        "-i",
        "resized_input.mp4",
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
    subprocess.run(cmd_concat)

    # Remove resized input video
    os.remove("resized_input.mp4")

    # Remove original input video
    os.remove(input_video)

    # Rename the temp output file to the original input video name
    os.rename(temp_output, input_video)

    print(f"Videos have been appended. Output saved as '{input_video}'.")
