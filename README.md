## pyaudio_sample
### 概要
[Pyaudio](https://people.csail.mit.edu/hubert/pyaudio/docs/)を使いwavファイルの読み込みとマイク入力処理を試す．
また，[matplotlib](https://matplotlib.org/)を使用し，波形をリアルタイムにプロットする．

### ソースコード
- wave_plot.py  
  wavファイルを読み込み，再生しながらリアルタイムに(時間領域)波形をプロットする．
- freq_plot.py  
  wavファイルを読み込み，再生しながらリアルタイムに周波数波形をプロットする．
- record_plot.py  
  マイクから入力された信号をフーリエ変換し，リアルタイムに周波数波形をプロットする．
