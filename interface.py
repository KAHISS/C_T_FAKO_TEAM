from tkinter import ttk
from tkinter import *
from tkcalendar import *
from customtkinter import *
from functions import GeneralFunctions


class Interface(GeneralFunctions):
    def __init__(self):
        self.colorsOfButtons = self.dataBases['config'].searchDatabase('SELECT * FROM Botões')[0]
        self.colorsOfFrames = self.dataBases['config'].searchDatabase('SELECT * FROM Frames')[0]
        self.colorsOfTabviews = self.dataBases['config'].searchDatabase('SELECT * FROM Tabviews')[0]
        self.colorsOfTreeviews = self.dataBases['config'].searchDatabase('SELECT * FROM Treeviews')[0]
        self.colorsOfEntrys = self.dataBases['config'].searchDatabase('SELECT * FROM Entrys')[0]
        self.colorsOfLabels = self.dataBases['config'].searchDatabase('SELECT * FROM Labels')[0]

    def labels(self, window, text, posx, posy, width=0.1, height=0.1, color='black', background='#ffffff', position=W, photo=None, size=21, font='Arial', custom='default'):
        label = None
        match custom:
            case 'default':
                label = CTkLabel(
                    window, text=text, font=CTkFont(font, size, 'bold'),
                    fg_color=self.colorsOfFrames[0],
                    anchor=position, text_color=self.colorsOfLabels[0] if custom == 'default' else self.colorsOfTabviews[1], image=photo
                )
                label.place(relx=posx, rely=posy, relwidth=width, relheight=height)
            case 'tabview':
                label = CTkLabel(
                    window, text=text, font=CTkFont(font, size, 'bold'),
                    fg_color=self.colorsOfTabviews[0],
                    anchor=position, text_color=self.colorsOfLabels[0] if custom == 'default' else self.colorsOfTabviews[1], image=photo
                )
                label.place(relx=posx, rely=posy, relwidth=width, relheight=height)
            case 'custom':
                label = CTkLabel(
                    window, text=text, font=CTkFont(font, size, 'bold'),
                    fg_color=background,
                    anchor=position, text_color='black', image=photo
                )
                label.place(relx=posx, rely=posy, relwidth=width, relheight=height)
            case 'optional':
                label = CTkLabel(
                    window, text=text, font=CTkFont(font, size, 'bold'),
                    fg_color=self.colorsOfFrames[0],
                    anchor=position, text_color=self.colorsOfLabels[1], image=photo
                )
                label.place(relx=posx, rely=posy, relwidth=width, relheight=height)
        return label

    def entry(
            self, window, posx, posy, width=0.1, height=0.1, value=None, type_entry='list', place_text='', position=LEFT, validity='no', function=None, background='#FFFFFF',
            radius=20, border=0, show='', font_size=16, border_color='#b59b50'
    ):
        if value is None:
            value = []
        camp = None
        match type_entry:
            case 'list':
                camp = CTkComboBox(
                    window, fg_color=self.colorsOfEntrys[0], text_color=self.colorsOfEntrys[1], border_color=self.colorsOfEntrys[2], values=value, dropdown_fg_color=self.colorsOfButtons[0], dropdown_hover_color=self.colorsOfButtons[3],
                    button_color=self.colorsOfButtons[0], button_hover_color=self.colorsOfButtons[3], font=CTkFont('Arial', font_size), dropdown_text_color=self.colorsOfButtons[1], command=function
                )
                camp.place(relx=posx, rely=posy, relwidth=width, relheight=height)
                camp.set('')
            case 'entry':
                camp = CTkEntry(
                    window, fg_color=self.colorsOfEntrys[0], text_color=self.colorsOfEntrys[1], border_color=self.colorsOfEntrys[2], font=CTkFont('Arial', font_size), placeholder_text=place_text,
                    placeholder_text_color='#222222', justify=position, show=show
                )
                camp.place(relx=posx, rely=posy, relwidth=width, relheight=height)
            case 'date':
                camp = DateEntry(
                    window, width=12, font='Arial', background=self.colorsOfButtons[0], fg=self.colorsOfEntrys[1], locale='pt_BR', headersbackground=self.colorsOfButtons[2], headersforeground=self.colorsOfButtons[1],
                    foreground=self.colorsOfLabels[0], highlightthickness=7, highlightcolor='black'
                )

                if validity == 'no':
                    camp.config(validate='none')
                    camp.delete(0, END)

                camp.place(relx=posx, rely=posy, relwidth=width, relheight=height)
            case 'entryLogin':
                camp = CTkEntry(
                    window, fg_color=self.colorsOfEntrys[0], text_color=self.colorsOfEntrys[1], border_color=self.colorsOfEntrys[2], font=CTkFont('Arial', 16), placeholder_text=place_text,
                    placeholder_text_color=self.colorsOfLabels[0], justify=position, corner_radius=radius, border_width=border, show=show
                )
                camp.place(relx=posx, rely=posy, relwidth=width, relheight=height)
        return camp

    def button(
            self, window, text, posx, posy, width=None, height=None, function=None, type_btn='normal', order_list=None, photo=None, background='#917c3f', retur_variable=None, value='', hover_cursor='#c9c9c9',
            border=2, color='#ffffff', border_color='#b59b50', custom='default'
    ):
        btn = None
        match type_btn:
            case 'normal':
                btn = CTkButton(
                    window, text=text, font=CTkFont('Arial', 17, 'bold'), command=function, image=photo,
                    fg_color=self.colorsOfButtons[0], text_color=self.colorsOfButtons[1], border_width=border, border_color=self.colorsOfButtons[2], hover_color=self.colorsOfButtons[3],
                    cursor='hand2'
                )
                btn.place(relx=posx, rely=posy, relwidth=width, relheight=height)
            case 'buttonPhoto':
                btn = CTkButton(window, command=function, image=photo, fg_color=self.colorsOfFrames[0] if custom == 'default' else self.colorsOfEntrys[0], cursor='hand2', text='', hover_color=self.colorsOfButtons[3], corner_radius=0)
                btn.place(relx=posx, rely=posy, relwidth=width, relheight=height)
            case 'tabview':
                btn = CTkButton(window, command=function, image=photo, fg_color=self.colorsOfTabviews[0], cursor='hand2', text='', hover_color=self.colorsOfButtons[3], corner_radius=0)
                btn.place(relx=posx, rely=posy, relwidth=width, relheight=height)
            case 'optionMenu':
                btn = CTkOptionMenu(
                    window, font=CTkFont('Arial', 17, 'bold'), command=function, values=order_list,
                    fg_color=self.colorsOfButtons[0], button_color=self.colorsOfButtons[0], text_color=self.colorsOfButtons[1], dropdown_fg_color=self.colorsOfButtons[0], dropdown_text_color=self.colorsOfButtons[1],
                    dropdown_hover_color=self.colorsOfButtons[3], button_hover_color=self.colorsOfButtons[3]
                )
                btn.place(relx=posx, rely=posy, relwidth=width, relheight=height)
            case 'radioButton':
                btn = CTkRadioButton(
                    window, text=text, variable=retur_variable, value=value, text_color=self.colorsOfLabels[0], border_color=self.colorsOfButtons[2],
                    font=CTkFont('Arial', 16, 'bold'), hover_color=self.colorsOfButtons[3], fg_color=self.colorsOfButtons[2]
                )
                btn.place(relx=posx, rely=posy, relwidth=width, relheight=height)
        return btn

    def ask(self, window, text1, text2, posx, posy, entry, width=None, height=None):
        question = StringVar(value='')
        yes = self.button(
            window, text1, posx, posy, width, height, type_btn='radioButton',
            value=text1, retur_variable=question
        )
        no = self.button(
            window, text2, posx + 0.07, posy, width, height, type_btn='radioButton',
            value=text2, retur_variable=question
        )
        yes.bind(
            '<Button-1>', lambda e: [
                entry.configure(state='normal', fg_color='#ffffff'),
                entry.delete(0, END),
            ]
        )
        no.bind(
            '<Button-1>', lambda e: [
                entry.delete(0, END),
                entry.insert(0, '===X==='),
                entry.configure(state='disable', fg_color='#f4f4f4')
            ]
        )

        return [question, yes, no]

    def frame(self, window, posx, posy, width=None, height=None, background_color='white', border_color='#b59b50', border=2, radius=5, type_frame='default', text=''):
        frm = None
        match type_frame:
            case 'default':
                frm = CTkFrame(window, fg_color=self.colorsOfFrames[0], border_color=self.colorsOfFrames[1], border_width=border, corner_radius=radius)
                frm.place(relx=posx, rely=posy, relwidth=width, relheight=height)
            case 'labelFrame':
                frm = LabelFrame(window, text=text, borderwidth=border, bg=self.colorsOfFrames[0], font=('Arial', '12', 'bold'), fg=self.colorsOfLabels[0])
                frm.place(relx=posx, rely=posy, relwidth=width, relheight=height)
            case 'scollFrame':
                frm = CTkScrollableFrame(window, fg_color=self.colorsOfFrames[0], border_color=self.colorsOfFrames[1], border_width=border, corner_radius=radius)
                frm.place(relx=posx, rely=posy, relwidth=width, relheight=height)
        return frm

    @staticmethod
    def notebook(locate, posx=0, posy=0.01, width=1, height=1):
        tab = ttk.Notebook(locate,)
        tab.place(relx=0, rely=0.01, relwidth=1, relheight=1)
        return tab

    @staticmethod
    def main_frame_notebook(locate, name_tab, bg='white'):
        frame = Frame(locate, background=bg)
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        locate.add(frame, text=name_tab, padding=[5, 0])
        return frame

    def tabview(self, locate, posx, posy, width, height, background='#b59b50', border='#b59b50', type_tab='default'):
        tab = None
        if type_tab == 'default':
            tab = CTkTabview(
                locate, fg_color=self.colorsOfTabviews[0], border_width=3, border_color=self.colorsOfTabviews[1], segmented_button_fg_color=self.colorsOfButtons[2], segmented_button_unselected_color=self.colorsOfButtons[0],
                text_color=self.colorsOfButtons[1], segmented_button_selected_color=self.colorsOfButtons[0], segmented_button_unselected_hover_color=self.colorsOfButtons[3], segmented_button_selected_hover_color=self.colorsOfButtons[2]
            )
            tab.place(relx=posx, rely=posy, relwidth=width, relheight=height)
        elif type_tab == 'frame':
            tab = CTkTabview(
                locate, fg_color=self.colorsOfFrames[0], border_width=3, border_color=self.colorsOfFrames[1], segmented_button_fg_color=self.colorsOfButtons[2], segmented_button_unselected_color=self.colorsOfButtons[0],
                text_color=self.colorsOfButtons[1], segmented_button_selected_color=self.colorsOfButtons[0], segmented_button_unselected_hover_color=self.colorsOfButtons[3], segmented_button_selected_hover_color=self.colorsOfButtons[2]
            )
            tab.place(relx=posx, rely=posy, relwidth=width, relheight=height)
        return tab

    def scrollbar(self, locate, orient, position, x_or_y):
        scrollbar = CTkScrollbar(
            locate, orientation=orient, button_color=self.colorsOfButtons[0], minimum_pixel_length=200, fg_color='#d8d8d8', border_spacing=1,
            button_hover_color=self.colorsOfButtons[3]
        )
        scrollbar.pack(side=position, fill=x_or_y)
        return scrollbar

    def treeview(self, locate, informations, max_width=0):
        # scrollbar ---------------------------------------------------
        yscrollbar = self.scrollbar(locate, 'vertical', RIGHT, Y)
        xscrollbar = self.scrollbar(locate, 'horizontal', BOTTOM, X)

        # Treeview -----------------------------------------------------
        treeview = ttk.Treeview(locate, columns=informations, show='headings', height=24, yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)
        yscrollbar.configure(command=treeview.yview)
        xscrollbar.configure(command=treeview.xview)

        # configurando
        for name in informations:
            if name == 'ID':
                treeview.column(f'{name}', minwidth=0, width=50, anchor=CENTER, stretch=False)
            elif name in ['Observações', 'Foto', 'observação', 'foto']:
                treeview.column(f'{name}', minwidth=0, width=0, anchor=CENTER, stretch=False)
            elif name in ['Cliente', 'Nome', 'Serviço', 'Profissional']:
                treeview.column(f'{name}', minwidth=0, width=400, anchor=CENTER, stretch=False)
            elif max_width > 0:
                treeview.column(f'{name}', minwidth=20, width=max_width, anchor=CENTER, stretch=False)
            else:
                treeview.column(f'{name}', minwidth=20, width=250, anchor=CENTER, stretch=False)
        for names in informations:
            treeview.heading(f'{names}', text=f'{names}')
        treeview.tag_configure('oddrow', background=self.colorsOfTreeviews[0])
        treeview.tag_configure('evenrow', background=self.colorsOfTreeviews[1])
        treeview.tag_configure('branca', background='#FFFFFF', foreground='black')
        treeview.tag_configure('cinza', background='#616161', foreground='white')
        treeview.tag_configure('amarela', background='#ffff00', foreground='black')
        treeview.tag_configure('laranja', background='#db8104', foreground='white')
        treeview.tag_configure('verde', background='#029c09', foreground='white')
        treeview.tag_configure('azul', background='#5d73fc', foreground='white')
        treeview.tag_configure('roxa', background='#b66eff', foreground='white')
        treeview.tag_configure('marrom', background='#756443', foreground='white')
        treeview.tag_configure('preta', background='#3d3d3d', foreground='white')
        treeview.place(relx=0.002, rely=0.01, relwidth=0.985, relheight=0.95)
        return treeview

    def text_box(self, locate, posx, posy, width, height, bg='white'):
        textBox = CTkTextbox(
            locate, border_width=2, border_color=self.colorsOfFrames[1], fg_color=self.colorsOfFrames[0], text_color=self.colorsOfLabels[0], font=CTkFont('Arial', 14),
            scrollbar_button_color=self.colorsOfButtons[0], scrollbar_button_hover_color=self.colorsOfButtons[3]
        )
        textBox.place(relx=posx, rely=posy, relwidth=width, relheight=height)
        return textBox

    def tab_of_buttons(
            self, posx, posy, width, height, locate, functions, icons, values=None, treeview='yes', type_btns='complete', type_register='Cadastrar',
            send_message='no'
    ):
        # buttons management ============
        frameBtns = self.tabview(locate, posx, posy, width, height)
        frameBtns.add('Gerenciamento')

        if type_btns == 'complete':
            # registration ----------
            registrationBtn = self.button(frameBtns.tab('Gerenciamento'), type_register, 0.225, 0.00, 0.55, 0.2, function=functions['register'])
            # search -------------
            searchBtn = self.button(frameBtns.tab('Gerenciamento'), 'Buscar', 0.225, 0.25, 0.55, 0.2, function=functions['search'])
            # update -------------
            updateBtn = self.button(frameBtns.tab('Gerenciamento'), 'Atualizar', 0.225, 0.50, 0.55, 0.2, function=functions['update'])
            # delete ---------
            deleteBtn = self.button(frameBtns.tab('Gerenciamento'), 'Deletar', 0.225, 0.75, 0.55, 0.2, function=functions['delete'])
        elif type_btns == 'sale':
            # registration ----------
            registrationBtn = self.button(frameBtns.tab('Gerenciamento'), 'Cadastrar', 0.225, 0.00, 0.55, 0.17, function=functions['register'])
            # search -------------
            searchBtn = self.button(frameBtns.tab('Gerenciamento'), 'Buscar', 0.225, 0.20, 0.55, 0.17, function=functions['search'])
            # update -------------
            updateBtn = self.button(frameBtns.tab('Gerenciamento'), 'Atualizar', 0.225, 0.40, 0.55, 0.17, function=functions['update'])
            # sale ---------
            saleBtn = self.button(frameBtns.tab('Gerenciamento'), 'Venda', 0.225, 0.60, 0.55, 0.17, function=functions['sale'])
            # delete
            deleteBtn = self.button(frameBtns.tab('Gerenciamento'), 'Deletar', 0.225, 0.80, 0.55, 0.17, function=functions['delete'])
        elif type_btns == 'management':
            # search -------------
            searchBtn = self.button(frameBtns.tab('Gerenciamento'), 'Buscar', 0.225, 0.05, 0.55, 0.2, function=functions['search'])
            # update -------------
            updateBtn = self.button(frameBtns.tab('Gerenciamento'), 'Atualizar', 0.225, 0.36, 0.55, 0.2, function=functions['update'])
            # delete ---------
            deleteBtn = self.button(frameBtns.tab('Gerenciamento'), 'Deletar', 0.225, 0.67, 0.55, 0.2, function=functions['delete'])
        elif type_btns == 'managementSchedule':
            # search -------------
            searchBtn = self.button(frameBtns.tab('Gerenciamento'), 'Buscar', 0.225, 0.02, 0.55, 0.2, function=functions['search'])
            # update -------------
            updateBtn = self.button(frameBtns.tab('Gerenciamento'), 'Atualizar', 0.225, 0.25, 0.55, 0.2, function=functions['update'])
            # reschedule -------------
            rescheduleBtn = self.button(frameBtns.tab('Gerenciamento'), 'Remarcar', 0.225, 0.49, 0.55, 0.2, function=functions['reschedule'])
            # delete ---------
            deleteBtn = self.button(frameBtns.tab('Gerenciamento'), 'Deletar', 0.225, 0.73, 0.55, 0.2, function=functions['delete'])

        if send_message == 'yes':
            # buttons send message ================
            frameBtns.add('Mensagem')
            # inform -----------------
            informBtn = self.button(frameBtns.tab('Mensagem'), 'Informar clientes', 0.225, 0.08, 0.55, 0.2, function=functions['InformClient'])
            # confirm -------------
            confirmBtn = self.button(frameBtns.tab('Mensagem'), 'Confirmar clientes', 0.225, 0.38, 0.55, 0.2, function=functions['confirmClient'])
            # message -------------
            sendMessageBtn = self.button(frameBtns.tab('Mensagem'), 'Enviar mensagem', 0.225, 0.68, 0.55, 0.2, function=functions['sendMessage'])

        if treeview == 'yes':
            # buttons treeview ================
            frameBtns.add('Tabela')
            # order --------------
            labelOrder = self.labels(frameBtns.tab('Tabela'), 'Ordem', 0.25, 0.0, width=0.50, height=0.2, position=CENTER, custom='tabview').configure(text_color=self.colorsOfButtons[1])
            orderBtn = self.button(frameBtns.tab('Tabela'), 'Deletar', 0.225, 0.20, 0.55, 0.2, type_btn='optionMenu', function=functions['order'], order_list=values)
            # pdf and informations ----------------
            labelInfo = self.labels(frameBtns.tab('Tabela'), 'Informações', 0.17, 0.45, width=0.7, height=0.2, color='#b59b50', background='#e8d499', position=CENTER, custom='tabview').configure(text_color=self.colorsOfButtons[1])
            pdf = self.button(frameBtns.tab('Tabela'), '', 0.3, 0.7, 0.2, photo=icons['pdf'][0], type_btn='tabview', background='pink', function=functions['pdf'])
            informacao = self.button(frameBtns.tab('Tabela'), '', 0.53, 0.7, 0.2, photo=icons['informações'][0], type_btn='tabview', background='pink', function=functions['informations'])
            return orderBtn

    def informations_simple(self, locate, type_info, informations, funcs, icons, photo):
        # frame inputs ==========================================
        frameInputsInformations = self.frame(locate, 0.195, 0.01, 0.6, 0.43)

        # info --------------------
        labelInfo = self.labels(frameInputsInformations, type_info, 0.03, 0.395, width=0.16)
        informationsEntry = self.entry(frameInputsInformations, 0.20, 0.39, 0.25, 0.12, type_entry='entry')

        # delete informations -------------
        deleteInformationsInputs = self.button(
            frameInputsInformations, 'apagar', 0.003, 0.87, 0.06, 0.12, function=lambda: informationsEntry.delete(0, END),
            photo=photo, type_btn='buttonPhoto', background='white', hover_cursor='white'
        )

        # frame treeview ==================
        treeviewInformationFrame = self.frame(locate, 0.195, 0.45, 0.6, 0.53)

        # Treeview -----------------------------------------------------
        treeviewInformation = self.treeview(treeviewInformationFrame, informations, max_width=1120)

        # buttons management ============
        orderBtnInformations = self.tab_of_buttons(0.49, 0.02, 0.45, 0.9, frameInputsInformations, funcs, icons, informations)

        return {'entry': informationsEntry, 'treeview': treeviewInformation, 'order': orderBtnInformations}

    def line_separator(self, locate, posx, posy, width=0.9, height=0.1):
        lineHigher = Canvas(locate, background=self.colorsOfFrames[0], highlightthickness=0)
        lineHigher.place(relx=posx, rely=posy, relwidth=width, relheight=height)
        lineHigher.create_line(1, 15, 3000, 15, fill=self.colorsOfFrames[1], width=2)
        return lineHigher
