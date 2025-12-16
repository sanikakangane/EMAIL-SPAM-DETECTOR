import csv
import time
import json
import matplotlib.pyplot as plt

# -------------------------------------------------
# Clean text helper
# -------------------------------------------------
def clean_text(text):
    text = text.lower()
    return "".join(ch if ch.isalnum() or ch.isspace() else " " for ch in text)

# -------------------------------------------------
# Decorator to log execution time
# -------------------------------------------------
def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        output = func(*args, **kwargs)
        end = time.time()
        print(f"[LOG] {func.__name__} took {end - start:.4f} seconds")
        return output
    return wrapper

# -------------------------------------------------
# Export report
# -------------------------------------------------
def export_report(results, filename="spam_report.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["sender", "subject", "spam_score", "is_spam"])
        writer.writeheader()
        writer.writerows(results)

# -------------------------------------------------
# Visualization
# -------------------------------------------------
def visualize_data(keyword_counts, spam_count, ham_count):
    # Bar Chart
    plt.figure(figsize=(8, 4))
    plt.bar(keyword_counts.keys(), keyword_counts.values())
    plt.xlabel("Keyword")
    plt.ylabel("Frequency")
    plt.title("Top Spam Keywords")
    plt.show()

    # Pie Chart
    plt.figure(figsize=(6, 6))
    plt.pie([spam_count, ham_count], labels=["Spam", "Not Spam"], autopct="%1.1f%%")
    plt.title("Spam vs Ham Distribution")
    plt.show()
