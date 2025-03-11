import random
import time

import random
import time

class Player:
    def __init__(self, name, player_class, health=100, score=0):
        self.name = name
        self.health = health
        self.score = score
        self.player_class = player_class
        self.ability_used = False  # Track if the dodge ability is used (Circuit Rogue only)
        self.toughness_active = False  # Not needed anymore but keep it for reference

        if self.player_class == "Signal Cleric":
            self.heal_used = False  # Signal Cleric always heals
        if self.player_class == "Code Mage":
            self.arcane_knowledge_used = True  # Code Mage always has Arcane Knowledge active
        if self.player_class == "Mech Guardian":
            self.toughness_active = True  # Mech Guardian's toughness is always active.

    def heal(self):
        """Signal Cleric specific healing ability."""
        if self.player_class == "Signal Cleric":
            self.health += 2  # Heal 2 health per correct answer
            fast_print("\nYour faith in the system restores you! You heal 2 health.")

    def take_damage(self, amount):
        if self.player_class == "Circuit Rogue" and not self.ability_used:
            fast_print("\nYour evasive circuits engage! You nimbly dodge the attack.")
            self.ability_used = True
        else:
            if self.player_class == "Mech Guardian" and self.toughness_active:
                # Ensure the Mech Guardian always takes at least 5 damage after toughness
                amount = max(5, amount - 10)  # Reduce damage by 10, but no less than 5
                fast_print("\n*Mech Guardian Toughness* Your reinforced systems absorb some of the impact!")

            self.health -= amount
            if self.health <= 0:
                print("\nYou have fallen in the Dungeon of the Lost Circuit...")
                print("Contact your senior CSx/CSE before you attempt this adventure again.")
                input("Press Enter to exit the game...")
                return False  # Return False if player dies
        return True  # Player is still alive

    def add_score(self, points):
        """Method to add points to the player's score."""
        self.score += points
        fast_print(f"\nYour score has increased by {points}. Current score: {self.score}")

    def highlight_incorrect_answer(self, options, correct_index):
        """This method highlights an incorrect answer for Code Mage, always active."""
        if self.player_class == "Code Mage":
            incorrect_indices = [i for i in range(len(options)) if i != correct_index]
            chosen_incorrect_index = random.choice(incorrect_indices)
            fast_print(f"\n*ARCANE KNOWLEDGE* Your intuition tells you one false response is: {options[chosen_incorrect_index]}\n")
        return options

    def reset_dodge_ability(self):
        """Reset dodge ability at the start of each new dungeon level for Circuit Rogue."""
        if self.player_class == "Circuit Rogue":
            self.ability_used = False


