#!/usr/bin/env python3
# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import anki_vector
def main():
args = anki_vector.util.parse_command_args()
with anki_vector.Robot(args.serial) as robot:
print("Say 'Hello World'...")
robot.behavior.say_text("a long time ago in a galaxy far")
robot.behavior.say_text("far away")
if __name__ == "__main__":
main()
"""Display an image on Vector's face
"""
import os
import sys
import time
try:
from PIL import Image
except ImportError:
sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")
import anki_vector
from anki_vector.util import degrees
def main():
args = anki_vector.util.parse_command_args()
with anki_vector.Robot(args.serial) as robot:
# If necessary, move Vector's Head and Lift to make it easy to see his face
robot.behavior.set_head_angle(degrees(45.0))
robot.behavior.set_lift_height(0.0)
current_directory = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(current_directory, "..", "face_images", "star_wars.jpg")
# Load an image
image_file = Image.open(image_path)
# Convert the image to the format used by the Screen
print("Display image on Vector's face...")
screen_data = anki_vector.screen.convert_image_to_screen_data(image_file)
duration_s = 4.0
robot.screen.set_screen_with_image_data(screen_data, duration_s)
time.sleep(duration_s)
if __name__ == "__main__":
main()
"""starwars
Make Vector say 'Hello World' in this simple Vector SDK example program.
"""
import anki_vector
def main():
args = anki_vector.util.parse_command_args()
with anki_vector.Robot(args.serial) as robot:
print("Say 'Hello World'...")
robot.behavior.say_text("STAR WARS")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("episode 4")
robot.behavior.say_text("")
robot.behavior.say_text("a new hope")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("It is a period of civil war Rebel spaceships")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("striking from a hidden base")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("have won their first victory against the evil Galactic Empire")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("During the battle Rebel spies managed to steal secret plans to the Empire’s ultimate weapon")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("the death star")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("an armored space station with enough power to destroy an entire planet")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("Pursued by the Empire’s sinister agents Princess Leia races home aboard her starship")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("")
robot.behavior.say_text("custodian of the stolen plans that can save her people and restore freedom to the galaxy")
if __name__ == "__main__":
main()
"""Play audio files through Vector's speaker.
"""
import anki_vector
def main():
args = anki_vector.util.parse_command_args()
with anki_vector.Robot(args.serial) as robot:
# You can find these sounds files here:
# https://github.com/anki/vector-python-sdk/blob/master/examples/sounds/vector_alert.wav
# https://github.com/anki/vector-python-sdk/blob/master/examples/sounds/vector_bell_whistle.wav
#
# Paste these two wav files next to this tutorial to play sounds.
robot.audio.stream_wav_file("r2d2c.wav",75)
robot.audio.stream_wav_file("r2d2a.wav",75)
robot.audio.stream_wav_file("r2d2b.wav",75)
if __name__ == "__main__":
main()