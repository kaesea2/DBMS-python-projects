from tkinter import *
from tkinter import messagebox

from estate import Estate
from household import Household
from property import Property
from thoroughfare import Thoroughfare
from receipt import Receipt


class ManagerGui(Tk):
    Receipts = []
    Thoroughfares = Thoroughfare.Thoroughfares
    Properties = Property.Properties
    Households = Household.Households

    def __init__(self):
        super().__init__()
        # containers
        self.Estate = []
        # set the windows components
        self.geometry('750x430')
        self.title('MANAGER WINDOW')
        self.configure(bg='#888')

        # frames
        self.menuFrame = Frame(self, bg='#888', width=740, height=100, pady=20)
        self.showFrame = Frame(self, bg="#fff", width=740, height=300)
        self.footerFrame = Frame(self, bg='#888', width=740, height=30, pady=20)

        # place the frames in window
        self.menuFrame.grid(row=0, column=0)
        self.showFrame.grid(row=1, column=0)
        self.footerFrame.grid(row=2, column=0)

        # menu functions
        self.estateFunctions = ['CREATE ESTATE', 'DELETE ESTATE', 'VIEW ESTATE']
        self.thoroughfareFunctions = ['CREATE THOROUGHFARE', 'DELETE THOROUGHFARE', 'VIEW THOROUGHFARE',
                                      'UPDATE THOROUGHFARE']
        self.propertyFunctions = ['CREATE PROPERTY', 'DELETE PROPERTY', 'VIEW PROPERTY', 'UPDATE PROPERTY']
        self.householdFunctions = ['CREATE HOUSEHOLD', 'DELETE HOUSEHOLD', 'VIEW HOUSEHOLD', 'UPDATE HOUSEHOLD']
        self.receiptFunctions = ['CREATE RECEIPT', 'VIEW RECEIPT']

        self.estateVar = StringVar(self.menuFrame)
        self.estateVar.set(self.estateFunctions[0])
        self.thoroughfareVar = StringVar(self.menuFrame)
        self.thoroughfareVar.set(self.thoroughfareFunctions[0])
        self.propertyVar = StringVar(self.menuFrame)
        self.propertyVar.set(self.propertyFunctions[0])
        self.householdVar = StringVar(self.menuFrame)
        self.householdVar.set(self.householdFunctions[0])
        self.receiptVar = StringVar(self.menuFrame)
        self.receiptVar.set(self.receiptFunctions[0])

        self.estateOptions = OptionMenu(self.menuFrame, self.estateVar, *self.estateFunctions)
        self.thoroughfareOptions = OptionMenu(self.menuFrame, self.thoroughfareVar, *self.thoroughfareFunctions)
        self.propertyOptions = OptionMenu(self.menuFrame, self.propertyVar, *self.propertyFunctions)
        self.householdOptions = OptionMenu(self.menuFrame, self.householdVar, *self.householdFunctions)
        self.receiptOptions = OptionMenu(self.menuFrame, self.receiptVar, *self.receiptFunctions)

        self.estateOptions.grid(row=0, column=0)
        self.thoroughfareOptions.grid(row=0, column=1)
        self.propertyOptions.grid(row=0, column=2)
        self.householdOptions.grid(row=0, column=3)
        self.receiptOptions.grid(row=0, column=4)

        self.estateVar.trace('w', self.estate_traceBack)
        self.thoroughfareVar.trace('w', self.thoroughfare_traceBack)
        self.propertyVar.trace('w', self.property_traceBack)
        self.householdVar.trace('w', self.household_traceBack)
        self.receiptVar.trace('w', self.receipt_traceBack)

        self.exit_button = Button(self.footerFrame, text='BACK', padx=20)
        self.basic_user_button = Button(self.footerFrame, text='BASIC USER', padx=20)

        self.exit_button.grid(row=0, column=0, sticky=N)
        self.basic_user_button.grid(row=0, column=1, sticky=N)

        self.exit_button.configure(command=self.exit_btn)
        self.basic_user_button.configure(command=self.basic_userClicked)

    def exit_btn(self):
        from adminGui import AdminGui
        self.withdraw()
        AdminGui().mainloop()

    def basic_userClicked(self):
        self.withdraw()
        from basicGui import BasicGui
        self.bacic_user_gui = BasicGui()
        self.bacic_user_gui.mainloop()


    def clearWindow(self):
        for widget in self.showFrame.winfo_children():
            widget.destroy()

    def estate_traceBack(self, *args):
        self.clearWindow()
        self.labeltest = Label(self.showFrame, pady=10, bg='#fff', text='{}'.format(self.estateVar.get()))
        self.labeltest.grid(row=0, column=0)
        if self.estateVar.get() == 'CREATE ESTATE':
            self.createEstateClicked()
        elif self.estateVar.get() == 'DELETE ESTATE':
            self.deleteEstateClicked()
        elif self.estateVar.get() == 'VIEW ESTATE':
            self.viewEstateClicked()

    def thoroughfare_traceBack(self, *args):
        self.clearWindow()
        self.labeltest = Label(self.showFrame, pady=10, bg='#fff', text='{}'.format(self.thoroughfareVar.get()))
        self.labeltest.grid(row=0, column=0)

        if self.thoroughfareVar.get() == 'CREATE THOROUGHFARE':
            self.labeltest.grid(row=0, column=0, columnspan=2)
            self.createThoroughfareClicked()
        elif self.thoroughfareVar.get() == 'DELETE THOROUGHFARE':
            self.labeltest.grid(row=0, column=0, columnspan=2)
            self.deleteThoroughfareClicked()
        elif self.thoroughfareVar.get() == 'VIEW THOROUGHFARE':
            self.viewThoroughfareClicked()
        elif self.thoroughfareVar.get() == 'UPDATE THOROUGHFARE':
            self.labeltest.grid(row=0, column=0, columnspan=2)
            self.updateThoroughfareClicked()

    def property_traceBack(self, *args):
        self.clearWindow()
        self.labeltest = Label(self.showFrame, pady=10, bg='#fff', text='{}'.format(self.propertyVar.get()))
        self.labeltest.grid(row=0, column=0)
        if self.propertyVar.get() == 'CREATE PROPERTY':
            self.labeltest.grid(row=0, column=0, columnspan=2)
            self.createPropertyClicked()
        elif self.propertyVar.get() == 'DELETE PROPERTY':
            self.labeltest.grid(row=0, column=0, columnspan=2)
            self.deletePropertyClicked()
        elif self.propertyVar.get() == 'VIEW PROPERTY':
            self.viewPropertyClicked()
        elif self.propertyVar.get() == 'UPDATE PROPERTY':
            self.labeltest.grid(row=0, column=0, columnspan=2)
            self.updatePropertyClicked()

    def household_traceBack(self, *args):
        self.clearWindow()
        self.labeltest = Label(self.showFrame, pady=10, bg='#fff', text='{}'.format(self.householdVar.get()))
        self.labeltest.grid(row=0, column=0)

        if self.householdVar.get() == 'CREATE HOUSEHOLD':
            self.labeltest.grid(row=0, column=0, columnspan=2)
            self.createHouseholdClicked()
        elif self.householdVar.get() == 'DELETE HOUSEHOLD':
            self.labeltest.grid(row=0, column=0, columnspan=2)
            self.deleteHouseholdClicked()
        elif self.householdVar.get() == 'VIEW HOUSEHOLD':
            self.viewHouseholdClicked()
        elif self.householdVar.get() == 'UPDATE HOUSEHOLD':
            self.labeltest.grid(row=0, column=0, columnspan=2)
            self.updateHouseholdClicked()

    def receipt_traceBack(self, *args):
        self.clearWindow()
        self.labeltest = Label(self.showFrame, pady=10, bg='#fff', text='{}'.format(self.receiptVar.get()))
        self.labeltest.grid(row=0, column=0)
        if self.receiptVar.get() == 'CREATE RECEIPT':
            self.labeltest.grid(row=0, column=0, columnspan=2)
            self.createReceiptClicked()
        elif self.receiptVar.get() == 'VIEW RECEIPT':
            self.viewReceiptClicked()

