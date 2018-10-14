import bisect
haystack = [1] + list(range(4,9)) + [12,15] + list(range(20,30,2))
needles = [0,1,2,5,8,10,22,23,29,30,31]
row_fmt='{0:2d}@{1:2d}  {2}{0:<2d}'

def demo(bisec_fn):
	   for needle in needles:
			   position = bisect_fn(haystack,needle)
			   offset = position * '  |'
			   print(row_fmt.format(needle,position,offset,needle))

import sys
if __name__=='__main__':
	if sys.argv[-1] == 'left':
		bisect_fn = bisect.bisect_left
	else:
		bisect_fn = bisect.bisect
	print('demo ',bisect_fn.__name__)
	print('     ',' '.join('%2d' % n for n in haystack))
	demo(bisect_fn)