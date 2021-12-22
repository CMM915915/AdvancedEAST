import docx
import win32com.client as wc

# doc文件另存为docx
word = wc.Dispatch("Word.Application")
doc = word.Documents.Open(r"F:\\PycharmProjects\\test_conda\\2020-4-12.doc")
# 上面的地方只能使用完整绝对地址，相对地址找不到文件，且，只能用“\\”，不能用“/”，哪怕加了 r 也不行，涉及到将反斜杠看成转义字符。
doc.SaveAs(r"F:\\PycharmProjects\\test_conda\\2020-4-12.docx", 12, False, "", True, "", False, False, False,
           False)  # 转换后的文件,12代表转换后为docx文件
# doc.SaveAs(r"F:\\***\\***\\appendDoc\\***.docx", 12)#或直接简写
# 注意SaveAs会打开保存后的文件，有时可能看不到，但后台一定是打开的
doc.Close
word.Quit

path = "F:\\PycharmProjects\\test_conda\\2020-4-12.docx"
file = docx.Document(path)
for p in file.paragraphs:
    print(p.text)