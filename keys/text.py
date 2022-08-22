class text:
    run = """
keys.run(Class, log, wasd):
 **Class(class parameter): the class that the execute function is in
  *Skey(key):
    DEFAULT esc
     key: the key that stops the script

  *log(1, 2, or 3):
    DEFAULT 3 
     1: if you want all buttons logged
     2: if you want some buttons logged
     3: if you want no buttons logged

  *wasd(True or False):
    DEFAULT False
     True: adds wasd to the foward/back/left/right commands
     False: removes wasd from the foward/back/left/right commands
    
  *keys(1, 2, 3, 4):
    DEFAULT 1
     1: activates commands for "up" "down" "right" "left"
     2: adds commands for "space" 
     3: adds commands for all normal characters(like abcd, and so on)
     4: adds commands for special characters(like f1, backspace, home, and so on)


EXAMPLES:
  keys.run(Class=Class, keys=1, wasd=False, log=2) or lib.run(Class, esc, 2, False, 1)"""
    full="""
*OPTIONAL
**REQUIRED

keys.run(Class, log, wasd):
 **Class(class parameter): the class that the execute function is in
  *Skey(key):
    DEFAULT esc
     key: the key that stops the script

  *log(1, 2, or 3):
    DEFAULT 3 
     1: if you want all buttons logged
     2: if you want some buttons logged
     3: if you want no buttons logged

  *wasd(True or False):
    DEFAULT False
     True: adds wasd to the foward/back/left/right commands
     False: removes wasd from the foward/back/left/right commands
    
  *keys(1, 2, 3, 4):
    DEFAULT 1
     1: activates commands for "up" "down" "right" "left"
     2: adds commands for "space" 
     3: adds commands for all normal characters(like abcd, and so on)
     4: adds commands for special characters(like f1, backspace, home, and so on)
       IMPORTANT: 4 is still a work in ptogress


EXAMPLES:
  keys.run(Class=Class, keys=1, wasd=False, log=2) or lib.run(Class, esc, 2, False, 1)


If you have further questions/ideas come talk to me or the teacher"""
