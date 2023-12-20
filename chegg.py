import matplotlib.pyplot as plt

# Define states and edges
states = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
edges = [(0, 1, 'a'), (1, 2, 'a'), (2, 3, 'a'), (3, 4, 'b'), (3, 6, 'b'),
         (4, 5, 'a'), (5, 6, 'b'), (6, 7, 'a'), (7, 8, 'b'), (7, 6, 'b'),
         (8, 9, 'a'), (9, 10, 'b'), (10, 11, 'a'), (11, -1, 'b')]

# Create plot
plt.figure(figsize=(8, 6))

# Draw nodes
for state in states:
    plt.plot(state, state, 'o', markersize=15, markerfacecolor='lightblue', markeredgewidth=2)
    plt.text(state + 0.1, state + 0.1, str(state), fontsize=12, ha='center')

# Draw edges
for start, end, label in edges:
    if start != -1:
        plt.plot([start, end], [start, end], 'b-', linewidth=2)
        plt.text((start + end) / 2, (start + end) / 2 + 0.1, label, fontsize=10, ha='center')

# Customize plot
plt.title('Graph for Second Pattern Matching Algorithm  a^2 * b^2 * (ab)^2')
plt.xlabel('State')
plt.ylabel('State')
plt.xlim(-0.5, 11.5)
plt.ylim(-0.5, 11.5)
plt.grid(True, linestyle='--', linewidth=0.5)

# Show plot
plt.tight_layout()
plt.show()