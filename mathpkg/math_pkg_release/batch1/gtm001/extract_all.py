#!/usr/bin/env python3
"""Extract ALL concepts from GTM001 sections and write v8 format files."""
import os, json

BASE = "/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch1/gtm001"

def write_concept(section, slug, ctype, title_en, statement, intro, proof="", chapter="", domain="foundations", subdomain="set-theory", difficulty="basic", deps=None, pages=""):
    d = os.path.join(BASE, section, slug)
    os.makedirs(d, exist_ok=True)

    # concept.yaml
    yaml = f"""id: {slug}
title_en: "{title_en}"
title_zh: ""
type: {ctype}
domain: {domain}
subdomain: {subdomain}
difficulty: {difficulty}
tags: []
depends_on: {{required:[], recommended:[], suggested:[]}}
source_books: [{{book_id:"gtm001",author:"Takeuti, Gaisi; Zaring, Wilson M.",title:"Introduction to Axiomatic Set Theory",chapter:"{chapter}",section:"",pages:"{pages}",role_in_book:""}}]
content_hash: ""
extraction_date: "2026-06-27"
extraction_agent: "v8-full-extract"
"""
    with open(os.path.join(d, "concept.yaml"), "w") as f: f.write(yaml)

    # theorem.tex
    with open(os.path.join(d, "theorem.tex"), "w") as f: f.write(statement)

    # introduce.en.md
    intro_md = f"""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
{intro}
"""
    with open(os.path.join(d, "introduce.en.md"), "w") as f: f.write(intro_md)

    # proof if provided
    if proof and ctype in ("theorem","proposition","lemma","corollary"):
        proof_md = f"""---
role: proof
locale: en
of_concept: {slug}
source_book: gtm001
source_chapter: "{chapter}"
source_section: ""
---
{proof}
"""
        with open(os.path.join(d, f"proof_gtm001_{chapter.replace(' ','_').replace('.','')}.en.md"), "w") as f: f.write(proof_md)

# ================================================================
# s001 - CHAPTER 1 (Introduction) + CHAPTER 2 (Language and Logic)
# ================================================================
S = "s001_CHAPTER_1"

write_concept(S, "well-formed-formula-rules", "definition", "Rules for Well-Formed Formulas",
r"""\text{The formal language consists of:}
\text{Free variables: } a_0, a_1, \ldots
\text{Bound variables: } x_0, x_1, \ldots
\text{Predicate symbol: } \in
\text{Logical symbols: } \neg, \lor, \land, \rightarrow, \leftrightarrow, \forall, \exists

\text{Rules for wffs:}
\begin{enumerate}
\item \text{If $a$ and $b$ are free variables, then $[a \in b]$ is a wff (atomic formula).}
\item \text{If $\varphi$ and $\psi$ are wffs, then $\neg\varphi$, $[\varphi \lor \psi]$, $[\varphi \land \psi]$, $[\varphi \rightarrow \psi]$, $[\varphi \leftrightarrow \psi]$ are wffs.}
\item \text{If $\varphi$ is a wff and $x$ is a bound variable, then $(\forall x)\varphi(x)$ and $(\exists x)\varphi(x)$ are wffs.}
\end{enumerate}""",
"Defines the inductive syntax rules for well-formed formulas (wffs) in the formal language of Zermelo-Fraenkel set theory. The language distinguishes between free variables and bound variables, with membership $\in$ as the only predicate symbol.",
chapter="2")

