with open('./1_input.txt', 'r') as lines:
    current_val = 51
    res = 0
    for line in lines:
        direction, num = line[0], int(line[1:])
        test_val = current_val
        #print(num, test_val, num - test_val, (test_val - num) % 100)
        if direction == 'L':
            if test_val - num < 1:
                test_val = 100 - (num - test_val)%100
            else:
                test_val-= num
        else:
            if test_val + num > 100:
                test_val = (test_val+num)%100
            else:
                test_val += num
        current_val = test_val
        print(current_val)
        if current_val == 1:
            res+=1
    print(res)
