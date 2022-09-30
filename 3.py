#Theater seats
print('Total amount of collums: ')
nCols=input()
if int(nCols)>=1 and int(nCols)<=1000:
    print('Total amount of rows: ')
    nRows=input()
    if int(nRows)>=1 and int(nRows)<=1000:
        print('Personal collumn: ')
        col=input()
        if int(col)>=1 and int(col)<=int(nCols):
            print('Personal row: ')
            row=input()
            if int(row)>=1 and int(row)<=int(nRows):
                seats = (int(nCols)-int(col)+1) * (int(nRows)-int(row))
                print('Seats needed to be jumped: ', seats)


