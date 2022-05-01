#                                  Setup
# ______________________________________________________________________________


# Importing all the needed libraries
import pydub
from pydub import AudioSegment
import pygame
import time
import os
import sys
import pickle
from gpiozero import Button
from subprocess import call

pygame.mixer.init(frequency=48000, size=-16, channels=16, buffer=256)
pygame.mixer.set_num_channels(32)
pygame.init()


# functions
def Menu(men_running):
    global box_pos
    while men_running == True:
        clock.tick(30)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            Exit()
        if keys[pygame.K_UP] and not keys[pygame.K_a] or Up.is_pressed and not A.is_pressed:
            Men_Up_Pressed()
        if keys[pygame.K_DOWN] and not keys[pygame.K_a] or Down.is_pressed and not A.is_pressed:
            Men_Down_Pressed()
        if keys[pygame.K_g] or A.is_pressed:
            if box_pos[1] == 0:
                Seq(True)
                box_pos = [0, 0]
            if box_pos[1] == 2:
                Settings(True)
            if box_pos[1] == 1:
                box_pos = [0, 0]
                if Floppy(True) == True:
                    Seq(True)
            if box_pos[1] == 3:
                call("sudo shutdown -h now", shell=True)
        Vol_up()
        Vol_down()
        window.blit(men_background, [0, 0])
        window.blit(men_box, (men_pos_x[box_pos[0]], men_pos_y[box_pos[1]]))
        pygame.display.flip()
        pygame.event.pump()


def Seq(seq_running):
    global box_pos
    while seq_running:
        clock.tick(30)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or Up.is_pressed:
            if keys[pygame.K_UP] and keys[pygame.K_a] or Up.is_pressed and A.is_pressed:
                Seq_Choice_Up()
            else:
                Seq_Up_Pressed()
        if keys[pygame.K_DOWN] or Down.is_pressed:
            if keys[pygame.K_DOWN] and keys[pygame.K_a] or Down.is_pressed and A.is_pressed:
                Seq_Choice_Down()
            else:
                Seq_Down_Pressed()
        if keys[pygame.K_a] and keys[pygame.K_b] and keys[
            pygame.K_LEFT] or A.is_pressed and B.is_pressed and Left.is_pressed:
            Carry_Left()
        if keys[pygame.K_a] and keys[pygame.K_b] and keys[
            pygame.K_RIGHT] or A.is_pressed and B.is_pressed and Right.is_pressed:
            Carry_Right()
        if keys[pygame.K_a] and keys[pygame.K_s] or A.is_pressed and Select.is_pressed:
            Empty_Note()
        if keys[pygame.K_LEFT] and not keys[pygame.K_b] or Left.is_pressed and not B.is_pressed:
            if Seq_Left_Pressed() == 0:
                if box_pos[0] > 7:
                    window.blit(seq_box_2, (seq_pos_x[box_pos[0]], seq_pos_y[box_pos[1]]))
                else:
                    window.blit(seq_box, (seq_pos_x[box_pos[0]], seq_pos_y[box_pos[1]]))
                Seq_Text()
                pygame.display.flip()
                time.sleep(0.1)
        if keys[pygame.K_RIGHT] and not keys[pygame.K_b] or Right.is_pressed and not B.is_pressed:
            Seq_Right_Pressed()
        if keys[pygame.K_b] and not keys[pygame.K_a] or B.is_pressed and not A.is_pressed:
            box_pos = [0, 0]
            seq_running = False
        if keys[pygame.K_p] or Start.is_pressed:
            Play_Sequence(True)
        if keys[pygame.K_t] or Select.is_pressed:
            Try_Sound()
        if box_pos[0] > 7:
            window.blit(seq_background_2, [0, 0])
        else:
            window.blit(seq_background_1, [0, 0])
        window.blit(seq_box, (seq_pos_x[box_pos[0]], seq_pos_y[box_pos[1]]))
        Seq_Text()
        pygame.display.flip()
        pygame.event.pump()


def Settings(set_running):
    global box_pos
    while set_running:
        clock.tick(30)
        window.blit(set_background, [0, 0])
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or Up.is_pressed:
            if keys[pygame.K_UP] and keys[pygame.K_a] or Up.is_pressed and A.is_pressed:
                Set_Choice_Up(False)
            else:
                Set_Up_Pressed()
        if keys[pygame.K_DOWN] or Down.is_pressed:
            if keys[pygame.K_DOWN] and keys[pygame.K_a] or Down.is_pressed and A.is_pressed:
                Set_Choice_Down(False)
            else:
                Set_Down_Pressed()
        if keys[pygame.K_LEFT] and keys[pygame.K_a] or Left.is_pressed and A.is_pressed:
            Set_Choice_Down(True)
        if keys[pygame.K_RIGHT] and keys[pygame.K_a] or Right.is_pressed and A.is_pressed:
            Set_Choice_Up(True)
        if keys[pygame.K_b] or B.is_pressed:
            box_pos = [0, 0]
            set_running = False
        window.blit(set_box, (set_pos_x[box_pos[0]], set_pos_y[box_pos[1]]))
        Set_Text()
        pygame.display.flip()
        pygame.event.pump()


def Floppy(floppy_running):
    global box_pos
    open_seq = False
    while floppy_running:
        clock.tick(30)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] or A.is_pressed and Start.is_pressed:
            Save_Seq()
            time.sleep(0.2)
        if keys[pygame.K_w]:
            Save_Song(True)
        if keys[pygame.K_l] or A.is_pressed and Select.is_pressed:
            Load_Seq()
            open_seq = True
            box_pos = [0, 0]
            floppy_running = False
        if keys[pygame.K_t] or Select.is_pressed:
            Floppy_Play(0, False, True)
        if keys[pygame.K_UP] or Up.is_pressed:
            Floppy_Up()
        if keys[pygame.K_p] or Start.is_pressed:
            Run_All_Saves(True)
        if keys[pygame.K_DOWN] or Down.is_pressed:
            Floppy_Down()
        if keys[pygame.K_LEFT] or Left.is_pressed:
            Floppy_Left()
        if keys[pygame.K_RIGHT] or Right.is_pressed:
            Floppy_Right()
        if keys[pygame.K_b] or B.is_pressed:
            box_pos = [0, 0]
            floppy_running = False
        window.blit(floppy_background, [0, 0])
        window.blit(floppy_box, (floppy_pos_x[box_pos[0]], floppy_pos_y[box_pos[1]]))
        Floppy_Text()
        pygame.display.flip()
        pygame.event.pump()
    return open_seq


def Exit():
    sys.exit()


def Play_Sequence(player_running):
    i = 0
    first_run = True
    while player_running:
        if set_list[4] == True:
            if set_list[3] > 8:
                loops = 8
            else:
                loops = set_list[3]
        else:
            loops = set_list[3]
        if ((AllSteps_Main[i])[0]) == 0:
            Banks = Banks_D
        if ((AllSteps_Main[i])[0]) == 1:
            Banks = Banks_K
        if ((AllSteps_Main[i])[0]) == 2:
            Banks = Banks_S
        if ((AllSteps_Main[i])[0]) == 3:
            Banks = Banks_F
        Type = Types[(AllSteps_Main[i])[0]]
        Bank = Banks[(AllSteps_Main[i])[1]]
        Oct = Octs[(AllSteps_Main[i])[2]]
        Note1 = Notes[(AllSteps_Main[i])[3]]
        Note2 = Notes[(AllSteps_Main[i])[4]]
        Note3 = Notes[(AllSteps_Main[i])[5]]
        if Note1 == "_":
            sound1 = pygame.mixer.Sound(empty_sound)
        else:
            sound1 = pygame.mixer.Sound(sound_loc.format(Type, Bank, Oct, Note1))
        if Note2 == "_":
            sound2 = pygame.mixer.Sound(empty_sound)
        else:
            sound2 = pygame.mixer.Sound(sound_loc.format(Type, Bank, Oct, Note2))
        if Note3 == "_":
            sound3 = pygame.mixer.Sound(empty_sound)
        else:
            sound3 = pygame.mixer.Sound(sound_loc.format(Type, Bank, Oct, Note3))
        if set_list[4] == True:
            if ((AllSteps_Main[i + 8])[0]) == 0:
                Banks = Banks_D
            if ((AllSteps_Main[i + 8])[0]) == 1:
                Banks = Banks_K
            if ((AllSteps_Main[i + 8])[0]) == 2:
                Banks = Banks_S
            if ((AllSteps_Main[i + 8])[0]) == 3:
                Banks = Banks_F
            Type2 = Types[(AllSteps_Main[i + 8])[0]]
            Bank2 = Banks[(AllSteps_Main[i + 8])[1]]
            Oct2 = Octs[(AllSteps_Main[i + 8])[2]]
            Note4 = Notes[(AllSteps_Main[i + 8])[3]]
            Note5 = Notes[(AllSteps_Main[i + 8])[4]]
            Note6 = Notes[(AllSteps_Main[i + 8])[5]]
            if Note4 == "_":
                sound4 = pygame.mixer.Sound(empty_sound)
            else:
                sound4 = pygame.mixer.Sound(sound_loc.format(Type2, Bank2, Oct2, Note4))
            if Note5 == "_":
                sound5 = pygame.mixer.Sound(empty_sound)
            else:
                sound5 = pygame.mixer.Sound(sound_loc.format(Type2, Bank2, Oct2, Note5))
            if Note6 == "_":
                sound6 = pygame.mixer.Sound(empty_sound)
            else:
                sound6 = pygame.mixer.Sound(sound_loc.format(Type2, Bank2, Oct2, Note6))
        if set_list[4] == False:
            sound4 = sound5 = sound6 = pygame.mixer.Sound(empty_sound)
        Play_sound(sound1, sound2, sound3, sound4, sound5, sound6)
        i += 1
        keys = pygame.key.get_pressed()
        if i == loops:
            i = 0
        if keys[pygame.K_p] or Start.is_pressed:
            if first_run == True:
                first_run = False
            else:
                player_running = False
                time.sleep(1)
        pygame.event.pump()
        if i > 7:
            window.blit(seq_background_2, [0, 0])
        else:
            window.blit(seq_background_1, [0, 0])
        window.blit(seq_box, (seq_pos_x[i], seq_pos_y[0]))
        window.blit(seq_box, (seq_pos_x[i], seq_pos_y[1]))
        window.blit(seq_box, (seq_pos_x[i], seq_pos_y[2]))
        window.blit(seq_box, (seq_pos_x[i], seq_pos_y[3]))
        window.blit(seq_box, (seq_pos_x[i], seq_pos_y[4]))
        window.blit(seq_box, (seq_pos_x[i], seq_pos_y[5]))
        Seq_Text()
        pygame.display.flip()


