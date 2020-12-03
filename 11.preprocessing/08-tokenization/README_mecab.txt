Windows Prebuilt MeCab Installation

Prerequisite
- python 2.7 or higher
- pip 2.7 or higher 

1. Windows 32bit는 mecab_x86 64bit 는 mecab_x64를 
   C:\mecab에 압축을 풀어 복사한다. 

2. mecab-python-module 폴더에서 python 버전과 windows버전
에 맞게 설치한다. 

https://github.com/Pusnow/mecab-ko-dic-msvc/releases/tag/mecab-ko-dic-2.1.1-20180720-msvc
에서 알맞은 버전의 whl을 다운받는다

e.g. python version 3.7 windows 64bit 인 경우
> pip install mecab_python-0.996_ko_0.9.2_msvc-cp37-cp37m-win_amd64.whl

설치 확인방법
>python
>>>import MeCab
>>>m = MeCab.Tagger('-d c:\mecab\mecab-ko-dic')
>>>ret = m.parse("아버지가 방에 들어가신다.")
.......
