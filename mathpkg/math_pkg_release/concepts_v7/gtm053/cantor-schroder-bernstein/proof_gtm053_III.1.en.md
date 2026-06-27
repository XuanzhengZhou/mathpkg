---
role: proof
locale: en
of_concept: cantor-schroder-bernstein
source_book: gtm053
source_chapter: "III"
source_section: "1"
---

# Proof of the Cantor-Schröder-Bernstein Theorem

**Theorem 1.2 (Cantor-Schröder-Bernstein-Zermelo).** If there exist injective maps $f : A \to B$ and $g : B \to A$, then there exists a bijection $h : A \to B$. Equivalently, if $|A| \leq |B|$ and $|B| \leq |A|$, then $|A| = |B|$.

*Proof.* Given injections $f : A \to B$ and $g : B \to A$, we construct a bijection $h : A \to B$.

Consider the following partition of $A$. Define a sequence of sets by recursion. Let $C_0 = A \setminus g(B)$ (the elements of $A$ not in the image of $g$). For $n \geq 0$, define
$$C_{n+1} = g(f(C_n)).$$
Let $C = \bigcup_{n=0}^\infty C_n$. The set $C$ consists of all elements of $A$ that can be "traced back" to elements not in the image of $g$, by alternately applying $f$ and $g$.

Now define $h : A \to B$ by:
$$h(a) = \begin{cases} f(a), & \text{if } a \in C, \\ g^{-1}(a), & \text{if } a \in A \setminus C. \end{cases}$$

Note that for $a \in A \setminus C$, we have $a \in g(B)$ (since otherwise $a \in C_0$), so $g^{-1}(a)$ is well-defined and unique (since $g$ is injective).

We verify that $h$ is a bijection:

**Injectivity:** Suppose $h(a_1) = h(a_2)$. 
- If both $a_1, a_2 \in C$, then $f(a_1) = f(a_2)$, so $a_1 = a_2$ by injectivity of $f$.
- If both $a_1, a_2 \in A \setminus C$, then $g^{-1}(a_1) = g^{-1}(a_2)$, so $a_1 = a_2$ by injectivity of $g^{-1}$.
- If $a_1 \in C$ and $a_2 \in A \setminus C$, then $h(a_1) = f(a_1)$ and $h(a_2) = g^{-1}(a_2)$. If $f(a_1) = g^{-1}(a_2)$, then $g(f(a_1)) = a_2$. But $g(f(a_1)) \in g(f(C)) \subseteq C$ by the definition of $C_{n+1}$, contradicting $a_2 \notin C$. Hence this case is impossible. The symmetric case is analogous.

**Surjectivity:** Let $b \in B$. If $g(b) \in A \setminus C$, then $h(g(b)) = g^{-1}(g(b)) = b$. If $g(b) \in C$, then either $g(b) \in C_0 = A \setminus g(B)$ (impossible since $g(b) \in g(B)$), or $g(b) \in C_{n+1} = g(f(C_n))$ for some $n$. Then $g(b) = g(f(c))$ for some $c \in C_n$. By injectivity of $g$, $b = f(c)$, and since $c \in C_n \subseteq C$, we have $h(c) = f(c) = b$.

Thus $h$ is a bijection, establishing $|A| = |B|$. $\square$
