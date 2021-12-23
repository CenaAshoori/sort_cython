import matplotlib.pyplot as plt
import matplotlib.colors 
from PIL import ImageColor
import matplotlib.pyplot as plt
import numpy as np

def save_plot(n,t1,t2 ):
    palett = """
#77D970
#FF0075
#172774
#EEEEEE
"""
    palett = list(map(lambda x:"#"+x.strip(),palett.split("#")[1:]))
    print(palett)
    # n = [2, 10, 100, 500, 1000]
    # t1 = [0, 1 , 2, 3 ,4]
    # t2 = [2, 4 , 5, 11 ,23]
    n = list(map(lambda x:str(x),n))


    width = .35      # the width of the bars: can also be len(x) sequence


    for i in range(len(palett)):
        fig, ax = plt.subplots()
        color_a = palett[(i+0)%len(palett)]
        color_b = palett[(i+1)%len(palett)]
        color_c = palett[(i+2)%len(palett)]
        color_d = palett[(i+3)%len(palett)]

        r,g,b = ImageColor.getcolor(color_a, "RGB")
        print (r,g,b)
        yiq = ((r*299)+(g*587)+(b*114))/1000
        text_color = "black" if yiq >= 128 else "white"
        print(text_color)
        plt.rcParams['text.color'] ='#{:02x}{:02x}{:02x}'.format(((255-r)%255), ((255-g)%255),((255-b)%255),)
        plt.rcParams['xtick.color'] ='#{:02x}{:02x}{:02x}'.format(((255-r)%255), ((255-g)%255),((255-b)%255),)
        plt.rcParams['ytick.color'] ='#{:02x}{:02x}{:02x}'.format(((255-r)%255), ((255-g)%255),((255-b)%255),)
        # plt.rcParams['board.color'] ='#{:02x}{:02x}{:02x}'.format(((255-r)%255), ((255-g)%255),((255-b)%255),)
        mokhalef = '#{:02x}{:02x}{:02x}'.format(((255-r)%255), ((255-g)%255),((255-b)%255),)
        ax.spines["top"].set_color(mokhalef)
        ax.spines["right"].set_color(mokhalef)
        ax.spines["left"].set_color(mokhalef)
        ax.spines["bottom"].set_color(mokhalef)
        ax.spines["bottom"].set_linestyle("-")
        
        plt.rcParams['axes.labelcolor'] =mokhalef
        ax.bar(n, t1, width,  label='Cython',color=color_b)

        ax.bar(n, t2, width,  bottom=t1,
            label='Python',color=color_c)

        ax.set_ylabel('Execution Time')
        ax.set_xlabel('Input')
        ax.set_title('Runtime by input size')
        ax.legend()

        plt.savefig("final/output"+f"_{i}", facecolor=color_d, bbox_inches="tight",
                    pad_inches=0.3, transparent=True)
        break
    plt.show()