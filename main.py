class Data:
    def __init__(self):
        self.student_list8 = [] #listfor8
        self.student_list9 = [] #listfor9
        self.student_list10 = [] #listfor10
        self.avgMarks = 0
        self.totalDays = 0
        self.totalDays8 = 0
        self.totalDays9 = 0
        self.totalDays10 = 0
        self.totalEarning = 0
        self.totalEarning8 = 0
        self.totalEarning9 = 0
        self.totalEarning10 = 0
        self.earningE = 0
        self.earningM = 0
        self.earningB = 0

    def add_std (self):
        print("1 for class 8")
        print("2 for class 9")
        print("3 for class 10")
        cls = input()
        if cls == '1':
            while True:
                print('Press 1 if you  want to add student.')
                print('Or press any key for exit from add student')
                a = int(input('press number: '))
                if a == 1:
                    d1 = {}
                    d1['name'] = input('student name: ')
                    d1['math'] = int(input('Press 1 if yes or 0 for no:'))
                    if d1['math'] == 1:
                        m1 = int(input('enter the earning from math subject: '))
                        self.earningM = self.earningM + m1
                    d1['english'] = int(input('Press 1 if yes or 0 for no:'))
                    if d1['english'] == 1:
                        e1 = int(input('enter the earning from english subject: '))
                        self.earningE = self.earningE + e1
                    d1['bangla'] = int(input('Press 1 if yes or 0 for no:'))
                    if d1['bangla'] == 1:
                        b1 = int(input('enter the earning from bangla subject: '))
                        self.earningB = self.earningB + b1
                    d1['ID'] = int(input('Student ID:'))
                    d1['avgMarks'] = int(input('avg marks: '))
                    d1['totalDays'] = int(input('Total Days taught: '))
                    d1['totalEarnings'] = int(input('Total Earnings: '))
                    self.student_list8.append(d1)
                    print('Successfully add student')
                    self.totalDays = self.totalDays + d1['totalDays']
                    self.totalDays8 = self.totalDays8 + d1['totalDays']
                    self.avgMarks = self.avgMarks + d1['avgMarks']
                    self.totalEarning = self.totalEarning + d1['totalEarnings']
                    self.totalEarning8 = self.totalEarning8 + d1['totalEarnings']
                    print('--------*--------------*---------')
                else:
                    self.main_menu()
                    break
        elif cls == '2':
            while True:
                print('Press 1 if you  want to add student.')
                print('Or press any key for exit from add student')
                a = int(input('press number: '))
                if a == 1:
                    d2 = {}
                    d2['name'] = input('student name: ')
                    d2['math'] = int(input('Press 1 if yes or 0 for no:'))
                    if d2['math'] == 1:
                        m2 = int(input('enter the earning from math subject: '))
                        self.earningM = self.earningM + m2
                    d2['english'] = int(input('Press 1 if yes or 0 for no:'))
                    if d2['english'] == 1:
                        e2 = int(input('enter the earning from english subject: '))
                        self.earningE = self.earningE + e2
                    d2['bangla'] = int(input('Press 1 if yes or 0 for no:'))
                    if d2['bangla'] == 1:
                        b2 = int(input('enter the earning from bangla subject: '))
                        self.earningB = self.earningB + b2
                    d2['ID'] = int(input('Student ID:'))
                    d2['avgMarks'] = int(input('avg marks: '))
                    d2['totalDays'] = int(input('Total Days taught: '))
                    d2['totalEarnings'] = int(input('Total Earnings: '))
                    self.student_list9.append(d2)
                    print('Successfully add student')
                    self.totalDays = self.totalDays + d2['totalDays']
                    self.totalDays9 = self.totalDays9 + d2['totalDays']
                    self.avgMarks = self.avgMarks + d2['avgMarks']
                    self.totalEarning = self.totalEarning + d2['totalEarnings']
                    self.totalEarning9 = self.totalEarning9 + d2['totalEarnings']
                    print('--------*--------------*---------')
                else:
                    self.main_menu()
                    break
        elif cls =='3':
            while True:
                print('Press 1 if you  want to add student.')
                print('Or press any key for exit from add student')
                a = int(input('press number: '))
                if a == 1:
                    d3 = {}
                    d3['name'] = input('student name: ')
                    d3['math'] = int(input('Press 1 if yes or 0 for no:'))
                    if d3['math'] == 1:
                        m3 = int(input('enter the earning from math subject: '))
                        self.earningM = self.earningM + m3
                    d3['english'] = int(input('Press 1 if yes or 0 for no:'))
                    if d3['english'] == 1:
                        e3 = int(input('enter the earning from english subject: '))
                        self.earningE = self.earningE + e3
                    d3['bangla'] = int(input('Press 1 if yes or 0 for no:'))
                    if d3['bangla'] == 1:
                        b3 = int(input('enter the earning from bangla subject: '))
                        self.earningB = self.earningB + b3
                    d3['ID'] = int(input('Student ID:'))
                    d3['avgMarks'] = int(input('avg marks: '))
                    d3['totalDays'] = int(input('Total Days taught: '))
                    d3['totalEarnings'] = int(input('Total Earnings: '))
                    self.student_list10.append(d3)
                    print('Successfully add student')
                    self.totalDays = self.totalDays + d3['totalDays']
                    self.totalDays10 = self.totalDays10 + d3['totalDays']
                    self.avgMarks = self.avgMarks + d3['avgMarks']
                    self.totalEarning = self.totalEarning + d3['totalEarnings']
                    self.totalEarning10 = self.totalEarning10 + d3['totalEarnings']
                    print('--------*--------------*---------')
                else:
                    self.main_menu()
                    break


    def edit_std (self):
        while True:
            marks = 0
            count=0
            print('Press 1 for edit student or Press anything:')
            a = int(input('press number: '))
            if a == 1:
                print("1 for class 8")
                print("2 for class 9")
                print("3 for class 10")
                cls =int(input('Enter class:'))
                if cls == 1:
                    b = int(input('Enter the student id that you want to edit in class 8: '))
                    t = int(input('Enter the total days:'))
                    for i in range(len(self.student_list8)):
                        if b == self.student_list8[i]:
                            self.student_list8[i]['totalDays']= self.student_list8[i]['totalDays']+t
                        if self.student_list8[i]['math'] == 1:
                            m = int(input('Enter the math marks:'))
                            marks=marks+m
                            count = count+1
                            self.earningM = self.earningM + t
                        if self.student_list8[i]['english'] == 1 :
                            m = int (input('Enter the english marks:'))
                            marks = marks + m
                            count = count + 1
                            self.earningE = self.earningE + t
                        if self.student_list8[i]['bangla'] == 1:
                            m = int(input('Enter the bangla marks:'))
                            marks = marks + m
                            count = count + 1
                            self.earningB = self.earningB + t

                    e = t*count*1
                    AVG = marks/count
                    self.totalDays8=self.totalDays8+t
                    self.student_list8[i]['totalEarnings']= self.student_list8[i]['totalEarnings']+e
                    self.totalEarning = self.totalEarning + self.student_list8[i]['totalEarnings']
                    self.totalEarning8 = self.totalEarning8 + self.student_list8[i]['totalEarnings']
                    self.student_list8[i]['avgMarks'] = self.student_list8[i]['avgMarks'] + AVG
                    self.avgMarks = self.avgMarks + self.student_list8[i]['avgMarks']
                elif cls == 2:
                    b = int(input('Enter the student id that you want to edit in class 9: '))
                    t = int(input('Enter the total days:'))
                    for i in range(len(self.student_list8)):
                        if b == self.student_list9[i]:
                            self.student_list9[i]['totalDays']= self.student_list9[i]['totalDays']+t
                        if self.student_list9[i]['math'] == 1:
                            m = int(input('Enter the math marks:'))
                            marks=marks+m
                            count = count+1
                            self.earningM = self.earningM + t
                        if self.student_list9[i]['english'] == 1 :
                            m = int (input('Enter the english marks:'))
                            marks = marks + m
                            count = count + 1
                            self.earningE = self.earningE + t
                        if self.student_list9[i]['bangla'] == 1:
                            m = int(input('Enter the bangla marks:'))
                            marks = marks + m
                            count = count + 1
                            self.earningB = self.earningB + t

                    e = t*count*1
                    AVG = marks/count
                    self.totalDays9 = self.totalDays9 + t
                    self.student_list9[i]['totalEarnings']= self.student_list9[i]['totalEarnings']+e
                    self.totalEarning = self.totalEarning + self.student_list9[i]['totalEarnings']
                    self.totalEarning9 = self.totalEarning9 + self.student_list9[i]['totalEarnings']
                    self.student_list9[i]['avgMarks'] = self.student_list9[i]['avgMarks'] + AVG
                    self.avgMarks = self.avgMarks + self.student_list9[i]['avgMarks']
                elif cls == 3:
                    b = int(input('Enter the student id that you want to edit in class 10: '))
                    t = int(input('Enter the total days:'))
                    for i in range(len(self.student_list10)):
                        if b == self.student_list10[i]:
                            self.student_list10[i]['totalDays']= self.student_list8[i]['totalDays']+t
                        if self.student_list10[i]['math'] == 1:
                            m = int(input('Enter the math marks:'))
                            marks=marks+m
                            count = count+1
                            self.earningM = self.earningM + t
                        if self.student_list10[i]['english'] == 1 :
                            m = int (input('Enter the english marks:'))
                            marks = marks + m
                            count = count + 1
                            self.earningE = self.earningE + t
                        if self.student_list10[i]['bangla'] == 1:
                            m = int(input('Enter the bangla marks:'))
                            marks = marks + m
                            count = count + 1
                            self.earningB = self.earningB + t

                    e = t*count*1
                    AVG = marks/count
                    self.totalDays10 = self.totalDays10 + t
                    self.student_list10[i]['totalEarnings']= self.student_list10[i]['totalEarnings']+e
                    self.totalEarning = self.totalEarning + self.student_list10[i]['totalEarnings']
                    self.totalEarning10 = self.totalEarning10 + self.student_list10[i]['totalEarnings']
                    self.student_list10[i]['avgMarks'] = self.student_list8[i]['avgMarks'] + AVG
                    self.avgMarks = self.avgMarks + self.student_list10[i]['avgMarks']
            else:
                self.main_menu()
                break
    def delete_std (self):
        while True:
            print('Press 1 if you  want to delete student.')
            print('Or press any key for exit from delete student')
            a = int(input('Press number: '))
            if a == 1:
                print("1 for class 8")
                print("2 for class 9")
                print("3 for class 10")
                cls = int(input('Enter class:'))
                if cls == 1:
                    b1 = int(input('Enter student id: '))
                    for i in range(len(self.student_list8)):
                        if self.student_list8[i]['ID'] == b1:
                            del self.student_list8[i]
                            print('Successfully deleted student from list')
                            print('------*----------------*-----------')
                        else:
                            print('Not in student list')
                            print('-------*-----------------*-----------')
                elif cls == 2:
                    b2 = int(input('Enter student id: '))
                    for i in range(len(self.student_list9)):
                        if self.student_list9[i]['ID'] == b2:
                            del self.student_list9[i]
                            print('Successfully deleted student from list')
                            print('------*----------------*-----------')
                        else:
                            print('Not in student list')
                            print('-------*-----------------*-----------')
                elif cls == 3:
                    b3 = int(input('Enter student id: '))
                    for i in range(len(self.student_list10)):
                        if self.student_list10[i]['ID'] == b3:
                            del self.student_list10[i]
                            print('Successfully deleted student from list')
                            print('------*----------------*-----------')
                        else:
                            print('Not in student list')
                            print('-------*-----------------*-----------')
            else:
                self.main_menu()
                break

    def list_std (self):
        print("1 for class 8")
        print("2 for class 9")
        print("3 for class 10")
        cls = int(input('Enter class:'))
        if cls == 1:
            print("Name" + " " + "TotalEarnings" + " " + "AverageMarks" )
            for i in range(len(self.student_list8)):
                print(self.student_list8[i]['name'] + "   " + str(self.student_list8[i]['totalEarnings']) + "   " + str(
                    self.student_list8[i]['avgMarks']))
                print('\n')
            print('-----*---------------*-----------')
            print('Press 1 for seeing individual student info or Press anything:')
            x = int(input('press number: '))
            if x == 1:
                b8 = int(input('Enter student id: '))
                for i in range(len(self.student_list8)):
                    if self.student_list8[i]['ID'] == b8:
                        print(self.student_list8[i])
                        print('------*----------------*-----------')
                    #else:
                        #print('Not in student list')
                        #print('-------*-----------------*-----------')

        elif cls == 2:
            print("Name" + " " + "TotalEarnings" + " " + "AverageMarks")
            for i in range(len(self.student_list9)):
                print(self.student_list9[i]['name'] + "   " + str(
                    self.student_list9[i]['totalEarnings']) + "   " + str(
                    self.student_list9[i]['avgMarks']))
                print('\n')
            print('-----*---------------*-----------')
            print('Press 1 for seeing individual student info or Press anything:')
            x = int(input('press number: '))
            if x == 1:
                b9 = int(input('Enter student id: '))
                for i in range(len(self.student_list9)):
                    if self.student_list9[i]['ID'] == b9:
                        print(self.student_list9[i])
                        print('------*----------------*-----------')
                    else:
                        print('Not in student list')
                        print('-------*-----------------*-----------')
        elif cls == 3:
            print("Name" + " " + "TotalEarnings" + " " + "AverageMarks")
            for i in range(len(self.student_list10)):
                print(self.student_list10[i]['name'] + "   " + str(
                    self.student_list10[i]['totalEarnings']) + "   " + str(
                    self.student_list10[i]['avgMarks']))
                print('\n')
            print('-----*---------------*-----------')
            print('Press 1 for seeing individual student info or Press anything:')
            x = int(input('press number: '))
            if x == 1:
                b10 = int(input('Enter student id: '))
                for i in range(len(self.student_list10)):
                    if self.student_list10[i]['ID'] == b10:
                        print(self.student_list10[i])
                        print('------*----------------*-----------')
                    else:
                        print('Not in student list')
                        print('-------*-----------------*-----------')
        self.main_menu()




    def overall_info (self):
        print('Total Days')
        print(self.totalDays)
        print('Total Days for class 8')
        print(self.totalDays8)
        print('Total Days for class 9')
        print(self.totalDays9)
        print('Total Days for class 10')
        print(self.totalDays10)
        print('Average Marks')
        print(self.avgMarks)
        print('Total Earnings')
        print(self.totalEarning)
        print('Earning from subject math: ')
        print(self.earningM)
        print('Earning from subject english: ')
        print(self.earningE)
        print('Earning from subject bangla: ')
        print(self.earningB)
        print('Total Earnings for class 8')
        print(self.totalEarning8)
        print('Total Earnings for class 9')
        print(self.totalEarning9)
        print('Total Earnings for class 10')
        print(self.totalEarning10)

        self.main_menu()

    def main_menu (self):
        print('1.Add Student')
        print('2.Edit Student')
        print('3.Delete Student')
        print('4.See list of student')
        print('5.See overall information')
        print('-----------------------------------------------')
        print('Enter the number what you want to do:')
s = Data()
s.main_menu()

while True:
    num = input()
    if num == '1':
        s.add_std()
    elif num == '2':
        s.edit_std()
    elif num == '3':
        s.delete_std()
    elif num == '4':
        s.list_std()
    elif num == '5':
        s.overall_info()
    else:
        s.main_menu()



