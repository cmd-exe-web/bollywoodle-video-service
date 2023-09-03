import subprocess
import os


def encode_to_h264(input_file, input_path):
    # Specify the output file name with .mp4 extension
    output_file = os.path.splitext(input_file)[0] + "_h264.mp4"

    output_directory = (
        os.getcwd() + "/temp"
    )  # Replace with the desired output directory
    # Construct the full path to the output file
    output_path = os.path.join(output_directory, output_file)

    # Construct the ffmpeg command
    cmd = [
        "ffmpeg",
        "-i",
        input_path,  # Input file path
        "-c:v",
        "libx264",  # H.264 codec
        "-crf",
        "23",  # Constant Rate Factor (adjust for quality)
        "-preset",
        "medium",  # Encoding speed/quality preset
        "-c:a",
        "aac",  # AAC audio codec
        "-strict",
        "experimental",  # Necessary for AAC codec
        "-b:a",
        "192k",  # Audio bitrate
        output_path,  # Output Path. Same as input path
    ]

    try:
        subprocess.run(cmd, check=True)

        # Remove the original input file
        os.remove(input_path)
        # Rename the new encoded file to match the original file's name
        os.rename(output_path, input_path)

        print(f"Encoding successful. Output file: {input_path}")
    except subprocess.CalledProcessError:
        print("Error occurred during encoding.")


if __name__ == "__main__":
    input_file = "70e28bcc-393e-4843-8881-126f3465a973.mp4"
    input_path = "./temp/" + input_file
    encode_to_h264(input_file, input_path)
