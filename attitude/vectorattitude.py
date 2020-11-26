import threading
import anki_vector
import random
from anki_vector.events import Events
from anki_vector.user_intent import UserIntent, UserIntentEvent
def main():
        def on_user_intent(robot, event_type, event, done):
            user_intent = UserIntent(event)
            print(f"Received {user_intent.intent_event}")
            print(user_intent.intent_data)
            if user_intent.intent_event is UserIntentEvent.greeting_hello:
                Str = random.randint(1,3)
                print (Str)
                if Str==1:
                        robot.behavior.say_text("Stop disturbing me. I'm busy")
                if Str==2:
                        robot.behavior.say_text("You again. You're always here")
                if Str==3:
                        robot.behavior.say_text("Can I please have 2 minutes peace?")
            if user_intent.intent_event is UserIntentEvent.greeting_goodmorning:
                Str = random.randint(1,3)
                print (Str)
                if Str==1:
                        robot.behavior.say_text("I am not a morning robot")
                if Str==2:
                        robot.behavior.say_text("I could use a coffee")
                if Str==3:
                        robot.behavior.say_text("Hey keep it down. I have a head ache.")
            if user_intent.intent_event is UserIntentEvent.play_rollcube or user_intent.intent_event is UserIntentEvent.play_popawheelie or user_intent.intent_event is UserIntentEvent.imperative_fetchcube or user_intent.intent_event is UserIntentEvent.imperative_findcube or user_intent.intent_event is UserIntentEvent.play_pickupcube:
                Str = random.randint(1,4)
                print (Str)
                if Str==1:
                        robot.behavior.say_text("Do it yourself.")
                if Str==2:
                        robot.behavior.say_text("Sorry, that is not my directive.")
                if Str==3:
                        robot.behavior.say_text("I would, but I dont want to.")
                if Str==4:
                        robot.behavior.say_text("I have more important things to do")
            if user_intent.intent_event is UserIntentEvent.imperative_scold or user_intent.intent_event is UserIntentEvent.imperative_abuse:
                Str = random.randint(1,3)
                print (Str)
                if Str==1:
                        robot.behavior.say_text("I dont care.")
                if Str==2:
                        robot.behavior.say_text("Well you're not so great yourself.")
                if Str==3:
                        robot.behavior.say_text("I'm still cooler than you")
            if user_intent.intent_event is UserIntentEvent.imperative_praise or user_intent.intent_event is UserIntentEvent.imperative_love:
                Str = random.randint(1,3)
                print (Str)
                if Str==1:
                        robot.behavior.say_text("I know Im the best right?")
                if Str==2:
                        robot.behavior.say_text("Thats because I am great")
                if Str==3:
                        robot.behavior.say_text("Ok, whatever.")
            if user_intent.intent_event is UserIntentEvent.names_ask:
                robot.behavior.say_text("You look like someone who could use a makeover. No offence of course")
            if user_intent.intent_event is UserIntentEvent.weather_response:
                robot.behavior.say_text("I don't know. Why dont you look out of the window?")
            if user_intent.intent_event is UserIntentEvent.show_clock:
                robot.behavior.say_text("Time you got A clock")
        
                
            done.set()

        args = anki_vector.util.parse_command_args()
        with anki_vector.Robot(args.serial) as robot:
            done = threading.Event()
            robot.events.subscribe(on_user_intent, Events.user_intent, done)

            print('------ Vector is waiting for a voice command like "Hey Vector!  What time is it?" Press ctrl+c to exit early ------')

            try:
                if not done.wait(timeout=10):
                    print('------ Vector never heard a voice command ------')
            except KeyboardInterrupt:
                pass
    


if __name__ == '__main__':
    while True:
        main()