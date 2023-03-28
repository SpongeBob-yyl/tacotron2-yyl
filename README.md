国内镜像源

- -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/：conda使用清华镜像源
- -i https://pypi.tuna.tsinghua.edu.cn/simple：pip使用清华镜像源

如何安装1.15.0版本的tensorflow

conda命令

- 激活环境：conda activate tf1.15.2
- 查看安装包：conda list

安装Apex

- git clone https://github.com/NVIDIA/apex
- cd apex
- python setup.py install

需要的库

_pytorch_select           1.1.0                       cpu    defaults
_tflow_select             2.1.0                       gpu    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
absl-py                   0.15.0             pyhd3eb1b0_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
aiohttp                   3.8.3            py37h2bbff1b_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
aiosignal                 1.2.0              pyhd3eb1b0_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
astor                     0.8.1            py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
async-timeout             4.0.2            py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
asynctest                 0.13.0                     py_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
attrs                     22.1.0           py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
audioread                 3.0.0            py37h03978a9_0    conda-forge
blas                      1.0                         mkl    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
blinker                   1.4              py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
brotli                    1.0.9                h2bbff1b_7    defaults
brotli-bin                1.0.9                h2bbff1b_7    defaults
brotlipy                  0.7.0           py37h2bbff1b_1003    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
ca-certificates           2023.01.10           haa95532_0    defaults
cachetools                4.2.2              pyhd3eb1b0_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
certifi                   2022.12.7        py37haa95532_0    defaults
cffi                      1.15.1           py37h2bbff1b_3    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
charset-normalizer        2.0.4              pyhd3eb1b0_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
click                     8.0.4            py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
colorama                  0.4.6            py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
cryptography              39.0.1           py37h21b164f_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
cudatoolkit               10.0.130                      0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
cudnn                     7.6.5                cuda10.0_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
cycler                    0.11.0             pyhd3eb1b0_0    defaults
decorator                 5.1.1              pyhd8ed1ab_0    conda-forge
exceptiongroup            1.1.1              pyhd8ed1ab_0    conda-forge
fftw                      3.3.9                h2bbff1b_1    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
flit-core                 3.6.0              pyhd3eb1b0_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
fonttools                 4.25.0             pyhd3eb1b0_0    defaults
freetype                  2.12.1               ha860e81_0    defaults
frozenlist                1.3.3            py37h2bbff1b_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
gast                      0.2.2                    py37_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
giflib                    5.2.1                h8cc25b3_3    defaults
glib                      2.69.1               h5dc1a3c_2    defaults
google-auth               2.6.0              pyhd3eb1b0_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
google-auth-oauthlib      0.4.4              pyhd3eb1b0_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
google-pasta              0.2.0              pyhd3eb1b0_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
grpcio                    1.42.0           py37hc60d5dd_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
gst-plugins-base          1.18.5               h9e645db_0    defaults
gstreamer                 1.18.5               hd78058f_0    defaults
h5py                      3.7.0            py37h3de5c98_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
hdf5                      1.10.6               h1756f20_1    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
icc_rt                    2022.1.0             h6049295_2    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
icu                       58.2                 ha925a31_3    defaults
idna                      3.4              py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
importlib-metadata        4.11.3           py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
importlib_metadata        1.5.0                    py37_0    conda-forge
inflect                   5.3.0            py37haa95532_1    defaults
iniconfig                 2.0.0              pyhd8ed1ab_0    conda-forge
intel-openmp              2021.4.0          haa95532_3556    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
joblib                    1.2.0              pyhd8ed1ab_0    conda-forge
jpeg                      9e                   h2bbff1b_1    defaults
keras-applications        1.0.8                      py_1    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
keras-preprocessing       1.1.2              pyhd3eb1b0_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
kiwisolver                1.4.4            py37hd77b12b_0    defaults
lerc                      3.0                  hd77b12b_0    defaults
libblas                   3.8.0                    20_mkl    conda-forge
libbrotlicommon           1.0.9                h2bbff1b_7    defaults
libbrotlidec              1.0.9                h2bbff1b_7    defaults
libbrotlienc              1.0.9                h2bbff1b_7    defaults
libcblas                  3.8.0                    20_mkl    conda-forge
libclang                  12.0.0          default_h627e005_2    defaults
libdeflate                1.17                 h2bbff1b_0    defaults
libffi                    3.4.2                hd77b12b_6    defaults
libflac                   1.3.4                h0e60522_0    conda-forge
libiconv                  1.16                 h2bbff1b_2    defaults
libogg                    1.3.5                h2bbff1b_1    defaults
libopus                   1.3.1                h8ffe710_1    conda-forge
libpng                    1.6.39               h8cc25b3_0    defaults
libprotobuf               3.20.3               h23ce68f_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
librosa                   0.9.2              pyhd8ed1ab_0    conda-forge
libsndfile                1.0.31               h0e60522_1    conda-forge
libtiff                   4.5.0                h6c2663c_2    defaults
libvorbis                 1.3.7                he774522_0    defaults
libwebp                   1.2.4                hbc33d0d_1    defaults
libwebp-base              1.2.4                h2bbff1b_1    defaults
libxml2                   2.9.14               h0ad7f3c_0    defaults
libxslt                   1.1.35               h2bbff1b_0    defaults
llvmlite                  0.37.0           py37habb0c8c_0    conda-forge
lz4-c                     1.9.4                h2bbff1b_0    defaults
markdown                  3.4.1            py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
matplotlib                3.5.3            py37haa95532_0    defaults
matplotlib-base           3.5.3            py37hd77b12b_0    defaults
mkl                       2020.2                      256    defaults
mkl-service               2.3.0            py37h196d8e1_0    defaults
mkl_fft                   1.3.0            py37h46781fe_0    defaults
mkl_random                1.1.1            py37h47e9c7a_0    defaults
multidict                 6.0.2            py37h2bbff1b_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
munkres                   1.1.4                      py_0    defaults
ninja                     1.10.2               haa95532_5    defaults
ninja-base                1.10.2               h6d14046_5    defaults
numba                     0.54.1           py37h3e99911_0    conda-forge
numpy                     1.19.2           py37hadc3359_0    defaults
numpy-base                1.19.2           py37ha3acd2a_0    defaults
nvidia-apex               0.1              py37h8e62851_4    conda-forge
oauthlib                  3.2.1            py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
openssl                   1.1.1t               h2bbff1b_0    defaults
opt_einsum                3.3.0              pyhd3eb1b0_1    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
packaging                 22.0             py37haa95532_0    defaults
pcre                      8.45                 hd77b12b_0    defaults
pillow                    9.4.0            py37hd77b12b_0    defaults
pip                       22.3.1           py37haa95532_0    defaults
platformdirs              3.1.1              pyhd8ed1ab_0    conda-forge
pluggy                    1.0.0            py37h03978a9_3    conda-forge
ply                       3.11                     py37_0    defaults
pooch                     1.7.0              pyhd8ed1ab_0    conda-forge
protobuf                  3.20.3           py37hd77b12b_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
pyasn1                    0.4.8              pyhd3eb1b0_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
pyasn1-modules            0.2.8                      py_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
pycparser                 2.21               pyhd3eb1b0_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
pyjwt                     2.4.0            py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
pyopenssl                 23.0.0           py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
pyparsing                 3.0.9            py37haa95532_0    defaults
pyqt                      5.15.7           py37hd77b12b_0    defaults
pyqt5-sip                 12.11.0          py37hd77b12b_0    defaults
pysocks                   1.7.1                    py37_1    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
pytest                    7.2.0            py37h03978a9_0    conda-forge
python                    3.7.16               h6244533_0    defaults
python-dateutil           2.8.2              pyhd3eb1b0_0    defaults
python_abi                3.7                     2_cp37m    conda-forge
pyyaml                    6.0              py37hcc03f2d_4    conda-forge
qt-main                   5.15.2               he8e5bd7_7    defaults
qt-webengine              5.15.9               hb9a9bb5_5    defaults
qtwebkit                  5.212                h3ad3cdb_4    defaults
requests                  2.28.1           py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
requests-oauthlib         1.3.0                      py_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
resampy                   0.4.2              pyhd8ed1ab_0    conda-forge
rsa                       4.7.2              pyhd3eb1b0_1    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
scikit-learn              1.0.2            py37hcabfae0_0    conda-forge
scipy                     1.6.2            py37h14eb087_0    defaults
setuptools                65.6.3           py37haa95532_0    defaults
sip                       6.6.2            py37hd77b12b_0    defaults
six                       1.16.0             pyhd3eb1b0_1    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
soundfile                 0.12.1                   pypi_0    pypi
sqlite                    3.41.1               h2bbff1b_0    defaults
tensorboard               1.15.0                   pypi_0    pypi
tensorboard-data-server   0.6.1            py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
tensorboard-plugin-wit    1.8.1            py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
tensorflow                1.15.0          gpu_py37hc3743a6_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
tensorflow-base           1.15.0          gpu_py37h1afeea4_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
tensorflow-estimator      1.15.1                   pypi_0    pypi
tensorflow-gpu            1.15.0               h0d30ee6_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
termcolor                 1.1.0            py37haa95532_1    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
threadpoolctl             3.1.0              pyh8a188c0_0    conda-forge
tk                        8.6.12               h2bbff1b_0    defaults
toml                      0.10.2             pyhd3eb1b0_0    defaults
tomli                     2.0.1              pyhd8ed1ab_0    conda-forge
torch                     1.8.1+cu111              pypi_0    pypi
torchaudio                0.8.1                    pypi_0    pypi
torchvision               0.9.1+cu111              pypi_0    pypi
tornado                   6.2              py37h2bbff1b_0    defaults
tqdm                      4.65.0             pyhd8ed1ab_1    conda-forge
typing-extensions         4.4.0            py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
typing_extensions         4.4.0            py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
unidecode                 1.0.22                   py37_0    defaults
urllib3                   1.26.14          py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
vc                        14.2                 h21ff451_1    defaults
vs2015_runtime            14.27.29016          h5e58377_2    defaults
werkzeug                  0.16.1                     py_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
wheel                     0.38.4           py37haa95532_0    defaults
win_inet_pton             1.1.0            py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
wincertstore              0.2              py37haa95532_2    defaults
wrapt                     1.14.1           py37h2bbff1b_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
xz                        5.2.10               h8cc25b3_1    defaults
yaml                      0.2.5                h8ffe710_2    conda-forge
yarl                      1.8.1            py37h2bbff1b_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
zipp                      3.11.0           py37haa95532_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
zlib                      1.2.13               h8cc25b3_0    https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
zstd                      1.5.2                h19a0ad4_0    defaults

