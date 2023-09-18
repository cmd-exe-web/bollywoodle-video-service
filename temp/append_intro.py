from moviepy.editor import VideoFileClip, concatenate_videoclips
import os


def append_videos(input_video, intro_video="./temp/intro.mp4"):
    # Load videos
    intro_clip = VideoFileClip(intro_video)
    input_clip = VideoFileClip(input_video)

    # Resize the input clip to match the dimensions of the intro clip
    input_clip = input_clip.resize(newsize=(intro_clip.size))

    # Concatenate clips
    final_clip = concatenate_videoclips([intro_clip, input_clip])

    # Get the directory of the input video
    output_dir = os.path.dirname(input_video)

    # Get the filename (without extension) of the input video
    output_video = os.path.splitext(os.path.basename(input_video))[0] + "_combined.mp4"

    # Save the final clip to the same directory
    final_output_path = os.path.join(output_dir, output_video)
    final_clip.write_videofile(final_output_path, codec="libx264", audio_codec="aac")

    # Close clips
    intro_clip.close()
    input_clip.close()

    # Rename combined output file to input file name
    os.rename(final_output_path, input_video)

    # Delete the original input file
    # os.remove(input_video)

    print(f"Videos have been appended. Output saved as '{input_video}'.")


# # Usage example with relative paths
# input_video = "./temp/ea62d5d6-f89c-41b6-afaa-b5e599050115.mp4"
# intro_video = "./temp/intro.mp4"

# append_videos(input_video, intro_video)
