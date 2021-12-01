"""
1A:
[[1], [[2]], 0, 1]
[[1], [[2]], 0, 1]
Note that extending b to a doesn't mean a is connected to b.

1B:
{'m': 1, 'i': 4, 's': 4, 2: 1, 3: 1, 4: 1, 'p': 2}
The order doesn't matter.

1C:
1
8
8
8

1D:
F
165
F

1E:
54

1F:
2
2
6
12
Don't get confused between the functions p, q and the variables p, q!
"""


## Question 2
answers = [
    ["Russell", "0930", "recursion"], ["Keng Hwee", "1020", "recursive"],
    ["Jonathan", "1021", "recurse"], ["Wei Han", "1100", "recursion"],
    ["Gerald", "1104", "recursion tree"], ["Hoi Yin", "1216", "recurse"]
]

# 2A
def minutes(time):
    return int(time[:2])*60 + int(time[2:])

# 2B
def get_answer(answers, name):
    for ans in answers:
        if ans[0] == name:
            return ans[2]
    return None

# 2C
def submit_answer(answers, name, time, answer):
    answers.append([name, time, answer])

# 2D
def resubmit_answer_wrong(answers, name, time, answer):
    for ans in answers:
        if ans[0] == name:
            ans = [name, time, answers]
        
def resubmit_answer(answers, name, time, answer):
    for i in range(len(answers)):
        if answers[i][0] == name:
            answers[i] = [name, time, answer]
            return

# 2E
def similarity_score(str1, str2):
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    n = min(len(str1), len(str2))
    k = 0
    for i in range(n):
        if str1[i] == str2[i]:
            k += 1
    return k/n

# 2F
def blame(answers, name1, name2):
    def get_time(answers, name):
        for ans in answers:
            if ans[0] == name:
                return ans[1]

    return abs(minutes(get_time(answers, name1)) - minutes(get_time(answers, name2))) < 60 \
           and similarity_score(get_answer(answers, name1), get_answer(answers, name2)) >= 0.8

# 2G
# A possible solution might be modifying the resubmit_answer function to not overwrite the submission.
# Instead, we use the normal submit_answer method even for resubmission.
# But this means we have to slightly modify get_answer to return a sequence of multiple answers
# in case someone has more than one submission.
# Consequently, we might also have to slightly modify the blame function to iterate through each of one's answers.

# Another possible implementation is to convert an answer data from (name, time, answer) to (name, time, answers)
# where answers is now a list of strings!


## Question 3
home = {
    'a.py': None,
    'b': {
        'd.py': None,
        'e.py': None,
    },
    'c': {
        'f.py': None,
        'g': {
            'i.py': None,
            'j.java': None
        },
        'h': {}
    }
}

# 3A
def cd(directory, path):
    steps = path.split("/")
    result = directory
    for s in steps[:-1]:
        result = result[s]
    return result
"""
print(cd(home, "c/."))
print(cd(home['b'], "."))
print(cd(home, "c/g/."))
"""

# 3B
# O(level) where level is the number of levels to traverse through
# Other implementations may have different time complexities and different notations

# 3C
def rename(directory, path, old_name, new_name):
    d = cd(directory, path)
    if new_name not in d:
        for name in d:
            if name == old_name:
                d[new_name] = d[old_name]
                del d[old_name]
                return # break is also okay
                # This way, we can prevent the RunTimeError from happening
                # (dictionary changed size during iteration)

"""
rename(home, "c/g/.", "i.py", "j.java")
print(home)
rename(home, "c/g/.", "i.py", "k.py")
print(home)
rename(home, "c/g/.", "i.py", "l.py")
print(home)
"""

# 3D
def copy(directory, path, new_path):
    d = cd(directory, path)
    new_d = cd(directory, new_path)
    for names in d:
        new_d[names] = d[names]

"""
copy(home, "c/g/.", ".")
print(home)
"""

"""
# BONUS PART
copy(home, ".", "c/.")
print(home)
"""

# 3E
def move(directory, path, new_path):
    d = cd(directory, path)
    new_d = cd(directory, new_path)
    d2 = d.copy()
    d.clear()
    for names in d2:
        new_d[names] = d2[names]

