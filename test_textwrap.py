#coding:utf8
import this
import textwrap

text = this.s

print("\n")

"""
class TextWrapper
    width:  行宽度 默认 70
    initial_indent: 会被添加到第一行首的位置 默认 ""
    subsequent_indent: 会被添加到除了第一行的行首 默认 ""
    expend_tabs: 是否将table转换为空格 默认 true
    replace_whitespace: 是否转换所有空白字符位空格 此操作位于 expend_tabs 后 默认 true
    fix_sentence_endings: 是否强制保证句号后面是两个空格 默认 false
    break_long_words: 是否允许单词换行 不允许的话将可能存在长度超过width的行存在 默认 true
    break_on_hyphens: 处理连字符 ???
    drop_whitespace: 删除前后空格 默认true
"""

#wrap 返回列表
if 0:
    wrap_text = textwrap.wrap(text,
                    width=70,
                    initial_indent="    ",
                    subsequent_indent="",
                    fix_sentence_endings=True,
                    )
    print(wrap_text)


#fill 返回字符串
if 0:
    fill_text = textwrap.fill(text,
                    width=70,
                    initial_indent="    ",
                    subsequent_indent="111",
                    fix_sentence_endings=True,
                    )
    print(fill_text)

#dedent 返回字符串
if 1:
    # 去掉每一行前的空格 按句号换行
    dedent_text = textwrap.dedent(text)
    print(dedent_text)

