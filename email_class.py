import re
import json
from spam_utils import clean_text, log_time


class Email:
    def __init__(self, sender, subject, body):
        self.sender = sender
        self.subject = subject
        self.body = body
        self.spam_score = 0
        self.is_spam = False

    # -----------------------------------
    # Analyze Email
    # -----------------------------------
    @log_time
    def analyze_email(self, spam_keywords, blacklist_senders):
        cleaned_subject = clean_text(self.subject)
        cleaned_body = clean_text(self.body)

        # Keyword rule
        keyword_hits = sum(1 for word in spam_keywords if word in cleaned_body)

        # Blacklist rule
        sender_hit = 1 if self.sender in blacklist_senders else 0

        # Total score
        self.spam_score = (keyword_hits * 2) + (sender_hit * 3)

        # Threshold
        self.is_spam = self.spam_score >= 3

    # -----------------------------------
    # Export analysis summary
    # -----------------------------------
    def to_dict(self):
        return {
            "sender": self.sender,
            "subject": self.subject,
            "spam_score": self.spam_score,
            "is_spam": self.is_spam
        }
