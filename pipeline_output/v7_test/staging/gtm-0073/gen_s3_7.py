#!/usr/bin/env python3
"""Generate concept files for GTM073 Ch4 Sections 3-7."""
import os

BASE = "/home/a123/文档/mathpkg/pipeline_output/v7_test/staging/gtm-0073/gtm-0073_ch03_concepts"
DATE = "2026-06-24"
AGENT = "v7-gtm073"
BOOK = "gtm-0073"
AUTHOR = "Hungerford, Thomas W."
TITLE = "Algebra"
CH = "IV"

def w_yaml(dirname, id_, title_en, title_zh, typ, sub, diff, sec, role):
    d = os.path.join(BASE, dirname)
    os.makedirs(d, exist_ok=True)
    c = f'id: {id_}\ntitle_en: "{title_en}"\ntitle_zh: "{title_zh}"\ntype: {typ}\ndomain: algebra\nsubdomain: {sub}\ndifficulty: {diff}\ntags: []\ndepends_on:\n  required: []\n  recommended: []\n  suggested: []\nproof_deps: {{}}\nsource_books:\n  - book_id: {BOOK}\n    author: "{AUTHOR}"\n    title: "{TITLE}"\n    chapter: {CH}\n    section: "{sec}"\n    pages: ""\n    role_in_book: "{role}"\ncontent_hash: ""\nextraction_date: "{DATE}"\nextraction_agent: "{AGENT}"\n'
    with open(os.path.join(d, "concept.yaml"), "w") as f:
        f.write(c)

def w_tex(dn, content):
    with open(os.path.join(BASE, dn, "theorem.tex"), "w") as f:
        f.write(content)

def w_intro(dn, content):
    h = '---\nrole: introduce\nlocale: en\ncontent_hash: ""\nwritten_against: ""\n---\n'
    with open(os.path.join(BASE, dn, "introduce.en.md"), "w") as f:
        f.write(h + content)

def w_proof(dn, sec, tech, content):
    ss = sec.replace(".", "_")
    fn = f"proof_{BOOK}_IV_{ss}_{tech}.en.md"
    h = f'---\nrole: proof\nsource_book: {BOOK}\nchapter: {CH}\nsection: "{sec}"\nproof_technique: {tech}\nlocale: en\ncontent_hash: ""\nwritten_against: ""\n---\n'
    with open(os.path.join(BASE, dn, fn), "w") as f:
        f.write(h + content)

print("Generating sections 3-7...")
cnt = 26

# ============================================================
# SECTION 3: PROJECTIVE AND INJECTIVE MODULES
# ============================================================
sec = "IV.3"

w_yaml("projective-module","projective-module","Projective Module","投射模","definition","module-theory","intermediate",sec,"Definition 3.1")
w_tex("projective-module",'An $R$-module $P$ is said to be \\emph{projective} if given any diagram of $R$-module homomorphisms\n\\[\n\\begin{array}{ccc}\n& & P \\\\\n& & f \\downarrow \\\\\nA & \\xrightarrow{g} & B \\to 0\n\\end{array}\n\\]\nwith bottom row exact ($g$ an epimorphism), there exists an $R$-module homomorphism $h : P \\to A$ such that $gh = f$.\n')
w_intro("projective-module","A module $P$ is projective if every homomorphism from $P$ to a quotient $B$ lifts to a homomorphism from $P$ to $A$. This lifting property against epimorphisms characterizes projective objects categorically. Free modules are prototypical examples.\n"); cnt+=1

w_yaml("free-modules-are-projective","free-modules-are-projective","Every Free Module is Projective","每个自由模都是投射模","theorem","module-theory","basic",sec,"Theorem 3.2")
w_tex("free-modules-are-projective","Every free module $F$ over a ring $R$ with identity is projective.\n")
w_intro("free-modules-are-projective","Theorem 3.2 establishes that free modules satisfy the projective lifting property. Given a free module on $X$, any homomorphism $f: F \\to B$ lifts to $A$ by choosing preimages of generators under the epimorphism $g$.\n")
w_proof("free-modules-are-projective",sec,"lifting-via-generators","Given $g: A \\to B$ epi and $f: F \\to B$ with $F$ free on $X$ ($\\iota: X \\to F$). For each $x \\in X$, $f(\\iota(x)) \\in B$. Since $g$ is epi, there exists $a_x \\in A$ with $g(a_x) = f(\\iota(x))$. The map $X \\to A$ given by $x \\mapsto a_x$ induces $h: F \\to A$ such that $h(\\iota(x)) = a_x$. Then $gh(\\iota(x)) = g(a_x) = f(\\iota(x))$, so $gh\\iota = f\\iota$. By uniqueness in Theorem 2.1(iv), $gh = f$.\n"); cnt+=1

w_yaml("homomorphic-image-of-projective","homomorphic-image-of-projective","Every Module is a Homomorphic Image of a Projective Module","每个模都是投射模的同态像","corollary","module-theory","basic",sec,"Corollary 3.3")
w_tex("homomorphic-image-of-projective","Every module $A$ over a ring $R$ is the homomorphic image of a projective $R$-module.\n")
w_intro("homomorphic-image-of-projective","Corollary 3.3 follows from Theorem 3.2 and Corollary 2.2: every module is a quotient of a free module, and free modules are projective.\n"); cnt+=1

w_yaml("projective-module-equivalent-conditions","projective-module-equivalent-conditions","Equivalent Conditions for Projective Modules","投射模的等价条件","theorem","module-theory","intermediate",sec,"Theorem 3.4")
w_tex("projective-module-equivalent-conditions",'Let $R$ be a ring. The following conditions on an $R$-module $P$ are equivalent:\n\\begin{enumerate}\n\\item[(i)] $P$ is projective;\n\\item[(ii)] every short exact sequence $0 \\to A \\xrightarrow{f} B \\xrightarrow{g} P \\to 0$ is split exact (hence $B \\cong A \\oplus P$);\n\\item[(iii)] there is a free module $F$ and an $R$-module $K$ such that $F \\cong K \\oplus P$.\n\\end{enumerate}\n')
w_intro("projective-module-equivalent-conditions","Theorem 3.4 gives two equivalent characterizations: any short exact sequence ending in $P$ splits (ii), and $P$ is a direct summand of a free module (iii). These are fundamental for the theory of projective resolutions.\n")
w_proof("projective-module-equivalent-conditions",sec,"diagram-chase","(i) $\\Rightarrow$ (ii) Consider the diagram with $1_P: P \\to P$ and epi $g: B \\to P$. Projectivity gives $h: P \\to B$ with $gh = 1_P$, so the sequence splits by Theorem 1.18.\n\n(ii) $\\Rightarrow$ (iii) By Corollary 2.2, there is a free module $F$ and an epimorphism $F \\to P$. The short exact sequence $0 \\to K \\to F \\to P \\to 0$ splits by (ii), giving $F \\cong K \\oplus P$.\n\n(iii) $\\Rightarrow$ (i) $F \\cong K \\oplus P$ free implies $P$ is a direct summand of a projective module. Compose any map $f: P \\to B$ with the projection $F \\to P$, lift via projectivity of $F$, then restrict via the injection $P \\to F$.\n"); cnt+=1

