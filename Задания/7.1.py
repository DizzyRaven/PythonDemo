def moon_weight(my_w, aw):
    m_k = 0.165
    years = 15
    #Прибавил один так как Пит считает до 15 не включая его... =(
    for x in range(0, (years + 1)):
        mn_w = my_w * m_k
        print("Year: %s. Weight: %s. Moon Weight: %s." % (x, my_w, mn_w))
        my_w += aw
