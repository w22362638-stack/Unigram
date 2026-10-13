import sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
key = "messageEditText.addTextChangedListener"
i = s.find(key)
j = s.find("public void afterTextChanged(Editable", i)
k = s.find("{", j) + 1
code = '''
        try {
            String __t = messageEditText.getText().toString();
            if (!__t.isEmpty() && __t.matches("\\\\d+")) {
                android.content.SharedPreferences __sp = org.telegram.messenger.MessagesController.getGlobalMainSettings();
                if (__sp.getBoolean("autosend_" + __t.length(), false)) {
                    sendMessage();
                    return;
                }
            }
        } catch (Exception ignore) {}
'''
open(p, "w", encoding="utf-8").write(s[:k] + code + s[k:])
print("تم")