w_yaml("direct-sum-projective-iff-summands-projective","direct-sum-projective-iff-summands-projective","A Direct Sum is Projective iff Each Summand is Projective","直和为投射模当且仅当每个直和项是投射模","proposition","module-theory","basic",sec,"Proposition 3.5")
w_tex("direct-sum-projective-iff-summands-projective","Let $R$ be a ring. A direct sum of $R$-modules $\\sum_{i \\in I} P_i$ is projective if and only if each $P_i$ is projective.\n")
w_intro("direct-sum-projective-iff-summands-projective","Projectivity is preserved under direct sums and inherited by summands. The proof uses the characterization of projectives as direct summands of free modules.\n"); cnt+=1

w_yaml("injective-module","injective-module","Injective Module","内射模","definition","module-theory","intermediate",sec,"Definition 3.6")
w_tex("injective-module",'An $R$-module $J$ is \\emph{injective} if given any diagram of $R$-module homomorphisms\n\\[\n\\begin{array}{ccc}\n0 \\to A & \\xrightarrow{g} & B \\\\\nf \\downarrow & & \\\\\nJ & &\n\\end{array}\n\\]\nwith top row exact ($g$ a monomorphism), there exists an $R$-module homomorphism $h : B \\to J$ such that $hg = f$.\n')
w_intro("injective-module","An injective module is dual to a projective module: instead of lifting against epimorphisms, maps extend along monomorphisms. Every homomorphism from a submodule $A$ into $J$ extends to the larger module $B$.\n"); cnt+=1

w_yaml("direct-product-injective-iff-factors-injective","direct-product-injective-iff-factors-injective","A Direct Product is Injective iff Each Factor is Injective","直积为内射模当且仅当每个因子是内射模","proposition","module-theory","basic",sec,"Proposition 3.7")
w_tex("direct-product-injective-iff-factors-injective","A direct product of $R$-modules $\\prod_{i \\in I} J_i$ is injective if and only if $J_i$ is injective for every $i \\in I$.\n")
w_intro("direct-product-injective-iff-factors-injective","Proposition 3.7 is the dual of Proposition 3.5. The direct product is injective precisely when each factor is injective.\n"); cnt+=1

w_yaml("injective-extension-from-left-ideals","injective-extension-from-left-ideals","Injective Module Characterization via Left Ideals (Baer's Criterion)","通过左理想刻画内射模（Baer判别法）","lemma","module-theory","intermediate",sec,"Lemma 3.8")
w_tex("injective-extension-from-left-ideals",'Let $R$ be a ring with identity. A unitary $R$-module $J$ is injective if and only if for every left ideal $L$ of $R$, any $R$-module homomorphism $L \\to J$ may be extended to an $R$-module homomorphism $R \\to J$.\n')
w_intro("injective-extension-from-left-ideals","Baer's Criterion reduces the verification of injectivity from arbitrary monomorphisms to extensions from left ideals of $R$. The proof uses Zorn's Lemma to extend a maximal partial extension.\n")
w_proof("injective-extension-from-left-ideals",sec,"zorns-lemma-extension","If $J$ is injective, the extension property holds by definition. Conversely, suppose $J$ has the extension property for left ideals. Given a diagram with $g: A \\to B$ mono and $f: A \\to J$, let $\\mathcal{S}$ be all homomorphisms $h: C \\to J$ where $\\operatorname{Im} g \\subset C \\subset B$, partially ordered by extension. Zorn's Lemma gives a maximal element $h: H \\to J$. If $H \\neq B$, pick $b \\in B - H$. Then $L = \\{r \\in R \\mid rb \\in H\\}$ is a left ideal. The map $L \\to J$, $r \\mapsto h(rb)$, extends to $k: R \\to J$ by hypothesis. With $c = k(1_R)$, define $\\bar{h}: H + Rb \\to J$ by $a + rb \\mapsto h(a) + rc$, which extends $h$ properly, contradicting maximality. Hence $H = B$.\n"); cnt+=1

w_yaml("injective-z-modules-are-divisible","injective-z-modules-are-divisible","Injective Z-Modules are Divisible Abelian Groups","内射Z-模是可除阿贝尔群","lemma","module-theory","intermediate",sec,"Lemma 3.9")
w_tex("injective-z-modules-are-divisible","A unitary $\\mathbb{Z}$-module $D$ is injective if and only if $D$ is a divisible abelian group.\n")
w_intro("injective-z-modules-are-divisible","Lemma 3.9 characterizes injective abelian groups as precisely the divisible groups. The only left ideals of $\\mathbb{Z}$ are principal, and extending a map $\\langle n \\rangle \\to D$ is equivalent to solving $nx = f(n)$ in $D$.\n")
w_proof("injective-z-modules-are-divisible",sec,"baer-criterion","($\\Rightarrow$) If $D$ is injective and $d \\in D$, define $f: \\langle n \\rangle \\to D$ by $f(n) = d$. By Lemma 3.8, extend to $h: \\mathbb{Z} \\to D$. Let $x = h(1)$; then $nx = nh(1) = h(n) = f(n) = d$, so $D$ is divisible.\n\n($\\Leftarrow$) If $D$ is divisible and $f: \\langle n \\rangle \\to D$, there exists $x \\in D$ with $nx = f(n)$. Define $h: \\mathbb{Z} \\to D$ by $1 \\mapsto x$, which extends $f$. By Lemma 3.8, $D$ is injective.\n"); cnt+=1

w_yaml("embedding-in-divisible-abelian-group","embedding-in-divisible-abelian-group","Every Abelian Group Can Be Embedded in a Divisible Group","每个阿贝尔群可嵌入可除群","lemma","module-theory","intermediate",sec,"Lemma 3.10")
w_tex("embedding-in-divisible-abelian-group","Every abelian group $A$ may be embedded in a divisible abelian group.\n")
w_intro("embedding-in-divisible-abelian-group","Lemma 3.10 shows every abelian group embeds in a divisible (hence injective) group. The proof uses $A \\cong F/K$ with $F$ free, embeds $F$ in a direct sum $D$ of copies of $\\mathbb{Q}$, then notes $D/f(K)$ stays divisible.\n"); cnt+=1

w_yaml("extension-from-left-ideals-via-hom","extension-from-left-ideals-via-hom","Extension from Left Ideals via Hom_Z(R,J)","通过Hom_Z(R,J)从左理想扩张","lemma","module-theory","advanced",sec,"Lemma 3.11")
w_tex("extension-from-left-ideals-via-hom","If $R$ is a ring with identity and $J$ is a divisible abelian group, then $\\operatorname{Hom}_{\\mathbb{Z}}(R,J)$ is an injective left $R$-module.\n")
w_intro("extension-from-left-ideals-via-hom","Lemma 3.11 constructs an important injective: if $J$ is a divisible group, $\\operatorname{Hom}_{\\mathbb{Z}}(R,J)$ with the $R$-module structure $(rf)(x) = f(xr)$ is injective. This is the coinduction functor preserving injectivity.\n"); cnt+=1

w_yaml("embedding-in-injective-module","embedding-in-injective-module","Every Module Can Be Embedded in an Injective Module","每个模可嵌入内射模","proposition","module-theory","intermediate",sec,"Proposition 3.12")
w_tex("embedding-in-injective-module","Every unitary module $A$ over a ring $R$ with identity may be embedded in an injective $R$-module.\n")
w_intro("embedding-in-injective-module","Proposition 3.12 is the dual of Corollary 3.3. Every module embeds in an injective module. The proof uses Lemma 3.10 to embed the underlying abelian group in a divisible group, then maps into $\\operatorname{Hom}_{\\mathbb{Z}}(R,J)$.\n"); cnt+=1

