import math

def calculate_min_cable(states, positions):
    """
    Calculates the minimum total length of cable to connect all OFF systems
    to the nearest ON system.

    Args:
        states (list[int]): A list representing the state of each system.
                              1 for ON, 0 for OFF.
        positions (list[int]): A list representing the position of each system.

    Returns:
        int: The minimum total cable length required.
    """
    n = len(states)
    if n == 0 or 1 not in states:
        # No systems or no ON systems to connect to
        return 0 
    
    # This list will store the distance to the nearest ON system for each system
    min_distances = [math.inf] * n

    # --- Pass 1: Left to Right ---
    # Find the distance to the nearest ON system on the left
    last_on_pos = -math.inf
    for i in range(n):
        if states[i] == 1:
            last_on_pos = positions[i]
        
        # Distance from the current system to the last seen ON system on the left
        if last_on_pos != -math.inf:
            min_distances[i] = positions[i] - last_on_pos

    # --- Pass 2: Right to Left ---
    # Find the distance to the nearest ON system on the right and update the minimum
    last_on_pos = math.inf
    total_cable_length = 0
    for i in range(n - 1, -1, -1):
        if states[i] == 1:
            last_on_pos = positions[i]
        
        # Distance from the current system to the last seen ON system on the right
        if last_on_pos != math.inf:
            # The actual minimum distance is the smaller of the distances
            # to the left ON system (calculated in pass 1) and the right ON system
            min_distances[i] = min(min_distances[i], last_on_pos - positions[i])

        # If the system is OFF, add its calculated minimum distance to the total
        if states[i] == 0:
            # Only add to total if a connection is possible (not infinity)
            if min_distances[i] != math.inf:
                total_cable_length += min_distances[i]

    return total_cable_length

# --- Example Usage ---
# Let's assume 0 = OFF and 1 = ON
system_states =   [0, 1, 0, 0, 1, 0]
system_positions = [5, 12, 20, 28, 40, 51]

# Calculate the minimum cable length
total_length = calculate_min_cable(system_states, system_positions)

print(f"System States: {system_states}")
print(f"System Positions: {system_positions}")
print(f"Minimum total cable length required: {total_length}") 
# Expected Output: (12-5) + (20-12) + (40-28) + (51-40) = 7 + 8 + 12 + 11 = 38
