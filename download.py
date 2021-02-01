import os

base = 'https://storage.googleapis.com/tensorflow/tf-keras-datasets/'
files = [
    'train-labels-idx1-ubyte.gz', 'train-images-idx3-ubyte.gz',
    't10k-labels-idx1-ubyte.gz', 't10k-images-idx3-ubyte.gz'
]

for f in files:
    fa = os.path.join(base, f)
    print('wget {}'.format(fa))
    print('ossutilmac64 cp {} oss://blade-opt/kubeflow/{}'.format(f, f))
    print('ossutilmac64 set-acl oss://blade-opt/kubeflow/{} public-read'.format(f))
