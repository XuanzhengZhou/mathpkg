---
role: proof
locale: en
of_concept: cayleys-theorem
source_book: gtm030
source_chapter: "I"
source_section: "10"
---

For each $a \in \mathfrak{G}$, define the right multiplication $a_r : \mathfrak{G} \to \mathfrak{G}$ by $x a_r = xa$. By the right cancellation law, $a_r$ is injective. Since for any $b \in \mathfrak{G}$, $b = (ba^{-1})a = (ba^{-1})a_r$, the map $a_r$ is surjective. Hence $a_r \in \mathfrak{G}(\mathfrak{G})$, the group of bijections of the set $\mathfrak{G}$.

Consider the product $a_r b_r$. For any $x \in \mathfrak{G}$, $x(a_r b_r) = (xa)b = x(ab)$ by associativity. Thus $a_r b_r = (ab)_r$, so the set $\mathfrak{G}_r = \{a_r\}$ is closed under composition. Moreover, $1_r$ is the identity in $\mathfrak{G}_r$, and $a_r (a^{-1})_r = (aa^{-1})_r = 1_r = (a^{-1}a)_r = (a^{-1})_r a_r$, so $(a_r)^{-1} = (a^{-1})_r \in \mathfrak{G}_r$. Thus $\mathfrak{G}_r$ is a transformation group.

The map $\varphi : \mathfrak{G} \to \mathfrak{G}_r$ defined by $\varphi(a) = a_r$ satisfies $\varphi(ab) = (ab)_r = a_r b_r = \varphi(a)\varphi(b)$. If $a \neq b$, then $1a_r = a \neq b = 1b_r$, so $\varphi$ is injective. By definition $\varphi$ is surjective onto $\mathfrak{G}_r$. Hence $\varphi$ is an isomorphism.
