export const meta = {
  name: 'v7-extract-gtm035',
  description: 'GTM035: 27 sections → concept extraction',
  phases: [{ title: 'Extract', detail: 'One agent per section' }]
}

var SECTIONS = ["/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s001_Section_1.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s002_Section_2.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s003_Section_3.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s004_Section_4.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s005_Section_5.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s006_Section_6.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s007_Section_7.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s008_Section_8.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s009_Section_9.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s00_preface.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s010_Section_10.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s011_Section_11.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s012_Section_12.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s013_Section_13.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s014_Section_14.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s015_Section_15.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s016_Section_16.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s017_Section_17.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s018_Section_18.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s019_Section_19.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s020_Section_20.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s021_Section_21.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s022_Section_22.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s023_Section_23.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s024_Section_24.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s025_Section_25.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM035)Several Complex Variables and Banach Algebras/s026_Section_26.md"]
var STAGING = '/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm035'
var BOOK_SLUG = 'gtm035'

phase('Extract')
log(BOOK_SLUG + ': ' + SECTIONS.length + ' sections')

var results = await pipeline(SECTIONS, function(prev, sp) {
  return async function() {
    var sn = sp.split('/').pop().replace('.md','')
    var dd = STAGING + '/' + sn
    
    var prompt = '=== V7 CONCEPT EXTRACTOR (Per-Section) ===\n\n' +
      'READ: ' + sp + '\n\n' +
      'Extract EVERY theorem, definition, lemma, proposition, corollary, axiom.\n' +
      'For EACH concept, write 3 files in: ' + dd + '/{SLUG}/\n\n' +
      '1. concept.yaml: id,title_en,title_zh:"",type,domain,subdomain,difficulty,tags,depends_on,source_books,content_hash:"",extraction_date:"2026-06-25",extraction_agent:"v7-test"\n' +
      '2. theorem.tex: PURE LaTeX STATEMENT only. NO proof.\n' +
      '3. introduce.en.md: YAML frontmatter(role:introduce,locale:en,content_hash:"",written_against:"") + 2-4 English sentences.\n\n' +
      'CRITICAL: slug = semantic-english-lowercase-hyphen (kummers-theorem NOT ' + key.lower() + '-thm-3-2). ' +
      'source_books = array of OBJECTS. theorem.tex = ZERO natural language.\n\n' +
      'Write .done: echo DONE > ' + dd + '/.done\n' +
      'Write .fail if stuck: echo FAIL > ' + dd + '/.fail'
    
    try { await agent(prompt, { label: sn.substring(0,40), phase: 'Extract' }) } catch(e) {}
    
    // Count on disk
    var cnt = 0
    try {
      var cr = await agent(
        'python3 -c "import os; d=\'' + dd + '\'; print(len([x for x in os.listdir(d) if os.path.isdir(os.path.join(d,x))]) if os.path.exists(d) else 0)"',
        { label: 'cnt-'+sn.substring(0,25), phase: 'Extract' }
      )
      cnt = cr ? parseInt(cr.trim()) || 0 : 0
    } catch(e) {}
    
    return { section: sn.substring(0,50), concepts: cnt }
  }
})

var valid = results.filter(function(r) { return r !== null })
var total = valid.reduce(function(s, r) { return s + (r.concepts || 0) }, 0)
log(BOOK_SLUG + ': ' + total + ' concepts from ' + valid.length + '/' + SECTIONS.length + ' sections')
return { book: BOOK_SLUG, sections: SECTIONS.length, sections_done: valid.length, concepts: total }