def fast_print(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def display_status(player):
    print(f"\n{player.name} - Class: {player.player_class} | Health: {player.health} | Score: {player.score}")

def choose_class():
    classes = {
        "Circuit Rogue": "A nimble engineer with quick reflexes. Can evade one wrong answer per dungeon level.",
        "Mech Guardian": "A heavily armored specialist. Innate toughness allows them to partially shrug off damage.",
        "Code Mage": "A master of logic. 'Arcane Knowledge' gives an innate sense to reveal one incorrect answer.",
        "Signal Cleric": "A repair expert. Correctly answering questions bolsters their faith in the system, healing them.",
    }
    fast_print("\nChoose your class:")
    for i, (cls, desc) in enumerate(classes.items(), 1):
        fast_print(f"{i}. {cls} - {desc}")
    
    while True:
        choice = input("Enter the number of your chosen class: ")
        if choice.isdigit() and 1 <= int(choice) <= len(classes):
            # Return the class name (key), not the description (value)
            return list(classes.keys())[int(choice) - 1]
        fast_print("Invalid choice. Please enter a number between 1 and 4.")


# The rest of your code remains the same
# You can now instantiate the Mech Guardian and it will always take 5 less damage from incorrect answers, with a minimum of 5 damage.




# List of all possible monsters
monsters_pool = [
    ("Rustbound Automaton", "A creaking machine with exposed wires and flickering lights."),
    ("Glitching Wraith", "A ghostly figure, its form shifting between code and shadow."),
    ("Circuit Lurker", "An insect-like construct with sparking mandibles."),
    ("Data Phantom", "A swirling mass of corrupted binary code."),
    ("Firewall Sentinel", "A hovering drone with plasma shields."),
    ("Overclocked Reaper", "A skeletal bot with a scythe made of fragmented data."),
    ("Bitcrushed Horror", "A creature distorted beyond recognition, its pixels tearing apart reality."),
    ("Packet Gremlin", "A mischievous gremlin that steals data packets and scrambles logic."),
    ("Debugging Shade", "A shadowy entity that erases code—and minds—with a touch."),
    ("Malware Lich", "An ancient AI sorcerer, corrupted by an eternal virus."),
    ("Lagging Phantom", "A specter that flickers in and out of existence, causing reality delays."),
    ("Syntax Revenant", "A resurrected coder, doomed to wander after an unfinished program."),
    ("Corrupted Compiler", "A once-powerful AI, now mutating every system it encounters."),
    ("Quantum Poltergeist", "A being that exists in multiple states, changing its form at random."),
    ("Hexadecimal Harbinger", "A digital prophet, foretelling system failures."),
    ("Cyber Wyrm", "A serpentine construct made of intertwined cables and plasma energy."),
    ("Void Spider", "A many-legged machine that weaves firewalls instead of webs."),
    ("Doomed AI Construct", "An abandoned research project that now seeks revenge on its creators."),
    ("Glitched Titan", "A massive golem, its codebase riddled with fatal errors."),
    ("Wormhole Djinn", "A spectral entity that manipulates logic loops and infinite recursion."),
    ("C++ Chimera", "A monstrous fusion of old and new codebases, barely holding itself together."),
    ("Cache Stalker", "A silent predator that lurks within memory caches, striking from the shadows."),
    ("Binary Golem", "A construct of pure ones and zeroes, shifting its form unpredictably."),
    ("DDoS Colossus", "A hulking brute that overwhelms with sheer attack volume."),
    ("Kernel Specter", "A ghostly administrator of a forgotten operating system."),
    ("Trojan Revenant", "A disguised foe that only reveals its true form when it's too late."),
    ("RAM Wraith", "A floating entity that drains memory from anything it touches."),
    ("Stack Overflow Beast", "A chaotic, looping horror that repeats its actions endlessly."),
    ("Encrypted Djinn", "A being of pure cryptographic power, bound by complex algorithms."),
    ("AI Usurper", "A rogue intelligence that believes itself the rightful ruler of cyberspace."),
]

# List of all possible questions
questions_pool = [
    ("What is the primary purpose of a PID controller?", ["To regulate system output using proportional, integral, and derivative actions.", "To amplify signals in a control loop.", "To measure temperature in an industrial process.", "To convert analog signals to digital."], 0),
    ("Which of the following best describes a closed-loop control system?", ["A system that operates without feedback.", "A system that adjusts its output based on feedback.", "A system that only uses feedforward control.", "A system that cannot be controlled manually."], 1),
    ("What does the 'D' term in a PID controller primarily respond to?", ["The present error.", "The accumulation of past errors.", "The rate of change of the error.", "The setpoint value."], 2),
    ("In control systems, what does 'overshoot' refer to?", ["The delay in system response.", "The time it takes for a system to reach steady-state.", "The difference between process variable and setpoint.", "The maximum deviation from the setpoint before stabilization."], 3),
    ("Which of the following is an advantage of feedforward control?", ["It does not require process modeling.", "It eliminates the need for sensors.", "It can compensate for disturbances before they affect the system.", "It completely replaces feedback control."], 2),
    ("Which component of a control system is responsible for measuring system output?", ["Controller", "Actuator", "Sensor", "Process"], 2),
    ("What is the primary function of a PLC in industrial automation?", ["To provide power to actuators.", "To execute logic-based control programs.", "To manually override system operations.", "To convert signals from analog to digital."], 1),
    ("What is a Bode plot used for in control engineering?", ["To analyze system stability and frequency response.", "To measure signal strength in a circuit.", "To determine the temperature variations in a process.", "To program a PLC."], 0),
    ("What does the term 'dead time' refer to in a control system?", ["The period when a system is completely inactive.", "The steady-state error in a system.", "The frequency at which a system becomes unstable.", "The time delay between input change and observed output response."], 3),
    ("Which of the following transfer functions represents a first-order system?", ["G(s) = 1 / (s^2 + s + 1)", "G(s) = 1 / (s + 1)", "G(s) = s / (s + 1)", "G(s) = (s^2 + s) / (s + 1)"], 1),
    ("What is the main purpose of a root locus plot?", ["To determine system stability and gain variation effects.", "To measure real-time temperature changes in a process.", "To analyze binary logic gates.", "To visualize discrete signal behavior."], 0),
    ("Which type of control strategy best minimizes steady-state error?", ["Proportional control.", "Derivative control.", "Integral control.", "Feedforward control."], 2),
    ("What is the primary function of a notch filter in a control system?", ["To amplify high-frequency signals.", "To reduce signal noise in the feedback loop.", "To eliminate a specific frequency from the system response.", "To enhance phase margin in the system."], 2),
    ("What happens if the proportional gain in a PID controller is set too high?", ["The system may become unstable and oscillate.", "The system will have zero steady-state error.", "The system response will slow down significantly.", "The integral and derivative terms will have no effect."], 0),
    ("Which of the following is a characteristic of an overdamped system?", ["Fast response with overshoot.", "Slow response without overshoot.", "Oscillations before reaching steady-state.", "Unstable system behavior."], 1),
    ("In a frequency response analysis, what does the phase margin indicate?", ["The difference between input and output frequency.", "The additional phase shift required to make the system unstable.", "The delay in system response.", "The rate of change of the system gain."], 1),
    ("Which of the following is NOT an advantage of using a digital controller over an analog controller?", ["Higher resistance to noise.", "More precise control over real-world processes.", "Infinite resolution in signal processing.", "Easier implementation of complex control algorithms."], 2),
    ("Which control system is commonly used in robotics to control joint movement?", ["PID Control.", "Bang-Bang Control.", "Deadbeat Control.", "Open-Loop Control."], 0),
    ("What is gain scheduling in control systems?", ["Adjusting controller parameters based on operating conditions.", "Maintaining a fixed gain for stability.", "Increasing proportional gain in real-time.", "Using multiple controllers for redundancy."], 0),
    ("Which mathematical technique is often used for optimal control system design?", ["Laplace Transforms.", "Fourier Series.", "Linear Quadratic Regulator (LQR).", "Runge-Kutta Method."], 2),
    ("What is the purpose of state-space representation in control engineering?", ["To describe system dynamics using differential equations.", "To provide a graphical representation of root locations.", "To analyze only linear time-invariant systems.", "To replace the need for PID controllers."], 0),
    ("Which of these best describes an unstable system?", ["A system that settles to a steady-state value.", "A system that has no transient response.", "A system with zero steady-state error.", "A system where output grows indefinitely without bound."], 3),
    ("What is a common drawback of integral control?", ["It introduces steady-state error.", "It can cause system drift.", "It can lead to oscillations and instability if not tuned properly.", "It reduces system response time."], 2),
    ("What is the function of an observer in state-space control?", ["To estimate unmeasured system states.", "To reduce the impact of sensor noise.", "To increase system damping.", "To eliminate feedback control."], 0),
    ("Which of the following control methods is best suited for highly nonlinear systems?", ["PID control.", "Fuzzy logic control.", "Bang-bang control.", "Open-loop control."], 1),
    ("What is the main advantage of using a lead compensator?", ["It improves phase margin and transient response.", "It completely eliminates steady-state error.", "It reduces overshoot but slows down the system.", "It is only useful for open-loop systems."], 0),
    ("What is a Nyquist plot used for?", ["To compute the PID gains of a system.", "To determine system gain at different input levels.", "To visualize root locus locations.", "To analyze the stability of a control system in the frequency domain."], 3)
]



# Create copies of lists to track used monsters/questions
available_monsters = monsters_pool.copy()
available_questions = questions_pool.copy()

def get_random_monster():
    global available_monsters
    if not available_monsters:
        available_monsters = monsters_pool.copy()
        random.shuffle(available_monsters)  # Properly randomize
    return available_monsters.pop()

def get_random_question():
    global available_questions
    if not available_questions:
        available_questions = questions_pool.copy()
        random.shuffle(available_questions)
    return available_questions.pop()

def ask_question(player, question, options, correct_index):
    fast_print(question)
    options = player.highlight_incorrect_answer(options, correct_index)  # Highlight one incorrect answer for Code Mage
    
    for i, option in enumerate(options, 1):
        fast_print(f"{i}. {option}")
    
    while True:
        try:
            choice = int(input("\nEnter the number of your answer: \n"))
            if 1 <= choice <= len(options):
                if choice - 1 == correct_index:  # Check for correct answer
                    if player.player_class == "Signal Cleric":
                        player.heal()  # Trigger healing only for Signal Cleric when the answer is correct
                        fast_print("\n*Signal Cleric's Healing* Your faith in the system restores your health!")
                    return True
                else:
                    return False  # Incorrect answer, no healing applied
        except ValueError:
            pass
        fast_print("Invalid choice. Please enter a valid number.")


def encounter_monster(player, level):
    name, description = get_random_monster()
    question, options, correct_index = get_random_question()
    damage = level * 5

    fast_print(f"\nA {name} appears! {description}")
    display_status(player)

    # Pass player object to ask_question function
    if ask_question(player, question, options, correct_index):
        fast_print("\nThe monster dissipates in a puff of logic!")
        return True, 0  # True for success, no damage taken
    else:
        fast_print(f"\nThe {name} strikes! You take {damage} damage.")
        return False, damage


def dungeon_level(player, level):
    fast_print(f"\nDescending to level {level}...")

    # Reset dodge ability at the start of each new dungeon level for Circuit Rogue
    player.reset_dodge_ability()

    # Encounter between 3 to 5 monsters at each level
    for _ in range(random.randint(3, 5)):
        success, damage = encounter_monster(player, level)
        if success:
            player.add_score(10)
        else:
            if not player.take_damage(damage):
                return  # Stop if player dies

    # If it's not the final level, prompt to descend further
    if level < 5:
        input("Press Enter to descend further...")
        dungeon_level(player, level + 1)  # Recursively go to the next level
    else:
        fast_print("\nYou've reached the Core of Automation! Prepare for the final battle...")
        final_boss(player)  # Handle final boss when reaching level 5

def final_boss(player):
    fast_print("\nYou have reached the Core of Automation! The corrupted nano-virus looms before you.")
    fast_print("To purge the infection, you must answer five difficult questions. Answer three correctly to win.")

    correct_answers = 0
    total_questions = 5  # You will be asked 5 questions

    for _ in range(total_questions):
        question, options, correct_index = get_random_question()
        if ask_question(player, question, options, correct_index):
            fast_print("\nThe virus weakens!")
            correct_answers += 1
        else:
            fast_print("\nThe virus retaliates! You take 15 damage.")
            if not player.take_damage(15):
                fast_print("\nYou have perished before completing your mission...")
                return

        if correct_answers >= 3:  # Player wins if they answer 3 questions correctly
            fast_print("\nYou have restored the Core of Automation!")
            break

    # If the player didn't answer 3 questions correctly by the time the loop ends, they still survive.
    if correct_answers < 3:
        fast_print("\nThe infection remains... but you have survived to fight another day.")
    
    display_status(player)  # Display final score
    input("\nPress Enter to exit the game...")


def main():
    fast_print("Welcome to the Dungeon of the Lost Circuit!")
    name = input("Enter your name, adventurer: ")
    player_class = choose_class()
    player = Player(name, player_class)
    display_status(player)
    dungeon_level(player, 1)

if __name__ == "__main__":
    main()