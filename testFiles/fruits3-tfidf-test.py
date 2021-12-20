
import testingtools
import crawler
import searchdata
import search

output = open('fruits3-tfidf-failed.txt', 'w')
success_output = open('fruits3-tfidf-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html')



#Test #0 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word coconut
expected = 0.026600235133183308
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word pear
expected = 0.008840395558896317
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word peach
expected = 0.0040866466743190825
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word blueberry
expected = 0.012902007293798208
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word orange
expected = 0.02856826003299051
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word fig
expected = 0.01253567369899127
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word papaya
expected = 0.021746229659516454
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word apricot
expected = 0.016572954723677334
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word banana
expected = 0.03755396894065185
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word cherry
expected = 0.023500556361826408
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word coconut
expected = 0.008859946693951895
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word pear
expected = 0.03255172000587697
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word peach
expected = 0.003946925333007955
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word blueberry
expected = 0.016488266393375375
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word orange
expected = 0.01223199701102837
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word fig
expected = 0.023646542527775323
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word papaya
expected = 0.02102651244016326
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word apricot
expected = 0.02737084296563426
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word banana
expected = 0.011526740957460318
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word cherry
expected = 0.0190926497087668
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word coconut
expected = 0.012750987266474166
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word pear
expected = 0.029672540985352273
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word peach
expected = 0.005701265208540306
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word blueberry
expected = 0.01788000836440647
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word orange
expected = 0.011834047995765757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word fig
expected = 0.02289470289552112
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word papaya
expected = 0.024235084020792663
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word apricot
expected = 0.017372331722302906
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word banana
expected = 0.011151736351992143
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word cherry
expected = 0.02200612066258256
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word pear
expected = 0.04891283591008144
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word peach
expected = 0.015929730254595636
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word orange
expected = 0.016734212037224756
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word fig
expected = 0.016572954723677334
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word papaya
expected = 0.03395381822080993
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word cherry
expected = 0.015929730254595636
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word coconut
expected = 0.014130111297777848
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word pear
expected = 0.026542992389967886
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word peach
expected = 0.024326637777813055
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word blueberry
expected = 0.01336716710601951
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word fig
expected = 0.01298762597983467
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word papaya
expected = 0.03919680652314111
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word apricot
expected = 0.025308919864144203
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #51 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word banana
expected = 0.024081753208408947
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #52 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word cherry
expected = 0.024326637777813055
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #53 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #54 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word coconut
expected = 0.015377576184001807
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #55 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word pear
expected = 0.007520720345308201
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #56 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word peach
expected = 0.01686073760261783
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #57 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word blueberry
expected = 0.007380618749331089
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #58 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word orange
expected = 0.024450166707072844
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #59 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word fig
expected = 0.024214555481985065
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #60 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word papaya
expected = 0.022124898268346908
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #61 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word apricot
expected = 0.0036122871150518383
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #62 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word banana
expected = 0.019887777635724264
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #63 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word cherry
expected = 0.013585654187304421
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #64 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #65 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word coconut
expected = 0.03255364513156448
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #66 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word pear
expected = 0.01253618930481603
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #67 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word peach
expected = 0.018118272796658414
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #68 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word blueberry
expected = 0.0240220235424081
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #69 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word orange
expected = 0.01206964769412811
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #70 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word fig
expected = 0.018849868135314314
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #71 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word papaya
expected = 0.01510994513775326
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #72 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word apricot
expected = 0.016572954723677334
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #73 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word banana
expected = 0.01358212929808343
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #74 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word cherry
expected = 0.02243409021879491
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #75 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #76 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word coconut
expected = 0.012750987266474166
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #77 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word pear
expected = 0.012291482707434161
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #78 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word peach
expected = 0.011265137072073942
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #79 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word blueberry
expected = 0.01788000836440647
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #80 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word orange
expected = 0.023117471758705398
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #81 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word fig
expected = 0.03357257486398112
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #82 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word papaya
expected = 0.006278736878359964
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #83 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word apricot
expected = 0.01172001055056407
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #84 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word banana
expected = 0.01652999051072932
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #85 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word cherry
expected = 0.005701265208540306
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #86 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #87 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word coconut
expected = 0.02753527511972982
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #88 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #89 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #90 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word blueberry
expected = 0.026048529702206495
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #91 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word orange
expected = 0.02555517941738175
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #92 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #93 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word papaya
expected = 0.05102572647560413
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #94 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word apricot
expected = 0.025308919864144203
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #95 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word banana
expected = 0.024081753208408947
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #96 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #97 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #98 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word coconut
expected = 0.029068085363904657
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #99 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word pear
expected = 0.024683755743156826
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #100 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word peach
expected = 0.016382011514733695
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #101 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #101 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word blueberry
expected = 0.017541565645895513
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word orange
expected = 0.020509383507006432
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word fig
expected = 0.023536125349822367
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word papaya
expected = 0.02150090795805931
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word apricot
expected = 0.006963170626144982
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word banana
expected = 0.019326881021089863
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word cherry
expected = 0.013197278133627663
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
