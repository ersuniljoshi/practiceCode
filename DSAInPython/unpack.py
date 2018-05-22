def func(x, y=None, z=None):
    print x, y, z


list_vec = [1, 0, 1]
tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1, 'a': 2}


func(list_vec)
func(*list_vec)
func(*tuple_vec)
func(**dict_vec)