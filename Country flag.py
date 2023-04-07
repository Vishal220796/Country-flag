from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Country flag")
root.geometry("600x600")
root.configure(background="orange")

get_input = Entry(root)
show_label = Label(root)

india_map = ImageTk.PhotoImage(Image.open ("India.jpg"))
america_map = ImageTk.PhotoImage(Image.open ("America.jpg"))
italy_map = ImageTk.PhotoImage(Image.open ("Italy.jpg"))
bahrain_map = ImageTk.PhotoImage(Image.open ("Bahrain.jpg"))
uae_map = ImageTk.PhotoImage(Image.open ("UAE.jpg"))
japan_map = ImageTk.PhotoImage(Image.open ("Japan.jpg"))
singapore_map = ImageTk.PhotoImage(Image.open ("Singapore.jpg"))

maps_dictionary = { "India" : india_map ,
                   "America" : america_map ,
                   "Italy" : italy_map , 
                   "Bahrain" : bahrain_map ,
                   "UAE" : uae_map , 
                   "Japan" : japan_map ,
                   "Singapore" : singapore_map,}

def showMaps():
    try:
        map_name = get_input.get()
        print(map_name)
        show_label['image'] = maps_dictionary[map_name]
    except:
            messagebox.showinfo("Error", "Sorry! This country flag cannot be shown")
            
            btn = Button(root , text="Show FLAG", bg="blue", command=showMaps)
            get_input.place(relx=0.5, rely=0.1, anchor=CENTER)
            btn.place(relx=0.5, rely=0.2, anchor=CENTER)
            show_label.place(relx=0.5, rely=0.6, anchor=CENTER)
            
            root.mainloop()