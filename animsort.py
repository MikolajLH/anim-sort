import numpy as np
from argparse import ArgumentParser
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sort_generators
import sort_generators.shell_sort

ALGORITHMS = ['quick', 'insertion', 'merge', 'heap', 'selection', 'comb', 'shell', 'bubble']

def get_title_and_generator(name):
    match name:
        case 'quick':
            return "QuickSort", sort_generators.quick_sort
        case 'merge':
            return "MergeSort", sort_generators.merge_sort
        case "insertion":
            return "InsertionSort", sort_generators.insertion_sort
        case 'heap':
            return "HeapSort", sort_generators.heap_sort
        case 'selection':
            return "SelectionSort", sort_generators.selection_sort
        case 'comb':
            return "CombSort", sort_generators.comb_sort
        case 'shell':
            return "ShellSort", sort_generators.shell_sort
        case 'bubble':
            return "BubbleSort", sort_generators.bubble_sort
        
    raise ValueError("Not implemented")


def animate(N, sort_generator, title, bar_color, pivot_color,*, filename = None, bg_color = 'white', title_color='black'):
    fig, ax = plt.subplots()
    fig.patch.set_facecolor(bg_color)
    ax.set_title(title, fontsize=20, color=title_color, fontweight='bold')
    ax.axis('off')

    array = np.arange(1, N + 1)
    np.random.shuffle(array)

    bars = plt.bar(np.arange(1, N + 1), array, width=0.6)

    def update_bars(frame):
        pivot = frame
        #print(array)
        for i, (bar, el) in enumerate(zip(bars, array)):
            bar.set_color(pivot_color if i == pivot else bar_color)
            bar.set_height(el)
        return bars

    anim = animation.FuncAnimation(fig, update_bars, sort_generator(array, lambda x, y: x < y), repeat= False, interval= 10, cache_frame_data= False)
    if filename:
        writer = animation.PillowWriter(fps=15, bitrate=1800)
        anim.save(filename, writer=writer)
    else:
        plt.show()

if __name__ == "__main__":
    parser = ArgumentParser(
        prog="anim-sort",
        description="generates bar plot amiation of chosen sorting algorithm")
    
    
    parser.add_argument('-N', dest='N', default=50, type=int, metavar="<int>", help="number of elements to sort")
    parser.add_argument('-o', dest='filename', default='sorting_animation', type=str, metavar="<str>", help="name of file in which the result will be stored")
    parser.add_argument('-a', dest='algo', default='merge', choices=ALGORITHMS, metavar='<str>', help=f'which sorting algorithm to use: {ALGORITHMS}')

    parser.add_argument('-bc', dest='bar_color', default='blue', metavar='<color>', type=str, help='color of bars')
    parser.add_argument('-pc', dest='pivot_color', default='red', metavar='<color>', type=str, help='color of pivot')

    parser.add_argument('--bg-color', dest='bg_color', default='white', metavar='<color>', type=str, help='background color')
    parser.add_argument('--tt-c', dest='title_color', default='black', metavar='<color>', type=str, help='title text color')

    args = parser.parse_args()
    title, alg_gen = get_title_and_generator(args.algo)

    animate(args.N, alg_gen, title, args.bar_color, args.pivot_color, filename=f"{args.filename}.gif", bg_color=args.bg_color, title_color=args.title_color)