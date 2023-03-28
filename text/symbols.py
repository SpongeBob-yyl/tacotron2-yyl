""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. '''
# from text import cmudict
#
# _pad        = '_'
# _punctuation = '!\'(),.:;? '
# _special = '-'
# _letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
#
# # Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
# _arpabet = ['@' + s for s in cmudict.valid_symbols]
#
# # Export all symbols:
# symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters) + _arpabet


# 创建特征数组
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