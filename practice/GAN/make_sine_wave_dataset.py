import numpy as np
import os

def makeWave(x, amplitude=1, frequency=1, phase=0, vertical_shift=0):
    wave = amplitude * np.sin(frequency * (x + phase)) + vertical_shift
    return wave



def makeDataset(length, x):
    # length is the number of data
    dataset = np.zeros((length, len(x)))
    for idx in range(length):
        amp = 0.8 + np.abs(np.random.randn())
        freq = 1.3 + 0.3 * np.random.randn()
        ph = np.pi/2 * np.random.randn()
        vs = np.random.randn()
        dataset[idx, :] = makeWave(x=x, amplitude=amp, frequency=freq, phase=ph, vertical_shift=vs)
    # dataset = torch.from_numpy(dataset)
    return dataset

if __name__=="__main__":
    os.makedirs("data/sines", exist_ok=True)
    
    data_length = 1000
    x10 = np.arange(0, 10, 0.25) # 40 points
    
    # make dataset
    dataset = makeDataset(length=data_length, x=x10)
    dataset_name = "data/sines/sine_dataset_" + str(data_length) + ".npy"
    # save dataset in npy
    with open(dataset_name, "wb") as f:
        np.save(f, dataset)
    
    x_name = "data/sines/sine_x_" + str(data_length) + ".npy"
    # save x
    with open(x_name, "wb") as f:
        np.save(f, x10)