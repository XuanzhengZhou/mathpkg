---
role: proof
locale: en
of_concept: fundamental-pair-lemma
source_book: gtm041
source_chapter: "2"
source_section: "2.3"
---

**Proof.** We arrange the elements of $\Omega$ in a sequence according to increasing distances from the origin, say
$$\Omega = \{0, w_1, w_2, \ldots\}$$
where
$$0 < |w_1| \leq |w_2| \leq \cdots \quad \text{and} \quad \arg w_n < \arg w_{n+1} \text{ if } |w_n| = |w_{n+1}|.$$

Let $\omega_1 = w_1$ and let $\omega_2$ be the first member of this sequence that is not a multiple of $\omega_1$. Then the triangle with vertices $0, \omega_1, \omega_2$ contains no element of $\Omega$ except the vertices, so $(\omega_1, \omega_2)$ is a fundamental pair which spans the set $\Omega$. Therefore there exist integers $a, b, c, d$ with $ad - bc = \pm 1$ such that
$$\begin{pmatrix} \omega_2 \\ \omega_1 \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} \omega_2' \\ \omega_1' \end{pmatrix}.$$

If $ad - bc = -1$ we can replace $c$ by $-c$, $d$ by $-d$, and $\omega_1$ by $-\omega_1$ and the same equation holds, except now $ad - bc = 1$. Because of the way we have chosen $\omega_1, \omega_2$ we have
$$|\omega_2| \geq |\omega_1| \quad \text{and} \quad |\omega_1 \pm \omega_2| \geq |\omega_2|,$$
since $\omega_1 \pm \omega_2$ are periods in $\Omega$ occurring later than $\omega_2$ in the sequence. $\square$
