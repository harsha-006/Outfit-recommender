def color_psychology_recommender():
    """
    Recommends an outfit color and item based on the user's mood,
    using color psychology principles.
    """

    mood_to_color = {
        "happy": "Yellow",
        "energetic": "Red",
        "motivated": "Red",
        "sad": "Blue",
        "stressed": "Blue",
        "calm": "Blue",
        "relaxed": "Green",
        "peaceful": "Green",
        "angry": "Red",
        "professional": "Black",
        "serious": "Black",
        "caring": "Pink",
        "soft": "Pink",
        "optimistic": "Yellow",
        "cheerful": "Yellow",
        "balanced": "Green",
        "nature-inspired": "Green",
        "confident": "Red",
        "passionate": "Red",
        "formal": "Black",
        "nurturing": "Pink",
        "bright": "Yellow"
    }

    color_to_outfit_item = {
        "Red": ["red t-shirt", "red dress", "red sneakers", "red hat"],
        "Blue": ["blue jeans", "blue shirt", "blue sweater", "blue hat"],
        "Yellow": ["yellow sundress", "yellow t-shirt", "yellow hat", "yellow hat"],
        "Green": ["green jacket", "green cargo pants", "green shirt", "green backpack"],
        "Black": ["black suit", "black dress", "black trousers", "black jacket"],
        "Pink": ["pink blouse", "pink sweater", "pink skirt", "pink scarf"]
    }

    print("Welcome to the Color Psychology Outfit Recommender!")
    print("What's your mood today?")
    print("Some options: happy, sad, angry, stressed, relaxed, energetic, professional, caring, optimistic, calm, peaceful, confident, motivated, formal, nurturing, bright")

    while True:
        user_mood = input("\nEnter your mood (or 'quit' to exit): ").strip().lower()

        if user_mood == 'quit':
            print("Thank you for using the recommender.. Goodbye!")
            break

        if user_mood in mood_to_color:
            recommended_color = mood_to_color[user_mood]
            print(f"\nBased on your '{user_mood}' mood, we recommend wearing: {recommended_color}")

            if recommended_color in color_to_outfit_item:
                suggested_items = color_to_outfit_item[recommended_color]
                print(f"How about a {suggested_items[0]} or a {suggested_items[1]}?")
                print(f"Consider these options too: {', '.join(suggested_items[2:])}")
            else:
                print("We don't have specific outfit suggestions for this color yet, but you can explore items in this shade!")

        else:
            print("Sorry, I don't recognize that mood. Please try one of the suggested moods or similar terms.")
            print("Moods I know:", ', '.join(mood_to_color.keys()))

if __name__ == "__main__":
    color_psychology_recommender()