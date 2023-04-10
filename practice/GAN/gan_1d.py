import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import torch
import math
import os
import argparse



parser = argparse.ArgumentParser()
parser.add_argument("--n_epochs", type=int, default=200, help="number of epochs of training")
parser.add_argument("--batch_size", type=int, default=64, help="size of the batches")
parser.add_argument("--lr", type=float, default=0.0002, help="adam: learning rate")
parser.add_argument("--b1", type=float, default=0.5, help="adam: decay of first order momentum of gradient")
parser.add_argument("--b2", type=float, default=0.999, help="adam: decay of first order momentum of gradient")
parser.add_argument("--n_cpu", type=int, default=8, help="number of cpu threads to use during batch generation")
parser.add_argument("--latent_dim", type=int, default=100, help="dimensionality of the latent space")
parser.add_argument("--img_size", type=int, default=28, help="size of each image dimension")
parser.add_argument("--channels", type=int, default=1, help="number of image channels")
parser.add_argument("--sample_interval", type=int, default=400, help="interval betwen image samples")
opt = parser.parse_args()
print(opt)

class Sines():
    def __init__(self):
        self.data = []
        self.x = np.arange(0, 10, 0.25) # 40 points
        self.num_data = 100
    
    def makeWave(self, amplitude=1, frequency=1, phase=0, vertical_shift=0):
        wave = amplitude * np.sin(frequency * (self.x + phase)) + vertical_shift
        return wave
    
    def makeDataset(self):
        dataset = np.zeros((self.num_data, len(self.x)))
        for idx in range(self.num_data):
            amp = 0.8 + np.abs(np.random.randn())
            freq = 1.3 + 0.3 * np.random.randn()
            ph = np.pi/2 * np.random.randn()
            vs = np.random.randn()
            dataset[idx, :] = self.makeWave(amplitude=amp, frequency=freq, phase=ph, vertical_shift=vs)
        dataset = torch.from_numpy(dataset)
        return dataset
    

if __name__=="__main__":
    print("===== main running =====")
    for epoch in range(opt.n_epochs):
        for i, (imgs, _) in enumerate(dataloader):    
            pass
#         # Adversarial ground truths            
            
#         # Configure input            
            
#         # -----------------
#         #  Train Generator
#         # -----------------


#         # ---------------------
#         #  Train Discriminator
#         # ---------------------