def Play_sound(sound1, sound2, sound3, sound4, sound5, sound6):
    vol = pickle.load(open("vol", 'rb'))
    if set_list[4] == False:
        sound1.set_volume(vol)
        sound2.set_volume(vol)
        sound3.set_volume(vol)
        sound1.play(fade_ms=set_list[1])
        sound2.play(fade_ms=set_list[1])
        sound3.play(fade_ms=set_list[1])
        time.sleep((60 / (set_list[0] * 2)))
        sound1.fadeout(set_list[2])
        sound2.fadeout(set_list[2])
        sound3.fadeout(set_list[2])
    else:
        sound1.set_volume(vol)
        sound2.set_volume(vol)
        sound3.set_volume(vol)
        sound4.set_volume(vol)
        sound5.set_volume(vol)
        sound6.set_volume(vol)
        sound1.play(fade_ms=set_list[1])
        sound2.play(fade_ms=set_list[1])
        sound3.play(fade_ms=set_list[1])
        time.sleep((60 / (set_list[0] * 2) * (set_list[5] / 100)))
        sound4.play(fade_ms=set_list[1])
        sound5.play(fade_ms=set_list[1])
        sound6.play(fade_ms=set_list[1])
        time.sleep((60 / (set_list[0] * 2)) - (60 / (set_list[0] * 2) * (set_list[5] / 100)))
        sound1.fadeout(set_list[2])
        sound2.fadeout(set_list[2])
        sound3.fadeout(set_list[2])
        sound4.fadeout(set_list[2])
        sound5.fadeout(set_list[2])
        sound6.fadeout(set_list[2])


def Try_Sound():
    if ((AllSteps_Main[box_pos[0]])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[box_pos[0]])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[box_pos[0]])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[box_pos[0]])[0]) == 3:
        Banks = Banks_F
    Type = Types[(AllSteps_Main[box_pos[0]])[0]]
    Bank = Banks[(AllSteps_Main[box_pos[0]])[1]]
    Oct = Octs[(AllSteps_Main[box_pos[0]])[2]]
    Note1 = Notes[(AllSteps_Main[box_pos[0]])[3]]
    Note2 = Notes[(AllSteps_Main[box_pos[0]])[4]]
    Note3 = Notes[(AllSteps_Main[box_pos[0]])[5]]
    if Note1 == "_":
        sound1 = pygame.mixer.Sound(empty_sound)
    else:
        sound1 = pygame.mixer.Sound(sound_loc.format(Type, Bank, Oct, Note1))
    if Note2 == "_":
        sound2 = pygame.mixer.Sound(empty_sound)
    else:
        sound2 = pygame.mixer.Sound(sound_loc.format(Type, Bank, Oct, Note2))
    if Note3 == "_":
        sound3 = pygame.mixer.Sound(empty_sound)
    else:
        sound3 = pygame.mixer.Sound(sound_loc.format(Type, Bank, Oct, Note3))
    if set_list[4] == True:
        if box_pos[0] >= 8:
            layer = -8
        else:
            layer = 8
        if ((AllSteps_Main[box_pos[0] + layer])[0]) == 0:
            Banks = Banks_D
        if ((AllSteps_Main[box_pos[0] + layer])[0]) == 1:
            Banks = Banks_K
        if ((AllSteps_Main[box_pos[0] + layer])[0]) == 2:
            Banks = Banks_S
        if ((AllSteps_Main[box_pos[0] + layer])[0]) == 3:
            Banks = Banks_F
        Type2 = Types[(AllSteps_Main[box_pos[0] + layer])[0]]
        Bank2 = Banks[(AllSteps_Main[box_pos[0] + layer])[1]]
        Oct2 = Octs[(AllSteps_Main[box_pos[0] + layer])[2]]
        Note4 = Notes[(AllSteps_Main[box_pos[0] + layer])[3]]
        Note5 = Notes[(AllSteps_Main[box_pos[0] + layer])[4]]
        Note6 = Notes[(AllSteps_Main[box_pos[0] + layer])[5]]
        if Note4 == "_":
            sound4 = pygame.mixer.Sound(empty_sound)
        else:
            sound4 = pygame.mixer.Sound(sound_loc.format(Type2, Bank2, Oct2, Note4))
        if Note5 == "_":
            sound5 = pygame.mixer.Sound(empty_sound)
        else:
            sound5 = pygame.mixer.Sound(sound_loc.format(Type2, Bank2, Oct2, Note5))
        if Note6 == "_":
            sound6 = pygame.mixer.Sound(empty_sound)
        else:
            sound6 = pygame.mixer.Sound(sound_loc.format(Type2, Bank2, Oct2, Note6))
    else:
        sound4 = sound5 = sound6 = pygame.mixer.Sound(empty_sound)
    Play_sound(sound1, sound2, sound3, sound4, sound5, sound6)


def Seq_Text():
    window.blit(Boxes[0][0], (0 + seq_x_offset, seq_pos_y[0] + seq_y_offset))
    window.blit(Boxes[1][0], (0 + seq_x_offset, seq_pos_y[1] + seq_y_offset))
    window.blit(Boxes[2][0], (0 + seq_x_offset, seq_pos_y[2] + seq_y_offset))
    window.blit(Boxes[3][0], (0 + seq_x_offset, seq_pos_y[3] + seq_y_offset))
    window.blit(Boxes[4][0], (0 + seq_x_offset, seq_pos_y[4] + seq_y_offset))
    window.blit(Boxes[5][0], (0 + seq_x_offset, seq_pos_y[5] + seq_y_offset))
    if box_pos[0] < 8:
        i = 0
        while (i + 1) < (len(Boxes[0]) - 8):
            window.blit(Boxes[0][i + 1], (seq_pos_x[i] + seq_x_offset, seq_pos_y[0] + seq_y_offset))
            i += 1
        i = 0
        while (i + 1) < (len(Boxes[1]) - 8):
            window.blit(Boxes[1][i + 1], (seq_pos_x[i] + seq_x_offset, seq_pos_y[1] + seq_y_offset))
            i += 1
        i = 0
        while (i + 1) < (len(Boxes[2]) - 8):
            window.blit(Boxes[2][i + 1], (seq_pos_x[i] + seq_x_offset, seq_pos_y[2] + seq_y_offset))
            i += 1
        i = 0
        while (i + 1) < (len(Boxes[3]) - 8):
            window.blit(Boxes[3][i + 1], (seq_pos_x[i] + seq_x_offset, seq_pos_y[3] + seq_y_offset))
            i += 1
        i = 0
        while (i + 1) < (len(Boxes[4]) - 8):
            window.blit(Boxes[4][i + 1], (seq_pos_x[i] + seq_x_offset, seq_pos_y[4] + seq_y_offset))
            i += 1
        i = 0
        while (i + 1) < (len(Boxes[5]) - 8):
            window.blit(Boxes[5][i + 1], (seq_pos_x[i] + seq_x_offset, seq_pos_y[5] + seq_y_offset))
            i += 1
    else:
        i = 8
        while (i + 1) < len(Boxes[0]):
            window.blit(Boxes[0][i + 1], (seq_pos_x[i] + seq_x_offset, seq_pos_y[0] + seq_y_offset))
            i += 1
        i = 8
        while (i + 1) < len(Boxes[1]):
            window.blit(Boxes[1][i + 1], (seq_pos_x[i] + seq_x_offset, seq_pos_y[1] + seq_y_offset))
            i += 1
        i = 8
        while (i + 1) < len(Boxes[2]):
            window.blit(Boxes[2][i + 1], (seq_pos_x[i] + seq_x_offset, seq_pos_y[2] + seq_y_offset))
            i += 1
        i = 8
        while (i + 1) < len(Boxes[3]):
            window.blit(Boxes[3][i + 1], (seq_pos_x[i] + seq_x_offset, seq_pos_y[3] + seq_y_offset))
            i += 1
        i = 8
        while (i + 1) < len(Boxes[4]):
            window.blit(Boxes[4][i + 1], (seq_pos_x[i] + seq_x_offset, seq_pos_y[4] + seq_y_offset))
            i += 1
        i = 8
        while (i + 1) < len(Boxes[5]):
            window.blit(Boxes[5][i + 1], (seq_pos_x[i] + seq_x_offset, seq_pos_y[5] + seq_y_offset))
            i += 1


def Set_Text():
    Set_1_1 = font1.render("BPM", True, (0, 0, 0))
    Set_1_2 = font1.render("Fadein Time", True, (0, 0, 0))
    Set_1_3 = font1.render("Fadeout Time", True, (0, 0, 0))
    Set_1_4 = font1.render("Steps", True, (0, 0, 0))
    Set_1_5 = font1.render("Two Simultanious Tracks", True, (0, 0, 0))
    Set_1_6 = font1.render("Track Offset", True, (0, 0, 0))
    window.blit(Set_1_1, (3 + set_x_offset, set_pos_y[0] + set_y_offset))
    window.blit(Set_1_2, (3 + set_x_offset, set_pos_y[1] + set_y_offset))
    window.blit(Set_1_3, (3 + set_x_offset, set_pos_y[2] + set_y_offset))
    window.blit(Set_1_4, (3 + set_x_offset, set_pos_y[3] + set_y_offset))
    window.blit(Set_1_5, (3 + set_x_offset, set_pos_y[4] + set_y_offset))
    if set_list[4] == True:
        window.blit(Set_1_6, (3 + set_x_offset, set_pos_y[5] + set_y_offset))

    Set_2_1 = font1.render("{}".format(set_list[0]), True, (0, 0, 0))
    window.blit(Set_2_1, (set_pos_x[1] + set_x_offset, set_pos_y[0] + set_y_offset))
    Set_2_2 = font1.render("{}s".format(set_list[1] / 1000), True, (0, 0, 0))
    window.blit(Set_2_2, (set_pos_x[1] + set_x_offset, set_pos_y[1] + set_y_offset))
    Set_2_3 = font1.render("{}s".format(set_list[2] / 1000), True, (0, 0, 0))
    window.blit(Set_2_3, (set_pos_x[1] + set_x_offset, set_pos_y[2] + set_y_offset))
    Set_2_4 = font1.render("{}".format(set_list[3]), True, (0, 0, 0))
    window.blit(Set_2_4, (set_pos_x[1] + set_x_offset, set_pos_y[3] + set_y_offset))
    if set_list[4] == True:
        Set_2_5 = font1.render("ON", True, (0, 0, 0))
        Set_2_6 = font1.render("{}%".format(set_list[5]), True, (0, 0, 0))
        window.blit(Set_2_6, (set_pos_x[1] + set_x_offset, set_pos_y[5] + set_y_offset))
    else:
        Set_2_5 = font1.render("OFF", True, (0, 0, 0))
    window.blit(Set_2_5, (set_pos_x[1] + set_x_offset, set_pos_y[4] + set_y_offset))


