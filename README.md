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

| Name                    | Model Size (MB) | Link                                                                                                                                                                                                        | SHA-256                                                                                                                              |
|-------------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| MobileNetV3-Small-Dedup | 3.7<br>3.6      | [PyTorch](https://github.com/clibdev/imagededup/releases/latest/download/mobilenetv3-small-dedup.pt)<br>[ONNX](https://github.com/clibdev/imagededup/releases/latest/download/mobilenetv3-small-dedup.onnx) | e04376504b51694ec16ea5473eaf7ba419061953323d89c8e2e3f0bd2087e51b<br>cfdb10bd95a6b02c1c41618e2d9037d0ca835279c6d8b4d93553a7a04c5ca327 |

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
