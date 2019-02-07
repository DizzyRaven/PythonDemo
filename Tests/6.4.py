my_w = 72
m_k = 0.165
aw = 1
years = 15
for x in range(0, (years + 1)):#Прибавил один так как Пит считает до 15 не включая его... =(
    mn_w = my_w * m_k
    print("Year: %s. Weight: %s. Moon Weight: %s." % (x, my_w, mn_w))
    my_w += aw