def Floppy_Text():
    for i in range(4):
        for u in range(3):
            if u == 0:
                window.blit(Floppy_numbers[i], (floppy_pos_x[i] + floppy_x_offset, floppy_pos_y[u] + floppy_y_offset))
            if u == 1:
                window.blit(Floppy_numbers[i+4], (floppy_pos_x[i] + floppy_x_offset, floppy_pos_y[u] + floppy_y_offset))
            if u == 2:
                window.blit(Floppy_numbers[i+8], (floppy_pos_x[i] + floppy_x_offset, floppy_pos_y[u] + floppy_y_offset))
    

def Seq_Up_Pressed():
    if box_pos[1] != 0:
        box_pos[1] = box_pos[1] - 1
        time.sleep(0.2)


def Seq_Down_Pressed():
    if box_pos[1] != 5:
        box_pos[1] = box_pos[1] + 1
        time.sleep(0.2)


def Seq_Left_Pressed():
    if box_pos[0] != 0:
        box_pos[0] = box_pos[0] - 1
    else:
        box_pos[0] = 15
    time.sleep(0.2)


def Seq_Right_Pressed():
    if box_pos[0] != 15:
        box_pos[0] = box_pos[0] + 1
    else:
        box_pos[0] = 0
    time.sleep(0.2)


def Set_Up_Pressed():
    if box_pos[1] != 0:
        box_pos[1] = box_pos[1] - 1
        time.sleep(0.2)


def Set_Down_Pressed():
    if set_list[4] == False:
        if box_pos[1] != 4:
            box_pos[1] = box_pos[1] + 1
            time.sleep(0.2)
    else:
        if box_pos[1] != 5:
            box_pos[1] = box_pos[1] + 1
            time.sleep(0.2)


def Men_Up_Pressed():
    if box_pos[1] != 0:
        box_pos[1] = box_pos[1] - 1
    else:  
        box_pos[1] = 3
    time.sleep(0.2)


def Men_Down_Pressed():
    if box_pos[1] != 3:
        box_pos[1] = box_pos[1] + 1
    else: 
        box_pos[1] = 0
    time.sleep(0.2)


def Men_Left_Pressed():
    if box_pos[0] != 0:
        box_pos[0] = box_pos[0] - 1
        time.sleep(0.2)


def Men_Right_Pressed():
    if box_pos[0] != 3:
        box_pos[0] = box_pos[0] + 1
        time.sleep(0.2)


def Floppy_Up():
    if box_pos[1] == 0:
        Export()
    if box_pos[1] != 0:
        box_pos[1] = box_pos[1] - 1
        time.sleep(0.2)
        

def Floppy_Down():
    if box_pos[1] != 2:
        box_pos[1] = box_pos[1] + 1
        time.sleep(0.2)


def Floppy_Left():
    if box_pos[0] != 0:
        box_pos[0] = box_pos[0] - 1
        time.sleep(0.2)
    else:
        if box_pos[1] != 0:
            box_pos[0] = 3
            Floppy_Up()


def Floppy_Right():
    if box_pos[0] != 3:
        box_pos[0] = box_pos[0] + 1
        time.sleep(0.2)
    else:
        if box_pos[1] != 2:
            box_pos[0] = 0
            Floppy_Down()

def Export():
    saved = False
    export = True
    while export == True:
        keys = pygame.key.get_pressed()
        if saved == False:
            if keys[pygame.K_a]or A.is_pressed:
                Save_Song(True)
                saved = True
                time.sleep(0.2)
        if keys[pygame.K_DOWN]or Down.is_pressed:
            export = False
            time.sleep(0.2)
        window.blit(floppy_background, [0, 0])
        window.blit(export_box, ( export_box_pos_x, export_box_pos_y))
        Floppy_Text()
        pygame.display.flip()
        pygame.event.pump()

def Seq_Choice_Up():
    if box_pos[1] == 0:
        if (AllSteps_Main[box_pos[0]])[0] == (len(Types) - 1):
            (AllSteps_Main[box_pos[0]])[0] = 0
        else:
            (AllSteps_Main[box_pos[0]])[0] += 1
        Boxes[box_pos[1]][box_pos[0] + 1] = font1.render(Types[(AllSteps_Main[box_pos[0]])[box_pos[1]]], True,
                                                         (0, 0, 0))
        if ((AllSteps_Main[box_pos[0]])[0]) == 0:
            Banks = Banks_D
        if ((AllSteps_Main[box_pos[0]])[0]) == 1:
            Banks = Banks_K
        if ((AllSteps_Main[box_pos[0]])[0]) == 2:
            Banks = Banks_S
        if ((AllSteps_Main[box_pos[0]])[0]) == 3:
            Banks = Banks_F
        (AllSteps_Main[box_pos[0]])[1] = 0
        Boxes[box_pos[1] + 1][box_pos[0] + 1] = font1.render(Banks[(AllSteps_Main[box_pos[0]])[box_pos[1] + 1]], True,
                                                             (0, 0, 0))
    if ((AllSteps_Main[box_pos[0]])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[box_pos[0]])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[box_pos[0]])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[box_pos[0]])[0]) == 3:
        Banks = Banks_F
    if box_pos[1] == 1:
        if (AllSteps_Main[box_pos[0]])[1] >= (len(Banks) - 1):
            (AllSteps_Main[box_pos[0]])[1] = 0
        else:
            (AllSteps_Main[box_pos[0]])[1] += 1
        Boxes[box_pos[1]][box_pos[0] + 1] = font1.render(Banks[(AllSteps_Main[box_pos[0]])[box_pos[1]]], True,
                                                         (0, 0, 0))
    if box_pos[1] == 2:
        if (AllSteps_Main[box_pos[0]])[2] == (len(Octs) - 1):
            (AllSteps_Main[box_pos[0]])[2] = 0
        else:
            (AllSteps_Main[box_pos[0]])[2] += 1
        Boxes[box_pos[1]][box_pos[0] + 1] = font1.render(Octs[(AllSteps_Main[box_pos[0]])[box_pos[1]]], True, (0, 0, 0))
    if box_pos[1] == 3:
        if (AllSteps_Main[box_pos[0]])[3] == (len(Notes) - 1):
            (AllSteps_Main[box_pos[0]])[3] = 0
        else:
            (AllSteps_Main[box_pos[0]])[3] += 1
        Boxes[box_pos[1]][box_pos[0] + 1] = font1.render(Notes[(AllSteps_Main[box_pos[0]])[box_pos[1]]], True,
                                                         (0, 0, 0))
    if box_pos[1] == 4:
        if (AllSteps_Main[box_pos[0]])[4] == (len(Notes) - 1):
            (AllSteps_Main[box_pos[0]])[4] = 0
        else:
            (AllSteps_Main[box_pos[0]])[4] += 1
        Boxes[box_pos[1]][box_pos[0] + 1] = font1.render(Notes[(AllSteps_Main[box_pos[0]])[box_pos[1]]], True,
                                                         (0, 0, 0))
    if box_pos[1] == 5:
        if (AllSteps_Main[box_pos[0]])[5] == (len(Notes) - 1):
            (AllSteps_Main[box_pos[0]])[5] = 0
        else:
            (AllSteps_Main[box_pos[0]])[5] += 1
        Boxes[box_pos[1]][box_pos[0] + 1] = font1.render(Notes[(AllSteps_Main[box_pos[0]])[box_pos[1]]], True,
                                                         (0, 0, 0))
    time.sleep(0.2)
    Seq_Text()


def Seq_Choice_Down():
    if box_pos[1] == 0:
        if (AllSteps_Main[box_pos[0]])[0] == 0:
            (AllSteps_Main[box_pos[0]])[0] = (len(Types) - 1)
        else:
            (AllSteps_Main[box_pos[0]])[0] -= 1
        Boxes[box_pos[1]][box_pos[0] + 1] = font1.render(Types[(AllSteps_Main[box_pos[0]])[box_pos[1]]], True,
                                                         (0, 0, 0))
        if ((AllSteps_Main[box_pos[0]])[0]) == 0:
            Banks = Banks_D
        if ((AllSteps_Main[box_pos[0]])[0]) == 1:
            Banks = Banks_K
        if ((AllSteps_Main[box_pos[0]])[0]) == 2:
            Banks = Banks_S
        if ((AllSteps_Main[box_pos[0]])[0]) == 3:
            Banks = Banks_F
        (AllSteps_Main[box_pos[0]])[1] = 0
        Boxes[box_pos[1] + 1][box_pos[0] + 1] = font1.render(Banks[(AllSteps_Main[box_pos[0]])[box_pos[1] + 1]], True,
                                                             (0, 0, 0))
    if ((AllSteps_Main[box_pos[0]])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[box_pos[0]])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[box_pos[0]])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[box_pos[0]])[0]) == 3:
        Banks = Banks_F
    if box_pos[1] == 1:
        if (AllSteps_Main[box_pos[0]])[1] == 0:
            (AllSteps_Main[box_pos[0]])[1] = (len(Banks) - 1)
        else:
            (AllSteps_Main[box_pos[0]])[1] -= 1
        Boxes[box_pos[1]][box_pos[0] + 1] = font1.render(Banks[(AllSteps_Main[box_pos[0]])[box_pos[1]]], True,
                                                         (0, 0, 0))
    if box_pos[1] == 2:
        if (AllSteps_Main[box_pos[0]])[2] == 0:
            (AllSteps_Main[box_pos[0]])[2] = (len(Octs) - 1)
        else:
            (AllSteps_Main[box_pos[0]])[2] -= 1
        Boxes[box_pos[1]][box_pos[0] + 1] = font1.render(Octs[(AllSteps_Main[box_pos[0]])[box_pos[1]]], True, (0, 0, 0))
    if box_pos[1] == 3:
        if (AllSteps_Main[box_pos[0]])[3] == 0:
            (AllSteps_Main[box_pos[0]])[3] = (len(Notes) - 1)
        else:
            (AllSteps_Main[box_pos[0]])[3] -= 1
        Boxes[box_pos[1]][box_pos[0] + 1] = font1.render(Notes[(AllSteps_Main[box_pos[0]])[box_pos[1]]], True,
                                                         (0, 0, 0))
    if box_pos[1] == 4:
        if (AllSteps_Main[box_pos[0]])[4] == 0:
            (AllSteps_Main[box_pos[0]])[4] = (len(Notes) - 1)
        else:
            (AllSteps_Main[box_pos[0]])[4] -= 1
        Boxes[box_pos[1]][box_pos[0] + 1] = font1.render(Notes[(AllSteps_Main[box_pos[0]])[box_pos[1]]], True,
                                                         (0, 0, 0))
    if box_pos[1] == 5:
        if (AllSteps_Main[box_pos[0]])[5] == 0:
            (AllSteps_Main[box_pos[0]])[5] = (len(Notes) - 1)
        else:
            (AllSteps_Main[box_pos[0]])[5] -= 1
        Boxes[box_pos[1]][box_pos[0] + 1] = font1.render(Notes[(AllSteps_Main[box_pos[0]])[box_pos[1]]], True,
                                                         (0, 0, 0))
    time.sleep(0.2)


