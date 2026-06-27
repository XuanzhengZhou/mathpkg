---
role: proof
locale: en
of_concept: frobenius-group-order-2n-properties
source_book: gtm006
source_chapter: "XIV"
source_section: "8"
---

(i) Let $\alpha$ be an element of order $2$ in $\Lambda$ and let $a$ be a point not fixed by $\alpha$. Set $b = a^\alpha$, so $\alpha$ interchanges $a$ and $b$. Now let $\Lambda_a$ be the stabilizer of $a$ in $\Lambda$. Since $\Lambda$ is a Frobenius group, $|\Lambda_a| = 2$. Let $\beta$ be the non-identity element of $\Lambda_a$. Then for any $c \in \mathcal{S} \setminus \{a\}$, the elements $a^{\beta c}$ for $c \in \mathcal{S} \setminus \{a\}$ give $n-1$ distinct conjugates of $\beta$. Since $\Lambda$ has $n$ involutions (each fixing exactly one point in its Frobenius complement action), and these involutions correspond bijectively to points of $\mathcal{S}$, given any distinct $a, b$ there exists an involution mapping $a$ to $b$.

(ii) Let $\alpha_0$ be an element of order $2$ in $\Lambda'$, let $\mathcal{T}$ be the orbit of $\Lambda'$ containing $a$ and let $|\mathcal{T}| = t$. Since $\alpha_0$ fixes only one point of $\mathcal{T}$, $t$ is odd. Furthermore since $\Lambda' \subseteq \Lambda_a$ and $|\Lambda_a| = 2 \geq |\Lambda'|$, $\Lambda' = \Lambda_a$ and hence the order of $\Lambda'$ is $2t$. Since $\Lambda'$ is a subgroup of the Frobenius group $\Lambda$, only the identity of $\Lambda'$ fixes $2$ points of $\mathcal{T}$ so that $\Lambda'$ is a Frobenius group on $\mathcal{T}$. The argument used at the beginning of the proof now establishes a one-to-one correspondence between the elements of order $2$ in $\Lambda'$ and the points of $\mathcal{T}$. Thus $r = t$ and $|\Lambda'| = 2r$.
