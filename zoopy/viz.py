'''
=================================
This module is part of ZOOPY
https://github.com/droyti46/zoopy
=================================

It contains instruments for data vizualization
'''

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from zoopy import animal

def plot_classification(animal_for_plotting: animal.Animal) -> None:

    '''
    Plots a hierarchical classification graph with rectangular nodes and arrows.
    
    Args:
        classification (dict): A dictionary representing the classification hierarchy.
    '''

    classification = animal_for_plotting.classification
    fig, ax = plt.subplots(figsize=(8, 10))

    # Vertical positions for nodes
    node_height = 0.4
    node_width = 2.5
    arrow_length = 0.2  # Space between nodes for arrows

    # Draw nodes and arrows
    for i, name in enumerate(classification.values()):
        # Vertical position (top to bottom)
        y = -i * (node_height + arrow_length)
        # Draw rectangle
        rect = Rectangle(
            (-node_width / 2, y - node_height / 2),
            node_width,
            node_height,
            facecolor='lightblue',
            edgecolor='black',
            alpha=0.9
        )
        ax.add_patch(rect)

        # Add text
        ax.text(0, y, name, ha='center', va='center', fontsize=10, fontfamily='sans-serif')

        # Draw arrow (if not the last node)
        if i < len(classification) - 1:
            # Position of the next node
            next_y = -(i + 1) * (node_height + arrow_length) 
            ax.annotate('', xy=(0, next_y + node_height / 2), xytext=(0, y - node_height / 2),
                        arrowprops=dict(arrowstyle='->', lw=1.5, color='gray'))

    ax.set_xlim(-node_width, node_width)
    ax.set_ylim(-len(classification) * (node_height + arrow_length), 0.5)
    ax.axis('off')
    plt.title(f'{animal_for_plotting.name} Classification', fontsize=15, pad=15)
    plt.show()