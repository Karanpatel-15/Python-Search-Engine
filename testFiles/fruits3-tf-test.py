
import testingtools
import crawler
import searchdata
import search

output = open('fruits3-tf-failed.txt', 'w')
success_output = open('fruits3-tf-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html')



#Test #0 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word coconut
expected = 0.11764705882352941
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word peach
expected = 0.11764705882352941
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word cherry
expected = 0.11764705882352941
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word kiwi
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word apple
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word apricot
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word blueberry
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word lime
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word fig
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word coconut
expected = 0.06060606060606061
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word peach
expected = 0.06060606060606061
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word cherry
expected = 0.07575757575757576
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word kiwi
expected = 0.07575757575757576
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word apple
expected = 0.12121212121212122
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word apricot
expected = 0.07575757575757576
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word banana
expected = 0.07575757575757576
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word blueberry
expected = 0.030303030303030304
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word lime
expected = 0.07575757575757576
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word fig
expected = 0.045454545454545456
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word coconut
expected = 0.041666666666666664
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word peach
expected = 0.09722222222222222
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word cherry
expected = 0.06944444444444445
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word kiwi
expected = 0.09722222222222222
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word apple
expected = 0.06944444444444445
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word apricot
expected = 0.1111111111111111
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word banana
expected = 0.027777777777777776
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word blueberry
expected = 0.06944444444444445
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word lime
expected = 0.06944444444444445
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word fig
expected = 0.041666666666666664
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word coconut
expected = 0.06060606060606061
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word peach
expected = 0.07575757575757576
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word cherry
expected = 0.06060606060606061
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word kiwi
expected = 0.06060606060606061
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word apple
expected = 0.10606060606060606
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word apricot
expected = 0.015151515151515152
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word banana
expected = 0.09090909090909091
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word blueberry
expected = 0.030303030303030304
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word lime
expected = 0.16666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word fig
expected = 0.10606060606060606
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word coconut
expected = 0.1388888888888889
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word peach
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word cherry
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word kiwi
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word apple
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word apricot
expected = 0.027777777777777776
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word banana
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word blueberry
expected = 0.1111111111111111
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #51 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word lime
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #52 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word fig
expected = 0.027777777777777776
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #53 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #54 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word coconut
expected = 0.1411764705882353
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #55 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word peach
expected = 0.08235294117647059
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #56 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word cherry
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #57 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word kiwi
expected = 0.047058823529411764
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #58 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word apple
expected = 0.023529411764705882
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #59 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word apricot
expected = 0.047058823529411764
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #60 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word banana
expected = 0.10588235294117647
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #61 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word blueberry
expected = 0.08235294117647059
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #62 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word lime
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #63 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word fig
expected = 0.08235294117647059
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #64 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #65 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word coconut
expected = 0.04878048780487805
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #66 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word peach
expected = 0.04878048780487805
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #67 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word cherry
expected = 0.12195121951219512
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #68 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word kiwi
expected = 0.07317073170731707
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #69 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word apple
expected = 0.07317073170731707
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #70 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word apricot
expected = 0.0975609756097561
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #71 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word banana
expected = 0.0975609756097561
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #72 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word blueberry
expected = 0.024390243902439025
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #73 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word lime
expected = 0.024390243902439025
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #74 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word fig
expected = 0.12195121951219512
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #75 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #76 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word coconut
expected = 0.10526315789473684
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #77 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #78 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word cherry
expected = 0.10526315789473684
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #79 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word kiwi
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #80 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word apple
expected = 0.15789473684210525
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #81 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word apricot
expected = 0.10526315789473684
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #82 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #83 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word blueberry
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #84 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #85 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word fig
expected = 0.15789473684210525
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #86 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #87 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word coconut
expected = 0.08
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #88 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word peach
expected = 0.04
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #89 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word cherry
expected = 0.14
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #90 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word kiwi
expected = 0.1
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #91 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #92 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word apricot
expected = 0.04
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #93 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word banana
expected = 0.12
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #94 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word blueberry
expected = 0.04
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #95 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word lime
expected = 0.1
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #96 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word fig
expected = 0.06
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #97 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #98 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #99 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word peach
expected = 0.07407407407407407
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #100 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word cherry
expected = 0.1111111111111111
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #101 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #101 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word kiwi
expected = 0.2222222222222222
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word apple
expected = 0.037037037037037035
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word apricot
expected = 0.18518518518518517
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word banana
expected = 0.1111111111111111
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word blueberry
expected = 0.037037037037037035
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word lime
expected = 0.037037037037037035
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word fig
expected = 0.07407407407407407
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
