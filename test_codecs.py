# coding:utf8
import codecs


# help(codecs)
# print 1

def test_BOM():
    with open('bom_txt.txt', 'r') as f:
        s = f.read()
    print s.decode('utf8')
    if s[:3] == codecs.BOM_UTF8:
        print 1
    return
if __name__ == "__main__":
    test_BOM()
