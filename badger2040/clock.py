import time
import machine
import badger2040

# We're going to keep the badger on, so slow down the system clock if on battery
badger2040.system_speed(badger2040.SYSTEM_SLOW)

rtc = machine.RTC()
display = badger2040.Badger2040()
display.led(128)
display.update_speed(badger2040.UPDATE_TURBO)
display.font("gothic")

cursors = ["year", "month", "day", "hour", "minute"]
set_clock = False
cursor = 0
last = 0

# Set up the buttons
button_down = machine.Pin(badger2040.BUTTON_DOWN, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_up = machine.Pin(badger2040.BUTTON_UP, machine.Pin.IN, machine.Pin.PULL_DOWN)

button_a = machine.Pin(badger2040.BUTTON_A, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_b = machine.Pin(badger2040.BUTTON_B, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_c = machine.Pin(badger2040.BUTTON_C, machine.Pin.IN, machine.Pin.PULL_DOWN)


def days_in_month(month, year):
    if month == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return 29
    return (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[month - 1]


# Button handling function
def button(pin):
    global last, set_clock, cursor, year, month, day, hour, minute

    time.sleep(0.01)
    if not pin.value():
        return

    if button_a.value() and button_c.value():
        machine.reset()

    adjust = 0
    changed = False

    if pin == button_b:
        set_clock = not set_clock
        changed = True
        if not set_clock:
            rtc.datetime((year, month, day, 0, hour, minute, second, 0))

    if set_clock:
        if pin == button_c:
            cursor += 1
            cursor %= len(cursors)

        if pin == button_a:
            cursor -= 1
            cursor %= len(cursors)

        if pin == button_up:
            adjust = 1

        if pin == button_down:
            adjust = -1

        if cursors[cursor] == "year":
            year += adjust
            year = max(year, 2022)
            day = min(day, days_in_month(month, year))
        if cursors[cursor] == "month":
            month += adjust
            month = min(max(month, 1), 12)
            day = min(day, days_in_month(month, year))
        if cursors[cursor] == "day":
            day += adjust
            day = min(max(day, 1), days_in_month(month, year))
        if cursors[cursor] == "hour":
            hour += adjust
            hour %= 24
        if cursors[cursor] == "minute":
            minute += adjust
            minute %= 60

    if set_clock or changed:
        draw_clock()


# Register the button handling function with the buttons
button_down.irq(trigger=machine.Pin.IRQ_RISING, handler=button)
button_up.irq(trigger=machine.Pin.IRQ_RISING, handler=button)
button_a.irq(trigger=machine.Pin.IRQ_RISING, handler=button)
button_b.irq(trigger=machine.Pin.IRQ_RISING, handler=button)
button_c.irq(trigger=machine.Pin.IRQ_RISING, handler=button)


def draw_clock():
    hms = "{:02}:{:02}:{:02}".format(hour, minute, second)
    ymd = "{:04}/{:02}/{:02}".format(year, month, day)

    hms_width = display.measure_text(hms, 1.8)
    hms_offset = int((badger2040.WIDTH / 2) - (hms_width / 2))
    h_width = display.measure_text(hms[0:2], 1.8)
    mi_width = display.measure_text(hms[3:5], 1.8)
    mi_offset = display.measure_text(hms[0:3], 1.8)

    ymd_width = display.measure_text(ymd, 1.0)
    ymd_offset = int((badger2040.WIDTH / 2) - (ymd_width / 2))
    y_width = display.measure_text(ymd[0:4], 1.0)
    m_width = display.measure_text(ymd[5:7], 1.0)
    m_offset = display.measure_text(ymd[0:5], 1.0)
    d_width = display.measure_text(ymd[8:10], 1.0)
    d_offset = display.measure_text(ymd[0:8], 1.0)

    display.pen(15)
    display.clear()
    display.pen(0)
    display.thickness(5)
    display.text(hms, hms_offset, 40, 1.8)
    display.thickness(3)
    display.text(ymd, ymd_offset, 100, 1.0)

    if set_clock:
        if cursors[cursor] == "year":
            display.line(ymd_offset, 120, ymd_offset + y_width, 120)
        if cursors[cursor] == "month":
            display.line(ymd_offset + m_offset, 120, ymd_offset + m_offset + m_width, 120)
        if cursors[cursor] == "day":
            display.line(ymd_offset + d_offset, 120, ymd_offset + d_offset + d_width, 120)

        if cursors[cursor] == "hour":
            display.line(hms_offset, 70, hms_offset + h_width, 70)
        if cursors[cursor] == "minute":
            display.line(hms_offset + mi_offset, 70, hms_offset + mi_offset + mi_width, 70)

    display.update()


year, month, day, wd, hour, minute, second, _ = rtc.datetime()

if (year, month, day) == (2021, 1, 1):
    rtc.datetime((2022, 2, 28, 0, 12, 0, 0, 0))

last_second = second

while True:
    if not set_clock:
        year, month, day, wd, hour, minute, second, _ = rtc.datetime()
        if second != last_second:
            draw_clock()
            last_second = second
    time.sleep(0.01)
