import cv2
import random
from pytube import YouTube


class VideoClipService:
    def __init__(self) -> None:
        pass

    def stream_youtube_video(self, url):
        try:
            yt = YouTube(url)
            video_stream = yt.streams.filter(adaptive=True).first().url
            return video_stream, yt.length
        except Exception as e:
            print("Error streaming the video:", e)
            return None, None

    def extract_random_frames(
        self, video_stream, num_frames, total_duration, excluded_start=0, excluded_end=0
    ):
        frames = []
        video_capture = cv2.VideoCapture(video_stream)

        # Get total frames in the video
        total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

        start_frame = excluded_start * total_frames // total_duration
        end_frame = (total_duration - excluded_end) * total_frames // total_duration

        for _ in range(num_frames):
            frame_number = random.randint(start_frame, end_frame)
            video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            ret, frame = video_capture.read()
            if ret:
                frames.append(frame)

        video_capture.release()
        return frames

    def save_frames_as_video(self, frames, save_path):
        height, width, _ = frames[0].shape
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(save_path, fourcc, 25, (width, height))

        for frame in frames:
            out.write(frame)

        out.release()

    def create_and_save_clip(self, youtube_url, save_video_path, num_frames_to_collect):
        video_stream, total_duration = self.stream_youtube_video(youtube_url)

        if video_stream and total_duration:
            frames = self.extract_random_frames(
                video_stream, num_frames_to_collect, total_duration
            )

            if frames:
                self.save_frames_as_video(frames, save_video_path)
                print(f"Random frames saved to {save_video_path}")
            else:
                print("Failed to extract frames from the video.")
        else:
            print("Error streaming the YouTube video.")
