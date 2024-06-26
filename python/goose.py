import os,time

def INIT_HONK():
 if os.name=="nt":
    import ctypes
    from ctypes import wintypes
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    kernel32.SetConsoleOutputCP(ctypes.c_uint(65001))  # CP_UTF8
    kernel32.SetConsoleCP(ctypes.c_uint(65001))        # CP_UTF8
    STD_OUTPUT_HANDLE = -11
    hConsole = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    if hConsole == wintypes.HANDLE(-1):
        return
    dwMode = ctypes.c_uint()
    if not kernel32.GetConsoleMode(hConsole, ctypes.byref(dwMode)):
        return
    dwMode.value |= 0x0004
    kernel32.SetConsoleMode(hConsole, dwMode)

colors=[
[223,224,232],
[163,167,194],
[171,81,48],
[255,137,51],
[20,24,46],
[207,117,43],
[128,128,128]
]

goose_frames=[
[
[6,6,6,6,6,6,6,6,6,6,6,0,0,6,6,6,],
[6,6,6,6,6,6,6,6,6,6,0,4,0,4,6,6,],
[6,6,6,6,6,6,6,6,6,6,0,3,3,3,3,3,],
[0,6,6,6,6,6,6,6,6,6,0,3,3,3,3,3,],
[0,0,6,6,6,6,6,6,6,6,0,0,0,6,6,6,],
[0,0,0,6,6,6,6,6,6,0,0,0,0,6,6,6,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,],
[0,0,0,1,1,0,0,0,1,1,0,0,0,6,6,6,],
[1,1,0,0,0,1,1,1,0,0,0,0,0,6,6,6,],
[6,1,1,1,0,0,0,0,0,0,0,1,1,6,6,6,],
[6,6,6,1,1,1,1,1,1,1,1,1,6,6,6,6,],
[6,6,6,2,6,6,6,6,6,6,6,2,6,6,6,6,],
[6,6,6,2,6,6,6,6,6,6,6,2,6,6,6,6,],
[6,6,6,2,6,6,6,6,6,6,6,2,6,6,6,6,],
[6,6,6,2,2,6,6,6,6,6,6,2,2,6,6,6,],
],

[
[6,6,6,6,6,6,6,6,6,0,0,0,6,6,6,6,],
[6,6,6,6,6,6,6,6,0,0,0,4,6,6,6,6,],
[0,0,6,6,6,6,6,6,0,4,0,0,6,6,6,6,],
[0,0,6,6,6,6,6,6,0,0,0,3,5,6,6,6,],
[0,0,0,6,6,6,6,6,0,0,5,3,3,3,6,6,],
[0,0,0,0,0,0,6,6,0,0,3,3,3,3,3,6,],
[0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,6,],
[0,0,0,0,0,0,0,0,0,0,0,6,3,3,6,6,],
[1,1,0,0,0,0,0,0,0,0,1,6,6,6,6,6,],
[6,1,1,0,0,0,0,0,0,1,1,6,6,6,6,6,],
[6,6,1,1,1,1,1,1,1,1,6,6,6,6,6,6,],
[6,6,6,2,6,6,6,6,2,6,6,6,6,6,6,6,],
[6,6,6,2,6,6,6,6,2,6,6,6,6,6,6,6,],
[6,6,6,2,6,6,6,6,2,6,6,6,6,6,6,6,],
[6,6,6,2,6,6,6,6,2,6,6,6,6,6,6,6,],
[6,6,6,2,2,6,6,6,2,2,6,6,6,6,6,6,],
],

[
[6,6,6,6,6,6,0,0,0,0,6,6,6,6,6,6,],
[6,6,6,6,6,6,4,0,0,4,6,6,6,6,6,6,],
[6,6,6,6,6,6,0,0,0,0,6,6,6,6,6,6,],
[6,6,6,6,6,6,5,3,3,5,6,6,6,6,6,6,],
[6,6,6,6,6,6,3,3,3,3,6,6,6,6,6,6,],
[6,6,6,6,0,0,0,0,0,0,0,0,6,6,6,6,],
[6,6,6,0,0,0,0,0,0,0,0,0,0,6,6,6,],
[6,6,0,0,0,0,0,0,0,0,0,0,0,0,6,6,],
[6,6,0,0,0,0,0,0,0,0,0,0,0,0,6,6,],
[6,6,1,1,0,0,0,0,0,0,0,0,1,1,6,6,],
[6,6,6,1,1,1,0,0,0,0,1,1,1,6,6,6,],
[6,6,6,6,1,1,1,1,1,1,1,1,6,6,6,6,],
[6,6,6,6,2,6,6,6,6,6,6,2,6,6,6,6,],
[6,6,6,6,2,6,6,6,6,6,6,2,6,6,6,6,],
[6,6,6,6,2,6,6,6,6,6,6,2,6,6,6,6,],
[6,6,6,6,2,6,6,6,6,6,6,2,6,6,6,6,],
],

[
[6,6,6,6,0,0,0,6,6,6,6,6,6,6,6,6,],
[6,6,6,6,4,0,0,0,6,6,6,6,6,6,6,6,],
[6,6,6,6,0,0,4,0,6,6,6,6,6,6,0,0,],
[6,6,6,5,3,0,0,0,6,6,6,6,6,6,0,0,],
[6,6,3,3,3,5,0,0,6,6,6,6,6,0,0,0,],
[6,3,3,3,3,3,0,0,6,6,0,0,0,0,0,0,],
[6,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,],
[6,6,3,3,6,0,0,0,0,0,0,0,0,0,0,1,],
[6,6,6,6,6,0,0,0,0,0,0,0,0,0,1,1,],
[6,6,6,6,6,1,1,0,0,0,0,0,0,1,1,6,],
[6,6,6,6,6,6,1,1,1,1,1,1,1,1,6,6,],
[6,6,6,6,6,6,6,2,6,6,6,6,2,6,6,6,],
[6,6,6,6,6,6,6,2,6,6,6,6,2,6,6,6,],
[6,6,6,6,6,6,6,2,6,6,6,6,2,6,6,6,],
[6,6,6,6,6,6,6,2,6,6,6,6,2,6,6,6,],
[6,6,6,6,6,6,2,2,6,6,6,2,2,6,6,6,],
],

[
[6,6,6,0,0,6,6,6,6,6,6,6,6,6,6,6,],
[6,6,4,0,4,0,6,6,6,6,6,6,6,6,6,6,],
[3,3,3,3,3,0,6,6,6,6,6,6,6,6,6,6,],
[3,3,3,3,3,0,6,6,6,6,6,6,6,6,6,0,],
[6,6,6,0,0,0,6,6,6,6,6,6,6,6,0,0,],
[6,6,6,0,0,0,0,6,6,6,6,6,6,0,0,0,],
[6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[6,6,6,0,0,0,1,1,0,0,0,1,1,0,0,0,],
[6,6,6,0,0,0,0,0,1,1,1,0,0,0,1,1,],
[6,6,6,1,1,0,0,0,0,0,0,0,1,1,1,6,],
[6,6,6,6,1,1,1,1,1,1,1,1,1,6,6,6,],
[6,6,6,6,2,6,6,6,6,6,6,6,2,6,6,6,],
[6,6,6,6,2,6,6,6,6,6,6,6,2,6,6,6,],
[6,6,6,6,2,6,6,6,6,6,6,6,2,6,6,6,],
[6,6,6,2,2,6,6,6,6,6,6,2,2,6,6,6,],
],

[
[6,3,3,3,0,0,6,6,6,6,6,6,6,6,6,6,],
[6,3,3,3,0,0,0,6,6,6,6,6,6,6,6,6,],
[6,6,3,3,0,0,0,6,6,6,6,6,6,6,6,6,],
[6,6,6,3,0,0,0,6,6,6,6,6,6,6,6,6,],
[6,6,6,6,0,0,0,6,6,6,6,6,6,6,6,6,],
[6,6,6,6,0,0,0,6,6,6,6,6,6,6,0,0,],
[6,6,6,6,0,0,0,0,0,0,0,6,0,0,0,0,],
[6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,],
[6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,],
[6,6,6,6,1,0,0,0,0,0,0,0,0,0,0,6,],
[6,6,6,6,1,1,0,0,0,0,0,0,0,1,1,6,],
[6,6,6,6,6,1,1,1,1,1,1,1,1,1,6,6,],
[6,6,6,6,6,6,6,2,6,6,6,6,2,6,6,6,],
[6,6,6,6,6,6,6,2,6,6,6,6,2,6,6,6,],
[6,6,6,6,6,6,6,2,6,6,6,6,2,6,6,6,],
[6,6,6,6,6,6,2,2,6,6,6,2,2,6,6,6,],
],

[
[6,6,6,6,6,6,0,0,0,0,6,6,6,6,6,6,],
[6,6,6,6,6,6,0,0,0,0,6,6,6,6,6,6,],
[6,6,6,6,6,6,0,0,0,0,6,6,6,6,6,6,],
[6,6,6,6,6,6,0,0,0,0,6,6,6,6,6,6,],
[6,6,6,6,6,6,0,0,0,0,6,6,6,6,6,6,],
[6,6,6,6,0,0,0,0,0,0,0,0,6,6,6,6,],
[6,6,6,0,0,0,0,1,1,0,0,0,0,6,6,6,],
[6,6,0,0,0,0,1,0,0,1,0,0,0,0,6,6,],
[6,6,0,0,0,0,1,0,0,1,0,0,0,0,6,6,],
[6,6,1,1,0,1,0,0,0,0,1,0,1,1,6,6,],
[6,6,6,1,1,1,0,0,0,0,1,1,1,6,6,6,],
[6,6,6,6,1,1,1,1,1,1,1,1,6,6,6,6,],
[6,6,6,6,2,6,6,6,6,6,6,2,6,6,6,6,],
[6,6,6,6,2,6,6,6,6,6,6,2,6,6,6,6,],
[6,6,6,6,2,6,6,6,6,6,6,2,6,6,6,6,],
[6,6,6,6,2,6,6,6,6,6,6,2,6,6,6,6,],
],

[
[6,6,6,6,6,6,6,6,6,6,0,0,3,3,3,6,],
[6,6,6,6,6,6,6,6,6,0,0,0,3,3,3,6,],
[6,6,6,6,6,6,6,6,6,0,0,0,3,3,6,6,],
[0,6,6,6,6,6,6,6,6,0,0,0,3,6,6,6,],
[0,6,6,6,6,6,6,6,6,0,0,0,6,6,6,6,],
[0,0,6,6,6,6,6,6,6,0,0,0,6,6,6,6,],
[0,0,0,6,6,0,0,0,0,0,0,0,6,6,6,6,],
[0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,],
[0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,],
[6,0,0,0,0,0,0,0,0,0,0,1,6,6,6,6,],
[6,1,1,0,0,0,0,0,0,0,1,1,6,6,6,6,],
[6,6,1,1,1,1,1,1,1,1,1,6,6,6,6,6,],
[6,6,6,2,6,6,6,6,2,6,6,6,6,6,6,6,],
[6,6,6,2,6,6,6,6,2,6,6,6,6,6,6,6,],
[6,6,6,2,6,6,6,6,2,6,6,6,6,6,6,6,],
[6,6,6,2,2,6,6,6,2,2,6,6,6,6,6,6,],
]

]

def draw_frame(frame,colors):
 output=""
 for i in range(0,len(frame),2):
  for n in range(len(frame[i])):
   output+=f"\033[38;2;{colors[frame[i][n]][0]};{colors[frame[i][n]][1]};{colors[frame[i][n]][2]}m\033[48;2;{colors[frame[i+1][n]][0]};{colors[frame[i+1][n]][1]};{colors[frame[i+1][n]][2]}m▀"
  output+="\033[0m\n"
 print(output+"\ni spin for fun\033[H")




print("\033[2J\033[H\033[?25l")
while True:
 draw_frame(goose_frames[0],colors)
 time.sleep(0.25)
 draw_frame(goose_frames[1],colors)
 time.sleep(0.25)
 draw_frame(goose_frames[2],colors)
 time.sleep(0.25)
 draw_frame(goose_frames[3],colors)
 time.sleep(0.25)
 draw_frame(goose_frames[4],colors)
 time.sleep(0.25)
 draw_frame(goose_frames[5],colors)
 time.sleep(0.25)
 draw_frame(goose_frames[6],colors)
 time.sleep(0.25)
 draw_frame(goose_frames[7],colors)
 time.sleep(0.25)
