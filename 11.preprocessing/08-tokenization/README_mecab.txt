Windows Prebuilt MeCab Installation

Prerequisite
- python 2.7 or higher
- pip 2.7 or higher 

1. Windows 32bit�� mecab_x86 64bit �� mecab_x64�� 
   C:\mecab�� ������ Ǯ�� �����Ѵ�. 

2. mecab-python-module �������� python ������ windows����
�� �°� ��ġ�Ѵ�. 

https://github.com/Pusnow/mecab-ko-dic-msvc/releases/tag/mecab-ko-dic-2.1.1-20180720-msvc
���� �˸��� ������ whl�� �ٿ�޴´�

e.g. python version 3.7 windows 64bit �� ���
> pip install mecab_python-0.996_ko_0.9.2_msvc-cp37-cp37m-win_amd64.whl

��ġ Ȯ�ι��
>python
>>>import MeCab
>>>m = MeCab.Tagger('-d c:\mecab\mecab-ko-dic')
>>>ret = m.parse("�ƹ����� �濡 ���Ŵ�.")
.......
