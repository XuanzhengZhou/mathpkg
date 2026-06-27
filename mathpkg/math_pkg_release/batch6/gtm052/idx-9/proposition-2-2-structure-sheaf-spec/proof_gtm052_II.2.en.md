---
role: proof
locale: en
of_concept: proposition-2-2-structure-sheaf-spec
source_book: gtm052
source_chapter: "II"
source_section: "2"
---

(a) First we define a homomorphism from $\mathcal{O}_\mathfrak{p}$ to $A_\mathfrak{p}$ by sending any local section $s$ in a neighborhood of $\mathfrak{p}$ to its value $s(\mathfrak{p}) \in A_\mathfrak{p}$. This gives a well-defined homomorphism $\varphi$ from $\mathcal{O}_\mathfrak{p}$ to $A_\mathfrak{p}$.

The map $\varphi$ is surjective, because any element of $A_\mathfrak{p}$ can be represented as a quotient $a/f$, with $a,f \in A$, $f \notin \mathfrak{p}$. Then $D(f)$ will be an open neighborhood of $\mathfrak{p}$, and $a/f$ defines a section of $\mathcal{O}$ over $D(f)$ whose value at $\mathfrak{p}$ is $a/f$. Hence $\varphi$ is surjective.

For injectivity, we define a map in the opposite direction. Any element of $\mathcal{O}_\mathfrak{p}$ is represented by a section $\langle s, U \rangle$ in some open neighborhood $U$ of $\mathfrak{p}$. Since distinguished open sets $D(f)$ form a base for the topology, we can shrink $U$ to $D(f)$ for some $f \notin \mathfrak{p}$. So the element is represented by a section over $D(f)$, i.e., an element of $A_f$. Restricting further if necessary, we may assume that this is given by $a/f^n \in A_f$. Then we map this to the element $a/f^n$ in the stalk $A_\mathfrak{p}$. One verifies that the map is well-defined and is the inverse of $\varphi$.

(b) There is a natural homomorphism $\psi: A_f \to \mathcal{O}(D(f))$, sending $a/f^n$ to the section given by $a/f^n$ on $D(f)$. We must show $\psi$ is an isomorphism.

First, injectivity of $\psi$: Suppose $a/f^n$ goes to zero in $\mathcal{O}(D(f))$. This means that for each $\mathfrak{p} \in D(f)$, the image of $a/f^n$ in $A_\mathfrak{p}$ is zero. This happens if and only if for each $\mathfrak{p} \in D(f)$, there exists $h \notin \mathfrak{p}$ such that $h a = 0$ in $A$. In other words, the annihilator $\text{Ann}(a)$ is not contained in any $\mathfrak{p} \in D(f)$, which means $V(\text{Ann}(a)) \cap D(f) = \varnothing$, so $f \in \sqrt{\text{Ann}(a)}$, i.e., $f^n a = 0$ in $A$ for some $n$. Hence $a/f^n = 0$ in $A_f$. This shows $\psi$ is injective.

Next, surjectivity of $\psi$: Let $s \in \mathcal{O}(D(f))$ be a section. By definition of the structure sheaf, $s$ can be covered by open sets $D(h_i) \subseteq D(f)$ on which $s$ is represented by elements $a_i/h_i$ in $A_{h_i}$.

We observe that $D(f)$ can be covered by a finite number of the $D(h_i)$. Indeed, $D(f) \subseteq \bigcup D(h_i)$ if and only if $V((f)) \supseteq \bigcap V((h_i)) = V(\sum(h_i))$. By (2.1c), this is equivalent to $f \in \sqrt{\sum(h_i)}$, or $f^n \in \sum(h_i)$ for some $n$, which means $f^n$ can be expressed as a finite sum $f^n = \sum b_i h_i$, $b_i \in A$. Hence a finite subset of the $h_i$ will do. So we fix a finite set $h_1, \ldots, h_r$ such that $D(f) \subseteq D(h_1) \cup \ldots \cup D(h_r)$.

On $D(h_i) \cap D(h_j) = D(h_i h_j)$ we have two elements of $A_{h_i h_j}$, namely $a_i/h_i$ and $a_j/h_j$, both representing $s$. By the injectivity of $\psi$ proved above applied to $D(h_i h_j)$, we must have $a_i/h_i = a_j/h_j$ in $A_{h_i h_j}$. Hence for some $n$,
$$(h_i h_j)^n (h_j a_i - h_i a_j) = 0.$$
Since there are only finitely many indices, we may pick $n$ so large that it works for all $i,j$ at once. Rewrite as
$$h_j^{n+1} (h_i^n a_i) - h_i^{n+1} (h_j^n a_j) = 0.$$
Replace each $h_i$ by $h_i^{n+1}$ and $a_i$ by $h_i^n a_i$. Then $s$ is still represented on $D(h_i)$ by $a_i/h_i$, and moreover $h_j a_i = h_i a_j$ for all $i,j$.

Now write $f^n = \sum b_i h_i$ with $b_i \in A$. Let $a = \sum b_i a_i$. Then on each $D(h_j)$,
$$a = \sum_i b_i a_i = \sum_i b_i \frac{h_j a_i}{h_j} = \frac{a_j}{h_j} \sum_i b_i h_i = \frac{a_j}{h_j} f^n.$$
Thus $a$ and $f^n$ give the same section on $D(h_j)$, so on $D(f)$, $s$ is represented by $a/f^n$. Hence $\psi$ is surjective.

(c) This follows from (b) by taking $f = 1$, since $D(1) = \text{Spec } A$ and $A_1 \cong A$.
