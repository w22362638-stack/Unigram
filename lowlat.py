import re, glob
files = glob.glob("TMessagesProj/**/WebRtcAudioTrack.java", recursive=True)
print("الملفات:", files)
for p in files:
    s = open(p, encoding="utf-8").read()
    if "PERFORMANCE_MODE_LOW_LATENCY" in s:
        print("موجود من قبل:", p); continue
    s2, n = re.subn(r"(\.setTransferMode\(AudioTrack\.MODE_STREAM\))",
                    r"\1\n          .setPerformanceMode(AudioTrack.PERFORMANCE_MODE_LOW_LATENCY)", s, count=1)
    if n:
        open(p, "w", encoding="utf-8").write(s2)
        print("تم التعديل:", p)
    else:
        print("ما لقيت السطر المناسب:", p)
