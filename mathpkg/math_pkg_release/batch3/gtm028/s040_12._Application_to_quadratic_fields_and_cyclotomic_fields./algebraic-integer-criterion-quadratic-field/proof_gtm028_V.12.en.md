---
role: proof
locale: en
of_concept: algebraic-integer-criterion-quadratic-field
source_book: gtm028
source_chapter: "V"
source_section: "12"
---

For $x = a + be$ to be an algebraic integer, it is necessary and sufficient that its trace $2a$ and its norm $a^2 - mb^2$ be ordinary integers. This follows from the general criterion that an element is an algebraic integer if and only if its minimal polynomial over $\mathbb{Q}$ has integer coefficients.

Write $a = \frac{1}{2}a'$ where $a'$ is an integer (since $2a$ must be an integer). The condition that $a^2 - mb^2$ be an integer implies that $mb^2$ has denominator dividing $4$ (since $a^2 = a'^2/4$). Thus $(2b)^2 m$ must be an integer. Since $m$ is square-free, $2b$ must be an integer, so we may write $b = \frac{1}{2}b'$ where $b'$ is an integer.

Substituting these expressions into the norm condition:
$$a^2 - mb^2 = \frac{a'^2}{4} - m\frac{b'^2}{4} = \frac{a'^2 - mb'^2}{4}.$$
For this to be an integer, we must have $a'^2 - mb'^2 \equiv 0 \pmod{4}$.

Now consider the two cases:
\begin{itemize}
\item If $m \equiv 1 \pmod{4}$: the condition $a'^2 - mb'^2 \equiv 0 \pmod{4}$ becomes $a'^2 - b'^2 \equiv 0 \pmod{4}$, which is equivalent to $a' \equiv b' \pmod{2}$. In this case the algebraic integers are precisely $\frac{1}{2}(a' + b'e)$ with $a' \equiv b' \pmod{2}$, i.e., with $a', b'$ both even or both odd. A basis of the ring of integers over $\mathbb{Z}$ is $\{1, \frac{1}{2}(1+e)\}$.
\item If $m \equiv 2 \pmod{4}$ or $m \equiv 3 \pmod{4}$: the condition $a'^2 - mb'^2 \equiv 0 \pmod{4}$ forces $a' \equiv b' \equiv 0 \pmod{2}$ (since otherwise the left side would be odd modulo 4). Thus $a$ and $b$ are integers, and the algebraic integers are of the form $a + be$ with $a, b \in \mathbb{Z}$. A basis of the ring of integers over $\mathbb{Z}$ is $\{1, e\}$.
\end{itemize}
