import os
import string
from collections import Counter

FILENAME = "sample.txt"
REPORT_FILE = "word_count_report.txt"

if not os.path.exists(FILENAME):
    text = input("sample.txt not found! Please enter a paragraph: ")
    with open(FILENAME, "w") as file:
        file.write(text)
    print("File created!\n")

with open(FILENAME, "r") as file:
    text = file.read().strip().lower()

text = text.translate(str.maketrans("", "", string.punctuation))
words = text.split()

word_counts = Counter(words)
total_words = sum(word_counts.values())
top_words = word_counts.most_common(5)

print(f"\nTotal words: {total_words}")
print("Top 5 most common words:")
for word, count in top_words:
    print(f"{word} - {count} {'times' if count > 1 else 'time'}")

with open(REPORT_FILE, "w") as report:
    report.write(f"Word Count Report\nTotal Words: {total_words}\nTop 5 Words:\n")
    for word, count in top_words:
        report.write(f"{word} - {count}\n")

print(f"\nReport saved in {REPORT_FILE}")
