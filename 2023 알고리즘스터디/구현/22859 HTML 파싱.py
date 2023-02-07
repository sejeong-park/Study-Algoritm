# 22859 HTML 파싱
import re
#origin = '<main><div title="title_name_1"><p>paragraph 1</p><p>paragraph 2 <i>Italic Tag</i> <br > </p><p>paragraph 3 <b>Bold Tag</b> end.</p></div><div title="title_name_2"><p>paragraph 4</p><p>paragraph 5 <i>Italic Tag 2</i> <br > end.</p></div></main>'
origin = input()
origin = origin.replace('<main>', '').replace('</main>', '').replace('><', '>\n<').replace('</div>','')
text_list = list(origin.split('\n'))
# print(text_list)
result = ''
for text in text_list:
	if text == '':
		continue
	if 'title' in text:
		text= 'title : ' + re.search('"(.+?)"', text).group(1)	# 정규식
	if '<p>' in text:
		cleaner = re.compile('<.*?>')
		text = re.sub(cleaner, '', text)
		text = text.replace('  ', ' ')	# 2개 연속으로 붙어 있는 경우
		text = text.strip()
	# result += text + '\n'
	print(text)




