def brute(fmt, callback=None, symbols={}):
	
	inside_tag = False

	i = 0
	tags = []
	while i < len(fmt):
		if fmt[i] == '<':
			inside_tag = True
			ll = i
		elif fmt[i] == '>' and inside_tag:
			inside_tag = False
			ul = i + 1
			tag = fmt[ll+1:ul-1].strip()
			length = ul - ll
			tags.append({ 'tag': tag, 'll': ll, 'ul': ul, 'length': length })
		i += 1

	brute_loop(fmt, tags, symbols, callback)

def brute_loop(fmt, tags, symbols, callback, offset=0):

	is_last_tag = False
	if len(tags) == 1:
		is_last_tag = True

	first_tag = tags[0]

	tag_set = symbols[first_tag['tag']]
	left = fmt[:first_tag['ll'] + offset]
	right = fmt[first_tag['ul'] + offset:]

	for ch in tag_set:
		fmt_temp = left + ch + right
		if is_last_tag:
			callback(fmt_temp)
		else:
			brute_loop(fmt_temp, tags[1:], symbols, callback, offset+len(ch)-first_tag['length'])


