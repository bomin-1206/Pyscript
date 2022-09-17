import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.naver.com/" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["#FFFF99", "#FF66cc"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "강보민")
write("description", "대소고 6기")
write("button", "저장")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "나이": "18세",
  "생일": "12.06",
  "좋아하는 캐릭터": "짱구",
  "좋아하는 과목": "수학"
}
information(informations)
