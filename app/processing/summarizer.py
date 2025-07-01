from transformers import pipeline
import logging
import os
from dotenv import load_dotenv
load_dotenv()

# pipe = pipeline("summarization", model="ARTeLab/it5-summarization-ilpost")
pipe = pipeline("summarization", model="flax-community/t5-base-cnn-dm", device=0)

## Note for me: device = 0 for gpu and -1 for cpu

ARTICLE = """ New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.
A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband.
Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other.
In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it was her "first and only" marriage.
Barrientos, now 39, is facing two criminal counts of "offering a false instrument for filing in the first degree," referring to her false statements on the
2010 marriage license application, according to court documents.
Prosecutors said the marriages were part of an immigration scam.
On Friday, she pleaded not guilty at State Supreme Court in the Bronx, according to her attorney, Christopher Wright, who declined to comment further.
After leaving court, Barrientos was arrested and charged with theft of service and criminal trespass for allegedly sneaking into the New York subway through an emergency exit, said Detective
Annette Markowski, a police spokeswoman. In total, Barrientos has been married 10 times, with nine of her marriages occurring between 1999 and 2002.
All occurred either in Westchester County, Long Island, New Jersey or the Bronx. She is believed to still be married to four men, and at one time, she was married to eight men at once, prosecutors say.
Prosecutors said the immigration scam involved some of her husbands, who filed for permanent residence status shortly after the marriages.
Any divorces happened only after such filings were approved. It was unclear whether any of the men will be prosecuted.
The case was referred to the Bronx District Attorney\'s Office by Immigration and Customs Enforcement and the Department of Homeland Security\'s
Investigation Division. Seven of the men are from so-called "red-flagged" countries, including Egypt, Turkey, Georgia, Pakistan and Mali.
Her eighth husband, Rashid Rajput, was deported in 2006 to his native Pakistan after an investigation by the Joint Terrorism Task Force.
If convicted, Barrientos faces up to four years in prison.  Her next court appearance is scheduled for May 18.
"""
# print(pipe(ARTICLE, max_length=130, min_length=30, do_sample=False))
# print(pipe(ARTICLE))

def summarize_news(news):
    
    summarized = []

    for article in news:
        content = article.get('content')
        if not content:  # skip if content is None or empty
            continue
        
        try:
            summary = pipe(content, max_new_tokens=80, min_length=30, do_sample=False)
            article['summary'] = summary[0]['summary_text']
            summarized.append(article)
        except Exception as e:
            logging.warning(f"Failed to summarize article: {article.get('title')} — {e}")
    logging.warning(f"Summarized {len(news)} articles")
    
    return summarized