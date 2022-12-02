# 맞춤법 검사기 plus
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white)


맞춤법 검사기 plus는 네이버 맞춤법 검사기를 이용한 파이썬 기반의 한글 맞춤법 검사기입니다.

![스크린샷](img/img001.png)

<br><br>
## **※ 특징**
500자 이상의 문장도 검사 가능
<br><br>

## Pyinstaller를 이용한 직접 빌드
### **Requirements**
다음 명령어를 통해 필요한 라이브러리를 내려받습니다.
```
pip install - r requirements.txt
```

### **exe 빌드**
```
pyinstaller --noconsole --onefile --icon=icon.ico --name=Spell_Checker_plus_v1.0 spell_checker_plus.py
```

### **exe 파일 확인**
.\dist 경로 안에 Spell_Checker_plus_v1.0.exe 생성됨
