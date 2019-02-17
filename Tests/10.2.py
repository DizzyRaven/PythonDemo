import pickle
favorites = input('Введите свои ништяки: \n')
favorites = favorites.rsplit(sep=None, maxsplit=-1)
name = input('Введите название файла: \n')
save_file = open('D:\\_MYDOC\\GitHub\\PythonDemo\\Test\\' + name + '.dat', 'wb')
pickle.dump(favorites, save_file)
save_file.close()
print(favorites)
