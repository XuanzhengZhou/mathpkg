---
role: proof
locale: en
of_concept: coherence-theorem-for-monoidal-categories
source_book: gtm005
source_chapter: "VII"
source_section: "2. Coherence"
---

**Proof.** Write the desired morphism as $w \mapsto w_b$, suggesting "Substitute $b$ in all the blanks of the word $w$". On objects $w$, set

$$(e_0)_b = e, \quad (-)_b = b, \quad (v \square w)_b = v_b \square w_b;$$

by induction, these formulas uniquely determine all $w_b$.

For words of fixed length $n$, construct a "basic" graph $G_n = G_{n,b}$. Its vertices are all words $w$ of length $n$ which do not involve $e_0$, while its edges $v \to w$ are certain arrows $v_b \to w_b$ in $B$, called "basic" arrows. Each instance

$$\alpha : u_b \square (v_b \square w_b) \to (u_b \square v_b) \square w_b$$

of associativity and each instance of $\alpha^{-1}$ is basic, as are all arrows $\beta \square 1$ or $1 \square \beta$ with $1 : v_b \to v_b$ an identity and $\beta$ already recognized as basic. Each basic arrow is either "directed" (involving $\alpha$) or "antidirected" (with $\alpha^{-1}$).

In the graph $G_n$, the paths from $u$ to $w$ are the composable sequences of basic arrows from $u_b$ to $w_b$; by composition each path yields an arrow $u_b \to w_b$. The goal is to prove that any two such paths yield equal arrows in $B$.

Observe that for each vertex $w$ there is a distinguished vertex $w^{(n)}$ (the "right-associated" word, e.g., $((a \square b) \square c) \square d$ for length 4) and a directed path from $w$ to $w^{(n)}$ consisting solely of $\alpha$ arrows. It suffices to show that any two directed paths (all $\alpha$'s, no $\alpha^{-1}$) from a vertex $v$ to $w^{(n)}$ are equal. Proceed by induction on the rank of $v$ (the number of $\alpha$'s needed to reach $w^{(n)}$).

Suppose the statement holds for all $v$ of smaller rank, and consider two different directed paths starting at $v$ with directed basic arrows $\beta$ and $\gamma$. Both $\beta$ and $\gamma$ decrease the rank. It suffices to show that one can "rejoin" their codomains $v'$ and $v''$ by directed paths to some common vertex $z$ such that the diamond from $v$ to $z$ is commutative.

If $\beta = \gamma$, take $z = v' = v''$. If $\beta \neq \gamma$, write $v = u \square w$ and observe that $\beta$ has one of three forms:
- $\beta = \beta' \square 1_w$: $\beta$ acts inside the first factor $u$;
- $\beta = 1_u \square \beta''$: $\beta$ acts inside the second factor $w$;
- $\beta = \alpha_{u,s,t}$, where $v = u \square w = u \square (s \square t)$.

Similarly for $\gamma$.

Compare the cases for $\beta$ and $\gamma$:
- If both act inside the same factor $u$, use induction on the length $n$.
- If $\beta$ acts inside $u$ and $\gamma$ inside $w$, use the diamond that commutes because $\square$ is a bifunctor.
- If one of $\beta$ or $\gamma$ is $\alpha_{u,s,t}$ and the other acts inside $u$, use the naturality of $\alpha$ to form a commutative diamond.
- If one is $\alpha_{u,s,t}$ and the other acts inside $w = s \square t$ (inside $s$ or $t$), naturality of $\alpha$ again provides a diamond.
- The remaining case: $\gamma$ acts inside $s \square t$ but not inside $s$ or $t$, so $\gamma$ must be an instance of $\alpha$, with $t = p \square q$. The diamond starts with
  $$v = u \square w = u \square (s \square (p \square q))$$
  with $\beta = \alpha$ and $\gamma = 1 \square \alpha$. This diamond is completed by the pentagon axiom (1.5), which asserts commutativity of the pentagon in any monoidal category.

This shows the graph $G_n$ is commutative in $B$, completing the coherence proof for associativity alone.

To incorporate $\lambda$ and $\varrho$, consider the larger graph $G_n'$ with vertices all words of length $n$ (including those involving $e_0$) and edges built from instances of $\alpha$, $\lambda$, $\varrho$ (and their inverses) boxed with identities. For each word $w$, there is a path $w \to w^{(n)}$ that first removes all occurrences of $e_0$ using $\lambda$ and $\varrho$, then applies $\alpha$'s. The triangle axiom (1.7) ensures that any two such paths yield equal arrows, and the identity $\lambda_e = \varrho_e$ guarantees consistency at the unit. This establishes the full coherence theorem. $\square$
