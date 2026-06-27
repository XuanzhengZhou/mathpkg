---
role: proof
locale: en
of_concept: derivative-zero-implies-constant
source_book: gtm011
source_chapter: "III"
source_section: "2"
---
Fix $z_0 \in G$ and let $\omega_0 = f(z_0)$. Put $A = \{z \in G: f(z) = \omega_0\}$. We show $A = G$ by proving $A$ is both open and closed in $G$. To see $A$ is closed: if $z \in G$ and $\{z_n\} \subset A$ with $z = \lim z_n$, then by continuity $f(z) = \lim f(z_n) = \omega_0$, so $z \in A$. To see $A$ is open: pick $a \in A$ and $R > 0$ with $B(a; R) \subset G$. For $z \in B(a; R)$, define $g(t) = f(a + t(z-a))$ on $[0,1]$. Then $g(t) = f(a + t(z-a))(z-a) = 0$, so $g$ is constant. Hence $f(z) = g(1) = g(0) = f(a) = \omega_0$. Thus $B(a; R) \subset A$ and $A = G$.
