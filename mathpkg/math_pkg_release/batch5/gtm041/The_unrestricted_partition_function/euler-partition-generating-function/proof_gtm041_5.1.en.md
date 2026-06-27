---
role: proof
locale: en
of_concept: euler-partition-generating-function
source_book: gtm041
source_chapter: "5"
source_section: "5.1"
---

The proof is given in Chapter 14 of [4] (Apostol, *Introduction to Analytic Number Theory*).

For each factor in the product, expand as a geometric series:

$$\frac{1}{1-x^m} = \sum_{k_m=0}^{\infty} x^{m k_m}.$$

Then the product becomes

$$\prod_{m=1}^{\infty} \frac{1}{1-x^m} = \prod_{m=1}^{\infty} \sum_{k_m=0}^{\infty} x^{m k_m} = \sum_{k_1=0}^{\infty} \sum_{k_2=0}^{\infty} \cdots x^{1 \cdot k_1 + 2 \cdot k_2 + 3 \cdot k_3 + \cdots}.$$

A given exponent $n$ arises whenever $n = k_1 + 2k_2 + 3k_3 + \cdots$, which corresponds to a partition of $n$ with $k_m$ parts equal to $m$. Since the $k_m$ are independent and the order of terms is irrelevant, each partition of $n$ contributes exactly 1 to the coefficient of $x^n$. The series converges absolutely for $|x| < 1$ because $p(n)$ grows subexponentially.
