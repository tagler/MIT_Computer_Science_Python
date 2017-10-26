# PROBLEM 1 ========================================================

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # results
    x = []

    # extract all keys and values
    k = aDict.keys()
    v = aDict.values()

    # temp list to track duplicates
    a = [0]*len(v)

    # find duplicates
    for i in range( len(v) ):
        for j in range( len(v) ):
            if ( i != j ):
                if v[i] == v[j]:
                    a[i] = 1

    # select keys for non-duplicates
    for m in range( len(v) ):
        if a[m] == 0:
            x.append( k[m] )

    # return sorted list
    return sorted(x)

# test cases
aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
aDict = {1: 1, 2: 1, 3: 1}

# PROBLEM 2 ============================================================

class courseInfo(object):

    def __init__(self, courseName):
        self.courseName = courseName
        self.psetsDone = []
        self.grade = "No Grade"

    def setPset(self, pset, score):
        self.psetsDone.append((pset, score))

    def getPset(self, pset):
        for (p, score) in self.psetsDone:
            if p == pset:
                return score

    def setGrade(self, grade):
        if self.grade == "No Grade":
            self.grade = grade

    def getGrade(self):
        return self.grade

class edx(object):
    def __init__(self, courses):
        self.myCourses = []
        for course in courses:
            self.myCourses.append(courseInfo(course))

    def setGrade(self, grade, course="6.03x"):
        """
        grade: integer greater than or equal to 0 and less than or equal to 100
        course: string

        This method sets the grade in the courseInfo object named by `course`.

        If `course` was not part of the initialization, then no grade is set, and no
        error is thrown.

        The method does not return a value.
        """
        for x in self.myCourses:
            if x.courseName == course:
                x.grade = grade

    def getGrade(self, course="6.02x"):
        """
        course: string

        This method gets the grade in the the courseInfo object named by `course`.

        returns: the integer grade for `course`.
        If `course` was not part of the initialization, returns -1.
        """
        for y in self.myCourses:
            if y.courseName == course:
                return y.grade
        return -1

    def setPset(self, pset, score, course="6.00x"):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string

        The `score` of the specified `pset` is set for the
        given `course` using the courseInfo object.

        If `course` is not part of the initialization, then no pset score is set,
        and no error is thrown.
        """
        for z in self.myCourses:
            if z.courseName == course:
                z.psetsDone.append((pset, score))

    def getPset(self, pset, course="6.00x"):
        """
        pset: a string or a number
        course: string

        returns: The score of the specified `pset` of the given
        `course` using the courseInfo object.
        If `course` was not part of the initialization, returns -1.
        """
        #   fill in code to get the pset
        for w in self.myCourses:
            if w.courseName == course:
                for (p, score) in w.psetsDone:
                    if p == pset:
                        return score
                return None
        return -1

edX = edx( ["6.00x","6.01x","6.02x"] )
edX.setPset(1,100)
edX.setPset(2,100,"6.00x")
edX.setPset(2,90,"6.00x")

edX.setGrade(100)

for c in ["6.00x","6.01x","6.02x"]:
    edX.setGrade(90,c)

# PROBLEM 3 ============================================================

class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name

class USResident(Person):
    """
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """
        Initializes a Person object. A USResident object inherits
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        if status == 'citizen':
            self.status = status
        elif status == 'legal_resident':
            self.status = status
        elif status == 'illegal_resident':
            self.status = status
        else:
            raise ValueError

    def getStatus(self):
        """
        Returns the status
        """
        return self.status

a = USResident('Tim Beaver', 'citizen')
print a.getStatus()
b = USResident('Tim Horton', 'non-resident')
