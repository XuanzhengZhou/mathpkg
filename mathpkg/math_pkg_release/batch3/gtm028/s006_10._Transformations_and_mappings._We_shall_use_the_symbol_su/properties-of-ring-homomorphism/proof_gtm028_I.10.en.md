---
role: proof
locale: en
of_concept: properties-of-ring-homomorphism
source_book: gtm028
source_chapter: "I"
source_section: "10. Transformations and mappings"
---

**Proof.** (a) Since $T$ is a homomorphism of the additive groups, we have $0T = \bar{0}$ and $(-a)T = -(aT)$ by the corresponding group-theoretic facts.

(b) $RT$ is the image of $R$ under $T$. For any $\bar{a}, \bar{b} \in RT$, there exist $a, b \in R$ with $aT = \bar{a}, bT = \bar{b}$. Then $\bar{a} - \bar{b} = aT - bT = (a-b)T \in RT$ and $\bar{a}\bar{b} = (aT)(bT) = (ab)T \in RT$, showing $RT$ is closed under subtraction and multiplication, hence a subring of $\bar{R}$.

(c) The kernel $N = \{a \in R : aT = \bar{0}\}$ is the kernel of the additive group homomorphism, hence an additive subgroup. If $a, b \in N$, then $(ab)T = (aT)(bT) = \bar{0} \cdot \bar{0} = \bar{0}$, so $ab \in N$, showing $N$ is closed under multiplication. Thus $N$ is a subring of $R$.

(d) This follows from Theorem 2 applied to the additive group of $R$: a homomorphism of additive groups is an isomorphism if and only if its kernel is trivial. Since $T$ already preserves multiplication, the condition $N = \{0\}$ is necessary and sufficient for $T$ to be a ring isomorphism.