# estate functions
    def createEstateClicked(self):
        # list components
        self.create_label = Label(self.showFrame)
        self.create_input = Entry(self.showFrame)
        self.submit_button = Button(self.showFrame)
        # add component to window
        self.create_label.grid(row=1, column=0)
        self.create_input.grid(row=2, column=0)
        self.submit_button.grid(row=3, column=0)
        # style the components
        self.create_label.configure(text="ENTER ESTATE NAME", padx=34, pady=5)
        self.create_input.configure(width=30)
        self.submit_button.configure(text='CREATE', padx=66)
        # assign event
        self.submit_button.configure(command=self.create_estate)

    def create_estate(self):
        name = self.create_input.get()
        estate = Estate(name).show()
        if estate in Estate.Estates:
            if estate not in self.Estate:
                self.Estate.append(estate)
                messagebox.showinfo(title="SUCCESS!!!", message="estate added successfully!")
            else:
                messagebox.showerror(title="ERROR!!!", message="add estate failed!")
            self.create_input.delete(0, 'end')
        else:
            messagebox.showerror(title="ERROR!!!", message="add estate failed!")

    def deleteEstateClicked(self):
        # list components
        self.delete_label = Label(self.showFrame)
        self.delete_input = Entry(self.showFrame)
        self.delete_submit_button = Button(self.showFrame)
        # add components to window
        self.delete_label.grid(row=1, column=0)
        self.delete_input.grid(row=2, column=0)
        self.delete_submit_button.grid(row=3, column=0)
        # style the components
        self.delete_label.configure(text="ENTER ESTATE NAME", padx=34, pady=5)
        self.delete_input.configure(width=30)
        self.delete_submit_button.configure(text='DELETE', padx=68)
        # assign event
        self.delete_submit_button.configure(command=self.delete_estate)

    def delete_estate(self):
        estate = Estate(self.delete_input.get()).show()
        if estate in self.Estate:
            self.Estate.remove(estate)
            messagebox.showinfo(title="SUCCESS!!!", message="estate deleted successfully!")
        else:
            messagebox.showerror(title="ERROR!!!", message="delete estate failed!")
        self.delete_input.delete(0, 'end')

    def viewEstateClicked(self):
        # list components
        self.view_estate_label = Label(self.showFrame)
        self.scroll = Scrollbar(self.showFrame, orient=VERTICAL)
        self.view_estate_list = Listbox(self.showFrame, yscrollcommand=self.scroll.set)

        # add components
        self.view_estate_label.grid(row=1, column=0)
        self.scroll.grid(row=2, column=0, sticky=E)
        self.view_estate_list.grid(row=2, column=0)
        # style the component
        self.view_estate_label.configure(text="Available Estate!", padx=30, pady=10)
        self.scroll.configure(command=self.view_estate_list.yview())
        self.view_estate_list.configure(height=8, width=15)

        # view estate function
        if len(self.Estate) != 0:
            for estates in self.Estate:
                if estates in Estate.Estates:
                    self.view_estate_list.insert(0, estates)
                else:
                    messagebox.showerror(title="ERROR!!!", message="no estate available!")
        else:
            messagebox.showerror(title="ERROR!!!", message="no estate available!")

