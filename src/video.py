import json
import os

from googleapiclient.discovery import build

API_KEY = os.getenv("API_KEY")
YOUTUBE = build('youtube', 'v3', developerKey=API_KEY)


class Video:

    def __init__(self, video_id):
        self.video_id = video_id

        data = self.get_data()
        self.title = data['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/watch?v={self.video_id}'
        self.view_count = int(data['items'][0]['statistics']['viewCount'])
        self.like_count = int(data['items'][0]['statistics']['likeCount'])

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.video_id}')"

    def get_data(self):
        '''
        Возвращает данные о видео в формате словаря
        :return: данные о канале
        '''
        data = YOUTUBE.videos().list(
            part='snippet,statistics,contentDetails,topicDetails',
            id=self.video_id
        ).execute()

        return data


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return f'{self.title}'
