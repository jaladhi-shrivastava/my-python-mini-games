mood_responses = {
    "happy": "That's awesome! Keep riding that good vibe and maybe share a smile with someone 😄",
    "sad": "Totally okay to feel low. Maybe take a walk, hug a pillow, or watch a comfort movie 🍫🎬",
    "anxious": "Deep breaths, one step at a time. You’re not alone — you’re just growing 💙",
    "angry": "Pause. Breathe. Maybe journal or punch a pillow (not a person 😅). You got this.",
    "overwhelmed": "Too much on the plate? Break it down. You only need to do one thing at a time 🧘",
    "excited": "Yay! Channel that energy into something fun or creative — ride the wave! 🚀",
    "okayish": "Meh days are totally valid. You're doing fine. Chill a bit or do something cozy ☕📖"
}

user_input=str(input("How's your day going? Tell me your mood! \n"))
if user_input in mood_responses:
    print(mood_responses.get(user_input))
else:
    print(mood_responses.get("Not sure??", "Take deep breath! Think again."))
