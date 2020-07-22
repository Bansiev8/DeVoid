import tkinter as kin
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_app = kin.Tk()
main_app.geometry('1920x1080')
main_app.title("DeVoid")
main_app.wm_iconbitmap("icon.ico")

#main menu

main_menu = kin.Menu()
    #file icons
new_icon = kin.PhotoImage(file='usingic/new.png')
open_icon = kin.PhotoImage(file='usingic/open.png')
save_icon = kin.PhotoImage(file='usingic/save.png')
saveas_icon = kin.PhotoImage(file='usingic/save_as.png')
exit_icon = kin.PhotoImage(file='usingic/exit.png')

file = kin.Menu(main_menu, tearoff=False)



      #edit icons
copy_icon = kin.PhotoImage(file='usingic/copy.png')
paste_icon = kin.PhotoImage(file='usingic/paste.png')
cut_icon = kin.PhotoImage(file='usingic/cut.png')
clear_icon = kin.PhotoImage(file='usingic/clear_all.png')
find_icon = kin.PhotoImage(file='usingic/find.png')

edit = kin.Menu(main_menu, tearoff=False)




    #view icons


toolbar_icon = kin.PhotoImage(file='usingic/tool_bar.png')
statusbar_icon = kin.PhotoImage(file='usingic/status_bar.png')

view = kin.Menu(main_menu, tearoff=False)




    #color icons

light_icon = kin.PhotoImage(file='usingic/light_default.png')
dark_icon = kin.PhotoImage(file='usingic/dark.png')

theme = kin.Menu(main_menu, tearoff=False)

theme_choice = kin.StringVar()
color_icons = (light_icon, dark_icon)
color_dict = {
    'Light (Default)' : ('#000000','#ffffff'),
    'Dark' : ('#ffffff', '#000000')
}


#cascade

main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Theme', menu=theme)


#tool bar

tool_bar = kin.Label(main_app)
tool_bar.pack(side=kin.TOP, fill=kin.X)
font_tup = kin.font.families()
font_fam = kin.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_fam, state='readonly')
font_box['values'] = font_tup
font_box.current(font_tup.index('Arial'))
font_box.grid(row=0, column=0, padx=5)


size = kin.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable=size, state='readonly')
font_size['values'] = tuple(range(8,80,2))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)

                         #buttons

bold_icon = kin.PhotoImage(file='usingic/bold.png')
bold = ttk.Button(tool_bar, image=bold_icon)
bold.grid(row=0, column=2, padx=5)

italic_icon = kin.PhotoImage(file='usingic/italic.png')
italic = ttk.Button(tool_bar, image=italic_icon)
italic.grid(row=0, column=4, padx=5)

under_icon = kin.PhotoImage(file='usingic/underline.png')
under = ttk.Button(tool_bar, image=under_icon)
under.grid(row=0, column=6, padx=5)

color_icon = kin.PhotoImage(file='usingic/font_color.png')
color = ttk.Button(tool_bar, image= color_icon)
color.grid(row=0, column=8, padx=5)

aln_lft_icon = kin.PhotoImage(file='usingic/align_left.png')
aln_lft = ttk.Button(tool_bar, image= aln_lft_icon)
aln_lft.grid(row=0, column=10, padx=5)

aln_rgt_icon = kin.PhotoImage(file='usingic/align_right.png')
aln_rgt = ttk.Button(tool_bar, image= aln_rgt_icon)
aln_rgt.grid(row=0, column=12, padx=5)

aln_cnt_icon = kin.PhotoImage(file='usingic/align_center.png')
aln_cnt = ttk.Button(tool_bar, image= aln_cnt_icon)
aln_cnt.grid(row=0, column=14, padx=5)



                                                #text editor


text = kin.Text(main_app)
text.config(wrap='word', relief=kin.FLAT)

scroll = kin.Scrollbar(main_app)
text.focus_set()
scroll.pack(side=kin.RIGHT, fill=kin.Y)
text.pack(fill=kin.BOTH, expand=True)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

curr_font = 'Arial'
curr_size = 12

def change_font(main_app):
    global curr_font
    curr_font = font_fam.get()
    text.configure(font=(curr_font, curr_size))

def change_size(main_app):
    global curr_size
    curr_size = size.get()
    text.configure(font=(curr_font, curr_size))

