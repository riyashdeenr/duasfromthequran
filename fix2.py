import os
print("Current directory:", os.getcwd())
print("File exists:", os.path.exists('prayers_with_arabic.html'))

# Read the HTML file
with open('prayers_with_arabic.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace line 105 content
old_text = 'ءَامَنَ ٱlrَّsُولُ بِمَآ أُndzِلَ إِلَيْهِ مِن rَّbِّهِۦ وَٱlْمُؤْمِنُونَ ۚ كُلٌّ ءَامَنَ بِٱllَّهِ وَməlَـٰٓئِkَتِهِۦ وَkُtُbِهِۦ وَrُsُلِهِۦ lَا nُfَرِّqُ بَيْنَ أَḥədٍۢ mِّن rُّsُلِهِۦ ۚ وَqَالُوا۟ sَمِعْنَا وَأَṭَْعْنَا ۖ غُfْرَانَكَ rَبَّnَا وَإِلَيْكَ ٱlْمَصِيرُ'
new_text = 'آمن الرسول بما أنزل إليه من ربه والمؤمنون ۚ كل آمن بالله وملائكته وكتبه ورسله لا نفرق بين أحد من رسله ۚ وقالوا سمعنا وأطعنا ۖ غفرانك ربنا وإليك المصير'

if old_text in content:
    content = content.replace(old_text, new_text, 1)  # Replace only first occurrence
    with open('prayers_with_arabic.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully replaced!")
else:
    print("Old text not found")
    print("First 500 chars:", content[2500:3000])
