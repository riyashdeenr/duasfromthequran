#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

# Read the file
with open('prayers_with_arabic.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replacement dictionary for corrupted entries
replacements = {
    # 2:260 - replace the corrupted Arabic portion
    r'(<td>2:260</td>.*?<span class="arabic" dir="rtl">).*?(</span><span class="translation">)': 
        r'\1وَإِذْ قَالَ إِبْرَاهِيمُ رَبِّ أَرِنِي كَيْفَ تُحْيِي الْمَوْتَىٰ ۖ قَالَ أَوَلَمْ تُؤْمِن ۖ قَالَ بَلَىٰ وَلَكِن لِّيَطْمَئِنَّ قَلْبِي ۖ قَالَ فَخُذْ أَرْبَعَةً مِّنَ الطَّيْرِ فَصُرْهُنَّ إِلَيْكَ ثُمَّ اجْعَلْ عَلَىٰ كُلِّ جَبَلٍ مِنْهُنَّ جُزْءًا ثُمَّ ادْعُهُنَّ يَأْتِينَكَ سَعْيًا ۚ وَاعْلَمْ أَنَّ اللَّهَ عَزِيزٌ حَكِيمٌ\2',
    
    # 2:285 - replace the corrupted Arabic portion
    r'(<td>2:285</td>.*?<span class="arabic" dir="rtl">).*?(</span><span class="translation">)':
        r'\1آمَنَ الرَّسُولُ بِمَا أُنزِلَ إِلَيْهِ مِن رَّبِّهِ وَالْمُؤْمِنُونَ ۚ كُلٌّ آمَنَ بِاللَّهِ وَمَلَائِكَتِهِ وَكُتُبِهِ وَرُسُلِهِ لَا نُفَرِّقُ بَيْنَ أَحَدٍ مِّن رُّسُلِهِ ۚ وَقَالُوا۟ سَمِعْنَا وَأَطَعْنَا ۖ غُفْرَانَكَ رَبَّنَا وَإِلَيْكَ الْمَصِيرُ\2',
    
    # 2:286 - replace the corrupted Arabic portion  
    r'(<td>2:286</td>.*?<span class="arabic" dir="rtl">).*?(</span><span class="translation">)':
        r'\1لَا يُكَلِّفُ اللَّهُ نَفْسًا إِلَّا وُسْعَهَا ۚ لَهَا مَا كَسَبَتْ وَعَلَيْهَا مَا اكْتَسَبَتْ ۗ رَبَّنَا لَا تُؤَاخِذْنَا إِن نَّسِينَا أَوْ أَخْطَأْنَا ۚ رَبَّنَا وَلَا تَحْمِلْ عَلَيْنَا إِصْرًا كَمَا حَمَلْتَهُ عَلَى الَّذِينَ مِن قَبْلِنَا ۚ رَبَّنَا وَلَا تُحَمِّلْنَا مَا لَا طَاقَةَ لَنَا بِهِ ۖ وَاعْفُ عَنَّا وَاغْفِرْ لَنَا وَارْحَمْنَا ۚ أَنتَ مَوْلَانَا فَانصُرْنَا عَلَى الْقَوْمِ الْكَافِرِينَ\2',
}

# Apply replacements
for pattern, replacement in replacements.items():
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write the file back
with open('prayers_with_arabic.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File updated successfully!")
