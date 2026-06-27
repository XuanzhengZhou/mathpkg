---
role: proof
locale: en
of_concept: dedekind-domain-noetherian-characterization
source_book: gtm028
source_chapter: "V"
source_section: "6"
---

The necessity of 1) follows from Theorem 11 and Lemma 3, and that of 2) from Theorem 10.

As for 3), consider an element $x$ of the quotient field $K$ of $R$ which is integral over $R$. There exists a common denominator $d \neq 0$ in $R$ such that $dx^n \in R$ for every $n \geq 0$. Then, for every prime ideal $\mathfrak{p}$ in $R$, we have $v_{\mathfrak{p}}(dx^n) = v_{\mathfrak{p}}(d) + n v_{\mathfrak{p}}(x) \geq 0$ for every $n$. As $v_{\mathfrak{p}}(d)$ and $v_{\mathfrak{p}}(x)$ are ordinary integers, this implies $v_{\mathfrak{p}}(x) \geq 0$, that is, $v_{\mathfrak{p}}(Rx) \geq 0$ for every prime ideal $\mathfrak{p}$; that is, $x \in R$. Thus $R$ is integrally closed.

For proving the converse, we first observe that, in the proof of Theorem 12, the assumption that every ideal in $R$ is invertible has been used only for the purpose of establishing that $R$ is noetherian, while the rest of the proof was based exclusively on the established fact that $R$ is noetherian and on the assumption that every proper prime ideal is invertible; in fact, in that proof we only needed the fact that the maximal ideal $\mathfrak{m}$ is invertible. Since, in the present case, we are given that $R$ is noetherian, it follows that in order to prove that $R$ is a Dedekind domain, we have only to show that every proper prime ideal $\mathfrak{p}$ of $R$ is invertible. We observe that if $y$ is some non-zero element of $\mathfrak{p}$, then $\mathfrak{p}$ must contain some prime ideal of the principal ideal $Ry$, and hence $\mathfrak{p}$ itself must be a prime ideal of $Ry$. The rest of the proof proceeds via Theorem 14 and Lemma 6 to establish the invertibility of $\mathfrak{p}$.