报错

- module 'tensorflow' has no attribute 'contrib'
  安装1.X版本的tensorflow
  - conda create --name tf1.15 python=3.7
  - conda activate tf1.15
  - conda install tensorflow-gpu=1.15.0
- ImportError: cannot import name 'trace' from tensorflow.python.profiler
  tensorflow-estimator 与 tensorflow版本不一致
  - conda install tensorflow-estimator=1.15.0，但是出现warning
    - tensorflow 1.15.0 requires tensorboard<1.16.0,>=1.15.0
    - tensorflow 1.15.0 requires tensorflow-estimator==1.15.1
  - conda install tensorflow-estimator=1.15.1
  - conda install tensorboard==1.15.0
- AssertionError：Torch not compiled with CUDA enabled
  pytorch版本与CUDA版本不一致
  安装合适版本的pytorch
  - pip install torch==1.8.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html
  - pip install torchvision==0.9.1+cu111 -f https://download.pytorch.org/whl/torch_stable.html
  - pip install torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
  - pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
- OSError: cannot load library 'F:\Anaconda\envs\tf1.15\Library\bin\sndfile.dll': error 0x7e
  使用pip指令进行插入soundfile时，所插入的仅仅是python包，若要使用soundfile则需要下载其启动文件（.exe）
  - http://www.mega-nerd.com/libsndfile/：下载对应文件
  - pip uninstall -y cffi pycparser SoundFile
  - pip install soundfile
- FileNotFoundError: [Errno 2] No such file or directory: 'DUMMY/LJ041-0048.wav'
- RuntimeError: CUDA out of memory. Tried to allocate 2.00 MiB (GPU 0; 3.00 GiB total capacity; 1.81 GiB already allocated; 1.91 MiB free; 1.86 GiB reserved in total by PyTorch)
- BrokenPipeError: [Errno 32] Broken pipe

记录

- conda install -c conda-forge nvidia-apex
- conda install matplotlib
- conda install -c conda-forge numpy
- conda install -c "conda-forge/label/cf201901" librosa
- conda install -c conda-forge inflect
- conda install scipy
- conda install Unidecode

记录1

- conda create --name tf1.15_py3.7 python=3.7
- conda activate tf1.15_py3.7
- conda install tensorflow-gpu=1.15.0 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/ 
- pip uninstall tensorflow-estimator
- conda install tensorflow-estimator=1.15.1 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
- conda install tensorboard==1.15.0 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
- pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
  
