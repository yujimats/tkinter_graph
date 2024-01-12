import numpy as np

def generate_random_data(x_range, random_range):
    np.random.seed(123)
    x = np.linspace(*x_range)
    random_values = np.random.uniform(*random_range, size=x.shape)
    y = x + random_values
    return x, y

if __name__=='__main__':
    x_range = (0, 30)
    random_range = (0, 2)
    x, y = generate_random_data(x_range=x_range, random_range=random_range)

    # save
    np.savetxt('data.csv', np.column_stack((x, y)), delimiter=',')
