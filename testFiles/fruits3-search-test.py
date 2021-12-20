
import testingtools
import crawler
import searchdata
import search

output = open('fruits3-search-failed.txt', 'w')
success_output = open('fruits3-search-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html')



#Test #0 checking search results for 'fig blueberry fig peach fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015138806859308056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012066522653626479}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.01010824395006799}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009997407254974574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009834221550614981}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.008824810340516208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.0073062932199098535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0059429462883809035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005665096863924677}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005597019167804524}]
result = search.search('fig blueberry fig peach fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #0 checking search results for 'fig blueberry fig peach fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #0 checking search results for 'fig blueberry fig peach fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking search results for 'fig blueberry fig peach fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-361.html', 'title': 'N-361', 'score': 0.9999978159315711}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-427.html', 'title': 'N-427', 'score': 0.9997165404885272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html', 'title': 'N-118', 'score': 0.9996929935780049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 0.9992559975266563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-792.html', 'title': 'N-792', 'score': 0.9991105101740878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-496.html', 'title': 'N-496', 'score': 0.998966962845068}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-15.html', 'title': 'N-15', 'score': 0.9989459726442026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-708.html', 'title': 'N-708', 'score': 0.9972854118290478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-783.html', 'title': 'N-783', 'score': 0.9959130346298051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-149.html', 'title': 'N-149', 'score': 0.9959084942659155}]
result = search.search('fig blueberry fig peach fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #1 checking search results for 'fig blueberry fig peach fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #1 checking search results for 'fig blueberry fig peach fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking search results for 'kiwi apricot banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01506369093556744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014901935390353716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.011503365829538712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010153074477345274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00788911910801382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0073578658161224915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.0065371360930786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005803349533079964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005700566778127513}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005565882157284923}]
result = search.search('kiwi apricot banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #2 checking search results for 'kiwi apricot banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #2 checking search results for 'kiwi apricot banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking search results for 'kiwi apricot banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-140.html', 'title': 'N-140', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-232.html', 'title': 'N-232', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html', 'title': 'N-555', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-242.html', 'title': 'N-242', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-749.html', 'title': 'N-749', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-677.html', 'title': 'N-677', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-771.html', 'title': 'N-771', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-954.html', 'title': 'N-954', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-312.html', 'title': 'N-312', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-670.html', 'title': 'N-670', 'score': 1.0000000000000002}]
result = search.search('kiwi apricot banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #3 checking search results for 'kiwi apricot banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #3 checking search results for 'kiwi apricot banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking search results for 'pear apricot banana kiwi tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.016367698804881425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015140321441683506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01203837526027441}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010306159680933893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.007957005366631034}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007429658752255588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.0060635356733800185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0059052929921225355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.005542099237965578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.005342240420072043}]
result = search.search('pear apricot banana kiwi tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #4 checking search results for 'pear apricot banana kiwi tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #4 checking search results for 'pear apricot banana kiwi tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking search results for 'pear apricot banana kiwi tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'title': 'N-59', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-984.html', 'title': 'N-984', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-577.html', 'title': 'N-577', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-771.html', 'title': 'N-771', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-276.html', 'title': 'N-276', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-954.html', 'title': 'N-954', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-676.html', 'title': 'N-676', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-758.html', 'title': 'N-758', 'score': 0.9987812613713154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9984242650043698}]
result = search.search('pear apricot banana kiwi tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #5 checking search results for 'pear apricot banana kiwi tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #5 checking search results for 'pear apricot banana kiwi tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking search results for 'apple pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.018303859559624765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015229810258370929}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013017724624730125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.01061983189264421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008918858841454583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0076497554510821}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006284421971449276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0057530354875322265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.0056512083649736845}]
result = search.search('apple pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #6 checking search results for 'apple pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #6 checking search results for 'apple pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking search results for 'apple pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-838.html', 'title': 'N-838', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'title': 'N-34', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-38.html', 'title': 'N-38', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-651.html', 'title': 'N-651', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-261.html', 'title': 'N-261', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html', 'title': 'N-286', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-232.html', 'title': 'N-232', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-202.html', 'title': 'N-202', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 1.0000000000000002}]
result = search.search('apple pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #7 checking search results for 'apple pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #7 checking search results for 'apple pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #8 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #8 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #9 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #9 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking search results for 'blueberry apricot lime pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.019398253539779607}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015612594529602288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01240957718251154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010588612071250267}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009027777233615912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007148244420686361}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.00685019237357385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005710841259826231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005687013793303019}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.00532676598727335}]
result = search.search('blueberry apricot lime pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #10 checking search results for 'blueberry apricot lime pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #10 checking search results for 'blueberry apricot lime pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking search results for 'blueberry apricot lime pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-326.html', 'title': 'N-326', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-359.html', 'title': 'N-359', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-648.html', 'title': 'N-648', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-300.html', 'title': 'N-300', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html', 'title': 'N-793', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-802.html', 'title': 'N-802', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html', 'title': 'N-257', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-256.html', 'title': 'N-256', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-868.html', 'title': 'N-868', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-294.html', 'title': 'N-294', 'score': 1.0}]
result = search.search('blueberry apricot lime pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #11 checking search results for 'blueberry apricot lime pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #11 checking search results for 'blueberry apricot lime pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking search results for 'lime pear coconut fig coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013707085441782986}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012475525084694445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.011705675172466639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010255798272528203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008938997653565957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008819477898664739}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007652277552021876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007394058068978145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005975909618638494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.00558475523383981}]
result = search.search('lime pear coconut fig coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #12 checking search results for 'lime pear coconut fig coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #12 checking search results for 'lime pear coconut fig coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking search results for 'lime pear coconut fig coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-336.html', 'title': 'N-336', 'score': 0.9998054901890818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-466.html', 'title': 'N-466', 'score': 0.9996610161131443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html', 'title': 'N-257', 'score': 0.9996509262900638}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-827.html', 'title': 'N-827', 'score': 0.9968080836318258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-377.html', 'title': 'N-377', 'score': 0.996415830210211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html', 'title': 'N-113', 'score': 0.9956388017935556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-281.html', 'title': 'N-281', 'score': 0.9950638470669587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-577.html', 'title': 'N-577', 'score': 0.9950548273034292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-884.html', 'title': 'N-884', 'score': 0.9950043951855245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-706.html', 'title': 'N-706', 'score': 0.9948193033231563}]
result = search.search('lime pear coconut fig coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #13 checking search results for 'lime pear coconut fig coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #13 checking search results for 'lime pear coconut fig coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking search results for 'peach apricot cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.019233292783822888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013941440488749372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013247284375684109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010089849480074216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00814626942536979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006706801158950476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.006560555821779724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006073737636224273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005835455844384757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005586031987247188}]
result = search.search('peach apricot cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #14 checking search results for 'peach apricot cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #14 checking search results for 'peach apricot cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking search results for 'peach apricot cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-309.html', 'title': 'N-309', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-925.html', 'title': 'N-925', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-454.html', 'title': 'N-454', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-895.html', 'title': 'N-895', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-586.html', 'title': 'N-586', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-340.html', 'title': 'N-340', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-526.html', 'title': 'N-526', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-572.html', 'title': 'N-572', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-107.html', 'title': 'N-107', 'score': 1.0}]
result = search.search('peach apricot cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #15 checking search results for 'peach apricot cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #15 checking search results for 'peach apricot cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking search results for 'banana peach cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01666292020031221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013769985363866918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012702398670605576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010075112867369703}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00767902982277696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007069484722189206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.006672344775152754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006585125168527642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006497275521795426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005672427730973626}]
result = search.search('banana peach cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #16 checking search results for 'banana peach cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #16 checking search results for 'banana peach cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking search results for 'banana peach cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-68.html', 'title': 'N-68', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-107.html', 'title': 'N-107', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-782.html', 'title': 'N-782', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html', 'title': 'N-598', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html', 'title': 'N-266', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-359.html', 'title': 'N-359', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html', 'title': 'N-911', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-165.html', 'title': 'N-165', 'score': 1.0000000000000002}]
result = search.search('banana peach cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #17 checking search results for 'banana peach cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #17 checking search results for 'banana peach cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking search results for 'orange papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.017448311225900983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01528994692121991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013169891782532802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.01021107794833601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009446032025500206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007950149247534552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.00743438270370637}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006934720814305263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006517318173817127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006398796598396929}]
result = search.search('orange papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #18 checking search results for 'orange papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #18 checking search results for 'orange papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking search results for 'orange papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-223.html', 'title': 'N-223', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-432.html', 'title': 'N-432', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-443.html', 'title': 'N-443', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'title': 'N-34', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html', 'title': 'N-842', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html', 'title': 'N-404', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-918.html', 'title': 'N-918', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-981.html', 'title': 'N-981', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html', 'title': 'N-736', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html', 'title': 'N-687', 'score': 1.0000000000000002}]
result = search.search('orange papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #19 checking search results for 'orange papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #19 checking search results for 'orange papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005672427730973626}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #20 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #20 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #21 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #21 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking search results for 'orange kiwi kiwi papaya tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.0192002086654518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015535175216224146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010510962924852494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.010327626122054486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.010208211848884187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009715709248957878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006976649819829168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006696419870097975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006395735074586474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006126281385119239}]
result = search.search('orange kiwi kiwi papaya tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #22 checking search results for 'orange kiwi kiwi papaya tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #22 checking search results for 'orange kiwi kiwi papaya tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking search results for 'orange kiwi kiwi papaya tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-826.html', 'title': 'N-826', 'score': 0.9997542356906833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-520.html', 'title': 'N-520', 'score': 0.9997542356906833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-490.html', 'title': 'N-490', 'score': 0.9997411843866063}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-306.html', 'title': 'N-306', 'score': 0.9997052676756358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-799.html', 'title': 'N-799', 'score': 0.9997052676756358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-464.html', 'title': 'N-464', 'score': 0.9996837696687862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-280.html', 'title': 'N-280', 'score': 0.999676997537932}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-138.html', 'title': 'N-138', 'score': 0.9996457914421757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html', 'title': 'N-928', 'score': 0.9996289748067742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html', 'title': 'N-225', 'score': 0.9995989738772315}]
result = search.search('orange kiwi kiwi papaya tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #23 checking search results for 'orange kiwi kiwi papaya tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #23 checking search results for 'orange kiwi kiwi papaya tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking search results for 'blueberry pear cherry apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01923122322686592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01559155487114157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013038912129420765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010265919442263327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008717983268626566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.00698666694090583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006281729693199039}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005894096226761155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.005478967636319977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005404262443773466}]
result = search.search('blueberry pear cherry apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #24 checking search results for 'blueberry pear cherry apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #24 checking search results for 'blueberry pear cherry apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking search results for 'blueberry pear cherry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-648.html', 'title': 'N-648', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-207.html', 'title': 'N-207', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-562.html', 'title': 'N-562', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html', 'title': 'N-113', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-784.html', 'title': 'N-784', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html', 'title': 'N-793', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-984.html', 'title': 'N-984', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9983112624366861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-455.html', 'title': 'N-455', 'score': 0.997317296534171}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9972687706234811}]
result = search.search('blueberry pear cherry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #25 checking search results for 'blueberry pear cherry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #25 checking search results for 'blueberry pear cherry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking search results for 'apple apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.019319061048434658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01565459383235844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01341931508697218}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00895804350243633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007768623288681725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.00610091081332208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006090174146708799}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006063278773617396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005942439634536096}]
result = search.search('apple apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #26 checking search results for 'apple apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #26 checking search results for 'apple apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking search results for 'apple apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html', 'title': 'N-928', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-328.html', 'title': 'N-328', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html', 'title': 'N-513', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-685.html', 'title': 'N-685', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-417.html', 'title': 'N-417', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-739.html', 'title': 'N-739', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-124.html', 'title': 'N-124', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-740.html', 'title': 'N-740', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-136.html', 'title': 'N-136', 'score': 1.0000000000000002}]
result = search.search('apple apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #27 checking search results for 'apple apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #27 checking search results for 'apple apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking search results for 'kiwi tomato papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.016318574200614822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014039277899028767}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012529115225900427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010523963452668332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009585638791585721}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007699993828635363}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007449213525731298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006925858951993234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006518091009967331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006297448657263517}]
result = search.search('kiwi tomato papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #28 checking search results for 'kiwi tomato papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #28 checking search results for 'kiwi tomato papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking search results for 'kiwi tomato papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-422.html', 'title': 'N-422', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-853.html', 'title': 'N-853', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-33.html', 'title': 'N-33', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html', 'title': 'N-842', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-11.html', 'title': 'N-11', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html', 'title': 'N-32', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-329.html', 'title': 'N-329', 'score': 1.0000000000000002}]
result = search.search('kiwi tomato papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #29 checking search results for 'kiwi tomato papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #29 checking search results for 'kiwi tomato papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking search results for 'cherry apple apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.019623087091648454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01411269667107302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012659018167875066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010689444999098387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008789683963555634}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007392968259732515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007093499282158914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006444785948075812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006393547904868524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.0061502196446790326}]
result = search.search('cherry apple apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #30 checking search results for 'cherry apple apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #30 checking search results for 'cherry apple apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking search results for 'cherry apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-304.html', 'title': 'N-304', 'score': 0.9999973073672037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-360.html', 'title': 'N-360', 'score': 0.9999960605107238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-82.html', 'title': 'N-82', 'score': 0.9999940274760166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-507.html', 'title': 'N-507', 'score': 0.9999906099510437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-934.html', 'title': 'N-934', 'score': 0.9999854177367862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-975.html', 'title': 'N-975', 'score': 0.9999785978687653}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-912.html', 'title': 'N-912', 'score': 0.9999265861657228}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-914.html', 'title': 'N-914', 'score': 0.9999258427093741}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-866.html', 'title': 'N-866', 'score': 0.999920960253831}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-401.html', 'title': 'N-401', 'score': 0.9999016602677355}]
result = search.search('cherry apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #31 checking search results for 'cherry apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #31 checking search results for 'cherry apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking search results for 'blueberry pear orange papaya papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01609608836484161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013492172856654707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.011982999579705462}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009995206387923434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009907146162126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.0074729630003545315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0074517495721325615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006211092401060737}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005466565299653002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005451127406308336}]
result = search.search('blueberry pear orange papaya papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #32 checking search results for 'blueberry pear orange papaya papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #32 checking search results for 'blueberry pear orange papaya papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking search results for 'blueberry pear orange papaya papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-353.html', 'title': 'N-353', 'score': 0.9997757750179754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-186.html', 'title': 'N-186', 'score': 0.999747041322277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-755.html', 'title': 'N-755', 'score': 0.999635128567126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.9996016874917786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-996.html', 'title': 'N-996', 'score': 0.9995366313351991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html', 'title': 'N-113', 'score': 0.999341297081517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-711.html', 'title': 'N-711', 'score': 0.9992991394312185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-645.html', 'title': 'N-645', 'score': 0.9984929833505292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html', 'title': 'N-286', 'score': 0.9978518715063336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html', 'title': 'N-248', 'score': 0.996733715046946}]
result = search.search('blueberry pear orange papaya papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #33 checking search results for 'blueberry pear orange papaya papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #33 checking search results for 'blueberry pear orange papaya papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking search results for 'banana peach papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.016932863327477832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01438437573861319}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012566066486612754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010532876768102278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008841920334065993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007217249601477192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007017417563513389}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006440723963874576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.0060498595397399345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005600692262217529}]
result = search.search('banana peach papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #34 checking search results for 'banana peach papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #34 checking search results for 'banana peach papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking search results for 'banana peach papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-728.html', 'title': 'N-728', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html', 'title': 'N-849', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-810.html', 'title': 'N-810', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-686.html', 'title': 'N-686', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-120.html', 'title': 'N-120', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-758.html', 'title': 'N-758', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-68.html', 'title': 'N-68', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-820.html', 'title': 'N-820', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-644.html', 'title': 'N-644', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-833.html', 'title': 'N-833', 'score': 1.0}]
result = search.search('banana peach papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #35 checking search results for 'banana peach papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #35 checking search results for 'banana peach papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking search results for 'lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #36 checking search results for 'lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #36 checking search results for 'lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking search results for 'lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}]
result = search.search('lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #37 checking search results for 'lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #37 checking search results for 'lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking search results for 'banana blueberry fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014909357694337821}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013214070829038674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01215802077173315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010403484152397514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008840801376231775}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007205719162144418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.006689530520682919}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005640092884198202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005318439717904757}]
result = search.search('banana blueberry fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #38 checking search results for 'banana blueberry fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #38 checking search results for 'banana blueberry fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking search results for 'banana blueberry fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-164.html', 'title': 'N-164', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-406.html', 'title': 'N-406', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-966.html', 'title': 'N-966', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-859.html', 'title': 'N-859', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-770.html', 'title': 'N-770', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-902.html', 'title': 'N-902', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-625.html', 'title': 'N-625', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-984.html', 'title': 'N-984', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html', 'title': 'N-801', 'score': 1.0000000000000002}]
result = search.search('banana blueberry fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #39 checking search results for 'banana blueberry fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #39 checking search results for 'banana blueberry fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking search results for 'fig lime tomato lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01863111981120661}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01417334334402279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.011225975086268264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009785570840185942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009644672517367815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008465993430700414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0077649675245764025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006656621254537411}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.0065485836497910736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006184756102494871}]
result = search.search('fig lime tomato lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #40 checking search results for 'fig lime tomato lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #40 checking search results for 'fig lime tomato lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking search results for 'fig lime tomato lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-208.html', 'title': 'N-208', 'score': 0.9999731373185332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-903.html', 'title': 'N-903', 'score': 0.999963307408323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-942.html', 'title': 'N-942', 'score': 0.9999447391590645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-727.html', 'title': 'N-727', 'score': 0.9999409828237422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'title': 'N-59', 'score': 0.9999384771132541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-271.html', 'title': 'N-271', 'score': 0.9999375949133215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-759.html', 'title': 'N-759', 'score': 0.9999327873404605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-563.html', 'title': 'N-563', 'score': 0.9998529556643848}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.9998029061252391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-969.html', 'title': 'N-969', 'score': 0.9998029061252391}]
result = search.search('fig lime tomato lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #41 checking search results for 'fig lime tomato lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #41 checking search results for 'fig lime tomato lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking search results for 'apple pear cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.017877351284639985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015384710432739309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013100111397317753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010383709704134537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008040656253828719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.007474235992183602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006915487572660847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.006284673584767969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005980041833256873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005739340184527211}]
result = search.search('apple pear cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #42 checking search results for 'apple pear cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #42 checking search results for 'apple pear cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking search results for 'apple pear cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-354.html', 'title': 'N-354', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-697.html', 'title': 'N-697', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-264.html', 'title': 'N-264', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-73.html', 'title': 'N-73', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-733.html', 'title': 'N-733', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-646.html', 'title': 'N-646', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-726.html', 'title': 'N-726', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-390.html', 'title': 'N-390', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-394.html', 'title': 'N-394', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-214.html', 'title': 'N-214', 'score': 1.0000000000000002}]
result = search.search('apple pear cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #43 checking search results for 'apple pear cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #43 checking search results for 'apple pear cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking search results for 'peach blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01840753793308014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013328984421536393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013066126395021312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006636407372527504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006235007559888876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006188589592883851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005858199346493231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005564504311234779}]
result = search.search('peach blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #44 checking search results for 'peach blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #44 checking search results for 'peach blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking search results for 'peach blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html', 'title': 'N-36', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html', 'title': 'N-513', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-572.html', 'title': 'N-572', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-132.html', 'title': 'N-132', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html', 'title': 'N-211', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-133.html', 'title': 'N-133', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html', 'title': 'N-416', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-601.html', 'title': 'N-601', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-215.html', 'title': 'N-215', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-547.html', 'title': 'N-547', 'score': 1.0000000000000002}]
result = search.search('peach blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #45 checking search results for 'peach blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #45 checking search results for 'peach blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking search results for 'banana papaya peach coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.015942710706188832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.012607100712520617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.011591618811439284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010371396090341793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00847040543063051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006820394139898835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006017133470339492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005941116720853785}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.005696092774730793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005510564446002089}]
result = search.search('banana papaya peach coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #46 checking search results for 'banana papaya peach coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #46 checking search results for 'banana papaya peach coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking search results for 'banana papaya peach coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-771.html', 'title': 'N-771', 'score': 0.9997437802883192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-493.html', 'title': 'N-493', 'score': 0.9996124293009894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-204.html', 'title': 'N-204', 'score': 0.9976845509702185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-295.html', 'title': 'N-295', 'score': 0.9976344093867787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-944.html', 'title': 'N-944', 'score': 0.9969365119222148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html', 'title': 'N-388', 'score': 0.9968219609305499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-172.html', 'title': 'N-172', 'score': 0.9962831178563165}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html', 'title': 'N-193', 'score': 0.9962553510023602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-959.html', 'title': 'N-959', 'score': 0.9959704384115279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-168.html', 'title': 'N-168', 'score': 0.995308136199631}]
result = search.search('banana papaya peach coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #47 checking search results for 'banana papaya peach coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #47 checking search results for 'banana papaya peach coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking search results for 'fig peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01754917779843951}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012062095601485455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010029239128097122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.009433677615679634}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008270977715148582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0077820233881763165}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006548805184656946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006288899918246183}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006270059508848329}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.005822785387235595}]
result = search.search('fig peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #48 checking search results for 'fig peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #48 checking search results for 'fig peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking search results for 'fig peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-88.html', 'title': 'N-88', 'score': 0.999997146063442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-727.html', 'title': 'N-727', 'score': 0.9999962994003575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-905.html', 'title': 'N-905', 'score': 0.999995539046152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-974.html', 'title': 'N-974', 'score': 0.9999924145171122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-229.html', 'title': 'N-229', 'score': 0.9999834963252165}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-39.html', 'title': 'N-39', 'score': 0.9999815891781583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html', 'title': 'N-18', 'score': 0.9999106783468987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-690.html', 'title': 'N-690', 'score': 0.9999086386987228}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-981.html', 'title': 'N-981', 'score': 0.9999005285255543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-413.html', 'title': 'N-413', 'score': 0.9998992286038179}]
result = search.search('fig peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #49 checking search results for 'fig peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #49 checking search results for 'fig peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking search results for 'coconut coconut lime cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014103735200931515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013159219393161569}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.011209226384593561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.01046855869393735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.009634522355123127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.007975537910079409}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007556260957830087}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007210302217709999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006257969921548905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.00564292202020439}]
result = search.search('coconut coconut lime cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #50 checking search results for 'coconut coconut lime cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #50 checking search results for 'coconut coconut lime cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking search results for 'coconut coconut lime cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html', 'title': 'N-497', 'score': 0.9996256866128199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-243.html', 'title': 'N-243', 'score': 0.9995029886788036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-841.html', 'title': 'N-841', 'score': 0.9995029886788036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-652.html', 'title': 'N-652', 'score': 0.9994889664511293}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-599.html', 'title': 'N-599', 'score': 0.9994755837725483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-884.html', 'title': 'N-884', 'score': 0.9994755837725483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-184.html', 'title': 'N-184', 'score': 0.9994388901223947}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-855.html', 'title': 'N-855', 'score': 0.9994204947620632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html', 'title': 'N-927', 'score': 0.9994066828836228}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-134.html', 'title': 'N-134', 'score': 0.9993987533372368}]
result = search.search('coconut coconut lime cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #51 checking search results for 'coconut coconut lime cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #51 checking search results for 'coconut coconut lime cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking search results for 'tomato orange cherry pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.018665285425670367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015608567604736837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013343298271338008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010139723858993263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.009204382708844923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008271009996145943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007126610614381645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006571427631583541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.0056855615367953465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005627383552118079}]
result = search.search('tomato orange cherry pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #52 checking search results for 'tomato orange cherry pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #52 checking search results for 'tomato orange cherry pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking search results for 'tomato orange cherry pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-223.html', 'title': 'N-223', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'title': 'N-59', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html', 'title': 'N-793', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-417.html', 'title': 'N-417', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-711.html', 'title': 'N-711', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-904.html', 'title': 'N-904', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-542.html', 'title': 'N-542', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-616.html', 'title': 'N-616', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-945.html', 'title': 'N-945', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html', 'title': 'N-598', 'score': 1.0}]
result = search.search('tomato orange cherry pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #53 checking search results for 'tomato orange cherry pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #53 checking search results for 'tomato orange cherry pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #54 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #54 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #55 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #55 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking search results for 'orange coconut apple papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01552184355200728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.014313860844294198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013240548245425232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.01025527984653817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009295081632169811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008147565680068157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007572076151148697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007422877606229649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.005910981636909265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005817722108847718}]
result = search.search('orange coconut apple papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #56 checking search results for 'orange coconut apple papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #56 checking search results for 'orange coconut apple papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking search results for 'orange coconut apple papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html', 'title': 'N-842', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html', 'title': 'N-404', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html', 'title': 'N-416', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-520.html', 'title': 'N-520', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-771.html', 'title': 'N-771', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-798.html', 'title': 'N-798', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-189.html', 'title': 'N-189', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-635.html', 'title': 'N-635', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html', 'title': 'N-237', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-426.html', 'title': 'N-426', 'score': 1.0}]
result = search.search('orange coconut apple papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #57 checking search results for 'orange coconut apple papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #57 checking search results for 'orange coconut apple papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking search results for 'peach orange papaya kiwi papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01403556967799665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.011990528291682099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.011938584422649863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009633180816565265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008584641670908916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007787207541929895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006407384321199617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006245444312378672}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006245056052723818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005919248580878124}]
result = search.search('peach orange papaya kiwi papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #58 checking search results for 'peach orange papaya kiwi papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #58 checking search results for 'peach orange papaya kiwi papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking search results for 'peach orange papaya kiwi papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.9997509038150195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-978.html', 'title': 'N-978', 'score': 0.9997168391690986}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-996.html', 'title': 'N-996', 'score': 0.9995440972488472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-485.html', 'title': 'N-485', 'score': 0.9995239399333025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-787.html', 'title': 'N-787', 'score': 0.9989069415484102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-326.html', 'title': 'N-326', 'score': 0.9968200736169237}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-711.html', 'title': 'N-711', 'score': 0.9967386914600004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-484.html', 'title': 'N-484', 'score': 0.995744870632581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-186.html', 'title': 'N-186', 'score': 0.9955673600173381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-860.html', 'title': 'N-860', 'score': 0.9954461452045764}]
result = search.search('peach orange papaya kiwi papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #59 checking search results for 'peach orange papaya kiwi papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #59 checking search results for 'peach orange papaya kiwi papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking search results for 'kiwi papaya pear cherry papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.014040976822866763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.012891822360821453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.011627120442571718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009756384106613428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.007942099506291512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007484003586148292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.00679246458392202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005947237825769497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.005740201367156049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005528505937055925}]
result = search.search('kiwi papaya pear cherry papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #60 checking search results for 'kiwi papaya pear cherry papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #60 checking search results for 'kiwi papaya pear cherry papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking search results for 'kiwi papaya pear cherry papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-996.html', 'title': 'N-996', 'score': 0.9995419598530486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-984.html', 'title': 'N-984', 'score': 0.9995315116455803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-711.html', 'title': 'N-711', 'score': 0.9993033739591172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-522.html', 'title': 'N-522', 'score': 0.9956447994368569}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-469.html', 'title': 'N-469', 'score': 0.9956251418004217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-75.html', 'title': 'N-75', 'score': 0.9956010955405096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-186.html', 'title': 'N-186', 'score': 0.9955877215371304}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-680.html', 'title': 'N-680', 'score': 0.995389463495791}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 0.995073705363867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-577.html', 'title': 'N-577', 'score': 0.9950242976577758}]
result = search.search('kiwi papaya pear cherry papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #61 checking search results for 'kiwi papaya pear cherry papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #61 checking search results for 'kiwi papaya pear cherry papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking search results for 'apricot orange fig coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014994815601993543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.013438884325370234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01317049195382574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.010055108169728407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010036432135923354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009532864155924315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0072890730239945755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006103315852303034}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005617601635790415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005416186447478803}]
result = search.search('apricot orange fig coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #62 checking search results for 'apricot orange fig coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #62 checking search results for 'apricot orange fig coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking search results for 'apricot orange fig coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html', 'title': 'N-205', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-572.html', 'title': 'N-572', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-207.html', 'title': 'N-207', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-392.html', 'title': 'N-392', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-713.html', 'title': 'N-713', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html', 'title': 'N-930', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-178.html', 'title': 'N-178', 'score': 0.9974719711426384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html', 'title': 'N-639', 'score': 0.9974455683958217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-974.html', 'title': 'N-974', 'score': 0.9974396302522339}]
result = search.search('apricot orange fig coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #63 checking search results for 'apricot orange fig coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #63 checking search results for 'apricot orange fig coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking search results for 'papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #64 checking search results for 'papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #64 checking search results for 'papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking search results for 'papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}]
result = search.search('papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #65 checking search results for 'papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #65 checking search results for 'papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking search results for 'orange apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.017495935503183513}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01565472410022374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013172066540554205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010523785147567601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008949952629575611}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008027466192654417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007651805446108983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006937878019581654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006517123537591563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006089791412513555}]
result = search.search('orange apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #66 checking search results for 'orange apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #66 checking search results for 'orange apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking search results for 'orange apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html', 'title': 'N-129', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-380.html', 'title': 'N-380', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-471.html', 'title': 'N-471', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html', 'title': 'N-842', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html', 'title': 'N-404', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html', 'title': 'N-32', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-332.html', 'title': 'N-332', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-981.html', 'title': 'N-981', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-110.html', 'title': 'N-110', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-409.html', 'title': 'N-409', 'score': 1.0000000000000002}]
result = search.search('orange apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #67 checking search results for 'orange apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #67 checking search results for 'orange apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking search results for 'cherry apricot banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.015969537080403898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015559448464479741}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.0126848560777458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.0105660538251734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.007741364876132766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.00658197803372589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0065172250268861545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006495939683751151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.006006487450906817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005937287707880879}]
result = search.search('cherry apricot banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #68 checking search results for 'cherry apricot banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #68 checking search results for 'cherry apricot banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking search results for 'cherry apricot banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-292.html', 'title': 'N-292', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'title': 'N-59', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-522.html', 'title': 'N-522', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-859.html', 'title': 'N-859', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-282.html', 'title': 'N-282', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-969.html', 'title': 'N-969', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-911.html', 'title': 'N-911', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-575.html', 'title': 'N-575', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html', 'title': 'N-506', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-218.html', 'title': 'N-218', 'score': 1.0000000000000002}]
result = search.search('cherry apricot banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #69 checking search results for 'cherry apricot banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #69 checking search results for 'cherry apricot banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking search results for 'banana tomato pear fig apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014933035784520264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01336985209554647}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013050149422705453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010297095462912855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008653279286201894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007287157834816897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005836327614790846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.005699026290448802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005614499593815344}]
result = search.search('banana tomato pear fig apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #70 checking search results for 'banana tomato pear fig apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #70 checking search results for 'banana tomato pear fig apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking search results for 'banana tomato pear fig apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-78.html', 'title': 'N-78', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-520.html', 'title': 'N-520', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-768.html', 'title': 'N-768', 'score': 0.9987530522008548}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-380.html', 'title': 'N-380', 'score': 0.9987428238486317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-392.html', 'title': 'N-392', 'score': 0.9985854568941515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html', 'title': 'N-567', 'score': 0.9983158759399896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-120.html', 'title': 'N-120', 'score': 0.9979918234879132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9979883933327599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 0.997828285436089}]
result = search.search('banana tomato pear fig apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #71 checking search results for 'banana tomato pear fig apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #71 checking search results for 'banana tomato pear fig apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking search results for 'orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #72 checking search results for 'orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #72 checking search results for 'orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking search results for 'orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #73 checking search results for 'orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #73 checking search results for 'orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking search results for 'fig orange pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.016614162252688913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015378124074963398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01333802126473579}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009983577729487892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009381233379612896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.009267719826127426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007516491036899642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.00694741788161871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005921674903637786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005652602883966511}]
result = search.search('fig orange pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #74 checking search results for 'fig orange pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #74 checking search results for 'fig orange pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking search results for 'fig orange pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html', 'title': 'N-205', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-417.html', 'title': 'N-417', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-147.html', 'title': 'N-147', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-709.html', 'title': 'N-709', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-207.html', 'title': 'N-207', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-534.html', 'title': 'N-534', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-452.html', 'title': 'N-452', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-828.html', 'title': 'N-828', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-195.html', 'title': 'N-195', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-238.html', 'title': 'N-238', 'score': 1.0}]
result = search.search('fig orange pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #75 checking search results for 'fig orange pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #75 checking search results for 'fig orange pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking search results for 'apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html', 'title': 'N-69', 'score': 0.005896359403508087}]
result = search.search('apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #76 checking search results for 'apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #76 checking search results for 'apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking search results for 'apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #77 checking search results for 'apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #77 checking search results for 'apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking search results for 'kiwi orange apple lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.018658381677694465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015174680364993927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012149308220675554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.01011273485381446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009388953666634788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007535178912080918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.0071353008975708985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00691941826775269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006518997675898347}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006190189874455138}]
result = search.search('kiwi orange apple lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #78 checking search results for 'kiwi orange apple lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #78 checking search results for 'kiwi orange apple lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking search results for 'kiwi orange apple lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html', 'title': 'N-793', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html', 'title': 'N-193', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-253.html', 'title': 'N-253', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'title': 'N-351', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-467.html', 'title': 'N-467', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-476.html', 'title': 'N-476', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-541.html', 'title': 'N-541', 'score': 0.999055243749658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-912.html', 'title': 'N-912', 'score': 0.9980641081138588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-333.html', 'title': 'N-333', 'score': 0.9975113926841243}]
result = search.search('kiwi orange apple lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #79 checking search results for 'kiwi orange apple lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #79 checking search results for 'kiwi orange apple lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking search results for 'cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #80 checking search results for 'cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #80 checking search results for 'cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking search results for 'cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #81 checking search results for 'cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #81 checking search results for 'cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #82 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #82 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #83 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #83 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking search results for 'cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #84 checking search results for 'cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #84 checking search results for 'cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking search results for 'cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #85 checking search results for 'cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #85 checking search results for 'cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking search results for 'peach tomato lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.017939738148841526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013651294012986745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013366262089398935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.01066114701696974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009323299552736542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0077154058298865465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006725693722377821}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006530045159494694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005672427730973626}]
result = search.search('peach tomato lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #86 checking search results for 'peach tomato lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #86 checking search results for 'peach tomato lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking search results for 'peach tomato lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-380.html', 'title': 'N-380', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html', 'title': 'N-687', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-87.html', 'title': 'N-87', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-102.html', 'title': 'N-102', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-131.html', 'title': 'N-131', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html', 'title': 'N-236', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-239.html', 'title': 'N-239', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-634.html', 'title': 'N-634', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-300.html', 'title': 'N-300', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html', 'title': 'N-491', 'score': 1.0000000000000002}]
result = search.search('peach tomato lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #87 checking search results for 'peach tomato lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #87 checking search results for 'peach tomato lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking search results for 'papaya kiwi apricot pear tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01745600915275458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01479425967267351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012184602831758717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010431028073195714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008808927678895292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007471087988856537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006211937527067887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005854691872500718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005789863836029921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005454694984415384}]
result = search.search('papaya kiwi apricot pear tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #88 checking search results for 'papaya kiwi apricot pear tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #88 checking search results for 'papaya kiwi apricot pear tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking search results for 'papaya kiwi apricot pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-276.html', 'title': 'N-276', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-713.html', 'title': 'N-713', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-771.html', 'title': 'N-771', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-731.html', 'title': 'N-731', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-767.html', 'title': 'N-767', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-758.html', 'title': 'N-758', 'score': 0.9988249550597008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-451.html', 'title': 'N-451', 'score': 0.9984849451119691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-360.html', 'title': 'N-360', 'score': 0.9983883801916598}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-695.html', 'title': 'N-695', 'score': 0.9980099802670186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9979335748537199}]
result = search.search('papaya kiwi apricot pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #89 checking search results for 'papaya kiwi apricot pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #89 checking search results for 'papaya kiwi apricot pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking search results for 'coconut pear papaya tomato blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.016187853972638184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015074432847950715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013250802512269412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010660359362739817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009524049202914418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006890150026535339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.005931543070317588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005830202403339078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.0053615428321016605}]
result = search.search('coconut pear papaya tomato blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #90 checking search results for 'coconut pear papaya tomato blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #90 checking search results for 'coconut pear papaya tomato blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking search results for 'coconut pear papaya tomato blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-464.html', 'title': 'N-464', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-850.html', 'title': 'N-850', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-562.html', 'title': 'N-562', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-242.html', 'title': 'N-242', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-412.html', 'title': 'N-412', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-713.html', 'title': 'N-713', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-828.html', 'title': 'N-828', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-843.html', 'title': 'N-843', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-23.html', 'title': 'N-23', 'score': 1.0}]
result = search.search('coconut pear papaya tomato blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #91 checking search results for 'coconut pear papaya tomato blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #91 checking search results for 'coconut pear papaya tomato blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking search results for 'blueberry peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01840753793308014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013328984421536393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013066126395021312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006636407372527504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006235007559888876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006188589592883851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005858199346493231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005564504311234779}]
result = search.search('blueberry peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #92 checking search results for 'blueberry peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #92 checking search results for 'blueberry peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking search results for 'blueberry peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html', 'title': 'N-36', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html', 'title': 'N-513', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-572.html', 'title': 'N-572', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-132.html', 'title': 'N-132', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html', 'title': 'N-211', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-133.html', 'title': 'N-133', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html', 'title': 'N-416', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-601.html', 'title': 'N-601', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-215.html', 'title': 'N-215', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-547.html', 'title': 'N-547', 'score': 1.0000000000000002}]
result = search.search('blueberry peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #93 checking search results for 'blueberry peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #93 checking search results for 'blueberry peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking search results for 'cherry apricot fig blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.016418395796332173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015270851000995221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013270387646453507}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010040982999668312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008221177191325514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008004947091986675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.0069567904654614385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.0058951273684186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.005855316741898307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005444092727021982}]
result = search.search('cherry apricot fig blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #94 checking search results for 'cherry apricot fig blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #94 checking search results for 'cherry apricot fig blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking search results for 'cherry apricot fig blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-572.html', 'title': 'N-572', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-207.html', 'title': 'N-207', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-859.html', 'title': 'N-859', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html', 'title': 'N-113', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-723.html', 'title': 'N-723', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-545.html', 'title': 'N-545', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-984.html', 'title': 'N-984', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.998287141013166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9981946901321713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-824.html', 'title': 'N-824', 'score': 0.9980098817079602}]
result = search.search('cherry apricot fig blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #95 checking search results for 'cherry apricot fig blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #95 checking search results for 'cherry apricot fig blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking search results for 'lime coconut kiwi kiwi kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.017654402535540056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015292430886263373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.010340018013011166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010132880420551382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009537732699214683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.009334997675882407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006895852556868728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006697613859495989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005346947144080375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005201273862384031}]
result = search.search('lime coconut kiwi kiwi kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #96 checking search results for 'lime coconut kiwi kiwi kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #96 checking search results for 'lime coconut kiwi kiwi kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking search results for 'lime coconut kiwi kiwi kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-300.html', 'title': 'N-300', 'score': 0.9991286500629453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-991.html', 'title': 'N-991', 'score': 0.9988979787149519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html', 'title': 'N-262', 'score': 0.9988507184495454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html', 'title': 'N-465', 'score': 0.9987659573560801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-347.html', 'title': 'N-347', 'score': 0.9987097330060191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-775.html', 'title': 'N-775', 'score': 0.996522030110362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-459.html', 'title': 'N-459', 'score': 0.996135016789961}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-660.html', 'title': 'N-660', 'score': 0.9947064999065388}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-15.html', 'title': 'N-15', 'score': 0.9945657995306948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html', 'title': 'N-604', 'score': 0.9945629751404337}]
result = search.search('lime coconut kiwi kiwi kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #97 checking search results for 'lime coconut kiwi kiwi kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #97 checking search results for 'lime coconut kiwi kiwi kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking search results for 'lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #98 checking search results for 'lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #98 checking search results for 'lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking search results for 'lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}]
result = search.search('lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #99 checking search results for 'lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #99 checking search results for 'lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking search results for 'banana apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01565637520971464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.014735049269568675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012436401085158519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009433297733804429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007287823087453355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005997574352003075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.005836972899667677}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005622576187960915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005567157211678762}]
result = search.search('banana apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #100 checking search results for 'banana apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #100 checking search results for 'banana apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking search results for 'banana apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-268.html', 'title': 'N-268', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-883.html', 'title': 'N-883', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-906.html', 'title': 'N-906', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-938.html', 'title': 'N-938', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-710.html', 'title': 'N-710', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html', 'title': 'N-555', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'title': 'N-59', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-363.html', 'title': 'N-363', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-607.html', 'title': 'N-607', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-599.html', 'title': 'N-599', 'score': 1.0000000000000002}]
result = search.search('banana apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #101 checking search results for 'banana apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #101 checking search results for 'banana apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking search results for 'peach papaya coconut banana pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01418496108339868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.013850054893598803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012916597472323049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.01057767123118894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009211757160405568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.00768396557066705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007387088125750084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005883439634643129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.005477851861205467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005388800135576237}]
result = search.search('peach papaya coconut banana pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #102 checking search results for 'peach papaya coconut banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #102 checking search results for 'peach papaya coconut banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking search results for 'peach papaya coconut banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-644.html', 'title': 'N-644', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html', 'title': 'N-598', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-412.html', 'title': 'N-412', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9985026051453022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-690.html', 'title': 'N-690', 'score': 0.9973048159304636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-833.html', 'title': 'N-833', 'score': 0.9966858408522239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-686.html', 'title': 'N-686', 'score': 0.9963335674246655}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-843.html', 'title': 'N-843', 'score': 0.9962234137599425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-297.html', 'title': 'N-297', 'score': 0.9945128127477785}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-776.html', 'title': 'N-776', 'score': 0.9944858175126179}]
result = search.search('peach papaya coconut banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #103 checking search results for 'peach papaya coconut banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #103 checking search results for 'peach papaya coconut banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking search results for 'apple blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01827179218148111}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015655029973113285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013325244906975939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010419889228229182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008934150839296719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006386271994449128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006052182655849464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005920288365668767}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.005318555780027771}]
result = search.search('apple blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #104 checking search results for 'apple blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #104 checking search results for 'apple blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking search results for 'apple blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-244.html', 'title': 'N-244', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-422.html', 'title': 'N-422', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-629.html', 'title': 'N-629', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-838.html', 'title': 'N-838', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html', 'title': 'N-129', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-209.html', 'title': 'N-209', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-268.html', 'title': 'N-268', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-558.html', 'title': 'N-558', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-673.html', 'title': 'N-673', 'score': 1.0000000000000002}]
result = search.search('apple blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #105 checking search results for 'apple blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #105 checking search results for 'apple blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking search results for 'kiwi tomato peach kiwi lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01900242064437506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014804248375913837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.011796324968420842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010558387325020015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009614640187498044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008557373402603551}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007553721538007653}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.007266411624305128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.0059888951984407605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005697010340434124}]
result = search.search('kiwi tomato peach kiwi lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #106 checking search results for 'kiwi tomato peach kiwi lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #106 checking search results for 'kiwi tomato peach kiwi lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking search results for 'kiwi tomato peach kiwi lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.9999151965896538}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-496.html', 'title': 'N-496', 'score': 0.9997551406451699}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-464.html', 'title': 'N-464', 'score': 0.9996753684926749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-297.html', 'title': 'N-297', 'score': 0.999671861348886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-412.html', 'title': 'N-412', 'score': 0.9996550354553834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-667.html', 'title': 'N-667', 'score': 0.9996108331359638}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-644.html', 'title': 'N-644', 'score': 0.9995177111811974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html', 'title': 'N-389', 'score': 0.9987842954421374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-682.html', 'title': 'N-682', 'score': 0.9983647698627465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-134.html', 'title': 'N-134', 'score': 0.9977020940604114}]
result = search.search('kiwi tomato peach kiwi lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #107 checking search results for 'kiwi tomato peach kiwi lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #107 checking search results for 'kiwi tomato peach kiwi lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking search results for 'papaya apple fig lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014731323802732524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01471577483868196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013102427597014337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010445061800046042}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009793172797293163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.00803674525028419}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007015620104579295}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006462157591968478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006458751484195867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006073551968835468}]
result = search.search('papaya apple fig lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #108 checking search results for 'papaya apple fig lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #108 checking search results for 'papaya apple fig lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking search results for 'papaya apple fig lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-58.html', 'title': 'N-58', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html', 'title': 'N-965', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-609.html', 'title': 'N-609', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-814.html', 'title': 'N-814', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-635.html', 'title': 'N-635', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 0.9982420432090637}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-912.html', 'title': 'N-912', 'score': 0.9980962753271754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-702.html', 'title': 'N-702', 'score': 0.9979503991836781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-297.html', 'title': 'N-297', 'score': 0.9978472713398364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-823.html', 'title': 'N-823', 'score': 0.9977014104262667}]
result = search.search('papaya apple fig lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #109 checking search results for 'papaya apple fig lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #109 checking search results for 'papaya apple fig lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking search results for 'coconut coconut blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014646426152898642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013014298789795086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010337659497590556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.010165517359574624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00988054944321762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.009563592068246807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008165059827966066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007451086378086184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005610821846624311}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005542535506971251}]
result = search.search('coconut coconut blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #110 checking search results for 'coconut coconut blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #110 checking search results for 'coconut coconut blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking search results for 'coconut coconut blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-921.html', 'title': 'N-921', 'score': 0.9999999993988372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-185.html', 'title': 'N-185', 'score': 0.9999927270895911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html', 'title': 'N-248', 'score': 0.9999879913775965}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-681.html', 'title': 'N-681', 'score': 0.9999850479019465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-116.html', 'title': 'N-116', 'score': 0.9999816936324414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-832.html', 'title': 'N-832', 'score': 0.9999419168933384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-538.html', 'title': 'N-538', 'score': 0.9999231999250815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-584.html', 'title': 'N-584', 'score': 0.9999130985522946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 0.9999073622968839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-715.html', 'title': 'N-715', 'score': 0.9999061073132084}]
result = search.search('coconut coconut blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #111 checking search results for 'coconut coconut blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #111 checking search results for 'coconut coconut blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking search results for 'peach fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.014094870583458102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013253599712779464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.012504374109528892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010681206693239485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009443641659024572}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.00830414602203418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007398708987786199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006232932222919356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006104838910935987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005731407357923604}]
result = search.search('peach fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #112 checking search results for 'peach fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #112 checking search results for 'peach fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking search results for 'peach fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-975.html', 'title': 'N-975', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html', 'title': 'N-205', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-227.html', 'title': 'N-227', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-235.html', 'title': 'N-235', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-244.html', 'title': 'N-244', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-422.html', 'title': 'N-422', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-913.html', 'title': 'N-913', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-985.html', 'title': 'N-985', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-33.html', 'title': 'N-33', 'score': 1.0}]
result = search.search('peach fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #113 checking search results for 'peach fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #113 checking search results for 'peach fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking search results for 'apricot cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01936597441396615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015685442284242682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013246232175876456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010524746293533983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007981848036837332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.007145494116260684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006331975019928861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005997674533634729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.00587311614316463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.005867899763222876}]
result = search.search('apricot cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #114 checking search results for 'apricot cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #114 checking search results for 'apricot cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking search results for 'apricot cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-693.html', 'title': 'N-693', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-215.html', 'title': 'N-215', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-667.html', 'title': 'N-667', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-229.html', 'title': 'N-229', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-71.html', 'title': 'N-71', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-673.html', 'title': 'N-673', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-87.html', 'title': 'N-87', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-407.html', 'title': 'N-407', 'score': 1.0}]
result = search.search('apricot cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #115 checking search results for 'apricot cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #115 checking search results for 'apricot cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking search results for 'peach apple apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.019623087091648454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015262873517550143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013324600301216592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009771679838169149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009372990366285274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0077640322050925754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007509572298636941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.007011036370199059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.0061502196446790326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.006047699110512701}]
result = search.search('peach apple apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #116 checking search results for 'peach apple apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #116 checking search results for 'peach apple apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking search results for 'peach apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-558.html', 'title': 'N-558', 'score': 0.9999974799666511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-821.html', 'title': 'N-821', 'score': 0.9999971255031006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html', 'title': 'N-957', 'score': 0.9999962959919294}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-654.html', 'title': 'N-654', 'score': 0.999995277219285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-82.html', 'title': 'N-82', 'score': 0.9999940274760166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-528.html', 'title': 'N-528', 'score': 0.9999940274760166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-272.html', 'title': 'N-272', 'score': 0.9999614306986123}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-376.html', 'title': 'N-376', 'score': 0.9999280191159404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-187.html', 'title': 'N-187', 'score': 0.9998900880146426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-612.html', 'title': 'N-612', 'score': 0.9998900880146426}]
result = search.search('peach apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #117 checking search results for 'peach apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #117 checking search results for 'peach apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking search results for 'cherry cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('cherry cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #118 checking search results for 'cherry cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #118 checking search results for 'cherry cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking search results for 'cherry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('cherry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #119 checking search results for 'cherry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #119 checking search results for 'cherry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking search results for 'lime kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.020271920433606563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015460052215236036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013283289361493766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010523867211405323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009791739737814876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0077156011885115144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.006953210495502798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006911860283771765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006750697669645524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006521447549740707}]
result = search.search('lime kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #120 checking search results for 'lime kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #120 checking search results for 'lime kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking search results for 'lime kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-223.html', 'title': 'N-223', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-269.html', 'title': 'N-269', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-906.html', 'title': 'N-906', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-187.html', 'title': 'N-187', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-319.html', 'title': 'N-319', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-65.html', 'title': 'N-65', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html', 'title': 'N-555', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-867.html', 'title': 'N-867', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-357.html', 'title': 'N-357', 'score': 1.0000000000000002}]
result = search.search('lime kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #121 checking search results for 'lime kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #121 checking search results for 'lime kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking search results for 'cherry tomato kiwi banana coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01489495981719204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012415725038040424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.011395755690131475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010055354886413317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.009633215006128548}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.0073064473679286795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0071344455140093365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.0070494212588370925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0058225884867303575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.005377759870114017}]
result = search.search('cherry tomato kiwi banana coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #122 checking search results for 'cherry tomato kiwi banana coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #122 checking search results for 'cherry tomato kiwi banana coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking search results for 'cherry tomato kiwi banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-568.html', 'title': 'N-568', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-332.html', 'title': 'N-332', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html', 'title': 'N-598', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html', 'title': 'N-162', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-385.html', 'title': 'N-385', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-530.html', 'title': 'N-530', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-541.html', 'title': 'N-541', 'score': 0.9986082615775856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9984262240971151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.998188774154642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-179.html', 'title': 'N-179', 'score': 0.9981690883152192}]
result = search.search('cherry tomato kiwi banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #123 checking search results for 'cherry tomato kiwi banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #123 checking search results for 'cherry tomato kiwi banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking search results for 'blueberry banana coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015658847385156893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013319835321055198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.011798046160488606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010516050736653959}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009264412264893012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007062503221651851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006860965236664772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005743516364614865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.005376869241997677}]
result = search.search('blueberry banana coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #124 checking search results for 'blueberry banana coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #124 checking search results for 'blueberry banana coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking search results for 'blueberry banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-350.html', 'title': 'N-350', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-201.html', 'title': 'N-201', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-625.html', 'title': 'N-625', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-562.html', 'title': 'N-562', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-436.html', 'title': 'N-436', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-642.html', 'title': 'N-642', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-838.html', 'title': 'N-838', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-332.html', 'title': 'N-332', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-292.html', 'title': 'N-292', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 1.0}]
result = search.search('blueberry banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #125 checking search results for 'blueberry banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #125 checking search results for 'blueberry banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking search results for 'kiwi peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.016678415898146184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012829848160487805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01231865556790048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010680809190464876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008726838783785603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008103286529973677}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.0069411645986591376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.0064375420954595934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006284455781650296}]
result = search.search('kiwi peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #126 checking search results for 'kiwi peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #126 checking search results for 'kiwi peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking search results for 'kiwi peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-227.html', 'title': 'N-227', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-33.html', 'title': 'N-33', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'title': 'N-34', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-471.html', 'title': 'N-471', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-11.html', 'title': 'N-11', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html', 'title': 'N-32', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-199.html', 'title': 'N-199', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html', 'title': 'N-736', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html', 'title': 'N-311', 'score': 1.0000000000000002}]
result = search.search('kiwi peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #127 checking search results for 'kiwi peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #127 checking search results for 'kiwi peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking search results for 'banana papaya lime cherry cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015115548822802473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.013217684851933935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01202832045102552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009436946794981393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008093715842568166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007863262737888904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.0066537763037884815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006215479533613356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006144627462650494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005706892400627353}]
result = search.search('banana papaya lime cherry cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #128 checking search results for 'banana papaya lime cherry cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #128 checking search results for 'banana papaya lime cherry cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking search results for 'banana papaya lime cherry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-412.html', 'title': 'N-412', 'score': 0.9996497059167252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-581.html', 'title': 'N-581', 'score': 0.9996305893409206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-493.html', 'title': 'N-493', 'score': 0.9996129283833635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-375.html', 'title': 'N-375', 'score': 0.9995672873871431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html', 'title': 'N-54', 'score': 0.9982014089219312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-594.html', 'title': 'N-594', 'score': 0.9978446336065669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-274.html', 'title': 'N-274', 'score': 0.9959915422029144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-823.html', 'title': 'N-823', 'score': 0.995840904017328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-451.html', 'title': 'N-451', 'score': 0.9955723360362974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-112.html', 'title': 'N-112', 'score': 0.9949697191719976}]
result = search.search('banana papaya lime cherry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #129 checking search results for 'banana papaya lime cherry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #129 checking search results for 'banana papaya lime cherry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking search results for 'tomato fig coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013216628234373156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01313616651907675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.011090240412881014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010683676941709958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.009655363188000666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009611765118328806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007397047653614305}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007098193689383894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005965720772285864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005425500013528597}]
result = search.search('tomato fig coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #130 checking search results for 'tomato fig coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #130 checking search results for 'tomato fig coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking search results for 'tomato fig coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html', 'title': 'N-205', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-235.html', 'title': 'N-235', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-244.html', 'title': 'N-244', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-913.html', 'title': 'N-913', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-33.html', 'title': 'N-33', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-953.html', 'title': 'N-953', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-194.html', 'title': 'N-194', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-922.html', 'title': 'N-922', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-250.html', 'title': 'N-250', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-998.html', 'title': 'N-998', 'score': 1.0000000000000002}]
result = search.search('tomato fig coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #131 checking search results for 'tomato fig coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #131 checking search results for 'tomato fig coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #132 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #132 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #133 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #133 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking search results for 'pear peach papaya apple peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.016161810849834733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.011765036043967317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.011758753161350315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.01053922276882167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008107393538479515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006883505660632855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006323693602002796}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006101241438642888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006069937708107427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006058327643839786}]
result = search.search('pear peach papaya apple peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #134 checking search results for 'pear peach papaya apple peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #134 checking search results for 'pear peach papaya apple peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking search results for 'pear peach papaya apple peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-697.html', 'title': 'N-697', 'score': 0.999772916945541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-771.html', 'title': 'N-771', 'score': 0.9997437391043981}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-232.html', 'title': 'N-232', 'score': 0.9997085474886974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-39.html', 'title': 'N-39', 'score': 0.9975920037340894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-354.html', 'title': 'N-354', 'score': 0.9968139299097865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-979.html', 'title': 'N-979', 'score': 0.9965275577812069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-229.html', 'title': 'N-229', 'score': 0.9964752494419757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-394.html', 'title': 'N-394', 'score': 0.9962004524524861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-704.html', 'title': 'N-704', 'score': 0.9953626193078104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'title': 'N-28', 'score': 0.9953622625121582}]
result = search.search('pear peach papaya apple peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #135 checking search results for 'pear peach papaya apple peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #135 checking search results for 'pear peach papaya apple peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking search results for 'kiwi lime banana fig peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.014786846926338344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014203508107462307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01184357946925366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010451163047325674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008887234153103456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007607221739928129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.006594557896957078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006524644407506883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006278569234209313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005740577878063323}]
result = search.search('kiwi lime banana fig peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #136 checking search results for 'kiwi lime banana fig peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #136 checking search results for 'kiwi lime banana fig peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking search results for 'kiwi lime banana fig peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-250.html', 'title': 'N-250', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html', 'title': 'N-567', 'score': 0.9982067973387749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-301.html', 'title': 'N-301', 'score': 0.9973644091796777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-334.html', 'title': 'N-334', 'score': 0.9963164013444584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-488.html', 'title': 'N-488', 'score': 0.9952427320864973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'title': 'N-351', 'score': 0.9951960055349782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-624.html', 'title': 'N-624', 'score': 0.994446703294336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-373.html', 'title': 'N-373', 'score': 0.9943340569079357}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-933.html', 'title': 'N-933', 'score': 0.993611556748431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9935372614887124}]
result = search.search('kiwi lime banana fig peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #137 checking search results for 'kiwi lime banana fig peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #137 checking search results for 'kiwi lime banana fig peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking search results for 'coconut apple pear pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01792204996215608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015739279801362704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013336606285804952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.01005665174433258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008104990353457405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.007885297803960778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007071719713450592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.00618724488204185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005203793557572491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005200228369976018}]
result = search.search('coconut apple pear pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #138 checking search results for 'coconut apple pear pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #138 checking search results for 'coconut apple pear pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking search results for 'coconut apple pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-258.html', 'title': 'N-258', 'score': 0.9998802686565084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-102.html', 'title': 'N-102', 'score': 0.9998375484161872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-635.html', 'title': 'N-635', 'score': 0.9997411453602754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-415.html', 'title': 'N-415', 'score': 0.999611816909979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html', 'title': 'N-846', 'score': 0.9996058876279054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.9995933190037547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-749.html', 'title': 'N-749', 'score': 0.9995693701483943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-667.html', 'title': 'N-667', 'score': 0.9995693701483943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-530.html', 'title': 'N-530', 'score': 0.9995693701483943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-609.html', 'title': 'N-609', 'score': 0.999442828461947}]
result = search.search('coconut apple pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #139 checking search results for 'coconut apple pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #139 checking search results for 'coconut apple pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking search results for 'cherry blueberry orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01864236234935037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015690982886149382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013416422931854551}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009759152366782868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.009266396552282138}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008246601136643038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.00655182473787789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.00640863946952367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006080411324131277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 0.00518970750185899}]
result = search.search('cherry blueberry orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #140 checking search results for 'cherry blueberry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #140 checking search results for 'cherry blueberry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking search results for 'cherry blueberry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-432.html', 'title': 'N-432', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-292.html', 'title': 'N-292', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-572.html', 'title': 'N-572', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-893.html', 'title': 'N-893', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-263.html', 'title': 'N-263', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-492.html', 'title': 'N-492', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-751.html', 'title': 'N-751', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-207.html', 'title': 'N-207', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html', 'title': 'N-793', 'score': 1.0}]
result = search.search('cherry blueberry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #141 checking search results for 'cherry blueberry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #141 checking search results for 'cherry blueberry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking search results for 'apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html', 'title': 'N-69', 'score': 0.005896359403508087}]
result = search.search('apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #142 checking search results for 'apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #142 checking search results for 'apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking search results for 'apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #143 checking search results for 'apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #143 checking search results for 'apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking search results for 'cherry banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015460517483464224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.014454824405884737}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013126369470553713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010520732969498296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008185687915598617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008078686178725973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006979552730875828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.006972659930192041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006495394782592469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006398796598396929}]
result = search.search('cherry banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #144 checking search results for 'cherry banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #144 checking search results for 'cherry banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking search results for 'cherry banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-443.html', 'title': 'N-443', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-913.html', 'title': 'N-913', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-71.html', 'title': 'N-71', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-83.html', 'title': 'N-83', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-851.html', 'title': 'N-851', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-869.html', 'title': 'N-869', 'score': 1.0000000000000002}]
result = search.search('cherry banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #145 checking search results for 'cherry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #145 checking search results for 'cherry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking search results for 'peach peach orange cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.014483540705710833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.011637293769098278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01128465966707555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010621779838417533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008584412600506007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007227621955237111}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007185432065644252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006347152766413105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006258273887058998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.005483992518957191}]
result = search.search('peach peach orange cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #146 checking search results for 'peach peach orange cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #146 checking search results for 'peach peach orange cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking search results for 'peach peach orange cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html', 'title': 'N-743', 'score': 0.9999735747051643}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'title': 'N-28', 'score': 0.9999627347663894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-727.html', 'title': 'N-727', 'score': 0.9998975021316339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html', 'title': 'N-506', 'score': 0.9996444056873008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-282.html', 'title': 'N-282', 'score': 0.9995669349520758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-292.html', 'title': 'N-292', 'score': 0.9994513042400767}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-264.html', 'title': 'N-264', 'score': 0.9994284511984204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-138.html', 'title': 'N-138', 'score': 0.9994284511984204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html', 'title': 'N-928', 'score': 0.9994074675929887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html', 'title': 'N-388', 'score': 0.9993881420537408}]
result = search.search('peach peach orange cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #147 checking search results for 'peach peach orange cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #147 checking search results for 'peach peach orange cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking search results for 'fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #148 checking search results for 'fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #148 checking search results for 'fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking search results for 'fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #149 checking search results for 'fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #149 checking search results for 'fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking search results for 'pear coconut blueberry peach pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.017501432238061304}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015057551208480345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013219427025763144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009942803589948099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009119361224626492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007526408950025269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007029819245929547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005825353880715224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005318234488110714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005111552168219287}]
result = search.search('pear coconut blueberry peach pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #150 checking search results for 'pear coconut blueberry peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #150 checking search results for 'pear coconut blueberry peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking search results for 'pear coconut blueberry peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html', 'title': 'N-846', 'score': 0.9997754139682368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-265.html', 'title': 'N-265', 'score': 0.9997078644601946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-572.html', 'title': 'N-572', 'score': 0.9996345096487967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html', 'title': 'N-262', 'score': 0.99960100474295}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-15.html', 'title': 'N-15', 'score': 0.99954713324983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-126.html', 'title': 'N-126', 'score': 0.9985459614832755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-178.html', 'title': 'N-178', 'score': 0.9977260337603633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-660.html', 'title': 'N-660', 'score': 0.9967297513217608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-303.html', 'title': 'N-303', 'score': 0.9963120184100203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-215.html', 'title': 'N-215', 'score': 0.9949025971013252}]
result = search.search('pear coconut blueberry peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #151 checking search results for 'pear coconut blueberry peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #151 checking search results for 'pear coconut blueberry peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #152 checking search results for 'blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005672427730973626}]
result = search.search('blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #152 checking search results for 'blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #152 checking search results for 'blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #153 checking search results for 'blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-223.html', 'title': 'N-223', 'score': 1.0}]
result = search.search('blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #153 checking search results for 'blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #153 checking search results for 'blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking search results for 'kiwi peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01535014900861867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013022738146551506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012829463334139504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010355523951655623}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00918265628922264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0076457726847538625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006913278029828951}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006479947167164574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.0064260703798912555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006283737978486484}]
result = search.search('kiwi peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #154 checking search results for 'kiwi peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #154 checking search results for 'kiwi peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking search results for 'kiwi peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-651.html', 'title': 'N-651', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-760.html', 'title': 'N-760', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html', 'title': 'N-928', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-175.html', 'title': 'N-175', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-306.html', 'title': 'N-306', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-469.html', 'title': 'N-469', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-324.html', 'title': 'N-324', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-691.html', 'title': 'N-691', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html', 'title': 'N-416', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html', 'title': 'N-846', 'score': 1.0000000000000002}]
result = search.search('kiwi peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #155 checking search results for 'kiwi peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #155 checking search results for 'kiwi peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking search results for 'peach kiwi coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01307644653133815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01299564253639729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012317911195401278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010684765780203232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.009155478680567125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.0088404277023215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.00774523410416248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063149161072035154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.006052717455158258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.005408480904981873}]
result = search.search('peach kiwi coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #156 checking search results for 'peach kiwi coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #156 checking search results for 'peach kiwi coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking search results for 'peach kiwi coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-250.html', 'title': 'N-250', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-578.html', 'title': 'N-578', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html', 'title': 'N-842', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-617.html', 'title': 'N-617', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html', 'title': 'N-928', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-833.html', 'title': 'N-833', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html', 'title': 'N-598', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-715.html', 'title': 'N-715', 'score': 1.0}]
result = search.search('peach kiwi coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #157 checking search results for 'peach kiwi coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #157 checking search results for 'peach kiwi coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking search results for 'tomato cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('tomato cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #158 checking search results for 'tomato cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #158 checking search results for 'tomato cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking search results for 'tomato cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('tomato cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #159 checking search results for 'tomato cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #159 checking search results for 'tomato cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking search results for 'orange apricot tomato orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.020332909040181153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015125789288161266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013490807790923827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.01011354659607141}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009533905678477034}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009520902648686018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.00669326088656843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.00655048740864763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006380812834779016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005591012000985864}]
result = search.search('orange apricot tomato orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #160 checking search results for 'orange apricot tomato orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #160 checking search results for 'orange apricot tomato orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking search results for 'orange apricot tomato orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html', 'title': 'N-51', 'score': 0.9999814431254515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-853.html', 'title': 'N-853', 'score': 0.9999796633904818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-470.html', 'title': 'N-470', 'score': 0.999978902154535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-656.html', 'title': 'N-656', 'score': 0.9999525205211187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-541.html', 'title': 'N-541', 'score': 0.9999280234122382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-985.html', 'title': 'N-985', 'score': 0.999906786743588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-469.html', 'title': 'N-469', 'score': 0.9998720415946747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-483.html', 'title': 'N-483', 'score': 0.9998720415946747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-370.html', 'title': 'N-370', 'score': 0.9997731513894429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-501.html', 'title': 'N-501', 'score': 0.9997537599090899}]
result = search.search('orange apricot tomato orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #161 checking search results for 'orange apricot tomato orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #161 checking search results for 'orange apricot tomato orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking search results for 'fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #162 checking search results for 'fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #162 checking search results for 'fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking search results for 'fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #163 checking search results for 'fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #163 checking search results for 'fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking search results for 'apricot coconut kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014871577355644294}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.014369123788367551}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012335721364198231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010397562773856164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.009041975341694191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00882302323190058}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007615468012337338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006211927611705091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005301013929718905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.005300305560888842}]
result = search.search('apricot coconut kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #164 checking search results for 'apricot coconut kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #164 checking search results for 'apricot coconut kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking search results for 'apricot coconut kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-495.html', 'title': 'N-495', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-197.html', 'title': 'N-197', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-319.html', 'title': 'N-319', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html', 'title': 'N-928', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html', 'title': 'N-416', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-754.html', 'title': 'N-754', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-990.html', 'title': 'N-990', 'score': 1.0}]
result = search.search('apricot coconut kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #165 checking search results for 'apricot coconut kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #165 checking search results for 'apricot coconut kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking search results for 'apple orange kiwi cherry peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.016199908411044413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014086589378950656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012610241660406434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009825296411657188}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.00841483265756198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.007940807882405605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0072152192100579}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006462058209918788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.0062438869797979656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0059391276394149504}]
result = search.search('apple orange kiwi cherry peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #166 checking search results for 'apple orange kiwi cherry peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #166 checking search results for 'apple orange kiwi cherry peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #167 checking search results for 'apple orange kiwi cherry peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html', 'title': 'N-846', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html', 'title': 'N-639', 'score': 0.9969370740834648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html', 'title': 'N-193', 'score': 0.9964520907943635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-333.html', 'title': 'N-333', 'score': 0.9964480331630405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9960896463896485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-827.html', 'title': 'N-827', 'score': 0.9951524161640342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-521.html', 'title': 'N-521', 'score': 0.9940554724028032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html', 'title': 'N-311', 'score': 0.9934107567601586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-310.html', 'title': 'N-310', 'score': 0.9916123379567884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html', 'title': 'N-160', 'score': 0.9916048668168447}]
result = search.search('apple orange kiwi cherry peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #167 checking search results for 'apple orange kiwi cherry peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #167 checking search results for 'apple orange kiwi cherry peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking search results for 'coconut peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013805451767886497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.013466690952042537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013081826337921335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009739928343071925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008631983224897286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007746970737909407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006345850245175608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('coconut peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #168 checking search results for 'coconut peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #168 checking search results for 'coconut peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking search results for 'coconut peach tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-901.html', 'title': 'N-901', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-195.html', 'title': 'N-195', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-592.html', 'title': 'N-592', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html', 'title': 'N-205', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-235.html', 'title': 'N-235', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-244.html', 'title': 'N-244', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-913.html', 'title': 'N-913', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-380.html', 'title': 'N-380', 'score': 1.0}]
result = search.search('coconut peach tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #169 checking search results for 'coconut peach tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #169 checking search results for 'coconut peach tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking search results for 'coconut fig pear lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015247082668322946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.014740007459669458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012649449247458106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.01057984387722349}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009475042565996095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.00803708886285145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007718673391843147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007467906969077687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005720543189904372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005436697326019866}]
result = search.search('coconut fig pear lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #170 checking search results for 'coconut fig pear lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #170 checking search results for 'coconut fig pear lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking search results for 'coconut fig pear lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-359.html', 'title': 'N-359', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'title': 'N-28', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-432.html', 'title': 'N-432', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html', 'title': 'N-736', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-920.html', 'title': 'N-920', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-776.html', 'title': 'N-776', 'score': 0.9986589649867937}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-396.html', 'title': 'N-396', 'score': 0.9981113838598994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-823.html', 'title': 'N-823', 'score': 0.9972681742318934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-536.html', 'title': 'N-536', 'score': 0.9972388291878957}]
result = search.search('coconut fig pear lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #171 checking search results for 'coconut fig pear lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #171 checking search results for 'coconut fig pear lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking search results for 'peach apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01936597441396615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013253250692357416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010416071883689041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.00754299623587247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006342027739056717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.00587311614316463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.00556536653497155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005460789415174648}]
result = search.search('peach apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #172 checking search results for 'peach apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #172 checking search results for 'peach apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking search results for 'peach apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-79.html', 'title': 'N-79', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-167.html', 'title': 'N-167', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-975.html', 'title': 'N-975', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-667.html', 'title': 'N-667', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html', 'title': 'N-205', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-227.html', 'title': 'N-227', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html', 'title': 'N-632', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 1.0}]
result = search.search('peach apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #173 checking search results for 'peach apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #173 checking search results for 'peach apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking search results for 'papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #174 checking search results for 'papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #174 checking search results for 'papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking search results for 'papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}]
result = search.search('papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #175 checking search results for 'papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #175 checking search results for 'papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking search results for 'coconut lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015479639579397422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.015376995634109386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012495609372299826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010659685921177295}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009661326906554477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008114219256311101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0075608735096337676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007539301689305089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005680886785254037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00549397121623214}]
result = search.search('coconut lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #176 checking search results for 'coconut lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #176 checking search results for 'coconut lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking search results for 'coconut lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'title': 'N-63', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-432.html', 'title': 'N-432', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-60.html', 'title': 'N-60', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-380.html', 'title': 'N-380', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-554.html', 'title': 'N-554', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-342.html', 'title': 'N-342', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-964.html', 'title': 'N-964', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-826.html', 'title': 'N-826', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-292.html', 'title': 'N-292', 'score': 1.0000000000000002}]
result = search.search('coconut lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #177 checking search results for 'coconut lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #177 checking search results for 'coconut lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking search results for 'cherry cherry apricot peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01743387346877701}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014690530787561747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013427685680197315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.00901980514873106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.008871685340478754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006630959679047836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006177062318591094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.006163766007589856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005814972028401553}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005492473085764459}]
result = search.search('cherry cherry apricot peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #178 checking search results for 'cherry cherry apricot peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #178 checking search results for 'cherry cherry apricot peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking search results for 'cherry cherry apricot peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html', 'title': 'N-580', 'score': 0.9999041881232191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-53.html', 'title': 'N-53', 'score': 0.9998547118679206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-551.html', 'title': 'N-551', 'score': 0.9997403653914906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html', 'title': 'N-416', 'score': 0.9995680397165032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-998.html', 'title': 'N-998', 'score': 0.9995680397165032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-773.html', 'title': 'N-773', 'score': 0.9995606671646373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-246.html', 'title': 'N-246', 'score': 0.9995456010742284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html', 'title': 'N-661', 'score': 0.9995349282314697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-748.html', 'title': 'N-748', 'score': 0.9995349282314697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-390.html', 'title': 'N-390', 'score': 0.9995197534611491}]
result = search.search('cherry cherry apricot peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #179 checking search results for 'cherry cherry apricot peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #179 checking search results for 'cherry cherry apricot peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking search results for 'kiwi pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.019374002042745444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015634982727113615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.011649897617635479}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010524288926723293}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00863961729429671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007739481981030725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006289078909692622}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.0062712325553256325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('kiwi pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #180 checking search results for 'kiwi pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #180 checking search results for 'kiwi pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking search results for 'kiwi pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-601.html', 'title': 'N-601', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-730.html', 'title': 'N-730', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-913.html', 'title': 'N-913', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-33.html', 'title': 'N-33', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-474.html', 'title': 'N-474', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-75.html', 'title': 'N-75', 'score': 1.0}]
result = search.search('kiwi pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #181 checking search results for 'kiwi pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #181 checking search results for 'kiwi pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking search results for 'coconut fig tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014716192100639885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013460649485539591}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.011518191665293215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.01068057561879902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00981771128384917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.008467662355084147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007227621524962007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0057990629024355185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005604833509617134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005399117986852951}]
result = search.search('coconut fig tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #182 checking search results for 'coconut fig tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #182 checking search results for 'coconut fig tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking search results for 'coconut fig tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html', 'title': 'N-205', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-223.html', 'title': 'N-223', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-235.html', 'title': 'N-235', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-244.html', 'title': 'N-244', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-432.html', 'title': 'N-432', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-853.html', 'title': 'N-853', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-913.html', 'title': 'N-913', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-33.html', 'title': 'N-33', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-38.html', 'title': 'N-38', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html', 'title': 'N-61', 'score': 1.0000000000000002}]
result = search.search('coconut fig tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #183 checking search results for 'coconut fig tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #183 checking search results for 'coconut fig tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking search results for 'pear lime kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.019801605219819846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01554456629380672}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.011441755304913797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010544224744158967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009208310644957226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0077189333184917155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007024358904830925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.00590201146048517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005847062310156996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.0057888843954576365}]
result = search.search('pear lime kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #184 checking search results for 'pear lime kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #184 checking search results for 'pear lime kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking search results for 'pear lime kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-75.html', 'title': 'N-75', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-581.html', 'title': 'N-581', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-180.html', 'title': 'N-180', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html', 'title': 'N-928', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-336.html', 'title': 'N-336', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html', 'title': 'N-793', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html', 'title': 'N-99', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html', 'title': 'N-193', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-138.html', 'title': 'N-138', 'score': 1.0}]
result = search.search('pear lime kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #185 checking search results for 'pear lime kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #185 checking search results for 'pear lime kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking search results for 'apricot banana lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.016442711871259976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015564446504404772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.011820073877233387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010617826022688839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008662622879873542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007190256959140411}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006886384332022339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006011065067723985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.005945342421669688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005598149847602369}]
result = search.search('apricot banana lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #186 checking search results for 'apricot banana lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #186 checking search results for 'apricot banana lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking search results for 'apricot banana lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-432.html', 'title': 'N-432', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-292.html', 'title': 'N-292', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-951.html', 'title': 'N-951', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html', 'title': 'N-555', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html', 'title': 'N-618', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-271.html', 'title': 'N-271', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-363.html', 'title': 'N-363', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-321.html', 'title': 'N-321', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-493.html', 'title': 'N-493', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-522.html', 'title': 'N-522', 'score': 1.0000000000000002}]
result = search.search('apricot banana lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #187 checking search results for 'apricot banana lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #187 checking search results for 'apricot banana lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking search results for 'lime orange fig tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.017200855641361798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015349923781274843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012559974999595148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010074354364779983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009461305927973163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.008628688471373266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007569185220979899}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006890816294477379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006435198875628968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}]
result = search.search('lime orange fig tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #188 checking search results for 'lime orange fig tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #188 checking search results for 'lime orange fig tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking search results for 'lime orange fig tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-443.html', 'title': 'N-443', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'title': 'N-34', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-57.html', 'title': 'N-57', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-22.html', 'title': 'N-22', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-333.html', 'title': 'N-333', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-250.html', 'title': 'N-250', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'title': 'N-351', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-920.html', 'title': 'N-920', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-635.html', 'title': 'N-635', 'score': 1.0000000000000002}]
result = search.search('lime orange fig tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #189 checking search results for 'lime orange fig tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #189 checking search results for 'lime orange fig tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking search results for 'peach apricot orange tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.018154753241118454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014133977425368212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012776547336131977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010072507788354395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007521513775147455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.006778946144639853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.00609204686944173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.00580199264703812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.0056495738959327175}]
result = search.search('peach apricot orange tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #190 checking search results for 'peach apricot orange tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #190 checking search results for 'peach apricot orange tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking search results for 'peach apricot orange tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-108.html', 'title': 'N-108', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-239.html', 'title': 'N-239', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-300.html', 'title': 'N-300', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'title': 'N-59', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html', 'title': 'N-604', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-53.html', 'title': 'N-53', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html', 'title': 'N-416', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-713.html', 'title': 'N-713', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-773.html', 'title': 'N-773', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-898.html', 'title': 'N-898', 'score': 1.0000000000000002}]
result = search.search('peach apricot orange tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #191 checking search results for 'peach apricot orange tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #191 checking search results for 'peach apricot orange tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking search results for 'apricot banana apple kiwi banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013635126971091984}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013095363515823686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01164354574206622}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009471672318187605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.007137889194568073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006710397320870429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006689544109002482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006389192367550475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0058528652715949675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.005241454925189067}]
result = search.search('apricot banana apple kiwi banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #192 checking search results for 'apricot banana apple kiwi banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #192 checking search results for 'apricot banana apple kiwi banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking search results for 'apricot banana apple kiwi banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html', 'title': 'N-434', 'score': 0.9998049078439655}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html', 'title': 'N-846', 'score': 0.9997732357879635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-868.html', 'title': 'N-868', 'score': 0.9997732357879635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-319.html', 'title': 'N-319', 'score': 0.9995967499951454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-787.html', 'title': 'N-787', 'score': 0.9982525087434675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html', 'title': 'N-311', 'score': 0.998153683794456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-809.html', 'title': 'N-809', 'score': 0.997818313525356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-773.html', 'title': 'N-773', 'score': 0.9949097480490688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-240.html', 'title': 'N-240', 'score': 0.994595629527953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-992.html', 'title': 'N-992', 'score': 0.9944640957563349}]
result = search.search('apricot banana apple kiwi banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #193 checking search results for 'apricot banana apple kiwi banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #193 checking search results for 'apricot banana apple kiwi banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.015745683271522128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.01349661732578097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010720780007956291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009911093874786484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007789147788928366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00726702789305354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006553792884515175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.0063987965983969275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.0060527174551582566}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #194 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #194 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'title': 'N-91', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-153.html', 'title': 'N-153', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #195 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #195 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking search results for 'papaya cherry peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02033957801858891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013567804228147186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013341369618039367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010212955534614578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.007852770124571244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006686449203842862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006615844388581724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006531831626631905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.00642598965791577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006030969922274791}]
result = search.search('papaya cherry peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #196 checking search results for 'papaya cherry peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #196 checking search results for 'papaya cherry peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking search results for 'papaya cherry peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html', 'title': 'N-32', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html', 'title': 'N-849', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-653.html', 'title': 'N-653', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-454.html', 'title': 'N-454', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-895.html', 'title': 'N-895', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-738.html', 'title': 'N-738', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-804.html', 'title': 'N-804', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-68.html', 'title': 'N-68', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html', 'title': 'N-598', 'score': 1.0}]
result = search.search('papaya cherry peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #197 checking search results for 'papaya cherry peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #197 checking search results for 'papaya cherry peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking search results for 'apricot peach cherry tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.019233292783822888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.013941440488749372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.013247284375684109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010089849480074216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00814626942536979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006706801158950476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.006560555821779724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006073737636224273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005835455844384757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.005586031987247188}]
result = search.search('apricot peach cherry tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #198 checking search results for 'apricot peach cherry tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #198 checking search results for 'apricot peach cherry tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking search results for 'apricot peach cherry tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-309.html', 'title': 'N-309', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-925.html', 'title': 'N-925', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-454.html', 'title': 'N-454', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-895.html', 'title': 'N-895', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-586.html', 'title': 'N-586', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-340.html', 'title': 'N-340', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-24.html', 'title': 'N-24', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-526.html', 'title': 'N-526', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-572.html', 'title': 'N-572', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-107.html', 'title': 'N-107', 'score': 1.0}]
result = search.search('apricot peach cherry tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #199 checking search results for 'apricot peach cherry tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #199 checking search results for 'apricot peach cherry tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
