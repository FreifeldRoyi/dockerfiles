import os

ignores = [".git", ".vscode"]
all_dirs = sorted([d[0][2:] for d in os.walk(".") if d[1] == [] and [ignore for ignore in ignores if ignore in d[0] or d[0] == "."] == []])

cur_dir = os.getcwd()
for d in all_dirs:
  cwd_dir = os.path.join(os.getcwd(),d)
  os.chdir(cwd_dir)
  if os.path.exists("./build.py"):
    os.system("python3 ./build.py")
  else:
    split = d.split(os.sep)[-1]
    split = split[2:] if len(split) >= 2 and split[0].isdigit() and split[1] == "-" else split
    os.system(f"docker build -t freifeld/{split} .")
  os.chdir(cur_dir)