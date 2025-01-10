## THIS IS FILE WITH EXAMPLE DATA AND USAGE, BECAUSE OF VERSION 0.1

result = """
[THINK]
For completing this task, i need write code that prints, umm... Hello World
[COMMAND]
touch main.py;nano main.py
[CLIPBOARD]
print("Hello world")
[HOTKEY]
ctrl+v;ctrl+s;ctrl+x
[COMMAND]
python main.py
"""

cleared_result = ""

def clear_output(output):
    global cleared_result
    lines = output.split("\n")
    for line in lines:
        if line.strip():
            cleared_result += line + "\n"
            
def proccess_commands():
    lines = cleared_result.split("\n")
    for line in range(len(lines)):
        if lines[line] == "[THINK]":
            print("THINK found")
        if lines[line] == "[COMMAND]":
            print("COMMAND found")
            command_list = lines[line + 1].split(";")
            for command in range(len(command_list)):
                print(f"Executing {command_list[command]}")
        if lines[line] == "[CLIPBOARD]":
            print(f"Copying {lines[line + 1]}")
        if lines[line] == "[HOTKEY]":
            print("HOTKEY found")
            hotkey_list = lines[line + 1].split(";")
            for hotkey in range(len(hotkey_list)):
                print(f"Pressing {hotkey_list[hotkey]}")
            

clear_output(result)
print(cleared_result)
proccess_commands()
