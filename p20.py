def f(time1, time2):
    def to_minutes(t):
        t_clean = t.lower().strip()
        is_pm = "pm" in t_clean
        is_am = "am" in t_clean
        t_clean = t_clean.replace("am", "").replace("pm", "")
        
        hours, minutes = map(int, t_clean.split(":"))
        
        if is_pm and hours != 12:
            hours += 12
        elif is_am and hours == 12:
            hours = 0
            
        return hours * 60 + minutes

    if to_minutes(time1) <= to_minutes(time2):
        return time1
    else:
        return time2

if __name__ == "__main__":
    print(f("13:06", "13:12"))
    print(f("1:38pm", "13:31"))
    print(f("08:08", "8:01am"))
    print(f("6:00pm", "18:00"))
