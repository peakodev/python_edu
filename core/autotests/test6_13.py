import shutil


def create_backup2(path, file_name, employee_residence):
    fpath = path +  '/' + file_name
    with open(fpath, 'wb') as file:
        for name, surname in employee_residence.items():
            file.write(f"{name} {surname}\n".encode())
    return shutil.make_archive('backup_folder', 'zip', path)



