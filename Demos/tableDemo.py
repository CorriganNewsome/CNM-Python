Customers = ["Lynda", "Rob", "Barney"]
heights = [10, 12, 8]
widths = [20, 60, 25]
Areas = 3 * [None]
Areas[0] = heights[0] * widths[0]
Areas[1] = heights[1] * widths[1]
Areas[2] = heights[2] * widths[2]

fmt = "%-00s %-10s %-10s %-10s"
fmtNum = "%-10s %-10.2f %-10.2f %-10.2f"
print(fmt % ("Customer", "Height", "Width", "Area"))
print(fmtNum % (Customers[0], heights[0], widths[0], Areas[0]))
print(fmtNum % (Customers[1], heights[1], widths[1], Areas[1]))
print(fmtNum % (Customers[2], heights[2], widths[2], Areas[2]))
