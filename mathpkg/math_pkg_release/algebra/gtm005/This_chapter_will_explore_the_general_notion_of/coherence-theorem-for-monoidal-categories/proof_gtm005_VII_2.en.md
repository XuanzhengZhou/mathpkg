---
role: proof
locale: en
of_concept: coherence-theorem-for-monoidal-categories
source_book: gtm005
source_chapter: "VII"
source_section: "2. Coherence"
---

Write the desired morphism as $w \mapsto w_b$, meaning "substitute $b$ in all the blanks of the word $w$". On objects $w$ set
$$(e_0)_b = e, \quad (-)_b = b, \quad (v \square w)_b = v_b \square w_b;$$
by induction, these formulas uniquely determine all $w_b$.

For words of fixed length $n$ construct a "basic" graph $G_n = G_{n,b}$. Its vertices are all words $w$ of length $n$ which do not involve $e_0$, while its edges $v \rightarrow w$ are identical with certain arrows $v_b \rightarrow w_b$ in $B$, called "basic" arrows. Each instance
$$\alpha : u_b \square (v_b \square w_b) \rightarrow (u_b \square v_b) \square w_b$$
of associativity and each instance of $\alpha^{-1}$ is basic, as are all arrows $\beta \square 1$ or $1 \square \beta$ with $1 : v_b \rightarrow v_b$ an identity and $\beta$ already recognized as basic. Each basic arrow is either "directed" (involving $\alpha$) or "antidirected" (with $\alpha^{-1}$). In $G_n$, paths from $u$ to $w$ are composable sequences of basic arrows from $u_b$ to $w_b$; by composition each path yields an arrow $u_b \rightarrow w_b$.

It suffices to show that any two directed paths (all $\alpha$'s, no $\alpha^{-1}$) from a $v_i$ to $w^{(n)}$ are equal. Proceed by induction on the rank of $v_i = v$. Suppose it true for all $v$ of smaller rank, and consider two different directed paths starting at $v$ with directed basic arrows $\beta$ and $\gamma$. Both $\beta$ and $\gamma$ decrease the rank, so it suffices to show that one can "rejoin" their codomains $v'$ and $v''$ by directed paths to some common vertex $z$ such that the diamond from $v$ to $z$ commutes.

Case subdivision: If $\beta = \gamma$, take $z = v' = v''$. If $\beta \neq \gamma$, write $v = u \square w$ and observe $\beta$ has one of three forms:
$$\beta = \beta' \square 1_w \quad \text{(acts inside the first factor $u$)},$$
$$\beta = 1_u \square \beta'' \quad \text{(acts inside the second factor)},$$
$$\beta = \alpha_{u,s,t}, \quad \text{where } v = u \square w = u \square (s \square t).$$

For $\gamma$ there are three corresponding cases.

- If both act inside the same factor $u$, use induction on the length $n$.
- If $\beta$ acts inside $u$ and $\gamma$ inside $w$, the diamond commutes because $\square$ is a bifunctor.
- If one, say $\beta$, is $\beta = \alpha_{u,s,t}$ and $\gamma$ acts inside $u$, use a diamond from $u \square (s \square t)$ to $(u' \square s) \square t$, which commutes by naturality of $\alpha$.
- If $\gamma$ acts inside $w = s \square t$ (inside $s$ or $t$), naturality of $\alpha$ again gives a commutative diamond.
- If $\gamma$ acts inside $s \square t$ but not inside $s$ or $t$, then $\gamma$ must be an instance of $\alpha$ with $t = p \square q$, giving the diamond:
  $$v = u \square (s \square (p \square q))$$
  with $\beta = \alpha$ and $\gamma = 1 \square \alpha$. This diamond is completed by the pentagon axiom (1.5).

This shows $G_n$ is commutative in $B$, completing the coherence proof as far as associativity is concerned.

To incorporate $\lambda$ and $\varrho$, consider the graph $G_n'$ with vertices all words of length $n$ (including those involving $e_0$) and edges all basic arrows built by boxing instances of $\alpha, \lambda, \varrho$ (and their inverses) with identities. For each word $w$, there is still at least one path $w \rightarrow w^{(n)}$. The composite arrow obtained from any such path equals that for a different path which first removes all $e$'s, then applies $\alpha$. This follows because when an $e$ is removed, the relevant instances of $\lambda$ and $\varrho$ compose with $\alpha$ via the triangle axiom (1.7) and the condition $\lambda_e = \varrho_e$.
