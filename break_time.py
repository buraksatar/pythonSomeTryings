# import modules
import time
import webbrowser

# declare variables
total_breaks = 3
break_count = 0

# call and show the current time
print("This program started on" + time.ctime() )

while ( break_count < total_breaks ) :
    # run it total_breaks times
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=lJXhxvJBeX0&spfreload=5")
    break_count = break_count + 1