# thoroughfare functions
    def createThoroughfareClicked(self):
        # list components
        self.create_label = Label(self.showFrame)
        self.create_input = Entry(self.showFrame)
        # drop-down menu
        self.tfare_typeLabel = Label(self.showFrame)
        self.tfare_type = ['street', 'lane', 'crescent', 'close', 'court', 'avenue', 'road']
        self.tfare_typeVar = StringVar(self.showFrame)
        self.tfare_typeVar.set(self.tfare_type[0])
        self.tfare_typeOption = OptionMenu(self.showFrame, self.tfare_typeVar, *self.tfare_type)

        self.tfare_propertyPositionLabel = Label(self.showFrame)
        self.tfare_propertyPosition = ['one-side', 'both-sides']
        self.tfare_propertyPositionVar = StringVar(self.showFrame)
        self.tfare_propertyPositionVar.set(self.tfare_propertyPosition[0])
        self.tfare_propertyPositionOption = OptionMenu(self.showFrame, self.tfare_propertyPositionVar,
                                                       *self.tfare_propertyPosition)

        self.create_button = Button(self.showFrame)
        # add component to window
        self.create_label.grid(row=1, column=0)
        self.create_input.grid(row=1, column=1)
        self.tfare_typeLabel.grid(row=2, column=0)
        self.tfare_typeOption.grid(row=2, column=1)
        self.tfare_propertyPositionLabel.grid(row=3, column=0)
        self.tfare_propertyPositionOption.grid(row=3, column=1)
        self.create_button.grid(row=4, column=0, columnspan=2)
        # style the components
        self.create_label.configure(text="Enter Name", padx=20, pady=5, bg="#fff")
        self.create_input.configure(width=15)
        self.tfare_typeLabel.configure(text='Thoroughfare Type', bg="#fff")
        self.tfare_propertyPositionLabel.configure(text='Property Position', bg="#fff")
        self.create_button.configure(text='CREATE', padx=75)
        # assign event
        self.create_button.configure(command=self.create_thoroughfare)

    def create_thoroughfare(self):
        thoroughfare_name = self.create_input.get()
        thoroughfare_type = self.tfare_typeVar.get()
        property_position = self.tfare_propertyPositionVar.get()

        thoroughfare = Thoroughfare(thoroughfare_name, thoroughfare_type, property_position).show()
        if thoroughfare not in self.Thoroughfares:
            self.Thoroughfares.append(thoroughfare)
            messagebox.showinfo(title="SUCCESS!!!", message="thoroughfare created successfully!")
        else:
            messagebox.showerror(title="ERROR!!!", message="create thoroughfare failed!")
        self.create_input.delete(0, 'end')

    def deleteThoroughfareClicked(self):
        # list components
        self.create_label = Label(self.showFrame)
        self.create_input = Entry(self.showFrame)

        # drop-down menu
        self.tfare_typeLabel = Label(self.showFrame)
        self.tfare_type = ['street', 'lane', 'crescent', 'close', 'court', 'avenue', 'road']
        self.tfare_typeVar = StringVar(self.showFrame)
        self.tfare_typeVar.set(self.tfare_type[0])
        self.tfare_typeOption = OptionMenu(self.showFrame, self.tfare_typeVar, *self.tfare_type)
        self.tfare_propertyPositionLabel = Label(self.showFrame)
        self.tfare_propertyPosition = ['one-side', 'both-sides']
        self.tfare_propertyPositionVar = StringVar(self.showFrame)
        self.tfare_propertyPositionVar.set(self.tfare_propertyPosition[0])
        self.tfare_propertyPositionOption = OptionMenu(self.showFrame, self.tfare_propertyPositionVar,
                                                       *self.tfare_propertyPosition)
        self.delete_button = Button(self.showFrame)
        # add component to window
        self.create_label.grid(row=1, column=0)
        self.create_input.grid(row=1, column=1)
        self.tfare_typeLabel.grid(row=2, column=0)
        self.tfare_typeOption.grid(row=2, column=1)
        self.tfare_propertyPositionLabel.grid(row=3, column=0)
        self.tfare_propertyPositionOption.grid(row=3, column=1)
        self.delete_button.grid(row=4, column=0, columnspan=2)
        # style the components
        self.create_label.configure(text="Enter Name", padx=20, pady=5, bg="#fff")
        self.create_input.configure(width=15)
        self.tfare_typeLabel.configure(text='Thoroughfare Type', bg="#fff")
        self.tfare_propertyPositionLabel.configure(text='Property Position', bg="#fff")
        self.delete_button.configure(text='DELETE', padx=75)
        # assign event
        self.delete_button.configure(command=self.delete_thoroughfare)

    def delete_thoroughfare(self):
        thoroughfare_name = self.create_input.get()
        thoroughfare_type = self.tfare_typeVar.get()
        property_position = self.tfare_propertyPositionVar.get()

        thoroughfare = Thoroughfare(thoroughfare_name, thoroughfare_type, property_position).show()
        if thoroughfare in self.Thoroughfares:
            self.Thoroughfares.remove(thoroughfare)
            messagebox.showinfo(title="SUCCESS!!!", message="thoroughfare deleted successfully!")
        else:
            messagebox.showerror(title="ERROR!!!", message="delete thoroughfare failed!")
        self.create_input.delete(0, 'end')

    def viewThoroughfareClicked(self):
        # list components
        self.view_tfare_label = Label(self.showFrame)
        self.scroll = Scrollbar(self.showFrame, orient=VERTICAL)
        self.view_tfare_list = Listbox(self.showFrame, yscrollcommand=self.scroll.set)

        # add components
        self.view_tfare_label.grid(row=1, column=0)
        self.scroll.grid(row=2, column=0, sticky=E)
        self.view_tfare_list.grid(row=2, column=0)
        # style the component
        self.view_tfare_label.configure(text="Available Thoroughfares!", padx=30, pady=10)
        self.scroll.configure(command=self.view_tfare_list.yview())
        self.view_tfare_list.configure(height=8, width=45)

        # view Thoroughfare function
        if len(self.Thoroughfares) != 0:
            for thoroughfare in self.Thoroughfares:
                self.view_tfare_list.insert(0, thoroughfare)
        else:
            messagebox.showerror(title="ERROR!!!", message="no thoroughfares available!")

    def updateThoroughfareClicked(self):
        # list components
        self.update_enter_label = Label(self.showFrame)
        self.tfare_input = Entry(self.showFrame)
        self.update_enter_label2 = Label(self.showFrame)
        self.new_tfare_input = Entry(self.showFrame)
        # drop-down menu
        self.tfare_typeLabel = Label(self.showFrame)
        self.tfare_type = ['street', 'lane', 'crescent', 'close', 'court', 'avenue', 'road']
        self.tfare_typeVar = StringVar(self.showFrame)
        self.tfare_typeVar.set(self.tfare_type[0])
        self.tfare_typeOption = OptionMenu(self.showFrame, self.tfare_typeVar, *self.tfare_type)
        self.tfare_propertyPositionLabel = Label(self.showFrame)
        self.tfare_propertyPosition = ['one-side', 'both-sides']
        self.tfare_propertyPositionVar = StringVar(self.showFrame)
        self.tfare_propertyPositionVar.set(self.tfare_propertyPosition[0])
        self.tfare_propertyPositionOption = OptionMenu(self.showFrame, self.tfare_propertyPositionVar,
                                                       *self.tfare_propertyPosition)
        self.update_button = Button(self.showFrame)
        # add component to window
        self.update_enter_label.grid(row=1, column=0)
        self.tfare_input.grid(row=1, column=1)
        self.update_enter_label2.grid(row=2, column=0)
        self.new_tfare_input.grid(row=2, column=1)
        self.tfare_typeLabel.grid(row=3, column=0)
        self.tfare_typeOption.grid(row=3, column=1)
        self.tfare_propertyPositionLabel.grid(row=4, column=0)
        self.tfare_propertyPositionOption.grid(row=4, column=1)
        self.update_button.grid(row=5, column=0, columnspan=2)
        # style the components
        self.update_enter_label.configure(text='thoroughfare name', bg="#fff")
        self.tfare_input.configure(width=15)
        self.update_enter_label2.configure(text='new thoroughfare name', bg="#fff")
        self.new_tfare_input.configure(width=15)
        self.tfare_typeLabel.configure(text='Thoroughfare Type', bg="#fff")
        self.tfare_propertyPositionLabel.configure(text='Property Position', bg="#fff")
        self.update_button.configure(text='UPDATE', padx=87)
        # assign event
        self.update_button.configure(command=self.update_thoroughfare)

    def update_thoroughfare(self):
        thoroughfare_name = self.tfare_input.get()
        thoroughfare_type = self.tfare_typeVar.get()
        property_position = self.tfare_propertyPositionVar.get()
        new_thoroughfare_name = self.new_tfare_input.get()
        thoroughfare = Thoroughfare(thoroughfare_name, thoroughfare_type, property_position).show()
        if thoroughfare in self.Thoroughfares:
            for i, item in enumerate(self.Thoroughfares):
                if item == thoroughfare:
                    self.Thoroughfares[i] = Thoroughfare(new_thoroughfare_name, thoroughfare_type,
                                                        property_position).show()
                    messagebox.showinfo(title="SUCCESS!!!", message="thoroughfare updated successfully!")
        else:
            messagebox.showerror(title="ERROR!!!", message="update thoroughfare failed!")
        self.tfare_input.delete(0, 'end')
        self.new_tfare_input.delete(0, 'end')

