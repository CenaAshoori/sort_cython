import matplotlib.pyplot as plt
import matplotlib.colors
from PIL import ImageColor
import matplotlib.pyplot as plt
import numpy as np


def save_plot(n, text, times):
    palett = """
#77D970
#FF0075
#172774
#EEEEEE
"""
    txt_1, txt_2, txt_3 = text
    t1, t2, t3 = times
    palett = list(map(lambda x: "#"+x.strip(), palett.split("#")[1:]))
    print(palett)

    n_labal = list(map(lambda x: str(x), n))
    n = np.array(n)
    min = n[1]-n[0] if len(n) > 1 else 1
    for i in range(0,len(n)-1):
        if n[i+1]-n[i] < min:
            min= n[i+1]-n[i]
    
    min -= 40

    for i in range(len(palett)):
        fig, ax = plt.subplots()
        color_a = palett[(i+0) % len(palett)]
        color_b = palett[(i+1) % len(palett)]
        color_c = palett[(i+2) % len(palett)]
        color_d = palett[(i+3) % len(palett)]

        r, g, b = ImageColor.getcolor(color_a, "RGB")
        print(r, g, b)
        yiq = ((r*299)+(g*587)+(b*114))/1000
        text_color = "black" if yiq >= 128 else "white"
        print(text_color)
        plt.rcParams['text.color'] = '#{:02x}{:02x}{:02x}'.format(
            ((255-r) % 255), ((255-g) % 255), ((255-b) % 255),)
        plt.rcParams['xtick.color'] = '#{:02x}{:02x}{:02x}'.format(
            ((255-r) % 255), ((255-g) % 255), ((255-b) % 255),)
        plt.rcParams['ytick.color'] = '#{:02x}{:02x}{:02x}'.format(
            ((255-r) % 255), ((255-g) % 255), ((255-b) % 255),)
        # plt.rcParams['board.color'] ='#{:02x}{:02x}{:02x}'.format(((255-r)%255), ((255-g)%255),((255-b)%255),)
        mokhalef = '#{:02x}{:02x}{:02x}'.format(
            ((255-r) % 255), ((255-g) % 255), ((255-b) % 255),)
        ax.spines["top"].set_color(mokhalef)
        ax.spines["right"].set_color(mokhalef)
        ax.spines["left"].set_color(mokhalef)
        ax.spines["bottom"].set_color(mokhalef)
        ax.spines["bottom"].set_linestyle("-")

        plt.rcParams['axes.labelcolor'] = mokhalef

        c      = ax.bar(n - min/3, t1, min/3,  label=txt_1, color=color_a)
        cython = ax.bar(n        , t2, min/3,   label=txt_2, color=color_b)
        python = ax.bar(n + min/3, t3, min/3,  
                        label=txt_3, color=color_c)

        ax.set_ylabel('Execution time(ms)')
        ax.set_xlabel('Input size')
        ax.set_title('Runtime by input size')
        ax.set_xticks(n, n_labal)

        ax.bar_label(c, padding=3)
        ax.bar_label(cython, padding=3)
        ax.bar_label(python, padding=3)
        ax.legend()

        plt.savefig("final/output"+f"_{i}", facecolor=color_d, bbox_inches="tight",
                    pad_inches=0.3, transparent=True)
        break
    plt.show()
