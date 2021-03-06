# lms_crawling

lms에서 자료들을 다운로드받을 목적으로 만든 프로젝트
현재는 내가 직접 html selector를 지정해주는 방식으로 구현
lms의 경우 강의에 따른 url의 변동이 없는 걸로 보아 post 방식으로 데이터를 주고받는 것 같은데, 나중에 이를 이용해서 좀 더 자동화 해봐야겠다.

### 프로젝트 구조
lms_crawling
- main.py
- my-config.json
- README.md


### main.py
프로그램 코드. 코드 양이 적어 한 파일로 작성함.

### my-config.json
프로그램 실행에 필요한 lms id, lms password, 강의명이 json형태로 저장되어 있음.