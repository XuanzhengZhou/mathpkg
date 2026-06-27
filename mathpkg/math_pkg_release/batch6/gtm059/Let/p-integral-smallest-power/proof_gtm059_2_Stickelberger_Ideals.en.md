---
role: proof
locale: en
of_concept: p-integral-smallest-power
source_book: gtm059
source_chapter: "2"
source_section: "Stickelberger Ideals and Bernoulli Distribution"
---

The argument uses the expression for the Bernoulli polynomial as in the previous lemma. We see that
$$p \sum_{i=1}^{k-1} \binom{k}{i} \binom{k}{i-1} p^{i-1} = p \text{ integral}.$$

The leading term is $p^{10} N^e$. The Bernoulli numbers $B_i$ are $p$-integral for $i < p$ by Kummer's criterion, and for $i \geq p$ the power $N^{i-1}$ in front makes $(1/N)^{i-1}$ integral, from which it follows that
$$\frac{N^{i-1}}{N} p^{i-1} = p \text{ integral},$$
whence $s$ has the stated value. We can write an element of $I$ in the form $c = 1 \bmod N$ and $c = 0 \bmod 1$ for any prime to see that $I \cap \mathbb{Z}$ contains elements prime to $L$. This proves the lemma.
