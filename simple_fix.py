#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read the HTML file
with open('prayers_with_arabic.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Replace line 105 (index 104) - the entire line
lines[104] = '      <tr><td>2:285</td><td><details><summary>Prayer of Believers #1</summary><div class="details-content"><span class="arabic" dir="rtl">آمن الرسول بما أنزل إليه من ربه والمؤمنون ۚ كل آمن بالله وملائكته وكتبه ورسله لا نفرق بين أحد من رسله ۚ وقالوا سمعنا وأطعنا ۖ غفرانك ربنا وإليك المصير</span><span class="translation">The Messenger ˹firmly˺ believes in what has been revealed to him from his Lord, and so do the believers. They ˹all˺ believe in Allah, His angels, His Books, and His messengers. ˹They proclaim,˺ "We make no distinction between any of His messengers." And they say, "We hear and obey. ˹We seek˺ Your forgiveness, our Lord! And to You ˹alone˺ is the final return."</span><a class="quran-link" href="https://quran.com/2/285" target="_blank">Read on Quran.com →</a></div></details></td></tr>\n'

# Write back to file
with open('prayers_with_arabic.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Done! Line 105 replaced successfully.")
