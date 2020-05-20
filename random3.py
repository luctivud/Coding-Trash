#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#   '          .       ,     神 | 光      .     '        .      , #
#     .      '        Udit Gupta @luctivud         ,              #
#  ,    '   ELDIOS | LIGHT | GREED | CIPHER | XAYN | KIRA '    .  #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
                ##     ##   ######   # #  ######
                ##     ##   ##  ##   ###    ##
                ##     ##   ##   #   # #    ##
                ###### ##   ######   # #    ##
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~| WORSHIPPER OF GREED |~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# import sys
# sys.setrecursionlimit(10**6)
def memoize(f):
    cache= {}
    def memf(key):
        if key not in cache:
            cache[key] = f(key)
        return cache[key]
    return memf

def get_interpretations(string):
	@memoize
	def get_branchs(string):
		if not string or len(string) == 1:
			return 0
		if string[0:2] <= '26':
			if '0' not in string[1:3]:
				return 1 + get_branchs(string[1:]) + get_branchs(string[2:])
			else:
				return get_branchs(string[2:])
		else:
			return get_branchs(string[1:])
	return 1 + get_branchs(string)
print(get_interpretations("220"))