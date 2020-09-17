#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#	 https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#!/usr/bin/python
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Yell the time every hour.
"""

import time
import anki_vector
import sys
from anki_vector.util import degrees
from anki_vector.events import Events
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, date

def make_text_image(text_to_draw, x, y, font=None):
	dimensions = (184, 96)
	text_image = Image.new('RGBA', dimensions, (0, 0, 0, 255))
	dc = ImageDraw.Draw(text_image)
	dc.text((x, y), text_to_draw, fill=(0, 255, 0, 255), font=font)
	return text_image

try:
	font_file = ImageFont.truetype("lcd.ttf", 75)
except IOError:
	try:
		font_file = ImageFont.truetype("arial.ttf", 27)
	except IOError:
		pass

import datetime
def main():
	args = anki_vector.util.parse_command_args()
	
	with anki_vector.Robot(args.serial) as robot:
		datetime.datetime.now().strftime(('%H:%M'))

		robot.anim.play_animation_trigger('GreetAfterLongTime')
		robot.audio.stream_wav_file("vector_bell_whistle.wav", 75)

		#prepare head for showing time
		robot.behavior.set_head_angle(degrees(30.0))
		robot.behavior.set_lift_height(0.0)

		#initialize time
		current_time = datetime.datetime.now().strftime(('%H:%M'))
		time_24hour = datetime.datetime.strptime(current_time, "%H:%M")
		time_12hour = time_24hour.strftime("%I:%M %p")

		#prepare time display
		face_sum = (str(time_12hour))
		text_to_draw = face_sum
		face_image = make_text_image(text_to_draw, 20, 5, font_file)

		print("Display time on Vector's face...")
		screen_data = anki_vector.screen.convert_image_to_screen_data(face_image)
		robot.screen.set_screen_with_image_data(screen_data, 10.0, interrupt_running=True)

		#tell the time
		print("Yell the current hour time")
		robot.behavior.say_text("The time is {}".format(str(time_12hour)))

		print("Sleep 5 seconds...")
		time.sleep(5)


if __name__ == '__main__':
	main()