w_yaml("injective-module-equivalent-conditions","injective-module-equivalent-conditions","Equivalent Conditions for Injective Modules","内射模的等价条件","proposition","module-theory","intermediate",sec,"Proposition 3.13")
w_tex("injective-module-equivalent-conditions",'The following conditions on a unitary module $J$ over a ring $R$ with identity are equivalent:\n\\begin{enumerate}\n\\item[(i)] $J$ is injective;\n\\item[(ii)] every short exact sequence $0 \\to J \\to B \\to C \\to 0$ is split exact (hence $B \\cong J \\oplus C$);\n\\item[(iii)] $J$ is a direct summand of any module $B$ containing $J$ as a submodule.\n\\end{enumerate}\n')
w_intro("injective-module-equivalent-conditions","Proposition 3.13 is the dual of Theorem 3.4. An injective module is always a direct summand of any containing module, and any short exact sequence beginning with $J$ splits.\n"); cnt+=1

print(f"Section 3 done. Count: {cnt}")

# ============================================================
# SECTION 4: HOM AND DUAL MODULES
# ============================================================
sec = "IV.4"

w_yaml("hom-left-exactness-covariant","hom-left-exactness-covariant","Left Exactness of Hom in the Covariant Argument","Hom在协变变元的左正合性","theorem","module-theory","intermediate",sec,"Theorem 4.2")
w_tex("hom-left-exactness-covariant",'Let $R$ be a ring. $0 \\to A \\xrightarrow{\\varphi} B \\xrightarrow{\\psi} C$ is an exact sequence of $R$-modules if and only if for every $R$-module $D$,\n\\[\n0 \\to \\operatorname{Hom}_R(D, A) \\xrightarrow{\\bar{\\varphi}} \\operatorname{Hom}_R(D, B) \\xrightarrow{\\bar{\\psi}} \\operatorname{Hom}_R(D, C)\n\\]\nis an exact sequence of abelian groups (where $\\bar{\\varphi}(f) = \\varphi f$ and $\\bar{\\psi}(g) = \\psi g$).\n')
w_intro("hom-left-exactness-covariant","The Hom functor is left exact in the second variable: it preserves monomorphisms and kernels. This is fundamental to homological algebra. The short exact sequence does not extend to $\\to 0$ in general.\n")
w_proof("hom-left-exactness-covariant",sec,"kernel-chase","($\\Rightarrow$) (i) $\\operatorname{Ker} \\bar{\\varphi} = 0$: if $\\varphi f = 0$, then $\\varphi(f(x)) = 0$ for all $x$. Since $\\varphi$ is mono, $f(x) = 0$, so $f = 0$. (ii) $\\operatorname{Im} \\bar{\\varphi} \\subset \\operatorname{Ker} \\bar{\\psi}$: $\\psi\\varphi = 0$ implies $\\bar{\\psi}\\bar{\\varphi} = 0$. (iii) $\\operatorname{Ker} \\bar{\\psi} \\subset \\operatorname{Im} \\bar{\\varphi}$: if $\\psi g = 0$, then $\\operatorname{Im} g \\subset \\operatorname{Ker} \\psi = \\operatorname{Im} \\varphi$. Since $\\varphi$ is mono, for each $d \\in D$ there is a unique $a \\in A$ with $g(d) = \\varphi(a)$. Define $f(d) = a$; verify $f$ is a homomorphism and $\\bar{\\varphi}(f) = g$.\n\n($\\Leftarrow$) Given exactness of Hom for all $D$, take $D = \\operatorname{Ker} \\varphi$ to show $\\varphi$ is mono, and $D = B/\\operatorname{Im} \\varphi$ to show $\\operatorname{Im} \\varphi = \\operatorname{Ker} \\psi$.\n"); cnt+=1

w_yaml("hom-left-exactness-contravariant","hom-left-exactness-contravariant","Left Exactness of Hom in the Contravariant Argument","Hom在反变变元的左正合性","theorem","module-theory","intermediate",sec,"Theorem 4.3")
w_tex("hom-left-exactness-contravariant",'Let $R$ be a ring. $A \\xrightarrow{\\theta} B \\xrightarrow{\\zeta} C \\to 0$ is an exact sequence of $R$-modules if and only if for every $R$-module $D$,\n\\[\n0 \\to \\operatorname{Hom}_R(C, D) \\xrightarrow{\\bar{\\zeta}} \\operatorname{Hom}_R(B, D) \\xrightarrow{\\bar{\\theta}} \\operatorname{Hom}_R(A, D)\n\\]\nis an exact sequence of abelian groups (where $\\bar{\\zeta}(f) = f\\zeta$ and $\\bar{\\theta}(g) = g\\theta$).\n')
w_intro("hom-left-exactness-contravariant","Theorem 4.3 is the dual of Theorem 4.2. The contravariant Hom functor $\\operatorname{Hom}_R(-, D)$ preserves cokernels, sending an exact sequence $A \\to B \\to C \\to 0$ to an exact sequence of abelian groups.\n"); cnt+=1

w_yaml("split-exact-preserved-by-hom","split-exact-preserved-by-hom","Split Exact Sequences are Preserved by Hom","Hom保持分裂正合列","proposition","module-theory","intermediate",sec,"Proposition 4.4")
w_tex("split-exact-preserved-by-hom",'The following conditions on modules over a ring $R$ are equivalent:\n\\begin{enumerate}\n\\item[(i)] $0 \\to A \\xrightarrow{\\varphi} B \\xrightarrow{\\psi} C \\to 0$ is a split exact sequence;\n\\item[(ii)] $0 \\to \\operatorname{Hom}_R(D,A) \\xrightarrow{\\bar{\\varphi}} \\operatorname{Hom}_R(D,B) \\xrightarrow{\\bar{\\psi}} \\operatorname{Hom}_R(D,C) \\to 0$ is a split exact sequence for every $D$;\n\\item[(iii)] $0 \\to \\operatorname{Hom}_R(C,D) \\xrightarrow{\\bar{\\psi}} \\operatorname{Hom}_R(B,D) \\xrightarrow{\\bar{\\varphi}} \\operatorname{Hom}_R(A,D) \\to 0$ is a split exact sequence for every $D$.\n\\end{enumerate}\n')
w_intro("split-exact-preserved-by-hom","Split exact sequences are preserved by both the covariant and contravariant Hom functors. While Hom is only left exact in general, split exactness guarantees the full exact sequence ending in $\\to 0$.\n"); cnt+=1