write_concept(S, "logical-axioms-and-inference-rules", "axiom", "Logical Axioms and Rules of Inference",
r"""\text{Logical Axioms:}
\begin{enumerate}
\item \varphi \rightarrow [\psi \rightarrow \varphi]
\item [\varphi \rightarrow [\psi \rightarrow \eta]] \rightarrow [[\varphi \rightarrow \psi] \rightarrow [\varphi \rightarrow \eta]]
\item [\neg \varphi \rightarrow \neg \psi] \rightarrow [\psi \rightarrow \varphi]
\item (\forall x)[\varphi \rightarrow \psi(x)] \rightarrow [\varphi \rightarrow (\forall x)\psi(x)] \quad \text{where the free variable on which we are quantifying does not occur in $\varphi$}
\item (\forall x)\varphi(x) \rightarrow \varphi(a)
\end{enumerate}

\text{Rules of Inference:}
\begin{enumerate}
\item \text{From $\varphi$ and $\varphi \rightarrow \psi$ to infer $\psi$ (Modus Ponens).}
\item \text{From $\varphi$ to infer $(\forall x)\varphi(x)$ (Generalization).}
\end{enumerate}""",
"The logical axioms and two rules of inference form the deductive apparatus. $\vdash\varphi$ means $\varphi$ is deducible from the logical and nonlogical axioms via the rules of inference. $\vdash_{\text{LA}}\varphi$ indicates deducibility using only the logical axioms. Two wffs are logically equivalent iff $\vdash_{\text{LA}}\varphi\leftrightarrow\psi$.",
chapter="2")

write_concept(S, "russells-paradox", "proposition", "Russell's Paradox",
r"""\text{If the collection of all sets that are not elements of themselves is a set, then this set has the property that it is an element of itself if and only if it is not an element of itself:}
(\exists a)(\forall x)[x \in a \leftrightarrow x \notin x] \rightarrow [a \in a \leftrightarrow a \notin a]""",
"Russell's paradox shows that the unrestricted Axiom of Abstraction (given any property there exists a set whose elements are exactly those objects having that property) leads to a contradiction. This motivates the Zermelo-Fraenkel distinction between sets and proper classes.",
chapter="1")

# ================================================================
# s002 - CHAPTER 3 (Equality) + CHAPTER 4 (Classes)
# ================================================================
S = "s002_CHAPTER_3"

write_concept(S, "definition-of-set-equality", "definition", "Definition of Set Equality",
r"""a = b \xleftrightarrow{\Delta} (\forall x)[x \in a \leftrightarrow x \in b]""",
"Two sets are equal if and only if they have exactly the same elements. This is the axiom of extensionality formulated as a definition.",
chapter="3")

write_concept(S, "equality-is-equivalence-relation", "proposition", "Equality is an Equivalence Relation",
r"""\text{(1) } a = a.
\text{(2) } a = b \rightarrow b = a.
\text{(3) } a = b \land b = c \rightarrow a = c.""",
"Proposition 3.2 establishes that set equality, as defined by extensionality, is an equivalence relation: it is reflexive, symmetric, and transitive.",
chapter="3",
proof=r"""\text{(1) } (\forall x)[x \in a \leftrightarrow x \in a].
\text{(2) } (\forall x)[x \in a \leftrightarrow x \in b] \rightarrow (\forall x)[x \in b \leftrightarrow x \in a].
\text{(3) } (\forall x)[x \in a \leftrightarrow x \in b] \land (\forall x)[x \in b \leftrightarrow x \in c] \rightarrow (\forall x)[x \in a \leftrightarrow x \in c].""")

write_concept(S, "axiom-of-extensionality", "axiom", "Axiom of Extensionality",
r"""a = b \land a \in c \rightarrow b \in c""",
"Axiom 1: If two sets are equal and one is an element of a third set, then the other is also an element of that set. This weaker form, together with the definition of equality, implies the full substitution principle.",
chapter="3")

write_concept(S, "equality-implies-membership-equivalence", "proposition", "Equality Implies Membership Equivalence",
r"""a = b \rightarrow [a \in c \leftrightarrow b \in c]""",
"Proposition 3.3: If two sets are equal, then one belongs to a third set if and only if the other does. Proved from Axiom 1 and symmetry of equality.",
chapter="3",
proof=r"""\text{From Axiom 1: } a = b \land a \in c \rightarrow b \in c.
\text{From Proposition 3.2(2): } a = b \rightarrow b = a.
\text{Thus } b = a \land b \in c \rightarrow a \in c.
\text{Therefore } a = b \rightarrow [a \in c \leftrightarrow b \in c].""")

