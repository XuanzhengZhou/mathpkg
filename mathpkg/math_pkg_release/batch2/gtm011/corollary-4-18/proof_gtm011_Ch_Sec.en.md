---
role: proof
locale: en
of_concept: corollary-4-18
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. If $G \neq \mathbb{C}$ the result is clear since $\mathbb{C}_\infty - G$ has only one component. If $G = \mathbb{C}$ then the result is trivial.

Theorem 4.9 has no converse as the following example illustrates. Let $1 > r_1 > r_2 > \ldots$ with $r_n \to 0$; for each $n$ let $\gamma_n$ be a proper closed arc of the circle $|z| = r_n$ with length $V(\gamma_n)$. Put $G = B(0; 1) - \left[ \bigcup_{n=1}^{\infty} \{ \gamma_n \} \cup \{0\} \right]$ and suppose that $\lim V(\gamma_n)/r_n = 2\pi$. So $\mathbb{C}_\infty - G = \

Since $\frac{V(\gamma_m)}{r_m} \to 2\pi$, $k_m(0) \to 0$; it follows that $h(z) \to 0$ as $z \to 0$. Thus, $G$ has a barrier at zero.

Exercises

1. Let $G = B(0; 1)$ and find a barrier for $G$ at each point of the boundary.
2. Let $G = \mathbb{C} - (\infty, 0]$ and construct a barrier for each point of $\partial_\infty G$.
3. Let $G$ be a region and $a$ a point in $\partial_\infty G$ such that there is a harmonic function $u: G \to \mathbb{R}$ with $\lim u(z) = 0$ and $\lim \inf u(z) > 0$ for all $w$ in $\partial_\infty G$, $w \neq a$. Show that there is a barrier for $G$ at $a$.
4. This exercise asks for an easier proof of a special case of Theorem 4.9. Let $G$ be a bounded region and let $a \in \partial G$ such that there is a point $b$ with $[a, b] \cap G^- = \{a\}$. Show that $G$ has a barrier at $a$. (Hint: Consider the transformation $(z-a)(z-b)^{-1}$.)

§5. Green’s Function

In this section Green’s Function is introduced and its existence is discussed. Green’s Function plays a vital role in differential equations and other fields of analysis.
