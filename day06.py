with open('day06_input.txt') as f:
    data = f.read().strip()

# Part one
marker_index = None
for i in range(0, len(data) - 3):
    marker = set(data[i:i + 4])
    if len(marker) == 4:
        marker_index = 4 + i
        break
print(f"Part one answer - Marker index: {marker_index}")

# Part two
message_index = None
for i in range(0, len(data) - 13):
    message = set(data[i:i + 14])
    if len(message) == 14:
        message_index = 14 + i
        break
print(f"Part two answer - Message index: {message_index}")