w_yaml("projective-characterization-via-hom","projective-characterization-via-hom","Projective Module Characterization via Hom","通过Hom刻画投射模","theorem","module-theory","intermediate",sec,"Theorem 4.5")
w_tex("projective-characterization-via-hom",'The following conditions on a module $P$ over a ring $R$ are equivalent:\n\\begin{enumerate}\n\\item[(i)] $P$ is projective;\n\\item[(ii)] if $\\psi : B \\to C$ is any $R$-module epimorphism, then $\\bar{\\psi} : \\operatorname{Hom}_R(P, B) \\to \\operatorname{Hom}_R(P, C)$ is an epimorphism;\n\\item[(iii)] if $0 \\to A \\to B \\to C \\to 0$ is any short exact sequence, then $0 \\to \\operatorname{Hom}_R(P, A) \\to \\operatorname{Hom}_R(P, B) \\to \\operatorname{Hom}_R(P, C) \\to 0$ is exact.\n\\end{enumerate}\n')
w_intro("projective-characterization-via-hom","$P$ is projective precisely when $\\operatorname{Hom}_R(P, -)$ preserves epimorphisms, or equivalently when it preserves short exact sequences. This bridges the categorical definition of projectivity with homological algebra.\n"); cnt+=1

w_yaml("injective-characterization-via-hom","injective-characterization-via-hom","Injective Module Characterization via Hom","通过Hom刻画内射模","proposition","module-theory","intermediate",sec,"Proposition 4.6")
w_tex("injective-characterization-via-hom",'The following conditions on a module $J$ over a ring $R$ are equivalent:\n\\begin{enumerate}\n\\item[(i)] $J$ is injective;\n\\item[(ii)] if $\\theta : A \\to B$ is any $R$-module monomorphism, then $\\bar{\\theta} : \\operatorname{Hom}_R(B, J) \\to \\operatorname{Hom}_R(A, J)$ is an epimorphism;\n\\item[(iii)] if $0 \\to A \\to B \\to C \\to 0$ is any short exact sequence, then $0 \\to \\operatorname{Hom}_R(C, J) \\to \\operatorname{Hom}_R(B, J) \\to \\operatorname{Hom}_R(A, J) \\to 0$ is exact.\n\\end{enumerate}\n')
w_intro("injective-characterization-via-hom","Proposition 4.6 is the dual of Theorem 4.5. $J$ is injective precisely when $\\operatorname{Hom}_R(-, J)$ sends monomorphisms to epimorphisms.\n"); cnt+=1

w_yaml("hom-isomorphisms-for-sum-and-product","hom-isomorphisms-for-sum-and-product","Hom Isomorphisms for Direct Sums and Products","Hom关于直和与直积的同构","theorem","module-theory","intermediate",sec,"Theorem 4.7")
w_tex("hom-isomorphisms-for-sum-and-product",'Let $A, B, \\{A_i\\}, \\{B_j\\}$ be modules over a ring $R$. Then:\n\\begin{enumerate}\n\\item[(i)] $\\operatorname{Hom}_R(\\sum A_i, B) \\cong \\prod \\operatorname{Hom}_R(A_i, B)$;\n\\item[(ii)] $\\operatorname{Hom}_R(A, \\prod B_j) \\cong \\prod \\operatorname{Hom}_R(A, B_j)$.\n\\end{enumerate}\n')
w_intro("hom-isomorphisms-for-sum-and-product","Hom from a direct sum is the product of Homs, and Hom into a direct product is the product of Homs. These are fundamental adjunction relations.\n"); cnt+=1

w_yaml("hom-as-bimodule","hom-as-bimodule","The Hom-Set as a Bimodule","Hom集作为双模","theorem","module-theory","intermediate",sec,"Theorem 4.8")
w_tex("hom-as-bimodule",'Let $R$ and $S$ be rings and let ${}_R A_S$, ${}_R B$, ${}_R C_S$, ${}_R D$ be (bi)modules.\n\\begin{enumerate}\n\\item[(i)] $\\operatorname{Hom}_R(A,B)$ is a right $S$-module, with $(fs)(a) = (f(a))s$.\n\\item[(ii)] If $\\varphi : A \\to A\'$ is an $R$-module homomorphism, then $\\bar{\\varphi} : \\operatorname{Hom}_R(A\',B) \\to \\operatorname{Hom}_R(A,B)$ is a homomorphism of right $S$-modules.\n\\item[(iii)] $\\operatorname{Hom}_R(C,D)$ is a left $S$-module, with $(sg)(c) = g(cs)$.\n\\item[(iv)] If $\\psi : D \\to D\'$ is an $R$-module homomorphism, then $\\bar{\\psi} : \\operatorname{Hom}_R(C,D) \\to \\operatorname{Hom}_R(C,D\')$ is a homomorphism of left $S$-modules.\n\\end{enumerate}\n')
w_intro("hom-as-bimodule","When modules carry bimodule structures, the Hom sets inherit module structures over the second ring. This is essential for the study of dual modules and adjunctions.\n"); cnt+=1

w_yaml("dual-module-properties","dual-module-properties","Properties of the Dual Module","对偶模的性质","theorem","module-theory","intermediate",sec,"Theorem 4.10")
w_tex("dual-module-properties",'Let $A, B$ be left modules over a ring $R$ and $A^* = \\operatorname{Hom}_R(A,R)$.\n\\begin{enumerate}\n\\item[(i)] If $\\varphi : A \\to C$ is a left $R$-module homomorphism, $\\bar{\\varphi} : C^* \\to A^*$ is a homomorphism of right $R$-modules.\n\\item[(ii)] $(A \\oplus C)^* \\cong A^* \\oplus C^*$.\n\\item[(iii)] If $R$ is a division ring and $0 \\to A \\to B \\to C \\to 0$ is exact, then $0 \\to C^* \\to B^* \\to A^* \\to 0$ is exact.\n\\end{enumerate}\n')
w_intro("dual-module-properties","The dual module $A^* = \\operatorname{Hom}_R(A,R)$ enjoys important properties. Dualization sends left modules to right modules, respects direct sums, and over division rings preserves short exact sequences.\n"); cnt+=1

w_yaml("dual-of-free-module","dual-of-free-module","The Dual of a Free Module","自由模的对偶","theorem","module-theory","intermediate",sec,"Theorem 4.11")
w_tex("dual-of-free-module",'Let $F$ be a free left $R$-module with finite basis $X = \\{x_1,\\ldots,x_n\\}$ over a ring $R$ with identity. For each $x \\in X$, define $f_x : F \\to R$ by $f_x(\\sum r_i x_i) = r_x$. Then $\\{f_x \\mid x \\in X\\}$ is a basis of the right $R$-module $F^*$, and $F^*$ is a free right $R$-module of the same rank as $F$.\n')
w_intro("dual-of-free-module","The dual of a finitely generated free module is again free, with the coordinate functionals forming a basis. This generalizes the dual basis in linear algebra.\n")
w_proof("dual-of-free-module",sec,"coordinate-functional-basis","Given $f \\in F^*$, let $s_i = f(x_i) \\in R$. For any $u = \\sum r_i x_i$, $\\langle u, f \\rangle = \\sum r_i s_i$. On the other hand, $\\langle u, \\sum f_i s_i \\rangle = \\sum r_i s_i$. Thus $f = \\sum f_i s_i$, so $\\{f_i\\}$ generates $F^*$. Linear independence: if $\\sum f_i r_i = 0$, evaluate at $x_j$ to get $r_j = 0$. Hence $\\{f_x\\}$ is a basis.\n"); cnt+=1

