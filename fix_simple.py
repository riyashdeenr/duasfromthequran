#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Read the HTML file
with open('prayers_with_arabic.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the three replacements
replacements = {
    # 2:260
    '2:260</td><td><details><summary>Prayer of Ibrāhīm(Abraham) عليه السلام #1</summary><div class="details-content"><span class="arabic" dir="rtl">': 
    '2:260</td><td><details><summary>Prayer of Ibrāhīm(Abraham) عليه السلام #1</summary><div class="details-content"><span class="arabic" dir="rtl">وإذ قال إبراهيم رب أرني كيف تحيي الموتى ۖ قال أولم تؤمن ۖ قال بلى ولكن ليطمئن قلبي ۖ قال فخذ أربعة من الطير فصرهن إليك ثم اجعل على كل جبل منهن جزءا ثم ادعهن يأتينك سعيا ۚ واعلم أن الله عزيز حكيم',
}

# Try to find and replace line 104 (2:260) - simpler approach
lines = content.split('\n')
for i, line in enumerate(lines):
    if i == 103:  # Line 104 (0-indexed)
        if '2:260' in line:
            # Extract the part before and after the span content
            start = line.find('<span class="arabic" dir="rtl">') + len('<span class="arabic" dir="rtl">')
            end = line.find('</span><span class="translation">')
            if start > -1 and end > -1:
                lines[i] = line[:start] + 'وإذ قال إبراهيم رب أرني كيف تحيي الموتى ۖ قال أولم تؤمن ۖ قال بلى ولكن ليطمئن قلبي ۖ قال فخذ أربعة من الطير فصرهن إليك ثم اجعل على كل جبل منهن جزءا ثم ادعهن يأتينك سعيا ۚ واعلم أن الله عزيز حكيم' + line[end:]
    elif i == 104:  # Line 105 (0-indexed)
        if '2:285' in line:
            start = line.find('<span class="arabic" dir="rtl">') + len('<span class="arabic" dir="rtl">')
            end = line.find('</span><span class="translation">')
            if start > -1 and end > -1:
                lines[i] = line[:start] + 'آمن الرسول بما أنزل إليه من ربه والمؤمنون ۚ كل آمن بالله وملائكته وكتبه ورسله لا نفرق بين أحد من رسله ۚ وقالوا سمعنا وأطعنا ۖ غفرانك ربنا وإليك المصير' + line[end:]
    elif i == 105:  # Line 106 (0-indexed)
        if '2:286' in line:
            start = line.find('<span class="arabic" dir="rtl">') + len('<span class="arabic" dir="rtl">')
            end = line.find('</span><span class="translation">')
            if start > -1 and end > -1:
                lines[i] = line[:start] + 'لا يكلف الله نفسا إلا وسعها ۚ لها ما كسبت وعليها ما اكتسبت ۗ ربنا لا تؤاخذنا إن نسينا أو أخطأنا ۚ ربنا ولا تحمل علينا إصرا كما حملته على الذين من قبلنا ۚ ربنا ولا تحملنا ما لا طاقة لنا به ۖ واعف عنا واغفر لنا وارحمنا ۚ أنت مولانا فانصرنا على القوم الكافرين' + line[end:]

# Write back
with open('prayers_with_arabic.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print("Fixed!")
