import re, sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()

# 1) احذف البلوك القديم
s, n = re.subn(r"\n        if \(__autoSending\) return;\n        try \{.*?catch \(Exception ignore\) \{ __autoSending = false; \}\n", "\n", s, flags=re.S)
print("حذفت بلوك قديم:", n)

# 2) ضيف البلوك الجديد
j = s.find("public void afterTextChanged(Editable", s.find("messageEditText.addTextChangedListener"))
k = s.find("{", j) + 1
code = r'''
        if (__autoSending) return;
        try {
            String __t = messageEditText.getText().toString();
            int __n = __t.length();
            boolean __on = (__n == 4 && textToolRepeat4) || (__n == 5 && textToolRepeat5) || (__n == 6 && textToolRepeat6) || (__n == 8 && textToolRepeat8) || (__n == 11 && textToolRepeat11);
            if (__on && __t.matches("\\d+")) {
                __autoSending = true;
                try { sendMessage(); } finally { __autoSending = false; }
                return;
            }
        } catch (Exception ignore) { __autoSending = false; }
'''
s = s[:k] + code + s[k:]

# 3) لا تكرار وقت الإرسال التلقائي
s, m = re.subn(r"int repeatCount = textToolRepeat11", "int repeatCount = __autoSending ? 1 : textToolRepeat11", s, count=1)
print("عدلت repeatCount:", m)

open(p, "w", encoding="utf-8").write(s)
