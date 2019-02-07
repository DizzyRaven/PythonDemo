def moon_weight():
    import sys
    print('Введите ваш нынешний земной вес')
    my_w = int(sys.stdin.readline())
    print('Введите ежегодный прирост вашего веса')
    aw = float(sys.stdin.readline())
    print('Введите количество лет')
    years = int(sys.stdin.readline())
    m_k = 0.165
    #Прибавил один так как Пит считает до 15 не включая его... =(
    for x in range(0, (years + 1)):
        mn_w = my_w * m_k
        print("Year: %s. Weight: %s. Moon Weight: %s." % (x, my_w, mn_w))
        my_w += aw
