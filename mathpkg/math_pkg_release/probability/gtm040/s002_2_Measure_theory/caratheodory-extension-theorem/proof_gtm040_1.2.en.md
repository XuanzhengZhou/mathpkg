---
role: proof
locale: en
of_concept: caratheodory-extension-theorem
source_book: gtm040
source_chapter: "1"
source_section: "2"
---
The proof proceeds via outer measure construction. Define for any subset $A \subset X$,
$$\mu(A) = \inf \left\{ \sum_n \nu(C_n) : C_n \in \mathcal{F}, A \subset \bigcup_n C_n \right\}.$$
By Lemmas 1-20 and 1-21, $\mu$ is an outer measure. Define the symmetric difference metric $d(A,B) = \mu(A \oplus B)$. Let $\mathcal{F}^*$ be the class of sets $A$ for which there exists a sequence $\{A_n\}$ in $\mathcal{F}$ with $d(A_n, A) \to 0$, and let $\mathcal{G}^*$ be the class of sets that are countable unions of sets in $\mathcal{F}^*$. Lemma 1-29 establishes that $\mu$ is completely additive on $\mathcal{G}^*$ and $\mathcal{G}^*$ is a Borel field. Since $\mathcal{G}^*$ is a Borel field containing $\mathcal{F}$, it contains $\mathcal{G}$, the smallest Borel field containing $\mathcal{F}$. The extended measure restricted to $\mathcal{G}$ satisfies the requirements. Uniqueness follows via sigma-finiteness: write $X = \bigcup_n B_n$ with $B_n \in \mathcal{F}$ of finite measure. For any $C \in \mathcal{G}$ and any alternative extension $\mu'$ agreeing with $\nu$ on $\mathcal{F}$, we have $\mu'(C) \leq \mu(C)$ by the outer measure infimum bound. Applying this inequality to both $C \cap B_n$ and $\tilde{C} \cap B_n$ and using $\mu'(C \cap B_n) + \mu'(\tilde{C} \cap B_n) = \nu(B_n) = \mu(C \cap B_n) + \mu(\tilde{C} \cap B_n)$ yields equality, since all terms are finite.
