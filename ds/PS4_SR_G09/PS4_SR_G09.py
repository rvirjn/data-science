# Description: Data Structure Assignment-1
# ASSIGNMENT1_BLR_B2_G09


class Student:
    def __init__(self):
        pass

    def initializeHash(self):
        """
        This function creates an empty hash table and points to null

        :param self:
        :return:
        """

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

    def hallOfFame(self, StudentHashRecords, CGPA):
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

    def destroyHash(StudentHashRecords):
        """
        This function destroys all the entries inside hashtable.
        This is a clean-up code

        :param StudentHashRecords:
        :return:
        """