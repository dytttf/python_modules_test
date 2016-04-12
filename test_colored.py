#coding:utf8
from colored import fg, bg, attr
from colored import fore, back, style
print '%s Hello World !!! %s' % (fg(1), attr(0))
print '%s%s Hello World !!! %s' %  (fg(1), bg(15), attr(0))

print ('%s%s Hello World !!! %s' % (fg('white'), bg('yellow'), attr('reset')))
print ('%s%s Hello World !!! %s' % (fg('orchid'), attr('bold'), attr('reset')))

color = fg('#c0c0c0') + bg('#00005f')
reset = attr('reset')
print color + 'Hello World' + reset
color = bg('indian_red_1a') + fg('white')
print color + 'Hello World' + reset

print fore.LIGHT_BLUE + back.RED + style.BOLD + 'Hello World' + style.RESET
