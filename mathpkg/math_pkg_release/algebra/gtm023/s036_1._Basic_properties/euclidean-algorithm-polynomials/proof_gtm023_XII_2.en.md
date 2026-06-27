---
role: proof
locale: en
of_concept: euclidean-algorithm-polynomials
source_book: gtm023
source_chapter: "XII"
source_section: "2"
---

Let $\deg f = n$ and $\deg g = m$. If $m > n$, write $f = g \cdot 0 + f$ and the lemma holds with $r = f$ ($\deg f = n < m$). Now consider $n \geq m$. Assume without loss of generality that $f$ and $g$ are monic. Then
$$f = t^{n-m}g + f_1, \quad \deg f_1 < n \text{ or } f_1 = 0.$$
If $f_1 = 0$, we are done with $q = t^{n-m}$, $r = 0$. If $f_1 \neq 0$, assume by induction on $n$ that the lemma holds for $f_1$: $f_1 = gq_1 + r_1$ where $\deg r_1 < \deg g$ or $r_1 = 0$. Then
$$f = t^{n-m}g + gq_1 + r_1 = (t^{n-m} + q_1)g + r_1$$
and the lemma follows by induction.
