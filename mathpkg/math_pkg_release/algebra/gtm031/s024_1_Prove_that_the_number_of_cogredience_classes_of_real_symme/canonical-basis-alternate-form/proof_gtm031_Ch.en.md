---
role: proof
locale: en
of_concept: canonical-basis-alternate-form
source_book: gtm031
source_chapter: ""
source_section: "Quaternionic Hermitian Forms"
---

Suppose that $g(x, y)$ is alternate and not identically $0$. Then we can find a pair of vectors $u, v$ such that $g(u, v) \neq 0$. By replacing $v$ by a suitable multiple $v_1$ of $v$ we then obtain $u_1 = u$ and $v_1$ such that $g(u_1, v_1) = 1$. Then $g(v_1, u_1) = -1$, $g(u_1, u_1) = 0 = g(v_1, v_1)$. It follows that $u_1$ and $v_1$ are linearly independent.

Now suppose we have already found $k$ pairs of vectors $u_1, v_1, u_2, v_2, \cdots, u_k, v_k$ that are linearly independent and satisfy

$$g(u_i, v_i) = 1, \quad g(v_i, u_i) = -1$$

with all other products $0$. Let $E_k$ denote the linear transformation

$$x \rightarrow \sum_1^k g(x, v_i)u_i - \sum_1^k g(x, u_i)v_i.$$

One verifies that $E_k$ is a projection on the space $\mathfrak{S}_k = [u_1, v_1, u_2, v_2, \cdots, u_k, v_k]$. Hence if $F_k = 1 - E_k$, then $\mathfrak{R} = \mathfrak{S}_k \oplus \mathfrak{R}F_k$. Also we can verify that $g(xE_k, yF_k) = 0$ and $g(xF_k, yE_k) = 0$, so the decomposition is orthogonal with respect to $g$. Moreover $g$ restricted to $\mathfrak{R}F_k$ is alternate. If this restriction is not identically zero, we can find another pair $u_{k+1}, v_{k+1}$ in $\mathfrak{R}F_k$ with $g(u_{k+1}, v_{k+1}) = 1$. The process continues until the restriction vanishes, at which point we choose any basis $z_1, \dots, z_{n-2r}$ for the remaining subspace, yielding the canonical basis.
