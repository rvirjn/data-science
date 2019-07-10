# Description: Data Structure Assignment-1
# ASSIGNMENT1_BLR_B2_G09

import re

class Student:
    def __init__(self):
        pass

    def initializeHash(self):
        """
        This function creates an empty hash table and points to null

        :param self:
        :return:
        """
        StudentHashRecords = {}
        return StudentHashRecords


def insertStudentRec(StudentHashRecords, studentId, CGPA):
    """
    This  function  inserts  the student id and corresponding CPGA into the
    hash table. The inputs need to be read from a file inputPS4.txt which
    contains the student ID and overall graduating CGPA (decimal value
    with a maximum of 5.0 points). The file read can happen outside the
    function and only the information in every individual row needs to be
    passed to the function

    :param studentId:
    :param CGPA:
    :return:
    """
    StudentHashRecords[studentId] = CGPA
    return StudentHashRecords


def hallOfFame(StudentHashRecords, CGPA):
    """
    This function prints the list of all students who have a CGPA greater
    than the CGPA passed to the function. The input CGPA can be read from
    the file promptsPS4.txt. The input can be identified with the tag
    mentioned below

    hallOfFame: 4.5

    This hall of fame list should be output in a file outputPS4.txt
    and should contain the studentid and CGPA.

    Output format:
    ----------
    hall of fame
    ----------
    Input: 4.5
    Total eligible students: 2
    Qualified students:
    2008CSE1225 / 4.5
    2008CSE1226 / 4.8
    -------------------------------------
    :param StudentHashRecords:
    :param CGPA:
    :return: Output
    """
    temp = {}
    count = 0
    output_format = """
    ----------hall of fame-----------------------
    Input: {CGPA}
    Total eligible students: {count}
    Qualified students:
    {Qualified_students}
    -------------------------------------------------
    """
    student_format = """{key} / {value}"""
    Qualified_students = ''
    for key in StudentHashRecords.keys():
        value = StudentHashRecords[key]
        if value == CGPA or value > CGPA:
            count = count + 1
            temp[key] = value
    for key in temp.keys():
        value = StudentHashRecords[key]
        Qualified_students = Qualified_students + ((student_format.format(key=key,
                                                         value=value))).strip() + '\n'
    output = output_format.format(CGPA=CGPA, count=count,
                           Qualified_students=Qualified_students)
    print(output)
    return output


def newCourseList(StudentHashRecords, CGPAFrom, CPGATo):
    """
    This function prints the list of all students who have a CGPA within
    the given range and have graduated in the last 5 years. The input
    CGPAs can be read from the file promptsPS4.txt. The input can be
    identified with the tag mentioned below

    courseOffer: 3.5 : 4:0

    This list should be output to outputPS4.txt that contains the student id and CGPA.

    Output format:
    ---------- new course candidates ----------
    Input: 3.5 to 4.0
    Total eligible students: 2
    Qualified students:
    2008CSE1223 / 3.5
    2008CSE1224 / 3.9
    ------------------------------------

    :param CGPAFrom:
    :param CPGATo:
    :return: Output
    """
    temp = {}
    count = 0
    Output_format = """
    ---------- new course candidates ------------------
    Input: {CGPAFrom} to {CPGATo}
    Total eligible students: {count}
    Qualified students:
    {students}
    -----------------------------------------------------
    """
    student_format = """{key} / {value}"""
    Qualified_students = ''
    for key in StudentHashRecords.keys():
        value = StudentHashRecords[key]
        if value >= CGPAFrom or value >= CPGATo:
            count = count + 1
            temp[key] = value
    for key in temp.keys():
        value = StudentHashRecords[key]
        Qualified_students = Qualified_students + ((student_format.format(key=key,
                                                         value=value))).strip() + '\n'

    output = Output_format.format(CPGATo=CPGATo, CGPAFrom=CGPAFrom,
                                   count=count,
                               students=Qualified_students)
    print(output)
    return output


def depAvg(StudentHashRecords):
    """
    This function prints the list of all departments followed by the
    maximum CGPA and average CGPA of all students in that department.
    The output should be captured in outputps4.txt following format

    Output format:
    ---------- department CGPA ----------
    CSE: max: 3.5, avg: 3.4
    MEC: max: 3.5, avg: 3.4
    ECE: max: 3.5, avg: 3.4
    ARC: max: 3.5, avg: 3.4
    -------------------------------------

    (Note: the above output numbers are indicative and not actuals.)

    :param StudentHashRecords:
    :return:
    """
    output_format = """
    ---------- department CGPA -------------
    {students}
    -----------------------------------------
    """
    student_format="""{dept}: max: {dept_max}, avg: {dept_avg}"""
    students = ''
    for key in StudentHashRecords.keys():
        value = StudentHashRecords[key]
        dept = re.split('(\d+)', key)[2]
        students = students + ((student_format.format(dept=dept, dept_max=value,
                                      dept_avg=value))).strip() + '\n'
    output = output_format.format(students=students)
    print(output)
    return output


def destroyHash(StudentHashRecords):
    """
    This function destroys all the entries inside hashtable.
    This is a clean-up code

    :param StudentHashRecords:
    :return:
    """
    StudentHashRecords.clear()
    return StudentHashRecords


def writeTofile(output):
    f = open("outputPS4.txt", "a")
    f.write(output)
    f.close()


if __name__ == "__main__":
    student = Student()
    StudentHashRecords = student.initializeHash()

    # create outputPS4.txt
    open("outputPS4.txt", "w").close()

    # input for function insertStudentRec()
    with open('inputPS4.txt') as input:
        lines = input.readlines()
        for line in lines:
            studentId = line.split('/')[0].strip()
            CGPA = line.split('/')[1].strip()
            insertStudentRec(StudentHashRecords, studentId, CGPA)

    # input for function hallOfFame()
    with open('promptsPS4.txt') as input:
        lines = input.readlines()
        for line in lines:
            if 'hallOfFame:' in line:
                CGPA = line.split('hallOfFame:')[1].strip()
    hallOfFame_output = hallOfFame(StudentHashRecords, CGPA)

    writeTofile(hallOfFame_output)

    # input for function newCourseList()
    with open('promptsPS4.txt') as input:
        lines = input.readlines()
        for line in lines:
            if 'courseOffer:' in line:
                rng  = line.split('courseOffer:')[1].strip()
                CGPAFrom = rng.split(':')[0].strip()
                CPGATo = rng.split(':')[1].strip()
    newCourseList_output = newCourseList(StudentHashRecords, CGPAFrom, CPGATo)
    writeTofile(newCourseList_output)

    # department CGPA
    depAvg_output = depAvg(StudentHashRecords)
    writeTofile(depAvg_output)

    # clean-up code
    StudentHashRecords = destroyHash(StudentHashRecords)