w_yaml("double-dual-and-reflexive-modules","double-dual-and-reflexive-modules","The Double Dual and Reflexive Modules","双重对偶与自反模","theorem","module-theory","intermediate",sec,"Theorem 4.12")
w_tex("double-dual-and-reflexive-modules",'Let $A$ be a left module over a ring $R$.\n\\begin{enumerate}\n\\item[(i)] There is an $R$-module homomorphism $\\theta : A \\to A^{**}$.\n\\item[(ii)] If $R$ has an identity and $A$ is free, then $\\theta$ is a monomorphism.\n\\item[(iii)] If $R$ has an identity and $A$ is free with a finite basis, then $\\theta$ is an isomorphism.\n\\end{enumerate}\nA module $A$ such that $\\theta : A \\to A^{**}$ is an isomorphism is said to be \\emph{reflexive}.\n')
w_intro("double-dual-and-reflexive-modules","There is a natural evaluation map $\\theta: A \\to A^{**}$ defined by $\\theta(a)(f) = f(a)$. For free modules this is injective; for finitely generated free modules it is an isomorphism (reflexive). This generalizes the fact that a finite-dimensional vector space is naturally isomorphic to its double dual.\n"); cnt+=1

print(f"Section 4 done. Count: {cnt}")

# ============================================================
# SECTION 5: TENSOR PRODUCTS
# ============================================================
sec = "IV.5"

w_yaml("tensor-product","tensor-product","Tensor Product of Modules","模的张量积","definition","module-theory","intermediate",sec,"Definition 5.1")
w_tex("tensor-product",'Let $A$ be a right module and $B$ a left module over a ring $R$. Let $F$ be the free abelian group on $A \\times B$. Let $K$ be the subgroup of $F$ generated by all elements:\n\\begin{enumerate}\n\\item[(i)] $(a + a\',b) - (a,b) - (a\',b)$;\n\\item[(ii)] $(a,b + b\') - (a,b) - (a,b\')$;\n\\item[(iii)] $(ar,b) - (a,rb)$.\n\\end{enumerate}\nThe quotient $F/K$ is the \\emph{tensor product} $A \\otimes_R B$. The coset $(a,b) + K$ is denoted $a \\otimes b$.\n')
w_intro("tensor-product","The tensor product $A \\otimes_R B$ is the universal middle linear construction on $A \\times B$. It is the quotient of the free abelian group on $A \\times B$ by relations enforcing bilinearity and the balanced condition $(ar) \\otimes b = a \\otimes (rb)$.\n"); cnt+=1

w_yaml("tensor-product-universal-property","tensor-product-universal-property","Universal Property of the Tensor Product","张量积的万有性质","theorem","module-theory","intermediate",sec,"Theorem 5.2")
w_tex("tensor-product-universal-property",'Let $A_R$ and ${}_R B$ be modules over a ring $R$, and let $C$ be an abelian group. If $g : A \\times B \\to C$ is a middle linear map, then there exists a unique group homomorphism $\\bar{g} : A \\otimes_R B \\to C$ such that $\\bar{g}(a \\otimes b) = g(a,b)$. $A \\otimes_R B$ is uniquely determined up to isomorphism by this property.\n')
w_intro("tensor-product-universal-property","Theorem 5.2 is the fundamental universal property of the tensor product: any middle linear map factors uniquely through $A \\otimes_R B$. This characterizes the tensor product up to unique isomorphism.\n")
w_proof("tensor-product-universal-property",sec,"universal-property","Let $F$ be the free abelian group on $A \\times B$ and $K$ as in Definition 5.1. The assignment $(a,b) \\mapsto g(a,b)$ determines a unique homomorphism $g_1: F \\to C$. Since $g$ is middle linear, $g_1$ maps every generator of $K$ to 0, so $K \\subset \\operatorname{Ker} g_1$. By Theorem 1.7, $g_1$ induces $\\bar{g}: F/K \\to C$ with $\\bar{g}[(a,b) + K] = g(a,b)$. But $F/K = A \\otimes_R B$ and $(a,b) + K = a \\otimes b$. Uniqueness follows because elementary tensors generate $A \\otimes_R B$.\n"); cnt+=1

w_yaml("tensor-product-right-exactness","tensor-product-right-exactness","Right Exactness of the Tensor Product","张量积的右正合性","theorem","module-theory","intermediate",sec,"Theorem 5.4")
w_tex("tensor-product-right-exactness",'If $A \\xrightarrow{f} B \\xrightarrow{g} C \\to 0$ is an exact sequence of left $R$-modules, then for every right $R$-module $D$,\n\\[\nD \\otimes_R A \\xrightarrow{1_D \\otimes f} D \\otimes_R B \\xrightarrow{1_D \\otimes g} D \\otimes_R C \\to 0\n\\]\nis an exact sequence of abelian groups. An analogous statement holds for an exact sequence in the first variable.\n')
w_intro("tensor-product-right-exactness","The tensor product is right exact: it preserves cokernels and epimorphisms, but not necessarily kernels. This is the dual of the left exactness of Hom and fundamental to homological algebra.\n"); cnt+=1

w_yaml("tensor-product-as-bimodule","tensor-product-as-bimodule","Tensor Product as a Bimodule","张量积作为双模","theorem","module-theory","intermediate",sec,"Theorem 5.5")
w_tex("tensor-product-as-bimodule","If $A$ is a left $S$-right $R$ bimodule and $B$ a left $R$-module, then $A \\otimes_R B$ is a left $S$-module with $s(a \\otimes b) = (sa) \\otimes b$. Similarly, if $A$ is a right $R$-module and $B$ a left $R$-right $S$ bimodule, then $A \\otimes_R B$ is a right $S$-module.\n")
w_intro("tensor-product-as-bimodule","When factors carry bimodule structures, the tensor product inherits a module structure over the extra ring. Over a commutative ring, $A \\otimes_R B$ is an $R$-$R$ bimodule with $r(a \\otimes b) = (ra) \\otimes b = a \\otimes (rb)$.\n"); cnt+=1

w_yaml("tensor-product-bilinear-maps-commutative","tensor-product-bilinear-maps-commutative","Universal Property for Bilinear Maps over Commutative Rings","交换环上双线性映射的万有性质","theorem","module-theory","intermediate",sec,"Theorem 5.6")
w_tex("tensor-product-bilinear-maps-commutative",'Let $A, B, C$ be modules over a commutative ring $R$. If $f: A \\times B \\to C$ is an $R$-bilinear map, then there exists a unique $R$-module homomorphism $\\bar{f}: A \\otimes_R B \\to C$ such that $\\bar{f}(a \\otimes b) = f(a,b)$. $A \\otimes_R B$ is uniquely determined up to $R$-module isomorphism.\n')
w_intro("tensor-product-bilinear-maps-commutative","Over a commutative ring, the tensor product satisfies a stronger universal property: $R$-bilinear maps from $A \\times B$ correspond uniquely to $R$-module homomorphisms from $A \\otimes_R B$.\n"); cnt+=1

w_yaml("tensor-with-ring-isomorphism","tensor-with-ring-isomorphism","Tensoring with the Base Ring","与基环作张量积","theorem","module-theory","basic",sec,"Theorem 5.7")
w_tex("tensor-with-ring-isomorphism",'If $R$ is a ring with identity and $A_R$, ${}_R B$ are unitary $R$-modules, then there are $R$-module isomorphisms\n\\[\nA \\otimes_R R \\cong A \\quad \\text{and} \\quad R \\otimes_R B \\cong B.\n\\]')
w_intro("tensor-with-ring-isomorphism","Tensoring with the base ring $R$ recovers the original module: $A \\otimes_R R \\cong A$ via $a \\otimes r \\mapsto ar$. This is the module-theoretic analogue of multiplying by 1.\n"); cnt+=1