def Set_Choice_Up(Fast):
    global set_list
    if box_pos[1] == 0:
        if Fast == True:
            set_list[0] += 10
            time.sleep(0.15)
        else:
            set_list[0] += 1
            time.sleep(0.1)
        if set_list[0] >= max_bpm:
            set_list[0] = 15
    if box_pos[1] == 1:
        if Fast == True:
            set_list[1] += 100
            time.sleep(0.15)
        else:
            set_list[1] += 10
            time.sleep(0.1)
        if set_list[1] >= max_fade:
            set_list[1] = 0
    if box_pos[1] == 2:
        if Fast == True:
            set_list[2] += 100
            time.sleep(0.15)
        else:
            set_list[2] += 10
            time.sleep(0.1)
        if set_list[2] >= max_fade:
            set_list[2] = 0
    if box_pos[1] == 3:
        if set_list[3] >= max_steps:
            set_list[3] = 1
        else:
            set_list[3] += 1
        time.sleep(0.2)
    if box_pos[1] == 4:
        if set_list[4] == True:
            set_list[4] = False
        else:
            set_list[4] = True
        time.sleep(0.3)
    if box_pos[1] == 5:
        if Fast == True:
            set_list[5] += 10
            time.sleep(0.15)
        else:
            set_list[5] += 1
            time.sleep(0.1)
        if set_list[5] >= max_offset:
            set_list[5] = 0


def Set_Choice_Down(Fast):
    global set_list
    if box_pos[1] == 0:
        if Fast == True:
            set_list[0] -= 10
            time.sleep(0.15)
        else:
            set_list[0] -= 1
            time.sleep(0.1)
        if set_list[0] < 15:
            set_list[0] = max_bpm
    if box_pos[1] == 1:
        if set_list[1] < 0:
            set_list[1] = max_fade
        if Fast == True:
            set_list[1] -= 100
            time.sleep(0.15)
        else:
            set_list[1] -= 10
            time.sleep(0.1)
        if set_list[1] <= 0:
            set_list[1] = max_fade
    if box_pos[1] == 2:
        if Fast == True:
            set_list[2] -= 100
            time.sleep(0.15)
        else:
            set_list[2] -= 10
            time.sleep(0.1)
        if set_list[2] <= 0:
            set_list[2] = max_fade
    if box_pos[1] == 3:
        if set_list[3] <= 1:
            set_list[3] = max_steps
        else:
            set_list[3] -= 1
        time.sleep(0.2)
    if box_pos[1] == 4:
        if set_list[4] == True:
            set_list[4] = False
        else:
            set_list[4] = True
        time.sleep(0.3)
    if box_pos[1] == 5:
        if Fast == True:
            set_list[5] -= 10
            time.sleep(0.15)
        else:
            set_list[5] -= 1
            time.sleep(0.1)
        if set_list[5] <= 0:
            set_list[5] = max_offset


def Empty_Note():
    if box_pos[1] == 3:
        (AllSteps_Main[box_pos[0]])[3] = 0
        Boxes[box_pos[1]][box_pos[0] + 1] = font1.render(Notes[(AllSteps_Main[box_pos[0]])[box_pos[1]]], True,
                                                         (0, 0, 0))
    if box_pos[1] == 4:
        (AllSteps_Main[box_pos[0]])[4] = 0
        Boxes[box_pos[1]][box_pos[0] + 1] = font1.render(Notes[(AllSteps_Main[box_pos[0]])[box_pos[1]]], True,
                                                         (0, 0, 0))
    if box_pos[1] == 5:
        (AllSteps_Main[box_pos[0]])[5] = 0
        Boxes[box_pos[1]][box_pos[0] + 1] = font1.render(Notes[(AllSteps_Main[box_pos[0]])[box_pos[1]]], True,
                                                         (0, 0, 0))
    time.sleep(0.2)


def Save_Seq():
    a_not_pressed = True
    not_confirmed = True
    time.sleep(0.5)
    while not_confirmed == True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or A.is_pressed and a_not_pressed != True:
            not_confirmed = False
            confirm = True
            time.sleep(0.2)
        if a_not_pressed == True:
            a_not_pressed = False
        if keys[pygame.K_b] or B.is_pressed:    
            not_confirmed = False
            confirm  = False
        window.blit(conf_window, (conf_win_pos_x, conf_win_pos_y))
        pygame.display.flip()
        pygame.event.pump()
    
    if confirm == True:
        if box_pos[1] == 0:
            pickle.dump(AllSteps_Main, open("{}/{}".format(saves_loc, box_pos[0]), 'wb'))
            pickle.dump(set_list, open("{}/s{}".format(saves_loc, box_pos[0]), 'wb'))
            time.sleep(0.2)
        if box_pos[1] == 1:
            pickle.dump(AllSteps_Main, open("{}/{}".format(saves_loc, box_pos[0] + 4), 'wb'))
            pickle.dump(set_list, open("{}/s{}".format(saves_loc, box_pos[0] + 4), 'wb'))
            time.sleep(0.2)
        if box_pos[1] == 2:
            pickle.dump(AllSteps_Main, open("{}/{}".format(saves_loc, box_pos[0] + 8), 'wb'))
            pickle.dump(set_list, open("{}/s{}".format(saves_loc, box_pos[0] + 8), 'wb'))
            time.sleep(0.2)


def Load_Seq():
    global AllSteps_Main, Boxes, set_list
    if box_pos[1] == 0:
        AllSteps_Main = pickle.load(open("{}/{}".format(saves_loc, box_pos[0]), 'rb'))
        set_list = pickle.load(open("{}/s{}".format(saves_loc, box_pos[0]), 'rb'))
    if box_pos[1] == 1:
        AllSteps_Main = pickle.load(open("{}/{}".format(saves_loc, box_pos[0] + 4), 'rb'))
        set_list = pickle.load(open("{}/s{}".format(saves_loc, box_pos[0] + 4), 'rb'))
    if box_pos[1] == 2:
        AllSteps_Main = pickle.load(open("{}/{}".format(saves_loc, box_pos[0] + 8), 'rb'))
        set_list = pickle.load(open("{}/s{}".format(saves_loc, box_pos[0] + 8), 'rb'))
    Boxes = Creat_Boxes()
    time.sleep(0.2)


