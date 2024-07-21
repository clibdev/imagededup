# Fork of [idealo/imagededup](https://github.com/idealo/imagededup)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.3. (🔥)
* Converted ONNX models from GitHub [releases page](https://github.com/clibdev/imagededup/releases). (🔥)
* The following deprecations has been fixed:
  * SetuptoolsDeprecationWarning: Invalid dash-separated options.
  * FutureWarning: Cython directive 'language_level' not set.

# Installation

```shell
pip install -r requirements.txt
```
```shell
python setup.py build_ext --inplace
```

# Pretrained models

| Name                    | Link                                                                                                                                                                                                              |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MobileNetV3-Small-Dedup | [PyTorch](https://github.com/clibdev/imagededup/releases/latest/download/https://mobilenetv3-small-dedup.pt), [ONNX](https://github.com/clibdev/imagededup/releases/latest/download/mobilenetv3-small-dedup.onnx) |

# Demo

```shell
python demo.py
```

# Export to ONNX format

```shell
pip install onnx
```
```shell
python export.py
```
