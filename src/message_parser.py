from collections import namedtuple
from datetime import datetime  # Import datetime module

def parse_message(line: str):
    message = namedtuple("message", "date_time, sender, text")

    line2 = line.split("-")
    
    date_time_str = line2[0].strip()
    datettime = datetime.strptime(date_time_str, "%d/%m/%y, %H:%M")
    datettime2 = datettime.strftime("%d/%m/%y %H:%M")

    nametext = line2[1]
    nametext = nametext.split(":")
    sender = nametext[0].strip()
    text = nametext[1].strip()

    return message(datettime2, sender, text)



if __name__ == "__main__":
    print(parse_message("12/12/22, 12:39 - Antonio Murillo: a ti cual es el destino de cracovia que no te respondia"))
    