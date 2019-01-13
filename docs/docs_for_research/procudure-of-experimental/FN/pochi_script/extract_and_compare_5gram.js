extractor = bmsys.extractor("uc");
source = fs.open("birthmark/5gram");
birthmarks = extractor.extract(source);

pair2 = bmsys.pairMaker("RoundRobinWithSamePair")
comparator = bmsys.comparator("JaccardIndex")
comparisons = comparator.compare(birthmarks, pair2);
fs.print(comparisons);

fs.print("extraction: " + birthmarks.time() + " ns")
fs.print("comparison: " + comparisons.time() + " ns")


