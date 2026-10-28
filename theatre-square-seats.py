row,column=map(int,input().split())
mirrored_row = 11 - row
if column <= 10:
    print("Right",mirrored_row,column)
else:
    mirrored_column =21-column
    print("Left",mirrored_row,mirrored_column)


    
        
