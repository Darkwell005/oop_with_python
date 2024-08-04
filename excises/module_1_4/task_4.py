class MediaPlayer:

    def open(self, file: str) -> None:
        self.filename = file

    def play(self) -> None:
        print(f"Воспроизведение {self.filename}")


if __name__ == "__main__":
    mp = MediaPlayer()
    mp.open("videoOne.mp4")
    mp.play()
