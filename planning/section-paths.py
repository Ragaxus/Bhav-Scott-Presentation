from math import pi, cos, sin
from string import Template

def get_point_along_circle(r, rad):
	return [r*cos(2*pi*rad), -r*sin(2*pi*rad)]

path_template = "<path d=\"M 0 0 {startx} {starty}  A {r} {r} 0 0 0  {endx} {endy} Z\" fill=\"url(#{fillurl})\"/>"

def print_segment(r, pct_start, pct_end, fillurl="off"):
	startx, starty = get_point_along_circle(r, pct_start)
	endx, endy = get_point_along_circle(r, pct_end) 
	return path_template.format(r=r, startx=startx, starty=starty, endx=endx, endy=endy, fillurl=fillurl)

topic_ids = [0, '1a', '1b', 2, 3, 4, 5, 6, 7, 8]
topics_to_color_gold = ['1a', '1b', 2, 3, 5, 8]
def determine_fill(topic_to_fill, active_topic_number):
	if (topic_ids.index(topic_to_fill) > topic_ids.index(active_topic_number)):
		return "off"
	if (topic_to_fill in topics_to_color_gold):
		return "golden-on"
	return "night-on"



if __name__ == "__main__":
	with open('progress-icon.svg.template', 'r') as svg_template_file:
		svg_template = Template(svg_template_file.read())

	r = 90
	phase = 1/8 + 1/16

	for topic in topic_ids: 

		paths = []
		paths.append(print_segment(r, phase, phase + 1/16, determine_fill('1a', topic)))
		paths.append(print_segment(r, phase + 1/16, phase + 1/8, determine_fill('1b', topic)))
		for i in reversed(range(1, 8)):
			paths.append(print_segment(r, phase + i/8, phase + (i+1)/8, determine_fill(topic_ids[i+2], topic)))
		result = svg_template.substitute({'paths': '\n'.join(paths)})

		with open(f'../images/progress-icons/progress-icon-{topic}.svg', 'w') as out_file:
			out_file.write(result)