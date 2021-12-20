
import testingtools
import crawler
import searchdata
import search

output = open('fruits-tf-failed.txt', 'w')
success_output = open('fruits-tf-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html')



#Test #0 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html and word apple
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html and word banana
expected = 0.17647058823529413
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html and word coconut
expected = 0.23529411764705882
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html and word pear
expected = 0.35294117647058826
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html and word peach
expected = 0.17647058823529413
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html and word apple
expected = 0.17857142857142858
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html and word banana
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html and word coconut
expected = 0.2857142857142857
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html and word pear
expected = 0.17857142857142858
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html and word peach
expected = 0.10714285714285714
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html and word banana
expected = 0.3333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html and word coconut
expected = 0.3333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html and word pear
expected = 0.3333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html and word apple
expected = 0.2112676056338028
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html and word banana
expected = 0.15492957746478872
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html and word coconut
expected = 0.16901408450704225
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html and word pear
expected = 0.23943661971830985
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html and word peach
expected = 0.22535211267605634
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html and word apple
expected = 0.20754716981132076
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html and word banana
expected = 0.2641509433962264
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html and word coconut
expected = 0.20754716981132076
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html and word pear
expected = 0.16981132075471697
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html and word peach
expected = 0.1509433962264151
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word apple
expected = 0.275
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word banana
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word coconut
expected = 0.325
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word pear
expected = 0.1
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word peach
expected = 0.175
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html and word apple
expected = 0.17857142857142858
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html and word banana
expected = 0.17857142857142858
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html and word coconut
expected = 0.21428571428571427
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html and word pear
expected = 0.17857142857142858
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html and word peach
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-500.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html and word apple
expected = 0.25862068965517243
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html and word banana
expected = 0.1724137931034483
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html and word coconut
expected = 0.1896551724137931
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html and word pear
expected = 0.25862068965517243
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html and word peach
expected = 0.1206896551724138
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html and word apple
expected = 0.18867924528301888
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html and word banana
expected = 0.1509433962264151
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html and word coconut
expected = 0.22641509433962265
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html and word pear
expected = 0.22641509433962265
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #51 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html and word peach
expected = 0.20754716981132076
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #52 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #53 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-344.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html and word apple
expected = 0.16666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #54 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html and word banana
expected = 0.11904761904761904
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #55 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html and word coconut
expected = 0.16666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #56 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html and word pear
expected = 0.3333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #57 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html and word peach
expected = 0.21428571428571427
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #58 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #59 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #60 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #61 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #62 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
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


#Test #64 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #64 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
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
