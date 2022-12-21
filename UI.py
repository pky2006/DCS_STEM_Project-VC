import tkinter as tk

window = tk.Tk()
window.geometry("1024x1080+100+100")
window.title("District Cooling System Q&A Game")
question_area=tk.Label(window, text="Distrcit Cooling System Q&A Game", font=("Arial Bold", 30))
question_area.grid(column=1080, row=720)

# window.geometry("10800x7200	")
# question_area=Label(window, text="Distrcit Cooling System Q&A Game", font=("Arial Bold", 30))
# question_area.grid(column=1080, row=720)
# yes=Button(window, text="Play",width=30)
# yes.grid(column=2080, row=800)
window.mainloop()

# window.state('zoomed')