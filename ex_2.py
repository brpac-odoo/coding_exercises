with open('./1_input.txt', 'r') as lines:
    #0 99, 
    test_val = 50
    res = 0
    for line in lines:
        direction, num = line[0], int(line[1:])
        rot = 0
        if num == 0:
            continue

        if direction == 'L':
            test_val = (100 - test_val)%100
        if test_val + num > 99:
            rot = (test_val + num) // 100
            test_val = (test_val + num) % 100
        else:
            test_val += num
        if direction == 'L':
            test_val = (100 - test_val)%100
                            
        res+= rot

    print(res)
