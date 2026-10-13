import sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
if "textToolRepeat12" in s:
    print("موجود من قبل"); sys.exit()

def rep(s, old, new):
    n = s.count(old)
    return s.replace(old, new, 1), (1 if n else 0)

s, a = rep(s, "private boolean textToolRepeat3 = false;",
           "private boolean textToolRepeat3 = false;\n    private boolean textToolRepeat12 = false;")
s, b = rep(s, '+ "إرسال تلقائي 3"',
           '+ "إرسال تلقائي 3",\n                        (textToolRepeat12 ? "✓ " : "□ ") + "إرسال تلقائي 12"')
s, c = rep(s, "textToolRepeat3 = !textToolRepeat3;",
           "textToolRepeat3 = !textToolRepeat3;\n                                } else if (which == 8) {\n                                    textToolRepeat12 = !textToolRepeat12;")
s, d = rep(s, "(__n == 11 && textToolRepeat11)",
           "(__n == 11 && textToolRepeat11) || (__n == 12 && textToolRepeat12)")

open(p, "w", encoding="utf-8").write(s)
print("متغير:", a, "| قائمة:", b, "| ضغط:", c, "| شرط:", d)