# property functions
    def createPropertyClicked(self):
        # list components
        self.thoroughfare_name_label = Label(self.showFrame)
        self.thoroughfare_input = Entry(self.showFrame)
        self.property_enter_name_label = Label(self.showFrame)
        self.property_input_name = Entry(self.showFrame)
        self.property_enter_number_label = Label(self.showFrame)
        self.property_input_number = Entry(self.showFrame)
        self.property_enter_date_label = Label(self.showFrame)
        self.property_input_date = Entry(self.showFrame)
        # drop-down menu
        self.building_type_label = Label(self.showFrame)
        self.building_type = ['detached', 'semi-detached', 'terrace', 'block of flats']
        self.building_typeVar = StringVar(self.showFrame)
        self.building_typeVar.set(self.building_type[0])
        self.building_typeOption = OptionMenu(self.showFrame, self.building_typeVar, *self.building_type)
        self.usage_status_label = Label(self.showFrame)
        self.usage_status = ['rented', 'owned', 'managed']
        self.usage_statusVar = StringVar(self.showFrame)
        self.usage_statusVar.set(self.usage_status[0])
        self.usage_statusOption = OptionMenu(self.showFrame, self.usage_statusVar, *self.usage_status)
        self.create_button = Button(self.showFrame)
        # add component to window
        self.thoroughfare_name_label.grid(row=1, column=0)
        self.thoroughfare_input.grid(row=1, column=1)
        self.property_enter_name_label.grid(row=2, column=0)
        self.property_input_name.grid(row=2, column=1)
        self.property_enter_number_label.grid(row=3, column=0)
        self.property_input_number.grid(row=3, column=1)
        self.property_enter_date_label.grid(row=4, column=0)
        self.property_input_date.grid(row=4, column=1)
        self.building_type_label.grid(row=5, column=0)
        self.building_typeOption.grid(row=5, column=1)
        self.usage_status_label.grid(row=6, column=0)
        self.usage_statusOption.grid(row=6, column=1)
        self.create_button.grid(row=7, column=0, columnspan=2)
        # style the components
        self.thoroughfare_name_label.configure(text='thoroughfare name', bg="#fff")
        self.thoroughfare_input.configure(width=15)
        self.property_enter_name_label.configure(text='building name', bg="#fff")
        self.property_input_name.configure(width=15)
        self.property_enter_number_label.configure(text='building number', bg="#fff")
        self.property_input_number.configure(width=15)
        self.property_enter_date_label.configure(text='completion date', bg="#fff")
        self.property_input_date.configure(width=15)
        self.building_type_label.configure(text='building type', bg="#fff")
        self.usage_status_label.configure(text='usage status', bg="#fff")
        self.create_button.configure(text='CREATE', padx=75)
        # assign event
        self.create_button.configure(command=self.create_property)

    def create_property(self):
        thoroughfare_name = self.thoroughfare_input.get()
        building_name = self.property_input_name.get()
        building_number = self.property_input_number.get()
        completion_date = self.property_input_date.get()
        building_type = self.building_typeVar.get()
        usage_status = self.usage_statusVar.get()

        property = Property(thoroughfare_name, building_name, building_number, building_type, usage_status,
                            completion_date).show()
        if property not in self.Properties:
            self.Properties.append(property)
            messagebox.showinfo(title="SUCCESS!!!", message="property created successfully!")
        else:
            messagebox.showerror(title="ERROR!!!", message="property creation failed!")

        self.thoroughfare_input.delete(0, 'end')
        self.property_input_name.delete(0, 'end')
        self.property_input_number.delete(0, 'end')
        self.property_input_date.delete(0, 'end')

    def deletePropertyClicked(self):
        # list components
        self.thoroughfare_name_label = Label(self.showFrame)
        self.thoroughfare_input = Entry(self.showFrame)
        self.property_enter_name_label = Label(self.showFrame)
        self.property_input_name = Entry(self.showFrame)
        self.property_enter_number_label = Label(self.showFrame)
        self.property_input_number = Entry(self.showFrame)
        self.property_enter_date_label = Label(self.showFrame)
        self.property_input_date = Entry(self.showFrame)
        # drop-down menu
        self.building_type_label = Label(self.showFrame)
        self.building_type = ['detached', 'semi-detached', 'terrace', 'block of flats']
        self.building_typeVar = StringVar(self.showFrame)
        self.building_typeVar.set(self.building_type[0])
        self.building_typeOption = OptionMenu(self.showFrame, self.building_typeVar, *self.building_type)
        self.usage_status_label = Label(self.showFrame)
        self.usage_status = ['rented', 'owned', 'managed']
        self.usage_statusVar = StringVar(self.showFrame)
        self.usage_statusVar.set(self.usage_status[0])
        self.usage_statusOption = OptionMenu(self.showFrame, self.usage_statusVar, *self.usage_status)
        self.create_button = Button(self.showFrame)
        # add component to window
        self.thoroughfare_name_label.grid(row=1, column=0)
        self.thoroughfare_input.grid(row=1, column=1)
        self.property_enter_name_label.grid(row=2, column=0)
        self.property_input_name.grid(row=2, column=1)
        self.property_enter_number_label.grid(row=3, column=0)
        self.property_input_number.grid(row=3, column=1)
        self.property_enter_date_label.grid(row=4, column=0)
        self.property_input_date.grid(row=4, column=1)
        self.building_type_label.grid(row=5, column=0)
        self.building_typeOption.grid(row=5, column=1)
        self.usage_status_label.grid(row=6, column=0)
        self.usage_statusOption.grid(row=6, column=1)
        self.create_button.grid(row=7, column=0, columnspan=2)
        # style the components
        self.thoroughfare_name_label.configure(text='thoroughfare name', bg="#fff")
        self.thoroughfare_input.configure(width=15)
        self.property_enter_name_label.configure(text='building name', bg="#fff")
        self.property_input_name.configure(width=15)
        self.property_enter_number_label.configure(text='building number', bg="#fff")
        self.property_input_number.configure(width=15)
        self.property_enter_date_label.configure(text='completion date', bg="#fff")
        self.property_input_date.configure(width=15)
        self.building_type_label.configure(text='building type', bg="#fff")
        self.usage_status_label.configure(text='usage status', bg="#fff")
        self.create_button.configure(text='DELETE', padx=75)
        # assign event
        self.create_button.configure(command=self.delete_property)

    def delete_property(self):
        thoroughfare_name = self.thoroughfare_input.get()
        building_name = self.property_input_name.get()
        building_number = self.property_input_number.get()
        completion_date = self.property_input_date.get()
        building_type = self.building_typeVar.get()
        usage_status = self.usage_statusVar.get()
        property = Property(thoroughfare_name, building_name, building_number, building_type, usage_status,
                            completion_date).show()
        if property in self.Properties:
            self.Properties.remove(property)
            messagebox.showinfo(title="SUCCESS!!!", message="property deleted successfully!")
        else:
            messagebox.showerror(title="ERROR!!!", message="delete property failed!")
        self.thoroughfare_input.delete(0, 'end')
        self.property_input_name.delete(0, 'end')
        self.property_input_number.delete(0, 'end')
        self.property_input_date.delete(0, 'end')

    def viewPropertyClicked(self):
        # list components
        self.view_property_label = Label(self.showFrame)
        self.scroll = Scrollbar(self.showFrame, orient=VERTICAL)
        self.view_property_list = Listbox(self.showFrame, yscrollcommand=self.scroll.set)

        # add components
        self.view_property_label.grid(row=1, column=0)
        self.scroll.grid(row=2, column=0, sticky=W)
        self.view_property_list.grid(row=2, column=0)
        # style the component
        self.view_property_label.configure(text="Available Properties!", padx=30, pady=10)
        self.scroll.configure(command=self.view_property_list.yview())
        self.view_property_list.configure(height=10, width=45)

        # View Property function
        if len(self.Properties) != 0:
            for property in self.Properties:
                self.view_property_list.insert(0, property)
        else:
            messagebox.showerror(title="ERROR!!!", message="no properties available!")

    def updatePropertyClicked(self):
        # property update function
        self.thoroughfare_name_label = Label(self.showFrame)
        self.thoroughfare_input = Entry(self.showFrame)
        self.property_enter_name_label = Label(self.showFrame)
        self.property_input_name = Entry(self.showFrame)
        self.property_enter_number_label = Label(self.showFrame)
        self.property_input_number = Entry(self.showFrame)
        self.property_enter_date_label = Label(self.showFrame)
        self.property_input_date = Entry(self.showFrame)
        # drop-down menu
        self.building_type_label = Label(self.showFrame)
        self.building_type = ['detached', 'semi-detached', 'terrace', 'block of flats']
        self.building_typeVar = StringVar(self.showFrame)
        self.building_typeVar.set(self.building_type[0])
        self.building_typeOption = OptionMenu(self.showFrame, self.building_typeVar, *self.building_type)

        self.usage_status_label = Label(self.showFrame)
        self.usage_status = ['rented', 'owned', 'managed']
        self.usage_statusVar = StringVar(self.showFrame)
        self.usage_statusVar.set(self.usage_status[0])
        self.usage_statusOption = OptionMenu(self.showFrame, self.usage_statusVar, *self.usage_status)
        self.new_thoroughfare_name_label = Label(self.showFrame)
        self.new_thoroughfare_input = Entry(self.showFrame)
        self.new_property_enter_name_label = Label(self.showFrame)
        self.new_property_input_name = Entry(self.showFrame)
        self.new_property_enter_number_label = Label(self.showFrame)
        self.new_property_input_number = Entry(self.showFrame)
        self.new_property_enter_date_label = Label(self.showFrame)
        self.new_property_input_date = Entry(self.showFrame)
        self.create_button = Button(self.showFrame)
        # add component to window
        self.thoroughfare_name_label.grid(row=1, column=0)
        self.thoroughfare_input.grid(row=1, column=1)
        self.property_enter_name_label.grid(row=2, column=0)
        self.property_input_name.grid(row=2, column=1)
        self.property_enter_number_label.grid(row=3, column=0)
        self.property_input_number.grid(row=3, column=1)
        self.property_enter_date_label.grid(row=4, column=0)
        self.property_input_date.grid(row=4, column=1)
        self.building_type_label.grid(row=5, column=0)
        self.building_typeOption.grid(row=5, column=1)
        self.usage_status_label.grid(row=6, column=0)
        self.usage_statusOption.grid(row=6, column=1)
        self.new_thoroughfare_name_label.grid(row=7, column=0)
        self.new_thoroughfare_input.grid(row=7, column=1)
        self.new_property_enter_name_label.grid(row=8, column=0)
        self.new_property_input_name.grid(row=8, column=1)
        self.new_property_enter_number_label.grid(row=9, column=0)
        self.new_property_input_number.grid(row=9, column=1)
        self.new_property_enter_date_label.grid(row=10, column=0)
        self.new_property_input_date.grid(row=10, column=1)
        self.create_button.grid(row=11, column=0, columnspan=2)
        # style the components
        self.thoroughfare_name_label.configure(text='thoroughfare name', bg="#fff")
        self.thoroughfare_input.configure(width=15)
        self.property_enter_name_label.configure(text='building name', bg="#fff")
        self.property_input_name.configure(width=15)
        self.property_enter_number_label.configure(text='building number', bg="#fff")
        self.property_input_number.configure(width=15)
        self.property_enter_date_label.configure(text='completion date', bg="#fff")
        self.property_input_date.configure(width=15)
        self.building_type_label.configure(text='building type', bg="#fff")
        self.usage_status_label.configure(text='usage status', bg="#fff")
        self.new_thoroughfare_name_label.configure(text='new thoroughfare name', bg="#fff")
        self.new_thoroughfare_input.configure(width=15)
        self.new_property_enter_name_label.configure(text='new building name', bg="#fff")
        self.new_property_input_name.configure(width=15)
        self.new_property_enter_number_label.configure(text='new building number', bg="#fff")
        self.new_property_input_number.configure(width=15)
        self.new_property_enter_date_label.configure(text='new completion date', bg="#fff")
        self.new_property_input_date.configure(width=15)
        self.create_button.configure(text='UPDATE', padx=85)
        # assign event
        self.create_button.configure(command=self.update_property)

    def update_property(self):
        thoroughfare_name = self.thoroughfare_input.get()
        building_name = self.property_input_name.get()
        building_number = self.property_input_number.get()
        completion_date = self.property_input_date.get()
        building_type = self.building_typeVar.get()
        usage_status = self.usage_statusVar.get()
        new_thoroughfare_name = self.new_thoroughfare_input.get()
        new_building_name = self.new_property_input_name.get()
        new_building_number = self.new_property_input_number.get()
        new_completion_date = self.new_property_input_date.get()
        property = Property(thoroughfare_name, building_name, building_number, building_type, usage_status,
                            completion_date).show()
        if property in self.Properties:
            for i, item in enumerate(self.Properties):
                if item == property:
                    self.Properties[i] = Property(new_thoroughfare_name, new_building_name, new_building_number,
                                                building_type, usage_status, new_completion_date).show()
                    messagebox.showinfo(title="SUCCESS!!!", message="property updated successfully!")
        else:
            messagebox.showerror(title="ERROR!!!", message="update property failed!")
        self.thoroughfare_input.delete(0, 'end')
        self.property_input_name.delete(0, 'end')
        self.property_input_number.delete(0, 'end')
        self.property_input_date.delete(0, 'end')
        self.new_thoroughfare_input.delete(0, 'end')
        self.new_property_input_name.delete(0, 'end')
        self.new_property_input_number.delete(0, 'end')
        self.new_property_input_date.delete(0, 'end')

        # household functions