w_yaml("associativity-of-tensor-product","associativity-of-tensor-product","Associativity of the Tensor Product","张量积的结合性","theorem","module-theory","intermediate",sec,"Theorem 5.8")
w_tex("associativity-of-tensor-product",'Let $R$ and $S$ be rings and $A_R$, ${}_R B_S$, ${}_S C$ (bi)modules. Then there is an isomorphism\n\\[\n(A \\otimes_R B) \\otimes_S C \\cong A \\otimes_R (B \\otimes_S C)\n\\]\ngiven by $(a \\otimes b) \\otimes c \\mapsto a \\otimes (b \\otimes c)$.\n')
w_intro("associativity-of-tensor-product","The tensor product is associative up to natural isomorphism. This allows unambiguous iteration of tensor products. The proof constructs mutual inverse homomorphisms using the universal property.\n"); cnt+=1

w_yaml("tensor-product-distributivity-over-direct-sum","tensor-product-distributivity-over-direct-sum","Distributivity of Tensor Product over Direct Sums","张量积对直和的分配性","theorem","module-theory","intermediate",sec,"Theorem 5.9")
w_tex("tensor-product-distributivity-over-direct-sum",'Let $R$ be a ring. There are isomorphisms:\n\\[\n\\left(\\sum_{i \\in I} A_i\\right) \\otimes_R B \\cong \\sum_{i \\in I} (A_i \\otimes_R B) \\quad \\text{and} \\quad A \\otimes_R \\left(\\sum_{j \\in J} B_j\\right) \\cong \\sum_{j \\in J} (A \\otimes_R B_j).\n\\]')
w_intro("tensor-product-distributivity-over-direct-sum","Theorem 5.9 states that the tensor product distributes over direct sums. This is a central structural result used in computations with free and projective modules.\n"); cnt+=1

w_yaml("hom-tensor-adjunction","hom-tensor-adjunction","Adjoint Associativity (Hom-Tensor Adjunction)","Hom-张量伴随性","theorem","module-theory","advanced",sec,"Theorem 5.10")
w_tex("hom-tensor-adjunction",'Let $R$ and $S$ be rings and $A_R$, ${}_R B_S$, ${}_S C$ (bi)modules. Then there is an isomorphism\n\\[\n\\operatorname{Hom}_S(A \\otimes_R B, C) \\cong \\operatorname{Hom}_R(A, \\operatorname{Hom}_S(B, C)).\n\\]')
w_intro("hom-tensor-adjunction","The Hom-Tensor adjunction is one of the most important isomorphisms in module theory. It is the foundation of much of homological algebra and category theory.\n"); cnt+=1

w_yaml("tensor-with-free-module-structure","tensor-with-free-module-structure","Structure of the Tensor Product with a Free Module","与自由模的张量积的结构","theorem","module-theory","intermediate",sec,"Theorem 5.11")
w_tex("tensor-with-free-module-structure",'Let $R$ be a ring with identity. If $A$ is a unitary right $R$-module and $F$ is a free left $R$-module with basis $Y$, then every element $u \\in A \\otimes_R F$ may be written uniquely as $u = \\sum_{i=1}^{n} a_i \\otimes y_i$, where $a_i \\in A$ and the $y_i$ are distinct elements of $Y$.\n')
w_intro("tensor-with-free-module-structure","When one factor is free, every element of the tensor product can be written uniquely as a finite sum $\\sum a_i \\otimes y_i$ with distinct basis elements $y_i$. This is proved via an isomorphism to a direct sum of copies of $A$.\n")
w_proof("tensor-with-free-module-structure",sec,"direct-sum-isomorphism","For each $y \\in Y$, let $A_y$ be a copy of $A$ and consider $\\sum_{y \\in Y} A_y$. Since $\\{y\\}$ is linearly independent, $\\varphi: R \\to Ry$ is an isomorphism, inducing $A \\cong A \\otimes_R Ry$. Summing over $Y$ and using Theorem 5.9 yields $A \\otimes_R F \\cong \\sum A_y$. Under this isomorphism, $a \\otimes y$ corresponds to $a$ in the $y$-th coordinate.\n"); cnt+=1

w_yaml("tensor-product-of-free-modules-is-free","tensor-product-of-free-modules-is-free","Tensor Product of Free Modules is Free","自由模的张量积是自由模","theorem","module-theory","intermediate",sec,"Theorem 5.12")
w_tex("tensor-product-of-free-modules-is-free","If $A$ is a free right $R$-module with basis $X$ and $B$ is a free left $R$-module with basis $Y$, then $A \\otimes_R B$ is a free $R$-module with basis $\\{x \\otimes y \\mid x \\in X, y \\in Y\\}$ of cardinality $|X||Y|$.\n")
w_intro("tensor-product-of-free-modules-is-free","The tensor product of free modules is again free, with basis given by pairwise tensor products of the original bases. The rank multiplies.\n"); cnt+=1

w_yaml("extension-of-scalars-for-free-modules","extension-of-scalars-for-free-modules","Extension of Scalars for Free Modules","自由模的标量扩张","corollary","module-theory","intermediate",sec,"Corollary 5.13")
w_tex("extension-of-scalars-for-free-modules","Let $S$ be a ring with identity and $R$ a subring of $S$ containing $1_S$. If $F$ is a free left $R$-module with basis $X$, then $S \\otimes_R F$ is a free left $S$-module with basis $\\{1_S \\otimes x \\mid x \\in X\\}$ of cardinality $|X|$.\n")
w_intro("extension-of-scalars-for-free-modules","Corollary 5.13 describes extension of scalars: tensoring a free $R$-module with $S$ over $R$ yields a free $S$-module of the same rank. This is the module-theoretic analogue of extending scalars for vector spaces.\n"); cnt+=1

print(f"Section 5 done. Count: {cnt}")

# ============================================================
# SECTION 6: MODULES OVER A PRINCIPAL IDEAL DOMAIN
# ============================================================
sec = "IV.6"

w_yaml("submodules-of-free-modules-over-pid-are-free","submodules-of-free-modules-over-pid-are-free","Submodules of Free Modules over a PID are Free","PID上自由模的子模是自由模","theorem","module-theory","intermediate",sec,"Theorem 6.1")
w_tex("submodules-of-free-modules-over-pid-are-free","Let $R$ be a principal ideal domain. Then every submodule $G$ of a free $R$-module $F$ is itself a free $R$-module, and $\\operatorname{rank} G \\leq \\operatorname{rank} F$.\n")
w_intro("submodules-of-free-modules-over-pid-are-free","Theorem 6.1 is a cornerstone result: over a PID, submodules of free modules are free. This generalizes the fact that subgroups of free abelian groups are free, and is essential for the structure theory of finitely generated modules over PIDs.\n"); cnt+=1

