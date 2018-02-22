# pytorch-pix2pix

A fork of PyTorch implementation of [Image-to-Image Translation Using Conditional Adversarial Networks](https://arxiv.org/pdf/1611.07004v1.pdf).

Based on [pix2pix](https://phillipi.github.io/pix2pix/) by Isola et al.

The examples from the paper: 


## preequirements

- Linux
- Python3 with numpy
- cuda
- pytorch
- torchvision

## Getting Started

**git clone**  
```console
$ git clone https://github.com/GINK03/pytorch-pix2pix
$ cd pix2pix-pytorch
```

**train dataset**
```console
$ python3 train.py --dataset facades --nEpochs 100 --cuda
```

**train dataset**
```console
$ python3 test.py --dataset facades --model checkpoint/facades/netG_model_epoch_200.pth --cuda
```

## Examples

### 白黒写真に色を付ける
夏＋花のデータセットを用いて、学習します
**Download**  
```console
$ wget https://www.dropbox.com/s/yhstjhqmsy1cneb/grayscale.zip?dl=0
$ mv grayscale.zip
$ cd dataset 
$ unzip grayscale.zip
```
**train dataset**
```console
$ python3 train.py --dataset grayscale --nEpochs 100 --cuda
```

**train dataset**
```console
$ python3 test.py --dataset grayscale --model checkpoint/grayscale/netG_model_epoch_100.pth --cuda
```

**example output**  

## Acknowledgments

This code is a concise implementation of [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix). Much easier to understand. And, transcode python2 coding style to python3.
