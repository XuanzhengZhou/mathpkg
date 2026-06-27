---
role: proof
locale: en
of_concept: multiplication-formula
source_book: gtm095
source_chapter: "1"
source_section: "4"
---

# Proof of the Multiplication Formula for Probabilities

From the definition of conditional probability (with $P(A) > 0$), we immediately obtain

$$P(AB) = P(B \mid A) \, P(A). \tag{5}$$

This is the multiplication formula for two events.

To generalize to $n$ events, we proceed by induction. Suppose that for $n-1$ events $A_1, \ldots, A_{n-1}$ with $P(A_1 \cdots A_{n-1}) > 0$, we have

$$P(A_1 \cdots A_{n-1}) = P(A_1) \, P(A_2 \mid A_1) \, P(A_3 \mid A_1 A_2) \cdots P(A_{n-1} \mid A_1 \cdots A_{n-2}).$$

Now consider $n$ events $A_1, \ldots, A_n$ with $P(A_1 \cdots A_{n-1}) > 0$. Applying formula (5) to the intersection $A_1 \cdots A_{n-1}$ (playing the role of $A$) and $A_n$ (playing the role of $B$), we obtain

$$P(A_1 \cdots A_n) = P(A_n \mid A_1 \cdots A_{n-1}) \, P(A_1 \cdots A_{n-1}).$$

Substituting the induction hypothesis for $P(A_1 \cdots A_{n-1})$ yields the general **multiplication formula** (also called the chain rule):

$$P(A_1 A_2 \cdots A_n) = P(A_1) \, P(A_2 \mid A_1) \, P(A_3 \mid A_1 A_2) \cdots P(A_n \mid A_1 \cdots A_{n-1}).$$
