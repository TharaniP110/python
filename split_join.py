def split_and_join(line):
    new_line=""
    for i in range(0,len(line)):
        if(line[i]==' '):
            new_line+="-"+""
        else:
            new_line+=line[i]+""
    return new_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
