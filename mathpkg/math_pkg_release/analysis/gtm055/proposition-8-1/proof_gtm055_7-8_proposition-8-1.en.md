---
role: proof
locale: en
of_concept: proposition-8-1
source_book: gtm055
source_chapter: "7-8"
source_section: "Section 09_Section_9"
---

Proof. If $\mu(A) = +\infty$ and $A$ is an atom with respect to $\mu$, then $\mu(F) < +\infty$ and $F \subset A$ imply $\mu(F) = 0$, so $\mu$ is certainly not locally finite. Suppose, in the converse direction, that $\mu$ fails to be locally finite. Then there exists a measurable set $E_0$ such that $\mu(E_0) = +\infty$ and such that

$$M = \sup \{ \mu(F) : F \in \mathbf{S}, F \subset E_0, \mu(F) < +\infty \} < +\infty.$$

Let $\{F_n\}_{n=1}^{\infty}$ be a sequence of measurable subsets of $E_0$ of finite measure such that $\mu(F_n) \to M$, and set $E_n = F_1 \cup \cdots \cup F_n$. Then $\mu(F_n) \leq \mu(E_n) < +\infty$ for each $n$, whence it follows at once that $\{\mu(E_n)\}$ also tends to $M$. But then, if $F_0 = \bigcup_{n=1}^{\infty} F_n = \bigcup_{n=1}^{\infty} E_n$, we have $\mu(F_0) = M$. Set $A = E_0 \setminus F_0$, and suppose $F$ is a measurable subset of $A$

defines a linear functional $L_0$ on $\mathcal{L}_0$. Moreover, it is a routine chore to verify that $L_0$ is a Lebesgue integral on $(Y, \mathbf{T})$. The measure $\nu$ associated with the integral $L_0$ is called the measure induced on $Y$ by $\Phi$ and $\mu$.
