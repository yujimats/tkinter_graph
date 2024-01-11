import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('matplotlib graph')

        # matplotlib配置用フレーム
        frame = tk.Frame(self.master)

        # matplotlibの描画領域の作成
        fig = Figure()
        self.ax = fig.add_subplot(1, 1, 1)
        # matplotlibの行場領域とウィジェットの関連付け
        self.fig_canvas = FigureCanvasTkAgg(fig, frame)
        # matplotlibのツールバーを作成
        self.toolbar = NavigationToolbar2Tk(self.fig_canvas, frame)
        # matploglibのグラフをフレームに配置
        self.fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # フレームをウィンドウに配置
        frame.pack()

        # ボタンの作成
        button = tk.Button(self.master, text='Draw Graph', command=self.button_click)
        # 配置
        button.pack(side=tk.BOTTOM)

    def button_click(self):
        with open('data.csv', 'r') as f:
            data = np.loadtxt(f, delimiter=',')
            x = data[:, 0]
            y = data[:, 1]
        self.ax.plot(x, y)
        self.fig_canvas.draw()

if __name__=='__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()