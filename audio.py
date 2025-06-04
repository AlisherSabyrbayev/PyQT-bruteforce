from PyQt5 import QtMultimedia
from PyQt5.QtCore import QUrl


class AudioPlayer:
    def __init__(self):
        self.playlist = QtMultimedia.QMediaPlaylist()
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setPlaylist(self.playlist)

    def add_music(self, file_path):
        url = QUrl.fromLocalFile(file_path)
        self.playlist.addMedia(QtMultimedia.QMediaContent(url))

    def play(self):
        self.playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)
        self.player.play()

    def stop(self):
        self.player.stop()

    def set_volume(self, volume):
        self.player.setVolume(volume)

    def pause(self):
        self.player.pause()

    def is_paused(self):
        return self.player.state() == QtMultimedia.QMediaPlayer.PausedState