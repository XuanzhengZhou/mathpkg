---
role: proof
source_book: gtm-0073
chapter: "VIII"
section: "VIII.1"
proof_technique: schreier-refinement-and-recursion
locale: en
content_hash: ""
written_against: ""
---
(\(\Rightarrow\)) Suppose \(A\) has a composition series \(S\) of length \(n\). If either chain condition fails, one can find submodules forming a normal series \(T\) of length \(n+1\). By Theorem 1.10, \(S\) and \(T\) have refinements that are equivalent. This is a contradiction since equivalent series have equal length: every refinement of the composition series \(S\) has the same length \(n\) as \(S\), but every refinement of \(T\) necessarily has length at least \(n+1\). Therefore, \(A\) satisfies both chain conditions.

(\(\Leftarrow\)) If \(B\) is a nonzero submodule of \(A\), let \(S(B)\) be the set of all submodules \(C\) of \(B\) such that \(C \neq B\). For each \(B\) there is a maximal element \(B'\) of \(S(B)\) by Theorem 1.4. By the Recursion Theorem, there is a function \(\varphi: \mathbb{N} \to S\) such that \(\varphi(0) = A\) and \(\varphi(n+1) = \varphi(n)'\). This yields a descending chain \(A \supset A_1 \supset A_2 \supset \cdots\) of submodules. By the DCC, this chain terminates at \(0\). Since each factor \(A_i/A_{i+1}\) is simple by maximality of the choice \(A_{i+1} = A_i'\), this forms a composition series for \(A\).
