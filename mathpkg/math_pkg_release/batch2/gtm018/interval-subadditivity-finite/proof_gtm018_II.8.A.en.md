---
role: proof
locale: en
of_concept: interval-subadditivity-finite
source_book: gtm018
source_chapter: "II"
source_section: "8"
---

We write $E_i = [a_i, b_i)$, $i = 0, 1, \dots, n$, and, without any loss of generality, we assume that

$$a_1 \leq \dots \leq a_n.$$

It follows from the assumed properties of $\{E_1, \dots, E_n\}$ that

$$a_0 \leq a_1 \leq b_1 \leq \dots \leq a_n \leq b_n \leq b_0,$$

and therefore

$$\sum_{i=1}^{n} \mu(E_i) = \sum_{i=1}^{n} (b_i - a_i) \leq$$

$$\leq \sum_{i=1}^{n} (b_i - a_i) + \sum_{i=1}^{n-1} (a_{i+1} - b_i) = b_n - a_1 \leq b_0 - a_0 = \mu(E_0).$$