write_concept(S, "substitution-of-equals", "theorem", "Substitution of Equals",
r"""a = b \rightarrow [\varphi(a) \leftrightarrow \varphi(b)]""",
"Theorem 3.4: If two sets are equal, any well-formed formula that holds for one also holds for the other. Proved by induction on the number of logical symbols in $\varphi$.",
chapter="3",
proof=r"""\text{(By induction on $n$ the number of logical symbols in $\varphi$).}
\text{If $n = 0$: $\varphi(a)$ is of the form $c \in d$, $c \in a$, $a \in c$, or $a \in a$. Each case follows from Definition 3.1 and Proposition 3.3.}

\text{Induction step ($n > 0$): $\varphi(a)$ must be of the form:}
\text{(1) $\neg\psi(a)$: By induction hypothesis, $a = b \rightarrow [\psi(a) \leftrightarrow \psi(b)]$, hence $a = b \rightarrow [\neg\psi(a) \leftrightarrow \neg\psi(b)]$.}
\text{(2) $\psi(a) \land \eta(a)$: By induction hypothesis for both, the result follows.}
\text{(3) $(\forall x)\psi(a, x)$: Choose a free variable $c$ distinct from $a, b$ not occurring in $\psi(a, x)$. Since $\psi(a, c)$ has fewer than $n$ logical symbols, $a = b \rightarrow [\psi(a, c) \leftrightarrow \psi(b, c)]$. Generalize on $c$ using Logical Axiom 4 to obtain the result.""")

write_concept(S, "wff-in-wider-sense", "definition", "Well-Formed Formula in the Wider Sense",
r"""\text{(1) If $a$ and $b$ are free variables, then $a \in b$ is a wff in the wider sense.}
\text{(2) If $\varphi$ and $\psi$ are wffs in the wider sense, then $a \in \{x \mid \psi(x)\}$, $\{x \mid \varphi(x)\} \in b$, and $\{x \mid \varphi(x)\} \in \{x \mid \psi(x)\}$ are wffs in the wider sense.}
\text{(3) If $\varphi$ and $\psi$ are wffs in the wider sense, then $\neg\varphi$, $\varphi \land \psi$, $\varphi \lor \psi$, $\varphi \rightarrow \psi$, and $\varphi \leftrightarrow \psi$ are wffs in the wider sense.}
\text{(4) If $\varphi(x)$ is a wff in the wider sense, then $(\forall x)\varphi(x)$ and $(\exists x)\varphi(x)$ are wffs in the wider sense.}""",
"Definition 4.1 extends the notion of wff to include class terms $\{x\mid\varphi(x)\}$. This allows formulas that speak about classes while remaining reducible to primitive notation.",
chapter="4")

write_concept(S, "class-term-reduction", "definition", "Class Term Reduction Rules",
r"""\text{(1) } [a \in b]^* \triangleq a \in b.
\text{(2) } [a \in \{x \mid \varphi(x)\}]^* \triangleq \varphi^*(a).
\text{(3) } [\{x \mid \varphi(x)\} \in a]^* \triangleq (\exists y)[y \in a \land (\forall z)[z \in y \leftrightarrow \varphi^*(z)]].
\text{(4) } [\{x \mid \varphi(x)\} \in \{x \mid \psi(x)\}]^* \triangleq (\exists y)[\psi^*(y) \land (\forall z)[z \in y \leftrightarrow \varphi^*(z)]].
\text{(5) } [\neg\varphi]^* \triangleq \neg\varphi^*.
\text{(6) } [\varphi \land \psi]^* \triangleq \varphi^* \land \psi^*.
\text{(7) } [(\forall x)\varphi(x)]^* \triangleq (\forall x)\varphi^*(x).""",
"Definition 4.3: Every wff in the wider sense is reducible to a unique primitive wff $\varphi^*$ determined by these rules. This avoids extending the primitive language while allowing class notation.",
chapter="4")

