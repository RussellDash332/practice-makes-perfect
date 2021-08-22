# Feel free to use this to run the sample execution
class Place:
    pass

class Person:
    pass

class Impostor:
    pass

ravn = Impostor("Ravn", "Pistol")
brendan = Impostor("Brendan", "Knife")
daryl = Person("Daryl")
tze = Person("Tze Lynn")
ryan = Person("Ryan")
clifton = Person("Clifton")
daniel = Person("Daniel")
room = Place("classroom")
toilet = Place("toilet")
hall = Place("hall")

print(daniel.get_state())               # Alive
print(daniel.move(toilet))              # Daniel moves to toilet
print(daryl.move(room))                 # Daryl moves to classroom
print(tze.move(hall))                   # Tze Lynn moves to hall
print(ryan.move(toilet))                # Ryan moves to toilet
print(brendan.move(toilet))             # Brendan moves to toilet
print(ravn.move(room))                  # Ravn moves to classroom
print(clifton.move(room))               # Clifton moves to classroom
print(room.get_people())                # Daryl, Ravn, Clifton in classroom
print(ravn.kill(ravn))                  # Cannot kill himself
print(ravn.victim_list())               # Killed nobody
print(tze.do_task("wiring"))            # Tze Lynn does wiring
print(brendan.kill(clifton))            # Clifton is in classroom. Cannot kill
print(ravn.kill(clifton))               # Ravn killed Clifton with a Pistol
print(ravn.report(tze))                 # Tze Lynn is in hall
print(ryan.report(brendan))             # Brendan is still alive
print(daniel.move(room))                # Daniel moves from toilet to classroom
print(ravn.report(clifton))             # Ravn reports Clifton and suspects Daryl, Daniel
print(ravn.victim_list())               # Ravn killed Clifton
print(clifton.get_state())              # Killed by Ravn
print(brendan.kill(ryan))               # Brendan killed Ryan with a Knife
print(brendan.move(room))               # Brendan moves from toilet to classroom
print(brendan.kill(ravn))               # Cannot kill another impostor
print(brendan.do_task("swipe card"))    # Brendan does swipe card
print(tze.move(toilet))                 # Tze Lynn moves from hall to toilet
print(tze.report(ryan))                 # Tze Lynn reports Ryan and nobody to suspect
print(hall.get_people())                # Nobody here
print(room.get_people())                # Daryl, Ravn, Clifton, Daniel, Brendan in classroom
                                        # order does not matter here
print(brendan.kill(daniel))             # Brendan killed Daniel with a Knife
print(ravn.report(daniel))              # Ravn reports Daniel and suspects Daryl, Brendan
print(brendan.victim_list())            # Brendan killed Daniel, Ryan
                                        # must be in alphabetical order
print(brendan.kill(daniel))             # Already killed