---
role: proof
locale: en
of_concept: root-test-for-series
source_book: gtm012
source_chapter: "4"
source_section: "4. Series"
---

# Proof of Root test for series (Proposition 4.5)

**Proposition 4.5 (Root test).** Suppose $(z_n)_{n=1}^{\infty}$ is a sequence in $\mathbb{C}$. Assume that the sequence $(|z_n|^{1/n})_{n=1}^{\infty}$ is bounded (so that its $\limsup$ and $\liminf$ exist).

(a) If $\limsup |z_n|^{1/n} < 1$, then $\sum z_n$ converges (absolutely).

(b) If $\limsup |z_n|^{1/n} > 1$, then $\sum z_n$ diverges.

**Proof.**

**(a)** Take $r$ such that $\limsup |z_n|^{1/n} < r < 1$. By Proposition 3.4 (characterization of $\limsup$), there exists $N$ such that $|z_n|^{1/n} \leq r$ for all $n \geq N$. Thus $|z_n| \leq r^n$ for all $n \geq N$. Since $0 < r < 1$, the geometric series $\sum r^n$ converges. By Proposition 4.3 (comparison test), $\sum |z_n|$ converges, hence $\sum z_n$ converges absolutely.

**(b)** In this case, $\limsup |z_n|^{1/n} > 1$. By Proposition 3.4, this means that $|z_n|^{1/n} \geq 1$ for infinitely many values of $n$, i.e., $|z_n| \geq 1$ for infinitely many $n$. Thus $z_n \not\to 0$. By Proposition 4.1 (if $\sum z_n$ converges then $z_n \to 0$), the series $\sum z_n$ diverges.

**Note on the boundedness assumption.** The statement and proof tacitly assume that $(|z_n|^{1/n})_{n=1}^{\infty}$ is a bounded sequence, so that the upper and lower limits exist. However, if this sequence is not bounded, then in particular $|z_n| \geq 1$ for infinitely many values of $n$, and Proposition 4.1 again implies divergence. So the boundedness hypothesis does not restrict the applicability of the test. $\square$
