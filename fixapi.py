import re, sys
p = "TMessagesProj/src/main/java/org/telegram/messenger/BuildVars.java"
aid = input("api_id (ارقام فقط): ").strip()
ah = input("api_hash (32 حرف): ").strip()
if not aid.isdigit():
    print("api_id لازم ارقام بس"); sys.exit(1)
if not re.fullmatch(r"[0-9a-fA-F]{32}", ah):
    print("api_hash لازم 32 حرف او رقم"); sys.exit(1)
s = open(p, encoding="utf-8").read()
s, a = re.subn(r"public static int APP_ID = [^\n]*;", "public static int APP_ID = " + aid + ";", s, count=1)
s, b = re.subn(r"public static String APP_HASH = [^\n]*;", 'public static String APP_HASH = "' + ah + '";', s, count=1)
if a != 1 or b != 1:
    print("ما لقيت السطرين، ما عدّلت شي:", a, b); sys.exit(1)
open(p, "w", encoding="utf-8").write(s)
print("تم")
