---
role: proof
locale: en
of_concept: structure-theorem-indefinite-type-i
source_book: gtm007
source_chapter: "V"
source_section: "1"
---

We use induction on $n$. Let $E \in S_n$ with $E$ indefinite and of type I. By Lemma 4, $E \simeq I_+ \oplus I_- \oplus F$. If $n = 2$, we have $F = 0$ and the result holds with $s = t = 1$. For $n > 2$, $F \in S_{n-2}$ is also indefinite and of type I (since $E$ and $I_+ \oplus I_-$ are), so by the induction hypothesis $F \simeq s' I_+ \oplus t' I_-$. Then

$$E \simeq I_+ \oplus I_- \oplus (s' I_+ \oplus t' I_-) = (s'+1)I_+ \oplus (t'+1)I_-,$$

completing the induction. Thus every indefinite type I element of $S_n$ is isomorphic to $s I_+ \oplus t I_-$ for some $s, t \geq 0$ with $s + t = n$.