font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_size)


                                                       #button functions
#bold
def change_bold():
    text_prop = kin.font.Font(font=text['font'])
    if text_prop.actual()['weight'] == 'normal':
        text.configure(font=(curr_font, curr_size, 'bold'))
    if text_prop.actual()['weight'] == 'bold':
        text.configure(font=(curr_font, curr_size, 'normal'))
bold.configure(command=change_bold)

#italic
def change_italic():
    text_prop = kin.font.Font(font=text['font'])
    if text_prop.actual()['slant'] == 'roman':
        text.configure(font=(curr_font, curr_size, 'italic'))
    if text_prop.actual()['slant'] == 'italic':
        text.configure(font=(curr_font, curr_size, 'normal'))
italic.configure(command=change_italic)

#underline
def change_under():
    text_prop = kin.font.Font(font=text['font'])
    if text_prop.actual()['underline'] == 0:
        text.configure(font=(curr_font, curr_size, 'underline'))
    if text_prop.actual()['underline'] == 1:
        text.configure(font=(curr_font, curr_size, 'normal'))
under.configure(command=change_under)

#fontcolor
def change_color():
    color = kin.colorchooser.askcolor()
    text.configure(fg=color[1])
color.configure(command=change_color)

#alignmethods
def alignleft():
    text_con =text.get(1.0, 'end')
    text.tag_config('left', justify=kin.LEFT)
    text.delete(1.0, kin.END)
    text.insert(kin.INSERT, text_con, 'left')
aln_lft.configure(command=alignleft)

def alignright():
    text_con =text.get(1.0, 'end')
    text.tag_config('right', justify=kin.RIGHT)
    text.delete(1.0, kin.END)
    text.insert(kin.INSERT, text_con, 'right')
aln_rgt.configure(command=alignright)

def aligncenter():
    text_con =text.get(1.0, 'end')
    text.tag_config('center', justify=kin.CENTER)
    text.delete(1.0, kin.END)
    text.insert(kin.INSERT, text_con, 'center')
aln_cnt.configure(command=aligncenter)



text.configure(font=('Arial, 12'))



                                                    #status bar

status = ttk.Label(main_app, text='Status Bar')
status.pack(side=kin.BOTTOM)

text_chan = False
def counts(event=None):
    global text_chan
    if text.edit_modified():
        text_chan = True
        words = len(text.get(1.0, 'end-1c').split())
        chars = len(text.get(1.0, 'end-1c'))#if no spaces needed .replace(' ','')
        status.config(text=f'Characters : {chars} Words : {words}')
    text.edit_modified(False)
text.bind("<<Modified>>", counts)


                         #main menu functions
                         #file commands
url = ''
def new_file(event=None):
    global url
    url = ''
    text.delete(1.0, kin.END)

def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(("Text File",'*.txt'),('All Files', '*.*')))
    try:
        with open(url, 'r') as fl:
            text.delete(1.0, kin.END)
            text.insert(1.0, fl.read())
    except FileNotFoundError:
        return
    except:
        return
    main_app.title(os.path.basename(url))

