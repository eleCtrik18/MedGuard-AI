import random

# constants/instructions.py

EMERGENCY_INSTRUCTIONS = {
    "not breathing": [
        [
            "I’m here to help. Please lay them flat on their back on a firm surface. This is important.",
            "Next, tilt their head back gently to open the airway. Can you see if there's anything blocking it?",
            "If the airway is clear, start chest compressions. Push down hard in the center of the chest at a rate of 100-120 compressions per minute. You're doing great."
        ],
        [
            "Stay calm. First, make sure the person is lying on their back on something firm.",
            "Now, lift their chin slightly to open the airway. Check quickly if there's anything in their mouth that shouldn't be there.",
            "If everything looks clear, begin CPR right away. Push down on their chest at a steady rhythm. Help is on the way."
        ],
        [
            "It’s crucial to act quickly. Start by ensuring they are lying flat on their back.",
            "Gently lift their chin to open the airway. If the airway is clear, you need to start chest compressions immediately.",
            "Remember, push down hard and fast in the center of the chest. Keep going until help arrives."
        ],
        [
            "I’m with you. First, make sure they are on a flat surface. This will help you perform CPR effectively.",
            "Gently tilt their head back to open the airway. Check if there's anything in their throat or mouth.",
            "If the airway is clear, begin compressions. Push down hard and fast in the center of the chest, keeping a steady rhythm. You're doing great, help is on the way."
        ]
    ],
    "severe bleeding": [
        [
            "It’s important to stop the bleeding. Press down firmly on the wound with a clean cloth or bandage.",
            "Keep steady pressure on the wound. If the blood soaks through, add another cloth on top, but don’t remove the first one.",
            "Try to keep the injured area raised above the heart if possible. You're doing well."
        ],
        [
            "Stay calm and apply pressure to the wound immediately with a clean cloth.",
            "Don’t lift the cloth to check the wound—just keep pressing. If the cloth becomes soaked, add another one on top.",
            "If you can, elevate the injured area to help reduce blood flow."
        ],
        [
            "The first thing you need to do is press down on the wound with something clean. Do you have a cloth or bandage?",
            "Keep holding that pressure. If the bleeding doesn’t slow down, add another layer of cloth.",
            "Try to lift the injured area above heart level if you can. Help is on the way."
        ],
        [
            "Quickly apply pressure to the bleeding area with a clean cloth or bandage.",
            "Hold the pressure steady. If the blood soaks through, don’t remove the cloth—just add another on top.",
            "Raise the injured area above the level of the heart if possible. You're doing the right thing."
        ]
    ],
    # Add more emergency scenarios following the same structure
}