w_yaml("projective-iff-free-over-pid","projective-iff-free-over-pid","Finitely Generated Modules over a PID: Projective iff Free","PID上有限生成模：投射当且仅当自由","theorem","module-theory","intermediate",sec,"Theorem 6.3")
w_tex("projective-iff-free-over-pid","Let $R$ be a principal ideal domain. A finitely generated $R$-module is projective if and only if it is free.\n")
w_intro("projective-iff-free-over-pid","For finitely generated modules over a PID, projective and free coincide. A projective is a direct summand of a free module, and submodules of free modules over a PID are free (Theorem 6.1).\n"); cnt+=1

w_yaml("order-ideal-and-torsion-submodule","order-ideal-and-torsion-submodule","Order Ideal and the Torsion Submodule","阶理想与挠子模","theorem","module-theory","intermediate",sec,"Theorem 6.4")
w_tex("order-ideal-and-torsion-submodule",'Let $A$ be a left module over an integral domain $R$ and $\\mathcal{O}_a = \\{r \\in R \\mid ra = 0\\}$.\n\\begin{enumerate}\n\\item[(i)] $\\mathcal{O}_a$ is an ideal of $R$.\n\\item[(ii)] $A_t = \\{a \\in A \\mid \\mathcal{O}_a \\neq 0\\}$ is the \\emph{torsion submodule} of $A$.\n\\item[(iii)] $R/\\mathcal{O}_a \\cong Ra$.\n\\item[(iv)] If $R$ is a PID, $p \\in R$ prime, and $p^i a = 0$, then $\\mathcal{O}_a = (p^j)$ with $0 \\leq j \\leq i$.\n\\item[(v)] If $\\mathcal{O}_a = (p^i)$, then $p^j a \\neq 0$ for $0 \\leq j < i$.\n\\end{enumerate}\n')
w_intro("order-ideal-and-torsion-submodule","The order ideal $\\mathcal{O}_a = \\{r \\mid ra = 0\\}$ generalizes the order of an element in a group. The torsion submodule $A_t$ consists of elements with nonzero order ideals. Over a PID, cyclic modules are isomorphic to $R/\\mathcal{O}_a$.\n"); cnt+=1

w_yaml("finitely-generated-torsion-free-over-pid-is-free","finitely-generated-torsion-free-over-pid-is-free","Finitely Generated Torsion-Free Modules over a PID are Free","PID上有限生成无挠模是自由模","theorem","module-theory","intermediate",sec,"Theorem 6.5")
w_tex("finitely-generated-torsion-free-over-pid-is-free","A finitely generated torsion-free module $A$ over a principal ideal domain $R$ is free.\n")
w_intro("finitely-generated-torsion-free-over-pid-is-free","Over a PID, finitely generated torsion-free modules are free. This generalizes the fact that finitely generated torsion-free abelian groups are free. The proof selects a maximal linearly independent subset and shows it spans after scaling.\n"); cnt+=1

w_yaml("torsion-torsion-free-decomposition","torsion-torsion-free-decomposition","Decomposition into Torsion and Torsion-Free Parts","挠部分与无挠部分的分解","theorem","module-theory","intermediate",sec,"Theorem 6.6")
w_tex("torsion-torsion-free-decomposition","If $A$ is a finitely generated module over a principal ideal domain $R$, then $A = A_t \\oplus F$, where $A_t$ is the torsion submodule and $F$ is a free $R$-module of finite rank. The rank of $F$ is uniquely determined by $A$.\n")
w_intro("torsion-torsion-free-decomposition","Every finitely generated module over a PID decomposes into its torsion part and a free part. $A/A_t$ is torsion-free, hence free (Theorem 6.5), and the exact sequence $0 \\to A_t \\to A \\to A/A_t \\to 0$ splits.\n"); cnt+=1

w_yaml("primary-decomposition-of-torsion-module","primary-decomposition-of-torsion-module","Primary Decomposition of a Torsion Module over a PID","PID上挠模的准素分解","theorem","module-theory","intermediate",sec,"Theorem 6.7")
w_tex("primary-decomposition-of-torsion-module",'Let $A$ be a torsion module over a PID $R$ and $A(p) = \\{a \\in A \\mid a \\text{ has order a power of } p\\}$.\n\\begin{enumerate}\n\\item[(i)] $A(p)$ is a submodule of $A$ for each prime $p \\in R$;\n\\item[(ii)] $A = \\sum A(p)$, where the sum is over all primes $p \\in R$. If $A$ is finitely generated, only finitely many $A(p)$ are nonzero.\n\\end{enumerate}\n')
w_intro("primary-decomposition-of-torsion-module","A torsion module decomposes into $p$-primary components $A(p)$, each consisting of elements annihilated by some power of $p$. The proof uses the Chinese Remainder Theorem to write $1_R$ as a linear combination of coprime elements.\n"); cnt+=1

w_yaml("cyclic-prime-power-order-properties","cyclic-prime-power-order-properties","Properties of Cyclic Modules of Prime Power Order","素幂阶循环模的性质","lemma","module-theory","intermediate",sec,"Lemma 6.8")
w_tex("cyclic-prime-power-order-properties",'Let $A$ be a cyclic module of order $p^n$ ($p$ prime) over a PID $R$, generated by $a$. Then there exists a submodule $C$ of $A$ maximal with respect to $Ra \\cap C = 0$, and then $A = Ra \\oplus C$ (so $C$ is cyclic of order $p^m$ with $m \\leq n$).\n')
w_intro("cyclic-prime-power-order-properties","Lemma 6.8 provides a decomposition of cyclic prime-power modules as a direct sum of a given cyclic submodule and a complementary cyclic submodule. This technical result is key to the structure theorem.\n"); cnt+=1

w_yaml("cyclic-summand-existence","cyclic-summand-existence","Existence of Cyclic Summands","循环直和项的存在性","lemma","module-theory","intermediate",sec,"Lemma 6.9")
w_tex("cyclic-summand-existence","Let $A$ be a finitely generated $p$-primary torsion module over a PID $R$. Then $A$ is a direct sum of cyclic $R$-modules of orders $p^{n_1}, \\ldots, p^{n_k}$ with $n_1 \\geq n_2 \\geq \\cdots \\geq n_k$.\n")
w_intro("cyclic-summand-existence","Every finitely generated $p$-primary torsion module decomposes as a direct sum of cyclic modules of descending prime power orders. This is used to prove the elementary divisor form of the structure theorem.\n"); cnt+=1

w_yaml("properties-of-ra-and-ar","properties-of-ra-and-ar","Properties of rA and A[r]","rA与A[r]的性质","lemma","module-theory","intermediate",sec,"Lemma 6.10")
w_tex("properties-of-ra-and-ar",'Let $r \\in R$ and $p \\in R$ prime.\n\\begin{enumerate}\n\\item[(i)] $rA$ and $A[r]$ are submodules of $A$.\n\\item[(ii)] $R/(p)$ is a field and $A[p]$ is a vector space over $R/(p)$.\n\\item[(iii)] $(R/(p^n))[p] \\cong R/(p)$ and $p^m(R/(p^n)) \\cong R/(p^{n-m})$ ($0 \\leq m < n$).\n\\item[(iv)] If $A \\cong \\sum A_i$, then $rA \\cong \\sum rA_i$ and $A[r] \\cong \\sum A_i[r]$.\n\\item[(v)] If $f: A \\to B$ is an isomorphism, then $f: A_t \\cong B_t$ and $f: A(p) \\cong B(p)$.\n\\end{enumerate}\n')
w_intro("properties-of-ra-and-ar","Lemma 6.10 collects essential properties of the submodules $rA$ (multiples) and $A[r]$ ($r$-torsion). Over a PID, $R/(p)$ is a field, making $A[p]$ a vector space. These properties are key to uniqueness in the structure theorem.\n"); cnt+=1

