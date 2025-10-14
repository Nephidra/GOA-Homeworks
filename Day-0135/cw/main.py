# def position(letter) :
#     return "Position of alphabet: " + str('abcdefghijklmnopqrstuvwxyz'.index(letter) + 1)

# def decode_resistor_colors(bands):
#     colors = {
#         "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
#         "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9
#     }
#     t = {"gold": 5, "silver": 10}
#     part = bands.split()
    
#     value = (colors[part[0]] * 10 + colors[part[1]]) * 10 ** colors[part[2]]
#     tol = t.get(part[3], 20) if len(part) > 3 else 20
#     if value >= 1000000:
#         ohm = f"{value/1000000:g}M"
#     elif value >= 1000:
#         ohm = f"{value/1000:g}k"
#     else : 
#         ohm = str(int(value))
#     return f"{ohm} ohms, {tol}%"




# def format_duration(seconds):
#     if seconds == 0:
#         return "now"
#     units = [
#         ("year", 365 * 24 * 60 * 60),
#         ("day", 24 * 60 * 60),
#         ("hour", 60 * 60),
#         ("minute", 60),
#         ("second", 1)
#     ]
#     result = []
    
#     for name, time in units  :
#         value = seconds // time
#         if value :
#             seconds %= time
#             if value == 1 :
#                 s = ""
#             else :
#                 s = "s"
#             result.append(f"{value} {name}{s}")
        
#     if len(result) == 1 :
#         return result[0]
#     else :
#         return ", ".join(result[:-1]) + " and " + result[-1]