# household functions
    def createHouseholdClicked(self):
        # list components
        self.householdname_label = Label(self.showFrame)
        self.householdname_input = Entry(self.showFrame)
        self.custodian_label = Label(self.showFrame)
        self.custodian_input = Entry(self.showFrame)
        # drop-down menu
        self.house_typeLabel = Label(self.showFrame)
        self.house_type = ['single', 'multiple']
        self.house_typeVar = StringVar(self.showFrame)
        self.house_typeVar.set(self.house_type[0])
        self.house_typeOption = OptionMenu(self.showFrame, self.house_typeVar, *self.house_type)
        self.create_button = Button(self.showFrame)
        # add component to window
        self.householdname_label.grid(row=1, column=0)
        self.householdname_input.grid(row=1, column=1)
        self.custodian_label.grid(row=2, column=0)
        self.custodian_input.grid(row=2, column=1)
        self.house_typeLabel.grid(row=3, column=0)
        self.house_typeOption.grid(row=3, column=1)
        self.create_button.grid(row=4, column=0, columnspan=2)
        # style the components
        self.householdname_label.configure(text="Household Name", bg="#fff")
        self.householdname_input.configure(width=15)
        self.custodian_label.configure(text='Custodian Name', bg='#fff')
        self.custodian_input.configure(width=15)
        self.house_typeLabel.configure(text='Household Type', bg="#fff")
        self.create_button.configure(text='CREATE', padx=75)
        # assign event
        self.create_button.configure(command=self.create_household)

    def create_household(self):
        name = self.householdname_input.get()
        custodian = self.custodian_input.get()
        housetype = self.house_typeVar.get()
        household = Household(name, custodian, housetype).show()
        if household not in self.Households:
            self.Households.append(household)
            messagebox.showinfo(title="SUCCESS!!!", message="household created successfully!")
        else:
            messagebox.showerror(title="ERROR!!!", message="household creation failed!")
        self.householdname_input.delete(0, 'end')
        self.custodian_input.delete(0, 'end')

    def deleteHouseholdClicked(self):
        # list components
        self.householdname_label = Label(self.showFrame)
        self.householdname_input = Entry(self.showFrame)
        self.custodian_label = Label(self.showFrame)
        self.custodian_input = Entry(self.showFrame)
        # drop-down menu
        self.house_typeLabel = Label(self.showFrame)
        self.house_type = ['single', 'multiple']
        self.house_typeVar = StringVar(self.showFrame)
        self.house_typeVar.set(self.house_type[0])
        self.house_typeOption = OptionMenu(self.showFrame, self.house_typeVar, *self.house_type)
        self.delete_button = Button(self.showFrame)
        # add component to window
        self.householdname_label.grid(row=1, column=0)
        self.householdname_input.grid(row=1, column=1)
        self.custodian_label.grid(row=2, column=0)
        self.custodian_input.grid(row=2, column=1)
        self.house_typeLabel.grid(row=3, column=0)
        self.house_typeOption.grid(row=3, column=1)
        self.delete_button.grid(row=4, column=0, columnspan=2)
        # style the components
        self.householdname_label.configure(text="Household Name", bg="#fff")
        self.householdname_input.configure(width=15)
        self.custodian_label.configure(text='Custodian Name', bg='#fff')
        self.custodian_input.configure(width=15)
        self.house_typeLabel.configure(text='Household Type', bg="#fff")
        self.delete_button.configure(text='DELETE', padx=75)
        # assign event
        self.create_button.configure(command=self.delete_household)

    def delete_household(self):
        name = self.householdname_input.get()
        custodian = self.custodian_input.get()
        housetype = self.house_typeVar.get()
        household = Household(name, custodian, housetype).show()
        if household in self.Households:
            self.Households.remove(household)
            messagebox.showinfo(title="SUCCESS!!!", message="household deleted successfully!")
        else:
            messagebox.showerror(title="ERROR!!!", message="delete household failed!")
        self.householdname_input.delete(0, 'end')
        self.custodian_input.delete(0, 'end')

    def viewHouseholdClicked(self):
        # household view function
        self.view_household_label = Label(self.showFrame)
        self.scroll = Scrollbar(self.showFrame, orient=VERTICAL)
        self.view_household_list = Listbox(self.showFrame, yscrollcommand=self.scroll.set)
        # add components
        self.view_household_label.grid(row=1, column=0)
        self.scroll.grid(row=2, column=0, sticky=E)
        self.view_household_list.grid(row=2, column=0)
        # style the component
        self.view_household_label.configure(text="Available Households!", padx=30, pady=10)
        self.scroll.configure(command=self.view_household_list.yview())
        self.view_household_list.configure(height=8, width=35)
        # View Household function
        if len(self.Households) != 0:
            for household in self.Households:
                self.view_household_list.insert(0, household)
        else:
            messagebox.showerror(title="ERROR!!!", message="no household available!")

    def updateHouseholdClicked(self):
        # list components
        self.householdname_label = Label(self.showFrame)
        self.householdname_input = Entry(self.showFrame)
        self.custodian_label = Label(self.showFrame)
        self.custodian_input = Entry(self.showFrame)
        # drop-down menu
        self.house_typeLabel = Label(self.showFrame)
        self.house_type = ['single', 'multiple']
        self.house_typeVar = StringVar(self.showFrame)
        self.house_typeVar.set(self.house_type[0])
        self.house_typeOption = OptionMenu(self.showFrame, self.house_typeVar, *self.house_type)
        self.newhouseholdname_label = Label(self.showFrame)
        self.newhouseholdname_input = Entry(self.showFrame)
        self.newcustodian_label = Label(self.showFrame)
        self.newcustodian_input = Entry(self.showFrame)
        self.newhouse_typeLabel = Label(self.showFrame)
        self.newhouse_type = ['single', 'multiple']
        self.newhouse_typeVar = StringVar(self.showFrame)
        self.newhouse_typeVar.set(self.house_type[0])
        self.newhouse_typeOption = OptionMenu(self.showFrame, self.newhouse_typeVar, *self.newhouse_type)
        self.update_button = Button(self.showFrame)
        # add component to window
        self.householdname_label.grid(row=1, column=0)
        self.householdname_input.grid(row=1, column=1)
        self.custodian_label.grid(row=2, column=0)
        self.custodian_input.grid(row=2, column=1)
        self.house_typeLabel.grid(row=3, column=0)
        self.house_typeOption.grid(row=3, column=1)
        self.newhouseholdname_label.grid(row=4, column=0)
        self.newhouseholdname_input.grid(row=4, column=1)
        self.newcustodian_label.grid(row=5, column=0)
        self.newcustodian_input.grid(row=5, column=1)
        self.newhouse_typeLabel.grid(row=6, column=0)
        self.newhouse_typeOption.grid(row=6, column=1)
        self.update_button.grid(row=7, column=0, columnspan=2)
        # style the components
        self.householdname_label.configure(text="Household Name", bg="#fff")
        self.householdname_input.configure(width=15)
        self.custodian_label.configure(text='Custodian Name', bg='#fff')
        self.custodian_input.configure(width=15)
        self.house_typeLabel.configure(text='Household Type', bg="#fff")
        self.update_button.configure(text='CREATE', padx=75)
        self.newhouseholdname_label.configure(text="New Household Name", bg="#fff")
        self.newhouseholdname_input.configure(width=15)
        self.newcustodian_label.configure(text='New Custodian Name', bg='#fff')
        self.newcustodian_input.configure(width=15)
        self.newhouse_typeLabel.configure(text='New Household Type', bg="#fff")
        self.update_button.configure(text='UPDATE', padx=85)
        # assign event
        self.update_button.configure(command=self.update_household)

    def update_household(self):
        name = self.householdname_input.get()
        custodian = self.custodian_input.get()
        housetype = self.house_typeVar.get()
        new_name = self.newhouseholdname_input.get()
        new_custodian = self.newcustodian_input.get()
        new_housetype = self.newhouse_typeVar.get()
        household = Household(name, custodian, housetype).show()
        if household in self.Households:
            for i, item in enumerate(self.Households):
                if item == household:
                    self.Households[i] = Household(new_name, new_custodian, new_housetype).show()
                    messagebox.showinfo(title="SUCCESS!!!", message="household updated successfully!")
        else:
            messagebox.showerror(title="ERROR!!!", message="update household failed!")
        self.householdname_input.delete(0, 'end')
        self.custodian_input.delete(0, 'end')
        self.newhouseholdname_input.delete(0, 'end')
        self.newcustodian_input.delete(0, 'end')

        # receipt functions

