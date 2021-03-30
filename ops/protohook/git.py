from os import listdir, system, chdir
import time

if __name__ == '__main__':
    t = time.time()
    branch_name = hash(t)
    chdir("protobufs")
    system(f"git checkout -b {branch_name}")
    system("git add .")
    system(f"""git commit -m "[{branch_name}] Automated files" """)
    system(f"git push --set-upstream origin {branch_name}")