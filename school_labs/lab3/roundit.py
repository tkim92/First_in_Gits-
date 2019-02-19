def roundit(n):
    i = n
    if i > 0:
        i = i + 0.5
        return(int(i))
    elif i < 0:
        i = i - 0.5
        return(int(i))

def main():
    roundit(7.8)

if __name__ == '__main__':
    main()
