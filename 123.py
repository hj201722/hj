import os
import google.auth
from googleapiclient.discovery import build

# API 키 설정
api_key = '~~'

# API 클라이언트 생성
youtube = build('youtube', 'v3', developerKey=api_key)

# 검색어 설정
queries = ['파이썬', 'python', 'Python','PYTHON', 'JAVA', '자바', 'java', 'Java','c언어','C언어','c 언어', 'C 언어', 'Clanguage', 'C language','html', 'HTML','리눅스', 'Linux', 'linux']

# 국가 코드
region_code = 'KR'

# 검색 결과 출력 파일 설정
output_file = 'output0.1.txt'

# 검색어마다 검색결과 크롤링하기
for query in queries:
    # API 호출하여 검색 결과 가져오기
    search_response = youtube.search().list(
        q=query,
        type='video',
        part='id,snippet',
        maxResults=10,
        regionCode=region_code  # 국가 코드 추가
    ).execute()

    # 검색 결과에서 필요한 정보 추출하기
    videos = []
    for search_result in search_response.get('items', []):
        video = {
            'title': search_result['snippet']['title'],
            'channel': search_result['snippet']['channelTitle'],
            'link': 'https://www.youtube.com/watch?v=' + search_result['id']['videoId']
        }
        videos.append(video)

    # 추출한 정보 출력하기
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write('Query: {}\n'.format(query))
        for video in videos:
            f.write(video['title'] + '\n')
            f.write(video['channel'] + '\n')
            f.write(video['link'] + '\n')
        f.write('\n')