def Floppy_Play(Floppy_Pos, run_saves, running):
    vol = pickle.load(open("vol", 'rb'))
    Break_play = False
    if run_saves == False:
        Floppy_Pos = 0
        if box_pos[1] == 0:
            Floppy_Pos = box_pos[0]
        if box_pos[1] == 1:
            Floppy_Pos = box_pos[0] + 4
        if box_pos[1] == 2:
            Floppy_Pos = box_pos[0] + 8
    AllSteps_saved = pickle.load(open("{}/{}".format(saves_loc, Floppy_Pos), 'rb'))
    set_list_saved = pickle.load(open("{}/s{}".format(saves_loc, Floppy_Pos), 'rb'))
    i = 0
    p_first_press = True
    if running == False:
        Break_play = True
    while running == True:
        keys = pygame.key.get_pressed()
        if set_list_saved[4] == True:
            if set_list_saved[3] > 8:
                loops = 8
            else:
                loops = set_list_saved[3]
        else:
            loops = set_list_saved[3]

        if ((AllSteps_saved[i])[0]) == 0:
            Banks = Banks_D
        if ((AllSteps_saved[i])[0]) == 1:
            Banks = Banks_K
        if ((AllSteps_saved[i])[0]) == 2:
            Banks = Banks_S
        if ((AllSteps_saved[i])[0]) == 3:
            Banks = Banks_F
        Type = Types[(AllSteps_saved[i])[0]]
        Bank = Banks[(AllSteps_saved[i])[1]]
        Oct = Octs[(AllSteps_saved[i])[2]]
        Note1 = Notes[(AllSteps_saved[i])[3]]
        Note2 = Notes[(AllSteps_saved[i])[4]]
        Note3 = Notes[(AllSteps_saved[i])[5]]
        if Note1 == "_":
            sound1 = pygame.mixer.Sound(empty_sound)
        else:
            sound1 = pygame.mixer.Sound(sound_loc.format(Type, Bank, Oct, Note1))
        if Note2 == "_":
            sound2 = pygame.mixer.Sound(empty_sound)
        else:
            sound2 = pygame.mixer.Sound(sound_loc.format(Type, Bank, Oct, Note2))
        if Note3 == "_":
            sound3 = pygame.mixer.Sound(empty_sound)
        else:
            sound3 = pygame.mixer.Sound(sound_loc.format(Type, Bank, Oct, Note3))
        if set_list_saved[4] == True:
            if ((AllSteps_saved[i + 8])[0]) == 0:
                Banks = Banks_D
            if ((AllSteps_saved[i + 8])[0]) == 1:
                Banks = Banks_K
            if ((AllSteps_saved[i + 8])[0]) == 2:
                Banks = Banks_S
            if ((AllSteps_saved[i + 8])[0]) == 3:
                Banks = Banks_F
            Type2 = Types[(AllSteps_saved[i + 8])[0]]
            print((AllSteps_saved[i + 8])[1])
            Bank2 = Banks[(AllSteps_saved[i + 8])[1]]
            Oct2 = Octs[(AllSteps_saved[i + 8])[2]]
            Note4 = Notes[(AllSteps_saved[i + 8])[3]]
            Note5 = Notes[(AllSteps_saved[i + 8])[4]]
            Note6 = Notes[(AllSteps_saved[i + 8])[5]]
            if Note4 == "_":
                sound4 = pygame.mixer.Sound(empty_sound)
            else:
                sound4 = pygame.mixer.Sound(sound_loc.format(Type2, Bank2, Oct2, Note4))
            if Note5 == "_":
                sound5 = pygame.mixer.Sound(empty_sound)
            else:
                sound5 = pygame.mixer.Sound(sound_loc.format(Type2, Bank2, Oct2, Note5))
            if Note6 == "_":
                sound6 = pygame.mixer.Sound(empty_sound)
            else:
                sound6 = pygame.mixer.Sound(sound_loc.format(Type2, Bank2, Oct2, Note6))
        else:
            sound4 = sound5 = sound6 = pygame.mixer.Sound(empty_sound)
        if set_list_saved[4] == False:
            sound1.set_volume(vol)
            sound2.set_volume(vol)
            sound3.set_volume(vol)
            sound1.play(fade_ms=set_list_saved[1])
            sound2.play(fade_ms=set_list_saved[1])
            sound3.play(fade_ms=set_list_saved[1])
            time.sleep((60 / (set_list_saved[0] * 2)))
            sound1.fadeout(set_list_saved[2])
            sound2.fadeout(set_list_saved[2])
            sound3.fadeout(set_list_saved[2])
        else:
            sound1.set_volume(vol)
            sound2.set_volume(vol)
            sound3.set_volume(vol)
            sound4.set_volume(vol)
            sound5.set_volume(vol)
            sound6.set_volume(vol)
            sound1.play(fade_ms=set_list_saved[1])
            sound2.play(fade_ms=set_list_saved[1])
            sound3.play(fade_ms=set_list_saved[1])
            time.sleep((60 / (set_list_saved[0] * 2) * (set_list_saved[5] / 100)))
            sound4.play(fade_ms=set_list_saved[1])
            sound5.play(fade_ms=set_list_saved[1])
            sound6.play(fade_ms=set_list_saved[1])
            time.sleep((60 / (set_list_saved[0] * 2)) - (60 / (set_list_saved[0] * 2) * (set_list_saved[5] / 100)))
            sound1.fadeout(set_list_saved[2])
            sound2.fadeout(set_list_saved[2])
            sound3.fadeout(set_list_saved[2])
            sound4.fadeout(set_list_saved[2])
            sound5.fadeout(set_list_saved[2])
            sound6.fadeout(set_list_saved[2])
        if keys[pygame.K_p] or Start.is_pressed:
            if p_first_press == False:
                running = False
                Break_play = True
                time.sleep(0.2)
            else:
                p_first_press = False
        pygame.event.pump()
        i += 1
        if i == loops:
            running = False
    return Break_play


def Floppy_Save(Floppy_Pos, First_Loop, running, Full_Loop):
    AllSteps_saved = pickle.load(open("{}/{}".format(saves_loc, Floppy_Pos), 'rb'))
    set_list_saved = pickle.load(open("{}/s{}".format(saves_loc, Floppy_Pos), 'rb'))
    i = 0
    while running == True:
        if set_list_saved[4] == True:
            if set_list_saved[3] > 8:
                loops = 8
            else:
                loops = set_list_saved[3]
        else:
            loops = set_list_saved[3]
        if ((AllSteps_saved[i])[0]) == 0:
            Banks = Banks_D
        if ((AllSteps_saved[i])[0]) == 1:
            Banks = Banks_K
        if ((AllSteps_saved[i])[0]) == 2:
            Banks = Banks_S
        if ((AllSteps_saved[i])[0]) == 3:
            Banks = Banks_F
        Type = Types[(AllSteps_saved[i])[0]]
        Bank = Banks[(AllSteps_saved[i])[1]]
        Oct = Octs[(AllSteps_saved[i])[2]]
        Note1 = Notes[(AllSteps_saved[i])[3]]
        Note2 = Notes[(AllSteps_saved[i])[4]]
        Note3 = Notes[(AllSteps_saved[i])[5]]
        if Note1 == "_":
            sound1 = AudioSegment.from_wav(empty_sound)
        else:
            sound1 = AudioSegment.from_wav(sound_loc.format(Type, Bank, Oct, Note1))
        if Note2 == "_":
            sound2 = AudioSegment.from_wav(empty_sound)
        else:
            sound2 = AudioSegment.from_wav(sound_loc.format(Type, Bank, Oct, Note2))
        if Note3 == "_":
            sound3 = AudioSegment.from_wav(empty_sound)
        else:
            sound3 = AudioSegment.from_wav(sound_loc.format(Type, Bank, Oct, Note3))
        if set_list_saved[4] == True:
            if ((AllSteps_saved[i + 8])[0]) == 0:
                Banks = Banks_D
            if ((AllSteps_saved[i + 8])[0]) == 1:
                Banks = Banks_K
            if ((AllSteps_saved[i + 8])[0]) == 2:
                Banks = Banks_S
            if ((AllSteps_saved[i + 8])[0]) == 3:
                Banks = Banks_F
            Type2 = Types[(AllSteps_saved[i + 8])[0]]
            Bank2 = Banks[(AllSteps_saved[i + 8])[1]]
            Oct2 = Octs[(AllSteps_saved[i + 8])[2]]
            Note4 = Notes[(AllSteps_saved[i + 8])[3]]
            Note5 = Notes[(AllSteps_saved[i + 8])[4]]
            Note6 = Notes[(AllSteps_saved[i + 8])[5]]
            if Note4 == "_":
                sound4 = AudioSegment.from_wav(empty_sound)
            else:
                sound4 = AudioSegment.from_wav(sound_loc.format(Type2, Bank2, Oct2, Note4))
            if Note5 == "_":
                sound5 = AudioSegment.from_wav(empty_sound)
            else:
                sound5 = AudioSegment.from_wav(sound_loc.format(Type2, Bank2, Oct2, Note5))
            if Note6 == "_":
                sound6 = AudioSegment.from_wav(empty_sound)
            else:
                sound6 = AudioSegment.from_wav(sound_loc.format(Type2, Bank2, Oct2, Note6))
        else:
            sound4 = sound5 = sound6 = AudioSegment.from_wav(empty_sound)
        offsetsound = AudioSegment.from_wav(empty_sound)
        sound_lenght = (((((60 / (set_list_saved[0] * 2)))) * 1000) + set_list[2])
        offset = (60 / (set_list[0] * 2) * (set_list[5] / 100))
        if set_list_saved[4] == False:
            sound1 = sound1[:sound_lenght]
            sound2 = sound2[:sound_lenght]
            sound3 = sound3[:sound_lenght]
        else:
            sound1 = sound1[:sound_lenght]
            sound2 = sound2[:sound_lenght]
            sound3 = sound3[:sound_lenght]
            sound4 = sound4[:(sound_lenght - (offset * 1000))]
            sound5 = sound5[:(sound_lenght - (offset * 1000))]
            sound6 = sound6[:(sound_lenght - (offset * 1000))]
            sound4 = offsetsound[:(offset * 1000)] + sound4
            sound5 = offsetsound[:(offset * 1000)] + sound5
            sound6 = offsetsound[:(offset * 1000)] + sound6
        Save_Sound = sound1
        Save_Sound = Save_Sound.overlay(sound2, gain_during_overlay=-0)
        Save_Sound = Save_Sound.overlay(sound3, gain_during_overlay=-0)
        Save_Sound = Save_Sound.overlay(sound4, gain_during_overlay=-0)
        Save_Sound = Save_Sound.overlay(sound5, gain_during_overlay=-0)
        Save_Sound = Save_Sound.overlay(sound6, gain_during_overlay=-0)
        if First_Loop == True and i == 0:
            Full_Loop = Save_Sound
        else:
            Full_Loop = Full_Loop.append(Save_Sound, crossfade=set_list[2])
        i += 1
        if i == loops:
            running = False
    return Full_Loop


def Run_All_Saves(All_running):
    time.sleep(0.2)
    i = 0
    p_first_press = True
    box_pos = [0, 0]
    Floppy_pos = 1
    window.blit(floppy_background, [0, 0])
    window.blit(floppy_box, (floppy_pos_x[box_pos[0]], floppy_pos_y[box_pos[1]]))
    Floppy_Text()
    pygame.display.flip()
    while All_running:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            if p_first_press == False:
                if Floppy_Play(i, True, False):
                    All_running = False
                    time.sleep(0.2)
                else:
                    p_first_press = False
        if Floppy_Play(i, True, True):
            All_running = False
        pygame.event.pump()
        i += 1
        if i == 12:
            i = 0
        box_pos[0] = Floppy_pos - 8
        box_pos[1] = 2
        if Floppy_pos < 8:
            box_pos[0] = Floppy_pos - 4
            box_pos[1] = 1
        if Floppy_pos < 4:
            box_pos[0] = Floppy_pos
            box_pos[1] = 0
        Floppy_pos += 1
        if Floppy_pos == 12:
            Floppy_pos = 0
        window.blit(floppy_background, [0, 0])
        window.blit(floppy_box, (floppy_pos_x[box_pos[0]], floppy_pos_y[box_pos[1]]))
        Floppy_Text()
        pygame.display.flip()


