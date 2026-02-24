from tkinter import *

class StartGame:

    def __init__(self):

        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        intro_string = ("In each round you will be invited to choose a colour. your goal is"
                        "to beat the target score and win the round (and keep your points).")

        choose_string = "How many rounds do you want to play?"

        start_labels_list = [
            ["Colour Quest", ("Arial", 16, "bold"), None],
            [intro_string, ("Arial", 12), None],
            [choose_string, ("Arial", 12, "bold"), "#009900"]
        ]

        start_label_ref = []
        for count, item in enumerate(start_labels_list):
            make_label = Label(self.start_frame, text=item[0], font=item[1],
                               fg=item[2],
                               wraplength=350, justify="left", pady=10, padx=20)
            make_label.grid(row=count)

            start_label_ref.append(make_label)

        self.choose_label = start_label_ref[2]

        self.entry_area_frame = Frame(self.start_frame)
        self.entry_area_frame.grid(row=3)

        self.num_rounds_entry = Entry(self.entry_area_frame, font=("Arial", 20, "bold"),
                                      width=10)
        self.num_rounds_entry.grid(row=0, column=0, padx=10, pady=10)

        self.play_button = Button(self.start_frame, font=("Arial", 16, "bold"),
                                  fg="#FFFFFF", bg="#0057D8", text="Play", width=10,
                                  command=self.check_rounds)
        self.play_button.grid(row=4, column=0)

    def check_rounds(self):

        Play(5)
        root.withdraw()

class Play:

    def __init__(self, how_many):
        self.play_box = Toplevel()

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)

        body_font = ("Arial", 12)

        play_labels_list = [
            ["Round # of #", ("Arial", 16, "bold"), None, 0],
            ["Score to beat: #", body_font, "#FFF2CC", 1],
            ["Choose a colour below. Good luck. 🍀", body_font, "#D5E8D4", 2],
            ["You chose, result", body_font, "#D5E8D4", 4]
        ]

        play_labels_ref = []
        for item in play_labels_list:
            self.make_label = Label(self.game_frame, text=item[0], font=item[1],
                                    bg=item[2], wraplength=300, justify="left")
            self.make_label.grid(row=item[3], pady=10, padx=10)

            play_labels_ref.append(item)

        self.heading_label = play_labels_ref[0]
        self.target_label = play_labels_ref[1]
        self.results_label = play_labels_ref[3]

        self.colour_frame = Frame(self.game_frame)
        self.colour_frame.grid(row=3)

        for item in range(0, 4):
            self.colour_button = Button(self.colour_frame, font=("Arial", 12),
                                       text="Colour Name", width=15)
            self.colour_button.grid(row=item // 2,
                                    column=item % 2,
                                    padx=5, pady=5)

        self.hints_stats_frame = Frame(self.game_frame)
        self.hints_stats_frame.grid(row=6)

        control_button_list = [
            [self.game_frame, "Next Round", "#0057D8", "", 21, 5, None],
            [self.hints_stats_frame, "Hints", "#FF8000", "", 10, 0, 0],
            [self.hints_stats_frame, "Stats", "#333333", "", 10, 0, 1],
            [self.game_frame, "End", "#990000", self.close_play, 21, 7, None]
        ]

        control_ref_list = []
        for item in control_button_list:
            make_control_button = Button(item[0], text=item[1], bg=item[2],
                                         command=item[3], font=("Arial", 16, "bold"),
                                         fg="#FFFFFF", width=item[4])
            make_control_button.grid(row=item[5], column=item[6], padx=5, pady=5)

            control_ref_list.append(make_control_button)

    def close_play(self):

        root.deiconify()
        self.play_box.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    StartGame()
    root.mainloop()