w_yaml("structure-theorem-fg-modules-over-pid","structure-theorem-fg-modules-over-pid","Structure Theorem for Finitely Generated Modules over a PID","PID上有限生成模的结构定理","theorem","module-theory","advanced",sec,"Theorem 6.12")
w_tex("structure-theorem-fg-modules-over-pid",'Let $A$ be a finitely generated module over a PID $R$.\n\\begin{enumerate}\n\\item[(i)] $A$ is the direct sum of a free submodule $F$ of finite rank and cyclic torsion modules of orders $r_1,\\ldots,r_t$ with $r_1 \\mid r_2 \\mid \\cdots \\mid r_t$ (\\emph{invariant factors}). The rank of $F$ and the ideals $(r_i)$ are uniquely determined.\n\\item[(ii)] $A$ is the direct sum of a free submodule $E$ of finite rank and cyclic torsion modules of orders $p_1^{s_1},\\ldots,p_k^{s_k}$ where $p_i$ are primes (\\emph{elementary divisors}). The rank of $E$ and the ideals $(p_i^{s_i})$ are uniquely determined up to order.\n\\end{enumerate}\n')
w_intro("structure-theorem-fg-modules-over-pid","Theorem 6.12 is the fundamental structure theorem for finitely generated modules over principal ideal domains, generalizing the classification of finitely generated abelian groups. Every such module decomposes by invariant factors or by elementary divisors, each providing complete isomorphism invariants.\n"); cnt+=1

w_yaml("classification-fg-modules-over-pid","classification-fg-modules-over-pid","Classification of Finitely Generated Modules over a PID","PID上有限生成模的分类","corollary","module-theory","advanced",sec,"Corollary 6.13")
w_tex("classification-fg-modules-over-pid","Two finitely generated modules over a PID, $A$ and $B$, are isomorphic if and only if $A/A_t$ and $B/B_t$ have the same rank and $A$ and $B$ have the same invariant factors (resp. elementary divisors).\n")
w_intro("classification-fg-modules-over-pid","Corollary 6.13 gives a complete classification: two finitely generated modules over a PID are isomorphic exactly when their free parts have the same rank and their torsion parts share the same invariant factors or elementary divisors.\n"); cnt+=1

print(f"Section 6 done. Count: {cnt}")

# ============================================================
# SECTION 7: ALGEBRAS
# ============================================================
sec = "IV.7"

w_yaml("k-algebra","k-algebra","K-Algebra","K-代数","definition","algebra","basic",sec,"Definition 7.1")
w_tex("k-algebra",'Let $K$ be a commutative ring with identity. A \\emph{$K$-algebra} $A$ is a ring $A$ such that:\n\\begin{enumerate}\n\\item[(i)] $(A,+)$ is a unitary left $K$-module;\n\\item[(ii)] $k(ab) = (ka)b = a(kb)$ for all $k \\in K$ and $a,b \\in A$.\n\\end{enumerate}\nA $K$-algebra that is a division ring is called a \\emph{division algebra}. A finite-dimensional algebra over a field $K$ is a \\emph{finite dimensional algebra over $K$}.\n')
w_intro("k-algebra","A $K$-algebra is simultaneously a ring and a $K$-module, with scalar multiplication compatible with ring multiplication. Examples include polynomial rings, matrix rings, and field extensions.\n"); cnt+=1

w_yaml("algebra-structure-via-tensor-product","algebra-structure-via-tensor-product","Algebra Structure via Tensor Product","通过张量积刻画代数结构","theorem","algebra","advanced",sec,"Theorem 7.2")
w_tex("algebra-structure-via-tensor-product",'Let $K$ be a commutative ring with identity and $A$ a unitary left $K$-module. Then $A$ is a $K$-algebra if and only if there exists a $K$-module homomorphism $\\pi : A \\otimes_K A \\to A$ (the \\emph{product map}) such that the associativity diagram commutes. $A$ has an identity if and only if there is a $K$-module homomorphism $I : K \\to A$ (the \\emph{unit map}) such that the unit diagram commutes.\n')
w_intro("algebra-structure-via-tensor-product","Theorem 7.2 gives a categorical/tensor characterization: a $K$-module $A$ is a $K$-algebra precisely when equipped with an associative product map $\\pi: A \\otimes_K A \\to A$, and is unital when there is a unit map $I: K \\to A$. This perspective is fundamental to the theory of coalgebras and Hopf algebras.\n"); cnt+=1

w_yaml("algebra-homomorphism-and-algebra-ideal","algebra-homomorphism-and-algebra-ideal","Algebra Homomorphism and Algebra Ideal","代数同态与代数理想","definition","algebra","basic",sec,"Definition 7.3")
w_tex("algebra-homomorphism-and-algebra-ideal",'Let $K$ be a commutative ring with identity and $A$, $B$ $K$-algebras.\n\\begin{enumerate}\n\\item[(i)] A $K$-algebra homomorphism $f: A \\to B$ is both a ring homomorphism and a $K$-module homomorphism.\n\\item[(ii)] A $K$-algebra ideal $I$ of $A$ is both a ring ideal and a $K$-submodule. If $A$ has an identity, every ideal is also an algebra ideal.\n\\end{enumerate}\n')
w_intro("algebra-homomorphism-and-algebra-ideal","Definition 7.3 extends homomorphisms and ideals to the algebra setting. An algebra homomorphism must respect both ring and scalar structures; an algebra ideal is simultaneously a ring ideal and a $K$-submodule.\n"); cnt+=1

w_yaml("tensor-product-of-algebras","tensor-product-of-algebras","Tensor Product of Algebras","代数的张量积","theorem","algebra","intermediate",sec,"Theorem 7.4")
w_tex("tensor-product-of-algebras",'Let $A$ and $B$ be algebras [with identity] over a commutative ring $K$ with identity. Then $A \\otimes_K B$ is a $K$-algebra [with identity] with product map $\\pi$ given by\n\\[\n(A \\otimes_K B) \\otimes_K (A \\otimes_K B) \\xrightarrow{1_A \\otimes \\alpha \\otimes 1_B} (A \\otimes_K A) \\otimes_K (B \\otimes_K B) \\xrightarrow{\\pi_A \\otimes \\pi_B} A \\otimes_K B,\n\\]\nwhere $\\alpha(a \\otimes b) = b \\otimes a$. For generators, $(a \\otimes b)(a_1 \\otimes b_1) = aa_1 \\otimes bb_1$, and if $A,B$ have identities, $1_A \\otimes 1_B$ is the identity.\n')
w_intro("tensor-product-of-algebras","The tensor product of two $K$-algebras is again a $K$-algebra. Multiplication is defined componentwise: $(a \\otimes b)(a_1 \\otimes b_1) = aa_1 \\otimes bb_1$, using the swap map $\\alpha$ to align factors correctly.\n"); cnt+=1

print(f"Section 7 done. Count: {cnt}")
print(f"\n=== FINAL COUNT: {cnt} concepts generated ===")
