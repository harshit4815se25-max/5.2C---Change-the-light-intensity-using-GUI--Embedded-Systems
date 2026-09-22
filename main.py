import tkinter as tk
from gpiozero import LED, PWMLED


# GPIO setup

living_led = PWMLED(14)
bathroom_led = LED(15)
closet_led = LED(18)


# Living room button

def toggle_living():
    if living_led.is_lit:
        living_led.off()
        living_button.config(text="TURN ON", bg="#2e8b57")
    else:
        living_led.on()
        living_button.config(text="TURN OFF", bg="#b22222")


# Bathroom button

def toggle_bathroom():
    if bathroom_led.is_lit:
        bathroom_led.off()
        bathroom_button.config(text="TURN ON", bg="#2e8b57")
    else:
        bathroom_led.on()
        bathroom_button.config(text="TURN OFF", bg="#b22222")


# Closet button

def toggle_closet():
    if closet_led.is_lit:
        closet_led.off()
        closet_button.config(text="TURN ON", bg="#2e8b57")
    else:
        closet_led.on()
        closet_button.config(text="TURN OFF", bg="#b22222")


# Brightness control

def change_brightness(value):
    brightness = float(value) / 100
    living_led.value = brightness

    brightness_value.config(
        text=f"{int(float(value))}%"
    )

    if brightness > 0:
        living_button.config(
            text="TURN OFF",
            bg="#b22222"
        )
    else:
        living_button.config(
            text="TURN ON",
            bg="#2e8b57"
        )


# Control all lights

def all_on():
    living_led.on()
    bathroom_led.on()
    closet_led.on()

    living_button.config(text="TURN OFF", bg="#b22222")
    bathroom_button.config(text="TURN OFF", bg="#b22222")
    closet_button.config(text="TURN OFF", bg="#b22222")


def all_off():
    living_led.off()
    bathroom_led.off()
    closet_led.off()

    living_button.config(text="TURN ON", bg="#2e8b57")
    bathroom_button.config(text="TURN ON", bg="#2e8b57")
    closet_button.config(text="TURN ON", bg="#2e8b57")


# Close program

def close_program():
    all_off()
    window.destroy()


# Create window

window = tk.Tk()

window.title("Smart Home Lights")
window.geometry("520x650")
window.configure(bg="#101820")
window.resizable(False, False)


# Header

header = tk.Frame(
    window,
    bg="#101820"
)

header.pack(fill="x", pady=(25, 10))


title = tk.Label(
    header,
    text="SMART HOME",
    font=("Arial", 26, "bold"),
    fg="white",
    bg="#101820"
)

title.pack()


subtitle = tk.Label(
    header,
    text="Raspberry Pi Lighting Control",
    font=("Arial", 12),
    fg="#aaaaaa",
    bg="#101820"
)

subtitle.pack(pady=5)


# Main panel

main_frame = tk.Frame(
    window,
    bg="#1c2730",
    padx=25,
    pady=20
)

main_frame.pack(
    padx=35,
    fill="both"
)


# Living room

living_title = tk.Label(
    main_frame,
    text="Living Room",
    font=("Arial", 17, "bold"),
    fg="white",
    bg="#1c2730"
)

living_title.pack(pady=(5, 10))


living_button = tk.Button(
    main_frame,
    text="TURN ON",
    width=16,
    font=("Arial", 11, "bold"),
    bg="#2e8b57",
    fg="white",
    command=toggle_living
)

living_button.pack(pady=5)


brightness_text = tk.Label(
    main_frame,
    text="Brightness",
    font=("Arial", 12),
    fg="#dddddd",
    bg="#1c2730"
)

brightness_text.pack(pady=(15, 0))


brightness_slider = tk.Scale(
    main_frame,
    from_=0,
    to=100,
    orient="horizontal",
    length=330,
    showvalue=False,
    bg="#1c2730",
    fg="white",
    troughcolor="#555555",
    highlightthickness=0,
    command=change_brightness
)

brightness_slider.set(100)
brightness_slider.pack()


brightness_value = tk.Label(
    main_frame,
    text="100%",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#1c2730"
)

brightness_value.pack(pady=(0, 15))


# Separator

separator = tk.Frame(
    main_frame,
    height=2,
    bg="#444444"
)

separator.pack(fill="x", pady=10)


# Bathroom

bathroom_title = tk.Label(
    main_frame,
    text="Bathroom",
    font=("Arial", 15, "bold"),
    fg="white",
    bg="#1c2730"
)

bathroom_title.pack(pady=5)


bathroom_button = tk.Button(
    main_frame,
    text="TURN ON",
    width=16,
    font=("Arial", 11, "bold"),
    bg="#2e8b57",
    fg="white",
    command=toggle_bathroom
)

bathroom_button.pack(pady=5)


# Closet

closet_title = tk.Label(
    main_frame,
    text="Closet",
    font=("Arial", 15, "bold"),
    fg="white",
    bg="#1c2730"
)

closet_title.pack(pady=8)


closet_button = tk.Button(
    main_frame,
    text="TURN ON",
    width=16,
    font=("Arial", 11, "bold"),
    bg="#2e8b57",
    fg="white",
    command=toggle_closet
)

closet_button.pack(pady=5)


# Master buttons

master_frame = tk.Frame(
    window,
    bg="#101820"
)

master_frame.pack(pady=25)


all_on_button = tk.Button(
    master_frame,
    text="ALL LIGHTS ON",
    width=16,
    font=("Arial", 11, "bold"),
    bg="#2874a6",
    fg="white",
    command=all_on
)

all_on_button.grid(row=0, column=0, padx=5)


all_off_button = tk.Button(
    master_frame,
    text="ALL LIGHTS OFF",
    width=16,
    font=("Arial", 11, "bold"),
    bg="#555555",
    fg="white",
    command=all_off
)

all_off_button.grid(row=0, column=1, padx=5)


# Exit button

exit_button = tk.Button(
    window,
    text="EXIT",
    width=14,
    font=("Arial", 11, "bold"),
    bg="#8b0000",
    fg="white",
    command=close_program
)

exit_button.pack(pady=5)


# Handle window close

window.protocol(
    "WM_DELETE_WINDOW",
    close_program
)


# Run program

window.mainloop()