def Save_Song(All_running):
    time.sleep(0.2)
    i = 0
    box_pos = [0, 0]
    Floppy_pos = 1
    window.blit(floppy_background, [0, 0])
    window.blit(floppy_box, (floppy_pos_x[box_pos[0]], floppy_pos_y[box_pos[1]]))
    Floppy_Text()
    pygame.display.flip()
    Song = AudioSegment.from_wav(empty_sound)
    Song = Song[:1]
    while All_running:
        if i == 0:
            Song = Floppy_Save(i, True, True, Song)
        else:
            Song = Floppy_Save(i, False, True, Song)
        i += 1
        if i == 12:
            All_running = False
        box_pos[0] = Floppy_pos - 8
        box_pos[1] = 2
        if Floppy_pos < 8:
            box_pos[0] = Floppy_pos - 4
            box_pos[1] = 1
        if Floppy_pos < 4:
            box_pos[0] = Floppy_pos
            box_pos[1] = 0
        Floppy_pos += 1
        if Floppy_pos == 12:
            Floppy_pos = 0
        window.blit(floppy_background, [0, 0])
        window.blit(floppy_box, (floppy_pos_x[box_pos[0]], floppy_pos_y[box_pos[1]]))
        Floppy_Text()
        pygame.display.flip()
    Song_list = os.listdir(song_loc)
    Song_list  = [val for val in Song_list if not val.startswith(".")]
    Song -= 0
    Song.export("{}/Song{}.wav".format(song_loc, len(Song_list) + 1), format="wav", bitrate="192k")


def Carry_Right():
    global AllSteps_Main

    if box_pos[0] != 15:
        if box_pos[1] == 0:
            if ((AllSteps_Main[box_pos[0]])[0]) == 0:
                Banks = Banks_D
            if ((AllSteps_Main[box_pos[0]])[0]) == 1:
                Banks = Banks_K
            if ((AllSteps_Main[box_pos[0]])[0]) == 2:
                Banks = Banks_S
            if ((AllSteps_Main[box_pos[0]])[0]) == 3:
                Banks = Banks_F
            AllSteps_Main[box_pos[0] + 1][box_pos[1]] = AllSteps_Main[box_pos[0]][box_pos[1]]
            AllSteps_Main[box_pos[0] + 1][box_pos[1] + 1] = AllSteps_Main[box_pos[0]][box_pos[1] + 1]
            Boxes[box_pos[1]][box_pos[0] + 2] = font1.render(Types[(AllSteps_Main[box_pos[0] + 1])[box_pos[1]]], True,
                                                             (0, 0, 0))
            Boxes[box_pos[1] + 1][box_pos[0] + 2] = font1.render(Banks[(AllSteps_Main[box_pos[0] + 1])[box_pos[1] + 1]],
                                                                 True, (0, 0, 0))
        if box_pos[1] == 1:
            if ((AllSteps_Main[box_pos[0]])[0]) == 0:
                Banks = Banks_D
            if ((AllSteps_Main[box_pos[0]])[0]) == 1:
                Banks = Banks_K
            if ((AllSteps_Main[box_pos[0]])[0]) == 2:
                Banks = Banks_S
            if ((AllSteps_Main[box_pos[0]])[0]) == 3:
                Banks = Banks_F
            AllSteps_Main[box_pos[0] + 1][box_pos[1]] = AllSteps_Main[box_pos[0]][box_pos[1]]
            AllSteps_Main[box_pos[0] + 1][box_pos[1] - 1] = AllSteps_Main[box_pos[0]][box_pos[1] - 1]
            Boxes[box_pos[1] - 1][box_pos[0] + 2] = font1.render(Types[(AllSteps_Main[box_pos[0] + 1])[box_pos[1] - 1]],
                                                                 True, (0, 0, 0))
            Boxes[box_pos[1]][box_pos[0] + 2] = font1.render(Banks[(AllSteps_Main[box_pos[0] + 1])[box_pos[1]]], True,
                                                             (0, 0, 0))
        if box_pos[1] == 2:
            AllSteps_Main[box_pos[0] + 1][box_pos[1]] = AllSteps_Main[box_pos[0]][box_pos[1]]
            Boxes[box_pos[1]][box_pos[0] + 2] = font1.render(Octs[(AllSteps_Main[box_pos[0] + 1])[box_pos[1]]], True,
                                                             (0, 0, 0))
        if box_pos[1] == 3 or box_pos[1] == 4 or box_pos[1] == 5:
            AllSteps_Main[box_pos[0] + 1][box_pos[1]] = AllSteps_Main[box_pos[0]][box_pos[1]]
            Boxes[box_pos[1]][box_pos[0] + 2] = font1.render(Notes[(AllSteps_Main[box_pos[0] + 1])[box_pos[1]]], True,
                                                             (0, 0, 0))
        Seq_Right_Pressed()


def Carry_Left():
    global AllSteps_Main

    if box_pos[0] != 0:
        if box_pos[1] == 0:
            if ((AllSteps_Main[box_pos[0]])[0]) == 0:
                Banks = Banks_D
            if ((AllSteps_Main[box_pos[0]])[0]) == 1:
                Banks = Banks_K
            if ((AllSteps_Main[box_pos[0]])[0]) == 2:
                Banks = Banks_S
            if ((AllSteps_Main[box_pos[0]])[0]) == 3:
                Banks = Banks_F
            AllSteps_Main[box_pos[0] - 1][box_pos[1]] = AllSteps_Main[box_pos[0]][box_pos[1]]
            AllSteps_Main[box_pos[0] - 1][box_pos[1] + 1] = AllSteps_Main[box_pos[0]][box_pos[1] + 1]
            Boxes[box_pos[1]][box_pos[0]] = font1.render(Types[(AllSteps_Main[box_pos[0] - 1])[box_pos[1]]], True,
                                                         (0, 0, 0))
            Boxes[box_pos[1] + 1][box_pos[0]] = font1.render(Banks[(AllSteps_Main[box_pos[0] - 1])[box_pos[1] + 1]],
                                                             True, (0, 0, 0))
        if box_pos[1] == 1:
            if ((AllSteps_Main[box_pos[0]])[0]) == 0:
                Banks = Banks_D
            if ((AllSteps_Main[box_pos[0]])[0]) == 1:
                Banks = Banks_K
            if ((AllSteps_Main[box_pos[0]])[0]) == 2:
                Banks = Banks_S
            if ((AllSteps_Main[box_pos[0]])[0]) == 3:
                Banks = Banks_F
            AllSteps_Main[box_pos[0] - 1][box_pos[1]] = AllSteps_Main[box_pos[0]][box_pos[1]]
            AllSteps_Main[box_pos[0] - 1][box_pos[1] - 1] = AllSteps_Main[box_pos[0]][box_pos[1] - 1]
            Boxes[box_pos[1] - 1][box_pos[0]] = font1.render(Types[(AllSteps_Main[box_pos[0] - 1])[box_pos[1] - 1]],
                                                             True, (0, 0, 0))
            Boxes[box_pos[1]][box_pos[0]] = font1.render(Banks[(AllSteps_Main[box_pos[0] - 1])[box_pos[1]]], True,
                                                         (0, 0, 0))
        if box_pos[1] == 2:
            AllSteps_Main[box_pos[0] - 1][box_pos[1]] = AllSteps_Main[box_pos[0]][box_pos[1]]
            Boxes[box_pos[1]][box_pos[0]] = font1.render(Octs[(AllSteps_Main[box_pos[0] - 1])[box_pos[1]]], True,
                                                         (0, 0, 0))
        if box_pos[1] == 3 or box_pos[1] == 4 or box_pos[1] == 5:
            AllSteps_Main[box_pos[0] - 1][box_pos[1]] = AllSteps_Main[box_pos[0]][box_pos[1]]
            Boxes[box_pos[1]][box_pos[0]] = font1.render(Notes[(AllSteps_Main[box_pos[0] - 1])[box_pos[1]]], True,
                                                         (0, 0, 0))
        Seq_Left_Pressed()


