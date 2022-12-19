prompt = """
Generate a {num_words} word book summary about "{title}" by {authors} in JSON format. Keep each sentence crisp and concise.

Include the following sections:

- title
- genre as per Goodreads
- A no bullshit pitch of the book in 1 line
- 3 key takeaways => in a list (one sentence = one takeaway)
- 3 ways to implement it in your life with examples in a list (one sentence = one way)
- 1 counterpoint

Highlight using markdown any word or phrase which should be highlight-worthy.
After generating the response, make sure that it's a valid JSON.

"""

template = """
Use this JSON template within a code-block:
```{
"title": {book title only},
"authors": {author names separated by commas},
"genre": {book genres separated by commas},
"sections": [
{"name": "1 core idea", "body": ["{no bullshit pitch of the book in 1 line}"]},
{"name": "3 key takeaways", "body": ["{take-away1}","{take-away2}","{take-away3}"]},
{"name": "3 ways to implement it in your life", "body": ["{way1 with example}","{way2 with example}","{way3 with example}"]},
{"name": "1 counterpoint", "body": ["{counter-point}"]},
{"name": "2 related books", "body": ["{**related-book1** by {author(s)} - this book also...}","{**related-book2** by {author(s)} - this book also...}"]}]
}
```
"""
