import csv
import json
from email_class import Email
from spam_utils import export_report, visualize_data


def load_spam_keywords():
    with open("spam_keywords.json") as f:
        data = json.load(f)
        return data["keywords"], data["blacklist_senders"]


def load_emails():
    emails = []
    with open("emails.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            emails.append(Email(row["sender"], row["subject"], row["body"]))
    return emails


if __name__ == "__main__":
    spam_keywords, blacklist = load_spam_keywords()
    emails = load_emails()

    results = []
    keyword_count = {word: 0 for word in spam_keywords}
    spam_count = ham_count = 0

    for mail in emails:
        mail.analyze_email(spam_keywords, blacklist)

        # Count spam/ham
        if mail.is_spam:
            spam_count += 1
        else:
            ham_count += 1

        # Count keyword frequency
        for word in spam_keywords:
            if word in mail.body.lower():
                keyword_count[word] += 1

        results.append(mail.to_dict())

    # Export report
    export_report(results)

    # Show visual charts
    visualize_data(keyword_count, spam_count, ham_count)

    print("\nSpam Report Generated: spam_report.csv")
