from gtts import gTTS # gTTS means Google text-to-speech

import os 
"""os means provides functions for creating and removing a directory (folder), fetching its contents,
      changing and identifying the current directory"""


# text is the our input text

text ="On this page you will find our complete list of high quality reading comprehension worksheets created specially by our team for students in grade levels K-12. Our worksheets elicit the use of critical thinking skills at every level. While some questions ask the reader to peruse the passage for particular details, most questions involve the use of deductive reasoning, conclusion making, logical inference, sequential analysis, tonal awareness, and an understanding of scope. These materials are highly effective in supplementing the education of verbal reasoning and critical thinking skills on behalf of the reader. What is more, these materials are applicable for students of all ages and ability levels. Many of the resources found on this page are available in online quiz form at our sister site, ReadTheory."

language='en'  #selecting the language is english 

obj=gTTS(text= text,lang=language,slow=False)

obj.save("Vc.mp3")  # saving the output file as the audio file

os.system("Vc.mp3")