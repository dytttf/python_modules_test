# coding:utf8
import ConfigParser

TEST_CONF = '''[db]
host = 127.0.0.1
port = 3306
'''

with open('test.conf', 'w') as f:
    f.write(TEST_CONF)

CONFIG_FILES = [
    "test.conf",
    'not_exists.conf',
    ]


# __init__(defaults=None) 默认 defaults 是 collecions.OrderDict
config = ConfigParser.ConfigParser()

# read(filenames) 从文件加载配置
print config.read(CONFIG_FILES)

# readfp(fp, filename=None)
# print config.readfp(file(config_files[0]))

# 查看所有 section
sections = config.sections()
example_section = sections[0]
print 'sections', sections
print 'example_section', example_section

# 判断是否存在指定 section
print config.has_section('special_section')

# 判断是否存在指定 option
print config.has_option('special_section', 'special_option')

# 获取指定 section 中的 option
example_section_options = config.options(example_section)
example_option = example_section_options[0]

# get(section, option, raw=False, vars=None) 获取 option
s = '%s.%s=%s' % (
    example_section,
    example_option,
    config.get(example_section, example_option)
    )
print s

# getint(section, options) # 将获取到的值转换为整型
# getfloat(section, options) # 将获取到的值转换为浮点型
# getboolean(section, options) # 将获取到的值转换为布尔型

# items(section, raw=False, vars=None)
# return [(option, option_value), ]
print config.items(example_section)

# remove_option(section, option) 删除 option
# config.remove_option(example_section, example_option)

# remove_section(section) 删除 section
# config.remove_section(example_section)

# add_section(section)  增加 section
config.add_section("special_section")

# set(section, option, value)  修改或添加 option
config.set("special_section", "special_option", "special_value")

# write(fp) 从配置生成文件
with open('temp.conf', 'wb') as f:
    config.write(f)
