# iTunes Display

from appscript import app
import configparser

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')
c = config_ini["DEFAULT"]


class MusicControl(object):
    """
    AppleScriptを利用して、Musicアプリをコントロールするクラス
    注意：MacOSに依存する
    """
    def __init__(self):
        super().__init__()
        self.app = app(c["App"])
        self.app.run()

    def pause(self):
        """
        再生を一時停止する
        :return:
        """
        self.app.playpause()

    def play(self):
        """
        再生
        :return:
        """
        self.app.play()

    def stop(self):
        """
        停止
        :return:
        """
        self.app.stop()

    def next_track(self):
        """
        次の曲へ飛ぶ
        :return:
        """
        self.app.next_track()
    
    def prev_track(self):
        """
        前の曲へ飛ぶ
        :return:
        """
        self.app.previous_track()

    @property
    def sound_volume(self) -> int:
        """
        ボリュームを0〜100の範囲で返す
        :return: 
        """
        return self.app.sound_volume.get()

    @sound_volume.setter
    def sound_volume(self, volume: int):
        """
        ボリュームを0〜100の範囲で設定する
        :return: 
        """
        self.app.sound_volume.set(volume)
    
    # 曲名
    @property
    def name(self) -> str:
        return self.app.current_track.name.get()
    # アーティスト
    @property
    def artist(self) -> str:
        return self.app.current_track.artist.get()
    # アルバム
    @property
    def album(self) -> str:
        return self.app.current_track.album.get()
    # 年
    @property
    def year(self) -> str:
        return self.app.current_track.year.get()
    # 作曲者
    @property
    def composer(self) -> str:
        return self.app.current_track.composer.get()
    # ジャンル
    @property
    def genre(self) -> str:
        return self.app.current_track.genre.get()
    # コメント
    @property
    def comment(self) -> str:
        return self.app.current_track.comment.get()
    # プレイリスト
    @property
    def playlist(self) -> str:
        return self.app.current_playlist.name.get()
    
    # 読み方　タグへの書き込み
    # @property
    # def read(self) -> str:
    #     return self.app.current_track.tags.get()
