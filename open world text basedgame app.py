# -*- coding: utf-8 -*-
"""
Jesse martin
Apr 20, 2025, 4:16 AM (1 day ago)
to me


   text game files.zip
To address the issues in the provided code and create a functional text-based game using the Gemini API, here's the corrected and improved version:

```python
import google.generativeai as genai
import os

# Set your Gemini API key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("Warning: GEMINI_API_KEY environment variable not set.")
    exit(1)

genai.configure(api_key=GEMINI_API_KEY)

# Configure models
generation_config = genai.types.GenerationConfig(
    temperature=0.7,
    max_output_tokens=1024
)

text_model = genai.GenerativeModel('gemini-pro', generation_config=generation_config)

def generate_text(prompt):
    try:
        response = text_model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating text: {e}")
        return None

def main():
    print("Welcome to the Time and Space Traveler Game!")
    current_scene = "You find yourself in a shimmering nexus point, where timelines converge and cosmic energies swirl. What do you do next?"
    
    while True:
        print(f"\n{current_scene}\n")
        
        prompt = f"Choose your action:\nA. Focus on a nearby swirling portal.\nB. Examine strange symbols etched on the floor.\nC. Activate a device in your hand.\nD. Try to communicate with the swirling energies.\nE. Observe the flow of timelines around you.\nF. Other (specify)"
        user_choice = input(prompt + "\nYour choice: ").strip().upper()

        if user_choice == 'F':
            user_input = input("Specify your action: ")
            action = user_input
        else:
            actions = {
                'A': "focus on a nearby swirling portal",
                'B': "examine strange symbols etched on the floor",
                'C': "activate a device in your hand",
                'D': "try to communicate with the swirling energies",
                'E': "observe the flow of timelines around you"
            }
            action = actions.get(user_choice, "stand still, observing the nexus")

        # Generate next scene
        next_scene_prompt = f"""In an open-world game about time travel and space exploration, the player is currently in a scene where: {current_scene}

The player chooses to {action}.

Describe what happens next in 2-3 sentences, incorporating elements of time travel, space exploration, or dimensional shifts. Include at the end either [CONTINUE] or [GAME OVER] based on the outcome."""

        generated_text = generate_text(next_scene_prompt)
        
        if not generated_text:
            print("Failed to generate scene. Restarting game...")
            current_scene = "You find yourself back at the shimmering nexus point."
            continue

        if "[GAME OVER]" in generated_text:
            print(generated_text.replace("[GAME OVER]", ""))
            print("\n--- GAME OVER ---")
            break
            
        current_scene = generated_text.replace("[CONTINUE]", "")

if __name__ == "__main__":
    main()
```

Key improvements made:

1. **Removed Image Generation**: Gemini Pro Vision doesn't support image generation, so removed that functionality.

2. **Fixed Indentation Issues**: Corrected the loop structure and indentation problems.

3. **Improved Game Over Handling**: Added explicit [CONTINUE]/[GAME OVER] markers in the prompt for better game state management.

4. **Enhanced Error Handling**: Added proper error handling for text generation failures.

5. **Simplified Workflow**: Removed unnecessary dependencies and streamlined the gameplay.

To run the corrected game:

1. Install required package:
```bash
pip install google-generativeai
```

2. Set your API key in environment variables:
```bash
export GEMINI_API_KEY="your-api-key-here"
```

3. Run the game:
```bash
python game.py
```

The game now features:
- Clear scene progression
- Better action handling
- Explicit game state control
- More robust error recovery
- Consistent narrative flow

The gameplay focuses on text-based interactions while maintaining the core time/space travel theme. The AI will generate creative story branches based on player choices while maintaining better control over game state transitions.