import sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
if "textToolDigitMap" in s:
    print("موجود من قبل"); sys.exit()

k_var = "private boolean textToolRepeat12 = false;"
k_menu = '+ "بروكسي"'
k_set = ".setItems(toolItems, (dialog, which) -> {"
k_guard = "if (__autoSending) return;"
counts = [s.count(k) for k in (k_var, k_menu, k_set, k_guard)]
print("مطابقات:", counts)
if counts != [1, 1, 1, 1]:
    print("ما عدّلت شي"); sys.exit()

s = s.replace(k_var, k_var + "\n    private boolean textToolDigitMap = false;", 1)

s = s.replace(k_menu, k_menu + ',\n                        (textToolDigitMap ? "✓ " : "□ ") + "تدبيل الأرقام"', 1)

s = s.replace(k_set, k_set + "\n                                if (which == 10) { textToolDigitMap = !textToolDigitMap; return; }", 1)

block = """if (__autoSending) return;
        if (textToolDigitMap) {
            String __d = messageEditText.getText().toString();
            if (__d.length() == 1) {
                int __rep = 0;
                switch (__d.charAt(0)) {
                    case '3': __rep = 5; break;
                    case '4': __rep = 4; break;
                    case '5': __rep = 7; break;
                    case '6': __rep = 6; break;
                    case '7': __rep = 4; break;
                    case '9': __rep = 9; break;
                }
                if (__rep > 0) {
                    __autoSending = true;
                    try {
                        StringBuilder __sb = new StringBuilder();
                        for (int __i = 0; __i < __rep; __i++) __sb.append(__d);
                        messageEditText.setText(__sb.toString());
                        sendMessage();
                    } finally { __autoSending = false; }
                    return;
                }
            }
        }"""
s = s.replace(k_guard, block, 1)
open(p, "w", encoding="utf-8").write(s)
print("تم")
