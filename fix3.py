import re, sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()

s, a = re.subn(r"int repeatCount = .*?: 1;", "int repeatCount = 1;", s, count=1, flags=re.S)
print("شلت التكرار:", a)

s, b = re.subn(r"تدبيل ×(\d+)", r"إرسال تلقائي \1", s)
print("غيّرت الأسماء:", b)

open(p, "w", encoding="utf-8").write(s)
