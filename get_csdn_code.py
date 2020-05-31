import re

regex = r"([0-9])|(>(.*?)<)"
text=""
test_str=input()
matches = re.finditer(regex, test_str, re.MULTILINE)

#第一次匹配,去除html标签
for matchNum, match in enumerate(matches, start=1):
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        if groupNum==3 and type(match.group(groupNum)) is str:
            text+=match.group(groupNum)
        try:
            if groupNum==1:
                int(match.group(groupNum))
                text+='\n'
        except:
            pass

#第二次匹配,转换一些html的保留字
def re_html_label(match_h):
    if match_h.group('left_angle_bracket')=='&lt;':
        return "<"
    elif match_h.group('right_angle_bracket')=='&gt;':
        return '>'
    elif match_h.group('and')=='&amp;':
        return '&'
    else:
        pass
    
regex2 = r"(?P<left_angle_bracket>&lt;)|(?P<right_angle_bracket>&gt;)|(?P<and>&amp;)"
text=re.sub(regex2,re_html_label,text)

print(text)
