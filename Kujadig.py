import time

class MarsDiggingRobot:
    def __init__(self, name, max_depth):
        self.name = KujaDig  # Robot's name
        self.depth_dug = 0  # Current depth dug (in cm)
        self.max_depth = max_depth  # Maximum depth to dig (in cm)
        self.energy_level = 100  # Energy level in percentage

    def move_to_site(self):
        """Simulates the robot moving to the designated dig site."""
        print(f"{self.name} is moving to the dig site...")
        time.sleep(2)  # Simulating movement delay
        print("Arrived at the dig site.")

    def dig(self):
        """Simulates the digging process."""
        if self.energy_level <= 10:
            print("Warning: Low energy! Returning for recharge.")
            return False  # Stop digging if energy is too low

        print(f"{self.name} starts digging...")
        time.sleep(1)  # Simulating digging time
        self.depth_dug += 10  # Increment depth (10 cm per dig cycle)
        self.energy_level -= 5  # Decrease energy level
        print(f"Current depth: {self.depth_dug} cm")

        return True  # Continue digging

    def deposit_soil(self):
        """Simulates the process of depositing soil nearby."""
        print(f"{self.name} is depositing soil...")
        time.sleep(1)  # Simulating deposit time
        print("Soil deposited.")

    def execute_digging(self):
        """Manages the entire digging process."""
        self.move_to_site()

        while self.depth_dug < self.max_depth:
            if not self.dig():
                print("Pausing operations. Recharge required.")
                break  # Stop digging if energy is too low
            self.deposit_soil()  # Remove dug-out soil

        print(f"Digging complete! Final depth: {self.depth_dug} cm.")

# Create a Mars digging robot instance
mars_rover = MarsDiggingRobot(name="DigBot", max_depth=50)

# Start the digging process
mars_rover.execute_digging()
