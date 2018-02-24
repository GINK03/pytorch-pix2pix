# pytorch-pix2pix

A fork of PyTorch implementation of [Image-to-Image Translation Using Conditional Adversarial Networks](https://arxiv.org/pdf/1611.07004v1.pdf).

Based on [pix2pix](https://phillipi.github.io/pix2pix/) by Isola et al.

The examples from the paper: 


## preequirements

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
$ wget https://www.dropbox.com/s/yhstjhqmsy1cneb/grayscale.zip
$ mv grayscale.zip dataset
$ cd dataset 
$ unzip grayscale.zip
```
**train dataset**
```console
$ python3 train.py --dataset grayscale --nEpochs 100 --cuda
```

**predict dataset**
```console
$ python3 test.py --dataset grayscale --model checkpoint/grayscale/netG_model_epoch_100.pth --cuda
```

**example output**  
<div align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/36538393-9d411e2c-1816-11e8-9ba1-f46298113e69.png">
</div>

### ノイズや欠落情報を復元する
"自然"のデータセットに対して、ノイズを乗せて復元を試みます  
**Download** 
```console
$ wget https://www.dropbox.com/s/1yvr560s24sliay/random_drop.zip
$ mv random_drop.zip dataset
$ cd dataset 
$ unzip random_drop.zip
```
**train dataset**
```console
$ python3 train.py --dataset random_drop --nEpochs 50 --cuda
```

**predict dataset**
```console
$ python3 test.py --dataset random_drop --model checkpoint/random_drop/netG_model_epoch_50.pth --cuda
```

**example output**  
<div align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/36575745-e9ecde36-188f-11e8-8614-844accb6a553.png">
</div>

### フォントのスタイルの変換を行う
人間が習字で書いたデータセットに対して、Takao Fontと対応させて、新規フォントを作るという発想です

**Download** 
```console
$ https://www.dropbox.com/s/owee6hxopnr4dpo/font.zip
$ mv font.zip dataset
$ cd dataset 
$ unzip font.zip
```
**train dataset**
```console
$ python3 train.py --dataset font --nEpochs 150 --cuda
```

**predict dataset**
```console
$ python3 test.py --dataset font --model checkpoint/font/netG_model_epoch_150.pth --cuda
```

**example output**  
<div align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/36622539-0fa7be28-1941-11e8-8ffa-06b105a5f4c4.png">
</div>


## Acknowledgments

This code is a concise implementation of [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix). Much easier to understand. And, transcode python2 coding style to python3.