def save_file(event=None):
    global url
    try:
        if url:
            content = str(text.get(1.0, kin.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',filetypes=(("Text File", '*.txt'), ('All Files', '*.*')))
            content2 = text.get(1.0, kin.END)
            url.write(content2)
            url.close()
    except:
        return


def saveas_file(event=None):
    global url
    try:
        content = text.get(1.0, kin.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',filetypes=(("Text File", '*.txt'), ('All Files', '*.*')))
        url.write(content)
        url.close()
    except:
        return

def exit_file(event=None):
    global url
    try:
        if text_chan:
            mbox = messagebox.askyesnocancel('Warning','Do You Want To Save The File')
            if mbox is True:
                if url:
                    content = text.get(1.0, kin.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_app.destroy()
                else:
                    content2 = str(text.get(1.0, kin.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',filetypes=(("Text File", '*.txt'), ('All Files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_app.destroy()
            elif mbox is False:
                main_app.destroy()
        else:
            main_app.destroy()
    except:
        return




file.add_command(label='New', image=new_icon, compound=kin.LEFT, accelerator='Ctrl+N', command=new_file)
file.add_command(label='Open', image=open_icon, compound=kin.LEFT, accelerator='Ctrl+O', command=open_file)
file.add_command(label='Save', image=save_icon, compound=kin.LEFT, accelerator='Ctrl+S', command=save_file)
file.add_command(label='SaveAs', image=saveas_icon, compound=kin.LEFT, accelerator='Ctrl+Alt+S', command=saveas_file)
file.add_command(label='Exit', image=exit_icon, compound=kin.LEFT, accelerator='Ctrl+Q', command=exit_file)

                            #edit commands


def find_text(event=None):
    def findd():
        word = find_inp.get()
        text.tag_remove('match', '1.0', kin.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text.search(word, start_pos, stopindex=kin.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text.tag_config('match', foreground='red', background='yellow')



    def replace():
        word = find_inp.get()
        replace_text = replace_inp.get()
        content = text.get(1.0, kin.END)
        new_content = content.replace(word, replace_text)
        text.delete(1.0, kin.END)
        text.insert(1.0, new_content)

    find = kin.Toplevel()
    find.geometry('450x250+500+200')
    find.title('Find')
    find.resizable(0,0)

    find_frame = ttk.LabelFrame(find, text="Find/Replace")
    find_frame.pack(pady=20)

    text_find = ttk.Label(find_frame, text='Find :')
    text_replace = ttk.Label(find_frame, text='Replace :')

    find_inp = ttk.Entry(find_frame, width=30)
    replace_inp = ttk.Entry(find_frame, width=30)

    find_button = ttk.Button(find_frame, text='Find', command=findd)
    replace_button = ttk.Button(find_frame, text='Replace', command=replace)

    text_find.grid(row=0, column=0, padx=4, pady=4)
    text_replace.grid(row=1, column=0, padx=4, pady=4)

    find_inp.grid(row=0, column=1, padx=4, pady=4)
    replace_inp.grid(row=1, column=1, padx=4, pady=4)

    find_button.grid(row=2, column=0, padx=4, pady=4)
    replace_button.grid(row=2, column=1, padx=4, pady=4)

    find.mainloop()

edit.add_command(label='Copy', image=copy_icon, compound=kin.LEFT, accelerator="Ctrl+C", command=lambda:text.event_generate("<Control c>") )
edit.add_command(label='Paste', image=paste_icon, compound=kin.LEFT, accelerator="Ctrl+V", command=lambda:text.event_generate("<Control v>"))
edit.add_command(label='Cut', image=cut_icon, compound=kin.LEFT, accelerator="Ctrl+X", command=lambda:text.event_generate("<Control x>"))
edit.add_command(label='Clear', image=clear_icon, compound=kin.LEFT, accelerator="Ctrl+shift+x", command=lambda:text.delete(1.0, kin.END))
edit.add_command(label='Find', image=find_icon, compound=kin.LEFT, accelerator="Ctrl+F", command=find_text)

                            #view commands


show_statusbar = kin.BooleanVar()
show_statusbar.set(True)
show_toolbar = kin.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else :
        text.pack_forget()
        status.pack_forget()
        tool_bar.pack(side=kin.TOP, fill=kin.X)
        text.pack(fill=kin.BOTH, expand=True)
        status.pack(side=kin.BOTTOM)
        show_toolbar = True


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status.pack_forget()
        show_statusbar = False
    else :
        status.pack(side=kin.BOTTOM)
        show_statusbar = True



view.add_checkbutton(label='Tool Bar', onvalue=True, offvalue=False, image=toolbar_icon, compound=kin.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar', onvalue=True, offvalue=False, image=statusbar_icon, compound=kin.LEFT, command=hide_statusbar)

                            #color commands
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text.config(background=bg_color, fg=fg_color)


count = 0
for i in color_dict:
    theme.add_radiobutton(label = i, image = color_icons[count], variable = theme_choice, compound = kin.LEFT, command=change_theme)
    count+=1


main_app.config(menu=main_menu)

main_app.bind("<Control-n>", new_file)
main_app.bind("<Control-o>", open_file)
main_app.bind("<Control-s>", save_file)
main_app.bind("<Control-Alt-s>", saveas_file)
main_app.bind("<Control-q>", exit_file)
main_app.bind("<Control-f>", find_text)

main_app.mainloop()