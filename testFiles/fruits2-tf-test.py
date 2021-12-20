
import testingtools
import crawler
import searchdata
import search

output = open('fruits2-tf-failed.txt', 'w')
success_output = open('fruits2-tf-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html')



#Test #0 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word banana
expected = 0.23255813953488372
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word peach
expected = 0.23255813953488372
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word apple
expected = 0.20930232558139536
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word pear
expected = 0.11627906976744186
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word coconut
expected = 0.20930232558139536
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html and word banana
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html and word peach
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html and word apple
expected = 0.20833333333333334
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html and word pear
expected = 0.20833333333333334
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html and word coconut
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html and word banana
expected = 0.203125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html and word peach
expected = 0.1875
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html and word apple
expected = 0.171875
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html and word pear
expected = 0.203125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html and word coconut
expected = 0.234375
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-574.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html and word banana
expected = 0.11764705882352941
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html and word peach
expected = 0.11764705882352941
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html and word apple
expected = 0.23529411764705882
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html and word pear
expected = 0.17647058823529413
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html and word coconut
expected = 0.35294117647058826
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html and word banana
expected = 0.23809523809523808
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html and word peach
expected = 0.09523809523809523
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html and word apple
expected = 0.19047619047619047
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html and word pear
expected = 0.19047619047619047
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html and word coconut
expected = 0.2857142857142857
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html and word banana
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html and word apple
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html and word pear
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html and word coconut
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html and word banana
expected = 0.1717171717171717
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html and word peach
expected = 0.21212121212121213
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html and word apple
expected = 0.2727272727272727
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html and word pear
expected = 0.20202020202020202
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html and word coconut
expected = 0.1414141414141414
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-741.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html and word banana
expected = 0.20253164556962025
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html and word peach
expected = 0.1518987341772152
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html and word apple
expected = 0.25316455696202533
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html and word pear
expected = 0.17721518987341772
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html and word coconut
expected = 0.21518987341772153
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html and word banana
expected = 0.2459016393442623
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html and word peach
expected = 0.14754098360655737
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html and word apple
expected = 0.26229508196721313
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html and word pear
expected = 0.09836065573770492
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #51 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html and word coconut
expected = 0.2459016393442623
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #52 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #53 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html and word banana
expected = 0.17142857142857143
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #54 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html and word peach
expected = 0.22857142857142856
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #55 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html and word apple
expected = 0.11428571428571428
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #56 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html and word pear
expected = 0.2571428571428571
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #57 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html and word coconut
expected = 0.22857142857142856
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #58 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #59 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #60 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #61 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #62 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #63 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #64 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #65 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
