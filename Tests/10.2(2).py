import pickle
load_file = open('D:\\_MYDOC\\GitHub\\PythonDemo\\Test\\Список ништяков.dat', 'rb')
loaded_data = pickle.load(load_file)
load_file.close()
print(loaded_data)