write_concept(S, "equality-of-terms", "definition", "Equality of Terms",
r"""\text{If $A$ and $B$ are terms (free variables or class symbols), then}
A = B \xrightarrow{\Delta} (\forall x)[x \in A \leftrightarrow x \in B]""",
"Definition 4.5 extends the definition of equality to terms (free variables or class symbols $A, B, C, \ldots$). Two terms are equal iff they have the same elements.",
chapter="4")

write_concept(S, "set-and-proper-class-predicates", "definition", "Set and Proper Class Predicates",
r"""\mathcal{M}(A) \xrightarrow{\Delta} (\exists x)[x = A].
\mathcal{Pr}(A) \xrightarrow{\Delta} \neg \mathcal{M}(A).""",
"Definition 4.10: $\mathcal{M}(A)$ means $A$ is a set (there exists some set equal to $A$). $\mathcal{Pr}(A)$ means $A$ is a proper class (not a set). Every set is a class, but not every class is a set.",
chapter="4")

write_concept(S, "class-membership-condition", "proposition", "Class Membership Condition",
r"""A \in \{x \mid \varphi(x)\} \leftrightarrow \mathcal{M}(A) \land \varphi(A)""",
"Proposition 4.12: An object is an element of the class $\{x\mid\varphi(x)\}$ iff that object is a set and has the defining property $\varphi$. This resolves Russell's paradox by restricting membership to sets.",
chapter="4",
proof=r"""\text{From Definitions 4.2 and 4.10, and Propositions 4.6 and 4.8.}""")

write_concept(S, "russell-class-is-proper", "proposition", "Russell Class is Proper",
r"""\text{Ru} \triangleq \{x \mid x \notin x\}.
\mathcal{Pr}(\text{Ru})""",
"Proposition 4.14: The Russell class $\text{Ru} = \{x \mid x \notin x\}$ is a proper class. If it were a set, then $\text{Ru} \in \text{Ru} \leftrightarrow \text{Ru} \notin \text{Ru}$, a contradiction.",
chapter="4",
proof=r"""\text{From Proposition 4.12: }
\mathcal{M}(\text{Ru}) \rightarrow [\text{Ru} \in \text{Ru} \leftrightarrow \text{Ru} \notin \text{Ru}].
\text{This is a contradiction. Therefore $\text{Ru}$ is a proper class.}""")

write_concept(S, "set-equals-class-of-its-elements", "proposition", "Set Equals Class of Its Elements",
r"""a = \{x \mid x \in a\}""",
"Proposition 4.9: Every set equals the class of its elements. This establishes that the class notation is a conservative extension: every set corresponds naturally to a class.",
chapter="4",
proof=r"""(\forall x)[x \in a \leftrightarrow x \in a].""")

# ================================================================
# s003 - CHAPTER 5 (Elementary Properties of Classes)
# ================================================================
S = "s003_CHAPTER_5"

write_concept(S, "unordered-pair-and-singleton", "definition", "Unordered Pair and Singleton",
r"""\{a, b\} \triangleq \{x \mid x = a \lor x = b\}.
\{a\} \triangleq \{a, a\}.""",
"Definition 5.1: The unordered pair $\{a,b\}$ is the class of all $x$ such that $x = a$ or $x = b$. The singleton $\{a\}$ is the pair $\{a,a\}$.",
chapter="5")

write_concept(S, "axiom-of-pairing", "axiom", "Axiom of Pairing",
r"""\mathcal{M}(\{a, b\})""",
"Axiom 2: The unordered pair of any two sets is a set. This ensures that the basic operation of forming pairs always yields a set.",
chapter="5")

