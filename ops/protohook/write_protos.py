from os import listdir, system, chdir
import time

if __name__ == '__main__':
    
    t = time.time()
    branch_name = hash(t)

    for proto_file in listdir("proto_files"):
        file = str(proto_file)
        attr_name = file.replace(".proto", "")
        system(f"cp proto_files/{proto_file} protobufs/strategies/{attr_name}/{file}")
    
    chdir("protobufs")
    system(f"git checkout -b {branch_name}")
    system("git add .")
    system("""git commit -m "[{branch_name}] Automated files" """)
    system(f"git push --set-upstream origin {branch_name}")
