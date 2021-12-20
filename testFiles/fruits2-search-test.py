
import testingtools
import crawler
import searchdata
import search

output = open('fruits2-search-failed.txt', 'w')
success_output = open('fruits2-search-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html')



#Test #0 checking search results for 'apple peach peach coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.011719967813318709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01074580613493269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009726094001108607}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.009194294058674089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.008595403384665412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.0084427315720509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.008296097855164436}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007351020181532651}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.006883513183464108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006539396720121394}]
result = search.search('apple peach peach coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #0 checking search results for 'apple peach peach coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #0 checking search results for 'apple peach peach coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking search results for 'apple peach peach coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-379.html', 'title': 'N-379', 'score': 0.9999611211778617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-643.html', 'title': 'N-643', 'score': 0.9999271006405076}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-38.html', 'title': 'N-38', 'score': 0.999835758881885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-899.html', 'title': 'N-899', 'score': 0.9995962027486648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-874.html', 'title': 'N-874', 'score': 0.9987637862012061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-390.html', 'title': 'N-390', 'score': 0.9987637862012061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-198.html', 'title': 'N-198', 'score': 0.9953584212073645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html', 'title': 'N-290', 'score': 0.9952605967877095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9950410000637774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-82.html', 'title': 'N-82', 'score': 0.9947218942634555}]
result = search.search('apple peach peach coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #1 checking search results for 'apple peach peach coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #1 checking search results for 'apple peach peach coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking search results for 'banana apple banana banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.013858194927045592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011198027452701882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.010522362145400234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.00996917091296714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009879203175548329}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.008513973060924725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.0076639141157468825}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.0075336621390086145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007277657245262519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007209999298089897}]
result = search.search('banana apple banana banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #2 checking search results for 'banana apple banana banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #2 checking search results for 'banana apple banana banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking search results for 'banana apple banana banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-26.html', 'title': 'N-26', 'score': 0.9999999211756202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-892.html', 'title': 'N-892', 'score': 0.9999944473909909}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-441.html', 'title': 'N-441', 'score': 0.9999649726222454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-669.html', 'title': 'N-669', 'score': 0.9999476130699614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-744.html', 'title': 'N-744', 'score': 0.9999272023312045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'title': 'N-830', 'score': 0.9999272023312045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-435.html', 'title': 'N-435', 'score': 0.9999186501008098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-258.html', 'title': 'N-258', 'score': 0.9998795599945708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html', 'title': 'N-718', 'score': 0.9998122946000483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-53.html', 'title': 'N-53', 'score': 0.9998122946000483}]
result = search.search('banana apple banana banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #3 checking search results for 'banana apple banana banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #3 checking search results for 'banana apple banana banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking search results for 'banana apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01760043385328955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012113974494578992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012090788373318905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011735556738228342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011001729294882301}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010049859168975073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00902725649960236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007793463871817541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007253331382606732}]
result = search.search('banana apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #4 checking search results for 'banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #4 checking search results for 'banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking search results for 'banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-111.html', 'title': 'N-111', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-513.html', 'title': 'N-513', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-528.html', 'title': 'N-528', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-398.html', 'title': 'N-398', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-757.html', 'title': 'N-757', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-121.html', 'title': 'N-121', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-306.html', 'title': 'N-306', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-982.html', 'title': 'N-982', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-179.html', 'title': 'N-179', 'score': 1.0}]
result = search.search('banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #5 checking search results for 'banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #5 checking search results for 'banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #6 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #6 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #7 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #7 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking search results for 'coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015842641448101158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01211020826453844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011483869599545097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010972527664583006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010854644615354948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010080813833178298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00887607634153808}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074182386121266234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006850823441047688}]
result = search.search('coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #8 checking search results for 'coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #8 checking search results for 'coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking search results for 'coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-863.html', 'title': 'N-863', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-671.html', 'title': 'N-671', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-444.html', 'title': 'N-444', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-797.html', 'title': 'N-797', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html', 'title': 'N-197', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-64.html', 'title': 'N-64', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-404.html', 'title': 'N-404', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-81.html', 'title': 'N-81', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-456.html', 'title': 'N-456', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-921.html', 'title': 'N-921', 'score': 1.0000000000000002}]
result = search.search('coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #9 checking search results for 'coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #9 checking search results for 'coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #10 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #10 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #11 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #11 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #12 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #12 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #13 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #13 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking search results for 'apple pear tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016365023383716065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011864271940507152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011602424733313296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011221965203735395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010579178635639886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.01013873115488159}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009135808735659187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0076252899259429035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007563001879266675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007222408903239571}]
result = search.search('apple pear tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #14 checking search results for 'apple pear tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #14 checking search results for 'apple pear tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking search results for 'apple pear tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-817.html', 'title': 'N-817', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-719.html', 'title': 'N-719', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html', 'title': 'N-381', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html', 'title': 'N-161', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-447.html', 'title': 'N-447', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-407.html', 'title': 'N-407', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-316.html', 'title': 'N-316', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-660.html', 'title': 'N-660', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'title': 'N-830', 'score': 1.0}]
result = search.search('apple pear tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #15 checking search results for 'apple pear tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #15 checking search results for 'apple pear tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking search results for 'tomato banana apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01760043385328955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012113974494578992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012090788373318905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011735556738228342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011001729294882301}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010049859168975073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00902725649960236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007793463871817541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007253331382606732}]
result = search.search('tomato banana apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #16 checking search results for 'tomato banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #16 checking search results for 'tomato banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking search results for 'tomato banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-111.html', 'title': 'N-111', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-513.html', 'title': 'N-513', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-528.html', 'title': 'N-528', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-398.html', 'title': 'N-398', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-757.html', 'title': 'N-757', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-121.html', 'title': 'N-121', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-306.html', 'title': 'N-306', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-982.html', 'title': 'N-982', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-179.html', 'title': 'N-179', 'score': 1.0}]
result = search.search('tomato banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #17 checking search results for 'tomato banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #17 checking search results for 'tomato banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking search results for 'coconut peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017741932005937947}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012095397269211846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011971965058115493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011735744493477543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010828756375968454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010103849224383558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008004516648110175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007623587821968054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007265577647854814}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.006175605447144896}]
result = search.search('coconut peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #18 checking search results for 'coconut peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #18 checking search results for 'coconut peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking search results for 'coconut peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-319.html', 'title': 'N-319', 'score': 0.9999999361842559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-854.html', 'title': 'N-854', 'score': 0.9999979497757108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-807.html', 'title': 'N-807', 'score': 0.9999971897388632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-62.html', 'title': 'N-62', 'score': 0.9999958708239478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-100.html', 'title': 'N-100', 'score': 0.9999954705738628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-74.html', 'title': 'N-74', 'score': 0.9999787436732015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-467.html', 'title': 'N-467', 'score': 0.9999769823430311}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-977.html', 'title': 'N-977', 'score': 0.9999667529035878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-238.html', 'title': 'N-238', 'score': 0.9999576510276118}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-344.html', 'title': 'N-344', 'score': 0.9999401702493369}]
result = search.search('coconut peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #19 checking search results for 'coconut peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #19 checking search results for 'coconut peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #20 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #20 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking search results for 'coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #21 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #21 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking search results for 'peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017550118729857473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011656932582640325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01142048412238662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011337787901014541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010950789412243948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010161262053867885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009025287207994238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007851229169293263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007845961180561788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007216203714936172}]
result = search.search('peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #22 checking search results for 'peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #22 checking search results for 'peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking search results for 'peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'title': 'N-183', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-364.html', 'title': 'N-364', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-774.html', 'title': 'N-774', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-236.html', 'title': 'N-236', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-205.html', 'title': 'N-205', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html', 'title': 'N-828', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html', 'title': 'N-229', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-580.html', 'title': 'N-580', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-625.html', 'title': 'N-625', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0000000000000002}]
result = search.search('peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #23 checking search results for 'peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #23 checking search results for 'peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking search results for 'tomato banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #24 checking search results for 'tomato banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #24 checking search results for 'tomato banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking search results for 'tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #25 checking search results for 'tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #25 checking search results for 'tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking search results for 'banana pear banana banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.012340321061365438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01154048840928966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010645679348863622}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.008598286509669347}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.008488399044667303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.008480394061135526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0075748503127700114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.007512285320440071}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0073210673790542686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.0066749350617987865}]
result = search.search('banana pear banana banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #26 checking search results for 'banana pear banana banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #26 checking search results for 'banana pear banana banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking search results for 'banana pear banana banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'title': 'N-830', 'score': 0.999891690809101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-797.html', 'title': 'N-797', 'score': 0.999766281283249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-163.html', 'title': 'N-163', 'score': 0.9997196905365122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-306.html', 'title': 'N-306', 'score': 0.9995586419275327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-286.html', 'title': 'N-286', 'score': 0.997969351643679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-588.html', 'title': 'N-588', 'score': 0.9972944909849887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-553.html', 'title': 'N-553', 'score': 0.9947903475339985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-926.html', 'title': 'N-926', 'score': 0.993356103216765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-64.html', 'title': 'N-64', 'score': 0.9931283632662363}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-745.html', 'title': 'N-745', 'score': 0.9919873113241857}]
result = search.search('banana pear banana banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #27 checking search results for 'banana pear banana banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #27 checking search results for 'banana pear banana banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking search results for 'banana coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01718997023167374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01208706964257492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011693076294116906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011206269293521722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010832104155960764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009982414809500502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00910552204361093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007850441844377491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007288029773052712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006736919019056488}]
result = search.search('banana coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #28 checking search results for 'banana coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #28 checking search results for 'banana coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking search results for 'banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'title': 'N-63', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'title': 'N-183', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-268.html', 'title': 'N-268', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-857.html', 'title': 'N-857', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-603.html', 'title': 'N-603', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-928.html', 'title': 'N-928', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-786.html', 'title': 'N-786', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-458.html', 'title': 'N-458', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-884.html', 'title': 'N-884', 'score': 1.0000000000000002}]
result = search.search('banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #29 checking search results for 'banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #29 checking search results for 'banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking search results for 'coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01718997023167374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01208706964257492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011693076294116906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011206269293521722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010832104155960764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009982414809500502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00910552204361093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007850441844377491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007288029773052712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006736919019056488}]
result = search.search('coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #30 checking search results for 'coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #30 checking search results for 'coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking search results for 'coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'title': 'N-63', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'title': 'N-183', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-268.html', 'title': 'N-268', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-857.html', 'title': 'N-857', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-603.html', 'title': 'N-603', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-928.html', 'title': 'N-928', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-786.html', 'title': 'N-786', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-458.html', 'title': 'N-458', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-884.html', 'title': 'N-884', 'score': 1.0000000000000002}]
result = search.search('coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #31 checking search results for 'coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #31 checking search results for 'coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #32 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #32 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #33 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #33 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking search results for 'tomato banana tomato apple coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017599004167524482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.0120719667466758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011747301732788646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011195732702533604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010854814090344183}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010045493195935921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008940861975716384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007856488379499342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007272754374664038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007119614658467722}]
result = search.search('tomato banana tomato apple coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #34 checking search results for 'tomato banana tomato apple coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #34 checking search results for 'tomato banana tomato apple coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking search results for 'tomato banana tomato apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-179.html', 'title': 'N-179', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-603.html', 'title': 'N-603', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-928.html', 'title': 'N-928', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'title': 'N-69', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-306.html', 'title': 'N-306', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-837.html', 'title': 'N-837', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-980.html', 'title': 'N-980', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html', 'title': 'N-906', 'score': 1.0}]
result = search.search('tomato banana tomato apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #35 checking search results for 'tomato banana tomato apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #35 checking search results for 'tomato banana tomato apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking search results for 'banana pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01670941806909784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012071491793215802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011848532967550793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011012325687601349}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010430880092533866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.0100485896996318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008988847823103913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007739110753157671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007492835360319172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006700433037127445}]
result = search.search('banana pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #36 checking search results for 'banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #36 checking search results for 'banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking search results for 'banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'title': 'N-63', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-522.html', 'title': 'N-522', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-216.html', 'title': 'N-216', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-889.html', 'title': 'N-889', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html', 'title': 'N-653', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-512.html', 'title': 'N-512', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-755.html', 'title': 'N-755', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-15.html', 'title': 'N-15', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-884.html', 'title': 'N-884', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'title': 'N-69', 'score': 1.0000000000000002}]
result = search.search('banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #37 checking search results for 'banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #37 checking search results for 'banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking search results for 'tomato pear apple tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01813147648332099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012096150028644849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011833057304008606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011345959507545668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01052576259873801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009135516621490822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007520651154782941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007499941928436314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007140873799605519}]
result = search.search('tomato pear apple tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #38 checking search results for 'tomato pear apple tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #38 checking search results for 'tomato pear apple tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking search results for 'tomato pear apple tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-92.html', 'title': 'N-92', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-155.html', 'title': 'N-155', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-637.html', 'title': 'N-637', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-379.html', 'title': 'N-379', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-438.html', 'title': 'N-438', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-143.html', 'title': 'N-143', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html', 'title': 'N-815', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-690.html', 'title': 'N-690', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html', 'title': 'N-900', 'score': 1.0000000000000002}]
result = search.search('tomato pear apple tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #39 checking search results for 'tomato pear apple tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #39 checking search results for 'tomato pear apple tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #40 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #40 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #41 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #41 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking search results for 'apple apple pear banana pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.018113618302986318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011723523490915695}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011559024514409776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011425152845518044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010581508563047381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010125675376031979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00909262409471345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007451411425524388}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007118676187805786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.0063280530644499785}]
result = search.search('apple apple pear banana pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #42 checking search results for 'apple apple pear banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #42 checking search results for 'apple apple pear banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking search results for 'apple apple pear banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-740.html', 'title': 'N-740', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-118.html', 'title': 'N-118', 'score': 0.9999867252311405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-438.html', 'title': 'N-438', 'score': 0.999979263275797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-151.html', 'title': 'N-151', 'score': 0.9999501363317277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-664.html', 'title': 'N-664', 'score': 0.9999469385038418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-702.html', 'title': 'N-702', 'score': 0.9999416810153937}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-279.html', 'title': 'N-279', 'score': 0.999931485033219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-91.html', 'title': 'N-91', 'score': 0.9997229336937246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-384.html', 'title': 'N-384', 'score': 0.9996219146057391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-499.html', 'title': 'N-499', 'score': 0.9990985156545678}]
result = search.search('apple apple pear banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #43 checking search results for 'apple apple pear banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #43 checking search results for 'apple apple pear banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking search results for 'coconut apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01832996118432234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012058969554624502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011874122316225049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011507913713472501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010891862743686864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010171409367176289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008880626423413049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.00785054050421375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007426245523254142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007052512952506606}]
result = search.search('coconut apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #44 checking search results for 'coconut apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #44 checking search results for 'coconut apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking search results for 'coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-486.html', 'title': 'N-486', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-550.html', 'title': 'N-550', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-603.html', 'title': 'N-603', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-928.html', 'title': 'N-928', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html', 'title': 'N-496', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html', 'title': 'N-967', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'title': 'N-69', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html', 'title': 'N-311', 'score': 1.0}]
result = search.search('coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #45 checking search results for 'coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #45 checking search results for 'coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking search results for 'banana banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('banana banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #46 checking search results for 'banana banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #46 checking search results for 'banana banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking search results for 'banana banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('banana banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #47 checking search results for 'banana banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #47 checking search results for 'banana banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking search results for 'tomato pear apple peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016963693468382352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01177493448432792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011736572188087822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.01134563213062057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010696844773432022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010129925079243323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008956219135828374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.00770182116528928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007255616309092154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006983761814318528}]
result = search.search('tomato pear apple peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #48 checking search results for 'tomato pear apple peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #48 checking search results for 'tomato pear apple peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking search results for 'tomato pear apple peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'title': 'N-830', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-664.html', 'title': 'N-664', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-403.html', 'title': 'N-403', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-648.html', 'title': 'N-648', 'score': 0.9993817981154297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-769.html', 'title': 'N-769', 'score': 0.9992665217295326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-416.html', 'title': 'N-416', 'score': 0.9992259424303972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0.9991255461102312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-237.html', 'title': 'N-237', 'score': 0.9990829388621023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-226.html', 'title': 'N-226', 'score': 0.9988455751959062}]
result = search.search('tomato pear apple peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #49 checking search results for 'tomato pear apple peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #49 checking search results for 'tomato pear apple peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #50 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #50 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #51 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #51 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking search results for 'banana tomato banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('banana tomato banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #52 checking search results for 'banana tomato banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #52 checking search results for 'banana tomato banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking search results for 'banana tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('banana tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #53 checking search results for 'banana tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #53 checking search results for 'banana tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #54 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #54 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #55 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #55 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking search results for 'tomato tomato pear tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato tomato pear tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #56 checking search results for 'tomato tomato pear tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #56 checking search results for 'tomato tomato pear tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking search results for 'tomato tomato pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('tomato tomato pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #57 checking search results for 'tomato tomato pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #57 checking search results for 'tomato tomato pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking search results for 'coconut apple coconut coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01737139098050491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01164922999717421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011607382255277523}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011053370725518413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01039499488716624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009498034348048226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.007202025322854328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.006884710811716236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006810996744740319}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.005639575307424332}]
result = search.search('coconut apple coconut coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #58 checking search results for 'coconut apple coconut coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #58 checking search results for 'coconut apple coconut coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking search results for 'coconut apple coconut coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-892.html', 'title': 'N-892', 'score': 0.9999924039501379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-220.html', 'title': 'N-220', 'score': 0.9989501428920651}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-573.html', 'title': 'N-573', 'score': 0.9983740562498026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-185.html', 'title': 'N-185', 'score': 0.9975441369382227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html', 'title': 'N-161', 'score': 0.9967363285220375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-746.html', 'title': 'N-746', 'score': 0.9967170939565597}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-537.html', 'title': 'N-537', 'score': 0.996159417724495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-454.html', 'title': 'N-454', 'score': 0.9933534112524028}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html', 'title': 'N-101', 'score': 0.9929257026165196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-854.html', 'title': 'N-854', 'score': 0.9919126481382149}]
result = search.search('coconut apple coconut coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #59 checking search results for 'coconut apple coconut coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #59 checking search results for 'coconut apple coconut coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking search results for 'pear peach tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017539141111190957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012079305636777653}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012015225511465041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.01184254425715884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010998975034235138}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010018445657901469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008844722156788623}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007850457847604228}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.006886943799158291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006373991240038296}]
result = search.search('pear peach tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #60 checking search results for 'pear peach tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #60 checking search results for 'pear peach tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking search results for 'pear peach tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-295.html', 'title': 'N-295', 'score': 0.9999999981872514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-344.html', 'title': 'N-344', 'score': 0.999999935760305}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-464.html', 'title': 'N-464', 'score': 0.9999970957164837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html', 'title': 'N-57', 'score': 0.9999968869300868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-193.html', 'title': 'N-193', 'score': 0.9999951727396859}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-821.html', 'title': 'N-821', 'score': 0.9999865573071349}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html', 'title': 'N-331', 'score': 0.9999793417281982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-523.html', 'title': 'N-523', 'score': 0.9999793417281982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-707.html', 'title': 'N-707', 'score': 0.9999716948838101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-319.html', 'title': 'N-319', 'score': 0.9999570248623436}]
result = search.search('pear peach tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #61 checking search results for 'pear peach tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #61 checking search results for 'pear peach tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking search results for 'coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015842641448101158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01211020826453844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011483869599545097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010972527664583006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010854644615354948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010080813833178298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00887607634153808}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074182386121266234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006850823441047688}]
result = search.search('coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #62 checking search results for 'coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #62 checking search results for 'coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking search results for 'coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-863.html', 'title': 'N-863', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-671.html', 'title': 'N-671', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-444.html', 'title': 'N-444', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-797.html', 'title': 'N-797', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html', 'title': 'N-197', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-64.html', 'title': 'N-64', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-404.html', 'title': 'N-404', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-81.html', 'title': 'N-81', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-456.html', 'title': 'N-456', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-921.html', 'title': 'N-921', 'score': 1.0000000000000002}]
result = search.search('coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #63 checking search results for 'coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #63 checking search results for 'coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking search results for 'peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017550118729857473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011656932582640325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01142048412238662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011337787901014541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010950789412243948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010161262053867885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009025287207994238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007851229169293263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007845961180561788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007216203714936172}]
result = search.search('peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #64 checking search results for 'peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #64 checking search results for 'peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking search results for 'peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'title': 'N-183', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-364.html', 'title': 'N-364', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-774.html', 'title': 'N-774', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-236.html', 'title': 'N-236', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-205.html', 'title': 'N-205', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html', 'title': 'N-828', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html', 'title': 'N-229', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-580.html', 'title': 'N-580', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-625.html', 'title': 'N-625', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0000000000000002}]
result = search.search('peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #65 checking search results for 'peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #65 checking search results for 'peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking search results for 'coconut pear pear peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017429428926467705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011749849797538401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.0111640295942219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010933470258388655}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010873980148630075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009729900022727446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00881685825593561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007545458371483438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.006930553400801387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.00650007618255572}]
result = search.search('coconut pear pear peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #66 checking search results for 'coconut pear pear peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #66 checking search results for 'coconut pear pear peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking search results for 'coconut pear pear peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-193.html', 'title': 'N-193', 'score': 0.9990418120273657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-191.html', 'title': 'N-191', 'score': 0.9977832216260127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-345.html', 'title': 'N-345', 'score': 0.9973957257616919}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-824.html', 'title': 'N-824', 'score': 0.9972290106054099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-437.html', 'title': 'N-437', 'score': 0.9968859308094584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-707.html', 'title': 'N-707', 'score': 0.9962561999973536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-293.html', 'title': 'N-293', 'score': 0.9952565857061882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-677.html', 'title': 'N-677', 'score': 0.9948293008894741}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-239.html', 'title': 'N-239', 'score': 0.9947283280959459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-156.html', 'title': 'N-156', 'score': 0.9937837386841532}]
result = search.search('coconut pear pear peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #67 checking search results for 'coconut pear pear peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #67 checking search results for 'coconut pear pear peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking search results for 'banana pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01670941806909784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012071491793215802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011848532967550793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011012325687601349}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010430880092533866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.0100485896996318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008988847823103913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007739110753157671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007492835360319172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006700433037127445}]
result = search.search('banana pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #68 checking search results for 'banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #68 checking search results for 'banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking search results for 'banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'title': 'N-63', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-522.html', 'title': 'N-522', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-216.html', 'title': 'N-216', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-889.html', 'title': 'N-889', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html', 'title': 'N-653', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-512.html', 'title': 'N-512', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-755.html', 'title': 'N-755', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-15.html', 'title': 'N-15', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-884.html', 'title': 'N-884', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'title': 'N-69', 'score': 1.0000000000000002}]
result = search.search('banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #69 checking search results for 'banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #69 checking search results for 'banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking search results for 'apple apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #70 checking search results for 'apple apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #70 checking search results for 'apple apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking search results for 'apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #71 checking search results for 'apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #71 checking search results for 'apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking search results for 'pear peach banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.012725479786283717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011097175457490055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.010585644293791998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.009948808489820608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009787655790402573}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009580873100392875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008789167831171939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.00737305682158313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.00705147151267853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.00647432061215487}]
result = search.search('pear peach banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #72 checking search results for 'pear peach banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #72 checking search results for 'pear peach banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking search results for 'pear peach banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-527.html', 'title': 'N-527', 'score': 0.999991516198713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-903.html', 'title': 'N-903', 'score': 0.9999156150692685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html', 'title': 'N-885', 'score': 0.9998238478711104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9990842520090095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-428.html', 'title': 'N-428', 'score': 0.998975335421906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-274.html', 'title': 'N-274', 'score': 0.9988237143955351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html', 'title': 'N-878', 'score': 0.9986698424960752}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-598.html', 'title': 'N-598', 'score': 0.9986233599542476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-964.html', 'title': 'N-964', 'score': 0.9986135568622673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-577.html', 'title': 'N-577', 'score': 0.9985677643254509}]
result = search.search('pear peach banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #73 checking search results for 'pear peach banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #73 checking search results for 'pear peach banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking search results for 'banana pear tomato tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01822499609141326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01202337960305141}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011595758767672997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01126755435821809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011001929532283903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010098105471770749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009085720138827618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007810174909831668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.006473419036770592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.0062853041894493115}]
result = search.search('banana pear tomato tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #74 checking search results for 'banana pear tomato tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #74 checking search results for 'banana pear tomato tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking search results for 'banana pear tomato tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-187.html', 'title': 'N-187', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html', 'title': 'N-331', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-740.html', 'title': 'N-740', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-523.html', 'title': 'N-523', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-185.html', 'title': 'N-185', 'score': 0.9999946603074673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-38.html', 'title': 'N-38', 'score': 0.9999926082777492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 0.9999890984631649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-118.html', 'title': 'N-118', 'score': 0.9999786208878436}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-971.html', 'title': 'N-971', 'score': 0.9999708999025319}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-438.html', 'title': 'N-438', 'score': 0.9999665769724299}]
result = search.search('banana pear tomato tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #75 checking search results for 'banana pear tomato tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #75 checking search results for 'banana pear tomato tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #76 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #76 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #77 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #77 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #78 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #78 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #79 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #79 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking search results for 'apple pear pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01813147648332099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012096150028644849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011833057304008606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011345959507545668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01052576259873801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00913551662149082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007520651154782941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0074999419284363135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007140873799605518}]
result = search.search('apple pear pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #80 checking search results for 'apple pear pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #80 checking search results for 'apple pear pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking search results for 'apple pear pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-92.html', 'title': 'N-92', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html', 'title': 'N-900', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-776.html', 'title': 'N-776', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-740.html', 'title': 'N-740', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-518.html', 'title': 'N-518', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-890.html', 'title': 'N-890', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-946.html', 'title': 'N-946', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html', 'title': 'N-381', 'score': 1.0}]
result = search.search('apple pear pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #81 checking search results for 'apple pear pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #81 checking search results for 'apple pear pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking search results for 'banana peach tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017550118729857473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011656932582640325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01142048412238662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011337787901014541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010950789412243948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010161262053867887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009025287207994238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007851229169293265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007845961180561788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007216203714936173}]
result = search.search('banana peach tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #82 checking search results for 'banana peach tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #82 checking search results for 'banana peach tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking search results for 'banana peach tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'title': 'N-183', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-364.html', 'title': 'N-364', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-570.html', 'title': 'N-570', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-774.html', 'title': 'N-774', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-236.html', 'title': 'N-236', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-205.html', 'title': 'N-205', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html', 'title': 'N-828', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html', 'title': 'N-229', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-580.html', 'title': 'N-580', 'score': 1.0000000000000002}]
result = search.search('banana peach tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #83 checking search results for 'banana peach tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #83 checking search results for 'banana peach tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking search results for 'tomato banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017550118729857473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011656932582640325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011420484122386618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011337787901014541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010950789412243948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010161262053867883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009025287207994236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007851229169293263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007845961180561786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007216203714936171}]
result = search.search('tomato banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #84 checking search results for 'tomato banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #84 checking search results for 'tomato banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking search results for 'tomato banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-813.html', 'title': 'N-813', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-238.html', 'title': 'N-238', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-370.html', 'title': 'N-370', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-173.html', 'title': 'N-173', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-338.html', 'title': 'N-338', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-535.html', 'title': 'N-535', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-178.html', 'title': 'N-178', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-271.html', 'title': 'N-271', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-391.html', 'title': 'N-391', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}]
result = search.search('tomato banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #85 checking search results for 'tomato banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #85 checking search results for 'tomato banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking search results for 'tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0.0}]
result = search.search('tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #86 checking search results for 'tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #86 checking search results for 'tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking search results for 'tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0}]
result = search.search('tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #87 checking search results for 'tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #87 checking search results for 'tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking search results for 'apple pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016605809898409755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01185342793117493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011678734124419285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009810855861162298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009767110846715329}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.00928130955489444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008740746831858092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007886655144883693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007428471031853662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006636882362239696}]
result = search.search('apple pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #88 checking search results for 'apple pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #88 checking search results for 'apple pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking search results for 'apple pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-583.html', 'title': 'N-583', 'score': 0.9999993684453062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-818.html', 'title': 'N-818', 'score': 0.9999966897964376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-451.html', 'title': 'N-451', 'score': 0.9999940129918854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-963.html', 'title': 'N-963', 'score': 0.9999937621283271}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-825.html', 'title': 'N-825', 'score': 0.999992732732806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-117.html', 'title': 'N-117', 'score': 0.9999919601256966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html', 'title': 'N-310', 'score': 0.9999792494791696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-470.html', 'title': 'N-470', 'score': 0.9999750845059309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-232.html', 'title': 'N-232', 'score': 0.999973858082214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-150.html', 'title': 'N-150', 'score': 0.9999639555475149}]
result = search.search('apple pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #89 checking search results for 'apple pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #89 checking search results for 'apple pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #90 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #90 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #91 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #91 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #92 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #92 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #93 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #93 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #94 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #94 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #95 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #95 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking search results for 'pear banana pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.018100381517039514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012021322127157744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011330845974469326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011219671312315778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011001016340730632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009849439089840812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00889211581665071}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007819065865813825}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.006662655275836762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.005983230031399676}]
result = search.search('pear banana pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #96 checking search results for 'pear banana pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #96 checking search results for 'pear banana pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking search results for 'pear banana pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html', 'title': 'N-331', 'score': 0.9999716037475628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-191.html', 'title': 'N-191', 'score': 0.9998224917283889}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-375.html', 'title': 'N-375', 'score': 0.9997817980581851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-501.html', 'title': 'N-501', 'score': 0.9993706318024046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-704.html', 'title': 'N-704', 'score': 0.9993066466973407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.9992403226062976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-328.html', 'title': 'N-328', 'score': 0.9992220410661299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-47.html', 'title': 'N-47', 'score': 0.9991563912518749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-193.html', 'title': 'N-193', 'score': 0.9990128095839201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-503.html', 'title': 'N-503', 'score': 0.9990056825294575}]
result = search.search('pear banana pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #97 checking search results for 'pear banana pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #97 checking search results for 'pear banana pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #98 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #98 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #99 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #99 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #100 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #100 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #101 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #101 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #102 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #102 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #103 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #103 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #104 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #104 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #105 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #105 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking search results for 'banana banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('banana banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #106 checking search results for 'banana banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #106 checking search results for 'banana banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking search results for 'banana banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('banana banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #107 checking search results for 'banana banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #107 checking search results for 'banana banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking search results for 'banana coconut apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017599004167524482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012071966746675801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011747301732788646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011195732702533604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010854814090344181}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010045493195935921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008940861975716384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.00785648837949934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007272754374664037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007119614658467722}]
result = search.search('banana coconut apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #108 checking search results for 'banana coconut apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #108 checking search results for 'banana coconut apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking search results for 'banana coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-928.html', 'title': 'N-928', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-306.html', 'title': 'N-306', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-837.html', 'title': 'N-837', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-309.html', 'title': 'N-309', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-603.html', 'title': 'N-603', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'title': 'N-69', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-980.html', 'title': 'N-980', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 1.0}]
result = search.search('banana coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #109 checking search results for 'banana coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #109 checking search results for 'banana coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #110 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #110 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #111 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #111 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking search results for 'tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0.0}]
result = search.search('tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #112 checking search results for 'tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #112 checking search results for 'tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking search results for 'tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0}]
result = search.search('tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #113 checking search results for 'tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #113 checking search results for 'tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #114 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #114 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #115 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #115 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking search results for 'apple peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016095350631103313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011738492510397939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01173717685922528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010985216997917411}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010879474014584126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010129116652445442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007851592713703314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007840601893309988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074259064541596365}]
result = search.search('apple peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #116 checking search results for 'apple peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #116 checking search results for 'apple peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking search results for 'apple peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-264.html', 'title': 'N-264', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-268.html', 'title': 'N-268', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-355.html', 'title': 'N-355', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html', 'title': 'N-381', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-216.html', 'title': 'N-216', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html', 'title': 'N-221', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-263.html', 'title': 'N-263', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-359.html', 'title': 'N-359', 'score': 1.0000000000000002}]
result = search.search('apple peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #117 checking search results for 'apple peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #117 checking search results for 'apple peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking search results for 'coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01718997023167374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01208706964257492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011693076294116906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011206269293521722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010832104155960764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009982414809500502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00910552204361093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007850441844377491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007288029773052712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006736919019056488}]
result = search.search('coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #118 checking search results for 'coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #118 checking search results for 'coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking search results for 'coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'title': 'N-63', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'title': 'N-183', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-268.html', 'title': 'N-268', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-857.html', 'title': 'N-857', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-603.html', 'title': 'N-603', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-928.html', 'title': 'N-928', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-786.html', 'title': 'N-786', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-458.html', 'title': 'N-458', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-884.html', 'title': 'N-884', 'score': 1.0000000000000002}]
result = search.search('coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #119 checking search results for 'coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #119 checking search results for 'coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking search results for 'tomato tomato peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015842641448101158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01211020826453844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011483869599545097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010972527664583006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010854644615354948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010080813833178298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00887607634153808}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074182386121266234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006850823441047688}]
result = search.search('tomato tomato peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #120 checking search results for 'tomato tomato peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #120 checking search results for 'tomato tomato peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking search results for 'tomato tomato peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-863.html', 'title': 'N-863', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-671.html', 'title': 'N-671', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-444.html', 'title': 'N-444', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-797.html', 'title': 'N-797', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-197.html', 'title': 'N-197', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-64.html', 'title': 'N-64', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-404.html', 'title': 'N-404', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-81.html', 'title': 'N-81', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-456.html', 'title': 'N-456', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-921.html', 'title': 'N-921', 'score': 1.0000000000000002}]
result = search.search('tomato tomato peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #121 checking search results for 'tomato tomato peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #121 checking search results for 'tomato tomato peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking search results for 'pear pear pear tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear pear pear tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #122 checking search results for 'pear pear pear tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #122 checking search results for 'pear pear pear tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking search results for 'pear pear pear tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('pear pear pear tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #123 checking search results for 'pear pear pear tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #123 checking search results for 'pear pear pear tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking search results for 'apple pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01813147648332099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012096150028644849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011833057304008606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011345959507545668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01052576259873801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00913551662149082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007520651154782941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0074999419284363135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007140873799605518}]
result = search.search('apple pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #124 checking search results for 'apple pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #124 checking search results for 'apple pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking search results for 'apple pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-92.html', 'title': 'N-92', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html', 'title': 'N-900', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-776.html', 'title': 'N-776', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-740.html', 'title': 'N-740', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-518.html', 'title': 'N-518', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-890.html', 'title': 'N-890', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-946.html', 'title': 'N-946', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html', 'title': 'N-381', 'score': 1.0}]
result = search.search('apple pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #125 checking search results for 'apple pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #125 checking search results for 'apple pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking search results for 'coconut coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #126 checking search results for 'coconut coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #126 checking search results for 'coconut coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking search results for 'coconut coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}]
result = search.search('coconut coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #127 checking search results for 'coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #127 checking search results for 'coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #128 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #128 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking search results for 'coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #129 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #129 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking search results for 'peach tomato banana peach pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.012642635058430517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011076919002424022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.010541360362477896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.009899825025152392}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.00975738639114938}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009556732093295758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008772800109415224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007358061623320025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007026721179898088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006456569031867734}]
result = search.search('peach tomato banana peach pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #130 checking search results for 'peach tomato banana peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #130 checking search results for 'peach tomato banana peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking search results for 'peach tomato banana peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-527.html', 'title': 'N-527', 'score': 0.9999940747956816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-903.html', 'title': 'N-903', 'score': 0.9999852596766301}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html', 'title': 'N-885', 'score': 0.9999371862791988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-428.html', 'title': 'N-428', 'score': 0.9990350757829686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-577.html', 'title': 'N-577', 'score': 0.9989437712759781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9989286353298223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-970.html', 'title': 'N-970', 'score': 0.998801582346434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-964.html', 'title': 'N-964', 'score': 0.9986644567441241}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-274.html', 'title': 'N-274', 'score': 0.9985173893767438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-998.html', 'title': 'N-998', 'score': 0.9983441482178604}]
result = search.search('peach tomato banana peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #131 checking search results for 'peach tomato banana peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #131 checking search results for 'peach tomato banana peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking search results for 'peach tomato coconut apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016732641273120536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011704507637273046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011696140257387164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011190958395635416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010923155499603184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010113972855512536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008928495257767032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007852915150706484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007421682954954111}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007197966155296847}]
result = search.search('peach tomato coconut apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #132 checking search results for 'peach tomato coconut apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #132 checking search results for 'peach tomato coconut apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking search results for 'peach tomato coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-550.html', 'title': 'N-550', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'title': 'N-830', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-664.html', 'title': 'N-664', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-403.html', 'title': 'N-403', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-888.html', 'title': 'N-888', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-672.html', 'title': 'N-672', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-309.html', 'title': 'N-309', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-534.html', 'title': 'N-534', 'score': 1.0}]
result = search.search('peach tomato coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #133 checking search results for 'peach tomato coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #133 checking search results for 'peach tomato coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking search results for 'pear pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.018332490473839804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012104989309179519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011443853196885685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011110616947823754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011006451250170801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009799784400902662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008857412548773081}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007858632155557094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0065504634404862615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006318628993167047}]
result = search.search('pear pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #134 checking search results for 'pear pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #134 checking search results for 'pear pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking search results for 'pear pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-972.html', 'title': 'N-972', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0.9999996757176325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html', 'title': 'N-129', 'score': 0.9999989356280637}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-67.html', 'title': 'N-67', 'score': 0.9999981424071263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-704.html', 'title': 'N-704', 'score': 0.9999974744429357}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-901.html', 'title': 'N-901', 'score': 0.9999972251869107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-254.html', 'title': 'N-254', 'score': 0.9999920031455724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-616.html', 'title': 'N-616', 'score': 0.9999899152570144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-437.html', 'title': 'N-437', 'score': 0.9999895787801917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-557.html', 'title': 'N-557', 'score': 0.9999895787801917}]
result = search.search('pear pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #135 checking search results for 'pear pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #135 checking search results for 'pear pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking search results for 'banana banana apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015469688248481306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011751015583011889}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011293518586939718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010799446051210047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010478821573120604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009232769545516419}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008304121444387379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007779022748677029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0076001029823598515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007416838162734326}]
result = search.search('banana banana apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #136 checking search results for 'banana banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #136 checking search results for 'banana banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking search results for 'banana banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-454.html', 'title': 'N-454', 'score': 0.9999994007328712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-287.html', 'title': 'N-287', 'score': 0.9999982833481671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html', 'title': 'N-699', 'score': 0.9999964916931758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-824.html', 'title': 'N-824', 'score': 0.9999931390136507}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-212.html', 'title': 'N-212', 'score': 0.9999885290828968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-875.html', 'title': 'N-875', 'score': 0.9999854038211861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html', 'title': 'N-76', 'score': 0.9999691752046376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-130.html', 'title': 'N-130', 'score': 0.9999690250961806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-950.html', 'title': 'N-950', 'score': 0.9999546302880309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-488.html', 'title': 'N-488', 'score': 0.9999523613739927}]
result = search.search('banana banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #137 checking search results for 'banana banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #137 checking search results for 'banana banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #138 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #138 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #139 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #139 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking search results for 'apple coconut tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016732641273120536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011704507637273046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011696140257387163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011190958395635414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01092315549960318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010113972855512536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008928495257767032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007852915150706486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.00742168295495411}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007197966155296847}]
result = search.search('apple coconut tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #140 checking search results for 'apple coconut tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #140 checking search results for 'apple coconut tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking search results for 'apple coconut tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-550.html', 'title': 'N-550', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-534.html', 'title': 'N-534', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-61.html', 'title': 'N-61', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'title': 'N-830', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-664.html', 'title': 'N-664', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-403.html', 'title': 'N-403', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-888.html', 'title': 'N-888', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-672.html', 'title': 'N-672', 'score': 1.0}]
result = search.search('apple coconut tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #141 checking search results for 'apple coconut tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #141 checking search results for 'apple coconut tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking search results for 'pear apple tomato coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016963693468382352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011774934484327922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01173657218808782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.01134563213062057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010696844773432022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010129925079243323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008956219135828372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.00770182116528928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007255616309092154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006983761814318528}]
result = search.search('pear apple tomato coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #142 checking search results for 'pear apple tomato coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #142 checking search results for 'pear apple tomato coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking search results for 'pear apple tomato coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'title': 'N-830', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-664.html', 'title': 'N-664', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-403.html', 'title': 'N-403', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-648.html', 'title': 'N-648', 'score': 0.9993817981154297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-769.html', 'title': 'N-769', 'score': 0.9992665217295326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-416.html', 'title': 'N-416', 'score': 0.9992259424303971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0.9991255461102312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-237.html', 'title': 'N-237', 'score': 0.9990829388621024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-226.html', 'title': 'N-226', 'score': 0.9988455751959062}]
result = search.search('pear apple tomato coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #143 checking search results for 'pear apple tomato coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #143 checking search results for 'pear apple tomato coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking search results for 'apple tomato peach pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016365023383716065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011864271940507154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011602424733313297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011221965203735395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010579178635639886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.01013873115488159}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009135808735659187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0076252899259429035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007563001879266675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007222408903239571}]
result = search.search('apple tomato peach pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #144 checking search results for 'apple tomato peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #144 checking search results for 'apple tomato peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking search results for 'apple tomato peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html', 'title': 'N-381', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-407.html', 'title': 'N-407', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-817.html', 'title': 'N-817', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'title': 'N-830', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-353.html', 'title': 'N-353', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-719.html', 'title': 'N-719', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html', 'title': 'N-161', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-447.html', 'title': 'N-447', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-87.html', 'title': 'N-87', 'score': 1.0}]
result = search.search('apple tomato peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #145 checking search results for 'apple tomato peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #145 checking search results for 'apple tomato peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking search results for 'pear coconut coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017329011576651773}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012045997397120825}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011735498621250506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011598697939608554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010012395007173276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009928338249545669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.007891010012982775}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007888889232497965}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007425548583530151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.006238069373375685}]
result = search.search('pear coconut coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #146 checking search results for 'pear coconut coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #146 checking search results for 'pear coconut coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking search results for 'pear coconut coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-923.html', 'title': 'N-923', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-854.html', 'title': 'N-854', 'score': 0.99999787959253}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-100.html', 'title': 'N-100', 'score': 0.9999953153068584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-973.html', 'title': 'N-973', 'score': 0.9999951660956372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-158.html', 'title': 'N-158', 'score': 0.9999914236075441}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html', 'title': 'N-878', 'score': 0.9999907282581038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-580.html', 'title': 'N-580', 'score': 0.9999895377254402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html', 'title': 'N-251', 'score': 0.9999691923568348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-218.html', 'title': 'N-218', 'score': 0.9999604480874766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-781.html', 'title': 'N-781', 'score': 0.9999536743212133}]
result = search.search('pear coconut coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #147 checking search results for 'pear coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #147 checking search results for 'pear coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking search results for 'pear apple peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016365023383716065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011864271940507154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011602424733313296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011221965203735395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010579178635639888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010138731154881592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009135808735659185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007625289925942902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007563001879266676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007222408903239571}]
result = search.search('pear apple peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #148 checking search results for 'pear apple peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #148 checking search results for 'pear apple peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking search results for 'pear apple peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-817.html', 'title': 'N-817', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-353.html', 'title': 'N-353', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-719.html', 'title': 'N-719', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html', 'title': 'N-381', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html', 'title': 'N-161', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-447.html', 'title': 'N-447', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-407.html', 'title': 'N-407', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-316.html', 'title': 'N-316', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-660.html', 'title': 'N-660', 'score': 1.0}]
result = search.search('pear apple peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #149 checking search results for 'pear apple peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #149 checking search results for 'pear apple peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #150 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #150 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #151 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #151 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #152 checking search results for 'tomato coconut coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01834136643573281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012065738703174815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011869399151857285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011820301434539313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01095916859133889}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010150183430556712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008551833629720269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007325862856852626}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006622572269774866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'title': 'N-28', 'score': 0.006339812476478669}]
result = search.search('tomato coconut coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #152 checking search results for 'tomato coconut coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #152 checking search results for 'tomato coconut coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #153 checking search results for 'tomato coconut coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-238.html', 'title': 'N-238', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-711.html', 'title': 'N-711', 'score': 0.9999999529342342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-467.html', 'title': 'N-467', 'score': 0.9999969740096938}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-805.html', 'title': 'N-805', 'score': 0.999994871513572}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-548.html', 'title': 'N-548', 'score': 0.9999917284514404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-877.html', 'title': 'N-877', 'score': 0.9999841131571597}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-920.html', 'title': 'N-920', 'score': 0.9999689931145107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-255.html', 'title': 'N-255', 'score': 0.9999627419388758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-559.html', 'title': 'N-559', 'score': 0.9999627419388758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-984.html', 'title': 'N-984', 'score': 0.9999428779221323}]
result = search.search('tomato coconut coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #153 checking search results for 'tomato coconut coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #153 checking search results for 'tomato coconut coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking search results for 'banana peach peach banana apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01401301869260844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011464151487456851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01114595333151333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010655104103893264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.009998785383453149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009421921692740094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008586189935040725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007749025561647262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007510594380941792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0071889501101600525}]
result = search.search('banana peach peach banana apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #154 checking search results for 'banana peach peach banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #154 checking search results for 'banana peach peach banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking search results for 'banana peach peach banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html', 'title': 'N-311', 'score': 0.9999774594906847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-869.html', 'title': 'N-869', 'score': 0.999968804924328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-338.html', 'title': 'N-338', 'score': 0.9999599337265654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-73.html', 'title': 'N-73', 'score': 0.9999510558708902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-465.html', 'title': 'N-465', 'score': 0.999925495305281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-488.html', 'title': 'N-488', 'score': 0.9997695590372777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-507.html', 'title': 'N-507', 'score': 0.9996195965412502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html', 'title': 'N-76', 'score': 0.999540553768831}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-371.html', 'title': 'N-371', 'score': 0.9994500759616222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-198.html', 'title': 'N-198', 'score': 0.9994092831650762}]
result = search.search('banana peach peach banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #155 checking search results for 'banana peach peach banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #155 checking search results for 'banana peach peach banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking search results for 'peach banana peach coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01308983939258589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.010697387006489862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.010356630285139858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010134654653172122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.00983070433908694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009215789969705509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00899921540639363}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007719607474247882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007697723978673802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007164236061730791}]
result = search.search('peach banana peach coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #156 checking search results for 'peach banana peach coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #156 checking search results for 'peach banana peach coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking search results for 'peach banana peach coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html', 'title': 'N-311', 'score': 0.9999756577949874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-338.html', 'title': 'N-338', 'score': 0.9999567238141295}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0.9999535185608831}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-142.html', 'title': 'N-142', 'score': 0.9999397585301635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-865.html', 'title': 'N-865', 'score': 0.9999376753019724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-118.html', 'title': 'N-118', 'score': 0.9998727232531295}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-291.html', 'title': 'N-291', 'score': 0.999836728250631}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-294.html', 'title': 'N-294', 'score': 0.9996398066810535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-509.html', 'title': 'N-509', 'score': 0.9996252761677523}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-800.html', 'title': 'N-800', 'score': 0.9993633622590646}]
result = search.search('peach banana peach coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #157 checking search results for 'peach banana peach coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #157 checking search results for 'peach banana peach coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking search results for 'banana banana apple coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015362665178199635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011469143079807129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010746420407149921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.0100573419719032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.00987375464189174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009154489598971648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00845356899823729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007636719996122505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007528981515842861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007398598737202903}]
result = search.search('banana banana apple coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #158 checking search results for 'banana banana apple coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #158 checking search results for 'banana banana apple coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking search results for 'banana banana apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-212.html', 'title': 'N-212', 'score': 0.9998594968808794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html', 'title': 'N-311', 'score': 0.9998523724452745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-649.html', 'title': 'N-649', 'score': 0.9998523724452745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-130.html', 'title': 'N-130', 'score': 0.9997950351919362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-874.html', 'title': 'N-874', 'score': 0.9997919986624735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-643.html', 'title': 'N-643', 'score': 0.9997919986624735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-338.html', 'title': 'N-338', 'score': 0.9997919986624735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-390.html', 'title': 'N-390', 'score': 0.9997919986624735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-899.html', 'title': 'N-899', 'score': 0.9996852434067924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-192.html', 'title': 'N-192', 'score': 0.9991724342671409}]
result = search.search('banana banana apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #159 checking search results for 'banana banana apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #159 checking search results for 'banana banana apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking search results for 'banana apple apple tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016532172637711288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011665086117967289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011592204702812504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.00991371018517387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.00984039769275185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009488612479279184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008777197575749796}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007580766258056144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.0068115323033498525}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006541760250069407}]
result = search.search('banana apple apple tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #160 checking search results for 'banana apple apple tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #160 checking search results for 'banana apple apple tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking search results for 'banana apple apple tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-932.html', 'title': 'N-932', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-544.html', 'title': 'N-544', 'score': 0.9999856950257058}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-903.html', 'title': 'N-903', 'score': 0.9999856950257058}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-583.html', 'title': 'N-583', 'score': 0.999850586461072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-145.html', 'title': 'N-145', 'score': 0.999822695377203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-567.html', 'title': 'N-567', 'score': 0.9997918545329689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-470.html', 'title': 'N-470', 'score': 0.9993197406300159}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-117.html', 'title': 'N-117', 'score': 0.9990436229714864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-939.html', 'title': 'N-939', 'score': 0.9986277054240745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-563.html', 'title': 'N-563', 'score': 0.9982680801270902}]
result = search.search('banana apple apple tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #161 checking search results for 'banana apple apple tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #161 checking search results for 'banana apple apple tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking search results for 'banana tomato apple pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017260483037191816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012087131638543018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011778013264012399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011015130730046984}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010427641032306225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010076040068669854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009033494987624435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007608390862673099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007603911585743191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0069079827106129045}]
result = search.search('banana tomato apple pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #162 checking search results for 'banana tomato apple pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #162 checking search results for 'banana tomato apple pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking search results for 'banana tomato apple pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'title': 'N-69', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-143.html', 'title': 'N-143', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-431.html', 'title': 'N-431', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-85.html', 'title': 'N-85', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-966.html', 'title': 'N-966', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-360.html', 'title': 'N-360', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-837.html', 'title': 'N-837', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-980.html', 'title': 'N-980', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html', 'title': 'N-340', 'score': 1.0}]
result = search.search('banana tomato apple pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #163 checking search results for 'banana tomato apple pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #163 checking search results for 'banana tomato apple pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking search results for 'apple tomato banana apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841620456966835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011971460022374304}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011785228515089745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011549903850458057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010686569089526527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010108145447128711}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009068583480694793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0075879854161607545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007207145580395754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006527179878903825}]
result = search.search('apple tomato banana apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #164 checking search results for 'apple tomato banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #164 checking search results for 'apple tomato banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking search results for 'apple tomato banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-429.html', 'title': 'N-429', 'score': 0.9999998669101298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-91.html', 'title': 'N-91', 'score': 0.9999993520004044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-629.html', 'title': 'N-629', 'score': 0.999996203086031}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-384.html', 'title': 'N-384', 'score': 0.9999938921014774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-678.html', 'title': 'N-678', 'score': 0.9999919163177872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-740.html', 'title': 'N-740', 'score': 0.9999793238617923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-932.html', 'title': 'N-932', 'score': 0.9999793238617923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-939.html', 'title': 'N-939', 'score': 0.9999742337489398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-539.html', 'title': 'N-539', 'score': 0.9999707095530507}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html', 'title': 'N-560', 'score': 0.9999702219021176}]
result = search.search('apple tomato banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #165 checking search results for 'apple tomato banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #165 checking search results for 'apple tomato banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking search results for 'peach banana coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015950288416089305}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011690815592633564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011502020040922434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.01113832501822201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010883759362484771}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010016937474234483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008943575371658545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007853500422846422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007250503455500904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007091128207558298}]
result = search.search('peach banana coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #166 checking search results for 'peach banana coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #166 checking search results for 'peach banana coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #167 checking search results for 'peach banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'title': 'N-183', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-570.html', 'title': 'N-570', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-813.html', 'title': 'N-813', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-990.html', 'title': 'N-990', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-891.html', 'title': 'N-891', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-147.html', 'title': 'N-147', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-178.html', 'title': 'N-178', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-543.html', 'title': 'N-543', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-271.html', 'title': 'N-271', 'score': 1.0000000000000002}]
result = search.search('peach banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #167 checking search results for 'peach banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #167 checking search results for 'peach banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #168 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #168 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #169 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #169 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #170 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #170 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #171 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #171 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking search results for 'coconut banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01718997023167374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01208706964257492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011693076294116906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011206269293521722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010832104155960764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009982414809500502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00910552204361093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007850441844377491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007288029773052712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006736919019056488}]
result = search.search('coconut banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #172 checking search results for 'coconut banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #172 checking search results for 'coconut banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking search results for 'coconut banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'title': 'N-63', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'title': 'N-183', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-268.html', 'title': 'N-268', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-857.html', 'title': 'N-857', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-603.html', 'title': 'N-603', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-928.html', 'title': 'N-928', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-786.html', 'title': 'N-786', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-458.html', 'title': 'N-458', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-884.html', 'title': 'N-884', 'score': 1.0000000000000002}]
result = search.search('coconut banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #173 checking search results for 'coconut banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #173 checking search results for 'coconut banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking search results for 'coconut apple apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01714110479689774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011342226582783096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011275203937458353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010042180998425812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.010003455662888511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009667374758657813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009131978286372359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0077827933551923665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007731506606703302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007092317988887165}]
result = search.search('coconut apple apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #174 checking search results for 'coconut apple apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #174 checking search results for 'coconut apple apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking search results for 'coconut apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-583.html', 'title': 'N-583', 'score': 0.9999993136684211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-506.html', 'title': 'N-506', 'score': 0.9999987976834983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-361.html', 'title': 'N-361', 'score': 0.9999987976834983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-330.html', 'title': 'N-330', 'score': 0.9999951187683941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-410.html', 'title': 'N-410', 'score': 0.9999944280404663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-389.html', 'title': 'N-389', 'score': 0.9999923228320287}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-18.html', 'title': 'N-18', 'score': 0.9999912692414569}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-141.html', 'title': 'N-141', 'score': 0.9999891771778412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-826.html', 'title': 'N-826', 'score': 0.9999870786927735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-56.html', 'title': 'N-56', 'score': 0.9999721750476245}]
result = search.search('coconut apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #175 checking search results for 'coconut apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #175 checking search results for 'coconut apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking search results for 'banana banana coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.014717912590507632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011384865984488542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010673085992621907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009877931319644526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009484924179354858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.00905198629634451}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008969561317055971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007780832902138458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.0075888483482094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007403386567966819}]
result = search.search('banana banana coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #176 checking search results for 'banana banana coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #176 checking search results for 'banana banana coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking search results for 'banana banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-361.html', 'title': 'N-361', 'score': 0.9999987658138942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html', 'title': 'N-790', 'score': 0.9999970786867334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-142.html', 'title': 'N-142', 'score': 0.9999933183407246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-800.html', 'title': 'N-800', 'score': 0.9999893806576247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-212.html', 'title': 'N-212', 'score': 0.9999879317118892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-26.html', 'title': 'N-26', 'score': 0.9999839571016191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-273.html', 'title': 'N-273', 'score': 0.9999821956388584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-987.html', 'title': 'N-987', 'score': 0.9999821895091083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-485.html', 'title': 'N-485', 'score': 0.9999676006661705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-509.html', 'title': 'N-509', 'score': 0.9999675836194201}]
result = search.search('banana banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #177 checking search results for 'banana banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #177 checking search results for 'banana banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking search results for 'coconut banana apple tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017599004167524485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012071966746675801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011747301732788647}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011195732702533606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010854814090344183}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010045493195935923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008940861975716384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.00785648837949934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007272754374664038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007119614658467723}]
result = search.search('coconut banana apple tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #178 checking search results for 'coconut banana apple tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #178 checking search results for 'coconut banana apple tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking search results for 'coconut banana apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-928.html', 'title': 'N-928', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-306.html', 'title': 'N-306', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-837.html', 'title': 'N-837', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-309.html', 'title': 'N-309', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-603.html', 'title': 'N-603', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'title': 'N-69', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-980.html', 'title': 'N-980', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 1.0}]
result = search.search('coconut banana apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #179 checking search results for 'coconut banana apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #179 checking search results for 'coconut banana apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking search results for 'peach apple coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01660455065656642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011797870011669886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01140967656129718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011296676987220991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010889909898739723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010051220293631409}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008946032780238911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007850788207840806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007286441159667781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007266122293148812}]
result = search.search('peach apple coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #180 checking search results for 'peach apple coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #180 checking search results for 'peach apple coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking search results for 'peach apple coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-309.html', 'title': 'N-309', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-603.html', 'title': 'N-603', 'score': 0.9997576379040719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-268.html', 'title': 'N-268', 'score': 0.9997275594984868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-385.html', 'title': 'N-385', 'score': 0.9995209076579317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-672.html', 'title': 'N-672', 'score': 0.9994992459147036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-769.html', 'title': 'N-769', 'score': 0.9994594584419931}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-648.html', 'title': 'N-648', 'score': 0.9993817981154298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-528.html', 'title': 'N-528', 'score': 0.9993474443916764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-760.html', 'title': 'N-760', 'score': 0.9993084997476785}]
result = search.search('peach apple coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #181 checking search results for 'peach apple coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #181 checking search results for 'peach apple coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking search results for 'banana tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01670941806909784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012071491793215802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011848532967550791}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011012325687601347}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010430880092533866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.0100485896996318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008988847823103913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007739110753157671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007492835360319172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006700433037127445}]
result = search.search('banana tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #182 checking search results for 'banana tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #182 checking search results for 'banana tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking search results for 'banana tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'title': 'N-63', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-216.html', 'title': 'N-216', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html', 'title': 'N-653', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-15.html', 'title': 'N-15', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-884.html', 'title': 'N-884', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'title': 'N-69', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-873.html', 'title': 'N-873', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-463.html', 'title': 'N-463', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-445.html', 'title': 'N-445', 'score': 1.0000000000000002}]
result = search.search('banana tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #183 checking search results for 'banana tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #183 checking search results for 'banana tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #184 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #184 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #185 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #185 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking search results for 'peach peach banana apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.013984442401257442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012129370857522888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010756382129393924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.010513324464153474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.009689900308048841}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009575725984738789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008839600294226273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007486577864042045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007307954147534854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006646560592285269}]
result = search.search('peach peach banana apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #186 checking search results for 'peach peach banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #186 checking search results for 'peach peach banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking search results for 'peach peach banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-1.html', 'title': 'N-1', 'score': 0.9999914642538495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-157.html', 'title': 'N-157', 'score': 0.999910938538658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9998974952064976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9998327685722124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-281.html', 'title': 'N-281', 'score': 0.9997647285653951}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html', 'title': 'N-276', 'score': 0.9997208511586104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-375.html', 'title': 'N-375', 'score': 0.9992691797931916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-328.html', 'title': 'N-328', 'score': 0.9992139777649526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-272.html', 'title': 'N-272', 'score': 0.9987804373386568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html', 'title': 'N-878', 'score': 0.9986637750007596}]
result = search.search('peach peach banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #187 checking search results for 'peach peach banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #187 checking search results for 'peach peach banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking search results for 'pear tomato banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01670941806909784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012071491793215802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011848532967550791}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011012325687601347}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010430880092533866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.0100485896996318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008988847823103913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007739110753157671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007492835360319172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006700433037127445}]
result = search.search('pear tomato banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #188 checking search results for 'pear tomato banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #188 checking search results for 'pear tomato banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking search results for 'pear tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'title': 'N-63', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-216.html', 'title': 'N-216', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html', 'title': 'N-653', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-15.html', 'title': 'N-15', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-884.html', 'title': 'N-884', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'title': 'N-69', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-873.html', 'title': 'N-873', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-463.html', 'title': 'N-463', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-445.html', 'title': 'N-445', 'score': 1.0000000000000002}]
result = search.search('pear tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #189 checking search results for 'pear tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #189 checking search results for 'pear tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #190 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #190 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #191 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #191 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking search results for 'banana apple tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01760043385328955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012113974494578992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012090788373318905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011735556738228342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011001729294882301}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010049859168975073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00902725649960236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007793463871817541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007253331382606732}]
result = search.search('banana apple tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #192 checking search results for 'banana apple tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #192 checking search results for 'banana apple tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking search results for 'banana apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-111.html', 'title': 'N-111', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-513.html', 'title': 'N-513', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-528.html', 'title': 'N-528', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-398.html', 'title': 'N-398', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-757.html', 'title': 'N-757', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-121.html', 'title': 'N-121', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-306.html', 'title': 'N-306', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-982.html', 'title': 'N-982', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-179.html', 'title': 'N-179', 'score': 1.0}]
result = search.search('banana apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #193 checking search results for 'banana apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #193 checking search results for 'banana apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking search results for 'apple apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #194 checking search results for 'apple apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #194 checking search results for 'apple apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking search results for 'apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'title': 'N-10', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'title': 'N-19', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'title': 'N-36', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 1.0}]
result = search.search('apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #195 checking search results for 'apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #195 checking search results for 'apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking search results for 'peach apple peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.012910579109882647}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012154340137223904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01074390744827247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.010407501807318321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009427531794778257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.009090330273899093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008766525989888417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.0076784877294553714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007296955306020476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007065396022368649}]
result = search.search('peach apple peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #196 checking search results for 'peach apple peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #196 checking search results for 'peach apple peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking search results for 'peach apple peach tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-22.html', 'title': 'N-22', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-414.html', 'title': 'N-414', 'score': 0.9999995520283711}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-339.html', 'title': 'N-339', 'score': 0.9999994422375723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-266.html', 'title': 'N-266', 'score': 0.999997662200111}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-507.html', 'title': 'N-507', 'score': 0.9999972085687506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-1.html', 'title': 'N-1', 'score': 0.9999932761837289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-302.html', 'title': 'N-302', 'score': 0.9999931835446344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-279.html', 'title': 'N-279', 'score': 0.9999773856311553}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-546.html', 'title': 'N-546', 'score': 0.9999461058874086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-873.html', 'title': 'N-873', 'score': 0.9999452234426198}]
result = search.search('peach apple peach tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #197 checking search results for 'peach apple peach tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #197 checking search results for 'peach apple peach tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking search results for 'coconut banana pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017361311817553224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01201583451636166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.01173790912143925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011433322178096077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010622893651574206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.01004311162787801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008893537197540352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007643588071655599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006943390262876339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006846899479777779}]
result = search.search('coconut banana pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #198 checking search results for 'coconut banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #198 checking search results for 'coconut banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking search results for 'coconut banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-884.html', 'title': 'N-884', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html', 'title': 'N-69', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-809.html', 'title': 'N-809', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-951.html', 'title': 'N-951', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-145.html', 'title': 'N-145', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-837.html', 'title': 'N-837', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html', 'title': 'N-885', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-980.html', 'title': 'N-980', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-906.html', 'title': 'N-906', 'score': 1.0}]
result = search.search('coconut banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #199 checking search results for 'coconut banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #199 checking search results for 'coconut banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