write_concept(S, "ordered-pair", "definition", "Ordered Pair (Kuratowski)",
r"""\langle a, b \rangle \triangleq \{x \mid x = \{a\} \lor x = \{a, b\}\}""",
"Definition 5.2: The ordered pair $\langle a,b\rangle$ is defined as $\{\{a\},\{a,b\}\}$, following Kuratowski. The fundamental property is $\langle a,b\rangle = \langle c,d\rangle \leftrightarrow a=c \land b=d$.",
chapter="5")

write_concept(S, "union-of-class", "definition", "Union of a Class",
r"""\cup(A) \triangleq \{x \mid (\exists y)[x \in y \land y \in A]\}""",
"Definition 5.5: $\cup(A)$ is the class of all elements of elements of $A$. This is the generalized union operation.",
chapter="5")

write_concept(S, "axiom-of-unions", "axiom", "Axiom of Unions",
r"""\mathcal{M}(\cup(a))""",
"Axiom 3: The union of a set is a set. This ensures closure under the union operation for all sets.",
chapter="5")

write_concept(S, "intersection-and-difference-of-classes", "definition", "Intersection and Difference of Classes",
r"""A \cup B \triangleq \{x \mid x \in A \lor x \in B\}.
A \cap B \triangleq \{x \mid x \in A \land x \in B\}.""",
"Definition 5.6-5.7: The union and intersection of two classes are defined via the corresponding logical operations on membership.",
chapter="5")

write_concept(S, "subclass-and-proper-subclass", "definition", "Subclass and Proper Subclass",
r"""A \subseteq B \xrightarrow{\Delta} (\forall x)[x \in A \rightarrow x \in B].
A \subset B \xrightarrow{\Delta} A \subseteq B \land A \neq B.""",
"Definition 5.9: $A\subseteq B$ means every element of $A$ is an element of $B$. $A\subset B$ is proper inclusion.",
chapter="5")

write_concept(S, "power-set", "definition", "Power Set",
r"""\mathcal{P}(a) \triangleq \{x \mid x \subseteq a\}""",
"Definition 5.10: The power set of $a$ is the class of all subsets of $a$.",
chapter="5")

write_concept(S, "axiom-of-powers", "axiom", "Axiom of Powers",
r"""\mathcal{M}(\mathcal{P}(a))""",
"Axiom 4: The power set of any set is a set.",
chapter="5")

write_concept(S, "axiom-schema-of-replacement", "axiom", "Axiom Schema of Replacement",
r"""[(\forall x)(\forall y)(\forall z)[\varphi(x, y) \land \varphi(x, z) \rightarrow y = z] \rightarrow \mathcal{M}(\{y \mid (\exists x \in a)\varphi(x, y)\})]""",
"Axiom 5 (Fraenkel's Axiom Schema of Replacement): If a formula $\varphi(x,y)$ defines a single-valued relation (a function in the intuitive sense), then the image of any set under this relation is a set. This is stronger than Zermelo's Separation.",
chapter="5")

write_concept(S, "axiom-schema-of-separation", "proposition", "Axiom Schema of Separation (Zermelo)",
r"""\mathcal{M}(a \cap A)""",
"Proposition 5.11: Zermelo's Axiom Schema of Separation follows from Replacement. It asserts that the intersection of a set with any class is a set, i.e., the class of elements of a given set satisfying any property is a set.",
chapter="5",
proof=r"""\text{Apply Axiom 5 (Replacement) to the wff $b \in A \land b = c$ where $b$ and $c$ do not occur in $A$.}
\text{Then } (\forall x, y, z)[x \in A \land x = y \land x \in A \land x = z \rightarrow y = z].
\text{Therefore } \mathcal{M}(\{y \mid (\exists x \in a)[x \in A \land x = y]\}) = \mathcal{M}(a \cap A).""")

