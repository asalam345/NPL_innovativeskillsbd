def activate_row(screen, row_index):
    for col in range(len(screen[row_index])):
        screen[row_index][col] = 1

monitor = [
[0, 0, 0], 
 [0, 0, 0], 
[0, 0, 0]
]
# print("monitor = [")
# for row_index, screen in enumerate(monitor):
#     print(f" {screen},")
# print(f" {monitor[-1]}")
# print("]")

for i in range(len(monitor)):
    activate_row(monitor, i)
    print(f"After activating row {i}: {monitor}")

