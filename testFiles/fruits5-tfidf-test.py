
import testingtools
import crawler
import searchdata
import search

output = open('fruits5-tfidf-failed.txt', 'w')
success_output = open('fruits5-tfidf-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html')



#Test #0 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word papaya
expected = 0.027222974345140327
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word lime
expected = 0.05814685895283705
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word pear
expected = 0.018666890552904814
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word apricot
expected = 0.009788610360804058
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word blueberry
expected = 0.019207749785150115
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word peach
expected = 0.0342686221773934
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word cherry
expected = 0.0174119425936928
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word papaya
expected = 0.010010305351485284
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word lime
expected = 0.023812767530720667
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word pear
expected = 0.010107707110898992
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word orange
expected = 0.010010305351485284
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word apricot
expected = 0.010400570386240288
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word kiwi
expected = 0.020385004666072477
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word blueberry
expected = 0.020385004666072477
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word peach
expected = 0.03205587864904253
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word cherry
expected = 0.004763198976294678
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word banana
expected = 0.03702440682625205
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word papaya
expected = 0.032075918518253574
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word lime
expected = 0.031452761085442586
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word pear
expected = 0.03238802197452078
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word orange
expected = 0.032075918518253574
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word apricot
expected = 0.017219073350844823
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word kiwi
expected = 0.017219073350844823
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word blueberry
expected = 0.03332644075666537
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word banana
expected = 0.016250982340756406
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word papaya
expected = 0.024449482216022805
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word lime
expected = 0.031452761085442586
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word pear
expected = 0.016734212037224756
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word orange
expected = 0.024449482216022805
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word apricot
expected = 0.017219073350844823
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word kiwi
expected = 0.025402677717233188
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word blueberry
expected = 0.008758006396682519
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word peach
expected = 0.023500556361826408
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word cherry
expected = 0.015609195249580477
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word papaya
expected = 0.007468349711196267
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word lime
expected = 0.03238071691934488
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word pear
expected = 0.03555865366445345
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word orange
expected = 0.012321293884309515
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word apricot
expected = 0.01528503528789975
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word kiwi
expected = 0.02017886996759202
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word blueberry
expected = 0.010293317452919096
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word peach
expected = 0.009522566465046026
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #51 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word cherry
expected = 0.011604779303045994
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #52 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word banana
expected = 0.01674634701935282
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #53 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #54 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word papaya
expected = 0.02289470289552112
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #55 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word lime
expected = 0.011492319122708275
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #56 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word pear
expected = 0.023117471758705398
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #57 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word orange
expected = 0.02289470289552112
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #58 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #59 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word kiwi
expected = 0.012176930710763402
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #60 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word blueberry
expected = 0.023787283262202967
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #61 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word peach
expected = 0.02200612066258256
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #62 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word cherry
expected = 0.03162024423649429
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #63 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word banana
expected = 0.03292034102216026
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #64 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #65 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #66 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word lime
expected = 0.03630954795325715
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #67 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word pear
expected = 0.02555517941738175
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #68 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word orange
expected = 0.01298762597983467
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #69 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word apricot
expected = 0.013493965809283838
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #70 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #71 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word blueberry
expected = 0.013493965809283838
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #72 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word peach
expected = 0.03559177484988699
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #73 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word cherry
expected = 0.023837141795301758
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #74 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #75 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #76 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word papaya
expected = 0.022104095819548787
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #77 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word lime
expected = 0.021674666757441664
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #78 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word pear
expected = 0.016928953011470436
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #79 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word orange
expected = 0.016765819098877022
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #80 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word apricot
expected = 0.014599341234656374
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #81 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word kiwi
expected = 0.020208062034061613
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #82 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word blueberry
expected = 0.008861673094745122
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #83 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word peach
expected = 0.018694907130698924
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #84 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word cherry
expected = 0.008033160830169998
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #85 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word banana
expected = 0.013778536844402093
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #86 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #87 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #88 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word lime
expected = 0.04294508020815085
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #89 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #90 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #91 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #92 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #93 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word blueberry
expected = 0.045503371467428756
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #94 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word peach
expected = 0.04209613481408626
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #95 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word cherry
expected = 0.04124908438899452
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #96 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #97 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #98 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word papaya
expected = 0.005166060749805927
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #99 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word lime
expected = 0.014881526053805143
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #100 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word pear
expected = 0.0250273231254915
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #101 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #101 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word orange
expected = 0.020029310274404445
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word apricot
expected = 0.010621925231790369
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word kiwi
expected = 0.013208244459248656
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word blueberry
expected = 0.02818739360284569
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word peach
expected = 0.012219227311803362
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word cherry
expected = 0.01429382180811301
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word banana
expected = 0.012465650333565267
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
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
