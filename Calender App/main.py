import tkinter as tk
from datetime import date
import calendar


# ==============================
# CONFIGURATION
# ==============================

BG = "#0b0f14"
CARD = "#111820"
CARD_2 = "#161f29"
TEXT = "#f2f5f7"
MUTED = "#8996a3"
ACCENT = "#00e5ff"
ACCENT_2 = "#00ff99"
HOVER = "#1e2b36"
TODAY_BG = "#00e5ff"
TODAY_TEXT = "#061016"


# ==============================
# MAIN WINDOW
# ==============================

window = tk.Tk()

window.title("Calendar by MusaWithPython")
window.geometry("600x650")
window.minsize(520, 600)
window.configure(bg=BG)


# ==============================
# ICON
# ==============================

try:
    icon = tk.PhotoImage(file="image.png")
    window.iconphoto(True, icon)
except:
    pass


# ==============================
# CALENDAR VARIABLES
# ==============================

today = date.today()

current_year = today.year
current_month = today.month


# ==============================
# HEADER
# ==============================

header = tk.Frame(window, bg=BG)
header.pack(fill="x", padx=30, pady=(25, 10))


title = tk.Label(
    header,
    text="CALENDAR",
    font=("Georgia", 24, "bold"),
    bg=BG,
    fg=TEXT
)
title.pack(anchor="w")


subtitle = tk.Label(
    header,
    text="MusaWithPython • Desktop Calendar",
    font=("Arial", 10),
    bg=BG,
    fg=ACCENT
)
subtitle.pack(anchor="w", pady=(2, 0))


# ==============================
# DATE DISPLAY
# ==============================

date_display = tk.Label(
    window,
    text="",
    font=("Arial", 11),
    bg=BG,
    fg=MUTED
)

date_display.pack(pady=(5, 15))


# ==============================
# CALENDAR CARD
# ==============================

calendar_card = tk.Frame(
    window,
    bg=CARD,
    highlightthickness=1,
    highlightbackground="#202b36"
)

calendar_card.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=5
)


# ==============================
# MONTH NAVIGATION
# ==============================

navigation = tk.Frame(calendar_card, bg=CARD)
navigation.pack(fill="x", padx=20, pady=(20, 10))


def button_hover(button, normal, hover):
    button.bind(
        "<Enter>",
        lambda event: button.config(bg=hover)
    )

    button.bind(
        "<Leave>",
        lambda event: button.config(bg=normal)
    )


def previous_month():
    global current_month, current_year

    current_month -= 1

    if current_month == 0:
        current_month = 12
        current_year -= 1

    draw_calendar()


def next_month():
    global current_month, current_year

    current_month += 1

    if current_month == 13:
        current_month = 1
        current_year += 1

    draw_calendar()


def go_today():
    global current_month, current_year

    current_month = today.month
    current_year = today.year

    draw_calendar()


previous_button = tk.Button(
    navigation,
    text="‹",
    font=("Arial", 22, "bold"),
    bg=CARD_2,
    fg=TEXT,
    activebackground=HOVER,
    activeforeground=ACCENT,
    bd=0,
    width=3,
    cursor="hand2",
    command=previous_month
)

previous_button.pack(side="left")

button_hover(previous_button, CARD_2, HOVER)


month_title = tk.Label(
    navigation,
    text="",
    font=("Arial", 18, "bold"),
    bg=CARD,
    fg=TEXT
)

month_title.pack(side="left", expand=True)


next_button = tk.Button(
    navigation,
    text="›",
    font=("Arial", 22, "bold"),
    bg=CARD_2,
    fg=TEXT,
    activebackground=HOVER,
    activeforeground=ACCENT,
    bd=0,
    width=3,
    cursor="hand2",
    command=next_month
)

next_button.pack(side="right")

button_hover(next_button, CARD_2, HOVER)


# ==============================
# TODAY BUTTON
# ==============================

