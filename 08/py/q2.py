class Channel:
    pass

class User:
    pass

class Tutor:
    pass

class Student:
    pass

class Owner:
    pass

general = Channel("general-helpdesk", ["Owner", "Tutor", "Student"])
announcements = Channel("announcements", ["Owner", "Tutor"])
secret = Channel("foobar", ["Owner"])

print(general.get_name())               # #general-helpdesk
print(secret.get_name())                # #foobar

russell = Owner("Russell")
clifton = Tutor("Clifton")
aeron = Student("Aeron")
kenghwee = User("Keng Hwee")

def display_hall_of_mute():
    channels = [general, announcements, secret]
    print()
    print("HALL OF MUTE")
    for channel in channels:
        print(f"{channel.get_name()}: {channel.hall_of_mute()}")
    print()

print(russell.get_role())               # Russell is the owner!
print(clifton.get_role())               # Clifton is a Tutor
print(aeron.get_role())                 # Aeron is a Student
print(kenghwee.get_role())              # Keng Hwee has no role
print()
print(russell.join(general))            # Russell joins #general-helpdesk
print(russell.join(general))            # Russell has already joined #general-helpdesk
print(clifton.join(general))            # Clifton joins #general-helpdesk
print(russell.mute(aeron, None, None))  # Russell muted Aeron indefinitely. Reason: None
print(aeron.join(general))              # Aeron is muted!
                                        # therefore cannot join
print(russell.unmute(aeron))            # Russell unmuted Aeron!
print(aeron.join(general))              # Aeron joins #general-helpdesk
print(kenghwee.join(general))           # Keng Hwee has no permission to join #general-helpdesk
print(general.get_members())            # ['Aeron', 'Clifton', 'Russell']
print()
print(russell.join(announcements))      # Russell joins #announcements
print(clifton.join(announcements))      # Clifton joins #announcements
print(aeron.join(announcements))        # Aeron has no permission to join #announcements
print(kenghwee.join(announcements))     # Keng Hwee has no permission to join #announcements
print(announcements.get_members())      # ['Clifton', 'Russell']
print()
print(russell.join(secret))             # Russell joins #foobar
print(clifton.join(secret))             # Clifton has no permission to join #foobar
print(aeron.join(secret))               # Aeron has no permission to join #foobar
print(kenghwee.join(secret))            # Keng Hwee has no permission to join #foobar
print(secret.get_members())             # ['Russell']
print()
print(russell.get_channels())           # ['announcements', 'foobar', 'general-helpdesk']
print(clifton.get_channels())           # ['announcements', 'general-helpdesk']
print(aeron.get_channels())             # ['general-helpdesk']
print(kenghwee.get_channels())          # []
print()

print(russell.message(announcements, "Tutorial is canceled!"))          # #announcements --- Russell: Tutorial is canceled!
print(clifton.message(general, "Hooray!"))                              # #general-helpdesk --- Clifton: Hooray!
print(aeron.message(announcements, "Tutorial is canceled!"))            # Aeron has not joined #announcements
print(kenghwee.message(announcements, "Tutorial is canceled!"))         # Keng Hwee has not joined #announcements
print(russell.message(secret, "I am alone!"))                           # #foobar --- Russell: I am alone!
print(clifton.message(secret, "WHAT"))                                  # Clifton has not joined #foobar
print()

print(russell.mute(kenghwee, None, "Testing"))                          # Russell muted Keng Hwee indefinitely. Reason: Testing
print(clifton.mute(russell, 10, "Revenge"))                             # Cannot mute a fellow tutor
print(kenghwee.mute(russell, 100, "Revenge"))                           # Keng Hwee is not allowed to send messages!
                                                                        # because he's muted
print(kenghwee.message(announcements, "Tutorial is canceled!"))         # Keng Hwee has not joined #announcements
print(clifton.unmute(kenghwee))                                         # Clifton unmuted Keng Hwee!
print(kenghwee.mute(russell, 100, "Revenge"))                           # Keng Hwee doesn't have a permission to mute another user
print(aeron.mute(clifton, 3, None))                                     # Aeron doesn't have a permission to mute another user
print(clifton.mute(aeron, 5, "Why would you try to mute me?"))          # Clifton muted Aeron for 5 minutes. Reason: Why would you try to mute me?
print(kenghwee.mute(kenghwee, 10, "No idea"))                           # Cannot mute oneself
print(russell.mute(russell, 10, "Same here"))                           # Cannot mute oneself
print(russell.mute(aeron, 3, "Spam"))                                   # Aeron is muted!
display_hall_of_mute()
'''
HALL OF MUTE
#general-helpdesk: ['Aeron']
#announcements: []
#foobar: []
'''

print(aeron.message(secret, "Hello"))                                   # Aeron has not joined #foobar
print(aeron.message(general, "Yoooo"))                                  # Aeron is not allowed to send messages in #general-helpdesk
print(aeron.message(announcements, "Test"))                             # Aeron has not joined #announcements
print(clifton.mute(russell, None, None))                                # Cannot mute a fellow tutor
print(russell.mute(clifton, None, "Muting a fellow tutor is a can"))    # Russell muted Clifton indefinitely. Reason: Muting a fellow tutor is a can
display_hall_of_mute()
'''
HALL OF MUTE
#general-helpdesk: ['Aeron', 'Clifton']
#announcements: ['Clifton']
#foobar: []
'''

print(clifton.mute(aeron, 3, "Spam?"))      # Clifton is not allowed to send messages!
print(russell.unmute(clifton))              # Russell unmuted Clifton!
display_hall_of_mute()
'''
HALL OF MUTE
#general-helpdesk: ['Aeron']
#announcements: []
#foobar: []
'''

print(clifton.mute(aeron, 3, "Spam?"))      # Aeron is muted!
print(aeron.message(general, "Yoooo"))      # Aeron is not allowed to send messages in #general-helpdesk
                                            # since he's muted
print(aeron.mute(kenghwee, 2, "Lol"))       # Aeron is not allowed to send messages!
                                            # again, because he's still muted
print(aeron.unmute(kenghwee))               # Keng Hwee is not muted :)
print(clifton.unmute(aeron))                # Clifton unmuted Aeron!
display_hall_of_mute()
'''
HALL OF MUTE
#general-helpdesk: []
#announcements: []
#foobar: []
'''

print(kenghwee.mute(russell, 10, None))                     # Keng Hwee doesn't have a permission to mute another user
print(kenghwee.message(general, "Hi guys I'm unmuted"))     # Keng Hwee has not joined #general-helpdesk
print(russell.message(general, "Hello"))                    # #general-helpdesk --- Russell: Hello
print(clifton.message(general, "Hello!"))                   # #general-helpdesk --- Clifton: Hello!
print(aeron.message(general, "I'm so happy!"))              # #general-helpdesk --- Aeron: I'm so happy!
print(aeron.message(announcements, "Test"))                 # Aeron has not joined #announcements
print(kenghwee.join(general))                               # Keng Hwee has no permission to join #general-helpdesk
print(russell.unmute(kenghwee))                             # Keng Hwee is not muted :)
print(russell.unmute(russell))                              # Russell is not muted :)