from tkinter import *
import sqlite3


class MainMenu():
    def __init__(self,master):
        self.master = master
        self.menubar = Menu(self.master)
        self.master.geometry('1000x600')
        self.PasswordMenu()

    def PasswordMenu(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title ("Appointment System")
        self.PasswordFrame = Frame(self.master)
        self.PasswordFrame.pack()

        background = Canvas(self.PasswordFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,55, image=photo)
        background.create_text(500, 50, text='Log In', font=('comic sans ms',50), fill='violetred4')
      
        self.Username = StringVar()
        self.Password = StringVar()
        
        self.Username_Text= Label(self.PasswordFrame, text= "Username: ", fg='black', bg='white', font=('ariel',12)).place(x=350, y=200)
        self.Username_Data= Entry(self.PasswordFrame, width = 20, font=('ariel',12), bg='grey88', textvariable = self.Username).place(x=450,y=200)
        self.Password_Text= Label(self.PasswordFrame, text= "Password: ", fg='black', bg='White', font=('ariel',12)).place(x=350, y=240)
        self.Password_Data= Entry(self.PasswordFrame, width = 20, font=('ariel',12), bg='grey88', show="*", textvariable = self.Password).place(x=450,y=240)

        self.Login = Button(self.PasswordFrame, text='Log In', font=('Comic Sans MS', 12,'underline'), fg='black', bg='white', relief=FLAT, command=self.MenuBar).place(x=500,y=280)
        self.CreateLogin = Button(self.PasswordFrame, text='Create Log In', font=('Comic Sans MS', 12,'underline'), fg='black', bg='white', relief=FLAT, command=self.CreateLogin).place(x=475,y=320)

    def LoginValidate(self):
        Username = self.Username.get()
        Password = self.Password.get()
        ID = Username[9:]

        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT USERNAME, PASSWORD FROM VOLUNTEERS WHERE VOLUNTEERID = %s' % (ID));
        login = cursor.fetchall()[0]

        if Username == login[0] and Password == login[1]:
            self.MenuBar()
        else:
            Label(self.PasswordFrame, text='Error!', fg='red', bg='white', font=('ariel',12)).place(x=500, y=400)

    def CreateLogin(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title ("Appointment System")
        self.CreateLoginFrame = Frame(self.master)
        self.CreateLoginFrame.pack()

        background = Canvas(self.CreateLoginFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,55, image=photo)
        background.create_text(500, 50, text='Create Log In', font=('comic sans ms',50), fill='violetred4')
      
        self.Username = StringVar()
        self.Password = StringVar()
        self.ReEnterPassword = StringVar()

        self.info = Label(self.CreateLoginFrame, text="Your Username is 'VOLUNTEER' followed by your record ID", fg='violetred4', bg='white', font=('ariel',12)).place(x=290, y=160)
        self.Username_Text= Label(self.CreateLoginFrame, text= "Username: ", fg='black', bg='white', font=('ariel',12)).place(x=350, y=200)
        self.Username_Data= Entry(self.CreateLoginFrame, width = 20, font=('ariel',12), bg='grey88', textvariable = self.Username).place(x=450,y=200)
        self.Password_Text= Label(self.CreateLoginFrame, text= "Password: ", fg='black', bg='White', font=('ariel',12)).place(x=350, y=240)
        self.Password_Data= Entry(self.CreateLoginFrame, width = 20, font=('ariel',12), bg='grey88', show="*", textvariable = self.Password).place(x=450,y=240)
        self.ReEnterPassword_Text= Label(self.CreateLoginFrame, text= "Re-Enter Password: ", fg='black', bg='White', font=('ariel',12)).place(x=285, y=280)
        self.ReEnterPassword_Data= Entry(self.CreateLoginFrame, width = 20, font=('ariel',12), bg='grey88', show="*", textvariable = self.ReEnterPassword).place(x=450,y=280)

        self.Login = Button(self.CreateLoginFrame, text='Create', font=('Comic Sans MS', 12,'underline'), fg='black', bg='white', relief=FLAT, command=self.CreateLoginValidate).place(x=500,y=320)
        self.Back = Button(self.CreateLoginFrame, text='Back', font=('Comic Sans MS', 12,'underline'), fg='black', bg='white', relief=FLAT, command=self.PasswordMenu).place(x=510,y=390)

    def CreateLoginValidate(self):
        try:
            self.Error.destroy()
        except:
            pass
        username = self.Username.get()
        password = self.Password.get()
        password2 = self.ReEnterPassword.get()

        ID = self.TotalID()
        database = sqlite3.connect('Appointments.db')

        if username == '':
            self.Error = Label(self.CreateLoginFrame, text="ERROR! Username wasn't entered", fg='red', bg='white', font=('ariel',12)).place(x=400, y=360)
        elif len(username) < 9:
            self.Error = Label(self.CreateLoginFrame, text='ERROR! Incorrect format for username', fg='red', bg='white', font=('ariel',12)).place(x=390, y=360)
        elif username[9:].isdigit() == FALSE:
            self.Error = Label(self.CreateLoginFrame, text="ERROR! ID isn't a digit", fg='red', bg='white', font=('ariel',12)).place(x=440, y=360)
        elif username[:9] != 'VOLUNTEER':
            self.Error = Label(self.CreateLoginFrame, text='ERROR! Incorrect format for username', fg='red', bg='white', font=('ariel',12)).place(x=390, y=360)
        elif int(username[9:]) > ID:
            self.Error = Label(self.CreateLoginFrame, text='ERROR! Incorrect ID', fg='red', bg='white', font=('ariel',12)).place(x=460, y=360)
        elif password != password2:
            self.Error = Label(self.CreateLoginFrame, text="ERROR! Passwords don't match", fg='red', bg='white', font=('ariel',12)).place(x=410, y=360)
        else:
            database.execute("UPDATE VOLUNTEERS set USERNAME = ? where VOLUNTEERID = ?", (username,username[9:]));
            database.commit()
            database.execute("UPDATE VOLUNTEERS set PASSWORD = ? where VOLUNTEERID = ?", (password,username[9:]));
            database.commit()
            self.PasswordMenu()

    def MenuBar(self):
        OptionsMenu = Menu(self.menubar, tearoff=FALSE)
        OptionsMenu.add_command(label="Set Up Database", command=self.SetUpDatabase)
        OptionsMenu.add_command(label="Set Up Tables", command=self.SetUpTables)
        OptionsMenu.add_command(label="Change Password", command=self.ChangePassword)
        OptionsMenu.add_separator()
        OptionsMenu.add_command(label="Log Out", command=self.LogOut)
        OptionsMenu.add_command(label="Exit", command=self.Exit)
        self.menubar.add_cascade(label="Options", menu=OptionsMenu)

        VolunteerMenu = Menu(self.menubar, tearoff=FALSE)
        VolunteerMenu.add_command(label="Add New Volunteer", command=self.AddVolunteer)
        VolunteerMenu.add_command(label="Search Volunteers", command=self.SearchVolunteer)
        VolunteerMenu.add_command(label="Update Volunteer Information", command=self.UpdateVolunteer)
        VolunteerMenu.add_command(label="Display All Volunteers", command=self.DisplayAllVolunteers)
        VolunteerMenu.add_command(label="Delete Volunteer", command=self.DeleteVolunteer)
        self.menubar.add_cascade(label="Volunteers", menu=VolunteerMenu)

        ServiceUserMenu = Menu(self.menubar, tearoff=FALSE)
        ServiceUserMenu.add_command(label="Add New Service User", command=self.AddServiceUser)
        ServiceUserMenu.add_command(label="Search Service Users", command=self.SearchServiceUser)
        ServiceUserMenu.add_command(label="Update Service Users Information", command=self.UpdateServiceUser)
        ServiceUserMenu.add_command(label="Display All Service Users", command=self.DisplayAllServiceUsers)
        ServiceUserMenu.add_command(label="Delete Service User", command=self.DeleteServiceUser)
        self.menubar.add_cascade(label="Service Users", menu=ServiceUserMenu)

        TransportMenu = Menu(self.menubar, tearoff=FALSE)
        TransportMenu.add_command(label="Add Transport Appointment", command=self.AddAppointment)
        TransportMenu.add_command(label="Search Appointments", command=self.SearchAppointments)
        TransportMenu.add_command(label="Update Appointment", command=self.UpdateAppointment)
        TransportMenu.add_command(label="Display All Appointments", command=self.DisplayAllAppointments)
        TransportMenu.add_command(label="Delete Apppointment", command=self.DeleteAppointments)
        TransportMenu.add_separator()
        TransportMenu.add_command(label="ExpensesForm", command=self.ExpensesForm)
        self.menubar.add_cascade(label="Transport Appointment", menu=TransportMenu)

        LunchClubMenu = Menu(self.menubar, tearoff=FALSE)
        LunchClubMenu.add_command(label='Add Lunch Club', command=self.AddLunchClub)
        LunchClubMenu.add_command(label='Search Lunch Club', command=self.DisplayLunchClub)
        LunchClubMenu.add_command(label='Update Lunch Club', command=self.UpdateLunchClub)
        LunchClubMenu.add_command(label='All Lunch Clubs', command=self.AllLunchClubs)
        LunchClubMenu.add_command(label='Delete Lunch Club', command=self.DeleteLunchClub)
        self.menubar.add_cascade(label='Lunch Club', menu=LunchClubMenu)

        self.master.config(menu=self.menubar)
        self.MainMenu()
        
    def MainMenu(self):
        self.ClearWindow()
        self.master.title('Appointment System')
        self.MainMenuFrame = Frame(self.master)
        self.MainMenuFrame.pack()

        background = Canvas(self.MainMenuFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 220, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(100,100, image=photo)

        background.create_text(500, 50, text='Main Menu', font=('comic sans ms',50), fill='violetred4')

    def SetUpDatabase(self):
        database = sqlite3.connect('Appointments.db')
        database.close()

    def SetUpTables(self):
        database = sqlite3.connect('Appointments.db')

        try:
            database.execute('''CREATE TABLE VOLUNTEERS
                               (VOLUNTEERID INTEGER PRIMARY KEY AUTOINCREMENT,
                                FIRST_NAME           TEXT           NOT NULL,
                                LAST_NAME            TEXT           NOT NULL,
                                DATE_OF_BIRTH        TEXT           NOT NULL,
                                ADDRESS              TEXT           NOT NULL,
                                POSTCODE             TEXT           NOT NULL,
                                MOBILE_NUMBER        TEXT,
                                TELEPHONE_NUMBER     TEXT           NOT NULL,
                                EMAIL                TEXT,
                                PROVIDE_TRANSPORT    TEXT           NOT NULL,
                                JOBS_THEY_CARRY_OUT  TEXT           NOT NULL,
                                USERNAME             TEXT,
                                PASSWORD             TEXT);''')
        except:
            pass

        try:
            database.execute('''CREATE TABLE SERVICE_USERS
                               (SERVICE_USERID INTEGER PRIMARY KEY AUTOINCREMENT,
                                FIRST_NAME           TEXT           NOT NULL,
                                LAST_NAME            TEXT           NOT NULL,
                                DATE_OF_BIRTH        TEXT           NOT NULL,
                                ADDRESS              TEXT           NOT NULL,
                                POSTCODE             TEXT           NOT NULL,
                                MOBILE_NUMBER        TEXT,
                                TELEPHONE_NUMBER     TEXT           NOT NULL,
                                EMAIL                TEXT,
                                MEDICAL_INFORMATION  TEXT           NOT NULL,
                                CLUBS_THEY_ATTEND    TEXT,
                                TRANSPORT_REQUIRED   TEXT           NOT NULL);''')
        except:
            pass

        try:
            database.execute('''CREATE TABLE APPOINTMENTS
                               (APPOINTMENTID INTEGER PRIMARY KEY NOT NULL,
                                VOLUNTEERID INTEGER NOT NULL,
                                SERVICE_USERID INTEGER NOT NULL,
                                DATE_OF_APPOINTMENT TEXT NOT NULL,
                                TIME_OF_APPOINTMENT TEXT NOT NULL,
                                START_LOCATION TEXT NOT NULL,
                                DESTINATION TEXT NOT NULL,
                                EXPENSES_PAID TEXT NOT NULL,
                                FOREIGN KEY(VOLUNTEERID) REFERENCES VOLUNTEERS(VOLUNTEERID),
                                FOREIGN KEY(SERVICE_USERID) REFERENCES SERVICE_USERS(SERVICE_USERID));''')

        except:
            pass

        try:
            database.execute('''CREATE TABLE LUNCH_CLUBS
                               (LUNCH_CLUBID    INTEGER  PRIMARY KEY NOT NULL,
                                VOLUNTEERID      INTEGER  NOT NULL,
                                SERVICE_USERID   INTEGER  NOT NULL,
                                DATE_OF_CLUB     TEXT     NOT NULL,
                                TIME_OF_CLUB     TEXT     NOT NULL,
                                COST             TEXT     NOT NULL,
                                FOREIGN KEY(VOLUNTEERID) REFERENCES VOLUNTEERS(VOLUNTEERID),
                                FOREIGN KEY(SERVICE_USERID) REFERENCES SERVICE_USERS(SERVICE_USERID));''')
        except:
            pass

        database.close()

##
##
##
##
##
##
##
##
##
##
##
##

    def AddVolunteer(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Add Volunteer')

        self.AddVolunteerFrame = Frame(self.master)
        self.AddVolunteerFrame.pack()

        background = Canvas(self.AddVolunteerFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Add Volunteer', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)

        self.Firstname = StringVar()
        self.Lastname = StringVar()
        self.Day = StringVar()
        self.Month = StringVar()
        self.Year = StringVar()
        self.Address = StringVar()
        self.Postcode = StringVar()
        self.MobileNo = StringVar()
        self.TelephoneNo = StringVar()
        self.Email = StringVar()
        self.ProvideTransport = StringVar()
        self.JobOption1 = IntVar()
        self.JobOption2 = IntVar()
        self.JobOption3 = IntVar()
        self.JobOption4 = IntVar()
        self.JobOption5 = IntVar()

        self.FirstnameText = Label(self.AddVolunteerFrame, text='Forenames:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=200)
        self.FirstnameEntry = Entry(self.AddVolunteerFrame, width=25, font=('ariel',10), bg='grey88', textvariable=self.Firstname).place(x=120,y=200)
        self.LastnameText = Label(self.AddVolunteerFrame, text='Surname:', fg='black', bg='white', font=('ariel',10)).place(x=330,y=200)
        self.LastnameEntry = Entry(self.AddVolunteerFrame, width=20, font=('ariel',10), bg='grey88', textvariable=self.Lastname).place(x=400,y=200)
        self.DateofBirthText = Label(self.AddVolunteerFrame, text='Date of Birth:', fg='black', bg='white', font=('ariel',10)).place(x=20,y=230)
        self.DateofBirthDay =  Entry(self.AddVolunteerFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Day).place(x=120,y=230)
        self.Divide = Label(self.AddVolunteerFrame, text='/', fg='black', bg='white', font=('ariel',12)).place(x=140, y=230)
        self.DateofBirthMonth =  Entry(self.AddVolunteerFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Month).place(x=155,y=230)
        self.Divide = Label(self.AddVolunteerFrame, text='/', fg='black', bg='white', font=('ariel',12)).place(x=175, y=230)
        self.DateofBirthYear =  Entry(self.AddVolunteerFrame, width=4, font=('ariel',10), bg='grey88', textvariable=self.Year).place(x=190,y=230)
        self.AddressText = Label(self.AddVolunteerFrame, text='Address:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=260)
        self.AddressEntry = Entry(self.AddVolunteerFrame, width=60, font=('ariel',10), bg='grey88', textvariable=self.Address).place(x=120, y=260)
        self.PostcodeText = Label(self.AddVolunteerFrame, text='Postcode:', fg='black', bg='white', font=('Ariel',10)).place(x=20,y=285)
        self.PostcodeEntry = Entry(self.AddVolunteerFrame, width=10, font=('ariel',10), bg='grey88', textvariable=self.Postcode).place(x=120,y=285)
        self.MobileNumberText = Label(self.AddVolunteerFrame, text='Mobile Number:', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=320)
        self.MobileNumberEntry = Entry(self.AddVolunteerFrame, width=15, font=('ariel',10), bg='grey88', textvariable=self.MobileNo).place(x=120, y=320)
        self.TelephoneNumberText = Label(self.AddVolunteerFrame, text='Telephone Number:', fg='black', bg='white', font=('Ariel',10)).place(x=250,y=320)
        self.TelephoneNumberEntry = Entry(self.AddVolunteerFrame, width=15, font=('ariel',10), bg='grey88', textvariable=self.TelephoneNo).place(x=375,y=320)
        self.EmailText = Label(self.AddVolunteerFrame, text='Email:', fg='black', bg='white', font=('Ariel',10)).place(x=20,y=350)
        self.EmailEntry = Entry(self.AddVolunteerFrame, width=40, font=('ariel',10), bg='grey88', textvariable=self.Email).place(x=120,y=350)
        self.ProvideTransportText = Label(self.AddVolunteerFrame, text='Can Provide Transport?', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=380)
        self.ProvideTransport.set('Select...')
        self.ProvideTransportEntry = OptionMenu(self.AddVolunteerFrame, self.ProvideTransport, 'Yes', 'No').place(x=175,y=380)
        self.JobsText = Label(self.AddVolunteerFrame, text='Jobs They Carry Out:', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=430)
        self.JobOption1Text = Checkbutton(self.AddVolunteerFrame, text='Driver', font=('ariel',10), bg='white', variable=self.JobOption1).place(x=150,y=430)
        self.JobOption2Text = Checkbutton(self.AddVolunteerFrame, text='Lunch Club', font=('ariel',10), bg='white', variable=self.JobOption2).place(x=150,y=450)
        self.JobOption3Text = Checkbutton(self.AddVolunteerFrame, text='Office', font=('ariel',10), bg='white', variable=self.JobOption3).place(x=150,y=470)
        self.JobOption4Text = Checkbutton(self.AddVolunteerFrame, text='Befriender', font=('ariel',10), bg='white', variable=self.JobOption4).place(x=150,y=490)
        self.JobOption5Text = Checkbutton(self.AddVolunteerFrame, text='Fundraiser', font=('ariel',10), bg='white', variable=self.JobOption5).place(x=150,y=510)

        self.SubmitButton = Button(self.AddVolunteerFrame, text='Submit Form', font=('comic sans ms',12), bg='darkseagreen3', fg='white', command=self.SubmitVolunteer).place(x=250, y=540)

    def SubmitVolunteer(self):
        ID = self.TotalID()
        ID +=1
        firstname = self.Firstname.get()
        lastname = self.Lastname.get()
        dateofbirth = self.Day.get() + '/' + self.Month.get() + '/' + self.Year.get()
        address = self.Address.get()
        postcode = self.Postcode.get()
        mobileno = self.MobileNo.get()
        telephoneno = self.TelephoneNo.get()
        email = self.Email.get()
        providetransport = self.ProvideTransport.get()
        job1 = self.JobOption1.get()
        job2 = self.JobOption2.get()
        job3 = self.JobOption3.get()
        job4 = self.JobOption4.get()
        job5 = self.JobOption5.get()

        jobscarriedoutlist = []
        if job1 == 1:
            jobscarriedoutlist.append('Driver')
        if job2 == 1:
            jobscarriedoutlist.append('Lunch Club')
        if job3 == 1:
            jobscarriedoutlist.append('Office')
        if job4 == 1:
            jobscarriedoutlist.append('Befriender')
        if job5 == 1:
            jobscarriedoutlist.append('Fundraiser')


        jobscarriedout = ', '.join(jobscarriedoutlist)

        database = sqlite3.connect('Appointments.db')
        database.execute('INSERT INTO VOLUNTEERS (VOLUNTEERID, FIRST_NAME,LAST_NAME,DATE_OF_BIRTH,ADDRESS,POSTCODE,MOBILE_NUMBER,TELEPHONE_NUMBER,EMAIL,PROVIDE_TRANSPORT,JOBS_THEY_CARRY_OUT) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (ID, firstname, lastname, dateofbirth, address, postcode, mobileno, telephoneno, email, providetransport, jobscarriedout));
        database.commit()

        self.Firstname.set('')
        self.Lastname.set('')
        self.Day.set('')
        self.Month.set('')
        self.Year.set('')
        self.Address.set('')
        self.Postcode.set('')
        self.MobileNo.set('')
        self.TelephoneNo.set('')
        self.Email.set('')
        self.ProvideTransport.set('')
        self.JobOption1.set(0)
        self.JobOption2.set(0)
        self.JobOption3.set(0)
        self.JobOption4.set(0)
        self.JobOption5.set(0)

    def SearchVolunteer(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Add Appointment')

        self.SearchVolunteerFrame = Frame(self.master)
        self.SearchVolunteerFrame.pack()

        background = Canvas(self.SearchVolunteerFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        background.create_line(0,250,1000,250, fill='black')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Search Volunteers', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)

        MaxID = self.TotalID()

        self.VolunteerID = StringVar()
        self.VolunteerIDText = Label(self.SearchVolunteerFrame, text='Volunteer ID:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=200)
        self.VolunteerIDEntry = Spinbox(self.SearchVolunteerFrame, width = 4, from_=0, to=MaxID, relief=FLAT, bg='grey88', textvariable = self.VolunteerID, command=self.DisplaySearchVolunteers).place(x=110, y=200)


    def DisplaySearchVolunteers(self):
        try:
            self.firstname.set('')
        except:
            pass
        try:
            self.lastname.set('')
        except:
            pass
        try:
            self.date_of_birth.set('')
        except:
            pass
        try:
            self.address.set('')
        except:
            pass
        try:
            self.postcode.set('')
        except:
            pass
        try:
            self.mobileno.set('')
        except:
            pass
        try:
            self.telephoneno.set('')
        except:
            pass
        try:
            self.email.set('')
        except:
            pass
        try:
            self.providetransport.set('')
        except:
            pass
        try:
            self.jobs_carried_out.set('')
        except:
            pass
        
        ID = self.VolunteerID.get()
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.date_of_birth = StringVar()
        self.address = StringVar()
        self.postcode = StringVar()
        self.mobileno = StringVar()
        self.telephoneno = StringVar()
        self.email = StringVar()
        self.providetransport = StringVar()
        self.jobs_carried_out = StringVar()

        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT * FROM VOLUNTEERS WHERE VOLUNTEERID = %s' % (ID));
        information = cursor.fetchall()[0]
        self.firstname.set(information[1])
        self.lastname.set(information[2])
        self.date_of_birth.set(information[3])
        self.address.set(information[4])
        self.postcode.set(information[5])
        self.mobileno.set(information[6])
        self.telephoneno.set(information[7])
        self.email.set(information[8])
        self.providetransport.set(information[9])
        self.jobs_carried_out.set(information[10])

        self.FirstnameText = Label(self.SearchVolunteerFrame, text='Forenames:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=280)
        self.FirstnameEntry = Label(self.SearchVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.firstname).place(x=175,y=280)
        self.LastnameText = Label(self.SearchVolunteerFrame, text='Surname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=380,y=280)
        self.LastnameEntry = Label(self.SearchVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.lastname).place(x=500,y=280)
        self.DateofBirthText = Label(self.SearchVolunteerFrame, text='Date of Birth:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20,y=310)
        self.DateofBirthEntry = Label(self.SearchVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.date_of_birth).place(x=175,y=310)
        self.AddressText = Label(self.SearchVolunteerFrame, text='Address:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=340)
        self.AddressEntry = Label(self.SearchVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.address).place(x=175, y=340)
        self.PostcodeText = Label(self.SearchVolunteerFrame, text='Postcode:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=370)
        self.PostcodeEntry = Label(self.SearchVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.postcode).place(x=175,y=370)
        self.MobileNumberText = Label(self.SearchVolunteerFrame, text='Mobile Number:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=400)
        self.MobileNumberEntry = Label(self.SearchVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.mobileno).place(x=175, y=400)
        self.TelephoneNumberText = Label(self.SearchVolunteerFrame, text='Telephone Number:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=380,y=400)
        self.TelephoneNumberEntry = Label(self.SearchVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.telephoneno).place(x=500,y=400)
        self.EmailText = Label(self.SearchVolunteerFrame, text='Email:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=430)
        self.EmailEntry = Label(self.SearchVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.email).place(x=175,y=430)
        self.ProvideTransportText = Label(self.SearchVolunteerFrame, text='Can Provide Transport?', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=460)
        self.ProvideTransportEntry = Label(self.SearchVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.providetransport).place(x=175,y=460)
        self.JobsText = Label(self.SearchVolunteerFrame, text='Jobs They Carry Out:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=490)
        self.JobsEntry = Label(self.SearchVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.jobs_carried_out).place(x=175,y=490)

    def UpdateVolunteer(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Update Volunteer')

        self.UpdateVolunteerFrame = Frame(self.master)
        self.UpdateVolunteerFrame.pack()

        background = Canvas(self.UpdateVolunteerFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Update Volunteer', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)

        MaxID = self.TotalID()

        self.VolunteerID = StringVar()
        self.VolunteerData = StringVar()
        
        self.VolunteerIDText = Label(self.UpdateVolunteerFrame, text='Volunteer ID:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=200)
        self.VolunteerIDEntry = Spinbox(self.UpdateVolunteerFrame, width = 4, from_=0, to=MaxID, relief=FLAT, bg='grey88', textvariable = self.VolunteerID).place(x=110, y=200)

        self.VolunteerDataText = Label(self.UpdateVolunteerFrame, text='What would you like to update:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=240)
        self.VolunteerData.set('Select...')
        self.VolunteerDataEntry = OptionMenu(self.UpdateVolunteerFrame, self.VolunteerData, 'Firstname', 'Surname', 'Date of Birth', 'Address', 'Postcode', 'Mobile Number', 'Telephone Number', 'Email', 'Provide Transport', 'Jobs They Carry Out').place(x=210,y=240)

        self.selectbutton123 = Button(self.UpdateVolunteerFrame, text='Select', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.UpdateVolunteer2).place(x=380, y=240)

    def UpdateVolunteer2(self):
        self.selectbutton123 = Button(self.UpdateVolunteerFrame, text='Select', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, state = DISABLED).place(x=380, y=240)
        Data = self.VolunteerData.get()

        self.Var = StringVar()
        self.Var2 = StringVar()
        self.Var3 = StringVar()
        self.Var4 = IntVar()
        self.Var5 = IntVar()
        self.Var6 = IntVar()
        self.Var7 = IntVar()
        self.Var8 = IntVar()

        self.DataLabel = Label(self.UpdateVolunteerFrame, text='What would you like to change it to?', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=280)

        if Data == 'Firstname':
            self.Label = Label(self.UpdateVolunteerFrame, text='Forenames:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=320)
            self.Entry = Entry(self.UpdateVolunteerFrame, width=25, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=120,y=320)
        elif Data == 'Surname':
            self.Label = Label(self.UpdateVolunteerFrame, text='Surname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20,y=320)
            self.Entry = Entry(self.UpdateVolunteerFrame, width=20, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=120,y=320)
        elif Data == 'Date of Birth':
            self.Label = Label(self.UpdateVolunteerFrame, text='Date of Birth:', fg='black', bg='white', font=('ariel',10)).place(x=20,y=320)
            self.Entry =  Entry(self.UpdateVolunteerFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=120,y=320)
            self.Divide = Label(self.UpdateVolunteerFrame, text='/', fg='black', bg='white', font=('ariel',12)).place(x=140, y=320)
            self.Entry2 =  Entry(self.UpdateVolunteerFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Var2).place(x=155,y=320)
            self.Divide = Label(self.UpdateVolunteerFrame, text='/', fg='black', bg='white', font=('ariel',12)).place(x=175, y=320)
            self.Entry3 =  Entry(self.UpdateVolunteerFrame, width=4, font=('ariel',10), bg='grey88', textvariable=self.Var3).place(x=190,y=320)
        elif Data == 'Address':
            self.Label = Label(self.UpdateVolunteerFrame, text='Address:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=320)
            self.Entry = Entry(self.UpdateVolunteerFrame, width=60, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=120, y=320)
        elif Data == 'Postcode':
            self.Label = Label(self.UpdateVolunteerFrame, text='Postcode:', fg='black', bg='white', font=('Ariel',10)).place(x=20,y=320)
            self.Entry = Entry(self.UpdateVolunteerFrame, width=10, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=120,y=320)
        elif Data == 'Mobile Number':
            self.Label = Label(self.UpdateVolunteerFrame, text='Mobile Number:', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=320)
            self.Entry = Entry(self.UpdateVolunteerFrame, width=15, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=120, y=320)
        elif Data == 'Telephone Number':
            self.Label = Label(self.UpdateVolunteerFrame, text='Telephone Number:', fg='black', bg='white', font=('Ariel',10)).place(x=20,y=320)
            self.Entry = Entry(self.UpdateVolunteerFrame, width=15, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=150,y=320)
        elif Data == 'Email':
            self.Label = Label(self.UpdateVolunteerFrame, text='Email:', fg='black', bg='white', font=('Ariel',10)).place(x=20,y=320)
            self.Entry = Entry(self.UpdateVolunteerFrame, width=40, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=120,y=320)
        elif Data == 'Provide Transport':
            self.Label = Label(self.UpdateVolunteerFrame, text='Can Provide Transport?', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=320)
            self.Var.set('Select...')
            self.Entry = OptionMenu(self.UpdateVolunteerFrame, self.Var, 'Yes', 'No').place(x=175,y=320)
        elif Data == 'Jobs They Carry Out':
            self.Label = Label(self.UpdateVolunteerFrame, text='Jobs They Carry Out:', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=320)
            self.Entry = Checkbutton(self.UpdateVolunteerFrame, text='Driver', font=('ariel',10), bg='white', variable=self.Var4).place(x=150,y=320)
            self.Entry2 = Checkbutton(self.UpdateVolunteerFrame, text='Lunch Club', font=('ariel',10), bg='white', variable=self.Var5).place(x=150,y=340)
            self.Entry3 = Checkbutton(self.UpdateVolunteerFrame, text='Office', font=('ariel',10), bg='white', variable=self.Var6).place(x=150,y=360)
            self.Entry4 = Checkbutton(self.UpdateVolunteerFrame, text='Befriender', font=('ariel',10), bg='white', variable=self.Var7).place(x=150,y=380)
            self.Entry5 = Checkbutton(self.UpdateVolunteerFrame, text='Fundraiser', font=('ariel',10), bg='white', variable=self.Var8).place(x=150,y=400)

        updatebutton = Button(self.UpdateVolunteerFrame, text='Update', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.UpdateVolunteer3).place(x=20, y=440)

    def UpdateVolunteer3(self):
        database = sqlite3.connect('Appointments.db')
        self.IDupdate = self.VolunteerID.get()
        Data = self.VolunteerData.get()
        Var = self.Var.get()
        Var2 = self.Var2.get()
        Var3 = self.Var3.get()
        Var4 = self.Var4.get()
        Var5 = self.Var5.get()
        Var6 = self.Var6.get()
        Var7 = self.Var7.get()
        Var8 = self.Var8.get()
        
        if Data == 'Firstname':
            database.execute("UPDATE VOLUNTEERS SET FIRST_NAME = ? WHERE VOLUNTEERID = ?", (Var,self.IDupdate));
            database.commit()
        elif Data == 'Surname':
            database.execute('UPDATE VOLUNTEERS SET LAST_NAME = ? WHERE VOLUNTEERID = ?', (Var,self.IDupdate));
            database.commit()
        elif Data == 'Date of Birth':
            dateofbirth = Var + '/' + Var2 + '/' + Var3
            database.execute('UPDATE VOLUNTEERS SET DATE_OF_BIRTH = ? WHERE VOLUNTEERID = ?', (dateofbirth,self.IDupdate));
            database.commit()
        elif Data == 'Address':
            database.execute('UPDATE VOLUNTEERS SET ADDRESS = ? WHERE VOLUNTEERID = ?', (Var,self.IDupdate));
            database.commit()
        elif Data == 'Postcode':
            database.execute('UPDATE VOLUNTEERS SET POSTCODE = ? WHERE VOLUNTEERID = ?', (Var,self.IDupdate));
            database.commit()
        elif Data == 'Mobile Number':
            database.execute('UPDATE VOLUNTEERS SET MOBILE_NUMBER = ? WHERE VOLUNTEERID = ?', (Var,self.IDupdate));
            database.commit()
        elif Data == 'Telephone Number':
            database.execute('UPDATE VOLUNTEERS SET TELEPHONE_NUMBER = ? WHERE VOLUNTEERID = ?', (Var,self.IDupdate));
            database.commit()
        elif Data == 'Email':
            database.execute('UPDATE VOLUNTEERS SET EMAIL = ? WHERE VOLUNTEERID = ?', (Var,self.IDupdate));
            database.commit()
        elif Data == 'Provide Transport':
            database.execute('UPDATE VOLUNTEERS SET PROVIDE_TRANSPORT = ? WHERE VOLUNTEERID = ?', (Var,self.IDupdate));
            database.commit()
        elif Data == 'Jobs They Carry Out':
            jobscarriedoutlist = []
            if self.Var4.get() == 1:
                jobscarriedoutlist.append('Driver')
            if self.Var5.get() == 1:
                jobscarriedoutlist.append('Lunch Club')
            if self.Var6.get() == 1:
                jobscarriedoutlist.append('Office')
            if self.Var7.get() == 1:
                jobscarriedoutlist.append('Befriender')
            if self.Var8.get() == 1:
                jobscarriedoutlist.append('Fundraiser')
                
            jobscarriedout = ','.join(jobscarriedoutlist)
            database.execute('UPDATE VOLUNTEERS SET JOBS_THEY_CARRY_OUT = ? WHERE VOLUNTEERID = ?', (jobscarriedout,self.IDupdate));
            database.commit()

        self.VolunteerData.set('Select...')
        self.Var.set('')
        self.Var2.set('')
        self.Var3.set('')
        self.Var4.set(0)
        self.Var5.set(0)
        self.Var6.set(0)
        self.Var7.set(0)
        self.Var8.set(0)
        self.VolunteerID.set(0)
        
        self.UpdateVolunteer4()

    def UpdateVolunteer4(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Update Volunteer')

        self.UpdateVolunteerFrame2 = Frame(self.master)
        self.UpdateVolunteerFrame2.pack()

        background = Canvas(self.UpdateVolunteerFrame2, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        background.create_line(0,250,1000,250, fill='black')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Update Volunteer', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)

        self.firstname = StringVar()
        self.lastname = StringVar()
        self.date_of_birth = StringVar()
        self.address = StringVar()
        self.postcode = StringVar()
        self.mobileno = StringVar()
        self.telephoneno = StringVar()
        self.email = StringVar()
        self.providetransport = StringVar()
        self.jobs_carried_out = StringVar()

        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT FIRST_NAME FROM VOLUNTEERS WHERE VOLUNTEERID = ?', (self.IDupdate));
        self.firstname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT LAST_NAME FROM VOLUNTEERS WHERE VOLUNTEERID = ?', (self.IDupdate));
        self.lastname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT DATE_OF_BIRTH FROM VOLUNTEERS WHERE VOLUNTEERID = ?', (self.IDupdate));
        self.date_of_birth.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT ADDRESS FROM VOLUNTEERS WHERE VOLUNTEERID = ?', (self.IDupdate));
        self.address.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT POSTCODE FROM VOLUNTEERS WHERE VOLUNTEERID = ?', (self.IDupdate));
        self.postcode.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT MOBILE_NUMBER FROM VOLUNTEERS WHERE VOLUNTEERID = ?', (self.IDupdate));
        self.mobileno.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT TELEPHONE_NUMBER FROM VOLUNTEERS WHERE VOLUNTEERID = ?', (self.IDupdate));
        self.telephoneno.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT EMAIL FROM VOLUNTEERS WHERE VOLUNTEERID = ?', (self.IDupdate));
        self.email.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT PROVIDE_TRANSPORT FROM VOLUNTEERS WHERE VOLUNTEERID = ?', (self.IDupdate));
        self.providetransport.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT JOBS_THEY_CARRY_OUT FROM VOLUNTEERS WHERE VOLUNTEERID = ?', (self.IDupdate));
        self.jobs_carried_out.set(cursor.fetchall()[0][0])

        self.FirstnameText = Label(self.UpdateVolunteerFrame2, text='Forenames:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=280)
        self.FirstnameEntry = Label(self.UpdateVolunteerFrame2, font=('ariel',10), bg='white', textvariable=self.firstname).place(x=175,y=280)
        self.LastnameText = Label(self.UpdateVolunteerFrame2, text='Surname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=380,y=280)
        self.LastnameEntry = Label(self.UpdateVolunteerFrame2, font=('ariel',10), bg='white', textvariable=self.lastname).place(x=500,y=280)
        self.DateofBirthText = Label(self.UpdateVolunteerFrame2, text='Date of Birth:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20,y=310)
        self.DateofBirthEntry = Label(self.UpdateVolunteerFrame2, font=('ariel',10), bg='white', textvariable=self.date_of_birth).place(x=175,y=310)
        self.AddressText = Label(self.UpdateVolunteerFrame2, text='Address:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=340)
        self.AddressEntry = Label(self.UpdateVolunteerFrame2, font=('ariel',10), bg='white', textvariable=self.address).place(x=175, y=340)
        self.PostcodeText = Label(self.UpdateVolunteerFrame2, text='Postcode:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=370)
        self.PostcodeEntry = Label(self.UpdateVolunteerFrame2, font=('ariel',10), bg='white', textvariable=self.postcode).place(x=175,y=370)
        self.MobileNumberText = Label(self.UpdateVolunteerFrame2, text='Mobile Number:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=400)
        self.MobileNumberEntry = Label(self.UpdateVolunteerFrame2, font=('ariel',10), bg='white', textvariable=self.mobileno).place(x=175, y=400)
        self.TelephoneNumberText = Label(self.UpdateVolunteerFrame2, text='Telephone Number:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=380,y=400)
        self.TelephoneNumberEntry = Label(self.UpdateVolunteerFrame2, font=('ariel',10), bg='white', textvariable=self.telephoneno).place(x=500,y=400)
        self.EmailText = Label(self.UpdateVolunteerFrame2, text='Email:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=430)
        self.EmailEntry = Label(self.UpdateVolunteerFrame2, font=('ariel',10), bg='white', textvariable=self.email).place(x=175,y=430)
        self.ProvideTransportText = Label(self.UpdateVolunteerFrame2, text='Can Provide Transport?', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=460)
        self.ProvideTransportEntry = Label(self.UpdateVolunteerFrame2, font=('ariel',10), bg='white', textvariable=self.providetransport).place(x=175,y=460)
        self.JobsText = Label(self.UpdateVolunteerFrame2, text='Jobs They Carry Out:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=490)
        self.JobsEntry = Label(self.UpdateVolunteerFrame2, font=('ariel',10), bg='white', textvariable=self.jobs_carried_out).place(x=175,y=490)

    def DisplayAllVolunteers(self):
        self.ClearWindow()
        self.master.geometry("1000x600")
        self.master.title("Display All Volunteers")

        self.DisplayAllVolunteersFrame = Frame(self.master)
        self.DisplayAllVolunteersFrame.pack()
        self.DisplayAllVolunteersFrame.grid_rowconfigure(0, weight=1)
        self.DisplayAllVolunteersFrame.grid_columnconfigure(0, weight=1)

        xscrollbar = Scrollbar(self.DisplayAllVolunteersFrame, orient=HORIZONTAL)
        xscrollbar.grid(row=1, column=0, sticky=E+W)
        yscrollbar = Scrollbar(self.DisplayAllVolunteersFrame)
        yscrollbar.grid(row=0, column=1, sticky=N+S)
        
        background = Canvas(self.DisplayAllVolunteersFrame, width=1000, height=600, scrollregion=(0, 0, 2500, 1000),
                xscrollcommand=xscrollbar.set,
                yscrollcommand=yscrollbar.set)

        xscrollbar.config(command=background.xview)
        yscrollbar.config(command=background.yview)

        background.create_rectangle(0, 0, 2500, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 2500, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 2500, 1000, fill="white", outline='white')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Displaying All Volunteers', font=('comic sans ms',50), fill='violetred4')
        background.create_window(60,130, window=Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu))

        background.grid(row=0, column=0, sticky=N+S+E+W)

        background.create_text(50,165, text='Volunteer ID', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(230,165, text='Forenames', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(440,165, text='Surname', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(610,165, text='Date of Birth', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(920,165, text='Address', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(1210,165, text='Postcode', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(1380,165, text='Mobile Number', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(1530,165, text='Telephone Number', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(1770,165, text='Email', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(2020,165, text='Can Provide Transport?', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(2300,165, text='Jobs They Carry Out', fill='violetred4', font=('Ariel',11,'underline'))


        VIDTotal = self.TotalID()
        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT FIRST_NAME FROM VOLUNTEERS');
        firstname = cursor.fetchall()
        cursor.execute('SELECT LAST_NAME FROM VOLUNTEERS');
        lastname = cursor.fetchall()
        cursor.execute('SELECT DATE_OF_BIRTH FROM VOLUNTEERS');
        dateofbirth = cursor.fetchall()
        cursor.execute('SELECT ADDRESS FROM VOLUNTEERS');
        address = cursor.fetchall()
        cursor.execute('SELECT POSTCODE FROM VOLUNTEERS');
        postcode = cursor.fetchall()
        cursor.execute('SELECT MOBILE_NUMBER FROM VOLUNTEERS');
        mobileno = cursor.fetchall()
        cursor.execute('SELECT TELEPHONE_NUMBER FROM VOLUNTEERS');
        telephoneno = cursor.fetchall()
        cursor.execute('SELECT EMAIL FROM VOLUNTEERS');
        email = cursor.fetchall()
        cursor.execute('SELECT PROVIDE_TRANSPORT FROM VOLUNTEERS');
        providetransport = cursor.fetchall()
        cursor.execute('SELECT JOBS_THEY_CARRY_OUT FROM VOLUNTEERS');
        jobs = cursor.fetchall()
        

        yvalue=190
        for a in range(1,(VIDTotal+1)):
            background.create_text(50,yvalue, font=('ariel',10), fill='black', text=a)
            yvalue += 20
        
        yvalue=190
        i=0
        for a in range(0,VIDTotal):
            vfirstname = firstname[i][0]
            background.create_text(230,yvalue, font=('ariel',10), fill='black', text=vfirstname)
            i += 1
            yvalue += 20

        yvalue=190
        i=0
        for a in range(0,VIDTotal):
            vlastname = lastname[i][0]
            background.create_text(440,yvalue, font=('ariel',10), fill='black', text=vlastname)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,VIDTotal):
            vdateofbirth = dateofbirth[i][0]
            background.create_text(610,yvalue, font=('ariel',10), fill='black', text=vdateofbirth)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,VIDTotal):
            vaddress = address[i][0]
            background.create_text(920,yvalue, font=('ariel',10), fill='black', text=vaddress)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,VIDTotal):
            vpostcode = postcode[i][0]
            background.create_text(1210,yvalue, font=('ariel',10), fill='black', text=vpostcode)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,VIDTotal):
            vmobileno = mobileno[i][0]
            background.create_text(1380,yvalue, font=('ariel',10), fill='black', text=vmobileno)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,VIDTotal):
            vtelephoneno = telephoneno[i][0]
            background.create_text(1530,yvalue, font=('ariel',10), fill='black', text=vtelephoneno)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,VIDTotal):
            vemail = email[i][0]
            background.create_text(1770,yvalue, font=('ariel',10), fill='black', text=vemail)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,VIDTotal):
            vprovidetransport = providetransport[i][0]
            background.create_text(2020,yvalue, font=('ariel',10), fill='black', text=vprovidetransport)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,VIDTotal):
            vjobs = jobs[i][0]
            background.create_text(2300,yvalue, font=('ariel',10), fill='black', text=vjobs)
            i += 1
            yvalue += 20


    def DeleteVolunteer(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Delete Volunteer')

        self.DeleteVolunteerFrame = Frame(self.master)
        self.DeleteVolunteerFrame.pack()

        background = Canvas(self.DeleteVolunteerFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        background.create_line(0,250,1000,250, fill='black')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Delete Volunteer', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)

        MaxID = self.TotalID()

        self.VolunteerID = StringVar()
        self.VolunteerIDText = Label(self.DeleteVolunteerFrame, text='Volunteer ID:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=200)
        self.VolunteerIDEntry = Spinbox(self.DeleteVolunteerFrame, width = 4, from_=0, to=MaxID, relief=FLAT, bg='grey88', textvariable = self.VolunteerID, command=self.DeleteVolunteer2).place(x=110, y=200)

    def DeleteVolunteer2(self):
        try:
            self.firstname.set('')
        except:
            pass
        try:
            self.lastname.set('')
        except:
            pass
        try:
            self.date_of_birth.set('')
        except:
            pass
        try:
            self.address.set('')
        except:
            pass
        try:
            self.postcode.set('')
        except:
            pass
        try:
            self.mobileno.set('')
        except:
            pass
        try:
            self.telephoneno.set('')
        except:
            pass
        try:
            self.email.set('')
        except:
            pass
        try:
            self.providetransport.set('')
        except:
            pass
        try:
            self.jobs_carried_out.set('')
        except:
            pass

        
        ID = self.VolunteerID.get()
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.date_of_birth = StringVar()
        self.address = StringVar()
        self.postcode = StringVar()
        self.mobileno = StringVar()
        self.telephoneno = StringVar()
        self.email = StringVar()
        self.providetransport = StringVar()
        self.jobs_carried_out = StringVar()

        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT FIRST_NAME FROM VOLUNTEERS WHERE VOLUNTEERID = %s' % (ID));
        self.firstname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT LAST_NAME FROM VOLUNTEERS WHERE VOLUNTEERID = %s' % (ID));
        self.lastname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT DATE_OF_BIRTH FROM VOLUNTEERS WHERE VOLUNTEERID = %s' % (ID));
        self.date_of_birth.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT ADDRESS FROM VOLUNTEERS WHERE VOLUNTEERID = %s' % (ID));
        self.address.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT POSTCODE FROM VOLUNTEERS WHERE VOLUNTEERID = %s' % (ID));
        self.postcode.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT MOBILE_NUMBER FROM VOLUNTEERS WHERE VOLUNTEERID = %s' % (ID));
        self.mobileno.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT TELEPHONE_NUMBER FROM VOLUNTEERS WHERE VOLUNTEERID = %s' % (ID));
        self.telephoneno.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT EMAIL FROM VOLUNTEERS WHERE VOLUNTEERID = %s ' % (ID));
        self.email.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT PROVIDE_TRANSPORT FROM VOLUNTEERS WHERE VOLUNTEERID = %s ' % (ID));
        self.providetransport.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT JOBS_THEY_CARRY_OUT FROM VOLUNTEERS WHERE VOLUNTEERID = %s' % (ID));
        self.jobs_carried_out.set(cursor.fetchall()[0][0])

        self.FirstnameText = Label(self.DeleteVolunteerFrame, text='Forenames:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=280)
        self.FirstnameEntry = Label(self.DeleteVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.firstname).place(x=175,y=280)
        self.LastnameText = Label(self.DeleteVolunteerFrame, text='Surname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=380,y=280)
        self.LastnameEntry = Label(self.DeleteVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.lastname).place(x=500,y=280)
        self.DateofBirthText = Label(self.DeleteVolunteerFrame, text='Date of Birth:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20,y=310)
        self.DateofBirthEntry = Label(self.DeleteVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.date_of_birth).place(x=175,y=310)
        self.AddressText = Label(self.DeleteVolunteerFrame, text='Address:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=340)
        self.AddressEntry = Label(self.DeleteVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.address).place(x=175, y=340)
        self.PostcodeText = Label(self.DeleteVolunteerFrame, text='Postcode:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=370)
        self.PostcodeEntry = Label(self.DeleteVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.postcode).place(x=175,y=370)
        self.MobileNumberText = Label(self.DeleteVolunteerFrame, text='Mobile Number:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=400)
        self.MobileNumberEntry = Label(self.DeleteVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.mobileno).place(x=175, y=400)
        self.TelephoneNumberText = Label(self.DeleteVolunteerFrame, text='Telephone Number:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=380,y=400)
        self.TelephoneNumberEntry = Label(self.DeleteVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.telephoneno).place(x=500,y=400)
        self.EmailText = Label(self.DeleteVolunteerFrame, text='Email:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=430)
        self.EmailEntry = Label(self.DeleteVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.email).place(x=175,y=430)
        self.ProvideTransportText = Label(self.DeleteVolunteerFrame, text='Can Provide Transport?', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=460)
        self.ProvideTransportEntry = Label(self.DeleteVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.providetransport).place(x=175,y=460)
        self.JobsText = Label(self.DeleteVolunteerFrame, text='Jobs They Carry Out:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=490)
        self.JobsEntry = Label(self.DeleteVolunteerFrame, font=('ariel',10), bg='white', textvariable=self.jobs_carried_out).place(x=175,y=490)


        deletebutton = Button(self.DeleteVolunteerFrame, text='Delete', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.DeleteVolunteer3).place(x=700, y=190)
        
    def DeleteVolunteer3(self):
        database = sqlite3.connect('Appointments.db')
        ID = self.VolunteerID.get()

        try:
            database.execute('DELETE FROM APPOINTMENTS WHERE VOLUNTEERID = ?', (ID));
            database.execute()

            database.execute('UPDATE APPOINTMENTS SET APPOINTMENTID = APPOINTMENTID-1 WHERE VOLUNTEERID > ?', (ID));
            database.execute()
        except:
            pass

        database.execute("DELETE FROM VOLUNTEERS WHERE VOLUNTEERID = ?", (ID));
        database.commit()
        
        database.execute("UPDATE VOLUNTEERS SET VOLUNTEERID = VOLUNTEERID-1 WHERE VOLUNTEERID > ?", (ID));
        database.commit()


        self.DisplayAllVolunteers()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def AddServiceUser(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Add Service User')

        self.AddServiceUserFrame = Frame(self.master)
        self.AddServiceUserFrame.pack()

        background = Canvas(self.AddServiceUserFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Add Service User', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)

        
        self.Firstname = StringVar()
        self.Lastname = StringVar()
        self.Day = StringVar()
        self.Month = StringVar()
        self.Year = StringVar()
        self.Address = StringVar()
        self.Postcode = StringVar()
        self.MobileNo = StringVar()
        self.TelephoneNo = StringVar()
        self.Email = StringVar()
        self.Medical = StringVar()
        self.ClubOption1 = IntVar()
        self.ClubOption2 = IntVar()
        self.RequireTransport = StringVar()

        self.FirstnameText = Label(self.AddServiceUserFrame, text='Forenames:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=200)
        self.FirstnameEntry = Entry(self.AddServiceUserFrame, width=25, font=('ariel',10), bg='grey88', textvariable=self.Firstname).place(x=120,y=200)
        self.LastnameText = Label(self.AddServiceUserFrame, text='Surname:', fg='black', bg='white', font=('ariel',10)).place(x=330,y=200)
        self.LastnameEntry = Entry(self.AddServiceUserFrame, width=20, font=('ariel',10), bg='grey88', textvariable=self.Lastname).place(x=400,y=200)
        self.DateofBirthText = Label(self.AddServiceUserFrame, text='Date of Birth:', fg='black', bg='white', font=('ariel',10)).place(x=20,y=230)
        self.DateofBirthDay =  Entry(self.AddServiceUserFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Day).place(x=120,y=230)
        self.Divide = Label(self.AddServiceUserFrame, text='/', fg='black', bg='white', font=('ariel',12)).place(x=140, y=230)
        self.DateofBirthMonth =  Entry(self.AddServiceUserFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Month).place(x=155,y=230)
        self.Divide = Label(self.AddServiceUserFrame, text='/', fg='black', bg='white', font=('ariel',12)).place(x=175, y=230)
        self.DateofBirthYear =  Entry(self.AddServiceUserFrame, width=4, font=('ariel',10), bg='grey88', textvariable=self.Year).place(x=190,y=230)
        self.AddressText = Label(self.AddServiceUserFrame, text='Address:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=260)
        self.AddressEntry = Entry(self.AddServiceUserFrame, width=60, font=('ariel',10), bg='grey88', textvariable=self.Address).place(x=120, y=260)
        self.PostcodeText = Label(self.AddServiceUserFrame, text='Postcode:', fg='black', bg='white', font=('Ariel',10)).place(x=20,y=285)
        self.PostcodeEntry = Entry(self.AddServiceUserFrame, width=10, font=('ariel',10), bg='grey88', textvariable=self.Postcode).place(x=120,y=285)
        self.MobileNumberText = Label(self.AddServiceUserFrame, text='Mobile Number:', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=320)
        self.MobileNumberEntry = Entry(self.AddServiceUserFrame, width=15, font=('ariel',10), bg='grey88', textvariable=self.MobileNo).place(x=120, y=320)
        self.TelephoneNumberText = Label(self.AddServiceUserFrame, text='Telephone Number:', fg='black', bg='white', font=('Ariel',10)).place(x=250,y=320)
        self.TelephoneNumberEntry = Entry(self.AddServiceUserFrame, width=15, font=('ariel',10), bg='grey88', textvariable=self.TelephoneNo).place(x=375,y=320)
        self.EmailText = Label(self.AddServiceUserFrame, text='Email:', fg='black', bg='white', font=('Ariel',10)).place(x=20,y=350)
        self.EmailEntry = Entry(self.AddServiceUserFrame, width=40, font=('ariel',10), bg='grey88', textvariable=self.Email).place(x=120,y=350)
        self.MedicalText = Label(self.AddServiceUserFrame, text='Medical Information:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=380)
        self.MedicalEntry = Entry(self.AddServiceUserFrame, width=60, font=('ariel',10), bg='grey88', textvariable=self.Medical).place(x=150, y=380)
        self.ClubsText = Label(self.AddServiceUserFrame, text='Clubs Attended:', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=410)
        self.ClubsOption1Text = Checkbutton(self.AddServiceUserFrame, text='Lunch Club', font=('ariel',10), bg='white', variable=self.ClubOption1).place(x=150,y=410)
        self.ClubsOption2Text = Checkbutton(self.AddServiceUserFrame, text="3F's", font=('ariel',10), bg='white', variable=self.ClubOption2).place(x=150,y=430)
        self.RequireTransportText = Label(self.AddServiceUserFrame, text='Transport Required?', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=470)
        self.RequireTransport.set('Select...')
        self.RequireTransportEntry = OptionMenu(self.AddServiceUserFrame, self.RequireTransport, 'Yes', 'No').place(x=150,y=470)

        self.SubmitButton = Button(self.AddServiceUserFrame, text='Submit Form', font=('comic sans ms',12), bg='darkseagreen3', fg='white', command=self.AddServiceUser2).place(x=250, y=540)    

    def AddServiceUser2(self):
        ID = self.SUTotalID()
        ID +=1
        firstname = self.Firstname.get()
        lastname = self.Lastname.get()
        day = self.Day.get()
        month = self.Month.get()
        year = self.Year.get()
        address = self.Address.get()
        postcode = self.Postcode.get()
        mobileno = self.MobileNo.get()
        telephoneno = self.TelephoneNo.get()
        email = self.Email.get()
        medical = self.Medical.get()
        club1 = self.ClubOption1.get()
        club2 = self.ClubOption2.get()
        requiretransport = self.RequireTransport.get()

        dateofbirth = day + '/' + month + '/' + year
        clubslist = []
        if club1 == 1:
            clubslist.append('Lunch Club')
        if club2 == 1:
            clubslist.append("3F's")

        clubs = ','.join(clubslist)

        database = sqlite3.connect('Appointments.db')
        database.execute('INSERT INTO SERVICE_USERS (SERVICE_USERID, FIRST_NAME,LAST_NAME,DATE_OF_BIRTH,ADDRESS,POSTCODE,MOBILE_NUMBER,TELEPHONE_NUMBER,EMAIL,MEDICAL_INFORMATION,CLUBS_THEY_ATTEND,TRANSPORT_REQUIRED) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (ID, firstname, lastname, dateofbirth, address, postcode, mobileno, telephoneno, email, medical, clubs, requiretransport));
        database.commit()

        self.Firstname.set('')
        self.Lastname.set('')
        self.Day.set('')
        self.Month.set('')
        self.Year.set('')
        self.Address.set('')
        self.Postcode.set('')
        self.MobileNo.set('')
        self.TelephoneNo.set('')
        self.Email.set('')
        self.Medical.set('')
        self.ClubOption1.set(0)
        self.ClubOption2.set(0)
        self.RequireTransport.set('')

    def SearchServiceUser(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Search Serivce User')

        self.SearchServiceUserFrame = Frame(self.master)
        self.SearchServiceUserFrame.pack()

        background = Canvas(self.SearchServiceUserFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        background.create_line(0,250,1000,250, fill='black')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Search Service Users', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)

        MaxID = self.SUTotalID()

        self.ServiceUserID = StringVar()
        self.ServiceUserIDText = Label(self.SearchServiceUserFrame, text='Service User ID:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=200)
        self.ServiceUserIDEntry = Spinbox(self.SearchServiceUserFrame, width = 4, from_=0, to=MaxID, relief=FLAT, bg='grey88', textvariable = self.ServiceUserID, command=self.SearchServiceUser2).place(x=120, y=200)

    
    def SearchServiceUser2(self):
        try:
            self.firstname.set('')
        except:
            pass
        try:
            self.lastname.set('')
        except:
            pass
        try:
            self.date_of_birth.set('')
        except:
            pass
        try:
            self.address.set('')
        except:
            pass
        try:
            self.postcode.set('')
        except:
            pass
        try:
            self.mobileno.set('')
        except:
            pass
        try:
            self.telephoneno.set('')
        except:
            pass
        try:
            self.email.set('')
        except:
            pass
        try:
            self.medical_info.set('')
        except:
            pass
        try:
            self.clubs_attended.set('')
        except:
            pass
        try:
            self.transport_required.set('')
        except:
            pass


        #FIRST_NAME, LAST_NAME, DATE_OF_BIRTH, ADDRESS, POSTCODE, MOBILE_NUMBER, TELEPHONE_NUMBER, EMAIL, MEDICAL_INFORMATION, CLUBS_THEY_ATTEND, TRANSPORT_REQUIRED 
        
        ID = self.ServiceUserID.get()
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.date_of_birth = StringVar()
        self.address = StringVar()
        self.postcode = StringVar()
        self.mobileno = StringVar()
        self.telephoneno = StringVar()
        self.email = StringVar()
        self.medical_info = StringVar()
        self.clubs_attended = StringVar()
        self.transport_required = StringVar()

        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT FIRST_NAME FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.firstname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT LAST_NAME FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.lastname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT DATE_OF_BIRTH FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.date_of_birth.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT ADDRESS FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.address.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT POSTCODE FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.postcode.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT MOBILE_NUMBER FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.mobileno.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT TELEPHONE_NUMBER FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.telephoneno.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT EMAIL FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.email.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT MEDICAL_INFORMATION FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.medical_info.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT CLUBS_THEY_ATTEND FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.clubs_attended.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT TRANSPORT_REQUIRED FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.transport_required.set(cursor.fetchall()[0][0])


        self.FirstnameText = Label(self.SearchServiceUserFrame, text='Forenames:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=280)
        self.FirstnameEntry = Label(self.SearchServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.firstname).place(x=160,y=280)
        self.LastnameText = Label(self.SearchServiceUserFrame, text='Surname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=330,y=280)
        self.LastnameEntry = Label(self.SearchServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.lastname).place(x=450,y=280)
        self.DateofBirthText = Label(self.SearchServiceUserFrame, text='Date of Birth:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20,y=310)
        self.DateofBirthEntry = Label(self.SearchServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.date_of_birth).place(x=160,y=310)
        self.AddressText = Label(self.SearchServiceUserFrame, text='Address:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=340)
        self.AddressEntry = Label(self.SearchServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.address).place(x=160, y=340)
        self.PostcodeText = Label(self.SearchServiceUserFrame, text='Postcode:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=370)
        self.PostcodeEntry = Label(self.SearchServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.postcode).place(x=160,y=370)
        self.MobileNumberText = Label(self.SearchServiceUserFrame, text='Mobile Number:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=400)
        self.MobileNumberEntry = Label(self.SearchServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.mobileno).place(x=160, y=400)
        self.TelephoneNumberText = Label(self.SearchServiceUserFrame, text='Telephone Number:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=330,y=400)
        self.TelephoneNumberEntry = Label(self.SearchServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.telephoneno).place(x=450,y=400)
        self.EmailText = Label(self.SearchServiceUserFrame, text='Email:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=430)
        self.EmailEntry = Label(self.SearchServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.email).place(x=160,y=430)
        self.MedicalInfoText = Label(self.SearchServiceUserFrame, text='Medical Information:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=460)
        self.MedicalInfoEntry = Label(self.SearchServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.medical_info).place(x=160,y=460)
        self.ClubsText = Label(self.SearchServiceUserFrame, text='Clubs Attended:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=490)
        self.ClubsEntry = Label(self.SearchServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.clubs_attended).place(x=160,y=490)
        self.TransportRequiredText = Label(self.SearchServiceUserFrame, text='Transport Required?', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=520)
        self.TransportRequiredEntry = Label(self.SearchServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.transport_required).place(x=160,y=520)

    def UpdateServiceUser(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Update Service User')

        self.UpdateServiceUserFrame = Frame(self.master)
        self.UpdateServiceUserFrame.pack()

        background = Canvas(self.UpdateServiceUserFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Update Service User', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)

        MaxID = self.SUTotalID()

        self.ServiceUserID = StringVar()
        self.ServiceUserData = StringVar()
        
        self.ServiceUserIDText = Label(self.UpdateServiceUserFrame, text='Service User ID:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=200)
        self.ServiceUserIDEntry = Spinbox(self.UpdateServiceUserFrame, width = 4, from_=0, to=MaxID, relief=FLAT, bg='grey88', textvariable = self.ServiceUserID).place(x=120, y=200)

        self.ServiceUserDataText = Label(self.UpdateServiceUserFrame, text='What would you like to update:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=240)
        self.ServiceUserData.set('Select...')
        self.ServiceUserDataEntry = OptionMenu(self.UpdateServiceUserFrame, self.ServiceUserData, 'Firstname', 'Surname', 'Date of Birth', 'Address', 'Postcode', 'Mobile Number', 'Telephone Number', 'Email', 'Medical Information', 'Clubs They Attend', 'Transport Required?').place(x=210,y=240)

        self.selectbuttonupdate = Button(self.UpdateServiceUserFrame, text='Select', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.UpdateServiceUser2).place(x=380, y=240)

    def UpdateServiceUser2(self):
        self.selectbuttonupdate = Button(self.UpdateServiceUserFrame, text='Select', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, state=DISABLED, command=self.UpdateServiceUser2).place(x=380, y=240)
        Data = self.ServiceUserData.get()

        self.Var = StringVar()
        self.Var2 = StringVar()
        self.Var3 = StringVar()
        self.Var4 = IntVar()
        self.Var5 = IntVar()

        self.DataLabel = Label(self.UpdateServiceUserFrame, text='What would you like to change it to?', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=280)

        if Data == 'Firstname':
            self.Label = Label(self.UpdateServiceUserFrame, text='Forenames:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=320)
            self.Entry = Entry(self.UpdateServiceUserFrame, width=25, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=120,y=320)
        elif Data == 'Surname':
            self.Label = Label(self.UpdateServiceUserFrame, text='Surname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20,y=320)
            self.Entry = Entry(self.UpdateServiceUserFrame, width=20, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=120,y=320)
        elif Data == 'Date of Birth':
            self.Label = Label(self.UpdateServiceUserFrame, text='Date of Birth:', fg='black', bg='white', font=('ariel',10)).place(x=20,y=320)
            self.Entry =  Entry(self.UpdateServiceUserFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=120,y=320)
            self.Divide = Label(self.UpdateServiceUserFrame, text='/', fg='black', bg='white', font=('ariel',12)).place(x=140, y=320)
            self.Entry2 =  Entry(self.UpdateServiceUserFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Var2).place(x=155,y=320)
            self.Divide = Label(self.UpdateServiceUserFrame, text='/', fg='black', bg='white', font=('ariel',12)).place(x=175, y=320)
            self.Entry3 =  Entry(self.UpdateServiceUserFrame, width=4, font=('ariel',10), bg='grey88', textvariable=self.Var3).place(x=190,y=320)
        elif Data == 'Address':
            self.Label = Label(self.UpdateServiceUserFrame, text='Address:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=320)
            self.Entry = Entry(self.UpdateServiceUserFrame, width=60, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=120, y=320)
        elif Data == 'Postcode':
            self.Label = Label(self.UpdateServiceUserFrame, text='Postcode:', fg='black', bg='white', font=('Ariel',10)).place(x=20,y=320)
            self.Entry = Entry(self.UpdateServiceUserFrame, width=10, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=120,y=320)
        elif Data == 'Mobile Number':
            self.Label = Label(self.UpdateServiceUserFrame, text='Mobile Number:', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=320)
            self.Entry = Entry(self.UpdateServiceUserFrame, width=15, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=120, y=320)
        elif Data == 'Telephone Number':
            self.Label = Label(self.UpdateServiceUserFrame, text='Telephone Number:', fg='black', bg='white', font=('Ariel',10)).place(x=20,y=320)
            self.Entry = Entry(self.UpdateServiceUserFrame, width=15, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=150,y=320)
        elif Data == 'Email':
            self.Label = Label(self.UpdateServiceUserFrame, text='Email:', fg='black', bg='white', font=('Ariel',10)).place(x=20,y=320)
            self.Entry = Entry(self.UpdateServiceUserFrame, width=40, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=120,y=320)
        elif Data == 'Medical Information':
            self.Label = Label(self.UpdateServiceUserFrame, text='Medical Information:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=320)
            self.Entry = Entry(self.UpdateServiceUserFrame, width=60, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=150, y=320)
        elif Data == 'Transport Required?':
            self.Label = Label(self.UpdateServiceUserFrame, text='Transport Required?', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=320)
            self.Var.set('Select...')
            self.Entry = OptionMenu(self.UpdateServiceUserFrame, self.Var, 'Yes', 'No').place(x=175,y=320)
        elif Data == 'Clubs They Attend':
            self.Label = Label(self.UpdateServiceUserFrame, text='Clubs Attended:', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=320)
            self.Entry = Checkbutton(self.UpdateServiceUserFrame, text='Lunch Club', font=('ariel',10), bg='white', variable=self.Var4).place(x=150,y=320)
            self.Entry2 = Checkbutton(self.UpdateServiceUserFrame, text="3F's", font=('ariel',10), bg='white', variable=self.Var5).place(x=150,y=340)

        updatebutton = Button(self.UpdateServiceUserFrame, text='Update', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.UpdateServiceUser3).place(x=20, y=440)

    def UpdateServiceUser3(self):
        database = sqlite3.connect('Appointments.db')
        self.IDSU = self.ServiceUserID.get()
        Data = self.ServiceUserData.get()
        Var = self.Var.get()
        Var2 = self.Var2.get()
        Var3 = self.Var3.get()
        Var4 = self.Var4.get()
        Var5 = self.Var5.get()
        
        if Data == 'Firstname':
            database.execute("UPDATE SERVICE_USERS SET FIRST_NAME = ? WHERE SERVICE_USERID = ?", (Var,self.IDSU));
            database.commit()
        elif Data == 'Surname':
            database.execute('UPDATE SERVICE_USERS SET LAST_NAME = ? WHERE SERVICE_USERID = ?', (Var,self.IDSU));
            database.commit()
        elif Data == 'Date of Birth':
            dateofbirth = Var + '/' + Var2 + '/' + Var3
            database.execute('UPDATE SERVICE_USERS SET DATE_OF_BIRTH = ? WHERE SERVICE_USERID = ?', (dateofbirth,self.IDSU));
            database.commit()
        elif Data == 'Address':
            database.execute('UPDATE SERVICE_USERS SET ADDRESS = ? WHERE SERVICE_USERID = ?', (Var,self.IDSU));
            database.commit()
        elif Data == 'Postcode':
            database.execute('UPDATE SERVICE_USERS SET POSTCODE = ? WHERE SERVICE_USERID = ?', (Var,self.IDSU));
            database.commit()
        elif Data == 'Mobile Number':
            database.execute('UPDATE SERVICE_USERS SET MOBILE_NUMBER = ? WHERE SERVICE_USERID = ?', (Var,self.IDSU));
            database.commit()
        elif Data == 'Telephone Number':
            database.execute('UPDATE SERVICE_USERS SET TELEPHONE_NUMBER = ? WHERE SERVICE_USERID = ?', (Var,self.IDSU));
            database.commit()
        elif Data == 'Email':
            database.execute('UPDATE SERVICE_USERS SET EMAIL = ? WHERE SERVICE_USERID = ?', (Var,self.IDSU));
            database.commit()
        elif Data == 'Medical Information':
            database.execute('UPDATE SERVICE_USERS SET MEDICAL_INFORMATION = ? WHERE SERVICE_USERID = ?', (Var,self.IDSU));
            database.commit()
        elif Data == 'Transport Required?':
            database.execute('UPDATE SERVICE_USERS SET TRANSPORT_REQUIRED  = ? WHERE SERVICE_USERID = ?', (Var,self.IDSU));
            database.commit()
        elif Data == 'Clubs They Attend':
            clubslist = []
            if Var4 == 1:
                clubslist.append('Lunch Club')
            if Var5 == 1:
                clubslist.append("3F's")
                
            clubs = ','.join(clubslist)
            database.execute('UPDATE SERVICE_USERS SET CLUBS_THEY_ATTEND = ? WHERE SERVICE_USERID = ?', (clubs,self.IDSU));
            database.commit()



        self.ServiceUserData.set('Select...')
        self.Var.set('')
        self.Var2.set('')
        self.Var3.set('')
        self.Var4.set(0)
        self.Var5.set(0)
        self.ServiceUserID.set(0)

        self.UpdateServiceUser4()


    def UpdateServiceUser4(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Update Service User')

        self.UpdateServiceUserFrame2 = Frame(self.master)
        self.UpdateServiceUserFrame2.pack()

        background = Canvas(self.UpdateServiceUserFrame2, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        background.create_line(0,250,1000,250, fill='black')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Update Service User', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)

        self.firstname = StringVar()
        self.lastname = StringVar()
        self.date_of_birth = StringVar()
        self.address = StringVar()
        self.postcode = StringVar()
        self.mobileno = StringVar()
        self.telephoneno = StringVar()
        self.email = StringVar()
        self.medical_info = StringVar()
        self.clubs_attended = StringVar()
        self.transport_required = StringVar()

        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT FIRST_NAME FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (self.IDSU));
        self.firstname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT LAST_NAME FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (self.IDSU));
        self.lastname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT DATE_OF_BIRTH FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (self.IDSU));
        self.date_of_birth.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT ADDRESS FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (self.IDSU));
        self.address.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT POSTCODE FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (self.IDSU));
        self.postcode.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT MOBILE_NUMBER FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (self.IDSU));
        self.mobileno.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT TELEPHONE_NUMBER FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (self.IDSU));
        self.telephoneno.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT EMAIL FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (self.IDSU));
        self.email.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT MEDICAL_INFORMATION FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (self.IDSU));
        self.medical_info.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT CLUBS_THEY_ATTEND FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (self.IDSU));
        self.clubs_attended.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT TRANSPORT_REQUIRED FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (self.IDSU));
        self.transport_required.set(cursor.fetchall()[0][0])


        self.FirstnameText = Label(self.UpdateServiceUserFrame2, text='Forenames:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=280)
        self.FirstnameEntry = Label(self.UpdateServiceUserFrame2, font=('ariel',10), bg='white', textvariable=self.firstname).place(x=160,y=280)
        self.LastnameText = Label(self.UpdateServiceUserFrame2, text='Surname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=330,y=280)
        self.LastnameEntry = Label(self.UpdateServiceUserFrame2, font=('ariel',10), bg='white', textvariable=self.lastname).place(x=450,y=280)
        self.DateofBirthText = Label(self.UpdateServiceUserFrame2, text='Date of Birth:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20,y=310)
        self.DateofBirthEntry = Label(self.UpdateServiceUserFrame2, font=('ariel',10), bg='white', textvariable=self.date_of_birth).place(x=160,y=310)
        self.AddressText = Label(self.UpdateServiceUserFrame2, text='Address:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=340)
        self.AddressEntry = Label(self.UpdateServiceUserFrame2, font=('ariel',10), bg='white', textvariable=self.address).place(x=160, y=340)
        self.PostcodeText = Label(self.UpdateServiceUserFrame2, text='Postcode:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=370)
        self.PostcodeEntry = Label(self.UpdateServiceUserFrame2, font=('ariel',10), bg='white', textvariable=self.postcode).place(x=160,y=370)
        self.MobileNumberText = Label(self.UpdateServiceUserFrame2, text='Mobile Number:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=400)
        self.MobileNumberEntry = Label(self.UpdateServiceUserFrame2, font=('ariel',10), bg='white', textvariable=self.mobileno).place(x=160, y=400)
        self.TelephoneNumberText = Label(self.UpdateServiceUserFrame2, text='Telephone Number:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=330,y=400)
        self.TelephoneNumberEntry = Label(self.UpdateServiceUserFrame2, font=('ariel',10), bg='white', textvariable=self.telephoneno).place(x=450,y=400)
        self.EmailText = Label(self.UpdateServiceUserFrame2, text='Email:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=430)
        self.EmailEntry = Label(self.UpdateServiceUserFrame2, font=('ariel',10), bg='white', textvariable=self.email).place(x=160,y=430)
        self.MedicalInfoText = Label(self.UpdateServiceUserFrame2, text='Medical Information:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=460)
        self.MedicalInfoEntry = Label(self.UpdateServiceUserFrame2, font=('ariel',10), bg='white', textvariable=self.medical_info).place(x=160,y=460)
        self.ClubsText = Label(self.UpdateServiceUserFrame2, text='Clubs Attended:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=490)
        self.ClubsEntry = Label(self.UpdateServiceUserFrame2, font=('ariel',10), bg='white', textvariable=self.clubs_attended).place(x=160,y=490)
        self.TransportRequiredText = Label(self.UpdateServiceUserFrame2, text='Transport Required?', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=520)
        self.TransportRequiredEntry = Label(self.UpdateServiceUserFrame2, font=('ariel',10), bg='white', textvariable=self.transport_required).place(x=160,y=520)

    def DisplayAllServiceUsers(self):
        self.ClearWindow()
        self.master.geometry("1000x600")
        self.master.title("Display All Service Users")

        self.DisplayAllServiceUsersFrame = Frame(self.master)
        self.DisplayAllServiceUsersFrame.pack()
        self.DisplayAllServiceUsersFrame.grid_rowconfigure(0, weight=1)
        self.DisplayAllServiceUsersFrame.grid_columnconfigure(0, weight=1)

        xscrollbar = Scrollbar(self.DisplayAllServiceUsersFrame, orient=HORIZONTAL)
        xscrollbar.grid(row=1, column=0, sticky=E+W)
        yscrollbar = Scrollbar(self.DisplayAllServiceUsersFrame)
        yscrollbar.grid(row=0, column=1, sticky=N+S)
        
        background = Canvas(self.DisplayAllServiceUsersFrame, width=1000, height=600, scrollregion=(0, 0, 2600, 1000),
                xscrollcommand=xscrollbar.set,
                yscrollcommand=yscrollbar.set)

        xscrollbar.config(command=background.xview)
        yscrollbar.config(command=background.yview)

        background.create_rectangle(0, 0, 2600, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 2600, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 2600, 1000, fill="white", outline='white')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Displaying All Service Users', font=('comic sans ms',50), fill='violetred4')
        #homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        #homebutton.place(x=40,y=110)

        background.grid(row=0, column=0, sticky=N+S+E+W)

        background.create_text(70,165, text='Service User ID', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(230,165, text='Forenames', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(420,165, text='Surname', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(570,165, text='Date of Birth', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(870,165, text='Address', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(1160,165, text='Postcode', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(1290,165, text='Mobile Number', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(1440,165, text='Telephone Number', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(1670,165, text='Email', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(2060,165, text='Medical Information', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(2350,165, text='Clubs They Attend', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(2500,165, text='Transport Required?', fill='violetred4', font=('Ariel',11,'underline'))

        #FIRST_NAME, LAST_NAME, DATE_OF_BIRTH, ADDRESS, POSTCODE, MOBILE_NUMBER, TELEPHONE_NUMBER, EMAIL, MEDICAL_INFORMATION, CLUBS_THEY_ATTEND, TRANSPORT_REQUIRED 

        SUIDTotal = self.SUTotalID()
        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT FIRST_NAME FROM SERVICE_USERS');
        firstname = cursor.fetchall()
        cursor.execute('SELECT LAST_NAME FROM SERVICE_USERS');
        lastname = cursor.fetchall()
        cursor.execute('SELECT DATE_OF_BIRTH FROM SERVICE_USERS');
        dateofbirth = cursor.fetchall()
        cursor.execute('SELECT ADDRESS FROM SERVICE_USERS');
        address = cursor.fetchall()
        cursor.execute('SELECT POSTCODE FROM SERVICE_USERS');
        postcode = cursor.fetchall()
        cursor.execute('SELECT MOBILE_NUMBER FROM SERVICE_USERS');
        mobileno = cursor.fetchall()
        cursor.execute('SELECT TELEPHONE_NUMBER FROM SERVICE_USERS');
        telephoneno = cursor.fetchall()
        cursor.execute('SELECT EMAIL FROM SERVICE_USERS');
        email = cursor.fetchall()
        cursor.execute('SELECT MEDICAL_INFORMATION FROM SERVICE_USERS');
        medicalinfo = cursor.fetchall()
        cursor.execute('SELECT CLUBS_THEY_ATTEND FROM SERVICE_USERS');
        clubs = cursor.fetchall()
        cursor.execute('SELECT TRANSPORT_REQUIRED FROM SERVICE_USERS');
        transportrequired = cursor.fetchall()
        

        yvalue=190
        for a in range(1,(SUIDTotal+1)):
            background.create_text(50,yvalue, font=('ariel',10), fill='black', text=a)
            yvalue += 20
        
        yvalue=190
        i=0
        for a in range(0,SUIDTotal):
            sufirstname = firstname[i][0]
            background.create_text(230,yvalue, font=('ariel',10), fill='black', text=sufirstname)
            i += 1
            yvalue += 20

        yvalue=190
        i=0
        for a in range(0,SUIDTotal):
            sulastname = lastname[i][0]
            background.create_text(420,yvalue, font=('ariel',10), fill='black', text=sulastname)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,SUIDTotal):
            sudateofbirth = dateofbirth[i][0]
            background.create_text(570,yvalue, font=('ariel',10), fill='black', text=sudateofbirth)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,SUIDTotal):
            suaddress = address[i][0]
            background.create_text(870,yvalue, font=('ariel',10), fill='black', text=suaddress)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,SUIDTotal):
            supostcode = postcode[i][0]
            background.create_text(1160,yvalue, font=('ariel',10), fill='black', text=supostcode)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,SUIDTotal):
            sumobileno = mobileno[i][0]
            background.create_text(1290,yvalue, font=('ariel',10), fill='black', text=sumobileno)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,SUIDTotal):
            sutelephoneno = telephoneno[i][0]
            background.create_text(1440,yvalue, font=('ariel',10), fill='black', text=sutelephoneno)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,SUIDTotal):
            suemail = email[i][0]
            background.create_text(1670,yvalue, font=('ariel',10), fill='black', text=suemail)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,SUIDTotal):
            sumedicalinfo = medicalinfo[i][0]
            background.create_text(2060,yvalue, font=('ariel',10), fill='black', text=sumedicalinfo)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,SUIDTotal):
            suclubs = clubs[i][0]
            background.create_text(2350,yvalue, font=('ariel',10), fill='black', text=suclubs)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,SUIDTotal):
            sutransportrequired = transportrequired[i][0]
            background.create_text(2500,yvalue, font=('ariel',10), fill='black', text=sutransportrequired)
            i += 1
            yvalue += 20

    def DeleteServiceUser(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Delete Service User')

        self.DeleteServiceUserFrame = Frame(self.master)
        self.DeleteServiceUserFrame.pack()

        background = Canvas(self.DeleteServiceUserFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        background.create_line(0,250,1000,250, fill='black')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Delete Service User', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)

        MaxID = self.SUTotalID()

        self.ServiceUserID = StringVar()
        self.ServiceUserText = Label(self.DeleteServiceUserFrame, text='Service User ID:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=200)
        self.ServiceUserIDEntry = Spinbox(self.DeleteServiceUserFrame, width = 4, from_=0, to=MaxID, relief=FLAT, bg='grey88', textvariable = self.ServiceUserID, command=self.DeleteServiceUser2).place(x=120, y=200)

    def DeleteServiceUser2(self):
        try:
            self.firstname.set('')
        except:
            pass
        try:
            self.lastname.set('')
        except:
            pass
        try:
            self.date_of_birth.set('')
        except:
            pass
        try:
            self.address.set('')
        except:
            pass
        try:
            self.postcode.set('')
        except:
            pass
        try:
            self.mobileno.set('')
        except:
            pass
        try:
            self.telephoneno.set('')
        except:
            pass
        try:
            self.email.set('')
        except:
            pass
        try:
            self.medical_info.set('')
        except:
            pass
        try:
            self.clubs_attended.set('')
        except:
            pass
        try:
            self.transport_required.set('')
        except:
            pass


        #FIRST_NAME, LAST_NAME, DATE_OF_BIRTH, ADDRESS, POSTCODE, MOBILE_NUMBER, TELEPHONE_NUMBER, EMAIL, MEDICAL_INFORMATION, CLUBS_THEY_ATTEND, TRANSPORT_REQUIRED 
        
        ID = self.ServiceUserID.get()
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.date_of_birth = StringVar()
        self.address = StringVar()
        self.postcode = StringVar()
        self.mobileno = StringVar()
        self.telephoneno = StringVar()
        self.email = StringVar()
        self.medical_info = StringVar()
        self.clubs_attended = StringVar()
        self.transport_required = StringVar()

        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT FIRST_NAME FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.firstname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT LAST_NAME FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.lastname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT DATE_OF_BIRTH FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.date_of_birth.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT ADDRESS FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.address.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT POSTCODE FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.postcode.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT MOBILE_NUMBER FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.mobileno.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT TELEPHONE_NUMBER FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.telephoneno.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT EMAIL FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.email.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT MEDICAL_INFORMATION FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.medical_info.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT CLUBS_THEY_ATTEND FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.clubs_attended.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT TRANSPORT_REQUIRED FROM SERVICE_USERS WHERE SERVICE_USERID = %s' % (ID));
        self.transport_required.set(cursor.fetchall()[0][0])


        self.FirstnameText = Label(self.DeleteServiceUserFrame, text='Forenames:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=280)
        self.FirstnameEntry = Label(self.DeleteServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.firstname).place(x=160,y=280)
        self.LastnameText = Label(self.DeleteServiceUserFrame, text='Surname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=330,y=280)
        self.LastnameEntry = Label(self.DeleteServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.lastname).place(x=450,y=280)
        self.DateofBirthText = Label(self.DeleteServiceUserFrame, text='Date of Birth:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20,y=310)
        self.DateofBirthEntry = Label(self.DeleteServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.date_of_birth).place(x=160,y=310)
        self.AddressText = Label(self.DeleteServiceUserFrame, text='Address:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=340)
        self.AddressEntry = Label(self.DeleteServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.address).place(x=160, y=340)
        self.PostcodeText = Label(self.DeleteServiceUserFrame, text='Postcode:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=370)
        self.PostcodeEntry = Label(self.DeleteServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.postcode).place(x=160,y=370)
        self.MobileNumberText = Label(self.DeleteServiceUserFrame, text='Mobile Number:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=400)
        self.MobileNumberEntry = Label(self.DeleteServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.mobileno).place(x=160, y=400)
        self.TelephoneNumberText = Label(self.DeleteServiceUserFrame, text='Telephone Number:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=330,y=400)
        self.TelephoneNumberEntry = Label(self.DeleteServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.telephoneno).place(x=450,y=400)
        self.EmailText = Label(self.DeleteServiceUserFrame, text='Email:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=430)
        self.EmailEntry = Label(self.DeleteServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.email).place(x=160,y=430)
        self.MedicalInfoText = Label(self.DeleteServiceUserFrame, text='Medical Information:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=460)
        self.MedicalInfoEntry = Label(self.DeleteServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.medical_info).place(x=160,y=460)
        self.ClubsText = Label(self.DeleteServiceUserFrame, text='Clubs Attended:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=490)
        self.ClubsEntry = Label(self.DeleteServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.clubs_attended).place(x=160,y=490)
        self.TransportRequiredText = Label(self.DeleteServiceUserFrame, text='Transport Required?', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=520)
        self.TransportRequiredEntry = Label(self.DeleteServiceUserFrame, font=('ariel',10), bg='white', textvariable=self.transport_required).place(x=160,y=520)

        deletebutton = Button(self.DeleteServiceUserFrame, text='Delete', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.DeleteServiceUser3).place(x=700, y=190)
        
    def DeleteServiceUser3(self):
        database = sqlite3.connect('Appointments.db')
        ID = self.ServiceUserID.get()

        try:
            database.execute('DELETE FROM APPOINTMENTS WHERE SERVICE_USERID = ?', (ID));
            database.execute()

            database.execute('UPDATE APPOINTMENTS SET APPOINTMENTID = APPOINTMENTID-1 WHERE SERVICE_USERID > ?', (ID));
            database.execute()
        except:
            pass

        database.execute("DELETE FROM SERVICE_USERS WHERE SERVICE_USERID = ?", (ID, ));
        database.commit()
        
        database.execute("UPDATE SERVICE_USERS SET SERVICE_USERID = SERVICE_USERID-1 WHERE SERVICE_USERID > ?", (ID, ));
        database.commit()

        self.DisplayAllServiceUsers()





    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def AddAppointment(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Add Appointment')

        self.AddAppointmentFrame = Frame(self.master)
        self.AddAppointmentFrame.pack()

        background = Canvas(self.AddAppointmentFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Add Appointment', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)

        self.VolunteerID = StringVar()
        self.ServiceUserID = StringVar()
        self.AppDay = StringVar()
        self.AppMonth = StringVar()
        self.AppYear = StringVar()
        VMAXID = self.TotalID()
        SUMAXID = self.SUTotalID()

        self.VolunteerIDText = Label(self.AddAppointmentFrame, text='Volunteer ID:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=200)
        self.VolunteerIDEntry = Spinbox(self.AddAppointmentFrame, width = 4, from_=0, to=VMAXID, relief=FLAT, bg='grey88', textvariable = self.VolunteerID, command=self.AddAppointment21).place(x=140, y=200)
        self.ServiceUserIDText = Label(self.AddAppointmentFrame, text='Service User ID:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=230)
        self.ServiceUserIDEntry = Spinbox(self.AddAppointmentFrame, width = 4, from_=0, to=SUMAXID, relief=FLAT, bg='grey88', textvariable = self.ServiceUserID, command=self.AddAppointment22).place(x=140, y=230)
        self.AppText = Label(self.AddAppointmentFrame, text='Date of Appointment:', fg='black', bg='white', font=('ariel',10)).place(x=20,y=270)
        self.AppDayEntry =  Entry(self.AddAppointmentFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.AppDay).place(x=155,y=270)
        self.Divide = Label(self.AddAppointmentFrame, text='/', fg='black', bg='white', font=('ariel',12)).place(x=175, y=270)
        self.AppMonthEntry =  Entry(self.AddAppointmentFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.AppMonth).place(x=190,y=270)
        self.Divide = Label(self.AddAppointmentFrame, text='/', fg='black', bg='white', font=('ariel',12)).place(x=210, y=270)
        self.AppYearEntry =  Entry(self.AddAppointmentFrame, width=4, font=('ariel',10), bg='grey88', textvariable=self.AppYear).place(x=225,y=270)

        selectbutton = Button(self.AddAppointmentFrame, text='Select', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.AddAppointment3).place(x=700, y=200)

    def AddAppointment21(self):
        try:
            self.Vfirstname.set('')
        except:
            pass
        try:
            self.Vlastname.set('')
        except:
            pass

        VID = self.VolunteerID.get()

        self.Vfirstname = StringVar()
        self.Vlastname = StringVar()

        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT FIRST_NAME FROM VOLUNTEERS WHERE VOLUNTEERID = ?', (VID));
        self.Vfirstname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT LAST_NAME FROM VOLUNTEERS WHERE VOLUNTEERID = ?', (VID));
        self.Vlastname.set(cursor.fetchall()[0][0])

        self.VolunteerFirstnameText = Label(self.AddAppointmentFrame, text='Firstname:', fg='black', bg='white', font=('ariel',10)).place(x=190, y=200)
        self.VolunteerFirstnameEntry = Label(self.AddAppointmentFrame, textvariable=self.Vfirstname, fg='black', bg='grey88', font=('ariel',10)).place(x=270, y=200)
        self.VolunteerSurnameText = Label(self.AddAppointmentFrame, text='Surname:', fg='black', bg='white', font=('ariel',10)).place(x=425, y=200)
        self.VolunteerSurnameEntry = Label(self.AddAppointmentFrame, textvariable=self.Vlastname, fg='black', bg='grey88', font=('ariel',10)).place(x=500, y=200)


    def AddAppointment22(self):
        try:
            self.SUfirstname.set('')
        except:
            pass
        try:
            self.SUlastname.set('')
        except:
            pass

        SUID = self.ServiceUserID.get()

        self.SUfirstname = StringVar()
        self.SUlastname = StringVar()

        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT FIRST_NAME FROM SERVICE_USERS WHERE SERVICE_USERID = ?', (SUID, ));
        self.SUfirstname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT LAST_NAME FROM SERVICE_USERS WHERE SERVICE_USERID = ?', (SUID, ));
        self.SUlastname.set(cursor.fetchall()[0][0])

        self.ServiceUserFirstnameText = Label(self.AddAppointmentFrame, text='Firstname:', fg='black', bg='white', font=('ariel',10)).place(x=190, y=230)
        self.ServiceUserFirstnameEntry = Label(self.AddAppointmentFrame, textvariable=self.SUfirstname, fg='black', bg='grey88', font=('ariel',10)).place(x=270, y=230)
        self.ServiceUserSurnameText = Label(self.AddAppointmentFrame, text='Surname:', fg='black', bg='white', font=('ariel',10)).place(x=425, y=230)
        self.ServiceUserSurnameEntry = Label(self.AddAppointmentFrame, textvariable=self.SUlastname, fg='black', bg='grey88', font=('ariel',10)).place(x=500, y=230)
    
    def AddAppointment3(self):
        VID = self.VolunteerID.get()
        SUID = self.ServiceUserID.get()

        self.date = StringVar()

        appday = self.AppDay.get()
        appmonth = self.AppMonth.get()
        appyear = self.AppYear.get()
        appdate = appday + '/' + appmonth + '/' + appyear
        self.date.set(appdate)

        self.AppTime = StringVar()
        self.StartLocation = StringVar()
        self.StartLocation2 = StringVar()
        self.StartLocationPostcode = StringVar()
        self.Destination = StringVar()
        self.Destination2 = StringVar()
        self.DestinationPostcode = StringVar()
        self.ExpensesPaid = StringVar()

        
        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT APPOINTMENTID FROM APPOINTMENTS WHERE VOLUNTEERID = ? AND DATE_OF_APPOINTMENT = ?', (VID, appdate));
        date = cursor.fetchall()

        times = ['10:00', '10:30', '11:00', '11:30', '12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00']

        for i in range(0,len(date)):
            appid = date[i][0]
            cursor.execute('SELECT TIME_OF_APPOINTMENT FROM APPOINTMENTS WHERE APPOINTMENTID = ?', (appid, ));
            time = cursor.fetchall()[0][0]
            times.remove(time)
           
        self.AppTimeText = Label(self.AddAppointmentFrame, text='Time of Appointment', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=310)
        self.AppTime.set('Select...')
        self.AppTimeEntry = OptionMenu(self.AddAppointmentFrame, self.AppTime,*times).place(x=150,y=310)

        self.StartLocationText = Label(self.AddAppointmentFrame, text='Start Location:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=350)
        self.StartLocationEntry = Entry(self.AddAppointmentFrame, width=60, font=('ariel',10), bg='grey88', textvariable=self.StartLocation).place(x=120, y=350)
        self.StartLocationEntry2 = Entry(self.AddAppointmentFrame, width=35, font=('ariel',10), bg='grey88', textvariable=self.StartLocation2).place(x=120, y=375)
        self.StartLocationPostcodeText = Label(self.AddAppointmentFrame, text='Postcode:', fg='black', bg='white', font=('Ariel',10)).place(x=400,y=375)
        self.StartLocationPostcodeEntry = Entry(self.AddAppointmentFrame, width=10, font=('ariel',10), bg='grey88', textvariable=self.StartLocationPostcode).place(x=470,y=375)
        self.DestinationText = Label(self.AddAppointmentFrame, text='Destination:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=405)
        self.DestinationEntry = Entry(self.AddAppointmentFrame, width=60, font=('ariel',10), bg='grey88', textvariable=self.Destination).place(x=120, y=405)
        self.DestinationEntry2 = Entry(self.AddAppointmentFrame, width=35, font=('ariel',10), bg='grey88', textvariable=self.Destination2).place(x=120, y=430)
        self.DestinationPostcodeText = Label(self.AddAppointmentFrame, text='Postcode:', fg='black', bg='white', font=('Ariel',10)).place(x=400,y=430)
        self.DestinationPostcodeEntry = Entry(self.AddAppointmentFrame, width=10, font=('ariel',10), bg='grey88', textvariable=self.DestinationPostcode).place(x=470,y=430)
        self.ExpensesPaidText = Label(self.AddAppointmentFrame, text='Expenses Paid?', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=460)
        self.ExpensesPaid.set('Select...')
        self.ExpensesPaidEntry = OptionMenu(self.AddAppointmentFrame, self.ExpensesPaid, 'Yes', 'No').place(x=130,y=460)

        self.SubmitButton = Button(self.AddAppointmentFrame, text='Submit Appointment', font=('comic sans ms',12), bg='darkseagreen3', fg='white', command=self.AddAppointment4).place(x=250, y=500)

    def AddAppointment4(self):
        ID = self.ATotalID()
        ID +=1
        VID = self.VolunteerID.get()
        SUID = self.ServiceUserID .get()
        appdate = self.date.get()
        apptime = self.AppTime.get()
        startloc = self.StartLocation.get()
        startloc2 = self.StartLocation2.get()
        startpost = self.StartLocationPostcode.get()
        destination = self.Destination.get()
        destination2 = self.Destination2.get()
        destinationpost = self.DestinationPostcode.get()
        expenses = self.ExpensesPaid.get()

        startlocation = startloc + ' ' + startloc2 + ', ' + startpost
        destination = destination + ' ' + destination + ', ' + destinationpost

        database = sqlite3.connect('Appointments.db')
        database.execute('INSERT INTO APPOINTMENTS (APPOINTMENTID, VOLUNTEERID, SERVICE_USERID, DATE_OF_APPOINTMENT, TIME_OF_APPOINTMENT, START_LOCATION, DESTINATION, EXPENSES_PAID) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (ID, VID, SUID, appdate, apptime, startlocation, destination, expenses));
        database.commit()

        self.VolunteerID.set(0)
        self.ServiceUserID.set(0)
        self.Vfirstname.set('')
        self.Vlastname.set('')
        self.SUfirstname.set('')
        self.SUlastname.set('')
        self.AppDay.set('')
        self.AppMonth.set('')
        self.AppYear.set('')
        self.AppTime.set('Select...')
        self.StartLocation.set('')
        self.StartLocation2.set('')
        self.StartLocationPostcode.set('')
        self.Destination.set('')
        self.Destination2.set('')
        self.DestinationPostcode.set('')
        self.ExpensesPaid.set('Select...')

    def SearchAppointments(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Search Appointment')

        self.SearchAppointmentFrame = Frame(self.master)
        self.SearchAppointmentFrame.pack()

        background = Canvas(self.SearchAppointmentFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        background.create_line(0,250,1000,250, fill='black')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Search Appointments', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)

        MaxID = self.ATotalID()

        self.AppID = StringVar()
        self.AppIDText = Label(self.SearchAppointmentFrame, text='Appointment Number:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=200)
        self.AppIDEntry = Spinbox(self.SearchAppointmentFrame, width = 4, from_=0, to=MaxID, relief=FLAT, bg='grey88', textvariable = self.AppID, command=self.SearchAppointments2).place(x=150, y=200)

    def SearchAppointments2(self):
        try:
            self.Vfirstname.set('')
        except:
            pass
        try:
            self.Vlastname.set('')
        except:
            pass
        try:
            self.SUfirstname.set('')
        except:
            pass
        try:
            self.SUlastname.set('')
        except:
            pass
        try:
            self.date_of_app.set('')
        except:
            pass
        try:
            self.time_of_app.set('')
        except:
            pass
        try:
            self.startloc.set('')
        except:
            pass
        try:
            self.destination.set('')
        except:
            pass
        try:
            self.expensespaid.set('')
        except:
            pass
        
        self.Vfirstname = StringVar()
        self.Vlastname = StringVar()
        self.SUfirstname = StringVar()
        self.SUlastname = StringVar()
        self.date_of_app = StringVar()
        self.time_of_app = StringVar()
        self.startloc = StringVar()
        self.destination = StringVar()
        self.expensespaid = StringVar()
        AppID2 = self.AppID.get()
        
        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT FIRST_NAME FROM VOLUNTEERS,APPOINTMENTS WHERE APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID');
        self.Vfirstname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT LAST_NAME FROM VOLUNTEERS,APPOINTMENTS WHERE APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID');
        self.Vlastname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT FIRST_NAME FROM SERVICE_USERS,APPOINTMENTS WHERE APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID');
        self.SUfirstname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT LAST_NAME FROM SERVICE_USERS,APPOINTMENTS WHERE APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID');
        self.SUlastname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT DATE_OF_APPOINTMENT FROM APPOINTMENTS WHERE APPOINTMENTID = ?', (AppID2));
        self.date_of_app.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT TIME_OF_APPOINTMENT FROM APPOINTMENTS WHERE APPOINTMENTID = ?', (AppID2));
        self.time_of_app.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT START_LOCATION FROM APPOINTMENTS WHERE APPOINTMENTID = ?', (AppID2));
        self.startloc.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT DESTINATION FROM APPOINTMENTS WHERE APPOINTMENTID = ?', (AppID2));
        self.destination.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT EXPENSES_PAID FROM APPOINTMENTS WHERE APPOINTMENTID = ?', (AppID2));
        self.expensespaid.set(cursor.fetchall()[0][0])
        
        self.VFirstnameText = Label(self.SearchAppointmentFrame, text='Volunteer Firstname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=280)
        self.VFirstnameEntry = Label(self.SearchAppointmentFrame, font=('ariel',10), bg='white', textvariable=self.Vfirstname).place(x=175,y=280)
        self.VLastnameText = Label(self.SearchAppointmentFrame, text='Volunteer Lastname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=400,y=280)
        self.VLastnameEntry = Label(self.SearchAppointmentFrame, font=('ariel',10), bg='white', textvariable=self.Vlastname).place(x=550,y=280)
        self.SUFirstnameText = Label(self.SearchAppointmentFrame, text='Service User Firstname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=320)
        self.SUFirstnameEntry = Label(self.SearchAppointmentFrame, font=('ariel',10), bg='white', textvariable=self.SUfirstname).place(x=175,y=320)
        self.SULastnameText = Label(self.SearchAppointmentFrame, text='Service User Lastname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=400,y=320)
        self.SULastnameEntry = Label(self.SearchAppointmentFrame, font=('ariel',10), bg='white', textvariable=self.SUlastname).place(x=550,y=320)
        self.DateofAppText = Label(self.SearchAppointmentFrame, text='Date of Appointment:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20,y=360)
        self.DateofAppEntry = Label(self.SearchAppointmentFrame, font=('ariel',10), bg='white', textvariable=self.date_of_app).place(x=175,y=360)
        self.TimeofAppText = Label(self.SearchAppointmentFrame, text='Time of Appointment:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=400)
        self.TimeofAppEntry = Label(self.SearchAppointmentFrame, font=('ariel',10), bg='white', textvariable=self.time_of_app).place(x=175, y=400)
        self.StartLocationText = Label(self.SearchAppointmentFrame, text='Start Location:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=440)
        self.StartLocationEntry = Label(self.SearchAppointmentFrame, font=('ariel',10), bg='white', textvariable=self.startloc).place(x=175,y=440)
        self.DestinationText = Label(self.SearchAppointmentFrame, text='Destination:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=480)
        self.DestinationEntry = Label(self.SearchAppointmentFrame, font=('ariel',10), bg='white', textvariable=self.destination).place(x=175,y=480)
        self.ExpensesPaidText = Label(self.SearchAppointmentFrame, text='Expenses Paid?', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=520)
        self.ExpensesPaidEntry = Label(self.SearchAppointmentFrame, font=('ariel',10), bg='white', textvariable=self.expensespaid).place(x=175,y=520)

    def UpdateAppointment(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Update Appointment')

        self.UpdateAppointmentFrame = Frame(self.master)
        self.UpdateAppointmentFrame.pack()

        background = Canvas(self.UpdateAppointmentFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Update Appointment', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)

        MaxID = self.ATotalID()

        self.AppointmentID = StringVar()
        self.AppointmentData = StringVar()
        
        self.AppointmentIDText = Label(self.UpdateAppointmentFrame, text='Appointment ID:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=200)
        self.AppointmentIDEntry = Spinbox(self.UpdateAppointmentFrame, width = 4, from_=0, to=MaxID, relief=FLAT, bg='grey88', textvariable = self.AppointmentID).place(x=120, y=200)

        self.AppointmentDataText = Label(self.UpdateAppointmentFrame, text='What would you like to update:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=240)
        self.AppointmentData.set('Select...')
        self.AppointmentDataEntry = OptionMenu(self.UpdateAppointmentFrame, self.AppointmentData, 'Volunteer ID', 'Service User ID', 'Date of Appointment', 'Time of Appointment', 'Start Location', 'Destination', 'Expenses Paid?' ).place(x=210,y=240)

        self.selectbuttonupdate = Button(self.UpdateAppointmentFrame, text='Select', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.UpdateAppointment2).place(x=450, y=240)

    def UpdateAppointment2(self):
        self.selectbuttonupdate = Button(self.UpdateAppointmentFrame, text='Select', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.UpdateAppointment2, state=DISABLED).place(x=450, y=240)
        ID = self.AppointmentID.get()
        Data = self.AppointmentData.get()
        VMAXID = self.TotalID()
        SUMAXID = self.SUTotalID()

        self.Var = StringVar()
        self.Var2 = StringVar()
        self.Var3 = StringVar()

        self.DataLabel = Label(self.UpdateAppointmentFrame, text='What would you like to change it to?', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=280)

        if Data == 'Volunteer ID':
            self.Label = Label(self.UpdateAppointmentFrame, text='Volunteer ID:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=320)
            self.Entry = Spinbox(self.UpdateAppointmentFrame, width = 4, from_=1, to=VMAXID, relief=FLAT, bg='grey88', textvariable = self.Var).place(x=120,y=320)
        elif Data == 'Service User ID':
            self.Label = Label(self.UpdateAppointmentFrame, text='Service User ID:', fg='black', bg='white', font=('ariel',10)).place(x=20,y=320)
            self.Entry = Spinbox(self.UpdateAppointmentFrame, width = 4, from_=1, to=SUMAXID, relief=FLAT, bg='grey88', textvariable = self.Var).place(x=120,y=320)
        elif Data == 'Date of Appointment':
            self.Label = Label(self.UpdateAppointmentFrame, text='Date of Appointment:', fg='black', bg='white', font=('ariel',10)).place(x=20,y=320)
            self.Entry =  Entry(self.UpdateAppointmentFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=150,y=320)
            self.Divide = Label(self.UpdateAppointmentFrame, text='/', fg='black', bg='white', font=('ariel',12)).place(x=170, y=320)
            self.Entry2 =  Entry(self.UpdateAppointmentFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Var2).place(x=185,y=320)
            self.Divide = Label(self.UpdateAppointmentFrame, text='/', fg='black', bg='white', font=('ariel',12)).place(x=205, y=320)
            self.Entry3 =  Entry(self.UpdateAppointmentFrame, width=4, font=('ariel',10), bg='grey88', textvariable=self.Var3).place(x=220,y=320)
        elif Data == 'Time of Appointment':
            database = sqlite3.connect('Appointments.db')
            cursor = database.cursor()
            cursor.execute('SELECT DATE_OF_APPOINTMENT FROM APPOINTMENTS WHERE APPOINTMENTID = ?', (ID));
            date = cursor.fetchall()[0][0]
            cursor.execute('SELECT TIME_OF_APPOINTMENT FROM APPOINTMENTS WHERE DATE_OF_APPOINTMENT = ?', (date, ));
            timeslist = cursor.fetchall()[0]

            times = ['10:00', '10:30', '11:00', '11:30', '12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00']

            for time in timeslist:
                times.remove(time)
            
            self.Label = Label(self.UpdateAppointmentFrame, text='Time of Appointment:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=320)
            self.Var.set('Select...')
            self.Entry = OptionMenu(self.UpdateAppointmentFrame,self.Var,*times).place(x=160, y=320)
        elif Data == 'Start Location':
            self.Label = Label(self.UpdateAppointmentFrame, text='Start Location:', fg='black', bg='white', font=('Ariel',10)).place(x=20,y=320)
            self.Entry = Entry(self.UpdateAppointmentFrame, width=60, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=120,y=320)
            self.Entry2 = Entry(self.UpdateAppointmentFrame, width=35, font=('ariel',10), bg='grey88', textvariable=self.Var2).place(x=120, y=345)
            self.Label2 = Label(self.UpdateAppointmentFrame, text='Postcode:', fg='black', bg='white', font=('Ariel',10)).place(x=400,y=345)
            self.Entry3 = Entry(self.UpdateAppointmentFrame, width=10, font=('ariel',10), bg='grey88', textvariable=self.Var3).place(x=470,y=345)
        elif Data == 'Destination':
            self.Label = Label(self.UpdateAppointmentFrame, text='Destination:', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=320)
            self.Entry = Entry(self.UpdateAppointmentFrame, width=60, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=120, y=320)
            self.Entry2 = Entry(self.UpdateAppointmentFrame, width=35, font=('ariel',10), bg='grey88', textvariable=self.Var2).place(x=120, y=345)
            self.Label2 = Label(self.UpdateAppointmentFrame, text='Postcode:', fg='black', bg='white', font=('Ariel',10)).place(x=400,y=345)
            self.Entry3 = Entry(self.UpdateAppointmentFrame, width=10, font=('ariel',10), bg='grey88', textvariable=self.Var3).place(x=470,y=345)
        elif Data == 'Expenses Paid?':
            self.Label = Label(self.UpdateAppointmentFrame, text='Expenses Paid?', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=320)
            self.Var.set('Select...')
            self.Entry = OptionMenu(self.UpdateAppointmentFrame, self.Var, 'Yes', 'No').place(x=175,y=320)


        updatebutton = Button(self.UpdateAppointmentFrame, text='Update', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.UpdateAppointment3).place(x=20, y=440)

    def UpdateAppointment3(self):
        database = sqlite3.connect('Appointments.db')
        ID = self.AppointmentID.get()
        Data = self.AppointmentData.get()
        Var = self.Var.get()
        Var2 = self.Var2.get()
        Var3 = self.Var3.get()

        #APPOINTMENTID, VOLUNTEERID, SERVICE_USERID, DATE_OF_APPOINTMENT, TIME_OF_APPOINTMENT, START_LOCATION, DESTINATION, EXPENSES_PAID
        
        if Data == 'Volunteer ID':
            database.execute("UPDATE APPOINTMENTS SET VOLUNTEERID = ? WHERE APPOINTMENTID = ?", (Var,ID));
            database.commit()
        elif Data == 'Service User ID':
            database.execute('UPDATE APPOINTMENTS SET SERVICE_USERID = ? WHERE APPOINTMENTID = ?', (Var,ID));
            database.commit()
        elif Data == 'Date of Appointment':
            date = Var + '/' + Var2 + '/' + Var3
            database.execute('UPDATE APPOINTMENTS SET DATE_OF_APPOINTMENT = ? WHERE APPOINTMENTID = ?', (date,ID));
            database.commit()
        elif Data == 'Time of Appointment':
            database.execute('UPDATE APPOINTMENTS SET TIME_OF_APPOINTMENT = ? WHERE APPOINTMENTID = ?', (Var,ID));
            database.commit()
        elif Data == 'Start Location':
            address1 = Var + ' ' + Var2 + ', ' + Var3
            database.execute('UPDATE APPOINTMENTS SET START_LOCATION = ? WHERE APPOINTMENTID = ?', (address1,ID));
            database.commit()
        elif Data == 'Destination':
            address2 = Var + ' ' + Var2 + ', ' + Var3
            database.execute('UPDATE APPOINTMENTS SET DESTINATION = ? WHERE APPOINTMENTID = ?', (address2,ID));
            database.commit()
        elif Data == 'Expenses Paid?':
            database.execute('UPDATE APPOINTMENTS SET EXPENSES_PAID = ? WHERE APPOINTMENTID = ?', (Var,ID));
            database.commit()

        self.DisplayAllAppointments()

    def DisplayAllAppointments(self):
        self.ClearWindow()
        self.master.geometry("1000x600")
        self.master.title("Display All Appointments")

        self.DisplayAllAppointmentFrame = Frame(self.master)
        self.DisplayAllAppointmentFrame.pack()
        self.DisplayAllAppointmentFrame.grid_rowconfigure(0, weight=1)
        self.DisplayAllAppointmentFrame.grid_columnconfigure(0, weight=1)

        xscrollbar = Scrollbar(self.DisplayAllAppointmentFrame, orient=HORIZONTAL)
        xscrollbar.grid(row=1, column=0, sticky=E+W)
        yscrollbar = Scrollbar(self.DisplayAllAppointmentFrame)
        yscrollbar.grid(row=0, column=1, sticky=N+S)
        
        background = Canvas(self.DisplayAllAppointmentFrame, width=1000, height=600, scrollregion=(0, 0, 2500, 1000),
                xscrollcommand=xscrollbar.set,
                yscrollcommand=yscrollbar.set)

        xscrollbar.config(command=background.xview)
        yscrollbar.config(command=background.yview)

        background.create_rectangle(0, 0, 2500, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 2500, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 2500, 1000, fill="white", outline='white')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(530,50,text='Displaying All Appointments', font=('comic sans ms',50), fill='violetred4')

        #homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        #homebutton.place(x=40,y=110)

        background.grid(row=0, column=0, sticky=N+S+E+W)

        self.Day = StringVar()
        self.Month = StringVar()
        self.Year = StringVar()
        self.Data = StringVar()
        self.Data2 = StringVar()

        background.create_text(60,130,text = 'Select Date:', fill='black', font=('Ariel',11))
        background.create_window(120,130,window = Entry(self.DisplayAllAppointmentFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Day))
        background.create_text(137,130,text='/', fill='black', font=('ariel',11))
        background.create_window(153,130,window = Entry(self.DisplayAllAppointmentFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Month))
        background.create_text(170,130,text='/', fill='black', font=('ariel',11))
        background.create_window(193,130,window = Entry(self.DisplayAllAppointmentFrame, width=4, font=('ariel',10), bg='grey88', textvariable=self.Year))
        background.create_text(300,130,text='Select Filter:', fill='black', font=('Ariel',11))
        background.create_window(400,130,window=OptionMenu(self.DisplayAllAppointmentFrame, self.Data, 'Volunteer:','Service User:'))
        background.create_window(570,130,window = Entry(self.DisplayAllAppointmentFrame, width=30, font=('ariel',10), bg='grey88', textvariable=self.Data2))
        background.create_window(650,130,window = Button(self.DisplayAllAppointmentFrame, text='Display', font=('Ariel',11), fg='black',bg='darkseagreen3',relief=FLAT, command=self.DisplayAllAppointmentsDate))

        background.create_text(60,165, text='Appointment ID', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(230,165, text='Volunteer Firstname', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(420,165, text='Volunteer Surname', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(620,165, text='Service User Firstname', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(820,165, text='Service User Surname', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(1000,165, text='Date of Appointment', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(1170,165, text='Time of Appointment', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(1530,165, text='Start Location', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(2080,165, text='Destination', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(2420,165, text='Expenses Paid?', fill='violetred4', font=('Ariel',11,'underline'))

        #APPOINTMENTID, VOLUNTEERID, SERVICE_USERID, DATE_OF_APPOINTMENT, TIME_OF_APPOINTMENT, START_LOCATION, DESTINATION, EXPENSES_PAID

        AIDTotal = self.ATotalID()
        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT FIRST_NAME FROM VOLUNTEERS,APPOINTMENTS WHERE APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID');
        vfirstname = cursor.fetchall()
        cursor.execute('SELECT LAST_NAME FROM VOLUNTEERS,APPOINTMENTS WHERE APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID');
        vlastname = cursor.fetchall()
        cursor.execute('SELECT FIRST_NAME FROM SERVICE_USERS,APPOINTMENTS WHERE APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID');
        SUfirstname = cursor.fetchall()
        cursor.execute('SELECT LAST_NAME FROM SERVICE_USERS,APPOINTMENTS WHERE APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID');
        SUlastname = cursor.fetchall()
        cursor.execute('SELECT DATE_OF_APPOINTMENT FROM APPOINTMENTS');
        dateofapp = cursor.fetchall()
        cursor.execute('SELECT TIME_OF_APPOINTMENT FROM APPOINTMENTS');
        timeofapp = cursor.fetchall()
        cursor.execute('SELECT START_LOCATION FROM APPOINTMENTS');
        startloc = cursor.fetchall()
        cursor.execute('SELECT DESTINATION FROM APPOINTMENTS');
        destination = cursor.fetchall()
        cursor.execute('SELECT EXPENSES_PAID FROM APPOINTMENTS');
        expensespaid = cursor.fetchall()
    
        
        yvalue=190
        for a in range(1,(AIDTotal+1)):
            background.create_text(50,yvalue, font=('ariel',10), fill='black', text=a)
            yvalue += 20
        
        yvalue=190
        i=0
        for a in range(0,AIDTotal):
            vfirstname2 = vfirstname[i][0]
            background.create_text(230,yvalue, font=('ariel',10), fill='black', text=vfirstname2)
            i += 1
            yvalue += 20

        yvalue=190
        i=0
        for a in range(0,AIDTotal):
            vlastname2 = vlastname[i][0]
            background.create_text(420,yvalue, font=('ariel',10), fill='black', text=vlastname2)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,AIDTotal):
            SUfirstname2 = SUfirstname[i][0]
            background.create_text(620,yvalue, font=('ariel',10), fill='black', text=SUfirstname2)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,AIDTotal):
            SUlastname2 = SUlastname[i][0]
            background.create_text(820,yvalue, font=('ariel',10), fill='black', text=SUlastname2)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,AIDTotal):
            dateofapp2 = dateofapp[i][0]
            background.create_text(1000,yvalue, font=('ariel',10), fill='black', text=dateofapp2)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,AIDTotal):
            timeofapp2 = timeofapp[i][0]
            background.create_text(1170,yvalue, font=('ariel',10), fill='black', text=timeofapp2)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,AIDTotal):
            startloc2 = startloc[i][0]
            background.create_text(1530,yvalue, font=('ariel',10), fill='black', text=startloc2)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,AIDTotal):
            destination2 = destination[i][0]
            background.create_text(2080,yvalue, font=('ariel',10), fill='black', text=destination2)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,AIDTotal):
            expensespaid2 = expensespaid[i][0]
            background.create_text(2420,yvalue, font=('ariel',10), fill='black', text=expensespaid2)
            i += 1
            yvalue += 20

    def DisplayAllAppointmentsDate(self):
        self.ClearWindow()
        self.master.geometry("1000x600")
        self.master.title("Display All Appointments")

        self.DisplayAllAppointment2Frame = Frame(self.master)
        self.DisplayAllAppointment2Frame.pack()
        self.DisplayAllAppointment2Frame.grid_rowconfigure(0, weight=1)
        self.DisplayAllAppointment2Frame.grid_columnconfigure(0, weight=1)

        xscrollbar = Scrollbar(self.DisplayAllAppointment2Frame, orient=HORIZONTAL)
        xscrollbar.grid(row=1, column=0, sticky=E+W)
        yscrollbar = Scrollbar(self.DisplayAllAppointment2Frame)
        yscrollbar.grid(row=0, column=1, sticky=N+S)
        
        background = Canvas(self.DisplayAllAppointment2Frame, width=1000, height=600, scrollregion=(0, 0, 2500, 1000),
                xscrollcommand=xscrollbar.set,
                yscrollcommand=yscrollbar.set)

        xscrollbar.config(command=background.xview)
        yscrollbar.config(command=background.yview)

        background.create_rectangle(0, 0, 2500, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 2500, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 2500, 1000, fill="white", outline='white')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Displaying All Appointments', font=('comic sans ms',50), fill='violetred4')
        #homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        #homebutton.place(x=40,y=110)

        background.grid(row=0, column=0, sticky=N+S+E+W)

        selectbutton = Button(self.DisplayAllAppointment2Frame, text='Select Different Date', font=('Ariel',11), fg='black',bg='darkseagreen3',relief=FLAT, command=self.DisplayAllAppointments).place(x=20, y=115)
        
        background.create_text(60,165, text='Appointment ID', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(230,165, text='Volunteer Firstname', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(420,165, text='Volunteer Surname', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(620,165, text='Service User Firstname', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(820,165, text='Service User Surname', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(1000,165, text='Date of Appointment', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(1170,165, text='Time of Appointment', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(1530,165, text='Start Location', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(2080,165, text='Destination', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(2420,165, text='Expenses Paid?', fill='violetred4', font=('Ariel',11,'underline'))
        
        #APPOINTMENTID, VOLUNTEERID, SERVICE_USERID, DATE_OF_APPOINTMENT, TIME_OF_APPOINTMENT, START_LOCATION, DESTINATION, EXPENSES_PAID

        AIDTotal = self.ATotalID()
        day = self.Day.get()
        month = self.Month.get()
        year = self.Year.get()
        date = day + '/' + month + '/' + year

        data = self.Data.get()
        data2 = self.Data2.get()
        names = data2.split(' ')
        
        
        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()

        if data == 'Select...' or data2 == '':
            cursor.execute('SELECT APPOINTMENTID FROM APPOINTMENTS WHERE DATE_OF_APPOINTMENT = ?', (date, ));
            appid = cursor.fetchall()
            cursor.execute("SELECT COUNT(APPOINTMENTID) FROM APPOINTMENTS WHERE DATE_OF_APPOINTMENT = ?", (date, ));
            maxappointments = cursor.fetchall()[0][0]
            print(maxappointments)
            cursor.execute('SELECT FIRST_NAME FROM VOLUNTEERS,APPOINTMENTS WHERE DATE_OF_APPOINTMENT = ? AND APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID', (date, ));
            vfirstname = cursor.fetchall()
            cursor.execute('SELECT LAST_NAME FROM VOLUNTEERS,APPOINTMENTS WHERE APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID AND DATE_OF_APPOINTMENT = ?', (date, ));
            vlastname = cursor.fetchall()
            cursor.execute('SELECT FIRST_NAME FROM SERVICE_USERS,APPOINTMENTS WHERE APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID AND DATE_OF_APPOINTMENT = ?', (date, ));
            SUfirstname = cursor.fetchall()
            cursor.execute('SELECT LAST_NAME FROM SERVICE_USERS,APPOINTMENTS WHERE APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID AND DATE_OF_APPOINTMENT = ?', (date, ));
            SUlastname = cursor.fetchall()
            cursor.execute('SELECT TIME_OF_APPOINTMENT FROM APPOINTMENTS WHERE DATE_OF_APPOINTMENT = ?', (date, ));
            timeofapp = cursor.fetchall()
            cursor.execute('SELECT START_LOCATION FROM APPOINTMENTS WHERE DATE_OF_APPOINTMENT = ?', (date, ));
            startloc = cursor.fetchall()
            cursor.execute('SELECT DESTINATION FROM APPOINTMENTS WHERE DATE_OF_APPOINTMENT = ?', (date, ));
            destination = cursor.fetchall()
            cursor.execute('SELECT EXPENSES_PAID FROM APPOINTMENTS WHERE DATE_OF_APPOINTMENT = ?', (date, ));
            expensespaid = cursor.fetchall()
            cursor.execute('SELECT MIN(TIME_OF_APPOINTMENT) FROM APPOINTMENTS WHERE DATE_OF_APPOINTMENT = ?', (date, ));
            mintimeofapp = cursor.fetchall()[0][0]
            cursor.execute('SELECT MAX(TIME_OF_APPOINTMENT) FROM APPOINTMENTS WHERE DATE_OF_APPOINTMENT = ?', (date, ));
            maxtimeofapp = cursor.fetchall()[0][0]

        elif data == 'Volunteer:' and data2 != '':
            firstname = names[0]
            lastname = names[1]
            
            cursor.execute('SELECT APPOINTMENTID FROM APPOINTMENTS,VOLUNTEERS WHERE DATE_OF_APPOINTMENT = ? AND VOLUNTEERS.FIRST_NAME = ? AND VOLUNTEERS.LAST_NAME = ? AND APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID', (date,firstname,lastname));
            appid = cursor.fetchall()
            cursor.execute("SELECT COUNT(APPOINTMENTID) FROM APPOINTMENTS,VOLUNTEERS WHERE DATE_OF_APPOINTMENT = ? AND VOLUNTEERS.FIRST_NAME = ? AND VOLUNTEERS.LAST_NAME = ? AND APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID", (date,firstname,lastname));
            totalid = cursor.fetchall()[0][0]
            cursor.execute('SELECT VOLUNTEERS.FIRST_NAME FROM APPOINTMENTS,VOLUNTEERS WHERE DATE_OF_APPOINTMENT = ? AND VOLUNTEERS.FIRST_NAME = ? AND VOLUNTEERS.LAST_NAME = ? AND APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID', (date,firstname,lastname));
            vfirstname = cursor.fetchall()
            cursor.execute('SELECT VOLUNTEERS.LAST_NAME FROM APPOINTMENTS,VOLUNTEERS WHERE DATE_OF_APPOINTMENT = ? AND VOLUNTEERS.FIRST_NAME = ? AND VOLUNTEERS.LAST_NAME = ? AND APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID', (date,firstname,lastname));
            vlastname = cursor.fetchall()
            cursor.execute('SELECT SERVICE_USERS.FIRST_NAME FROM SERVICE_USERS,APPOINTMENTS,VOLUNTEERS WHERE DATE_OF_APPOINTMENT = ? AND VOLUNTEERS.FIRST_NAME = ? AND VOLUNTEERS.LAST_NAME = ? AND APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID AND APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID', (date,firstname,lastname));
            SUfirstname = cursor.fetchall()
            cursor.execute('SELECT SERVICE_USERS.LAST_NAME FROM SERVICE_USERS,APPOINTMENTS,VOLUNTEERS WHERE DATE_OF_APPOINTMENT = ? AND VOLUNTEERS.FIRST_NAME = ? AND VOLUNTEERS.LAST_NAME = ? AND APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID AND APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID', (date,firstname,lastname));
            SUlastname = cursor.fetchall()
            cursor.execute('SELECT TIME_OF_APPOINTMENT FROM APPOINTMENTS,VOLUNTEERS WHERE DATE_OF_APPOINTMENT = ? AND VOLUNTEERS.FIRST_NAME = ? AND VOLUNTEERS.LAST_NAME = ? AND APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID', (date,firstname,lastname));
            timeofapp = cursor.fetchall()
            cursor.execute('SELECT START_LOCATION FROM APPOINTMENTS,VOLUNTEERS WHERE DATE_OF_APPOINTMENT = ? AND VOLUNTEERS.FIRST_NAME = ? AND VOLUNTEERS.LAST_NAME = ? AND APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID', (date,firstname,lastname));
            startloc = cursor.fetchall()
            cursor.execute('SELECT DESTINATION FROM APPOINTMENTS,VOLUNTEERS WHERE DATE_OF_APPOINTMENT = ? AND VOLUNTEERS.FIRST_NAME = ? AND VOLUNTEERS.LAST_NAME = ? AND APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID', (date,firstname,lastname));
            destination = cursor.fetchall()
            cursor.execute('SELECT EXPENSES_PAID FROM APPOINTMENTS,VOLUNTEERS WHERE DATE_OF_APPOINTMENT = ? AND VOLUNTEERS.FIRST_NAME = ? AND VOLUNTEERS.LAST_NAME = ? AND APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID', (date,firstname,lastname));
            expensespaid = cursor.fetchall()
            cursor.execute('SELECT COUNT(APPOINTMENTID) FROM APPOINTMENTS,VOLUNTEERS WHERE DATE_OF_APPOINTMENT = ? AND VOLUNTEERS.FIRST_NAME = ? AND VOLUNTEERS.LAST_NAME = ? AND APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID', (date,firstname,lastname));
            maxappointments = cursor.fetchall()[0][0]
            cursor.execute('SELECT MIN(TIME_OF_APPOINTMENT) FROM APPOINTMENTS,VOLUNTEERS WHERE DATE_OF_APPOINTMENT = ? AND VOLUNTEERS.FIRST_NAME = ? AND VOLUNTEERS.LAST_NAME = ? AND APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID', (date,firstname,lastname));
            mintimeofapp = cursor.fetchall()[0][0]
            cursor.execute('SELECT MAX(TIME_OF_APPOINTMENT) FROM APPOINTMENTS,VOLUNTEERS WHERE DATE_OF_APPOINTMENT = ? AND VOLUNTEERS.FIRST_NAME = ? AND VOLUNTEERS.LAST_NAME = ? AND APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID', (date,firstname,lastname));
            maxtimeofapp = cursor.fetchall()[0][0]

        elif data == 'Service User:' and data2 != '':
            firstname = names[0]
            lastname = names[1]
            
            cursor.execute('SELECT APPOINTMENTID FROM APPOINTMENTS,SERVICE_USERS WHERE DATE_OF_APPOINTMENT = ? AND SERVICE_USERS.FIRST_NAME = ? AND SERVICE_USERS.LAST_NAME = ? AND APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID', (date,firstname,lastname));
            appid = cursor.fetchall()
            cursor.execute("SELECT COUNT(APPOINTMENTID) FROM APPOINTMENTS,SERVICE_USERS WHERE DATE_OF_APPOINTMENT = ? AND SERVICE_USERS.FIRST_NAME = ? AND SERVICE_USERS.LAST_NAME = ? AND APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID", (date,firstname,lastname));
            totalid = cursor.fetchall()[0][0]
            cursor.execute('SELECT VOLUNTEERS.FIRST_NAME FROM APPOINTMENTS,VOLUNTEERS,SERVICE_USERS WHERE DATE_OF_APPOINTMENT = ? AND SERVICE_USERS.FIRST_NAME = ? AND SERVICE_USERS.LAST_NAME = ? AND APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID AND APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID', (date,firstname,lastname));
            vfirstname = cursor.fetchall()
            cursor.execute('SELECT VOLUNTEERS.LAST_NAME FROM APPOINTMENTS,VOLUNTEERS,SERVICE_USERS WHERE DATE_OF_APPOINTMENT = ? AND SERVICE_USERS.FIRST_NAME = ? AND SERVICE_USERS.LAST_NAME = ? AND APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID AND APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID', (date,firstname,lastname));
            vlastname = cursor.fetchall()
            cursor.execute('SELECT SERVICE_USERS.FIRST_NAME FROM SERVICE_USERS,APPOINTMENTS WHERE DATE_OF_APPOINTMENT = ? AND SERVICE_USERS.FIRST_NAME = ? AND SERVICE_USERS.LAST_NAME = ? AND APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID', (date,firstname,lastname));
            SUfirstname = cursor.fetchall()
            cursor.execute('SELECT SERVICE_USERS.LAST_NAME FROM SERVICE_USERS,APPOINTMENTS WHERE DATE_OF_APPOINTMENT = ? AND SERVICE_USERS.FIRST_NAME = ? AND SERVICE_USERS.LAST_NAME = ? AND APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID', (date,firstname,lastname));
            SUlastname = cursor.fetchall()
            cursor.execute('SELECT TIME_OF_APPOINTMENT FROM APPOINTMENTS,SERVICE_USERS WHERE DATE_OF_APPOINTMENT = ? AND SERVICE_USERS.FIRST_NAME = ? AND SERVICE_USERS.LAST_NAME = ? AND APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID', (date,firstname,lastname));
            timeofapp = cursor.fetchall()
            cursor.execute('SELECT START_LOCATION FROM APPOINTMENTS,SERVICE_USERS WHERE DATE_OF_APPOINTMENT = ? AND SERVICE_USERS.FIRST_NAME = ? AND SERVICE_USERS.LAST_NAME = ? AND APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID', (date,firstname,lastname));
            startloc = cursor.fetchall()
            cursor.execute('SELECT DESTINATION FROM APPOINTMENTS,SERVICE_USERS WHERE DATE_OF_APPOINTMENT = ? AND SERVICE_USERS.FIRST_NAME = ? AND SERVICE_USERS.LAST_NAME = ? AND APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID', (date,firstname,lastname));
            destination = cursor.fetchall()
            cursor.execute('SELECT EXPENSES_PAID FROM APPOINTMENTS,SERVICE_USERS WHERE DATE_OF_APPOINTMENT = ? AND SERVICE_USERS.FIRST_NAME = ? AND SERVICE_USERS.LAST_NAME = ? AND APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID', (date,firstname,lastname));
            expensespaid = cursor.fetchall()
            cursor.execute('SELECT COUNT(APPOINTMENTID) FROM APPOINTMENTS,SERVICE_USERS WHERE DATE_OF_APPOINTMENT = ? AND SERVICE_USERS.FIRST_NAME = ? AND SERVICE_USERS.LAST_NAME = ? AND APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID', (date,firstname,lastname));
            maxappointments = cursor.fetchall()[0][0]
            cursor.execute('SELECT MIN(TIME_OF_APPOINTMENT) FROM APPOINTMENTS,SERVICE_USERS WHERE DATE_OF_APPOINTMENT = ? AND SERVICE_USERS.FIRST_NAME = ? AND SERVICE_USERS.LAST_NAME = ? AND APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID', (date,firstname,lastname));
            mintimeofapp = cursor.fetchall()[0][0]
            cursor.execute('SELECT MAX(TIME_OF_APPOINTMENT) FROM APPOINTMENTS,SERVICE_USERS WHERE DATE_OF_APPOINTMENT = ? AND SERVICE_USERS.FIRST_NAME = ? AND SERVICE_USERS.LAST_NAME = ? AND APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID', (date,firstname,lastname));
            mintimeofapp = cursor.fetchall()[0][0]

        else:
            self.DisplayAllAppointments()
            
    
        yvalue=190
        i = 0
        for a in range(0,maxappointments):
            appid2 = appid[i][0]
            background.create_text(60,yvalue, font=('ariel',10), fill='black', text=appid2)
            i += 1
            yvalue += 20
        
        yvalue=190
        i=0
        for a in range(0,maxappointments):
            vfirstname2 = vfirstname[i][0]
            background.create_text(230,yvalue, font=('ariel',10), fill='black', text=vfirstname2)
            i += 1
            yvalue += 20

        yvalue=190
        i=0
        for a in range(0,maxappointments):
            vlastname2 = vlastname[i][0]
            background.create_text(420,yvalue, font=('ariel',10), fill='black', text=vlastname2)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,maxappointments):
            SUfirstname2 = SUfirstname[i][0]
            background.create_text(620,yvalue, font=('ariel',10), fill='black', text=SUfirstname2)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,maxappointments):
            SUlastname2 = SUlastname[i][0]
            background.create_text(820,yvalue, font=('ariel',10), fill='black', text=SUlastname2)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,maxappointments):
            background.create_text(1000,yvalue, font=('ariel',10), fill='black', text=date)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,maxappointments):
            timeofapp2 = timeofapp[i][0]
            background.create_text(1170,yvalue, font=('ariel',10), fill='black', text=timeofapp2)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,maxappointments):
            startloc2 = startloc[i][0]
            background.create_text(1530,yvalue, font=('ariel',10), fill='black', text=startloc2)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,maxappointments):
            destination2 = destination[i][0]
            background.create_text(2080,yvalue, font=('ariel',10), fill='black', text=destination2)
            i += 1
            yvalue += 20

        yvalue = 190
        i=0
        for a in range(0,maxappointments):
            expensespaid2 = expensespaid[i][0]
            background.create_text(2420,yvalue, font=('ariel',10), fill='black', text=expensespaid2)
            i += 1
            yvalue += 20

        background.create_text(96,yvalue+30, font=('ariel',10), fill='black', text='Total Appointments Today: ' + str(maxappointments))
        background.create_text(120,yvalue+60, font=('ariel',10), fill='black', text='First Appointment Today Is At: ' + str(mintimeofapp))
        background.create_text(120,yvalue+90, font=('ariel',10), fill='black', text='Last Appointment Today Is At: ' + str(maxtimeofapp))
     

    def DeleteAppointments(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Delete Appointment')

        self.DeleteAppointmentFrame = Frame(self.master)
        self.DeleteAppointmentFrame.pack()

        background = Canvas(self.DeleteAppointmentFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        background.create_line(0,250,1000,250, fill='black')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Delete Appointment', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)

        MaxID = self.ATotalID()

        self.AppointmentID = StringVar()
        self.AppointmentIDText = Label(self.DeleteAppointmentFrame, text='Appointment ID:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=200)
        self.AppointmentIDEntry = Spinbox(self.DeleteAppointmentFrame, width = 4, from_=0, to=MaxID, relief=FLAT, bg='grey88', textvariable = self.AppointmentID, command=self.DeleteAppointments2).place(x=130, y=200)

    def DeleteAppointments2(self):
        try:
            self.Vfirstname.set('')
        except:
            pass
        try:
            self.Vlastname.set('')
        except:
            pass
        try:
            self.SUfirstname.set('')
        except:
            pass
        try:
            self.SUlastname.set('')
        except:
            pass
        try:
            self.date_of_app.set('')
        except:
            pass
        try:
            self.time_of_app.set('')
        except:
            pass
        try:
            self.startloc.set('')
        except:
            pass
        try:
            self.destination.set('')
        except:
            pass
        try:
            self.expensespaid.set('')
        except:
            pass
        
        self.Vfirstname = StringVar()
        self.Vlastname = StringVar()
        self.SUfirstname = StringVar()
        self.SUlastname = StringVar()
        self.date_of_app = StringVar()
        self.time_of_app = StringVar()
        self.startloc = StringVar()
        self.destination = StringVar()
        self.expensespaid = StringVar()
        AppID2 = self.AppointmentID.get()
        
        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT FIRST_NAME FROM VOLUNTEERS,APPOINTMENTS WHERE APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID');
        self.Vfirstname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT LAST_NAME FROM VOLUNTEERS,APPOINTMENTS WHERE APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID');
        self.Vlastname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT FIRST_NAME FROM SERVICE_USERS,APPOINTMENTS WHERE APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID');
        self.SUfirstname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT LAST_NAME FROM SERVICE_USERS,APPOINTMENTS WHERE APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID');
        self.SUlastname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT DATE_OF_APPOINTMENT FROM APPOINTMENTS WHERE APPOINTMENTID = ?', (AppID2));
        self.date_of_app.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT TIME_OF_APPOINTMENT FROM APPOINTMENTS WHERE APPOINTMENTID = ?', (AppID2));
        self.time_of_app.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT START_LOCATION FROM APPOINTMENTS WHERE APPOINTMENTID = ?', (AppID2));
        self.startloc.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT DESTINATION FROM APPOINTMENTS WHERE APPOINTMENTID = ?', (AppID2));
        self.destination.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT EXPENSES_PAID FROM APPOINTMENTS WHERE APPOINTMENTID = ?', (AppID2));
        self.expensespaid.set(cursor.fetchall()[0][0])
        
        self.VFirstnameText = Label(self.DeleteAppointmentFrame, text='Volunteer Firstname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=280)
        self.VFirstnameEntry = Label(self.DeleteAppointmentFrame, font=('ariel',10), bg='white', textvariable=self.Vfirstname).place(x=175,y=280)
        self.VLastnameText = Label(self.DeleteAppointmentFrame, text='Volunteer Lastname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=400,y=280)
        self.VLastnameEntry = Label(self.DeleteAppointmentFrame, font=('ariel',10), bg='white', textvariable=self.Vlastname).place(x=550,y=280)
        self.SUFirstnameText = Label(self.DeleteAppointmentFrame, text='Service User Firstname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=320)
        self.SUFirstnameEntry = Label(self.DeleteAppointmentFrame, font=('ariel',10), bg='white', textvariable=self.SUfirstname).place(x=175,y=320)
        self.SULastnameText = Label(self.DeleteAppointmentFrame, text='Service User Lastname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=400,y=320)
        self.SULastnameEntry = Label(self.DeleteAppointmentFrame, font=('ariel',10), bg='white', textvariable=self.SUlastname).place(x=550,y=320)
        self.DateofAppText = Label(self.DeleteAppointmentFrame, text='Date of Appointment:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20,y=360)
        self.DateofAppEntry = Label(self.DeleteAppointmentFrame, font=('ariel',10), bg='white', textvariable=self.date_of_app).place(x=175,y=360)
        self.TimeofAppText = Label(self.DeleteAppointmentFrame, text='Time of Appointment:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=400)
        self.TimeofAppEntry = Label(self.DeleteAppointmentFrame, font=('ariel',10), bg='white', textvariable=self.time_of_app).place(x=175, y=400)
        self.StartLocationText = Label(self.DeleteAppointmentFrame, text='Start Location:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=440)
        self.StartLocationEntry = Label(self.DeleteAppointmentFrame, font=('ariel',10), bg='white', textvariable=self.startloc).place(x=175,y=440)
        self.DestinationText = Label(self.DeleteAppointmentFrame, text='Destination:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=480)
        self.DestinationEntry = Label(self.DeleteAppointmentFrame, font=('ariel',10), bg='white', textvariable=self.destination).place(x=175,y=480)
        self.ExpensesPaidText = Label(self.DeleteAppointmentFrame, text='Expenses Paid?', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=520)
        self.ExpensesPaidEntry = Label(self.DeleteAppointmentFrame, font=('ariel',10), bg='white', textvariable=self.destination).place(x=175,y=520)

        deletebutton = Button(self.DeleteAppointmentFrame, text='Delete', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.DeleteAppointments3).place(x=700, y=190)

        
    def DeleteAppointments3(self):
        database = sqlite3.connect('Appointments.db')
        ID = self.AppointmentID.get()

        database.execute("DELETE FROM APPOINTMENTS WHERE APPOINTMENTID = ?", (ID));
        database.commit()
        
        database.execute("UPDATE APPOINTMENTS SET APPOINTMENTID = APPOINTMENTID-1 WHERE APPOINTMENTID > ?", (ID));
        database.commit()

        self.DisplayAllAppointments()

    def ExpensesForm(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Search Appointment')

        self.ExpensesFrame = Frame(self.master)
        self.ExpensesFrame.pack()

        background = Canvas(self.ExpensesFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        background.create_line(0,250,1000,250, fill='black')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Expenses Form', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)

        MaxID = self.ATotalID()

        self.AppID = StringVar()
        self.AppIDText = Label(self.ExpensesFrame, text='Select Appointment:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=200)
        self.AppIDEntry = Spinbox(self.ExpensesFrame, width = 4, from_=0, to=MaxID, relief=FLAT, bg='grey88', textvariable = self.AppID, command=self.ExpensesForm2).place(x=150, y=200)

    def ExpensesForm2(self):
        try:
            self.Vfirstname.set('')
        except:
            pass
        try:
            self.Vlastname.set('')
        except:
            pass
        try:
            self.SUfirstname.set('')
        except:
            pass
        try:
            self.SUlastname.set('')
        except:
            pass
        try:
            self.date_of_app.set('')
        except:
            pass
        try:
            self.time_of_app.set('')
        except:
            pass
        try:
            self.startloc.set('')
        except:
            pass
        try:
            self.destination.set('')
        except:
            pass
        try:
            self.expensespaid.set('')
        except:
            pass
        
        self.Vfirstname = StringVar()
        self.Vlastname = StringVar()
        self.SUfirstname = StringVar()
        self.SUlastname = StringVar()
        self.date_of_app = StringVar()
        self.time_of_app = StringVar()
        self.startloc = StringVar()
        self.destination = StringVar()
        self.expensespaid = StringVar()
        AppID2 = self.AppID.get()
        
        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT FIRST_NAME FROM VOLUNTEERS,APPOINTMENTS WHERE APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID');
        self.Vfirstname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT LAST_NAME FROM VOLUNTEERS,APPOINTMENTS WHERE APPOINTMENTS.VOLUNTEERID = VOLUNTEERS.VOLUNTEERID');
        self.Vlastname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT FIRST_NAME FROM SERVICE_USERS,APPOINTMENTS WHERE APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID');
        self.SUfirstname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT LAST_NAME FROM SERVICE_USERS,APPOINTMENTS WHERE APPOINTMENTS.SERVICE_USERID = SERVICE_USERS.SERVICE_USERID');
        self.SUlastname.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT DATE_OF_APPOINTMENT FROM APPOINTMENTS WHERE APPOINTMENTID = ?', (AppID2));
        self.date_of_app.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT TIME_OF_APPOINTMENT FROM APPOINTMENTS WHERE APPOINTMENTID = ?', (AppID2));
        self.time_of_app.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT START_LOCATION FROM APPOINTMENTS WHERE APPOINTMENTID = ?', (AppID2));
        self.startloc.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT DESTINATION FROM APPOINTMENTS WHERE APPOINTMENTID = ?', (AppID2));
        self.destination.set(cursor.fetchall()[0][0])
        cursor.execute('SELECT EXPENSES_PAID FROM APPOINTMENTS WHERE APPOINTMENTID = ?', (AppID2));
        self.expensespaid.set(cursor.fetchall()[0][0])
        
        self.VFirstnameText = Label(self.ExpensesFrame, text='Volunteer Firstname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=280)
        self.VFirstnameEntry = Label(self.ExpensesFrame, font=('ariel',10), bg='white', textvariable=self.Vfirstname).place(x=175,y=280)
        self.VLastnameText = Label(self.ExpensesFrame, text='Volunteer Lastname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=400,y=280)
        self.VLastnameEntry = Label(self.ExpensesFrame, font=('ariel',10), bg='white', textvariable=self.Vlastname).place(x=550,y=280)
        self.SUFirstnameText = Label(self.ExpensesFrame, text='Service User Firstname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=320)
        self.SUFirstnameEntry = Label(self.ExpensesFrame, font=('ariel',10), bg='white', textvariable=self.SUfirstname).place(x=175,y=320)
        self.SULastnameText = Label(self.ExpensesFrame, text='Service User Lastname:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=400,y=320)
        self.SULastnameEntry = Label(self.ExpensesFrame, font=('ariel',10), bg='white', textvariable=self.SUlastname).place(x=550,y=320)
        self.DateofAppText = Label(self.ExpensesFrame, text='Date of Appointment:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20,y=360)
        self.DateofAppEntry = Label(self.ExpensesFrame, font=('ariel',10), bg='white', textvariable=self.date_of_app).place(x=175,y=360)
        self.TimeofAppText = Label(self.ExpensesFrame, text='Time of Appointment:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=400)
        self.TimeofAppEntry = Label(self.ExpensesFrame, font=('ariel',10), bg='white', textvariable=self.time_of_app).place(x=175, y=400)
        self.StartLocationText = Label(self.ExpensesFrame, text='Start Location:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=440)
        self.StartLocationEntry = Label(self.ExpensesFrame, font=('ariel',10), bg='white', textvariable=self.startloc).place(x=175,y=440)
        self.DestinationText = Label(self.ExpensesFrame, text='Destination:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=480)
        self.DestinationEntry = Label(self.ExpensesFrame, font=('ariel',10), bg='white', textvariable=self.destination).place(x=175,y=480)
        self.ExpensesPaidText = Label(self.ExpensesFrame, text='Expenses Paid?', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20,y=520)
        self.ExpensesPaidEntry = Label(self.ExpensesFrame, font=('ariel',10), bg='white', textvariable=self.expensespaid).place(x=175,y=520)

        self.miles = StringVar()

        self.NumberofMilesText = Label(self.ExpensesFrame, text='Miles Driven:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=300, y=200)
        self.NumberofMilesEntry = Entry(self.ExpensesFrame, width=4, bg='grey88', font=('ariel',10), textvariable=self.miles).place(x=390, y=200)

        self.selectbutton = Button(self.ExpensesFrame, text='Select', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.ExpensesForm3).place(x=500, y=200)

    def ExpensesForm3(self):
        #remove label. round expenses to 2 decimal places. add new column to volunteer table. remove the apppointment once the expenses have been added to the table?
        #remove the amount once the appointment has been updated to the expenses paid says yes.
        
        miles = float(self.miles.get())

        expenses = 0

        if miles <= 0:
            Label(self.ExpensesFrame, text='ERROR! Invalid Number of Miles', fg='red', bg='white', font=('ariel',10,'bold')).place(x=580, y=200)
        elif miles > 0 and miles <= 3:
            expenses = 4
        else:
            miles -= 3
            amount = miles * 0.6
            expenses = 4 + amount

        print(expenses)
            



        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def AllLunchClubs(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Lunch Clubs')

        self.LunchClubsFrame = Frame(self.master)
        self.LunchClubsFrame.pack()
        self.LunchClubsFrame.grid_rowconfigure(0, weight=1)
        self.LunchClubsFrame.grid_columnconfigure(0, weight=1)

        yscrollbar = Scrollbar(self.LunchClubsFrame)
        yscrollbar.grid(row=0, column=1, sticky=N+S)

        background = Canvas(self.LunchClubsFrame, width=1700, height=1000, scrollregion=(0, 0, 1700, 1000),
                yscrollcommand=yscrollbar.set)


        yscrollbar.config(command=background.yview)

        background.create_rectangle(0, 0, 1700, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1700, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1700, 1000, fill="white", outline='white')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Displaying Lunch Clubs', font=('comic sans ms',50), fill='violetred4')

        background.grid(row=0, column=0, sticky=N+S+E+W)

        self.Day = StringVar()
        self.Month = StringVar()
        self.Year = StringVar()

        background.create_text(60,130,text = 'Select Date:', fill='black', font=('Ariel',11))
        background.create_window(120,130,window = Entry(self.LunchClubsFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Day))
        background.create_text(137,130,text='/', fill='black', font=('ariel',11))
        background.create_window(153,130,window = Entry(self.LunchClubsFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Month))
        background.create_text(170,130,text='/', fill='black', font=('ariel',11))
        background.create_window(193,130,window = Entry(self.LunchClubsFrame, width=4, font=('ariel',10), bg='grey88', textvariable=self.Year))
        background.create_window(250,130,window = Button(self.LunchClubsFrame, text='Display', font=('Ariel',11), fg='black',bg='darkseagreen3',relief=FLAT, command=self.DisplayLunchClubByDate))
    

        background.create_text(60,165, text='Lunch Club ID', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(250,165, text='Helpers', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(440,165, text='Service Users', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(600,165, text='Date of Club', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(720,165, text='Time of Club', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(850,165, text='Cost of Club', fill='violetred4', font=('Ariel',11,'underline'))
        
        

        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()

        #LUNCH_CLUBS:  VOLUNTEERID, SERVICE_USERID, DATE_OF_CLUB, TIME_OF_CLUB, COST

        cursor.execute('SELECT * FROM LUNCH_CLUBS');
        information=cursor.fetchall()

        maxid = self.LunchClubTotalID()

        y_value = 160
        idpos = 1
        for i in range(0,maxid):
            y_value += 30
            date = information[i][3]
            time = information[i][4]
            cost = information[i][5]
            background.create_text(60,y_value,text = idpos, fill='black', font=('Ariel',10))
            background.create_text(600,y_value,text=date, fill='black', font=('Ariel',10))
            background.create_text(720,y_value,text=time, fill='black', font=('Ariel',10))
            background.create_text(850,y_value,text='£'+cost, fill='black', font=('Ariel',10))
            idpos += 1
            y_value2 = y_value
            helpers = information[i][1]
            helperlist = helpers.split(', ')
            for name in helperlist:
                background.create_text(250,y_value2,text = name, fill='black', font=('Ariel',10))
                y_value2 += 20
            y_value3 = y_value
            susers = information[i][2]
            suserslist = susers.split(', ')
            for name in suserslist:
                background.create_text(440,y_value3,text = name, fill='black', font=('Ariel',10))
                y_value3 += 20
            if y_value2 > y_value3:
                y_value = y_value2
            elif y_value3 > y_value2:
                y_value = y_value3
            else:
                y_value = y_value2

##        y_value = 160
##        idpos = 1
##        for i in range(0,maxid):
##            y_value += 30
##            date = information[i][3]
##            time = information[i][4]
##            cost = information[i][5]
##            background.create_text(60,y_value,text = idpos, fill='black', font=('Ariel',10))
##            background.create_text(600,y_value,text=date, fill='black', font=('Ariel',10))
##            background.create_text(720,y_value,text=time, fill='black', font=('Ariel',10))
##            background.create_text(850,y_value,text='£'+cost, fill='black', font=('Ariel',10))
##            idpos += 1
##            helpers = information[i][1]
##            helperlist = helpers.split(', ')
##            for name in helperlist:
##                background.create_text(250,y_value,text = name, fill='black', font=('Ariel',10))
##                y_value += 20
##
##        y_value = 160
##        for i in range(0,maxid):
##            y_value += 30
##            susers = information[i][2]
##            suserslist = susers.split(', ')
##            for name in suserslist:
##                background.create_text(440,y_value,text = name, fill='black', font=('Ariel',10))
##                y_value += 20

    def DisplayLunchClubByDate(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Lunch Clubs')

        self.LunchClubsByDateFrame = Frame(self.master)
        self.LunchClubsByDateFrame.pack()
        self.LunchClubsByDateFrame.grid_rowconfigure(0, weight=1)
        self.LunchClubsByDateFrame.grid_columnconfigure(0, weight=1)

        xscrollbar = Scrollbar(self.LunchClubsByDateFrame, orient=HORIZONTAL)
        xscrollbar.grid(row=1, column=0, sticky=E+W)
        yscrollbar = Scrollbar(self.LunchClubsByDateFrame)
        yscrollbar.grid(row=0, column=1, sticky=N+S)

        background = Canvas(self.LunchClubsByDateFrame, width=1700, height=1000, scrollregion=(0, 0, 1700, 1000),
                xscrollcommand=xscrollbar.set,
                yscrollcommand=yscrollbar.set)

        xscrollbar.config(command=background.xview)
        yscrollbar.config(command=background.yview)

        background.create_rectangle(0, 0, 1700, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1700, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1700, 1000, fill="white", outline='white')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Displaying Lunch Clubs', font=('comic sans ms',50), fill='violetred4')

        background.grid(row=0, column=0, sticky=N+S+E+W)

        background.create_window(100,130,window = Button(self.LunchClubsByDateFrame, text='Select Different Date', font=('Ariel',11), fg='black',bg='darkseagreen3',relief=FLAT, command=self.AllLunchClubs))
    

        background.create_text(60,165, text='Lunch Club ID', fill='violetred4', font=('ariel',11,'underline'))
        background.create_text(250,165, text='Helpers', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(440,165, text='Service Users', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(600,165, text='Date of Club', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(720,165, text='Time of Club', fill='violetred4', font=('Ariel',11,'underline'))
        background.create_text(850,165, text='Cost of Club', fill='violetred4', font=('Ariel',11,'underline'))
        
        

        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()

        #LUNCH_CLUBS:  VOLUNTEERID, SERVICE_USERID, DATE_OF_CLUB, TIME_OF_CLUB, COST
        
        selectdate = self.Day.get() + '/' + self.Month.get() + '/' + self.Year.get()
        print(selectdate)
        cursor.execute('SELECT * FROM LUNCH_CLUBS WHERE DATE_OF_CLUB = ?', (selectdate, ));
        information=cursor.fetchall()

        y_value = 160
        idpos = 1
        for i in range(0,len(information)):
            y_value += 30
            date = information[i][3]
            time = information[i][4]
            cost = information[i][5]
            background.create_text(60,y_value,text = idpos, fill='black', font=('Ariel',10))
            background.create_text(600,y_value,text=date, fill='black', font=('Ariel',10))
            background.create_text(720,y_value,text=time, fill='black', font=('Ariel',10))
            background.create_text(850,y_value,text='£'+cost, fill='black', font=('Ariel',10))
            idpos += 1
            y_value2 = y_value
            helpers = information[i][1]
            helperlist = helpers.split(', ')
            for name in helperlist:
                background.create_text(250,y_value2,text = name, fill='black', font=('Ariel',10))
                y_value2 += 20
            y_value3 = y_value
            susers = information[i][2]
            suserslist = susers.split(', ')
            for name in suserslist:
                background.create_text(440,y_value3,text = name, fill='black', font=('Ariel',10))
                y_value3 += 20
            if y_value2 > y_value3:
                y_value = y_value2
            elif y_value3 > y_value2:
                y_value = y_value3
            else:
                y_value = y_value2
            

##        y_value = 160
##        for i in range(0,len(information)):
##            y_value += 30
##            susers = information[i][2]
##            suserslist = susers.split(', ')
##            for name in suserslist:
##                background.create_text(440,y_value,text = name, fill='black', font=('Ariel',10))
##                y_value += 20


        

##        self.LunchClubID = StringVar()
##        
##        background.create_text(700,165, text='Select the Lunch Club ID you would like to view:', fill='violetred4', font=('ariel',11,'underline'))
##        background.create_window(500,185,window = Spinbox(self.LunchClubsFrame, width = 4, from_=0, to=maxid, relief=FLAT, bg='grey88', textvariable = self.LunchClubID, command=self.DisplayLunchClub))
##    

        
    def DisplayLunchClub(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Display Lunch Club')

        self.SearchLunchClubFrame = Frame(self.master)
        self.SearchLunchClubFrame.pack()

        self.background = Canvas(self.SearchLunchClubFrame, width=1000, height=600)
        self.background.pack()

        self.background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        self.background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        self.background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        self.background.create_line(0,250,1000,250, fill='black')
        photo = PhotoImage(file="Logo_GIF.gif")
        self.background.create_image(80,50, image=photo)

        self.background.create_text(500, 50, text='Search Lunch Clubs', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(self.background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)

        MaxID = self.LunchClubTotalID()

        self.LunchClubID = StringVar()
        self.LunchClubIDText = Label(self.SearchLunchClubFrame, text='Lunch Club ID:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=200)
        self.LunchClubIDEntry = Spinbox(self.SearchLunchClubFrame, width = 4, from_=0, to=MaxID, relief=FLAT, bg='grey88', textvariable = self.LunchClubID, command=self.DisplayLunchClub2).place(x=110, y=200)


    def DisplayLunchClub2(self):
        try:
            self.volunteers.set('')
        except:
            pass
        try:
            self.serviceusers.set('')
        except:
            pass
        try:
            self.date_of_club.set('')
        except:
            pass
        try:
            self.time_of_club.set('')
        except:
            pass
        try:
            self.cost_of_club.set('')
        except:
            pass
        
        ID = self.LunchClubID.get()
        self.volunteers = StringVar()
        self.serviceusers = StringVar()
        self.date_of_club = StringVar()
        self.time_of_club = StringVar()
        self.cost_of_club = StringVar()
        
        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT * FROM LUNCH_CLUBS WHERE LUNCH_CLUBID = %s' % (ID));
        information = cursor.fetchall()[0]
        self.volunteers.set(information[1])
        self.serviceusers.set(information[2])     
        self.date_of_club.set(information[3])
        self.time_of_club.set(information[4])
        self.cost_of_club.set(information[5])

                    
        self.VnameText = Label(self.SearchLunchClubFrame, text='Volunteer Helpers:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=280)
        self.VnameEntry = Label(self.SearchLunchClubFrame, font=('ariel',10), bg='white', textvariable=self.volunteers).place(x=20,y=310)
        self.SUnameText = Label(self.SearchLunchClubFrame, text='Service Users / Atendees:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=340)
        self.VnameEntry = Label(self.SearchLunchClubFrame, font=('ariel',10), bg='white', textvariable=self.serviceusers).place(x=20,y=370)
        self.DateofClubText = Label(self.SearchLunchClubFrame, text='Date of Club:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20,y=400)
        self.DateofClubEntry = Label(self.SearchLunchClubFrame, font=('ariel',10), bg='white', textvariable=self.date_of_club).place(x=150,y=400)
        self.TimeofClubText = Label(self.SearchLunchClubFrame, text='Time of Club:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20,y=430)
        self.TimeofClubEntry = Label(self.SearchLunchClubFrame, font=('ariel',10), bg='white', textvariable=self.time_of_club).place(x=150,y=430)
        self.CostofClubText = Label(self.SearchLunchClubFrame, text='Cost of Club:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20,y=460)
        self.PoundText = Label(self.SearchLunchClubFrame, text='£', fg='black', bg='white', font=('ariel',10)).place(x=150,y=460)
        self.CostofClubEntry = Label(self.SearchLunchClubFrame, font=('ariel',10), bg='white', textvariable=self.cost_of_club).place(x=160,y=460)

        #LUNCH_CLUBS:  VOLUNTEERID, SERVICE_USERID, DATE_OF_CLUB, TIME_OF_CLUB, COST

##        service_users = information[2].split(', ')
##        requiretransport = []
##        for i in range(0,len(service_users)-1):
##            name = service_users[i].split(' ')
##            cursor.execute('SELECT TRANSPORT_REQUIRED FROM SERVICE_USERS WHERE FIRST_NAME = ? AND LAST_NAME = ?', (str(name[0]), str(name[1])));
##            requiretransport.append(cursor.fetchall()[0][0])
##
##        print(requiretransport)
##            
##        
##        yvalue2 = yvalue + 50
##        self.LastnameText = Label(self.SearchLunchClubFrame, textvariable=self.sunames, fg='black', bg='white', font=('ariel',10,'underline')).place(x=20,y=yvalue+30)
##        self.RequireTransportText = Label(self.SearchLunchClubFrame, textvariable=self.require_transport, fg='black', bg='white', font=('ariel',10,'underline')).place(x=280,y=yvalue+30)
##        self.AmountText = Label(self.SearchLunchClubFrame, textvariable=self.cost, fg='black', bg='white', font=('ariel',10,'underline')).place(x=480,y=yvalue+30)
##        for i in range(0,len(service_users)-1):
##            service_username = service_users[i]
##            self.SUFirstname = Label(self.SearchLunchClubFrame, font=('ariel',10), bg='white', text=service_username).place(x=20,y=yvalue2)
##            self.RequireTransport = Label(self.SearchLunchClubFrame, font=('ariel',10), bg='white', text=requiretransport[i]).place(x=280,y=yvalue2)
##            if requiretransport[i] == 'Yes':
##                amount = '10'
##            else:
##                amount = '6'
##            self.amount = Label(self.SearchLunchClubFrame, font=('ariel',10), bg='white', text=amount).place(x=480,y=yvalue2)
##            yvalue += 20
##            i += 1

        





    def AddLunchClub(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Add Lunch Club')

        self.AddLunchClubFrame = Frame(self.master)
        self.AddLunchClubFrame.pack()

        background = Canvas(self.AddLunchClubFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Add Lunch Club', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)


        maxid = self.TotalID()
        maxid2 = self.SUTotalID()
        #LUNCH_CLUBS:  VOLUNTEERID, SERVICE_USERID, DATE_OF_CLUB, TIME_OF_CLUB, COST
                               
        database = sqlite3.connect('Appointments.db');
        cursor = database.cursor()
        cursor.execute('SELECT FIRST_NAME,LAST_NAME FROM VOLUNTEERS');
        names = cursor.fetchall()
        cursor.execute('SELECT FIRST_NAME,LAST_NAME FROM SERVICE_USERS');
        names2 = cursor.fetchall()
        
        self.namelist = []
        self.namelistV = []
        for i in range(0,maxid):
            name = names[i]
            fullname = name[0] + ' ' + name[1]
            self.namelist.append(fullname)
            i += 1

        self.namelist2 = []
        self.namelistSU = []
        for i in range(0,maxid2):
            name = names2[i]
            fullname = name[0] + ' ' + name[1]
            self.namelist2.append(fullname)
            i += 1

        
        self.Helper = StringVar()
        self.ServiceUser = StringVar()
        self.helperpos = 220
        self.supos = 220

        self.HelperText = Label(self.AddLunchClubFrame, text='Add Helper:', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=185)
        self.Helper.set('Select...')
        self.HelperEntry = OptionMenu(self.AddLunchClubFrame, self.Helper,*self.namelist).place(x=110,y=180)
        self.Add = Button(self.AddLunchClubFrame, text='Add', font=('comic sans ms',11), bg='darkseagreen3', fg='white', command=self.AddV).place(x=280, y=180)

        self.ServiceUserText = Label(self.AddLunchClubFrame, text='Add Service User:', fg='black', bg='white', font=('Ariel',10)).place(x=500, y=185)
        self.ServiceUser.set('Select...')
        self.ServiceUserEntry = OptionMenu(self.AddLunchClubFrame, self.ServiceUser,*self.namelist2).place(x=620,y=180)
        self.Add = Button(self.AddLunchClubFrame, text='Add', font=('comic sans ms',11), bg='darkseagreen3', fg='white', command=self.AddSU).place(x=790, y=180)

        Button(self.AddLunchClubFrame, text='Done', font=('comic sans ms',11), bg='darkseagreen3', fg='white', command=self.AddLunchClub2).place(x=900, y=180)
        
    def AddV(self):
        helper = self.Helper.get()
        self.namelistV.append(helper)
        self.namelist.remove(helper)

        if len(self.namelist) == 0:
            Label(self.AddLunchClubFrame, text=helper, fg='black', bg='white', font=('Ariel',10)).place(x=20, y=self.helperpos)
            self.helperpos += 20
            self.namelist.append('')
            self.HelperText = Label(self.AddLunchClubFrame, text='Add Helper:', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=185)
            self.Helper.set(' ')
            self.HelperEntry = OptionMenu(self.AddLunchClubFrame, self.Helper,*self.namelist).place(x=110,y=180)
        else:
            self.HelperText = Label(self.AddLunchClubFrame, text='Add Helper:', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=185)
            self.Helper.set('Select...')
            self.HelperEntry = OptionMenu(self.AddLunchClubFrame, self.Helper,*self.namelist).place(x=110,y=180)
            Label(self.AddLunchClubFrame, text=helper, fg='black', bg='white', font=('Ariel',10)).place(x=20, y=self.helperpos)
            self.helperpos += 20

    def AddSU(self):
        su = self.ServiceUser.get()
        self.namelistSU.append(su)
        self.namelist2.remove(su)

        if len(self.namelist2) == 0:
            Label(self.AddLunchClubFrame, text=su, fg='black', bg='white', font=('Ariel',10)).place(x=500, y=self.supos)
            self.supos += 20
            self.namelist2.append('')
            self.ServiceUserText = Label(self.AddLunchClubFrame, text='Add Service User:', fg='black', bg='white', font=('Ariel',10)).place(x=500, y=185)
            self.ServiceUser.set(' ')
            self.ServiceUserEntry = OptionMenu(self.AddLunchClubFrame, self.ServiceUser,*self.namelist2).place(x=620,y=180)
        else:
            self.ServiceUserText = Label(self.AddLunchClubFrame, text='Add Service User:', fg='black', bg='white', font=('Ariel',10)).place(x=500, y=185)
            self.ServiceUser.set('Select...')
            self.ServiceUserEntry = OptionMenu(self.AddLunchClubFrame, self.ServiceUser,*self.namelist2).place(x=620,y=180)
            Label(self.AddLunchClubFrame, text=su, fg='black', bg='white', font=('Ariel',10)).place(x=500, y=self.supos)
            self.supos += 20

    def AddLunchClub2(self):
        self.y_coord = 0

        if self.helperpos > self.supos:
            self.y_coord = self.helperpos
        elif self.supos > self.helperpos:
            self.y_coord = self.supos
        else:
            self.y_coord = self.supos

        self.Day = StringVar()
        self.Month = StringVar()
        self.Year = StringVar()
        self.Hour = StringVar()
        self.Minute = StringVar()

        self.DateOfClubText = Label(self.AddLunchClubFrame, text='Date of Club:', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=self.y_coord+30)
        self.DateofClubDay =  Entry(self.AddLunchClubFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Day).place(x=120,y=self.y_coord+30)
        self.Divide = Label(self.AddLunchClubFrame, text='/', fg='black', bg='white', font=('ariel',12)).place(x=140, y=self.y_coord+30)
        self.DateofClubMonth =  Entry(self.AddLunchClubFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Month).place(x=155,y=self.y_coord+30)
        self.Divide = Label(self.AddLunchClubFrame, text='/', fg='black', bg='white', font=('ariel',12)).place(x=175, y=self.y_coord+30)
        self.DateofClubYear =  Entry(self.AddLunchClubFrame, width=4, font=('ariel',10), bg='grey88', textvariable=self.Year).place(x=190,y=self.y_coord+30)
        self.TimeofClubText = Label(self.AddLunchClubFrame, text='Time of Club:', fg='black', bg='white', font=('Ariel',10)).place(x=20, y=self.y_coord+60)
        self.TimeofClubHour =  Entry(self.AddLunchClubFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Hour).place(x=120,y=self.y_coord+60)
        self.Divide = Label(self.AddLunchClubFrame, text=':', fg='black', bg='white', font=('ariel',12)).place(x=140, y=self.y_coord+60)
        self.TimeofClubMinuite =  Entry(self.AddLunchClubFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Minute).place(x=155,y=self.y_coord+60)

        Button(self.AddLunchClubFrame, text='Add', font=('comic sans ms',11), bg='darkseagreen3', fg='white', command=self.AddLunchClub3).place(x=50, y=self.y_coord+100)

    def AddLunchClub3(self):
        ID = self.LunchClubTotalID()
        ID += 1
        volunteers = ', '.join(self.namelistV)
        service_users = ', '.join(self.namelistSU)
        dateofclub = self.Day.get() + '/' + self.Month.get() + '/' + self.Year.get()
        timeofclub = self.Hour.get() + ':' + self.Minute.get()


        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()

        costlist = []
        for i in range(0,len(self.namelistSU)-1):
            fullname = self.namelistSU[i]
            name = fullname.split(' ')
            cursor.execute("SELECT TRANSPORT_REQUIRED FROM SERVICE_USERS WHERE FIRST_NAME = ? AND LAST_NAME = ?", (name[0],name[1]));
            costlist.append(cursor.fetchall()[0][0])

        totalcost = 0
        for cost in costlist:
            if cost == 'Yes':
                totalcost += 10
            else:
                totalcost += 6
                       
        
        database.execute('INSERT INTO LUNCH_CLUBS (LUNCH_CLUBID, VOLUNTEERID, SERVICE_USERID, DATE_OF_CLUB, TIME_OF_CLUB, COST) \
                VALUES (?, ?, ?, ?, ?, ?)', (ID,volunteers,service_users,dateofclub,timeofclub,totalcost));
        database.commit()

        self.AddLunchClub()
        

    def UpdateLunchClub(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Update Volunteer')

        self.UpdateLunchClubFrame = Frame(self.master)
        self.UpdateLunchClubFrame.pack()

        background = Canvas(self.UpdateLunchClubFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,50, image=photo)

        background.create_text(500, 50, text='Update Lunch Club', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)

        MaxID = self.LunchClubTotalID()

        self.LunchClubID = StringVar()
        self.LunchClubData = StringVar()
        
        self.LunchClubIDText = Label(self.UpdateLunchClubFrame, text='Lunch Club ID:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=200)
        self.LunchClubIDEntry = Spinbox(self.UpdateLunchClubFrame, width = 4, from_=0, to=MaxID, relief=FLAT, bg='grey88', textvariable = self.LunchClubID).place(x=120, y=200)

        self.LunchClubDataText = Label(self.UpdateLunchClubFrame, text='What would you like to update:', fg='black', bg='white', font=('Ariel',10,'underline')).place(x=20, y=240)
        self.LunchClubData.set('Select...')
        self.LunchClubDataEntry = OptionMenu(self.UpdateLunchClubFrame, self.LunchClubData,'Volunteer Helpers', 'Service Users', 'Date of Club', 'Time of Club').place(x=210,y=240)

        self.selectbutton123 = Button(self.UpdateLunchClubFrame, text='Select', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.UpdateLunchClub2).place(x=380, y=240)

    def UpdateLunchClub2(self):
        self.selectbutton123 = Button(self.UpdateLunchClubFrame, text='Select', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, state = DISABLED).place(x=380, y=240)
        Data = self.LunchClubData.get()

        maxid = self.TotalID()
        maxid2 = self.SUTotalID()
        #LUNCH_CLUBS:  VOLUNTEERID, SERVICE_USERID, DATE_OF_CLUB, TIME_OF_CLUB, COST
                               
        database = sqlite3.connect('Appointments.db');
        cursor = database.cursor()
        cursor.execute('SELECT FIRST_NAME,LAST_NAME FROM VOLUNTEERS');
        names = cursor.fetchall()
        cursor.execute('SELECT FIRST_NAME,LAST_NAME FROM SERVICE_USERS');
        names2 = cursor.fetchall()
        
        self.namelist = []
        self.namelistV = []
        for i in range(0,maxid):
            name = names[i]
            fullname = name[0] + ' ' + name[1]
            self.namelist.append(fullname)
            i += 1

        self.namelist2 = []
        self.namelistSU = []
        for i in range(0,maxid2):
            name = names2[i]
            fullname = name[0] + ' ' + name[1]
            self.namelist2.append(fullname)
            i += 1


        self.Var = StringVar()
        self.Var2 = StringVar()
        self.Var3 = StringVar()
        self.Helper = StringVar()
        self.ServiceUser = StringVar()
        self.helperpos = 350
        self.supos = 350

        self.DataLabel = Label(self.UpdateLunchClubFrame, text='What would you like to change it to?', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=280)

        if Data == 'Volunteer Helpers':
            self.HelperText = Label(self.UpdateLunchClubFrame, text='Add Helper:', fg='black', bg='white', font=('Ariel',10,'bold')).place(x=20, y=320)
            self.Helper.set('Select...')
            self.HelperEntry = OptionMenu(self.UpdateLunchClubFrame, self.Helper,*self.namelist).place(x=150,y=320)
            self.Add = Button(self.UpdateLunchClubFrame, text='Add', font=('comic sans ms',11), bg='darkseagreen3', fg='white', command=self.AddV2).place(x=400, y=320)
        elif Data == 'Service Users':
            self.ServiceUserText = Label(self.UpdateLunchClubFrame, text='Add Service User:', fg='black', bg='white', font=('Ariel',10,'bold')).place(x=20, y=320)
            self.ServiceUser.set('Select...')
            self.ServiceUserEntry = OptionMenu(self.UpdateLunchClubFrame, self.ServiceUser,*self.namelist2).place(x=150,y=320)
            self.Add = Button(self.UpdateLunchClubFrame, text='Add', font=('comic sans ms',11), bg='darkseagreen3', fg='white', command=self.AddSU2).place(x=400, y=320)
        elif Data == 'Date of Club':
            self.Label = Label(self.UpdateLunchClubFrame, text='Date of Club:', fg='black', bg='white', font=('ariel',10)).place(x=20,y=320)
            self.Entry =  Entry(self.UpdateLunchClubFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=120,y=320)
            self.Divide = Label(self.UpdateLunchClubFrame, text='/', fg='black', bg='white', font=('ariel',12)).place(x=140, y=320)
            self.Entry2 =  Entry(self.UpdateLunchClubFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Var2).place(x=155,y=320)
            self.Divide = Label(self.UpdateLunchClubFrame, text='/', fg='black', bg='white', font=('ariel',12)).place(x=175, y=320)
            self.Entry3 =  Entry(self.UpdateLunchClubFrame, width=4, font=('ariel',10), bg='grey88', textvariable=self.Var3).place(x=190,y=320)
        elif Data == 'Time of Club':
            self.Label = Label(self.UpdateLunchClubFrame, text='Time of Club:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=320)
            self.Entry =  Entry(self.UpdateLunchClubFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Var).place(x=120,y=320)
            self.Divide = Label(self.UpdateLunchClubFrame, text=':', fg='black', bg='white', font=('ariel',12)).place(x=140, y=320)
            self.Entry2 =  Entry(self.UpdateLunchClubFrame, width=2, font=('ariel',10), bg='grey88', textvariable=self.Var2).place(x=155,y=320)

        updatebutton = Button(self.UpdateLunchClubFrame, text='Update', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.UpdateLunchClub3).place(x=380, y=500)

    def AddV2(self):
        helper = self.Helper.get()
        self.namelistV.append(helper)
        self.namelist.remove(helper)

        if len(self.namelist) == 0:
            Label(self.UpdateLunchClubFrame, text=helper, fg='black', bg='white', font=('Ariel',10)).place(x=20, y=self.helperpos)
            self.helperpos += 20
            self.namelist.append('')
            self.HelperText = Label(self.UpdateLunchClubFrame, text='Add Helper:', fg='black', bg='white', font=('Ariel',10,'bold')).place(x=20, y=320)
            self.Helper.set(' ')
            self.HelperEntry = OptionMenu(self.UpdateLunchClubFrame, self.Helper,*self.namelist).place(x=150,y=320)
        else:
            self.HelperText = Label(self.UpdateLunchClubFrame, text='Add Helper:', fg='black', bg='white', font=('Ariel',10,'bold')).place(x=20, y=320)
            self.Helper.set('Select...')
            self.HelperEntry = OptionMenu(self.UpdateLunchClubFrame, self.Helper,*self.namelist).place(x=150,y=320)
            Label(self.UpdateLunchClubFrame, text=helper, fg='black', bg='white', font=('Ariel',10)).place(x=20, y=self.helperpos)
            self.helperpos += 20

    def AddSU2(self):
        su = self.ServiceUser.get()
        self.namelistSU.append(su)
        self.namelist2.remove(su)

        if len(self.namelist2) == 0:
            Label(self.UpdateLunchClubFrame, text=su, fg='black', bg='white', font=('Ariel',10)).place(x=20, y=self.supos)
            self.supos += 20
            self.namelist2.append('')
            self.ServiceUserText = Label(self.UpdateLunchClubFrame, text='Add Service User:', fg='black', bg='white', font=('Ariel',10,'bold')).place(x=20, y=320)
            self.ServiceUser.set(' ')
            self.ServiceUserEntry = OptionMenu(self.UpdateLunchClubFrame, self.ServiceUser,*self.namelist2).place(x=150,y=320)
        else:
            self.ServiceUserText = Label(self.UpdateLunchClubFrame, text='Add Service User:', fg='black', bg='white', font=('Ariel',10,'bold')).place(x=20, y=320)
            self.ServiceUser.set('Select...')
            self.ServiceUserEntry = OptionMenu(self.UpdateLunchClubFrame, self.ServiceUser,*self.namelist2).place(x=150,y=320)
            Label(self.UpdateLunchClubFrame, text=su, fg='black', bg='white', font=('Ariel',10)).place(x=20, y=self.supos)
            self.supos += 20

    def UpdateLunchClub3(self):
        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        self.IDupdate2 = self.LunchClubID.get()
        Data = self.LunchClubData.get()
        Var = self.Var.get()
        Var2 = self.Var2.get()
        Var3 = self.Var3.get()
        volunteers = ', '.join(self.namelistV)
        service_users = ', '.join(self.namelistSU)
        
        if Data == 'Volunteer Helpers':
            database.execute("UPDATE LUNCH_CLUBS SET VOLUNTEERID = ? WHERE LUNCH_CLUBID = ?", (volunteers,self.IDupdate2));
            database.commit()
        elif Data == 'Service Users':
            database.execute('UPDATE LUNCH_CLUBS SET SERVICE_USERID = ? WHERE LUNCH_CLUBID = ?', (service_users,self.IDupdate2));
            database.commit()

            costlist = []
            for i in range(0,len(self.namelistSU)):
                fullname = self.namelistSU[i]
                print(fullname)
                name = fullname.split(' ')
                cursor.execute("SELECT TRANSPORT_REQUIRED FROM SERVICE_USERS WHERE FIRST_NAME = ? AND LAST_NAME = ?", (name[0],name[1]));
                costlist.append(cursor.fetchall()[0][0])

            totalcost = 0
            for cost in costlist:
                if cost == 'Yes':
                    totalcost += 10
                else:
                    totalcost += 6
            
            database.execute('UPDATE LUNCH_CLUBS SET COST = ? WHERE LUNCH_CLUBID = ?', (totalcost,self.IDupdate2));
            database.commit()        
            
        elif Data == 'Date of Club':
            dateofclub = Var + '/' + Var2 + '/' + Var3
            database.execute('UPDATE LUNCH_CLUBS SET DATE_OF_CLUB = ? WHERE LUNCH_CLUBID = ?', (dateofclub,self.IDupdate2));
            database.commit()
        elif Data == 'Time of Club':
            timeofclub = Var + ':' + Var2
            database.execute('UPDATE LUNCH_CLUBS SET TIME_OF_CLUB = ? WHERE LUNCH_CLUBID = ?', (timeofclub,self.IDupdate2));
            database.commit()

        self.AllLunchClubs()

    def DeleteLunchClub(self):
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title('Display Lunch Club')

        self.SearchLunchClubFrame = Frame(self.master)
        self.SearchLunchClubFrame.pack()

        self.background = Canvas(self.SearchLunchClubFrame, width=1000, height=600)
        self.background.pack()

        self.background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        self.background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        self.background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        self.background.create_line(0,250,1000,250, fill='black')
        photo = PhotoImage(file="Logo_GIF.gif")
        self.background.create_image(80,50, image=photo)

        self.background.create_text(500, 50, text='Delete Lunch Club', font=('comic sans ms',50), fill='violetred4')

        homebutton = Button(self.background, text='Home', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.MainMenu)
        homebutton.place(x=40,y=110)

        MaxID = self.LunchClubTotalID()

        self.LunchClubID = StringVar()
        self.LunchClubIDText = Label(self.SearchLunchClubFrame, text='Lunch Club ID:', fg='black', bg='white', font=('ariel',10)).place(x=20, y=200)
        self.LunchClubIDEntry = Spinbox(self.SearchLunchClubFrame, width = 4, from_=0, to=MaxID, relief=FLAT, bg='grey88', textvariable = self.LunchClubID, command=self.DisplayLunchClub2).place(x=110, y=200)

        self.delete = Button(self.SearchLunchClubFrame, text='Delete', font=('comic sans ms',12), fg='white',bg='darkseagreen3',relief=FLAT, command=self.DeleteLunchClub3).place(x=700, y=190)

    def DeleteLunchClub2(self):
        try:
            self.volunteers.set('')
        except:
            pass
        try:
            self.serviceusers.set('')
        except:
            pass
        try:
            self.date_of_club.set('')
        except:
            pass
        try:
            self.time_of_club.set('')
        except:
            pass
        
        ID = self.LunchClubID.get()
        self.volunteers = StringVar()
        self.serviceusers = StringVar()
        self.date_of_club = StringVar()
        self.time_of_club = StringVar()

        
        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT * FROM LUNCH_CLUBS WHERE LUNCH_CLUBID = %s' % (ID));
        information = cursor.fetchall()[0]
        self.volunteers.set(information[1])
        self.serviceusers.set(information[2])     
        self.date_of_club.set(information[3])
        self.time_of_club.set(information[4])

        self.VnameText = Label(self.SearchLunchClubFrame, text='Volunteer Helpers:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=280)
        self.VnameEntry = Label(self.SearchLunchClubFrame, font=('ariel',10), bg='white', textvariable=self.volunteers).place(x=20,y=310)
        self.SUnameText = Label(self.SearchLunchClubFrame, text='Service Users / Atendees:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20, y=340)
        self.VnameEntry = Label(self.SearchLunchClubFrame, font=('ariel',10), bg='white', textvariable=self.serviceusers).place(x=20,y=370)
        self.DateofClubText = Label(self.SearchLunchClubFrame, text='Date of Club:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20,y=400)
        self.DateofClubEntry = Label(self.SearchLunchClubFrame, font=('ariel',10), bg='white', textvariable=self.date_of_club).place(x=150,y=400)
        self.TimeofClubText = Label(self.SearchLunchClubFrame, text='Time of Club:', fg='black', bg='white', font=('ariel',10,'underline')).place(x=20,y=430)
        self.TimeofClubEntry = Label(self.SearchLunchClubFrame, font=('ariel',10), bg='white', textvariable=self.time_of_club).place(x=150,y=430)

    def DeleteLunchClub3(self):
        ID = self.LunchClubID.get()

        database = sqlite3.connect('Appointments.db');
        database.execute("DELETE FROM LUNCH_CLUBS WHERE LUNCH_CLUBID = ?", (ID));
        database.commit()

        database.execute("UPDATE LUNCH_CLUBS SET LUNCH_CLUBID = LUNCH_CLUBID-1 WHERE LUNCH_CLUBID > ?", (ID, ));
        database.commit() 

        self.AllLunchClubs()
        

    def TotalID(self):
        database = sqlite3.connect('Appointments.db');
        cursor = database.cursor()
        cursor.execute("SELECT MAX(VOLUNTEERID) FROM VOLUNTEERS");
        result = cursor.fetchall()[0][0]
        result = int(result)
        return result

    def SUTotalID(self):
        database = sqlite3.connect('Appointments.db');
        cursor = database.cursor()
        cursor.execute("SELECT MAX(SERVICE_USERID) FROM SERVICE_USERS");
        result = cursor.fetchall()[0][0]
        result = int(result)
        return result

    def ATotalID(self):
        database = sqlite3.connect('Appointments.db');
        cursor = database.cursor()
        cursor.execute("SELECT MAX(APPOINTMENTID) FROM APPOINTMENTS");
        result = cursor.fetchall()[0][0]
        print(result)
        result = int(result)
        return result

    def LunchClubTotalID(self):
        database = sqlite3.connect('Appointments.db');
        cursor = database.cursor()
        cursor.execute("SELECT MAX(LUNCH_CLUBID) FROM LUNCH_CLUBS");
        result = cursor.fetchall()[0][0]
        print(result)
        result = int(result)
        return result


    def ChangePassword(self):
        self.ATotalID()
        self.ClearWindow()
        self.master.geometry('1000x600')
        self.master.title ("Appointment System")
        self.ChangePasswordFrame = Frame(self.master)
        self.ChangePasswordFrame.pack()

        background = Canvas(self.ChangePasswordFrame, width=1000, height=600)
        background.pack()

        background.create_rectangle(0, 0, 1000, 200, fill="white", outline='white')
        background.create_rectangle(0,110, 1000, 300, fill='darkseagreen3', outline='darkseagreen3')
        background.create_rectangle(0,150, 1000, 600, fill="white", outline='white')
        photo = PhotoImage(file="Logo_GIF.gif")
        background.create_image(80,55, image=photo)
        background.create_text(500, 50, text='Change Password', font=('comic sans ms',50), fill='violetred4')
      
        self.Username = StringVar()
        self.Password = StringVar()
        self.NewPassword = StringVar()
        self.ReEnterPassword = StringVar()

        self.Username_Text= Label(self.ChangePasswordFrame, text= "Username: ", fg='black', bg='white', font=('ariel',12)).place(x=285, y=200)
        self.Username_Data= Entry(self.ChangePasswordFrame, width = 20, font=('ariel',12), bg='grey88', textvariable = self.Username).place(x=450,y=200)
        self.Password_Text= Label(self.ChangePasswordFrame, text= " Current Password: ", fg='black', bg='White', font=('ariel',12)).place(x=280, y=240)
        self.Password_Data= Entry(self.ChangePasswordFrame, width = 20, font=('ariel',12), bg='grey88', show="*", textvariable = self.Password).place(x=450,y=240)
        self.NewPassword_Text= Label(self.ChangePasswordFrame, text= "New Password: ", fg='black', bg='White', font=('ariel',12)).place(x=285, y=280)
        self.NewPassword_Data= Entry(self.ChangePasswordFrame, width = 20, font=('ariel',12), bg='grey88', show="*", textvariable = self.NewPassword).place(x=450,y=280)
        self.ReEnterPassword_Text= Label(self.ChangePasswordFrame, text= "Re-Enter Password: ", fg='black', bg='White', font=('ariel',12)).place(x=285, y=320)
        self.ReEnterPassword_Data= Entry(self.ChangePasswordFrame, width = 20, font=('ariel',12), bg='grey88', show="*", textvariable = self.ReEnterPassword).place(x=450,y=320)

        self.Login = Button(self.ChangePasswordFrame, text='Change', font=('Comic Sans MS', 12,'underline'), fg='black', bg='white', relief=FLAT, command=self.ChangePassword2).place(x=500,y=350)

    def ChangePassword2(self):
        username = self.Username.get()
        password = self.Password.get()
        newpassword = self.NewPassword.get()
        reenterpassword = self.ReEnterPassword.get()

        ID = username[9:]

        database = sqlite3.connect('Appointments.db')
        cursor = database.cursor()
        cursor.execute('SELECT USERNAME, PASSWORD FROM VOLUNTEERS WHERE VOLUNTEERID = %s' % (ID));
        login = cursor.fetchall()[0]

        if username == login[0] and password == login[1]:
            if newpassword == reenterpassword:
                database.execute("UPDATE VOLUNTEERS set PASSWORD = ? where VOLUNTEERID = ?", (newpassword,username[9:]));
                database.commit()
            else:
                Label(self.ChangePasswordFrame, text='Error!', fg='red', bg='white', font=('ariel',12)).place(x=500, y=400)
        else:
            Label(self.ChangePasswordFrame, text='Error!', fg='red', bg='white', font=('ariel',12)).place(x=450, y=400)

        self.Username.set('')
        self.Password.set('')
        self.NewPassword.set('')
        self.ReEnterPassword.set('')

        Label(self.ChangePasswordFrame, text='Password Changed', fg='violetred4', bg='white', font=('ariel',12)).place(x=500, y=400)


    def LogOut(self):
        self.PasswordMenu()
        self.menubar.delete(0,END)

    def ClearWindow(self):
        self.master.geometry('1000x600')
        try:
            self.PasswordFrame.pack_forget()
        except:
            pass
        try:
            self.CreateLoginFrame.pack_forget()
        except:
            pass
        try:
            self.DisplayAllVolunteersFrame.pack_forget()
        except:
            pass
        try:
            self.MainMenuFrame.pack_forget()
        except:
            pass
        try:
            self.AddVolunteerFrame.pack_forget()
        except:
            pass
        try:
            self.AddServiceUserFrame.pack_forget()
        except:
            pass
        try:
            self.SearchVolunteerFrame.pack_forget()
        except:
            pass
        try:
            self.SearchServiceUserFrame.pack_forget()
        except:
            pass
        try:
            self.DisplayAllServiceUsersFrame.pack_forget()
        except:
            pass
        try:
            self.UpdateVolunteerFrame.pack_forget()
        except:
            pass
        try:
            self.UpdateVolunteerFrame2.pack_forget()
        except:
            pass
        try:
            self.DeleteVolunteerFrame.pack_forget()
        except:
            pass
        try:
            self.UpdateServiceUserFrame.pack_forget()
        except:
            pass
        try:
            self.UpdateServiceUserFrame2.pack_forget()
        except:
            pass
        try:
            self.DeleteServiceUserFrame.pack_forget()
        except:
            pass
        try:
            self.AddAppointmentFrame.pack_forget()
        except:
            pass
        try:
            self.UpdateAppointmentFrame.pack_forget()
        except:
            pass
        try:
            self.SearchAppointmentFrame.pack_forget()
        except:
            pass
        try:
            self.DisplayAllAppointmentFrame.pack_forget()
        except:
            pass
        try:
            self.DisplayAllAppointment2Frame.pack_forget()
        except:
            pass
        try:
            self.DeleteAppointmentFrame.pack_forget()
        except:
            pass
        try:
            self.LunchClubsFrame.pack_forget()
        except:
            pass
        try:
            self.AddLunchClubFrame.pack_forget()
        except:
            pass
        try:
            self.LunchClubsFrame.pack_forget()
        except:
            pass
        try:
            self.LunchClubsByDateFrame.pack_forget()
        except:
            pass
        try:
            self.SearchLunchClubFrame.pack_forget()
        except:
            pass
        try:
            self.UpdateLunchClubFrame.pack_forget()
        except:
            pass
        
        

    def Exit(self):
        self.master.destroy()



def Main():
    root = Tk()
    app = MainMenu(root)
    root.mainloop()


if __name__ == "__main__":
    Main()
