def bubble(file1, file2, file3):
    files_list = [file1, file2, file3]
    nlist = [len(file1[1]), len(file2[1]), len(file3[1])]
    for i in range(len(nlist) - 1):
        for j in range(len(nlist)-i-1):
            if nlist[j] > nlist[j+1]:
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
                files_list[j], files_list[j+1] = files_list[j+1], files_list[j]
    return files_list

