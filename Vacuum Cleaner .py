class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment
        self.position = 0  # Vacuum cleaner's initial position
    def clean(self):
        dirty_cells = [i for i, cell in enumerate(self.environment) if cell == 'Dirty']

        while dirty_cells:
            current_cell = self.position
            if self.environment[current_cell] == 'Dirty':
                print(f"Cleaning cell {current_cell}")
                self.environment[current_cell] = 'Clean'
            next_cell = dirty_cells[0]
            if current_cell < next_cell:
                print("Moving right")
                self.position += 1
            elif current_cell > next_cell:
                print("Moving left")
                self.position -= 1
            dirty_cells = [i for i, cell in enumerate(self.environment) if cell == 'Dirty']
        print("All cells are clean.")
if __name__ == "__main__":
    environment = ['Dirty', 'Clean', 'Dirty', 'Clean', 'Clean']
    vacuum_cleaner = VacuumCleaner(environment)
    print("Initial state:")
    for i, cell in enumerate(environment):
        print(f"Cell {i}: {cell}")
    print("\nCleaning process:")
    vacuum_cleaner.clean()
