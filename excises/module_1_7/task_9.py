class Video:

    def __init__(self):
        self.name = None

    def create(self, name: str):
        self.name = name

    def play(self):
        print(f"Воспроизведение видео {self.name}")


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video: "Video"):
        cls.videos.append(video)
        print(cls.videos)

    @classmethod
    def play(cls, video_indx):
        pass  # Что делать дальше не понимаю


v1 = Video()
v2 = Video()
v1.create("Python")
v2.create("Python OOП")
YouTube.add_video(v1)
YouTube.add_video(v2)
