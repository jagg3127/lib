from pynput.keyboard import Key, Listener

def __r(key):
    if key == Key.esc and key == Key.f1:
        return False

def __p(key):
    main=globals()["main"]
    on=globals()["on"]
    try:
        test=key.char
        if on:
            print(test)
    except:
        if key == Key.up:
            main.execute(main, "up")
        elif key == Key.down:
            main.execute(main, "down")
        elif key == Key.right:
            main.execute(main, "right")
        elif key == Key.left:
            main.execute(main, "left")
        elif key == Key.space:
            main.execute(main, "space")
        elif key == Key.esc and key == Key.f1:
            return True            
        else:
            x=str(key).split(".")
            if on:
                print(f"Special: {x[1]}")



def run(x, on:bool):
    globals()["main"] = x
    globals()["on"] = on

    with Listener(on_press=__p, on_release=__r) as l:
        l.start
        l.join()