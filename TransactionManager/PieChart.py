from tkinter import *
from tkinter.ttk import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class PieChart(Frame):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.data = data
        self.create_chart()

    def create_chart(self):
        categories, amounts = zip(*self.data.items())

        # Create the pie chart
        fig, ax = plt.subplots()
        ax.pie(amounts, labels=categories, autopct='%1.1f%%')

        # Add the pie chart to the Tkinter frame
        chart = FigureCanvasTkAgg(fig, self)
        chart.get_tk_widget().pack()

        # Redraw the canvas
        chart.draw()