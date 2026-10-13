import re, sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
# شيل البلوك القديم
s = re.sub(r"\n        try \{\n            String __t.*?catch \(Exception ignore\) \{\}\n", "\n", s, flags=re.S)
# حارس منع التكرار
if "__autoSending" not in s:
    i = s.find("public class ChatActivityEnterView")
    k = s.find("{", i) + 1
    s = s[:k] + "\n    private boolean __autoSending = false;\n" + s[k:]
j = s.find("public void afterTextChanged(Editable", s.find("messageEditText.addTextChangedListener"))
k = s.find("{", j) + 1
code = '''
        if (__autoSending) return;
        try {
            String __t = messageEditText.getText().toString();
            if (__t.matches("\\\\d+")) {
                android.content.SharedPreferences __sp = org.telegram.messenger.MessagesController.getGlobalMainSettings();
                if (__sp.getBoolean("autosend_" + __t.length(), false)) {
                    __autoSending = true;
                    try { sendMessage(); } finally { __autoSending = false; }
                    return;
                }
            }
        } catch (Exception ignore) { __autoSending = false; }
'''
open(p, "w", encoding="utf-8").write(s[:k] + code + s[k:])
print("تم")