# receipt functions
    def createReceiptClicked(self):
        # list components
        self.receipthousehold_label = Label(self.showFrame)
        self.receipthousehold_input = Entry(self.showFrame)
        self.create_button = Button(self.showFrame)
        # add component to window
        self.receipthousehold_label.grid(row=1, column=0)
        self.receipthousehold_input.grid(row=1, column=1)
        self.create_button.grid(row=2, column=0, columnspan=2)
        # style the components
        self.receipthousehold_label.configure(text="Household Name", bg="#fff")
        self.receipthousehold_input.configure(width=15)
        self.create_button.configure(text='GENERATE', padx=75)
        # assign event
        self.create_button.configure(command=self.create_receipt)

    def create_receipt(self):
        household = self.receipthousehold_input.get()
        receipt = Receipt(household).show()
        if receipt not in self.Receipts:
            self.Receipts.append(receipt)
            Receipt.receipts.append(receipt)
            messagebox.showinfo(title="SUCCESS!!!", message="receipt created successfully!")
        else:
            messagebox.showerror(title="ERROR!!!", message="create receipt failed!")
        self.receipthousehold_input.delete(0, 'end')

    def viewReceiptClicked(self):
        # list components
        self.view_receipt_label = Label(self.showFrame)
        self.scroll = Scrollbar(self.showFrame, orient=VERTICAL)
        self.view_receipt_list = Listbox(self.showFrame, yscrollcommand=self.scroll.set)
        # add components
        self.view_receipt_label.grid(row=1, column=0)
        self.scroll.grid(row=2, column=0, sticky=E)
        self.view_receipt_list.grid(row=2, column=0)
        # style the component
        self.view_receipt_label.configure(text="Available Receipts!", padx=30, pady=10)
        self.scroll.configure(command=self.view_receipt_list.yview())
        self.view_receipt_list.configure(height=8, width=25)
        # View Receipt function
        if len(self.Receipts) != 0:
            for receipt in self.Receipts:
                if receipt in Receipt.receipts:
                    self.view_receipt_list.insert(0, receipt)
                else:
                    messagebox.showerror(title="ERROR!!!", message="no receipt available!")
        else:
            messagebox.showerror(title="ERROR!!!", message="no receipt available!")