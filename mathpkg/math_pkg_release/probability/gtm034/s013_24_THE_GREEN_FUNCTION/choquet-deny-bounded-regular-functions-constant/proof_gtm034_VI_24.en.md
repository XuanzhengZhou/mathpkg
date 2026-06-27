---
role: proof
locale: en
of_concept: choquet-deny-bounded-regular-functions-constant
source_book: gtm034
source_chapter: "VI"
source_section: "24"
---

Given \(f\) satisfying the hypotheses, set \(g(x) = f(x) - f(x-a)\) for arbitrary \(a \in R^+\). Then \(g\) is bounded and \(Pg = g\). Let \(M = \sup g(x)\). Using Cantor's diagonal process, extract a subsequence \(x_{n'}\) such that \(g_{n'}(x) = g(x + x_{n'}) \to g^*(x)\) for all \(x \in R\), with \(g^*(0) = M\) and \(Pg^* = g^*\). By the aperiodicity of \(P\), iterating \(P\) on the equation \(g^*(a) = Pg^*(a)\) and using the maximum property forces \(M \leq 0\), hence \(g(x) \leq 0\) or \(f(x) \leq f(x-a)\). Applying the same argument to \(-f\) gives \(f(x) = f(x-a)\). Since the random walk is aperiodic, any \(y \in R\) can be written as \(y = a - b\) with \(a,b \in R^+\), so \(f\) is constant.