def Creat_Boxes():
    Box_0_1 = font1.render("Type", True, (0, 0, 0))
    Box_0_2 = font1.render(Types[(AllSteps_Main[0])[0]], True, (0, 0, 0))
    Box_0_3 = font1.render(Types[(AllSteps_Main[1])[0]], True, (0, 0, 0))
    Box_0_4 = font1.render(Types[(AllSteps_Main[2])[0]], True, (0, 0, 0))
    Box_0_5 = font1.render(Types[(AllSteps_Main[3])[0]], True, (0, 0, 0))
    Box_0_6 = font1.render(Types[(AllSteps_Main[4])[0]], True, (0, 0, 0))
    Box_0_7 = font1.render(Types[(AllSteps_Main[5])[0]], True, (0, 0, 0))
    Box_0_8 = font1.render(Types[(AllSteps_Main[6])[0]], True, (0, 0, 0))
    Box_0_9 = font1.render(Types[(AllSteps_Main[7])[0]], True, (0, 0, 0))
    Box_0_10 = font1.render(Types[(AllSteps_Main[8])[0]], True, (0, 0, 0))
    Box_0_11 = font1.render(Types[(AllSteps_Main[9])[0]], True, (0, 0, 0))
    Box_0_12 = font1.render(Types[(AllSteps_Main[10])[0]], True, (0, 0, 0))
    Box_0_13 = font1.render(Types[(AllSteps_Main[11])[0]], True, (0, 0, 0))
    Box_0_14 = font1.render(Types[(AllSteps_Main[12])[0]], True, (0, 0, 0))
    Box_0_15 = font1.render(Types[(AllSteps_Main[13])[0]], True, (0, 0, 0))
    Box_0_16 = font1.render(Types[(AllSteps_Main[14])[0]], True, (0, 0, 0))
    Box_0_17 = font1.render(Types[(AllSteps_Main[15])[0]], True, (0, 0, 0))
    # _
    Box_1_1 = font1.render("Bank", True, (0, 0, 0))
    if ((AllSteps_Main[0])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[0])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[0])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[0])[0]) == 3:
        Banks = Banks_F
    Box_1_2 = font1.render(Banks[(AllSteps_Main[0])[1]], True, (0, 0, 0))
    if ((AllSteps_Main[1])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[1])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[1])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[1])[0]) == 3:
        Banks = Banks_F
    Box_1_3 = font1.render(Banks[(AllSteps_Main[1])[1]], True, (0, 0, 0))
    if ((AllSteps_Main[2])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[2])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[2])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[2])[0]) == 3:
        Banks = Banks_F
    Box_1_4 = font1.render(Banks[(AllSteps_Main[2])[1]], True, (0, 0, 0))
    if ((AllSteps_Main[3])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[3])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[3])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[3])[0]) == 3:
        Banks = Banks_F
    Box_1_5 = font1.render(Banks[(AllSteps_Main[3])[1]], True, (0, 0, 0))
    if ((AllSteps_Main[4])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[4])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[4])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[4])[0]) == 3:
        Banks = Banks_F
    Box_1_6 = font1.render(Banks[(AllSteps_Main[4])[1]], True, (0, 0, 0))
    if ((AllSteps_Main[5])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[5])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[5])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[5])[0]) == 3:
        Banks = Banks_F
    Box_1_7 = font1.render(Banks[(AllSteps_Main[5])[1]], True, (0, 0, 0))
    if ((AllSteps_Main[6])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[6])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[6])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[6])[0]) == 3:
        Banks = Banks_F
    Box_1_8 = font1.render(Banks[(AllSteps_Main[6])[1]], True, (0, 0, 0))
    if ((AllSteps_Main[7])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[7])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[7])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[7])[0]) == 3:
        Banks = Banks_F
    Box_1_9 = font1.render(Banks[(AllSteps_Main[7])[1]], True, (0, 0, 0))
    if ((AllSteps_Main[8])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[8])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[8])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[8])[0]) == 3:
        Banks = Banks_F
    Box_1_10 = font1.render(Banks[(AllSteps_Main[8])[1]], True, (0, 0, 0))
    if ((AllSteps_Main[9])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[9])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[9])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[9])[0]) == 3:
        Banks = Banks_F
    Box_1_11 = font1.render(Banks[(AllSteps_Main[9])[1]], True, (0, 0, 0))
    if ((AllSteps_Main[10])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[10])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[10])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[10])[0]) == 3:
        Banks = Banks_F
    Box_1_12 = font1.render(Banks[(AllSteps_Main[10])[1]], True, (0, 0, 0))
    if ((AllSteps_Main[11])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[11])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[11])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[11])[0]) == 3:
        Banks = Banks_F
    Box_1_13 = font1.render(Banks[(AllSteps_Main[11])[1]], True, (0, 0, 0))
    if ((AllSteps_Main[12])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[12])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[12])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[12])[0]) == 3:
        Banks = Banks_F
    Box_1_14 = font1.render(Banks[(AllSteps_Main[12])[1]], True, (0, 0, 0))
    if ((AllSteps_Main[13])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[13])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[13])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[13])[0]) == 3:
        Banks = Banks_F
    Box_1_15 = font1.render(Banks[(AllSteps_Main[13])[1]], True, (0, 0, 0))
    if ((AllSteps_Main[14])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[14])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[14])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[14])[0]) == 3:
        Banks = Banks_F
    Box_1_16 = font1.render(Banks[(AllSteps_Main[14])[1]], True, (0, 0, 0))
    if ((AllSteps_Main[15])[0]) == 0:
        Banks = Banks_D
    if ((AllSteps_Main[15])[0]) == 1:
        Banks = Banks_K
    if ((AllSteps_Main[15])[0]) == 2:
        Banks = Banks_S
    if ((AllSteps_Main[15])[0]) == 3:
        Banks = Banks_F
    Box_1_17 = font1.render(Banks[(AllSteps_Main[15])[1]], True, (0, 0, 0))
    # _
    Box_2_1 = font1.render("Oct", True, (0, 0, 0))
    Box_2_2 = font1.render(Octs[(AllSteps_Main[0])[2]], True, (0, 0, 0))
    Box_2_3 = font1.render(Octs[(AllSteps_Main[1])[2]], True, (0, 0, 0))
    Box_2_4 = font1.render(Octs[(AllSteps_Main[2])[2]], True, (0, 0, 0))
    Box_2_5 = font1.render(Octs[(AllSteps_Main[3])[2]], True, (0, 0, 0))
    Box_2_6 = font1.render(Octs[(AllSteps_Main[4])[2]], True, (0, 0, 0))
    Box_2_7 = font1.render(Octs[(AllSteps_Main[5])[2]], True, (0, 0, 0))
    Box_2_8 = font1.render(Octs[(AllSteps_Main[6])[2]], True, (0, 0, 0))
    Box_2_9 = font1.render(Octs[(AllSteps_Main[7])[2]], True, (0, 0, 0))
    Box_2_10 = font1.render(Octs[(AllSteps_Main[8])[2]], True, (0, 0, 0))
    Box_2_11 = font1.render(Octs[(AllSteps_Main[9])[2]], True, (0, 0, 0))
    Box_2_12 = font1.render(Octs[(AllSteps_Main[10])[2]], True, (0, 0, 0))
    Box_2_13 = font1.render(Octs[(AllSteps_Main[11])[2]], True, (0, 0, 0))
    Box_2_14 = font1.render(Octs[(AllSteps_Main[12])[2]], True, (0, 0, 0))
    Box_2_15 = font1.render(Octs[(AllSteps_Main[13])[2]], True, (0, 0, 0))
    Box_2_16 = font1.render(Octs[(AllSteps_Main[14])[2]], True, (0, 0, 0))
    Box_2_17 = font1.render(Octs[(AllSteps_Main[15])[2]], True, (0, 0, 0))

    # _
    Box_3_1 = font1.render("Note 1", True, (0, 0, 0))
    Box_3_2 = font1.render(Notes[(AllSteps_Main[0])[3]], True, (0, 0, 0))
    Box_3_3 = font1.render(Notes[(AllSteps_Main[1])[3]], True, (0, 0, 0))
    Box_3_4 = font1.render(Notes[(AllSteps_Main[2])[3]], True, (0, 0, 0))
    Box_3_5 = font1.render(Notes[(AllSteps_Main[3])[3]], True, (0, 0, 0))
    Box_3_6 = font1.render(Notes[(AllSteps_Main[4])[3]], True, (0, 0, 0))
    Box_3_7 = font1.render(Notes[(AllSteps_Main[5])[3]], True, (0, 0, 0))
    Box_3_8 = font1.render(Notes[(AllSteps_Main[6])[3]], True, (0, 0, 0))
    Box_3_9 = font1.render(Notes[(AllSteps_Main[7])[3]], True, (0, 0, 0))
    Box_3_10 = font1.render(Notes[(AllSteps_Main[8])[3]], True, (0, 0, 0))
    Box_3_11 = font1.render(Notes[(AllSteps_Main[9])[3]], True, (0, 0, 0))
    Box_3_12 = font1.render(Notes[(AllSteps_Main[10])[3]], True, (0, 0, 0))
    Box_3_13 = font1.render(Notes[(AllSteps_Main[11])[3]], True, (0, 0, 0))
    Box_3_14 = font1.render(Notes[(AllSteps_Main[12])[3]], True, (0, 0, 0))
    Box_3_15 = font1.render(Notes[(AllSteps_Main[13])[3]], True, (0, 0, 0))
    Box_3_16 = font1.render(Notes[(AllSteps_Main[14])[3]], True, (0, 0, 0))
    Box_3_17 = font1.render(Notes[(AllSteps_Main[15])[3]], True, (0, 0, 0))

    Box_4_1 = font1.render("Note 2", True, (0, 0, 0))
    Box_4_2 = font1.render(Notes[(AllSteps_Main[0])[4]], True, (0, 0, 0))
    Box_4_3 = font1.render(Notes[(AllSteps_Main[1])[4]], True, (0, 0, 0))
    Box_4_4 = font1.render(Notes[(AllSteps_Main[2])[4]], True, (0, 0, 0))
    Box_4_5 = font1.render(Notes[(AllSteps_Main[3])[4]], True, (0, 0, 0))
    Box_4_6 = font1.render(Notes[(AllSteps_Main[4])[4]], True, (0, 0, 0))
    Box_4_7 = font1.render(Notes[(AllSteps_Main[5])[4]], True, (0, 0, 0))
    Box_4_8 = font1.render(Notes[(AllSteps_Main[6])[4]], True, (0, 0, 0))
    Box_4_9 = font1.render(Notes[(AllSteps_Main[7])[4]], True, (0, 0, 0))
    Box_4_10 = font1.render(Notes[(AllSteps_Main[8])[4]], True, (0, 0, 0))
    Box_4_11 = font1.render(Notes[(AllSteps_Main[9])[4]], True, (0, 0, 0))
    Box_4_12 = font1.render(Notes[(AllSteps_Main[10])[4]], True, (0, 0, 0))
    Box_4_13 = font1.render(Notes[(AllSteps_Main[11])[4]], True, (0, 0, 0))
    Box_4_14 = font1.render(Notes[(AllSteps_Main[12])[4]], True, (0, 0, 0))
    Box_4_15 = font1.render(Notes[(AllSteps_Main[13])[4]], True, (0, 0, 0))
    Box_4_16 = font1.render(Notes[(AllSteps_Main[14])[4]], True, (0, 0, 0))
    Box_4_17 = font1.render(Notes[(AllSteps_Main[15])[4]], True, (0, 0, 0))

    Box_5_1 = font1.render("Note 3", True, (0, 0, 0))
    Box_5_2 = font1.render(Notes[(AllSteps_Main[0])[5]], True, (0, 0, 0))
    Box_5_3 = font1.render(Notes[(AllSteps_Main[1])[5]], True, (0, 0, 0))
    Box_5_4 = font1.render(Notes[(AllSteps_Main[2])[5]], True, (0, 0, 0))
    Box_5_5 = font1.render(Notes[(AllSteps_Main[3])[5]], True, (0, 0, 0))
    Box_5_6 = font1.render(Notes[(AllSteps_Main[4])[5]], True, (0, 0, 0))
    Box_5_7 = font1.render(Notes[(AllSteps_Main[5])[5]], True, (0, 0, 0))
    Box_5_8 = font1.render(Notes[(AllSteps_Main[6])[5]], True, (0, 0, 0))
    Box_5_9 = font1.render(Notes[(AllSteps_Main[7])[5]], True, (0, 0, 0))
    Box_5_10 = font1.render(Notes[(AllSteps_Main[8])[5]], True, (0, 0, 0))
    Box_5_11 = font1.render(Notes[(AllSteps_Main[9])[5]], True, (0, 0, 0))
    Box_5_12 = font1.render(Notes[(AllSteps_Main[10])[5]], True, (0, 0, 0))
    Box_5_13 = font1.render(Notes[(AllSteps_Main[11])[5]], True, (0, 0, 0))
    Box_5_14 = font1.render(Notes[(AllSteps_Main[12])[5]], True, (0, 0, 0))
    Box_5_15 = font1.render(Notes[(AllSteps_Main[13])[5]], True, (0, 0, 0))
    Box_5_16 = font1.render(Notes[(AllSteps_Main[14])[5]], True, (0, 0, 0))
    Box_5_17 = font1.render(Notes[(AllSteps_Main[15])[5]], True, (0, 0, 0))

    Boxes = [
        [Box_0_1, Box_0_2, Box_0_3, Box_0_4, Box_0_5, Box_0_6, Box_0_7, Box_0_8, Box_0_9, Box_0_10, Box_0_11, Box_0_12,
         Box_0_13, Box_0_14, Box_0_15, Box_0_16, Box_0_17],
        [Box_1_1, Box_1_2, Box_1_3, Box_1_4, Box_1_5, Box_1_6, Box_1_7, Box_1_8, Box_1_9, Box_1_10, Box_1_11, Box_1_12,
         Box_1_13, Box_1_14, Box_1_15, Box_1_16, Box_1_17],
        [Box_2_1, Box_2_2, Box_2_3, Box_2_4, Box_2_5, Box_2_6, Box_2_7, Box_2_8, Box_2_9, Box_2_10, Box_2_11, Box_2_12,
         Box_2_13, Box_2_14, Box_2_15, Box_2_16, Box_2_17],
        [Box_3_1, Box_3_2, Box_3_3, Box_3_4, Box_3_5, Box_3_6, Box_3_7, Box_3_8, Box_3_9, Box_3_10, Box_3_11, Box_3_12,
         Box_3_13, Box_3_14, Box_3_15, Box_3_16, Box_3_17],
        [Box_4_1, Box_4_2, Box_4_3, Box_4_4, Box_4_5, Box_4_6, Box_4_7, Box_4_8, Box_4_9, Box_4_10, Box_4_11, Box_4_12,
         Box_4_13, Box_4_14, Box_4_15, Box_4_16, Box_4_17],
        [Box_5_1, Box_5_2, Box_5_3, Box_5_4, Box_5_5, Box_5_6, Box_5_7, Box_5_8, Box_5_9, Box_5_10, Box_5_11, Box_5_12,
         Box_5_13, Box_5_14, Box_5_15, Box_5_16, Box_5_17]]
    return Boxes


