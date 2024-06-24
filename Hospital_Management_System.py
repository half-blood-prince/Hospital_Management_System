from tkinter import*
from tkinter import ttk 
import random
import time 
import datetime
from tkinter import messagebox
import mysql.connector
 

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')

        self.NameTablet = StringVar()
        self.Ref = StringVar()
        self.Dose = StringVar()
        self.NoOfTablets = StringVar()
        self.Lot = StringVar()
        self.IssuedDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.PossibleSideEffects = StringVar()
        self.FurtherInformation = StringVar()
        self.BloodPressure = StringVar()
        self.StorageAdvice = StringVar()
        self.Medication = StringVar()
        self.PatientID = StringVar()
        self.NHSNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()
        self.Prescription = StringVar()



        lbltitle = Label(self.root,bd=20, relief=RIDGE, text="Hospital Management System", bg='white', fg='red', font=('times new roman', 50, 'bold'))
        lbltitle.pack(side=TOP, fill=X)

        # ==================DataFrame===================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE,)
        Dataframe.place(x=0, y=130, width=1530, height=400)
        
        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, 
                                   font=('arial', 12, 'bold'), text="Patient Information", fg='red', bg='white')
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                    font=('arial', 12, 'bold'), text="Prescription", fg='red', bg='white')
        DataframeRight.place(x=990, y=5, width=460, height=350)

        # ==================ButtonFrame==================
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # ==================Details Frame==================
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        # ==================DataFrameLeft==================

        lblNameTablet = Label(DataframeLeft, text="Name of Tablet", font=('arial', 12, 'bold'), padx=2, pady=2, bg='white') 
        lblNameTablet.grid(row=0, column=0, sticky=W)

        comNameTablet = ttk.Combobox(DataframeLeft,textvariable=self.NameTablet,state="readonly", font=('arial', 12, 'bold'),
                                      width=33)
        comNameTablet['values'] = ('', 'Ibuprofen', 'Paracetamol', 'Amoxicillin', 'Aspirin', 'Codeine')
        comNameTablet.current(0)
        comNameTablet.grid(row=0, column=1)

        lblRef = Label(DataframeLeft,text="Reference No", font=('arial', 12, 'bold'), padx=2, pady=2, bg='white')
        lblRef.grid(row=1, column=0, sticky=W)
        txtRef = Entry(DataframeLeft, font=('arial', 13, 'bold'), textvariable=self.Ref,width=35)
        txtRef.grid(row=1, column=1)

        lblDose = Label(DataframeLeft, text="Dose", font=('arial', 12, 'bold'), padx=2, pady=4, bg='white')
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, font=('arial', 13, 'bold'),textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)

        lblNoOfTablets = Label(DataframeLeft, text="No. of Tablets", font=('arial', 12, 'bold'), padx=2, pady=6, bg='white')
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        txtNoOfTablets = Entry(DataframeLeft, font=('arial', 13, 'bold'), textvariable=self.NoOfTablets,width=35)
        txtNoOfTablets.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, text="Lot", font=('arial', 12, 'bold'), padx=2, pady=6, bg='white')
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, font=('arial', 13, 'bold'), textvariable=self.Lot,width=35)
        txtLot.grid(row=4, column=1)

        lblIssuedDate = Label(DataframeLeft, text="Issued Date", font=('arial', 12, 'bold'), padx=2, pady=6, bg='white')
        lblIssuedDate.grid(row=5, column=0, sticky=W)
        txtIssuedDate = Entry(DataframeLeft, font=('arial', 13, 'bold'), textvariable=self.IssuedDate,width=35)
        txtIssuedDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft, text="Exp Date", font=('arial', 12, 'bold'), padx=2, pady=6, bg='white')
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, font=('arial', 13, 'bold'), textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataframeLeft, text="Daily Dose", font=('arial', 12, 'bold'), padx=2, pady=6, bg='white')
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataframeLeft, font=('arial', 13, 'bold'),textvariable=self.DailyDose, width=35)
        txtDailyDose.grid(row=7, column=1)

        lblPossibleSideEffects = Label(DataframeLeft, text="Possible Side Effects", font=('arial', 12, 'bold'), padx=2, pady=6, bg='white')
        lblPossibleSideEffects.grid(row=8, column=0, sticky=W)
        txtPossibleSideEffects = Entry(DataframeLeft, font=('arial', 13, 'bold'), textvariable=self.PossibleSideEffects,width=35)
        txtPossibleSideEffects.grid(row=8, column=1)

        lblFurtherInformation = Label(DataframeLeft, text="Further Information", font=('arial', 12, 'bold'), padx=2, pady=6, bg='white')
        lblFurtherInformation.grid(row=0, column=2, sticky=W)
        txtFurtherInformation = Entry(DataframeLeft, font=('arial', 13, 'bold'), textvariable=self.FurtherInformation,width=35)
        txtFurtherInformation.grid(row=0, column=3)

        lblBloodPressure = Label(DataframeLeft, text="Blood Pressure", font=('arial', 12, 'bold'), padx=2, pady=6, bg='white')
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(DataframeLeft, font=('arial', 13, 'bold'), textvariable=self.BloodPressure,width=35)
        txtBloodPressure.grid(row=1, column=3)

        lblStorageAdvice = Label(DataframeLeft, text="Storage Advice", font=('arial', 12, 'bold'), padx=2, pady=6, bg='white')
        lblStorageAdvice.grid(row=2, column=2, sticky=W)
        txtStorageAdvice = Entry(DataframeLeft, font=('arial', 13, 'bold'), textvariable=self.StorageAdvice,width=35)
        txtStorageAdvice.grid(row=2, column=3)

        lblMedication = Label(DataframeLeft,text="Medication", font=('arial', 12, 'bold'), padx=2, pady=6, bg='white')
        lblMedication.grid(row=3, column=2, sticky=W)
        txtMedication = Entry(DataframeLeft, font=('arial', 13, 'bold'),textvariable=self.Medication,  width=35)
        txtMedication.grid(row=3, column=3)

        lblPatientID = Label(DataframeLeft, text="Patient ID", font=('arial', 12, 'bold'), padx=2, pady=6, bg='white')
        lblPatientID.grid(row=4, column=2, sticky=W)
        txtPatientID = Entry(DataframeLeft, font=('arial', 13, 'bold'),textvariable=self.PatientID, width=35)
        txtPatientID.grid(row=4, column=3)

        lblNHSNumber = Label(DataframeLeft, text="NHS Number", font=('arial', 12, 'bold'), padx=2, pady=6, bg='white')
        lblNHSNumber.grid(row=5, column=2, sticky=W)
        txtNHSNumber = Entry(DataframeLeft, font=('arial', 13, 'bold'),textvariable=self.NHSNumber, width=35)
        txtNHSNumber.grid(row=5, column=3)

        lblPatientName = Label(DataframeLeft, text="Patient Name", font=('arial', 12, 'bold'), padx=2, pady=6, bg='white')
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(DataframeLeft, font=('arial', 13, 'bold'), textvariable=self.PatientName,width=35)
        txtPatientName.grid(row=6, column=3)

        lblDateOfBirth = Label(DataframeLeft, text="Date of Birth", font=('arial', 12, 'bold'), padx=2, pady=6, bg='white')
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth = Entry(DataframeLeft, font=('arial', 13, 'bold'),textvariable=self.DateOfBirth, width=35)
        txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(DataframeLeft, text="Patient Address", font=('arial', 12, 'bold'), padx=2, pady=6, bg='white')
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(DataframeLeft, font=('arial', 13, 'bold'), textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8, column=3)

        # ==================DataFrameRight==================
        self.txtPrescription = Text(DataframeRight, font=('arial', 12, 'bold'), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # ==================ButtonFrame==================
        btnPrescription = Button(Buttonframe, text='Prescription', font=('arial', 12, 'bold'),bg="green",fg="white", width=20, height=2,padx=2, pady=2)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, text='Prescription Data', font=('arial', 12, 'bold'),bg="green",fg="white", width=20, height=2,padx=2, pady=2)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text='Update', font=('arial', 12, 'bold'),bg="green",fg="white", width=20, height=2,padx=2, pady=2)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text='Delete', font=('arial', 12, 'bold'),bg="green",fg="white", width=20, height=2,padx=2, pady=2)
        btnDelete.grid(row=0, column=3)

        btnReset = Button(Buttonframe, text='Reset', font=('arial', 12, 'bold'),bg="green",fg="white", width=20, height=2,padx=2, pady=2)
        btnReset.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text='Exit', font=('arial', 12, 'bold'),bg="green",fg="white", width=20, height=2,padx=2, pady=2)
        btnExit.grid(row=0, column=5)

        # ==================Table==================
        # ==================Scroll Bar==================
        scroll_y = Scrollbar(Detailsframe, orient=VERTICAL)
        scroll_x = Scrollbar(Detailsframe, orient=HORIZONTAL)

        self.hospital_table= ttk.Treeview(Detailsframe, column=('Name of Tablet', 'Dose', 'No. of Tablets', 'Lot', 'Issued Date', 'Exp Date', 'Daily Dose', 'Possible Side Effects', 'Further Information', 'Blood Pressure', 'Storage Advice', 'Medication', 'Patient ID', 'NHS Number', 'Patient Name', 'Date of Birth', 'Patient Address', 'Prescription'),
                                              yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview, orient=VERTICAL)

        self.hospital_table.heading('Name of Tablet', text='Name of Tablet')
        self.hospital_table.heading('Dose', text='Dose')
        self.hospital_table.heading('No. of Tablets', text='No. of Tablets')
        self.hospital_table.heading('Lot', text='Lot')
        self.hospital_table.heading('Issued Date', text='Issued Date')
        self.hospital_table.heading('Exp Date', text='Exp Date')
        self.hospital_table.heading('Daily Dose', text='Daily Dose')
        self.hospital_table.heading('Possible Side Effects', text='Possible Side Effects')
        self.hospital_table.heading('Further Information', text='Further Information')
        self.hospital_table.heading('Blood Pressure', text='Blood Pressure')
        self.hospital_table.heading('Storage Advice', text='Storage Advice')
        self.hospital_table.heading('Medication', text='Medication')
        self.hospital_table.heading('Patient ID', text='Patient ID')
        self.hospital_table.heading('NHS Number', text='NHS Number')
        self.hospital_table.heading('Patient Name', text='Patient Name')
        self.hospital_table.heading('Date of Birth', text='Date of Birth')
        self.hospital_table.heading('Patient Address', text='Patient Address')
        self.hospital_table.heading('Prescription', text='Prescription')

        self.hospital_table['show'] = 'headings'

        self.hospital_table.column('Name of Tablet', width=100)
        self.hospital_table.column('Dose', width=100)
        self.hospital_table.column('No. of Tablets', width=100)
        self.hospital_table.column('Lot', width=100)
        self.hospital_table.column('Issued Date', width=100)
        self.hospital_table.column('Exp Date', width=100)
        self.hospital_table.column('Daily Dose', width=100)
        self.hospital_table.column('Possible Side Effects', width=100)
        self.hospital_table.column('Further Information', width=100)
        self.hospital_table.column('Blood Pressure', width=100)
        self.hospital_table.column('Storage Advice', width=100)
        self.hospital_table.column('Medication', width=100)
        self.hospital_table.column('Patient ID', width=100)
        self.hospital_table.column('NHS Number', width=100)
        self.hospital_table.column('Patient Name', width=100)
        self.hospital_table.column('Date of Birth', width=100)
        self.hospital_table.column('Patient Address', width=100)
        self.hospital_table.column('Prescription', width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>")

        self.fetchData()

    # ==================Function==================
    def iPrescriptionData(self):
        if self.NameTablet.get() == "" or self.Ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Cse20bce0835!", database="Mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                              (self.NameTablet.get(),
                               self.Ref.get(),
                               self.Dose.get(),
                               self.NoOfTablets.get(),
                               self.Lot.get(),
                               self.IssuedDate.get(),
                               self.ExpDate.get(),
                               self.DailyDose.get(),
                               self.PossibleSideEffects.get(),
                               self.FurtherInformation.get(),
                               self.BloodPressure.get(),
                               self.StorageAdvice.get(),
                               self.Medication.get(),
                               self.PatientID.get(),
                               self.NHSNumber.get(),
                               self.PatientName.get(),
                               self.DateOfBirth.get(),
                               self.PatientAddress.get(),
                               self.Prescription.get()
                               ))
            conn.commit()
            self.fetchData()
            conn.close()
            messagebox.showinfo("Success", "Data inserted successfully")
    def fetchData(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Cse20bce0835!", database="Mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for row in rows:
                self.hospital_table.insert('', END, values=row)
            conn.commit()
        conn.close()
    def get_cursor(self):

        
            











    







        


root = Tk()
ob = Hospital(root)
root.mainloop()


    

