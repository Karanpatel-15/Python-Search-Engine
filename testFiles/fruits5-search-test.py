
import testingtools
import crawler
import searchdata
import search

output = open('fruits5-search-failed.txt', 'w')
success_output = open('fruits5-search-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html')



#Test #0 checking search results for 'papaya orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01959802281391832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959661}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00921301020119066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008876792757873259}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007598885617369492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.0068605175713338665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006825903635115942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.0050275862800066}]
result = search.search('papaya orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #0 checking search results for 'papaya orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #0 checking search results for 'papaya orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking search results for 'papaya orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'title': 'N-59', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html', 'title': 'N-80', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'title': 'N-90', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-121.html', 'title': 'N-121', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'title': 'N-407', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'title': 'N-675', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-34.html', 'title': 'N-34', 'score': 1.0000000000000002}]
result = search.search('papaya orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #1 checking search results for 'papaya orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #1 checking search results for 'papaya orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking search results for 'cherry tomato kiwi tomato cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01209513317605306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.0070376425978125705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.00686466291831452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006772127203283749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.006409768059911789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006408864719791094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005923559593863288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005364644431550108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.00517375420199732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005103090572636868}]
result = search.search('cherry tomato kiwi tomato cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #2 checking search results for 'cherry tomato kiwi tomato cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #2 checking search results for 'cherry tomato kiwi tomato cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking search results for 'cherry tomato kiwi tomato cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-166.html', 'title': 'N-166', 'score': 0.9999341294022389}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-330.html', 'title': 'N-330', 'score': 0.999827397217877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-867.html', 'title': 'N-867', 'score': 0.9998217348698544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'title': 'N-44', 'score': 0.999816194582502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-590.html', 'title': 'N-590', 'score': 0.999793781826968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html', 'title': 'N-120', 'score': 0.9997902477658185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-521.html', 'title': 'N-521', 'score': 0.9997853924493275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-659.html', 'title': 'N-659', 'score': 0.9997759955550113}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-435.html', 'title': 'N-435', 'score': 0.9997714488333211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-568.html', 'title': 'N-568', 'score': 0.9997612155819147}]
result = search.search('cherry tomato kiwi tomato cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #3 checking search results for 'cherry tomato kiwi tomato cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #3 checking search results for 'cherry tomato kiwi tomato cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking search results for 'lime fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013757205549599109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00921301020119066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008843082449883468}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.0076688926416836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007480347135816114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006903083906890486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0068794343821956365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.0058906054096750345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('lime fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #4 checking search results for 'lime fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #4 checking search results for 'lime fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking search results for 'lime fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'title': 'N-53', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-85.html', 'title': 'N-85', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-114.html', 'title': 'N-114', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-34.html', 'title': 'N-34', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-185.html', 'title': 'N-185', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html', 'title': 'N-308', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-405.html', 'title': 'N-405', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-859.html', 'title': 'N-859', 'score': 1.0000000000000002}]
result = search.search('lime fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #5 checking search results for 'lime fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #5 checking search results for 'lime fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking search results for 'apple blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008778572121110812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00875573717362931}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.0074501397105086855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007383564107954054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006484562189848527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005269255623684993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.00513759103948942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005130720332080339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.00497744493513729}]
result = search.search('apple blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #6 checking search results for 'apple blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #6 checking search results for 'apple blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking search results for 'apple blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html', 'title': 'N-625', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-187.html', 'title': 'N-187', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html', 'title': 'N-263', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-622.html', 'title': 'N-622', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-975.html', 'title': 'N-975', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-571.html', 'title': 'N-571', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-955.html', 'title': 'N-955', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-980.html', 'title': 'N-980', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-623.html', 'title': 'N-623', 'score': 1.0000000000000002}]
result = search.search('apple blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #7 checking search results for 'apple blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #7 checking search results for 'apple blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking search results for 'lime coconut orange orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.011932850077778678}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.011762322810378962}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008856835375907672}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008635014051448484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007327720854865693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006925673072482798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006387178194155831}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0062968868222823705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005554113033331254}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.0050079874592819165}]
result = search.search('lime coconut orange orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #8 checking search results for 'lime coconut orange orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #8 checking search results for 'lime coconut orange orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking search results for 'lime coconut orange orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html', 'title': 'N-869', 'score': 0.9996548762995413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-978.html', 'title': 'N-978', 'score': 0.9995476451788956}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-967.html', 'title': 'N-967', 'score': 0.9995184965861712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-547.html', 'title': 'N-547', 'score': 0.9995184965861712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-926.html', 'title': 'N-926', 'score': 0.9994919941569993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-319.html', 'title': 'N-319', 'score': 0.999425378131214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html', 'title': 'N-88', 'score': 0.9994066709987665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-114.html', 'title': 'N-114', 'score': 0.9993893936695735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-145.html', 'title': 'N-145', 'score': 0.999358536038677}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-217.html', 'title': 'N-217', 'score': 0.9993084392251154}]
result = search.search('lime coconut orange orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #9 checking search results for 'lime coconut orange orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #9 checking search results for 'lime coconut orange orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking search results for 'blueberry peach lime lime fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.021912702395552423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01434776362640492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.007790679728732385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007478363307060798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.007324517311557167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007062067751198632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006709309219445208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.00639382345774848}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005431701973644375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.004780083019766349}]
result = search.search('blueberry peach lime lime fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #10 checking search results for 'blueberry peach lime lime fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #10 checking search results for 'blueberry peach lime lime fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking search results for 'blueberry peach lime lime fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-513.html', 'title': 'N-513', 'score': 0.9980504785501233}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-759.html', 'title': 'N-759', 'score': 0.9974262524373715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-924.html', 'title': 'N-924', 'score': 0.9965818792766055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-293.html', 'title': 'N-293', 'score': 0.9964104555777693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html', 'title': 'N-717', 'score': 0.995027532945159}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'title': 'N-675', 'score': 0.9948293083315318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-564.html', 'title': 'N-564', 'score': 0.994807966241003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-406.html', 'title': 'N-406', 'score': 0.9947848883250292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-485.html', 'title': 'N-485', 'score': 0.9945691264527108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 0.9940964628350036}]
result = search.search('blueberry peach lime lime fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #11 checking search results for 'blueberry peach lime lime fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #11 checking search results for 'blueberry peach lime lime fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking search results for 'cherry lime banana banana pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.012810460522512343}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.010965264311435345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.007949766922082852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007299644013248192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.007026615958966778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006762504215917017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006531797851983445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006440051759672403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005014509321751}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.00490400712637179}]
result = search.search('cherry lime banana banana pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #12 checking search results for 'cherry lime banana banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #12 checking search results for 'cherry lime banana banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking search results for 'cherry lime banana banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-886.html', 'title': 'N-886', 'score': 0.999745754105846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-62.html', 'title': 'N-62', 'score': 0.9995086618180332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-852.html', 'title': 'N-852', 'score': 0.9992577871657117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-870.html', 'title': 'N-870', 'score': 0.9971165930964176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-879.html', 'title': 'N-879', 'score': 0.9970869325914932}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 0.9965527212045593}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-834.html', 'title': 'N-834', 'score': 0.9956712908553236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-69.html', 'title': 'N-69', 'score': 0.9953577527366179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-43.html', 'title': 'N-43', 'score': 0.9951422763354758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-871.html', 'title': 'N-871', 'score': 0.9947078341208049}]
result = search.search('cherry lime banana banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #13 checking search results for 'cherry lime banana banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #13 checking search results for 'cherry lime banana banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking search results for 'orange banana papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.0161053347132096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014369924253540887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009042256839866574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.00847885271998369}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007485286757510898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006740698636833837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006716834795751753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006702881203976017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006105737433377699}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.005007161997925154}]
result = search.search('orange banana papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #14 checking search results for 'orange banana papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #14 checking search results for 'orange banana papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking search results for 'orange banana papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-119.html', 'title': 'N-119', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-991.html', 'title': 'N-991', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html', 'title': 'N-96', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-161.html', 'title': 'N-161', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-171.html', 'title': 'N-171', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-409.html', 'title': 'N-409', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-727.html', 'title': 'N-727', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-417.html', 'title': 'N-417', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-632.html', 'title': 'N-632', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html', 'title': 'N-895', 'score': 1.0}]
result = search.search('orange banana papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #15 checking search results for 'orange banana papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #15 checking search results for 'orange banana papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking search results for 'banana apricot orange orange fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.012396654070218685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.010915755239789224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.00832851945166317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008067912278697412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007368304585275243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006960504391231184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006877786888486404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006565336574193369}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006072320933295809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.004696637645473479}]
result = search.search('banana apricot orange orange fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #16 checking search results for 'banana apricot orange orange fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #16 checking search results for 'banana apricot orange orange fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking search results for 'banana apricot orange orange fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-708.html', 'title': 'N-708', 'score': 0.9996944403943855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-596.html', 'title': 'N-596', 'score': 0.9996830242537103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-199.html', 'title': 'N-199', 'score': 0.9984799011505281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-404.html', 'title': 'N-404', 'score': 0.9971427157063826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-525.html', 'title': 'N-525', 'score': 0.9962953116620007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-482.html', 'title': 'N-482', 'score': 0.9958945974374818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html', 'title': 'N-765', 'score': 0.9952679760561279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-99.html', 'title': 'N-99', 'score': 0.9951537790575874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-779.html', 'title': 'N-779', 'score': 0.994622996960606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-917.html', 'title': 'N-917', 'score': 0.9938360263934293}]
result = search.search('banana apricot orange orange fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #17 checking search results for 'banana apricot orange orange fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #17 checking search results for 'banana apricot orange orange fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking search results for 'apricot cherry lime blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014029543554296047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.013575805584544675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008501490013214309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008159171153616418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.0073799256650998925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007199846480529908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006975148339715804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006489545481401475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005411370963969015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.004962634972246697}]
result = search.search('apricot cherry lime blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #18 checking search results for 'apricot cherry lime blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #18 checking search results for 'apricot cherry lime blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking search results for 'apricot cherry lime blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-364.html', 'title': 'N-364', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html', 'title': 'N-200', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html', 'title': 'N-562', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-862.html', 'title': 'N-862', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-714.html', 'title': 'N-714', 'score': 0.9984089162725215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html', 'title': 'N-448', 'score': 0.9983971373283862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-846.html', 'title': 'N-846', 'score': 0.9983945785247718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-213.html', 'title': 'N-213', 'score': 0.99825300653402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.9975880687961373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-248.html', 'title': 'N-248', 'score': 0.997256160700814}]
result = search.search('apricot cherry lime blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #19 checking search results for 'apricot cherry lime blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #19 checking search results for 'apricot cherry lime blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking search results for 'pear pear blueberry coconut pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013328622965821059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008945935228799393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.007810829743145091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007653527219769704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.005995647710290797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.005619547617586196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005532619316173981}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005481091071734186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.004760144797356155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.0044732594031318875}]
result = search.search('pear pear blueberry coconut pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #20 checking search results for 'pear pear blueberry coconut pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #20 checking search results for 'pear pear blueberry coconut pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking search results for 'pear pear blueberry coconut pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-123.html', 'title': 'N-123', 'score': 0.9994834492415927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-40.html', 'title': 'N-40', 'score': 0.9990776182113013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-117.html', 'title': 'N-117', 'score': 0.9988923067615612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-108.html', 'title': 'N-108', 'score': 0.9987786126200251}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-901.html', 'title': 'N-901', 'score': 0.9975748750993291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-31.html', 'title': 'N-31', 'score': 0.9974998777300093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-239.html', 'title': 'N-239', 'score': 0.9974565044660103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-969.html', 'title': 'N-969', 'score': 0.9967644104456628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-225.html', 'title': 'N-225', 'score': 0.9959607190368628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-987.html', 'title': 'N-987', 'score': 0.9959182245243581}]
result = search.search('pear pear blueberry coconut pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #21 checking search results for 'pear pear blueberry coconut pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #21 checking search results for 'pear pear blueberry coconut pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking search results for 'tomato kiwi papaya tomato lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.02225945913279588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013783952111422403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008720310103784906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008252773368108465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007683091735097943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007138102339808768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006679224718218903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006482365148728844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005779038744051266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005346996258197379}]
result = search.search('tomato kiwi papaya tomato lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #22 checking search results for 'tomato kiwi papaya tomato lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #22 checking search results for 'tomato kiwi papaya tomato lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking search results for 'tomato kiwi papaya tomato lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-387.html', 'title': 'N-387', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-176.html', 'title': 'N-176', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html', 'title': 'N-164', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-214.html', 'title': 'N-214', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-364.html', 'title': 'N-364', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-632.html', 'title': 'N-632', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-687.html', 'title': 'N-687', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-712.html', 'title': 'N-712', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-302.html', 'title': 'N-302', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-772.html', 'title': 'N-772', 'score': 1.0000000000000002}]
result = search.search('tomato kiwi papaya tomato lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #23 checking search results for 'tomato kiwi papaya tomato lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #23 checking search results for 'tomato kiwi papaya tomato lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking search results for 'apple kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009047898216176764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008849639962160242}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006782109080848896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006686736342187827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005623628634923476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'title': 'N-4', 'score': 0.005372748134323713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005269255623684993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005130720332080339}]
result = search.search('apple kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #24 checking search results for 'apple kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #24 checking search results for 'apple kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking search results for 'apple kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'title': 'N-53', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-373.html', 'title': 'N-373', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-399.html', 'title': 'N-399', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-555.html', 'title': 'N-555', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html', 'title': 'N-260', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-294.html', 'title': 'N-294', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-828.html', 'title': 'N-828', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html', 'title': 'N-625', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-187.html', 'title': 'N-187', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-68.html', 'title': 'N-68', 'score': 1.0000000000000002}]
result = search.search('apple kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #25 checking search results for 'apple kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #25 checking search results for 'apple kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking search results for 'orange banana lime banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.012623393423877293}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.011991861025427493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009166358435572737}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007441754293065275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.007354140116805486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006664714534997754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.0060742170135744756}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.005969098686194611}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005508640133690791}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005014864711198609}]
result = search.search('orange banana lime banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #26 checking search results for 'orange banana lime banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #26 checking search results for 'orange banana lime banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking search results for 'orange banana lime banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-387.html', 'title': 'N-387', 'score': 0.9998745957083682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-877.html', 'title': 'N-877', 'score': 0.9996920195355726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-886.html', 'title': 'N-886', 'score': 0.999570339951431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-69.html', 'title': 'N-69', 'score': 0.9995480275216985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-267.html', 'title': 'N-267', 'score': 0.9995374148839523}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-108.html', 'title': 'N-108', 'score': 0.9994804346526884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-390.html', 'title': 'N-390', 'score': 0.9994556776146606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-793.html', 'title': 'N-793', 'score': 0.9994556776146606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html', 'title': 'N-126', 'score': 0.9994441017261618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-218.html', 'title': 'N-218', 'score': 0.9994330181054625}]
result = search.search('orange banana lime banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #27 checking search results for 'orange banana lime banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #27 checking search results for 'orange banana lime banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking search results for 'pear papaya fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.022556451769606824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013828937621730772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008614819881268871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008393296272926842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007517926964277265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007259767340723406}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.00650545276302925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005835427921898784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005732591625610598}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005060973459576686}]
result = search.search('pear papaya fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #28 checking search results for 'pear papaya fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #28 checking search results for 'pear papaya fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking search results for 'pear papaya fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html', 'title': 'N-346', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-329.html', 'title': 'N-329', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-73.html', 'title': 'N-73', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-38.html', 'title': 'N-38', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-568.html', 'title': 'N-568', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-492.html', 'title': 'N-492', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-720.html', 'title': 'N-720', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-793.html', 'title': 'N-793', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-788.html', 'title': 'N-788', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-676.html', 'title': 'N-676', 'score': 1.0000000000000002}]
result = search.search('pear papaya fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #29 checking search results for 'pear papaya fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #29 checking search results for 'pear papaya fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking search results for 'apricot tomato banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014248984533193046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009129170033410556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008064081151278046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.0076990312178169375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007293294950225148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007038887584123178}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006875496734756531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005876929438680796}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005127088861940443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005016850531842438}]
result = search.search('apricot tomato banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #30 checking search results for 'apricot tomato banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #30 checking search results for 'apricot tomato banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking search results for 'apricot tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-212.html', 'title': 'N-212', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-239.html', 'title': 'N-239', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-921.html', 'title': 'N-921', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-47.html', 'title': 'N-47', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-72.html', 'title': 'N-72', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-151.html', 'title': 'N-151', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'title': 'N-169', 'score': 1.0}]
result = search.search('apricot tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #31 checking search results for 'apricot tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #31 checking search results for 'apricot tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking search results for 'cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #32 checking search results for 'cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #32 checking search results for 'cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking search results for 'cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #33 checking search results for 'cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #33 checking search results for 'cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking search results for 'lime banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01959802281391832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014090901734054615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00904389594643429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008760444496979086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0070792467301026745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006989694820629549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005886906025989564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005181026047321569}]
result = search.search('lime banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #34 checking search results for 'lime banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #34 checking search results for 'lime banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking search results for 'lime banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html', 'title': 'N-327', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html', 'title': 'N-378', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'title': 'N-44', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-135.html', 'title': 'N-135', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-202.html', 'title': 'N-202', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html', 'title': 'N-517', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html', 'title': 'N-528', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-555.html', 'title': 'N-555', 'score': 1.0000000000000002}]
result = search.search('lime banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #35 checking search results for 'lime banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #35 checking search results for 'lime banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking search results for 'cherry blueberry pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014082261980304713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.00839198503405557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008228281452014232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007261931616729517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007099933716276452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006846229904864042}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.0063624883897625715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005281846240816962}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005061496364647039}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.005056367204996033}]
result = search.search('cherry blueberry pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #36 checking search results for 'cherry blueberry pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #36 checking search results for 'cherry blueberry pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking search results for 'cherry blueberry pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'title': 'N-169', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-823.html', 'title': 'N-823', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html', 'title': 'N-973', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-366.html', 'title': 'N-366', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-887.html', 'title': 'N-887', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-19.html', 'title': 'N-19', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-364.html', 'title': 'N-364', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-538.html', 'title': 'N-538', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-588.html', 'title': 'N-588', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-691.html', 'title': 'N-691', 'score': 1.0000000000000002}]
result = search.search('cherry blueberry pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #37 checking search results for 'cherry blueberry pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #37 checking search results for 'cherry blueberry pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking search results for 'fig fig cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.02448465434712968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01445571688771404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00920454178774972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008852018856991826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007477541976292341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007465296026063533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006640689967929963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006503029744986051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005549144472853955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.005170016830274103}]
result = search.search('fig fig cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #38 checking search results for 'fig fig cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #38 checking search results for 'fig fig cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking search results for 'fig fig cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-854.html', 'title': 'N-854', 'score': 0.9999998398651934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-889.html', 'title': 'N-889', 'score': 0.9999962202693687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-476.html', 'title': 'N-476', 'score': 0.9999945756326716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-139.html', 'title': 'N-139', 'score': 0.9999923409095957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-662.html', 'title': 'N-662', 'score': 0.9999918969052026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-686.html', 'title': 'N-686', 'score': 0.9999814797763699}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-219.html', 'title': 'N-219', 'score': 0.9999193681664967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-758.html', 'title': 'N-758', 'score': 0.9998932978060681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-785.html', 'title': 'N-785', 'score': 0.9998750264769735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html', 'title': 'N-594', 'score': 0.9998258512649391}]
result = search.search('fig fig cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #39 checking search results for 'fig fig cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #39 checking search results for 'fig fig cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking search results for 'cherry coconut apple cherry cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.010790068273483937}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.0077305860074368855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.0068426700934378455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006199068742563081}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006083418385687155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005278737983756064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005188616701907272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.004960559515723933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.004753845306210994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.004682057609185211}]
result = search.search('cherry coconut apple cherry cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #40 checking search results for 'cherry coconut apple cherry cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #40 checking search results for 'cherry coconut apple cherry cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking search results for 'cherry coconut apple cherry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'title': 'N-407', 'score': 0.9998958631515686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-469.html', 'title': 'N-469', 'score': 0.9995123583664169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-553.html', 'title': 'N-553', 'score': 0.9994073172586668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-532.html', 'title': 'N-532', 'score': 0.9992877922327803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-390.html', 'title': 'N-390', 'score': 0.9991867767041226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html', 'title': 'N-235', 'score': 0.9991088288391512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html', 'title': 'N-88', 'score': 0.9990625767749525}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-106.html', 'title': 'N-106', 'score': 0.9990444967467649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html', 'title': 'N-488', 'score': 0.9990270661377908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-974.html', 'title': 'N-974', 'score': 0.9988822162860721}]
result = search.search('cherry coconut apple cherry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #41 checking search results for 'cherry coconut apple cherry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #41 checking search results for 'cherry coconut apple cherry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #42 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #42 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #43 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #43 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking search results for 'papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}]
result = search.search('papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #44 checking search results for 'papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #44 checking search results for 'papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking search results for 'papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}]
result = search.search('papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #45 checking search results for 'papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #45 checking search results for 'papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking search results for 'papaya pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01950291001893492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013722327645816877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008635634647189432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008516815162314109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.00752941815955579}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007287949833811631}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006349982921113973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006027552336974923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005864815267294833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005116244614533907}]
result = search.search('papaya pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #46 checking search results for 'papaya pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #46 checking search results for 'papaya pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking search results for 'papaya pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-373.html', 'title': 'N-373', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html', 'title': 'N-88', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-859.html', 'title': 'N-859', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html', 'title': 'N-277', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-253.html', 'title': 'N-253', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-73.html', 'title': 'N-73', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html', 'title': 'N-83', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-551.html', 'title': 'N-551', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-852.html', 'title': 'N-852', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-732.html', 'title': 'N-732', 'score': 1.0000000000000002}]
result = search.search('papaya pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #47 checking search results for 'papaya pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #47 checking search results for 'papaya pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking search results for 'apricot orange orange tomato fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01196223478532235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.011833857546740954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008414436264411403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00787814263911414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007428992452635474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0070422237462356594}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006867615049941287}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006366019125361788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006075091814323987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.004760864152510488}]
result = search.search('apricot orange orange tomato fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #48 checking search results for 'apricot orange orange tomato fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #48 checking search results for 'apricot orange orange tomato fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking search results for 'apricot orange orange tomato fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-199.html', 'title': 'N-199', 'score': 0.9998887249439503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-708.html', 'title': 'N-708', 'score': 0.9997140022155127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-596.html', 'title': 'N-596', 'score': 0.9997033667494809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-831.html', 'title': 'N-831', 'score': 0.9996931741815369}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-220.html', 'title': 'N-220', 'score': 0.9996834014928868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html', 'title': 'N-261', 'score': 0.9996772268985386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-58.html', 'title': 'N-58', 'score': 0.9996401015468531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html', 'title': 'N-765', 'score': 0.999625030573263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-114.html', 'title': 'N-114', 'score': 0.9996110519777575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-943.html', 'title': 'N-943', 'score': 0.9996110519777575}]
result = search.search('apricot orange orange tomato fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #49 checking search results for 'apricot orange orange tomato fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #49 checking search results for 'apricot orange orange tomato fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking search results for 'papaya cherry fig apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.020224414073694515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014035213039075928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008679349730067822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.0076739139974701465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007356149215788241}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007166052653762562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006166715350142637}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005846300097905393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005410402032129796}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005047906690350054}]
result = search.search('papaya cherry fig apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #50 checking search results for 'papaya cherry fig apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #50 checking search results for 'papaya cherry fig apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking search results for 'papaya cherry fig apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-855.html', 'title': 'N-855', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-25.html', 'title': 'N-25', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-971.html', 'title': 'N-971', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-456.html', 'title': 'N-456', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-714.html', 'title': 'N-714', 'score': 0.9987531021553887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-775.html', 'title': 'N-775', 'score': 0.9972510606153964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-844.html', 'title': 'N-844', 'score': 0.9972420922518582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.9967325996120479}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-394.html', 'title': 'N-394', 'score': 0.9963422286662235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-830.html', 'title': 'N-830', 'score': 0.9961717311311644}]
result = search.search('papaya cherry fig apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #51 checking search results for 'papaya cherry fig apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #51 checking search results for 'papaya cherry fig apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking search results for 'orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #52 checking search results for 'orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #52 checking search results for 'orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking search results for 'orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #53 checking search results for 'orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #53 checking search results for 'orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking search results for 'tomato apple apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014564602387590582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009047898216176766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.0074036902956404835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006617492142540352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748253}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006191216587822922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005269255623684994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005145047672791457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005022116799989984}]
result = search.search('tomato apple apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #54 checking search results for 'tomato apple apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #54 checking search results for 'tomato apple apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking search results for 'tomato apple apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html', 'title': 'N-100', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-212.html', 'title': 'N-212', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-433.html', 'title': 'N-433', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-457.html', 'title': 'N-457', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-767.html', 'title': 'N-767', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html', 'title': 'N-939', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-47.html', 'title': 'N-47', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-124.html', 'title': 'N-124', 'score': 1.0000000000000002}]
result = search.search('tomato apple apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #55 checking search results for 'tomato apple apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #55 checking search results for 'tomato apple apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #56 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #56 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #57 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #57 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking search results for 'cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #58 checking search results for 'cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #58 checking search results for 'cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking search results for 'cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #59 checking search results for 'cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #59 checking search results for 'cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking search results for 'banana apple blueberry papaya apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014113372998284884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.012407923540213226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008694506038263794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008240551572787741}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.00707062970858443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006916455553741348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006404434900940496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005723218505594765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005068920913100018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.004977585573160822}]
result = search.search('banana apple blueberry papaya apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #60 checking search results for 'banana apple blueberry papaya apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #60 checking search results for 'banana apple blueberry papaya apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking search results for 'banana apple blueberry papaya apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html', 'title': 'N-96', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-865.html', 'title': 'N-865', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html', 'title': 'N-101', 'score': 0.9984331790676816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-484.html', 'title': 'N-484', 'score': 0.9979953661031533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html', 'title': 'N-234', 'score': 0.9979947651209189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html', 'title': 'N-321', 'score': 0.9979570101114463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-626.html', 'title': 'N-626', 'score': 0.9965686315791777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-435.html', 'title': 'N-435', 'score': 0.9965567125251958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html', 'title': 'N-208', 'score': 0.9965270376739105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-888.html', 'title': 'N-888', 'score': 0.9950709214907336}]
result = search.search('banana apple blueberry papaya apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #61 checking search results for 'banana apple blueberry papaya apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #61 checking search results for 'banana apple blueberry papaya apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking search results for 'banana lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01959802281391832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014090901734054615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00904389594643429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008760444496979086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0070792467301026745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006989694820629549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005886906025989564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005181026047321569}]
result = search.search('banana lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #62 checking search results for 'banana lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #62 checking search results for 'banana lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking search results for 'banana lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html', 'title': 'N-327', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html', 'title': 'N-378', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'title': 'N-44', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-135.html', 'title': 'N-135', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-202.html', 'title': 'N-202', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html', 'title': 'N-517', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html', 'title': 'N-528', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-555.html', 'title': 'N-555', 'score': 1.0000000000000002}]
result = search.search('banana lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #63 checking search results for 'banana lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #63 checking search results for 'banana lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking search results for 'apricot peach lime apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014556841005307084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.013879939134233887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008737929070488265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008677928798537233}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.0074333491266309025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007184711456911252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006429574466776329}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.00614852029638468}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005870151339622786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.0050999677722138375}]
result = search.search('apricot peach lime apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #64 checking search results for 'apricot peach lime apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #64 checking search results for 'apricot peach lime apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking search results for 'apricot peach lime apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html', 'title': 'N-684', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-511.html', 'title': 'N-511', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-399.html', 'title': 'N-399', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-187.html', 'title': 'N-187', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-609.html', 'title': 'N-609', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-71.html', 'title': 'N-71', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html', 'title': 'N-200', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-937.html', 'title': 'N-937', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-563.html', 'title': 'N-563', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html', 'title': 'N-315', 'score': 0.997345374462442}]
result = search.search('apricot peach lime apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #65 checking search results for 'apricot peach lime apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #65 checking search results for 'apricot peach lime apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking search results for 'pear fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01950291001893492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014116704500492584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008635634647189432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008516815162314109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.00752941815955579}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007471972519175664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006947064283263248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006745293846435827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.0057330950903437755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005430313114579634}]
result = search.search('pear fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #66 checking search results for 'pear fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #66 checking search results for 'pear fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking search results for 'pear fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-56.html', 'title': 'N-56', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'title': 'N-169', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-211.html', 'title': 'N-211', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-423.html', 'title': 'N-423', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-168.html', 'title': 'N-168', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-238.html', 'title': 'N-238', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-914.html', 'title': 'N-914', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html', 'title': 'N-965', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html', 'title': 'N-203', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-564.html', 'title': 'N-564', 'score': 1.0000000000000002}]
result = search.search('pear fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #67 checking search results for 'pear fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #67 checking search results for 'pear fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking search results for 'fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}]
result = search.search('fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #68 checking search results for 'fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #68 checking search results for 'fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking search results for 'fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}]
result = search.search('fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #69 checking search results for 'fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #69 checking search results for 'fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #70 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #70 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #71 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #71 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking search results for 'kiwi peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01462057710776871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00916167405211538}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008848559751307928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006949816978643529}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006916156262605176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006084371387888807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005461921274348834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.004919361874775038}]
result = search.search('kiwi peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #72 checking search results for 'kiwi peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #72 checking search results for 'kiwi peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking search results for 'kiwi peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'title': 'N-407', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html', 'title': 'N-939', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-43.html', 'title': 'N-43', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-151.html', 'title': 'N-151', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'title': 'N-169', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-202.html', 'title': 'N-202', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-382.html', 'title': 'N-382', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-399.html', 'title': 'N-399', 'score': 1.0000000000000002}]
result = search.search('kiwi peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #73 checking search results for 'kiwi peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #73 checking search results for 'kiwi peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking search results for 'kiwi banana orange pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014121447387904502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008811688342652607}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008296281896390957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.00745492113696164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007148965660360226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0067040944600994514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006538391600618776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005908926020935862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.0053283147973004165}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.0051323301201030465}]
result = search.search('kiwi banana orange pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #74 checking search results for 'kiwi banana orange pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #74 checking search results for 'kiwi banana orange pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking search results for 'kiwi banana orange pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html', 'title': 'N-209', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-959.html', 'title': 'N-959', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-955.html', 'title': 'N-955', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-809.html', 'title': 'N-809', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-885.html', 'title': 'N-885', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-354.html', 'title': 'N-354', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-320.html', 'title': 'N-320', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-632.html', 'title': 'N-632', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-29.html', 'title': 'N-29', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html', 'title': 'N-710', 'score': 1.0}]
result = search.search('kiwi banana orange pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #75 checking search results for 'kiwi banana orange pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #75 checking search results for 'kiwi banana orange pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking search results for 'pear lime apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01553480422691007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014600969734661639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00877415751934855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008548088030355876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007706964977199231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007408232423973748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006879055256465818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006722951857535215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.0051254864552737625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.00505682671800126}]
result = search.search('pear lime apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #76 checking search results for 'pear lime apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #76 checking search results for 'pear lime apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking search results for 'pear lime apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-423.html', 'title': 'N-423', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-338.html', 'title': 'N-338', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-286.html', 'title': 'N-286', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-187.html', 'title': 'N-187', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-364.html', 'title': 'N-364', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-876.html', 'title': 'N-876', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-596.html', 'title': 'N-596', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-852.html', 'title': 'N-852', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-71.html', 'title': 'N-71', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-359.html', 'title': 'N-359', 'score': 1.0000000000000002}]
result = search.search('pear lime apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #77 checking search results for 'pear lime apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #77 checking search results for 'pear lime apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking search results for 'papaya coconut coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014588066276856063}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01401114859975992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.00880304894470267}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00766545951993994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007431779979921161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006131617655323352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006124519605811513}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.005800103463553714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.004986082690616165}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.004978606212641293}]
result = search.search('papaya coconut coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #78 checking search results for 'papaya coconut coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #78 checking search results for 'papaya coconut coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking search results for 'papaya coconut coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-779.html', 'title': 'N-779', 'score': 0.9999972598039912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-889.html', 'title': 'N-889', 'score': 0.9999958056241315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-580.html', 'title': 'N-580', 'score': 0.999995258457914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-639.html', 'title': 'N-639', 'score': 0.9999932378054412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-259.html', 'title': 'N-259', 'score': 0.9999928366840473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html', 'title': 'N-87', 'score': 0.9999924145171122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-384.html', 'title': 'N-384', 'score': 0.9999874532731292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 0.9999805541124152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-440.html', 'title': 'N-440', 'score': 0.9999170282620554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-821.html', 'title': 'N-821', 'score': 0.999896506945306}]
result = search.search('papaya coconut coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #79 checking search results for 'papaya coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #79 checking search results for 'papaya coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #80 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #80 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #81 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #81 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking search results for 'kiwi peach banana peach apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014022073857947324}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009053643167185323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008101153177794142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007313372704255132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007200239371732501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006980403661170594}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006817218388065425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005596195937418051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005182285306892251}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.004891963327658366}]
result = search.search('kiwi peach banana peach apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #82 checking search results for 'kiwi peach banana peach apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #82 checking search results for 'kiwi peach banana peach apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking search results for 'kiwi peach banana peach apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html', 'title': 'N-308', 'score': 0.9997171903413381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html', 'title': 'N-973', 'score': 0.9996701473117455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html', 'title': 'N-111', 'score': 0.9996213475075938}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html', 'title': 'N-209', 'score': 0.9996127013867506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-22.html', 'title': 'N-22', 'score': 0.9996127013867506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-955.html', 'title': 'N-955', 'score': 0.9995671331766822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-482.html', 'title': 'N-482', 'score': 0.9984516321728708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html', 'title': 'N-448', 'score': 0.9976693405269633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html', 'title': 'N-465', 'score': 0.9976074647549027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-115.html', 'title': 'N-115', 'score': 0.9962221805509479}]
result = search.search('kiwi peach banana peach apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #83 checking search results for 'kiwi peach banana peach apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #83 checking search results for 'kiwi peach banana peach apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking search results for 'apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #84 checking search results for 'apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #84 checking search results for 'apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking search results for 'apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'title': 'N-53', 'score': 1.0}]
result = search.search('apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #85 checking search results for 'apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #85 checking search results for 'apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking search results for 'tomato apple cherry tomato papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01669486304174167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013853763635464209}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008610215806578546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.0075597734912246015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.00722104406521374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.00706314640116939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006024293802674098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005780146274914979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005379500411073336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.0051759648786640685}]
result = search.search('tomato apple cherry tomato papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #86 checking search results for 'tomato apple cherry tomato papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #86 checking search results for 'tomato apple cherry tomato papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking search results for 'tomato apple cherry tomato papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-273.html', 'title': 'N-273', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-569.html', 'title': 'N-569', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-759.html', 'title': 'N-759', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-921.html', 'title': 'N-921', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-829.html', 'title': 'N-829', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html', 'title': 'N-101', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-889.html', 'title': 'N-889', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-364.html', 'title': 'N-364', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-855.html', 'title': 'N-855', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html', 'title': 'N-146', 'score': 1.0}]
result = search.search('tomato apple cherry tomato papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #87 checking search results for 'tomato apple cherry tomato papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #87 checking search results for 'tomato apple cherry tomato papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking search results for 'blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005181026047321568}]
result = search.search('blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #88 checking search results for 'blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #88 checking search results for 'blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking search results for 'blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #89 checking search results for 'blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #89 checking search results for 'blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking search results for 'blueberry peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014287560881190917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009205959754157257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.007991106777017148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007734456897596643}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.00707352939745872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006924828798703992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006917927278807953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005289229069919684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005273248622481399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005176515934238456}]
result = search.search('blueberry peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #90 checking search results for 'blueberry peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #90 checking search results for 'blueberry peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking search results for 'blueberry peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html', 'title': 'N-465', 'score': 0.9999996632907793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-138.html', 'title': 'N-138', 'score': 0.9999980091273476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-401.html', 'title': 'N-401', 'score': 0.9999966250926886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html', 'title': 'N-80', 'score': 0.9999945289866975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-259.html', 'title': 'N-259', 'score': 0.9999925740292982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-358.html', 'title': 'N-358', 'score': 0.9999895772864723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-370.html', 'title': 'N-370', 'score': 0.9999828934783845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html', 'title': 'N-87', 'score': 0.9998995286353443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-159.html', 'title': 'N-159', 'score': 0.9998735438410287}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-43.html', 'title': 'N-43', 'score': 0.9998619790416788}]
result = search.search('blueberry peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #91 checking search results for 'blueberry peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #91 checking search results for 'blueberry peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking search results for 'papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}]
result = search.search('papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #92 checking search results for 'papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #92 checking search results for 'papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking search results for 'papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}]
result = search.search('papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #93 checking search results for 'papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #93 checking search results for 'papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking search results for 'lime peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.019792678824805714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014578217103481284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008501619396847302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008488297108337222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007052769349148549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006815925861997122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005883300353498685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005387160801070893}]
result = search.search('lime peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #94 checking search results for 'lime peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #94 checking search results for 'lime peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking search results for 'lime peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-399.html', 'title': 'N-399', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-468.html', 'title': 'N-468', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html', 'title': 'N-490', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-71.html', 'title': 'N-71', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html', 'title': 'N-747', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-858.html', 'title': 'N-858', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'title': 'N-59', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'title': 'N-90', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html', 'title': 'N-100', 'score': 1.0}]
result = search.search('lime peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #95 checking search results for 'lime peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #95 checking search results for 'lime peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking search results for 'apple blueberry orange apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014088210019028198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008715548605647268}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008641260451507446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007351668637564179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.0067424839351213905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006402305412124435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006042960441106155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005042903610863689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.004958897170893589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.004845966176412634}]
result = search.search('apple blueberry orange apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #96 checking search results for 'apple blueberry orange apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #96 checking search results for 'apple blueberry orange apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking search results for 'apple blueberry orange apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html', 'title': 'N-96', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-173.html', 'title': 'N-173', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-667.html', 'title': 'N-667', 'score': 0.9987219189460272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html', 'title': 'N-101', 'score': 0.9983688765582185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-580.html', 'title': 'N-580', 'score': 0.9979451435262316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html', 'title': 'N-968', 'score': 0.9978034373013638}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-213.html', 'title': 'N-213', 'score': 0.9972990884416492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html', 'title': 'N-648', 'score': 0.997278713230397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-339.html', 'title': 'N-339', 'score': 0.9972004770294647}]
result = search.search('apple blueberry orange apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #97 checking search results for 'apple blueberry orange apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #97 checking search results for 'apple blueberry orange apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking search results for 'pear blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014620584532414079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008957207194358581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008866630617779708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007237677690811102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007138969174558063}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006949061311214818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006876910079512763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005220890244637338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.005173257257766003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005032889075430583}]
result = search.search('pear blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #98 checking search results for 'pear blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #98 checking search results for 'pear blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking search results for 'pear blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'title': 'N-53', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html', 'title': 'N-231', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-26.html', 'title': 'N-26', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html', 'title': 'N-88', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'title': 'N-169', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-211.html', 'title': 'N-211', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html', 'title': 'N-278', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-621.html', 'title': 'N-621', 'score': 1.0000000000000002}]
result = search.search('pear blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #99 checking search results for 'pear blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #99 checking search results for 'pear blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'title': 'N-4', 'score': 0.005372748134323713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #100 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #100 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #101 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #101 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking search results for 'banana papaya apricot fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.019498312690246752}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013802842147653}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008839806733188882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008449331691489386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007570683519281174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.0071963544436439986}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006525795318176526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0063066770766986155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.00584057684563071}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.00516466746031299}]
result = search.search('banana papaya apricot fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #102 checking search results for 'banana papaya apricot fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #102 checking search results for 'banana papaya apricot fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking search results for 'banana papaya apricot fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-247.html', 'title': 'N-247', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-865.html', 'title': 'N-865', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-645.html', 'title': 'N-645', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-867.html', 'title': 'N-867', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-210.html', 'title': 'N-210', 'score': 0.9986984143599998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html', 'title': 'N-321', 'score': 0.9979529330389318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-219.html', 'title': 'N-219', 'score': 0.9979473030508418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-779.html', 'title': 'N-779', 'score': 0.9974325390353217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-326.html', 'title': 'N-326', 'score': 0.9974300419601394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-199.html', 'title': 'N-199', 'score': 0.9974177318754385}]
result = search.search('banana papaya apricot fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #103 checking search results for 'banana papaya apricot fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #103 checking search results for 'banana papaya apricot fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking search results for 'lime banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01959802281391832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014090901734054615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00904389594643429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008760444496979086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0070792467301026745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006989694820629549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005886906025989564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005181026047321569}]
result = search.search('lime banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #104 checking search results for 'lime banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #104 checking search results for 'lime banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking search results for 'lime banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html', 'title': 'N-327', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html', 'title': 'N-378', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'title': 'N-44', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-135.html', 'title': 'N-135', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-202.html', 'title': 'N-202', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html', 'title': 'N-517', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html', 'title': 'N-528', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-555.html', 'title': 'N-555', 'score': 1.0000000000000002}]
result = search.search('lime banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #105 checking search results for 'lime banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #105 checking search results for 'lime banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking search results for 'pear lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.019308841884856914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014577632708795894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008527199543906853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008335388262253253}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007698675289623947}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007405078808162829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006875859926650469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006520999978127136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005223070101355963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.005159575024279354}]
result = search.search('pear lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #106 checking search results for 'pear lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #106 checking search results for 'pear lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking search results for 'pear lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'title': 'N-53', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'title': 'N-59', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html', 'title': 'N-638', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-666.html', 'title': 'N-666', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-26.html', 'title': 'N-26', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-41.html', 'title': 'N-41', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'title': 'N-44', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'title': 'N-256', 'score': 1.0000000000000002}]
result = search.search('pear lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #107 checking search results for 'pear lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #107 checking search results for 'pear lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking search results for 'apricot tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('apricot tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #108 checking search results for 'apricot tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #108 checking search results for 'apricot tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking search results for 'apricot tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'title': 'N-53', 'score': 1.0}]
result = search.search('apricot tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #109 checking search results for 'apricot tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #109 checking search results for 'apricot tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #110 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #110 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #111 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #111 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking search results for 'blueberry lime pear kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014525212729816874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.013356832711204783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008823218982399848}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008510544537273948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007441727216646669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007363250778883612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006841860591672253}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0067678253861054565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.0051641609805113805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005164105283288538}]
result = search.search('blueberry lime pear kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #112 checking search results for 'blueberry lime pear kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #112 checking search results for 'blueberry lime pear kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking search results for 'blueberry lime pear kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-187.html', 'title': 'N-187', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-623.html', 'title': 'N-623', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'title': 'N-30', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'title': 'N-256', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-954.html', 'title': 'N-954', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-364.html', 'title': 'N-364', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-389.html', 'title': 'N-389', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-390.html', 'title': 'N-390', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-862.html', 'title': 'N-862', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 1.0}]
result = search.search('blueberry lime pear kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #113 checking search results for 'blueberry lime pear kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #113 checking search results for 'blueberry lime pear kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking search results for 'pear lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.019308841884856914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014577632708795894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008527199543906853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008335388262253253}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007698675289623947}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007405078808162829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006875859926650469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006520999978127136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005223070101355963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.005159575024279354}]
result = search.search('pear lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #114 checking search results for 'pear lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #114 checking search results for 'pear lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking search results for 'pear lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'title': 'N-53', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'title': 'N-59', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html', 'title': 'N-638', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-666.html', 'title': 'N-666', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-26.html', 'title': 'N-26', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-41.html', 'title': 'N-41', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'title': 'N-44', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'title': 'N-256', 'score': 1.0000000000000002}]
result = search.search('pear lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #115 checking search results for 'pear lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #115 checking search results for 'pear lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking search results for 'tomato banana blueberry pear fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01431118149992946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.013754150266877674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00877360121416962}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008090175971097912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007384624503885362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007056694111470625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006842768862679625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006738742344121448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005254786949319094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.005150626477125927}]
result = search.search('tomato banana blueberry pear fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #116 checking search results for 'tomato banana blueberry pear fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #116 checking search results for 'tomato banana blueberry pear fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking search results for 'tomato banana blueberry pear fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'title': 'N-169', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-823.html', 'title': 'N-823', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-538.html', 'title': 'N-538', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-959.html', 'title': 'N-959', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-720.html', 'title': 'N-720', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-685.html', 'title': 'N-685', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html', 'title': 'N-832', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-143.html', 'title': 'N-143', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html', 'title': 'N-717', 'score': 1.0}]
result = search.search('tomato banana blueberry pear fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #117 checking search results for 'tomato banana blueberry pear fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #117 checking search results for 'tomato banana blueberry pear fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking search results for 'kiwi apple papaya pear apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014190778603692758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.012336388770159603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008827534612961194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008742800657997353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007245459631011072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007234939280366845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006371892631680886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005492227188703076}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005434414968883645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005045311323615331}]
result = search.search('kiwi apple papaya pear apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #118 checking search results for 'kiwi apple papaya pear apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #118 checking search results for 'kiwi apple papaya pear apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking search results for 'kiwi apple papaya pear apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-364.html', 'title': 'N-364', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-484.html', 'title': 'N-484', 'score': 0.9987270821284813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html', 'title': 'N-234', 'score': 0.9980099578529256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-836.html', 'title': 'N-836', 'score': 0.9973039440496743}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html', 'title': 'N-208', 'score': 0.9971092170472964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-518.html', 'title': 'N-518', 'score': 0.9965682085836367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.9965539733650107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-124.html', 'title': 'N-124', 'score': 0.9962802113229314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-841.html', 'title': 'N-841', 'score': 0.9946925022424138}]
result = search.search('kiwi apple papaya pear apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #119 checking search results for 'kiwi apple papaya pear apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #119 checking search results for 'kiwi apple papaya pear apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking search results for 'papaya tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01950291001893492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013722327645816877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.00863563464718943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008516815162314109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007529418159555791}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007287949833811631}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006349982921113972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006027552336974922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005864815267294833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005116244614533907}]
result = search.search('papaya tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #120 checking search results for 'papaya tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #120 checking search results for 'papaya tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking search results for 'papaya tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'title': 'N-59', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-239.html', 'title': 'N-239', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-437.html', 'title': 'N-437', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-767.html', 'title': 'N-767', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-843.html', 'title': 'N-843', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-921.html', 'title': 'N-921', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-124.html', 'title': 'N-124', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'title': 'N-256', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html', 'title': 'N-754', 'score': 1.0000000000000002}]
result = search.search('papaya tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #121 checking search results for 'papaya tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #121 checking search results for 'papaya tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking search results for 'lime peach orange fig cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01776853963926059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013498455652136514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008629100787874973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.0081246702369603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007545002339725034}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007354385707670935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006889066842977117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006309020164197769}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.0058771521966019735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.0051584797234902995}]
result = search.search('lime peach orange fig cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #122 checking search results for 'lime peach orange fig cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #122 checking search results for 'lime peach orange fig cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking search results for 'lime peach orange fig cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-267.html', 'title': 'N-267', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-805.html', 'title': 'N-805', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html', 'title': 'N-296', 'score': 0.9988743982658277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html', 'title': 'N-968', 'score': 0.9985900126336013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html', 'title': 'N-332', 'score': 0.9983806785602304}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-860.html', 'title': 'N-860', 'score': 0.9980413049944539}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html', 'title': 'N-226', 'score': 0.9973965297945421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-383.html', 'title': 'N-383', 'score': 0.9971486093463678}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-414.html', 'title': 'N-414', 'score': 0.995807781096553}]
result = search.search('lime peach orange fig cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #123 checking search results for 'lime peach orange fig cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #123 checking search results for 'lime peach orange fig cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking search results for 'lime tomato papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013318916765634512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008843082449883466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.0076688926416835996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.0069827770000694565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006680428515982417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006615252080546574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005575127875808561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005474494487476343}]
result = search.search('lime tomato papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #124 checking search results for 'lime tomato papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #124 checking search results for 'lime tomato papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking search results for 'lime tomato papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'title': 'N-59', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-26.html', 'title': 'N-26', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-493.html', 'title': 'N-493', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-176.html', 'title': 'N-176', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-427.html', 'title': 'N-427', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-214.html', 'title': 'N-214', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-918.html', 'title': 'N-918', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-734.html', 'title': 'N-734', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-302.html', 'title': 'N-302', 'score': 1.0000000000000002}]
result = search.search('lime tomato papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #125 checking search results for 'lime tomato papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #125 checking search results for 'lime tomato papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking search results for 'pear banana apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014378133294206931}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009048955075399512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008260433331442142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007706964977199231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007344036653464012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006879055256465818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006722951857535215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.0052566696958165175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005057348431481428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.00505682671800126}]
result = search.search('pear banana apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #126 checking search results for 'pear banana apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #126 checking search results for 'pear banana apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking search results for 'pear banana apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'title': 'N-169', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-820.html', 'title': 'N-820', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html', 'title': 'N-209', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-887.html', 'title': 'N-887', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-596.html', 'title': 'N-596', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-955.html', 'title': 'N-955', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-962.html', 'title': 'N-962', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-738.html', 'title': 'N-738', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-514.html', 'title': 'N-514', 'score': 1.0000000000000002}]
result = search.search('pear banana apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #127 checking search results for 'pear banana apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #127 checking search results for 'pear banana apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking search results for 'fig lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013757205549599109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00921301020119066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008843082449883468}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.0076688926416836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007480347135816114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006903083906890486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0068794343821956365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.0058906054096750345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('fig lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #128 checking search results for 'fig lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #128 checking search results for 'fig lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking search results for 'fig lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'title': 'N-53', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-85.html', 'title': 'N-85', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-114.html', 'title': 'N-114', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-34.html', 'title': 'N-34', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-185.html', 'title': 'N-185', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html', 'title': 'N-308', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-405.html', 'title': 'N-405', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-859.html', 'title': 'N-859', 'score': 1.0000000000000002}]
result = search.search('fig lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #129 checking search results for 'fig lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #129 checking search results for 'fig lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking search results for 'lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}]
result = search.search('lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #130 checking search results for 'lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #130 checking search results for 'lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking search results for 'lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}]
result = search.search('lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #131 checking search results for 'lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #131 checking search results for 'lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking search results for 'apple fig papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.023140789912233686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01406567624411286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008767395436564674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008080941519788729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007240735015612389}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007153798228481743}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006774706479657236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.0057814455170319135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005183313826932791}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005007445585389665}]
result = search.search('apple fig papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #132 checking search results for 'apple fig papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #132 checking search results for 'apple fig papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking search results for 'apple fig papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-572.html', 'title': 'N-572', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html', 'title': 'N-754', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'title': 'N-76', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-876.html', 'title': 'N-876', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-73.html', 'title': 'N-73', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-855.html', 'title': 'N-855', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-568.html', 'title': 'N-568', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-492.html', 'title': 'N-492', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-934.html', 'title': 'N-934', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-175.html', 'title': 'N-175', 'score': 1.0000000000000002}]
result = search.search('apple fig papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #133 checking search results for 'apple fig papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #133 checking search results for 'apple fig papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #134 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #134 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #135 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #135 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking search results for 'apple kiwi pear cherry orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013968921093887482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008594495377166535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008289144375347118}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007317782875046192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.00707339116601187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.0060911804269389485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006062380880686234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005766406970253722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005149819425879659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005058211994552593}]
result = search.search('apple kiwi pear cherry orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #136 checking search results for 'apple kiwi pear cherry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #136 checking search results for 'apple kiwi pear cherry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking search results for 'apple kiwi pear cherry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-885.html', 'title': 'N-885', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-740.html', 'title': 'N-740', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-464.html', 'title': 'N-464', 'score': 0.9985456823472735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-680.html', 'title': 'N-680', 'score': 0.9983647294575233}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html', 'title': 'N-226', 'score': 0.9982372156935331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html', 'title': 'N-717', 'score': 0.9975488283699284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html', 'title': 'N-760', 'score': 0.9972703957558545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html', 'title': 'N-334', 'score': 0.99670726367071}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-518.html', 'title': 'N-518', 'score': 0.9964590991266192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-931.html', 'title': 'N-931', 'score': 0.996184013604367}]
result = search.search('apple kiwi pear cherry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #137 checking search results for 'apple kiwi pear cherry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #137 checking search results for 'apple kiwi pear cherry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking search results for 'apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #138 checking search results for 'apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #138 checking search results for 'apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking search results for 'apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'title': 'N-53', 'score': 1.0}]
result = search.search('apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #139 checking search results for 'apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #139 checking search results for 'apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking search results for 'tomato banana fig coconut cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.014269661681457579}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01403590077522994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008522028259563925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008381803557158654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007272092665278805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007223300455954351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006405012498728588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.0060309439201478654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005945675230133869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.0053302664860460005}]
result = search.search('tomato banana fig coconut cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #140 checking search results for 'tomato banana fig coconut cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #140 checking search results for 'tomato banana fig coconut cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking search results for 'tomato banana fig coconut cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html', 'title': 'N-306', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-426.html', 'title': 'N-426', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html', 'title': 'N-308', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-113.html', 'title': 'N-113', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-646.html', 'title': 'N-646', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-558.html', 'title': 'N-558', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-348.html', 'title': 'N-348', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-685.html', 'title': 'N-685', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-354.html', 'title': 'N-354', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-266.html', 'title': 'N-266', 'score': 0.9986283827994271}]
result = search.search('tomato banana fig coconut cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #141 checking search results for 'tomato banana fig coconut cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #141 checking search results for 'tomato banana fig coconut cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #142 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #142 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #143 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #143 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking search results for 'pear banana coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014435748497953328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008201162948354483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008173865212866461}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.0073545922823419095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.00695703811098768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006807589566353047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005886967708053723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005385112867054458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005320894132312285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005057894580276697}]
result = search.search('pear banana coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #144 checking search results for 'pear banana coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #144 checking search results for 'pear banana coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking search results for 'pear banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-168.html', 'title': 'N-168', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-735.html', 'title': 'N-735', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-343.html', 'title': 'N-343', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-814.html', 'title': 'N-814', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-685.html', 'title': 'N-685', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html', 'title': 'N-235', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-774.html', 'title': 'N-774', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html', 'title': 'N-209', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-217.html', 'title': 'N-217', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-177.html', 'title': 'N-177', 'score': 1.0}]
result = search.search('pear banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #145 checking search results for 'pear banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #145 checking search results for 'pear banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking search results for 'pear banana blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014474079327624012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008948388941600618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008094638587247977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007333296469800969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006918392112900344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006888705123211101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006659170940013657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005187678277023559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.005162014830565029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005078563839536835}]
result = search.search('pear banana blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #146 checking search results for 'pear banana blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #146 checking search results for 'pear banana blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking search results for 'pear banana blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'title': 'N-169', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-823.html', 'title': 'N-823', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-887.html', 'title': 'N-887', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-367.html', 'title': 'N-367', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html', 'title': 'N-986', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html', 'title': 'N-263', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-538.html', 'title': 'N-538', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-892.html', 'title': 'N-892', 'score': 1.0000000000000002}]
result = search.search('pear banana blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #147 checking search results for 'pear banana blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #147 checking search results for 'pear banana blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking search results for 'papaya fig apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.022335859703798786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013600673026260123}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008761699703447564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00872003385903541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007516969052558944}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.0072645334120516256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006496782629194684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006174470399647394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005739246030950094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005312262087037083}]
result = search.search('papaya fig apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #148 checking search results for 'papaya fig apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #148 checking search results for 'papaya fig apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking search results for 'papaya fig apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-250.html', 'title': 'N-250', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-73.html', 'title': 'N-73', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-267.html', 'title': 'N-267', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-469.html', 'title': 'N-469', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-529.html', 'title': 'N-529', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html', 'title': 'N-638', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html', 'title': 'N-235', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html', 'title': 'N-754', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html', 'title': 'N-346', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-582.html', 'title': 'N-582', 'score': 1.0}]
result = search.search('papaya fig apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #149 checking search results for 'papaya fig apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #149 checking search results for 'papaya fig apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking search results for 'banana tomato apricot tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014369705679729002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009049271370264053}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008315192239450462}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007699156474972097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.00716145346728636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006991737511071455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006681761564166175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005949780827334881}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005240209718032615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.0050685538944989575}]
result = search.search('banana tomato apricot tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #150 checking search results for 'banana tomato apricot tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #150 checking search results for 'banana tomato apricot tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking search results for 'banana tomato apricot tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-212.html', 'title': 'N-212', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'title': 'N-169', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html', 'title': 'N-278', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html', 'title': 'N-528', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-105.html', 'title': 'N-105', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html', 'title': 'N-351', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-460.html', 'title': 'N-460', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-99.html', 'title': 'N-99', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-887.html', 'title': 'N-887', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-57.html', 'title': 'N-57', 'score': 1.0}]
result = search.search('banana tomato apricot tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #151 checking search results for 'banana tomato apricot tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #151 checking search results for 'banana tomato apricot tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #152 checking search results for 'cherry coconut apricot papaya lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.017622382606655693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013690015486765609}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008620572145163903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008152997842147723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.0072144036255768484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007190157786563335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006140783531864627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005797207696113914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005540798664632619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005387663388185243}]
result = search.search('cherry coconut apricot papaya lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #152 checking search results for 'cherry coconut apricot papaya lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #152 checking search results for 'cherry coconut apricot papaya lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #153 checking search results for 'cherry coconut apricot papaya lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'title': 'N-90', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.9965584096748993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-937.html', 'title': 'N-937', 'score': 0.9962098780248352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-952.html', 'title': 'N-952', 'score': 0.9961354373322822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-852.html', 'title': 'N-852', 'score': 0.9949986771085472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-493.html', 'title': 'N-493', 'score': 0.9949462297319309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-670.html', 'title': 'N-670', 'score': 0.9946122867957163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html', 'title': 'N-648', 'score': 0.9945577142083002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-888.html', 'title': 'N-888', 'score': 0.9943149018043909}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-924.html', 'title': 'N-924', 'score': 0.9934924447288389}]
result = search.search('cherry coconut apricot papaya lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #153 checking search results for 'cherry coconut apricot papaya lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #153 checking search results for 'cherry coconut apricot papaya lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking search results for 'apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #154 checking search results for 'apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #154 checking search results for 'apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking search results for 'apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'title': 'N-53', 'score': 1.0}]
result = search.search('apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #155 checking search results for 'apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #155 checking search results for 'apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking search results for 'papaya peach papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.024373878514282483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.011815599712714207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.007993166369696754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00723429394217539}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.0071103080814621565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079187909695656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.0068793529919002954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.00617197842874469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.005990478732544069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005433040785653924}]
result = search.search('papaya peach papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #156 checking search results for 'papaya peach papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #156 checking search results for 'papaya peach papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking search results for 'papaya peach papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-181.html', 'title': 'N-181', 'score': 0.9999958888412631}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 0.9999941188498764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html', 'title': 'N-371', 'score': 0.9999938667820097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html', 'title': 'N-322', 'score': 0.9999933976769397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-339.html', 'title': 'N-339', 'score': 0.9999933976769397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.999991691148895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-677.html', 'title': 'N-677', 'score': 0.9999902017265238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html', 'title': 'N-963', 'score': 0.9999884339792378}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-216.html', 'title': 'N-216', 'score': 0.9999877799081285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-223.html', 'title': 'N-223', 'score': 0.9999721343902191}]
result = search.search('papaya peach papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #157 checking search results for 'papaya peach papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #157 checking search results for 'papaya peach papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking search results for 'blueberry lime cherry papaya papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.02207183475652919}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.012030057271061252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008324186152298362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.007410267219345531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007227484878080565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006935276573510616}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006662434836313718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006101324917090704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005328388472882429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.00526518049327747}]
result = search.search('blueberry lime cherry papaya papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #158 checking search results for 'blueberry lime cherry papaya papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #158 checking search results for 'blueberry lime cherry papaya papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking search results for 'blueberry lime cherry papaya papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-862.html', 'title': 'N-862', 'score': 0.9998522715240861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html', 'title': 'N-200', 'score': 0.999673214315739}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html', 'title': 'N-923', 'score': 0.9996338538756044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html', 'title': 'N-332', 'score': 0.9985059449037319}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-835.html', 'title': 'N-835', 'score': 0.9973229395193316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-276.html', 'title': 'N-276', 'score': 0.9964811864147719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-286.html', 'title': 'N-286', 'score': 0.9934673499814503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html', 'title': 'N-371', 'score': 0.9930328730050315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-672.html', 'title': 'N-672', 'score': 0.9922723941449313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html', 'title': 'N-562', 'score': 0.9920736774233703}]
result = search.search('blueberry lime cherry papaya papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #159 checking search results for 'blueberry lime cherry papaya papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #159 checking search results for 'blueberry lime cherry papaya papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking search results for 'lime kiwi kiwi apricot peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013535664611120244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.010545692443849959}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008727937625679812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008604941677083531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007288238777510423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007216782293608962}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006596132432144143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.00650480169232681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.0060393217796718855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.004902422835404189}]
result = search.search('lime kiwi kiwi apricot peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #160 checking search results for 'lime kiwi kiwi apricot peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #160 checking search results for 'lime kiwi kiwi apricot peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking search results for 'lime kiwi kiwi apricot peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html', 'title': 'N-562', 'score': 0.999697734637197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-191.html', 'title': 'N-191', 'score': 0.9996033222132166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-91.html', 'title': 'N-91', 'score': 0.999538565777845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-945.html', 'title': 'N-945', 'score': 0.999538565777845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-230.html', 'title': 'N-230', 'score': 0.9978700605628232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-427.html', 'title': 'N-427', 'score': 0.9967136509048408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-604.html', 'title': 'N-604', 'score': 0.9952434369128634}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-257.html', 'title': 'N-257', 'score': 0.9941476919559175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-369.html', 'title': 'N-369', 'score': 0.9938553390361463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html', 'title': 'N-92', 'score': 0.9935804031804732}]
result = search.search('lime kiwi kiwi apricot peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #161 checking search results for 'lime kiwi kiwi apricot peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #161 checking search results for 'lime kiwi kiwi apricot peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking search results for 'papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}]
result = search.search('papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #162 checking search results for 'papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #162 checking search results for 'papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking search results for 'papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}]
result = search.search('papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #163 checking search results for 'papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #163 checking search results for 'papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking search results for 'papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}]
result = search.search('papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #164 checking search results for 'papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #164 checking search results for 'papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking search results for 'papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}]
result = search.search('papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #165 checking search results for 'papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #165 checking search results for 'papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking search results for 'cherry cherry kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.012234840567873878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.00709187182496879}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.006961490259305909}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006806481197246196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.006522244660752102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006474714810723054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.0059536089305658076}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005383269346412227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005177697204596243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005086895309746825}]
result = search.search('cherry cherry kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #166 checking search results for 'cherry cherry kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #166 checking search results for 'cherry cherry kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #167 checking search results for 'cherry cherry kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-954.html', 'title': 'N-954', 'score': 0.9999816018665468}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-492.html', 'title': 'N-492', 'score': 0.9999714623867298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-964.html', 'title': 'N-964', 'score': 0.9999047377115888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-924.html', 'title': 'N-924', 'score': 0.9999047377115888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-674.html', 'title': 'N-674', 'score': 0.9998989756151804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-487.html', 'title': 'N-487', 'score': 0.999871278088663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-551.html', 'title': 'N-551', 'score': 0.9998595097646541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-972.html', 'title': 'N-972', 'score': 0.9997686520621253}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-947.html', 'title': 'N-947', 'score': 0.9996492547457432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-207.html', 'title': 'N-207', 'score': 0.9996164568519703}]
result = search.search('cherry cherry kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #167 checking search results for 'cherry cherry kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #167 checking search results for 'cherry cherry kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking search results for 'fig banana apricot banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013030566919529548}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.012091377728357923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008516910907621038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.0072652045041170865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.007140402114258573}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006986366421839534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006524770122665614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006454446384955102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.00594821314338537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.0045914059130915605}]
result = search.search('fig banana apricot banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #168 checking search results for 'fig banana apricot banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #168 checking search results for 'fig banana apricot banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking search results for 'fig banana apricot banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html', 'title': 'N-474', 'score': 0.9999152164872351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-837.html', 'title': 'N-837', 'score': 0.9998665165604123}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html', 'title': 'N-923', 'score': 0.9997379996591474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-325.html', 'title': 'N-325', 'score': 0.9996875532446011}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-481.html', 'title': 'N-481', 'score': 0.9996241075253274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-512.html', 'title': 'N-512', 'score': 0.9996209744170608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-267.html', 'title': 'N-267', 'score': 0.9995305578665713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-447.html', 'title': 'N-447', 'score': 0.9994598205856781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html', 'title': 'N-346', 'score': 0.9994475285301452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 0.9994245076989585}]
result = search.search('fig banana apricot banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #169 checking search results for 'fig banana apricot banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #169 checking search results for 'fig banana apricot banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #170 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #170 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #171 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #171 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking search results for 'coconut lime fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.02285180299447972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014047197284889188}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008886144075320184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008759301296442664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.0073408563260076495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007061360326101843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006909685634462767}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005672127013113561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005502235118111835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.00518133424156731}]
result = search.search('coconut lime fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #172 checking search results for 'coconut lime fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #172 checking search results for 'coconut lime fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking search results for 'coconut lime fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-547.html', 'title': 'N-547', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-354.html', 'title': 'N-354', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-61.html', 'title': 'N-61', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-114.html', 'title': 'N-114', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html', 'title': 'N-308', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-113.html', 'title': 'N-113', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html', 'title': 'N-306', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html', 'title': 'N-368', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-217.html', 'title': 'N-217', 'score': 1.0}]
result = search.search('coconut lime fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #173 checking search results for 'coconut lime fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #173 checking search results for 'coconut lime fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking search results for 'coconut blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.01462057710776871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008626494477363265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008333234755220296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.00737513551193414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007057849308340884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006902477826467551}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005462480997813795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005196557021211873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.0048451370470433}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.0048137366806068295}]
result = search.search('coconut blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #174 checking search results for 'coconut blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #174 checking search results for 'coconut blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking search results for 'coconut blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'title': 'N-407', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'title': 'N-44', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-72.html', 'title': 'N-72', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-150.html', 'title': 'N-150', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-196.html', 'title': 'N-196', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-651.html', 'title': 'N-651', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html', 'title': 'N-966', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-438.html', 'title': 'N-438', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html', 'title': 'N-260', 'score': 1.0000000000000002}]
result = search.search('coconut blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #175 checking search results for 'coconut blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #175 checking search results for 'coconut blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking search results for 'kiwi tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'title': 'N-4', 'score': 0.005372748134323713}]
result = search.search('kiwi tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #176 checking search results for 'kiwi tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #176 checking search results for 'kiwi tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking search results for 'kiwi tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 1.0}]
result = search.search('kiwi tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #177 checking search results for 'kiwi tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #177 checking search results for 'kiwi tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking search results for 'banana pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014381957531693227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008963917013084568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.007873440747053477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007698675289623947}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007290037396642998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006875859926650469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006520999978127136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005739889487388331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.0054829215575220545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.005159575024279354}]
result = search.search('banana pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #178 checking search results for 'banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #178 checking search results for 'banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking search results for 'banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-207.html', 'title': 'N-207', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html', 'title': 'N-298', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'title': 'N-407', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'title': 'N-675', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'title': 'N-44', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-56.html', 'title': 'N-56', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-150.html', 'title': 'N-150', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'title': 'N-169', 'score': 1.0000000000000002}]
result = search.search('banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #179 checking search results for 'banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #179 checking search results for 'banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking search results for 'peach tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959661}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00921301020119066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008904284110532115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007698917378646352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007404620178416595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.00659603485468099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006337194041189021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005746968466638175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005208716022108618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005161326974356845}]
result = search.search('peach tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #180 checking search results for 'peach tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #180 checking search results for 'peach tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking search results for 'peach tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-572.html', 'title': 'N-572', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-34.html', 'title': 'N-34', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html', 'title': 'N-88', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'title': 'N-169', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html', 'title': 'N-973', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-820.html', 'title': 'N-820', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-97.html', 'title': 'N-97', 'score': 1.0000000000000002}]
result = search.search('peach tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #181 checking search results for 'peach tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #181 checking search results for 'peach tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking search results for 'pear banana blueberry orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014121447387904502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008773601214169618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008205822041280345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.0072114504393996255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007047990237148007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006603703308802904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006475401365785116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005195297091396875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'title': 'N-39', 'score': 0.005132330120103045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005064048857967905}]
result = search.search('pear banana blueberry orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #182 checking search results for 'pear banana blueberry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #182 checking search results for 'pear banana blueberry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking search results for 'pear banana blueberry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-367.html', 'title': 'N-367', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html', 'title': 'N-717', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html', 'title': 'N-986', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html', 'title': 'N-832', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-959.html', 'title': 'N-959', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-143.html', 'title': 'N-143', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-756.html', 'title': 'N-756', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-824.html', 'title': 'N-824', 'score': 0.9984070174013233}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html', 'title': 'N-600', 'score': 0.9981589664732643}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html', 'title': 'N-388', 'score': 0.9977835424869967}]
result = search.search('pear banana blueberry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #183 checking search results for 'pear banana blueberry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #183 checking search results for 'pear banana blueberry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking search results for 'peach orange apricot apple peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013815991723906905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008632472123495064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008590942003280491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007143500176218247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006960632285494054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.006335064914734281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006216654064967504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005508788490424796}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005054351952091581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.004887450564948624}]
result = search.search('peach orange apricot apple peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #184 checking search results for 'peach orange apricot apple peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #184 checking search results for 'peach orange apricot apple peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking search results for 'peach orange apricot apple peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-173.html', 'title': 'N-173', 'score': 0.9997445164792221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-532.html', 'title': 'N-532', 'score': 0.9996934174834754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 0.999631290735728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-971.html', 'title': 'N-971', 'score': 0.999631290735728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html', 'title': 'N-488', 'score': 0.9995823424537761}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-758.html', 'title': 'N-758', 'score': 0.9993247148827523}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-671.html', 'title': 'N-671', 'score': 0.9979343518911077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-160.html', 'title': 'N-160', 'score': 0.9974728040155894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-723.html', 'title': 'N-723', 'score': 0.9973861594026658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-914.html', 'title': 'N-914', 'score': 0.9965427693680657}]
result = search.search('peach orange apricot apple peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #185 checking search results for 'peach orange apricot apple peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #185 checking search results for 'peach orange apricot apple peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking search results for 'lime lime lime apple orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.02437881870082356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014189860604053344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007650751984992546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.006840818765060017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006624369150117568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.006345069653021318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005861476443736988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005437369647230715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.0051274994747863714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.00477361301410292}]
result = search.search('lime lime lime apple orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #186 checking search results for 'lime lime lime apple orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #186 checking search results for 'lime lime lime apple orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking search results for 'lime lime lime apple orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html', 'title': 'N-754', 'score': 0.9996663463956105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-294.html', 'title': 'N-294', 'score': 0.9996364249121995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-971.html', 'title': 'N-971', 'score': 0.999161121823608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-884.html', 'title': 'N-884', 'score': 0.9990164223763496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-740.html', 'title': 'N-740', 'score': 0.9989863225409432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-664.html', 'title': 'N-664', 'score': 0.9988992928437155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html', 'title': 'N-111', 'score': 0.9987115511641124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-34.html', 'title': 'N-34', 'score': 0.9986745640718909}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-921.html', 'title': 'N-921', 'score': 0.9982978370399991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-422.html', 'title': 'N-422', 'score': 0.9976518151236708}]
result = search.search('lime lime lime apple orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #187 checking search results for 'lime lime lime apple orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #187 checking search results for 'lime lime lime apple orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking search results for 'orange lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.01940485085997773}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013318916765634514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00921301020119066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008677191542395815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007485676688763367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.00736196389525052}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007052948872038279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006615252080546574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.00557512787580856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005182060518420735}]
result = search.search('orange lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #188 checking search results for 'orange lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #188 checking search results for 'orange lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking search results for 'orange lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'title': 'N-59', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html', 'title': 'N-80', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'title': 'N-90', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-121.html', 'title': 'N-121', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-135.html', 'title': 'N-135', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-151.html', 'title': 'N-151', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-218.html', 'title': 'N-218', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-297.html', 'title': 'N-297', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-387.html', 'title': 'N-387', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html', 'title': 'N-528', 'score': 1.0000000000000002}]
result = search.search('orange lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #189 checking search results for 'orange lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #189 checking search results for 'orange lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking search results for 'lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.027715789659140615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014643860655959658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.009213010201190659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008928095854558027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007741171716967465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007500758212344802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007079246730102673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006942686950637583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006192196133748252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005482921557522054}]
result = search.search('lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #190 checking search results for 'lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #190 checking search results for 'lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking search results for 'lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'title': 'N-14', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'title': 'N-23', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0}]
result = search.search('lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #191 checking search results for 'lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #191 checking search results for 'lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking search results for 'kiwi banana cherry lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013891219071111375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.013780141973096939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.00847899942070671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.007769700032884008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007697077161090446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007129267681876506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007039157481510876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.0064353982298023475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.005830117664081032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005155455193231744}]
result = search.search('kiwi banana cherry lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #192 checking search results for 'kiwi banana cherry lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #192 checking search results for 'kiwi banana cherry lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking search results for 'kiwi banana cherry lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-413.html', 'title': 'N-413', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-623.html', 'title': 'N-623', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-436.html', 'title': 'N-436', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-810.html', 'title': 'N-810', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-354.html', 'title': 'N-354', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html', 'title': 'N-308', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html', 'title': 'N-306', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-705.html', 'title': 'N-705', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html', 'title': 'N-296', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-180.html', 'title': 'N-180', 'score': 0.9983689028065026}]
result = search.search('kiwi banana cherry lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #193 checking search results for 'kiwi banana cherry lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #193 checking search results for 'kiwi banana cherry lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking search results for 'apple blueberry lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.015931640943902474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014482939389771701}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008432866140951118}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008300478728261292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007448576890495017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006914212058075205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.00645237943958866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.005758888167962824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005137981048331398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.004968917864192657}]
result = search.search('apple blueberry lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #194 checking search results for 'apple blueberry lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #194 checking search results for 'apple blueberry lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking search results for 'apple blueberry lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-955.html', 'title': 'N-955', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-651.html', 'title': 'N-651', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html', 'title': 'N-96', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-859.html', 'title': 'N-859', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-978.html', 'title': 'N-978', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html', 'title': 'N-164', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-799.html', 'title': 'N-799', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-432.html', 'title': 'N-432', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-187.html', 'title': 'N-187', 'score': 1.0}]
result = search.search('apple blueberry lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #195 checking search results for 'apple blueberry lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #195 checking search results for 'apple blueberry lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking search results for 'cherry apple blueberry apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014126864486354715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.00847167241583376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008316752781335222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007192609925789994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.006889088133954565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.00619434309280368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.00581510298711705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005193570731243062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005090061328667073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.004947352080817345}]
result = search.search('cherry apple blueberry apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #196 checking search results for 'cherry apple blueberry apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #196 checking search results for 'cherry apple blueberry apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking search results for 'cherry apple blueberry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-364.html', 'title': 'N-364', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-356.html', 'title': 'N-356', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-571.html', 'title': 'N-571', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-840.html', 'title': 'N-840', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html', 'title': 'N-200', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-685.html', 'title': 'N-685', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html', 'title': 'N-101', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-714.html', 'title': 'N-714', 'score': 0.9987924223497705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-622.html', 'title': 'N-622', 'score': 0.9987402487052205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-667.html', 'title': 'N-667', 'score': 0.9986935439146144}]
result = search.search('cherry apple blueberry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #197 checking search results for 'cherry apple blueberry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #197 checking search results for 'cherry apple blueberry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking search results for 'cherry tomato tomato blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.013975587608642774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.008350186148847688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008110232231998544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.007594846358933276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.007065104409528041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.007011160176183812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006063707002572326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.0054829215575220545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'title': 'N-60', 'score': 0.005137378631206669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005029248487485744}]
result = search.search('cherry tomato tomato blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #198 checking search results for 'cherry tomato tomato blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #198 checking search results for 'cherry tomato tomato blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking search results for 'cherry tomato tomato blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html', 'title': 'N-80', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html', 'title': 'N-87', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html', 'title': 'N-327', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-767.html', 'title': 'N-767', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-34.html', 'title': 'N-34', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'title': 'N-169', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html', 'title': 'N-633', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html', 'title': 'N-966', 'score': 1.0000000000000002}]
result = search.search('cherry tomato tomato blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #199 checking search results for 'cherry tomato tomato blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #199 checking search results for 'cherry tomato tomato blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
