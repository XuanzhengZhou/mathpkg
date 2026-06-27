---
role: proof
locale: en
of_concept: phi-injective-stone-cech
source_book: gtm015
source_chapter: "64"
source_section: "Stone-Čech compactification"
---

# Proof of The embedding map in Stone-Čech is injective

Proof. Suppose $s, t \in T, s \neq t$. By complete regularity, there exists $x \in \mathcal{C}^\infty(T)$ such that $x(s) = 0$ and $x(t) = 1$, thus $f_s(x) \neq f_t(x)$.

(64

$F(f) = 1$ and $F = 0$ on $\overline{\varphi(T)}$. In particular, $F = 0$ on $\varphi(T)$ and $F \neq 0$. Say $F = \hat{x}$, $x \in \mathcal{C}^\infty(T)$. Then

$$0 = F(\varphi(t)) = \hat{x}(f_t) = f_t(x) = x(t)$$

for all $t \in T$, thus $x = 0$, whence $F = \hat{x} = 0$, a contradiction.
