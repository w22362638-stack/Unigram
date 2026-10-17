import re, sys
h = "TMessagesProj/jni/voip/webrtc/modules/audio_coding/codecs/opus/audio_coder_opus_common.h"
cm = open("TMessagesProj/jni/CMakeLists.txt", encoding="utf-8").read()
if not re.search(r"\blog\b", cm):
    print("مكتبة log مو مربوطة، ما عدّلت شي"); sys.exit()
s = open(h, encoding="utf-8").read()
if "AudioPktDur" in s:
    print("موجود من قبل"); sys.exit()
k1 = "class OpusFrame : public AudioDecoder::EncodedAudioFrame {"
k2 = "    return (ret < 0) ? 0 : static_cast<size_t>(ret);\n  }\n\n  bool IsDtxPacket()"
print("مطابقات:", s.count(k1), s.count(k2))
if s.count(k1) != 1 or s.count(k2) != 1:
    print("ما عدّلت شي"); sys.exit()
s = s.replace(k1, "#include <atomic>\n#include <android/log.h>\n\n" + k1, 1)
log = r'''    static std::atomic<int> __lastDur{-1};
    if (ret >= 0 && is_primary_payload_ && __lastDur.exchange(ret) != ret) {
      __android_log_print(ANDROID_LOG_WARN, "AudioPktDur", "opus packet samples=%d ms=%d", ret, ret / 48);
    }
'''
s = s.replace(k2, log + k2, 1)
open(h, "w", encoding="utf-8").write(s)
print("تم")
