import argparse
import os
import torch
from imagededup.utils.models import MobilenetV3


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--device', default='cpu', type=str, help='cuda:0 or cpu')
    args = parser.parse_args()

    model_path = 'mobilenetv3-small-dedup.pt'
    torch.save(MobilenetV3(), model_path)
    model = torch.load(model_path)

    model_path = os.path.splitext(model_path)[0] + '.onnx'

    dummy_input = torch.randn(1, 3, 224, 224).to(args.device)
    torch.onnx.export(
        model,
        dummy_input,
        model_path,
        verbose=False,
        input_names=['input'],
        output_names=['output'],
        dynamic_axes={'input': {0: '?'}, 'output': {0: '?'}},
        opset_version=17
    )
