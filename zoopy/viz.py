'''
=================================
This module is part of ZOOPY
https://github.com/droyti46/zoopy
=================================

It contains instruments for data vizualization

functions:
    plot_classification(...)
'''

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from zoopy import animal

def plot_classification(animal_for_plotting: animal.Animal) -> None:

    '''
    Plots a hierarchical classification graph
    
    Parameters:
        animal_for_plotting (zoopy.animal.Animal): an animal for plot classification
    '''

    classification = animal_for_plotting.classification
    fig, ax = plt.subplots(figsize=(8, 10))

    # Vertical positions for nodes
    node_height = 0.4
    node_width = 20
    # Space between nodes for arrows
    arrow_length = 0.2

    # Draw nodes and arrows
    for i, taxon_info in enumerate(classification.items()):
        taxon, name = taxon_info
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
        indent = 0.09
        ax.text(0, y + indent, taxon, ha='center', va='center', fontsize=10, fontfamily='sans-serif', weight='bold')
        ax.text(0, y - indent, name, ha='center', va='center', fontsize=10, fontfamily='sans-serif')

        # Draw arrow (if not the last node)
        if i < len(classification) - 1:
            next_y = -(i + 1) * (node_height + arrow_length) 
            ax.annotate('', xy=(0, next_y + node_height / 2), xytext=(0, y - node_height / 2),
                        arrowprops=dict(arrowstyle='->', lw=1.5, color='gray'))

    ax.set_xlim(-node_width, node_width)
    ax.set_ylim(-len(classification) * (node_height + arrow_length), 0.5)
    ax.axis('off')
    plt.title(f'{animal_for_plotting.name} Classification', fontsize=15, pad=15)
    plt.show()
    
def plot_geo(animal_for_plotting: animal.Animal) -> None:
    pass