write_concept(S, "empty-set", "definition", "Empty Set",
r"""0 \triangleq \{x \mid x \neq x\}""",
"Definition 5.14: The empty set $0$ is the class of all $x$ such that $x\neq x$. It contains no elements.",
chapter="5")

write_concept(S, "empty-set-is-a-set", "corollary", "The Empty Set is a Set",
r"""\mathcal{M}(0)""",
"Corollary 5.16: The empty set is a set. This follows from the fact that $a - a = 0$ and $a - A$ is a set for any set $a$ and class $A$.",
chapter="5",
proof=r"""\text{From Proposition 5.15: } a - a = 0.
\text{From Proposition 5.13: } \mathcal{M}(a - A) \text{ for any set $a$ and class $A$}.
\text{Therefore } \mathcal{M}(0).""")

write_concept(S, "universal-class", "definition", "Universal Class",
r"""V \triangleq \{x \mid x = x\}""",
"Definition 5.20: The universal class $V$ is the class of all sets (everything that is self-identical).",
chapter="5")

write_concept(S, "universal-class-is-proper", "proposition", "The Universal Class is Proper",
r"""\mathcal{Pr}(V)""",
"Proposition 5.21: The universal class $V$ is a proper class. If it were a set, then $V \in V$, which would lead to an infinite descending $\in$-chain contradicting Regularity.",
chapter="5",
proof=r"""\text{Since $V = V$, if $V$ were a set, then $V \in V$. This contradicts Proposition 5.18/Corollary 5.19 ($a \notin a$).}""")

write_concept(S, "axiom-of-regularity-weak", "axiom", "Axiom of Regularity (Weak Form)",
r"""a \neq 0 \rightarrow (\exists x \in a)[x \cap a = 0]""",
"Axiom 6: Every nonempty set has an element that is disjoint from it. This prevents infinite descending $\in$-chains and ensures the universe is well-founded.",
chapter="5")

write_concept(S, "axiom-of-regularity-strong", "axiom", "Axiom of Regularity (Strong Form)",
r"""A \neq 0 \rightarrow (\exists x \in A)[x \cap A = 0]""",
"Axiom 6': The strong form of Regularity asserts the same property for nonempty classes, not just sets. Later proved equivalent to the weak form.",
chapter="5")

write_concept(S, "no-membership-loops", "proposition", "No Finite Membership Loops",
r"""\neg [a_1 \in a_2 \in \cdots \in a_n \in a_1]""",
"Proposition 5.18: There are no finite $\in$-loops (cycles of the membership relation). In particular, $a \notin a$. Proved from the Axiom of Regularity.",
chapter="5",
proof=r"""\text{Let } a = \{a_1, a_2, \ldots, a_n\}.
\text{Suppose } a_1 \in a_2 \in \cdots \in a_n \in a_1.
\text{Then } (\forall x)[x \in a \rightarrow x \cap a \neq 0], \text{ contradicting Regularity.}""")

write_concept(S, "epsilon-induction", "proposition", "Epsilon-Induction Principle",
r"""(\forall x)[x \subseteq A \rightarrow x \in A] \rightarrow A = V""",
"Proposition 5.22: If a class $A$ contains every set whose elements are all in $A$, then $A = V$. This is the principle of $\in$-induction, fundamental for proofs by induction on the membership relation.",
chapter="5",
proof=r"""\text{Assume } (\forall x)[x \subseteq A \rightarrow x \in A].
\text{Let } B = V - A. \text{ If } B \neq 0, \text{ then by Regularity } (\exists a \in B)[a \cap B = 0].
\text{Then } (\forall y)[y \in a \rightarrow y \notin B], \text{ i.e., } a \subseteq A.
\text{By hypothesis } a \in A, \text{ contradicting } a \in B.
\text{Therefore } B = 0 \text{ and } A = V.""")

print(f"Created {3 + 11 + 18} concepts for s001-s003")
print("Done with chapters 1-5")
