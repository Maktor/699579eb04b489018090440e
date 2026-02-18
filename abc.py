import matplotlib.pyplot as plt

def draw_tic_tac_toe():
    fig, ax = plt.subplots(figsize=(6, 6))
    
    fig.patch.set_facecolor('#fdf6e3')
    ax.set_facecolor('#fdf6e3')

    ax.plot([0.5, 3.5], [1.5, 1.5], color='black', lw=4, solid_capstyle='round')
    ax.plot([0.5, 3.5], [2.5, 2.5], color='black', lw=4, solid_capstyle='round')
    ax.plot([1.5, 1.5], [0.5, 3.5], color='black', lw=4, solid_capstyle='round')
    ax.plot([2.5, 2.5], [0.5, 3.5], color='black', lw=4, solid_capstyle='round')

    ax.text(2, 2, 'X', size=50, ha='center', va='center', color='#e74c3c', weight='bold')
    ax.text(3, 2, 'O', size=50, ha='center', va='center', color='#3498db', weight='bold')

    ax.set_xticks([1, 2, 3])
    ax.set_yticks([1, 2, 3])
    ax.set_xticklabels(['A', 'B', 'C'], fontsize=14, fontweight='bold')
    ax.set_yticklabels(['1', '2', '3'], fontsize=14, fontweight='bold')

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_xlim(0.5, 3.5)
    ax.set_ylim(0.5, 3.5)
    ax.invert_yaxis() 
    ax.tick_params(axis='both', which='both', length=0) 

    plt.tight_layout()
    plt.show()

draw_tic_tac_toe()
