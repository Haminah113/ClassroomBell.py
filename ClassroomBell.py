import time

def classroom_bell_cycle():
    # Time duration for each stage (in seconds)
    lecture_duration = 25   # Lecture session
    short_break_duration = 5  # Short break
    lunch_break_duration = 15  # Lunch break

    while True:
        # Lecture session
        print("Lecture session: START")
        time.sleep(lecture_duration)
        print("Lecture session: DONE")
        print("Bell rings: DING DONG!")
        time.sleep(1)  # Short transition

        # Short break
        print("Short break: START")
        time.sleep(short_break_duration)
        print("Short break: DONE")
        print("Bell rings: DING DONG!")
        time.sleep(1)  # Short transition

        # Lunch break
        print("Lunch break: START")
        time.sleep(lunch_break_duration)
        print("Lunch break: DONE")
        print("Bell rings: DING DONG!")
        time.sleep(1)  # Restart the cycle

# Run the classroom bell cycle
classroom_bell_cycle()