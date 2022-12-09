import torch
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
from config import opt


def test(**kwargs):
    pass

def train(**kwargs):
    # data
    data_train = datasets.ImageFolder(opt.train_data_root, transform=transforms.Compose([
        transforms.Resize(256),     # expand to 256, keep the aspect ratio unchanged
        transforms.CenterCrop(224), # cur from center to 224
        transforms.ToTensor(),
    ])) 
    data_train_loader = DataLoader(data_train,
        batch_size=opt.batch_size,
        shuffle=True
    )

def val(model, dataloader):
    pass

def help():
    pass

if __name__ == '__main__':
    import fire
    pass