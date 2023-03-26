- filelists：Wave/000001.wav|ka3er3pu3#2pei2wai4sun1#1wan2hua2ti1#4。
- 音频文件导入Wave

hparams.py

- text_cleaners=['english_cleaners', 'chinese_cleaners']

- training_files='filelists/BZNSYP_audio_pinyin_train_filelist.txt'
- validation_files='filelists/BZNSYP_audio_pinyin_val_filelist.txt'
-     max_wav_value=29171.0,
      sampling_rate=48000,
      filter_length=4096,
      hop_length=int(48000 * 0.0125),
      win_length=int(48000 * 0.05),
      n_mel_channels=80,
      mel_fmin=0.0,
      mel_fmax=48000 / 2

symbols.py

-     # 创建特征数组
      yun_mu = 'a o e i u v er ai ei ui ao ou ia ie iu ua un uo ve iao iou uai uei an ian ' \
               'uan van en in uen vn ang iang uang eng ing ueng ong iong'
      sheng_mu = 'b p m f d t n l g k h j q x zh ch sh z c s r y w'
      symbols = yun_mu.split(' ')
      for yun in yun_mu.split(' '):
          for i in range(1, 5):
              symbols.append(yun + str(i))
      for sheng in sheng_mu.split(' '):
          symbols.append(sheng)
      symbols.sort()

__init__.py

- 去除_curly_re = re.compile(r'(.*?)\{(.+?)\}(.*)')
- 更改text_to_sequence()函数
      for py in text:
          # print(py)
          while len(py):
              match_s = ''
              for symbol in symbols:
                  if re.match(symbol, py) != None:
                      match_s = symbol
              if match_s == '':
                  break
              else:
                  sequence.append(_symbol_to_id[match_s])
              py = py.strip(match_s)
      # if len(s) > 1 and s[0] == '@':
      #   s = '{%s}' % s[1:]
  
