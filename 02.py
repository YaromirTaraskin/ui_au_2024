import sys
from functools import reduce

ru_alphas = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
latinated = 'abvgd__zijklmnoprstufh_____y_e__'
ru_latinated = {k: v for k, v in zip(ru_alphas, latinated)}
ru_latinated['е'] = 'je'
ru_latinated['ж'] = 'zh'
ru_latinated['ц'] = 'tz'
ru_latinated['ч'] = 'ch'
ru_latinated['ш'] = 'sh'
ru_latinated['щ'] = 'shch'
ru_latinated['ъ'] = ''
ru_latinated['ь'] = ''
ru_latinated['ю'] = 'ju'
ru_latinated['я'] = 'ja'
ru_latinated[' '] = '_'

text_pr = [sys.argv[1].lower().strip() if len(sys.argv) > 1 else sys.stdin.read().lower().strip()]
text_pr.extend(list(ru_latinated.keys()))
text = reduce(lambda acc, el: acc.replace(el, ru_latinated[el]), text_pr)

print(text)