today_button = tk.Button(
    calendar_card,
    text="TODAY",
    font=("Arial", 9, "bold"),
    bg=ACCENT,
    fg=TODAY_TEXT,
    activebackground=ACCENT_2,
    activeforeground=TODAY_TEXT,
    bd=0,
    padx=15,
    pady=6,
    cursor="hand2",
    command=go_today
)

today_button.pack(pady=(0, 15))

button_hover(today_button, ACCENT, ACCENT_2)


# ==============================
# CALENDAR FRAME
# ==============================

days_frame = tk.Frame(
    calendar_card,
    bg=CARD
)

days_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=5
)


# ==============================
# DRAW CALENDAR
# ==============================

def draw_calendar():

    # Clear old calendar
    for widget in days_frame.winfo_children():
        widget.destroy()

    # Month title
    month_name = calendar.month_name[current_month]

    month_title.config(
        text=f"{month_name} {current_year}"
    )

    # Date information
    if current_year == today.year and current_month == today.month:

        date_display.config(
            text=today.strftime("%A, %d %B %Y")
        )

    else:

        first_day = date(
            current_year,
            current_month,
            1
        )

        date_display.config(
            text=first_day.strftime("%B %Y")
        )

    # Make columns equal
    for column in range(7):
        days_frame.columnconfigure(
            column,
            weight=1
        )

    # Weekday headers
    weekdays = [
        "MON",
        "TUE",
        "WED",
        "THU",
        "FRI",
        "SAT",
        "SUN"
    ]

    for column, day_name in enumerate(weekdays):

        label = tk.Label(
            days_frame,
            text=day_name,
            font=("Arial", 9, "bold"),
            bg=CARD,
            fg=ACCENT if column < 5 else ACCENT_2
        )

        label.grid(
            row=0,
            column=column,
            sticky="nsew",
            pady=(5, 12)
        )

    # Get month data
    month_calendar = calendar.monthcalendar(
        current_year,
        current_month
    )

    # Create day buttons
    for row, week in enumerate(month_calendar, start=1):

        days_frame.rowconfigure(
            row,
            weight=1
        )

        for column, day in enumerate(week):

            if day == 0:
                continue

            is_today = (
                day == today.day
                and current_month == today.month
                and current_year == today.year
            )

            if is_today:

                bg = TODAY_BG
                fg = TODAY_TEXT

            else:

                bg = CARD_2
                fg = TEXT

            day_button = tk.Button(
                days_frame,
                text=str(day),
                font=("Arial", 11, "bold"),
                bg=bg,
                fg=fg,
                activebackground=ACCENT,
                activeforeground=TODAY_TEXT,
                bd=0,
                cursor="hand2",
                relief="flat"
            )

            day_button.grid(
                row=row,
                column=column,
                sticky="nsew",
                padx=4,
                pady=4
            )

            # Don't override today's colors
            if not is_today:

                day_button.bind(
                    "<Enter>",
                    lambda event, b=day_button:
                    b.config(
                        bg=HOVER,
                        fg=ACCENT
                    )
                )

                day_button.bind(
                    "<Leave>",
                    lambda event, b=day_button:
                    b.config(
                        bg=CARD_2,
                        fg=TEXT
                    )
                )


# ==============================
# FOOTER
# ==============================

footer = tk.Frame(
    window,
    bg=BG
)

footer.pack(
    fill="x",
    padx=30,
    pady=(10, 20)
)


footer_left = tk.Label(
    footer,
    text="‹ ›  Navigate",
    font=("Arial", 9),
    bg=BG,
    fg=MUTED
)

footer_left.pack(side="left")


footer_right = tk.Label(
    footer,
    text="MusaWithPython",
    font=("Arial", 9, "bold"),
    bg=BG,
    fg=ACCENT
)

footer_right.pack(side="right")


# ==============================
# KEYBOARD SHORTCUTS
# ==============================

window.bind(
    "<Left>",
    lambda event: previous_month()
)

window.bind(
    "<Right>",
    lambda event: next_month()
)

window.bind(
    "<Home>",
    lambda event: go_today()
)


# ==============================
# START
# ==============================

draw_calendar()

window.mainloop()