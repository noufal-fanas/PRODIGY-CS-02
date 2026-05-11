import os
import random
import time
from PIL import Image
from tkinter import Tk, filedialog

# UI Colors
C = '\033[96m' # Cyan
M = '\033[95m' # Magenta
Y = '\033[93m' # Yellow
G = '\033[92m' # Green
W = '\033[0m'  # Reset
BOLD = '\033[1m'

# --- THE MASTERPIECE ASCII ---
MONA_LISA = r"""
                                  _______
                           _,,ad8888888888bba,_
                        ,ad88888I888888888888888ba,
                      ,88888888I88888888888888888888a,
                    ,d888888888I8888888888888888888888b,
                   d88888PP''  ''YY88888888888888888888b,
                 ,d88"'__,,--------,,,,.;ZZZY8888888888888,
                ,8IIl'"                ;;l"ZZZIII8888888888,
               ,I88l;'                  ;lZZZZZ888III8888888,
              ,II88Zl;.                  ;llZZZZZ888888I888888,
             ,II888Zl;.                .;;;;;lllZZZ888888I8888b
            ,II8888Z;;                  `;;;;;''llZZ8888888I8888,
            II88888Z;'                        .;lZZZ8888888I888b
            II88888Z; _,aaa,      .,aaaaa,__.l;llZZZ88888888I888
            II88888IZZZZZZZZZ,  .ZZZZZZZZZZZZZZ;llZZ88888888I888,
            II88888IZZ<'(@@>Z|  |ZZZ<'(@@>ZZZZ;;llZZ888888888I88I
           ,II88888;   `''' ;|  |ZZ; `'''     ;;llZ8888888888I888
           II888888l            `;;           .;llZZ8888888888I888,
          ,II888888Z;            ;;;         .;;llZZZ8888888888I888I
          III888888Zl;    ..,    `;;        ,;;lllZZZ88888888888I888
          II88888888Z;;...;(_    _)      ,;;;llZZZZ88888888888I888,
          II88888888Zl;;;;;' `--'Z;.    .,;;;;llZZZZ88888888888I888b
          ]I888888888Z;;;;'    ";llllll;..;;;lllZZZZ88888888888I8888,
          II888888888Zl.;;"Y88bd888P";;,..;lllZZZZZ88888888888I8888I
          II8888888888Zl;.; `"PPP";;;,..;lllZZZZZZZ88888888888I88888
          II888888888888Zl;;. `;;;l;;;;lllZZZZZZZZW88888888888I88888
          `II8888888888888Zl;.     ,;;lllZZZZZZZZWMZ88888888888I88888
           II8888888888888888ZbaalllZZZZZZZZZWWMZZZ8888888888I888888,
           `II88888888888888888b"WWZZZZZWWWMMZZZZZZI888888888I888888b
            `II88888888888888888;ZZMMMMMMZZZZZZZZllI888888888I8888888
             `II8888888888888888 `;lZZZZZZZZZZZlllll888888888I8888888,
              II8888888888888888, `;lllZZZZllllll;;.Y88888888I8888888b,
"""

TITLE = r"""
 ██████╗ ██╗██╗  ██╗██╗███████╗    ████████╗██████╗ ██╗██╗  ██╗██╗███████╗
 ██╔══██╗██║╚██╗██╔╝██║██╔════╝    ╚══██╔══╝██╔══██╗██║╚██╗██╔╝██║██╔════╝
 ██████╔╝██║ ╚███╔╝ ██║█████╗         ██║   ██████╔╝██║ ╚███╔╝ ██║█████╗  
 ██╔═══╝ ██║ ██╔██╗ ██║██╔══╝         ██║   ██╔══██╗██║ ██╔██╗ ██║██╔══╝  
 ██║     ██║██╔╝ ██╗██║███████╗       ██║   ██║  ██║██║██╔╝ ██╗██║███████╗
 ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚══════╝
"""

def center_print(text_block, color=W):
    try:
        width = os.get_terminal_size().columns
    except:
        width = 100
    lines = text_block.split('\n')
    for line in lines:
        pad = (width - len(line)) // 2
        print(f"{' ' * max(0, pad)}{color}{line}{W}")

def show_display():
    os.system('cls' if os.name == 'nt' else 'clear')
    center_print(MONA_LISA, C)
    center_print(TITLE, M)
    
    try: w = os.get_terminal_size().columns
    except: w = 100
    
    sep = "═" * 60
    print(f"{Y}{sep.center(w)}{W}")
    cred = "v1.0 | Developed by Noufal N S "
    print(f"{G}{BOLD}{cred.center(w)}{W}")
    print(f"{Y}{sep.center(w)}{W}\n")

def get_path(is_file=True):
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    p = filedialog.askopenfilename() if is_file else filedialog.askdirectory()
    root.destroy()
    return p

def engine(mode):
    show_display()
    img_p = get_path(True)
    if not img_p: return
    out_d = get_path(False)
    if not out_d: return
    
    try:
        key = int(input(f"{C}    >> ENTER SECRET PASSKEY (Numeric): {W}"))
    except: return

    print(f"\n{Y}    [*] Processing Pixel Data...{W}")
    
    try:
        img = Image.open(img_p).convert("RGB")
        px = list(img.getdata())
        idx = list(range(len(px)))
        random.seed(key)

        if mode == "encrypt":
            px = [(r^key%255, g^key%255, b^key%255) for r,g,b in px]
            random.shuffle(idx)
            res = [None]*len(px)
            for i, n in enumerate(idx): res[n] = px[i]
        else:
            random.shuffle(idx)
            un = [None]*len(px)
            for i, o in enumerate(idx): un[i] = px[o]
            res = [(r^key%255, g^key%255, b^key%255) for r,g,b in un]

        out_img = Image.new("RGB", img.size)
        out_img.putdata(res)
        name = f"PT_{mode}_{int(time.time())}.png"
        out_img.save(os.path.join(out_d, name))
        print(f"\n{G}    [✔] SUCCESS: Rendered as {name}{W}")
    except Exception as e:
        print(f"\n\033[91m    [!] ERROR: {e}{W}")
    input(f"\n{M}    Press ENTER to return...{W}")

def main():
    while True:
        show_display()
        try: w = os.get_terminal_size().columns
        except: w = 100
        
        opts = ["[1] Encrypt Art", "[2] Decrypt Art", "[3] Exit System"]
        for o in opts:
            print(o.center(w))
            
        cmd = input(f"\n{Y}    noufal@pixie-trixie:~$ {W}")
        if cmd == '1': engine("encrypt")
        elif cmd == '2': engine("decrypt")
        elif cmd == '3': break

if __name__ == "__main__":
    main()