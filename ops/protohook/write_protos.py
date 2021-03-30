from os import system, listdir

if __name__ == '__main__':

    for proto_file in listdir("proto_files"):
        file = str(proto_file)
        attr_name = file.replace(".proto", "")
        system(f"cp proto_files/{proto_file} protobufs/strategies/{attr_name}/{file}")
    