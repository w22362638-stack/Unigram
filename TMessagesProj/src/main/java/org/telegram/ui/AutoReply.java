package org.telegram.ui;

import java.util.regex.*;

public class AutoReply {
    public static boolean enabled = false;
    private static final Pattern WORD = Pattern.compile("123\\s*(\\S+)");

    public static String extract(String t) {
        if (!enabled || t == null) return null;
        Matcher m = WORD.matcher(t);
        if (m.find()) return m.group(1);
        return null;
    }
}