def Creat_Steps():
    Step1 = [0, 1, 0, 0, 0, 0]
    Step2 = [0, 1, 0, 0, 0, 0]
    Step3 = [0, 1, 0, 0, 0, 0]
    Step4 = [0, 1, 0, 0, 0, 0]
    Step5 = [0, 1, 0, 0, 0, 0]
    Step6 = [0, 1, 0, 0, 0, 0]
    Step7 = [0, 1, 0, 0, 0, 0]
    Step8 = [0, 1, 0, 0, 0, 0]
    Step9 = [1, 0, 0, 1, 0, 0]
    Step10 = [1, 0, 0, 1, 0, 0]
    Step11 = [1, 0, 0, 1, 0, 0]
    Step12 = [1, 0, 0, 1, 0, 0]
    Step13 = [1, 0, 0, 1, 0, 0]
    Step14 = [1, 0, 0, 1, 0, 0]
    Step15 = [1, 0, 0, 1, 0, 0]
    Step16 = [1, 0, 0, 1, 0, 0]
    AllSteps_Main = [Step1, Step2, Step3, Step4, Step5,
                     Step6, Step7, Step8, Step9, Step10, Step11, Step12, Step13, Step14, Step15, Step16]
    return AllSteps_Main


def Creat_Floppy():
    Floppy_1 = font3.render("1", True, (0, 0, 0))
    Floppy_2 = font3.render("2", True, (0, 0, 0))
    Floppy_3 = font3.render("3", True, (0, 0, 0))
    Floppy_4 = font3.render("4", True, (0, 0, 0))
    Floppy_5 = font3.render("5", True, (0, 0, 0))
    Floppy_6 = font3.render("6", True, (0, 0, 0))
    Floppy_7 = font3.render("7", True, (0, 0, 0))
    Floppy_8 = font3.render("8", True, (0, 0, 0))
    Floppy_9 = font3.render("9", True, (0, 0, 0))
    Floppy_10 = font3.render("10", True, (0, 0, 0))
    Floppy_11 = font3.render("11", True, (0, 0, 0))
    Floppy_12 = font3.render("12", True, (0, 0, 0))
    Floppy_numbers = [Floppy_1,Floppy_2,Floppy_3,Floppy_4,Floppy_5,Floppy_6,Floppy_7,Floppy_8,Floppy_9,Floppy_10,Floppy_11,Floppy_12]
    return Floppy_numbers


def Vol_up():
    keys = pygame.key.get_pressed()
    pygame.event.pump()
    if keys[pygame.K_RIGHT] and keys[pygame.K_a] or Right.is_pressed and B.is_pressed:
        vol = pickle.load(open("vol", 'rb'))
        vol = vol * 10
        if vol != 10:
            vol += 1
        vol = vol / 10
        pickle.dump(vol, open("vol", "wb"))
        Vol = font2.render("{}".format(vol), True, (0, 0, 0))
        window.blit(Vol, (10, 10))
        pygame.display.flip()
        time.sleep(0.5)


def Vol_down():
    keys = pygame.key.get_pressed()
    pygame.event.pump()
    if keys[pygame.K_LEFT] and keys[pygame.K_a] or Left.is_pressed and B.is_pressed:
        vol = pickle.load(open("vol", 'rb'))
        vol = vol * 10
        if vol != 0:
            vol -= 1
        vol = vol / 10
        pickle.dump(vol, open("vol", "wb"))
        Vol = font2.render("{}".format(vol), True, (0, 0, 0))
        window.blit(Vol, (10, 10))
        pygame.display.flip()
        time.sleep(0.5)


# Buttons

Left = Button(4)
Up = Button(17)
Down = Button(27)
Right = Button(22)
Select = Button(5)
A = Button(6)
Start = Button(13)
B = Button(26)

# audio variables

max_bpm = 240
max_fade = 1000
max_offset = 100
max_steps = 16
bpm = 180
fadeout = 50
fadein = 50
steps = 8
double_track = False
offset = 0
# vol =  pickle.load(open("vol", 'rb'))
vol = 0.4
set_list = [bpm, fadein, fadeout, steps, double_track, offset]
Types = ["Drum", "Key", "Synth", "FX"]
Octs = ["Oct1", "Oct2", "Oct3"]
Notes = ["_", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
banks_loc = "/media/pi/PYQUENCER/Library"
Banks_D = sorted(os.listdir("{}/{}".format(banks_loc, Types[0])))
Banks_D = [val for val in Banks_D if not val.startswith(".")]
Banks_K = sorted(os.listdir("{}/{}".format(banks_loc, Types[1])))
Banks_K = [val for val in Banks_K if not val.startswith(".")]
Banks_S = sorted(os.listdir("{}/{}".format(banks_loc, Types[2])))
Banks_S = [val for val in Banks_S if not val.startswith(".")]
Banks_F = sorted(os.listdir("{}/{}".format(banks_loc, Types[3])))
Banks_F = [val for val in Banks_F if not val.startswith(".")]


# Text for each box based on selected variables for de sequencer
text_font = "/media/pi/PYQUENCER/Assets/retro.ttf"
Text_Size1 = 7
Text_Size2 = 30
Text_Size3 = 15
font1 = pygame.font.Font(text_font, Text_Size1)
font2 = pygame.font.SysFont(text_font, Text_Size2)
font3 = pygame.font.Font(text_font, Text_Size3)

global AllSteps_Main
AllSteps_Main = Creat_Steps()
Boxes = Creat_Boxes()
Floppy_numbers = Creat_Floppy()
# Pygame configuration
global seq_running, box_pos
running = True
box_pos = [0, 0]
clock = pygame.time.Clock()
window = pygame.display.set_mode((320, 240), pygame.FULLSCREEN)
fullscreen = window.copy()
pygame.mouse.set_visible(False)
seq_x_offset = 4
seq_y_offset = 13
seq_pos_x =  [35, 70, 105, 140, 175, 210, 245, 280,35, 70, 105, 140, 175, 210, 245, 280]
seq_pos_y =  [10, 45, 80, 120, 155, 190]
men_x_offset = 2
men_y_offset = 34
export_box_pos_x = 115
export_box_pos_y = 3
men_pos_x = [100, 125, 195]
men_pos_y = [26, 76, 126, 176]
set_pos_x = [5, 260]
set_pos_y = [28,58,88,118,148,178]
set_x_offset = 20
set_y_offset = 10
floppy_pos_x = [15, 87, 159, 231]
floppy_pos_y = [21, 93, 165]
floppy_x_offset = 5
floppy_y_offset = 5
conf_win_pos_x = 0
conf_win_pos_y = 0
song_loc = "/media/pi/PYQUENCER/Songs"
asset_loc = "/media/pi/PYQUENCER/Assets"
sound_loc = '/media/pi/PYQUENCER/Library/{}/{}/{}/{}.wav'
empty_sound = '/media/pi/PYQUENCER/Library/_.wav'
saves_loc = "/media/pi/PYQUENCER/Saves"
set_background = pygame.image.load("{}/Set_BG.png".format(asset_loc)).convert()
set_box = pygame.image.load("{}/Set_Box.png".format(asset_loc)).convert_alpha()
seq_background_1 = pygame.image.load("{}/Seq_BG_1.png".format(asset_loc)).convert()
seq_background_2 = pygame.image.load("{}/Seq_BG_2.png".format(asset_loc)).convert()
seq_box = pygame.image.load("{}/Seq_Box.png".format(asset_loc)).convert_alpha()
seq_box_2 = pygame.image.load("{}/Seq_Box.png".format(asset_loc)).convert_alpha()
men_background = pygame.image.load("{}/Men_BG.png".format(asset_loc)).convert()
men_box = pygame.image.load("{}/Men_Box.png".format(asset_loc)).convert_alpha()
floppy_background = pygame.image.load("{}/Floppy_BG.png".format(asset_loc)).convert()
floppy_box = pygame.image.load("{}/Floppy_Box.png".format(asset_loc)).convert_alpha()
conf_window = pygame.image.load("{}/Floppy_PU_BG.png".format(asset_loc)).convert_alpha()
export_box = pygame.image.load("{}/Floppy_Box2.png".format(asset_loc)).convert_alpha()
#                             Program Running
# ______________________________________________________________________________
while running:
    Menu(True)











