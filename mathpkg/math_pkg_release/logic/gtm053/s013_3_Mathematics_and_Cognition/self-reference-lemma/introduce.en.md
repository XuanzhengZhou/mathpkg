---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Self-Reference Lemma (also known as the Diagonal Lemma or Fixed-Point Lemma) is the key technical tool underlying both Tarski's theorem on the undefinability of truth and Godel's incompleteness theorems. It states that for any formula $P(x)$ with one free variable, one can effectively construct a sentence $Q_P$ that asserts "I do not satisfy $P$." The construction uses the definability of the diagonal function $y = \operatorname{diag} x$, which maps the Godel number of a formula $\phi(x)$ to the Godel number of $\phi(\overline{N}(\phi(x)))$. This self-referential ability is what allows formal systems to reason about their own provability and truth predicates.