# The reason why move(home, ".", ".") exists
def move_wrong(directory, path, new_path):
    d = cd(directory, path)
    new_d = cd(directory, new_path)
    for names in d:
        new_d[names] = d[names]
    d.clear()

"""
print(cd(home, "c/."))
move(home, "c/g/.", ".")
print(home)
move(home, ".", ".")
print(home)
move(home, "c/.", "c/.")
print(cd(home, "c/."))
"""

## Question 4
class Cell:
    def __init__(self, health, damage):
        self.health = min(100, health)
        self.damage = damage
        self.dead = False

    def regenerate(self):
        self.health = min(100, self.health + 20)

class RedBloodCell(Cell):
    def __init__(self, health, damage, utility):
        super().__init__(health, damage)
        self.utility = utility

    def regenerate(self):
        self.health = min(100, self.health + 30 * self.utility)

# 4A
# 40, 79.0 (not 79), AttributeError, 100
blood = RedBloodCell(40 , 0, 1.3)

# 4B
"""
dead_blood = RedBloodCell(0, 0, 1.5)
print(dead_blood.health) # 0
dead_blood.regenerate()
print(dead_blood.health) # 45.0, what?
"""
# This is because we haven't made use of the self.dead attribute. We can simply add them as conditionals on
# both classes' implementation of regenerate.
# (writing the modified function only is acceptable, in this case Cell.regenerate() and RBC.regenerate())
class Cell:
    def __init__(self, health, damage):
        self.health = min(100, health)
        self.damage = damage
        self.dead = False

    def regenerate(self):
        if not self.dead:
            self.health = min(100, self.health + 20)

class RedBloodCell(Cell):
    def __init__(self, health, damage, utility):
        super().__init__(health, damage)
        self.utility = utility

    def regenerate(self):
        if not self.dead:
            self.health = min(100, self.health + 30 * self.utility)

# 4C
class WhiteBloodCell(Cell):
    def __init__(self, damage, utility):
        self.health = 30
        self.damage = damage
        # using super().__init__(30, damage) is okay I guess
        self.utility = utility
        self.dead = False

    def regenerate(self):
        if not self.dead:
            self.health = min(100, self.health + 30 * self.utility)
            self.utility *= 1.1

    def attack(self, other):
        if other != self:
            if self.health < 50:
                print("Cell needs to regenerate...")
            else:
                other.health = max(0, other.health - self.damage * self.utility)
                if other.health == 0:
                    other.dead = True
                if isinstance(other, RedBloodCell):
                    other.utility *= 0.7
                print("Cell attacked!")

"""
U1146 = WhiteBloodCell(40, 1.5)
ordinary = Cell(30, 1)
U1146.attack(U1146)
U1146.attack(ordinary)
print(ordinary.health)  # 30
U1146.regenerate()
U1146.attack(ordinary)
print(ordinary.health)  # 0

U1147 = WhiteBloodCell(40, 1.5)
AE3803 = RedBloodCell(80, 0, 1.2)
U1147.regenerate()
U1147.attack(AE3803)
print(AE3803.health)    # 14.0
print(AE3803.utility)   # 0.84
"""

# 4D
class CancerCell(RedBloodCell, WhiteBloodCell):
    pass

cancer = CancerCell(100, 1000, 1.7)
skin = Cell(50, 1)
# cancer.attack(skin)

# There is a diamond inheritance here. Note that the super().__init__(health, damage) in RBC does not refer to Cell anymore but WBC.
# However, we cannot swap RBC and WBC as they have a different number of constructor parameters.
# A way to fix this is to modify RBC's constructor method to manually assign the properties instead of calling super().__init__
# Here's a better one.
class RedBloodCell(Cell):
    def __init__(self, health, damage, utility):
        self.health = health
        self.damage = damage
        self.dead = False
        self.utility = utility

    def regenerate(self):
        if not self.dead:
            self.health = min(100, self.health + 30 * self.utility)

class CancerCell(RedBloodCell, WhiteBloodCell):
    pass

cancer = CancerCell(100, 1000, 1.7)
skin = Cell(50, 1)
# cancer.attack(skin)
