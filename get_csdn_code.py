import re

regex = r"([0-9])|(>(.*?)<)"
text=""
test_str = "<ol class=\"hljs-ln\"><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"1\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\"><span class=\"hljs-function\"><span class=\"hljs-keyword\">int</span> <span class=\"hljs-title\">fun</span><span class=\"hljs-params\">(<span class=\"hljs-keyword\">float</span> *s, <span class=\"hljs-keyword\">int</span> n, <span class=\"hljs-keyword\">float</span> *aver)</span></span></div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"2\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">{</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"3\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">	    <span class=\"hljs-keyword\">float</span> sum = <span class=\"hljs-number\">0</span>,m;</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"4\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">		<span class=\"hljs-keyword\">int</span> count=<span class=\"hljs-number\">0</span>;</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"5\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">		</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"6\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">	<span class=\"hljs-keyword\">for</span> (<span class=\"hljs-keyword\">int</span> i = <span class=\"hljs-number\">0</span>; i &lt; n; i++)</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"7\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">	{</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"8\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">		sum += *(s + i);</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"9\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">	</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"10\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">	}</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"11\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">	*aver = sum / n;</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"12\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">	m = sum / n;</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"13\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">	<span class=\"hljs-keyword\">for</span> (<span class=\"hljs-keyword\">int</span> i = <span class=\"hljs-number\">0</span>; i &lt; n; i++)</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"14\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">	{</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"15\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">		<span class=\"hljs-keyword\">if</span> (*(s + i) &gt;= m)</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"16\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">		{</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"17\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">			count++;</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"18\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">		}</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"19\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">	}</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"20\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">	<span class=\"hljs-keyword\">return</span> count;</div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"21\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\"> </div></div></li><li><div class=\"hljs-ln-numbers\"><div class=\"hljs-ln-line hljs-ln-n\" data-line-number=\"22\"></div></div><div class=\"hljs-ln-code\"><div class=\"hljs-ln-line\">}</div></div></li></ol>"

matches = re.finditer(regex, test_str, re.MULTILINE)

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
print(text)
