import os

def find_missing_files(imweb_dir="../imweb", img_dir="../img", output_file="missing_files.txt"):
    """
    imweb 폴더에 있는 .html 파일 중, img 폴더에 대응하는 .jpg 파일이 없는 목록을 찾습니다.
    """
    imweb_files = {f.split('.')[0] for f in os.listdir(imweb_dir)}
    img_files = {f.split('.')[0] for f in os.listdir(img_dir)}
    
    missing_files = imweb_files - img_files
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("imweb 폴더에 있지만 img 폴더에 없는 파일 목록입니다.\n")
        f.write("--------------------------------------------------\n")
        for filename in sorted(list(missing_files)):
            f.write(f"{filename}\n")
            
    print(f"작업이 완료되었습니다. '{output_file}' 파일을 확인하세요.")

if __name__ == "__main__":
    find_missing_files()