import tkinter

def show_image(label):
    img = tkinter.PhotoImage(file='alligator.png')
    label.configure(image= img)
    label.image = img

def main():
    window = tkinter.Tk()
    question = tkinter.Label(window, text="Want to see cool image?")

    image = tkinter.Label(window, image=None)

    button = tkinter.Button(
        window,
        text="Click Here!",
        width=25,
        height=5,
        command= lambda: show_image(image)
    )

    question.pack()
    button.pack()
    image.pack()
    window.mainloop()


if __name__ == "__main__":
    main()