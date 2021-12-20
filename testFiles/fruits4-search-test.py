
import testingtools
import crawler
import searchdata
import search

output = open('fruits4-search-failed.txt', 'w')
success_output = open('fruits4-search-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html')



#Test #0 checking search results for 'coconut apricot fig apple orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017540178367107497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01746763294237247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015919807128081997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014196552183241144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007927382011435773}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.0075285865921497375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007409564782159022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007406175902308089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006003432825600685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005964031224522057}]
result = search.search('coconut apricot fig apple orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #0 checking search results for 'coconut apricot fig apple orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #0 checking search results for 'coconut apricot fig apple orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking search results for 'coconut apricot fig apple orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-52.html', 'title': 'N-52', 'score': 0.9979524608069142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-290.html', 'title': 'N-290', 'score': 0.9975741853013568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-776.html', 'title': 'N-776', 'score': 0.9975426539662995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-148.html', 'title': 'N-148', 'score': 0.995191978715051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9950219042260149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-383.html', 'title': 'N-383', 'score': 0.9949598253410725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-970.html', 'title': 'N-970', 'score': 0.994231158338116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html', 'title': 'N-154', 'score': 0.993470953090427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-460.html', 'title': 'N-460', 'score': 0.9931235704468857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-762.html', 'title': 'N-762', 'score': 0.9928377645102195}]
result = search.search('coconut apricot fig apple orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #1 checking search results for 'coconut apricot fig apple orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #1 checking search results for 'coconut apricot fig apple orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking search results for 'papaya apricot fig lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01770154382672397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016607646230434175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015421030493323691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014955743445976713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.01067553515818616}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008369812671312558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008179671643687972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00765770169986489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006460031348089923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0056883803603104705}]
result = search.search('papaya apricot fig lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #2 checking search results for 'papaya apricot fig lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #2 checking search results for 'papaya apricot fig lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking search results for 'papaya apricot fig lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-488.html', 'title': 'N-488', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-184.html', 'title': 'N-184', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-61.html', 'title': 'N-61', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-363.html', 'title': 'N-363', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html', 'title': 'N-246', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-617.html', 'title': 'N-617', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-25.html', 'title': 'N-25', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-794.html', 'title': 'N-794', 'score': 1.0}]
result = search.search('papaya apricot fig lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #3 checking search results for 'papaya apricot fig lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #3 checking search results for 'papaya apricot fig lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking search results for 'cherry orange cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017940566033301374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016741808438495046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015615885414280758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014939422504334214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.009702238199138456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00823206186584542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007808407948742328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007783499486461561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006084162461337374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005631107133343049}]
result = search.search('cherry orange cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #4 checking search results for 'cherry orange cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #4 checking search results for 'cherry orange cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking search results for 'cherry orange cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-318.html', 'title': 'N-318', 'score': 0.9999954385455884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-117.html', 'title': 'N-117', 'score': 0.9999945489655915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-461.html', 'title': 'N-461', 'score': 0.9999942920331009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-97.html', 'title': 'N-97', 'score': 0.9999939742639495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-785.html', 'title': 'N-785', 'score': 0.9999938755578398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html', 'title': 'N-286', 'score': 0.9999485017157879}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-993.html', 'title': 'N-993', 'score': 0.9999453232546164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-814.html', 'title': 'N-814', 'score': 0.9999269196614089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-252.html', 'title': 'N-252', 'score': 0.9999034764054295}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-594.html', 'title': 'N-594', 'score': 0.999881258174568}]
result = search.search('cherry orange cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #5 checking search results for 'cherry orange cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #5 checking search results for 'cherry orange cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking search results for 'lime banana blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01726378288162326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01716338334238272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016300379084658135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015454173376978911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008639823002303643}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.0077157720480099685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.006679487120765484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0061861108854210515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005884867716662431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005409327573766698}]
result = search.search('lime banana blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #6 checking search results for 'lime banana blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #6 checking search results for 'lime banana blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking search results for 'lime banana blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-577.html', 'title': 'N-577', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-712.html', 'title': 'N-712', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-620.html', 'title': 'N-620', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-639.html', 'title': 'N-639', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-875.html', 'title': 'N-875', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-342.html', 'title': 'N-342', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-479.html', 'title': 'N-479', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-302.html', 'title': 'N-302', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-434.html', 'title': 'N-434', 'score': 1.0000000000000002}]
result = search.search('lime banana blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #7 checking search results for 'lime banana blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #7 checking search results for 'lime banana blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking search results for 'tomato banana lime papaya banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018380469617559368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018339221231109076}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01494255619962434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.014514828945745833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008150420352904243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008129668339450013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007532200858787789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.0069286495585199415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005611314118688192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.005340976702083447}]
result = search.search('tomato banana lime papaya banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #8 checking search results for 'tomato banana lime papaya banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #8 checking search results for 'tomato banana lime papaya banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking search results for 'tomato banana lime papaya banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-978.html', 'title': 'N-978', 'score': 0.9998469761945564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html', 'title': 'N-139', 'score': 0.9997844957781601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-64.html', 'title': 'N-64', 'score': 0.9997569525346248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-935.html', 'title': 'N-935', 'score': 0.9997317037866954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-351.html', 'title': 'N-351', 'score': 0.9997216343606334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-616.html', 'title': 'N-616', 'score': 0.9997198800777869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-775.html', 'title': 'N-775', 'score': 0.9996773435447522}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-363.html', 'title': 'N-363', 'score': 0.999674111795188}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-517.html', 'title': 'N-517', 'score': 0.9996677801993272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html', 'title': 'N-798', 'score': 0.9996413143492925}]
result = search.search('tomato banana lime papaya banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #9 checking search results for 'tomato banana lime papaya banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #9 checking search results for 'tomato banana lime papaya banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking search results for 'peach pear blueberry pear peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01807170119150778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016223292363240494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014673530212353434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.014142722758146976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008152926767592187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007427266250954751}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007187127203097219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00712240020617772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006126667867795512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.0053744035725676875}]
result = search.search('peach pear blueberry pear peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #10 checking search results for 'peach pear blueberry pear peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #10 checking search results for 'peach pear blueberry pear peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking search results for 'peach pear blueberry pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-267.html', 'title': 'N-267', 'score': 0.9998541114183372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-255.html', 'title': 'N-255', 'score': 0.9998420305520667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-836.html', 'title': 'N-836', 'score': 0.9998091895865339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-411.html', 'title': 'N-411', 'score': 0.9997113714369238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-668.html', 'title': 'N-668', 'score': 0.9996916763696987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-58.html', 'title': 'N-58', 'score': 0.9992432349224423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.9992342075625669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-216.html', 'title': 'N-216', 'score': 0.9992214009300826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html', 'title': 'N-605', 'score': 0.9990070928617331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html', 'title': 'N-379', 'score': 0.9988973578690772}]
result = search.search('peach pear blueberry pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #11 checking search results for 'peach pear blueberry pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #11 checking search results for 'peach pear blueberry pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking search results for 'apricot peach coconut peach lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018077268255649554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017968457761556055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016522067774586736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014910197642651224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008217766492274622}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007865816924170925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007318724106602644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007038103260294974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005404156410580581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.00530937885503312}]
result = search.search('apricot peach coconut peach lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #12 checking search results for 'apricot peach coconut peach lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #12 checking search results for 'apricot peach coconut peach lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking search results for 'apricot peach coconut peach lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-899.html', 'title': 'N-899', 'score': 0.9996495118776029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-362.html', 'title': 'N-362', 'score': 0.9995625639221257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-315.html', 'title': 'N-315', 'score': 0.9981012253808603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-141.html', 'title': 'N-141', 'score': 0.9970312970258157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-102.html', 'title': 'N-102', 'score': 0.9965537132585102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-525.html', 'title': 'N-525', 'score': 0.9965466599224859}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-566.html', 'title': 'N-566', 'score': 0.9963023501521615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-501.html', 'title': 'N-501', 'score': 0.995536644951706}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-316.html', 'title': 'N-316', 'score': 0.9955089036386602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.9949306926373771}]
result = search.search('apricot peach coconut peach lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #13 checking search results for 'apricot peach coconut peach lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #13 checking search results for 'apricot peach coconut peach lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking search results for 'kiwi papaya kiwi banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017732033813935233}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016801293054967057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015004544446239698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.014835972139818658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008719064168579566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.00827417152921499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0074796055498842625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.006764990980679734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006472092603642258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html', 'title': 'N-80', 'score': 0.005250265278263153}]
result = search.search('kiwi papaya kiwi banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #14 checking search results for 'kiwi papaya kiwi banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #14 checking search results for 'kiwi papaya kiwi banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking search results for 'kiwi papaya kiwi banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-445.html', 'title': 'N-445', 'score': 0.9996483762135322}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-649.html', 'title': 'N-649', 'score': 0.9994674973971298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-199.html', 'title': 'N-199', 'score': 0.9994674973971298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-577.html', 'title': 'N-577', 'score': 0.9994453573815545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-393.html', 'title': 'N-393', 'score': 0.9994453573815545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-457.html', 'title': 'N-457', 'score': 0.999389023047149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-254.html', 'title': 'N-254', 'score': 0.999373012110637}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-917.html', 'title': 'N-917', 'score': 0.9992874126745043}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html', 'title': 'N-453', 'score': 0.9988092117134884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-336.html', 'title': 'N-336', 'score': 0.9986965661679809}]
result = search.search('kiwi papaya kiwi banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #15 checking search results for 'kiwi papaya kiwi banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #15 checking search results for 'kiwi papaya kiwi banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking search results for 'blueberry banana kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017361710695318257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017357658008331313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.0161350028846927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015453552131460446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008264024543242267}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007440211993930907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.0064469637859404065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006361368778929702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0056310064219540325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005345380978021258}]
result = search.search('blueberry banana kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #16 checking search results for 'blueberry banana kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #16 checking search results for 'blueberry banana kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking search results for 'blueberry banana kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-219.html', 'title': 'N-219', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-556.html', 'title': 'N-556', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-867.html', 'title': 'N-867', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-235.html', 'title': 'N-235', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-621.html', 'title': 'N-621', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-5.html', 'title': 'N-5', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-555.html', 'title': 'N-555', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-586.html', 'title': 'N-586', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-865.html', 'title': 'N-865', 'score': 1.0000000000000002}]
result = search.search('blueberry banana kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #17 checking search results for 'blueberry banana kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #17 checking search results for 'blueberry banana kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking search results for 'coconut tomato fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018534911303090134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01681868637351407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01632042539462621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015461705935265727}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0077159506091554995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00727209715472346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006442078297348807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005667022183583937}]
result = search.search('coconut tomato fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #18 checking search results for 'coconut tomato fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #18 checking search results for 'coconut tomato fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking search results for 'coconut tomato fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-218.html', 'title': 'N-218', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-541.html', 'title': 'N-541', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-556.html', 'title': 'N-556', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html', 'title': 'N-614', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html', 'title': 'N-789', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-208.html', 'title': 'N-208', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-262.html', 'title': 'N-262', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-877.html', 'title': 'N-877', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-776.html', 'title': 'N-776', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-25.html', 'title': 'N-25', 'score': 1.0000000000000002}]
result = search.search('coconut tomato fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #19 checking search results for 'coconut tomato fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #19 checking search results for 'coconut tomato fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking search results for 'fig papaya papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01848294621253086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016233098214483373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01411266398987891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.012929607471292442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010985923816164287}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008183340221834312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007720516156582319}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007646273339849249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006556168901611941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0059853304559281855}]
result = search.search('fig papaya papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #20 checking search results for 'fig papaya papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #20 checking search results for 'fig papaya papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking search results for 'fig papaya papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-396.html', 'title': 'N-396', 'score': 0.9999969841748346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-435.html', 'title': 'N-435', 'score': 0.9999969841748346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-551.html', 'title': 'N-551', 'score': 0.9999963985749605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-360.html', 'title': 'N-360', 'score': 0.9999958517135868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-867.html', 'title': 'N-867', 'score': 0.9999950184682221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-407.html', 'title': 'N-407', 'score': 0.9999936889874922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-97.html', 'title': 'N-97', 'score': 0.9999934131139054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-845.html', 'title': 'N-845', 'score': 0.9999924977225879}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 0.9999766624879022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-357.html', 'title': 'N-357', 'score': 0.9999733668606545}]
result = search.search('fig papaya papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #21 checking search results for 'fig papaya papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #21 checking search results for 'fig papaya papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking search results for 'cherry fig apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017867652588578448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01742322126625632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01678652050985696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013723947504342082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00820927384847492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008083043654042502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007642910628311346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007526508795179724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006140803383228797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006066438177389991}]
result = search.search('cherry fig apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #22 checking search results for 'cherry fig apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #22 checking search results for 'cherry fig apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking search results for 'cherry fig apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-319.html', 'title': 'N-319', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-567.html', 'title': 'N-567', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-307.html', 'title': 'N-307', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-945.html', 'title': 'N-945', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-752.html', 'title': 'N-752', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-558.html', 'title': 'N-558', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-819.html', 'title': 'N-819', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-483.html', 'title': 'N-483', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-619.html', 'title': 'N-619', 'score': 1.0000000000000002}]
result = search.search('cherry fig apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #23 checking search results for 'cherry fig apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #23 checking search results for 'cherry fig apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking search results for 'apricot cherry coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017526573155236515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016648940219080137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014830235637786085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010164154334805437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.00793001549506684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0076357685014345755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00697098355045415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006279004349888554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006188224853595129}]
result = search.search('apricot cherry coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #24 checking search results for 'apricot cherry coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #24 checking search results for 'apricot cherry coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking search results for 'apricot cherry coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-899.html', 'title': 'N-899', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-319.html', 'title': 'N-319', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-189.html', 'title': 'N-189', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-166.html', 'title': 'N-166', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-503.html', 'title': 'N-503', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-749.html', 'title': 'N-749', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-141.html', 'title': 'N-141', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html', 'title': 'N-394', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-803.html', 'title': 'N-803', 'score': 1.0}]
result = search.search('apricot cherry coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #25 checking search results for 'apricot cherry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #25 checking search results for 'apricot cherry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking search results for 'coconut papaya cherry coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.0179133046301983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017674905024774496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01675640526262997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01548734554893874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.00875158167244832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007102778719386593}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006853791493792121}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006539458052154658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.005867010106398381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005575476412335099}]
result = search.search('coconut papaya cherry coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #26 checking search results for 'coconut papaya cherry coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #26 checking search results for 'coconut papaya cherry coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking search results for 'coconut papaya cherry coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.9996293926694007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-880.html', 'title': 'N-880', 'score': 0.9996128493841164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-143.html', 'title': 'N-143', 'score': 0.9995976208195935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-64.html', 'title': 'N-64', 'score': 0.9995803026996223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-77.html', 'title': 'N-77', 'score': 0.9995431295801971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-332.html', 'title': 'N-332', 'score': 0.9995190677436258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-438.html', 'title': 'N-438', 'score': 0.9995135733087289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-924.html', 'title': 'N-924', 'score': 0.999501148464325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html', 'title': 'N-552', 'score': 0.999501148464325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-522.html', 'title': 'N-522', 'score': 0.9994260658400413}]
result = search.search('coconut papaya cherry coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #27 checking search results for 'coconut papaya cherry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #27 checking search results for 'coconut papaya cherry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking search results for 'kiwi blueberry kiwi pear blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017225980727962793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016670373350047556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015654954352793647}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015314332703189566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007623004900237566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007272891978801367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.00686133466703565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.005819976414619429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005676619764449864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.00566912211645911}]
result = search.search('kiwi blueberry kiwi pear blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #28 checking search results for 'kiwi blueberry kiwi pear blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #28 checking search results for 'kiwi blueberry kiwi pear blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking search results for 'kiwi blueberry kiwi pear blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-922.html', 'title': 'N-922', 'score': 0.9998858393582061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-101.html', 'title': 'N-101', 'score': 0.9998754179622225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-648.html', 'title': 'N-648', 'score': 0.9998754179622225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-677.html', 'title': 'N-677', 'score': 0.9998379440818804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-483.html', 'title': 'N-483', 'score': 0.9998318340505863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-569.html', 'title': 'N-569', 'score': 0.9998052175926244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-84.html', 'title': 'N-84', 'score': 0.9998012542623328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-678.html', 'title': 'N-678', 'score': 0.999799977487094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-935.html', 'title': 'N-935', 'score': 0.9997821297300072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-194.html', 'title': 'N-194', 'score': 0.999762151511013}]
result = search.search('kiwi blueberry kiwi pear blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #29 checking search results for 'kiwi blueberry kiwi pear blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #29 checking search results for 'kiwi blueberry kiwi pear blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.005378522404349503}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #30 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #30 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #31 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #31 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking search results for 'fig peach orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018508317845971074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018152526835475753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015016126535940798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014961145454514886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007862770412499536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007462666538548309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007202366524528733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.0063259987206382845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005845349225366277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.005352888438936703}]
result = search.search('fig peach orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #32 checking search results for 'fig peach orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #32 checking search results for 'fig peach orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking search results for 'fig peach orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-242.html', 'title': 'N-242', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-556.html', 'title': 'N-556', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-292.html', 'title': 'N-292', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-677.html', 'title': 'N-677', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html', 'title': 'N-456', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-175.html', 'title': 'N-175', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-320.html', 'title': 'N-320', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-362.html', 'title': 'N-362', 'score': 1.0}]
result = search.search('fig peach orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #33 checking search results for 'fig peach orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #33 checking search results for 'fig peach orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking search results for 'orange peach blueberry cherry tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01786276950994048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017714574780222227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015686911562443506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014832372637547326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.0082217856477237}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.0070317919664958355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00649348342282348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006183860864543579}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.005660404236614161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.00525264696003093}]
result = search.search('orange peach blueberry cherry tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #34 checking search results for 'orange peach blueberry cherry tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #34 checking search results for 'orange peach blueberry cherry tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking search results for 'orange peach blueberry cherry tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-833.html', 'title': 'N-833', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-677.html', 'title': 'N-677', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-342.html', 'title': 'N-342', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-560.html', 'title': 'N-560', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-569.html', 'title': 'N-569', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-824.html', 'title': 'N-824', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-386.html', 'title': 'N-386', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-332.html', 'title': 'N-332', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-410.html', 'title': 'N-410', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-102.html', 'title': 'N-102', 'score': 0.9987921266407667}]
result = search.search('orange peach blueberry cherry tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #35 checking search results for 'orange peach blueberry cherry tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #35 checking search results for 'orange peach blueberry cherry tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking search results for 'peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0059763991091016985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}]
result = search.search('peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #36 checking search results for 'peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #36 checking search results for 'peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking search results for 'peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #37 checking search results for 'peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #37 checking search results for 'peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking search results for 'apple fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01839249866983282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018172294328638962}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016768367128873043}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013282649420091056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008323640654486292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008103438569811184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007794229149037832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007629494422303598}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.00598257880796825}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0059763991091017}]
result = search.search('apple fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #38 checking search results for 'apple fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #38 checking search results for 'apple fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking search results for 'apple fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-158.html', 'title': 'N-158', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-219.html', 'title': 'N-219', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-317.html', 'title': 'N-317', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-541.html', 'title': 'N-541', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-709.html', 'title': 'N-709', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-899.html', 'title': 'N-899', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html', 'title': 'N-24', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html', 'title': 'N-92', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-446.html', 'title': 'N-446', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-502.html', 'title': 'N-502', 'score': 1.0000000000000002}]
result = search.search('apple fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #39 checking search results for 'apple fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #39 checking search results for 'apple fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking search results for 'fig kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018163169204821663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016307122922031465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015383324841057151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01535036172731807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.0087391241293}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008105974711685128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007760879864471845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006438100705934343}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0059763991091016985}]
result = search.search('fig kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #40 checking search results for 'fig kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #40 checking search results for 'fig kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking search results for 'fig kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-158.html', 'title': 'N-158', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html', 'title': 'N-37', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-101.html', 'title': 'N-101', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'title': 'N-72', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-250.html', 'title': 'N-250', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html', 'title': 'N-983', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-324.html', 'title': 'N-324', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-29.html', 'title': 'N-29', 'score': 1.0000000000000002}]
result = search.search('fig kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #41 checking search results for 'fig kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #41 checking search results for 'fig kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking search results for 'fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #42 checking search results for 'fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #42 checking search results for 'fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking search results for 'fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #43 checking search results for 'fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #43 checking search results for 'fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking search results for 'orange fig pear banana papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017721381691761885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016251716345604114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015601973699235277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014963436175452368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008290239632029649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007974832852283925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007943029984040482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007031626742653157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006462676386024867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005351328482531389}]
result = search.search('orange fig pear banana papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #44 checking search results for 'orange fig pear banana papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #44 checking search results for 'orange fig pear banana papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking search results for 'orange fig pear banana papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-488.html', 'title': 'N-488', 'score': 0.9974563307509837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9958141887098964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-60.html', 'title': 'N-60', 'score': 0.9945663631924806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-56.html', 'title': 'N-56', 'score': 0.9944331173939074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-647.html', 'title': 'N-647', 'score': 0.9944100981301088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-148.html', 'title': 'N-148', 'score': 0.9943050621338535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-86.html', 'title': 'N-86', 'score': 0.9942618306762725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html', 'title': 'N-253', 'score': 0.9942519846799927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-449.html', 'title': 'N-449', 'score': 0.9934373827035679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-806.html', 'title': 'N-806', 'score': 0.993328565742315}]
result = search.search('orange fig pear banana papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #45 checking search results for 'orange fig pear banana papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #45 checking search results for 'orange fig pear banana papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking search results for 'apple kiwi coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018463216836294614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016690671637598985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016681542604429368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014222789624608632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008907881883532679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008101855359759502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007732586317464353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007595970845484302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006169939954382512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005886033811840303}]
result = search.search('apple kiwi coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #46 checking search results for 'apple kiwi coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #46 checking search results for 'apple kiwi coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking search results for 'apple kiwi coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-148.html', 'title': 'N-148', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-247.html', 'title': 'N-247', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-667.html', 'title': 'N-667', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-922.html', 'title': 'N-922', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-672.html', 'title': 'N-672', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-195.html', 'title': 'N-195', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-301.html', 'title': 'N-301', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-501.html', 'title': 'N-501', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-337.html', 'title': 'N-337', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-204.html', 'title': 'N-204', 'score': 1.0}]
result = search.search('apple kiwi coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #47 checking search results for 'apple kiwi coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #47 checking search results for 'apple kiwi coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking search results for 'banana banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.005378522404349503}]
result = search.search('banana banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #48 checking search results for 'banana banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #48 checking search results for 'banana banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking search results for 'banana banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('banana banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #49 checking search results for 'banana banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #49 checking search results for 'banana banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking search results for 'banana pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01740939515097538}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016397648398364013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01543331043165836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.012916743944783425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008344836428224095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008212290075434017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007956166899860362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0070016862671781616}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006500643237154173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005419997846535832}]
result = search.search('banana pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #50 checking search results for 'banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #50 checking search results for 'banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking search results for 'banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-652.html', 'title': 'N-652', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-45.html', 'title': 'N-45', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-101.html', 'title': 'N-101', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-224.html', 'title': 'N-224', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-235.html', 'title': 'N-235', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html', 'title': 'N-377', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-567.html', 'title': 'N-567', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-314.html', 'title': 'N-314', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-690.html', 'title': 'N-690', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-455.html', 'title': 'N-455', 'score': 1.0000000000000002}]
result = search.search('banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #51 checking search results for 'banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #51 checking search results for 'banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking search results for 'coconut coconut apple orange cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01735860842776267}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01639272803564148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016079754825359133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015224253548397815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007303169496606626}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.00683304180652935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.0068129038876287165}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006316737572121301}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006115362087870348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.005746652060278618}]
result = search.search('coconut coconut apple orange cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #52 checking search results for 'coconut coconut apple orange cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #52 checking search results for 'coconut coconut apple orange cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking search results for 'coconut coconut apple orange cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-332.html', 'title': 'N-332', 'score': 0.9996958428072831}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html', 'title': 'N-873', 'score': 0.9996736000641864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-514.html', 'title': 'N-514', 'score': 0.9996342922723586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-372.html', 'title': 'N-372', 'score': 0.998447574196563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-84.html', 'title': 'N-84', 'score': 0.9983554198635652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-119.html', 'title': 'N-119', 'score': 0.9978333055776761}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-410.html', 'title': 'N-410', 'score': 0.9972428882182478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-438.html', 'title': 'N-438', 'score': 0.996607807741552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-774.html', 'title': 'N-774', 'score': 0.9958690432432046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-397.html', 'title': 'N-397', 'score': 0.9958069333265888}]
result = search.search('coconut coconut apple orange cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #53 checking search results for 'coconut coconut apple orange cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #53 checking search results for 'coconut coconut apple orange cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking search results for 'apple pear coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018012998965228434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016653152361682817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.014724532532261032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014196296046043581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.00849163234957933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007981469046388748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007596977948160174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007572091523372869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006194842747553331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.00583323965702325}]
result = search.search('apple pear coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #54 checking search results for 'apple pear coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #54 checking search results for 'apple pear coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking search results for 'apple pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-509.html', 'title': 'N-509', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-319.html', 'title': 'N-319', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-799.html', 'title': 'N-799', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html', 'title': 'N-93', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-553.html', 'title': 'N-553', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-51.html', 'title': 'N-51', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-975.html', 'title': 'N-975', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-629.html', 'title': 'N-629', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html', 'title': 'N-979', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-264.html', 'title': 'N-264', 'score': 1.0000000000000002}]
result = search.search('apple pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #55 checking search results for 'apple pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #55 checking search results for 'apple pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking search results for 'pear pear blueberry pear pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017526712598318558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.014217586915665971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.012424662964822458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010516803529697548}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00871416111674179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007476705025324893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006616542331166072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006023196835344332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.0058069238584845815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.005450807210450873}]
result = search.search('pear pear blueberry pear pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #56 checking search results for 'pear pear blueberry pear pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #56 checking search results for 'pear pear blueberry pear pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking search results for 'pear pear blueberry pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-128.html', 'title': 'N-128', 'score': 0.9999904141821121}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-22.html', 'title': 'N-22', 'score': 0.9999763436073354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-563.html', 'title': 'N-563', 'score': 0.9999739898489851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-99.html', 'title': 'N-99', 'score': 0.9999664869438306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-213.html', 'title': 'N-213', 'score': 0.9999522121855257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-141.html', 'title': 'N-141', 'score': 0.9999290654911152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-930.html', 'title': 'N-930', 'score': 0.9999115864105629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-227.html', 'title': 'N-227', 'score': 0.9996447019494066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-823.html', 'title': 'N-823', 'score': 0.9996413799546716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-924.html', 'title': 'N-924', 'score': 0.9996413799546716}]
result = search.search('pear pear blueberry pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #57 checking search results for 'pear pear blueberry pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #57 checking search results for 'pear pear blueberry pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.005378522404349503}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #58 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #58 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #59 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #59 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking search results for 'papaya tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('papaya tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #60 checking search results for 'papaya tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #60 checking search results for 'papaya tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking search results for 'papaya tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 1.0}]
result = search.search('papaya tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #61 checking search results for 'papaya tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #61 checking search results for 'papaya tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking search results for 'pear papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01798240281681793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016768144338376183}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015404104246470209}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.013046662961846967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.01099326627530173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008513027875913006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007013750996083834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0065577838755536515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006114857315303332}]
result = search.search('pear papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #62 checking search results for 'pear papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #62 checking search results for 'pear papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking search results for 'pear papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-219.html', 'title': 'N-219', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-239.html', 'title': 'N-239', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html', 'title': 'N-92', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-757.html', 'title': 'N-757', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html', 'title': 'N-37', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-147.html', 'title': 'N-147', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html', 'title': 'N-30', 'score': 1.0000000000000002}]
result = search.search('pear papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #63 checking search results for 'pear papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #63 checking search results for 'pear papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking search results for 'apple banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018576625341197427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018550979173833602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01640754086111273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013803037917696093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007673712811489487}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007581824303266141}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006275262757339211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005246135096679755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html', 'title': 'N-80', 'score': 0.005011939250590545}]
result = search.search('apple banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #64 checking search results for 'apple banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #64 checking search results for 'apple banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking search results for 'apple banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-861.html', 'title': 'N-861', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html', 'title': 'N-92', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html', 'title': 'N-447', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-556.html', 'title': 'N-556', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-147.html', 'title': 'N-147', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-251.html', 'title': 'N-251', 'score': 1.0000000000000002}]
result = search.search('apple banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #65 checking search results for 'apple banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #65 checking search results for 'apple banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking search results for 'peach peach kiwi cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01804140856451327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017644950299900142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016547665271301425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01533164955630394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007897194073090176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006847313622312926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.0067681091185603035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.006071309941454656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006016512164943339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0057197876107226734}]
result = search.search('peach peach kiwi cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #66 checking search results for 'peach peach kiwi cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #66 checking search results for 'peach peach kiwi cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking search results for 'peach peach kiwi cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-397.html', 'title': 'N-397', 'score': 0.9998887877816806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-5.html', 'title': 'N-5', 'score': 0.999695891852393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-272.html', 'title': 'N-272', 'score': 0.9996516361624943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-212.html', 'title': 'N-212', 'score': 0.9995758271910281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-541.html', 'title': 'N-541', 'score': 0.9994871367605012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-354.html', 'title': 'N-354', 'score': 0.9994722219363382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-711.html', 'title': 'N-711', 'score': 0.9994403676561752}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-578.html', 'title': 'N-578', 'score': 0.9994198478172065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html', 'title': 'N-769', 'score': 0.9994133778224589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-289.html', 'title': 'N-289', 'score': 0.9994121048147643}]
result = search.search('peach peach kiwi cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #67 checking search results for 'peach peach kiwi cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #67 checking search results for 'peach peach kiwi cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking search results for 'orange coconut papaya apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018149308053151056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017822213976836636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015748259045896364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01428656019559464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007931062165279678}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.0075110073435845194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007376838600236463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007180771302060162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006069938282688601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.00598884152012463}]
result = search.search('orange coconut papaya apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #68 checking search results for 'orange coconut papaya apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #68 checking search results for 'orange coconut papaya apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking search results for 'orange coconut papaya apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-166.html', 'title': 'N-166', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-196.html', 'title': 'N-196', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-114.html', 'title': 'N-114', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-699.html', 'title': 'N-699', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html', 'title': 'N-979', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-435.html', 'title': 'N-435', 'score': 0.9989685907443525}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-115.html', 'title': 'N-115', 'score': 0.9979929423249204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-927.html', 'title': 'N-927', 'score': 0.9979803459771059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-666.html', 'title': 'N-666', 'score': 0.9979062947010147}]
result = search.search('orange coconut papaya apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #69 checking search results for 'orange coconut papaya apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #69 checking search results for 'orange coconut papaya apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking search results for 'blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0059763991091016985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}]
result = search.search('blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #70 checking search results for 'blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #70 checking search results for 'blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking search results for 'blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 1.0}]
result = search.search('blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #71 checking search results for 'blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #71 checking search results for 'blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking search results for 'orange kiwi peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018028952630036073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01677841146370893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015407954972656731}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014990123972366678}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007612017304525094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007593883223287237}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00695093858299602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.006286382234528953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006171683220676471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.005378522404349503}]
result = search.search('orange kiwi peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #72 checking search results for 'orange kiwi peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #72 checking search results for 'orange kiwi peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking search results for 'orange kiwi peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-235.html', 'title': 'N-235', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-833.html', 'title': 'N-833', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-677.html', 'title': 'N-677', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html', 'title': 'N-456', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-866.html', 'title': 'N-866', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-423.html', 'title': 'N-423', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-480.html', 'title': 'N-480', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-49.html', 'title': 'N-49', 'score': 1.0}]
result = search.search('orange kiwi peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #73 checking search results for 'orange kiwi peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #73 checking search results for 'orange kiwi peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking search results for 'cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #74 checking search results for 'cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #74 checking search results for 'cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking search results for 'cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #75 checking search results for 'cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #75 checking search results for 'cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking search results for 'pear tomato orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01860545529731037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015568460904394859}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015403883530114038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.013110385528746564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007988311752363045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007846151567708575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007669575281321461}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.0073514637757687955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006557914662350003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('pear tomato orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #76 checking search results for 'pear tomato orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #76 checking search results for 'pear tomato orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking search results for 'pear tomato orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-674.html', 'title': 'N-674', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-235.html', 'title': 'N-235', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-148.html', 'title': 'N-148', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-646.html', 'title': 'N-646', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-902.html', 'title': 'N-902', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-952.html', 'title': 'N-952', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html', 'title': 'N-951', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-429.html', 'title': 'N-429', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-481.html', 'title': 'N-481', 'score': 1.0000000000000002}]
result = search.search('pear tomato orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #77 checking search results for 'pear tomato orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #77 checking search results for 'pear tomato orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking search results for 'tomato papaya kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01856817960587615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017779231822637978}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01631509609547916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015211625045033447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010468579745529744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008594587263382893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.00784840087232002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006583144879460788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005807288771427389}]
result = search.search('tomato papaya kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #78 checking search results for 'tomato papaya kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #78 checking search results for 'tomato papaya kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking search results for 'tomato papaya kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-303.html', 'title': 'N-303', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-608.html', 'title': 'N-608', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-446.html', 'title': 'N-446', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html', 'title': 'N-527', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-768.html', 'title': 'N-768', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-338.html', 'title': 'N-338', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-486.html', 'title': 'N-486', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-69.html', 'title': 'N-69', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-152.html', 'title': 'N-152', 'score': 1.0000000000000002}]
result = search.search('tomato papaya kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #79 checking search results for 'tomato papaya kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #79 checking search results for 'tomato papaya kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking search results for 'pear apricot coconut banana blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.016840206411182574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016364411714429865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01628161141313611}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015251789304138043}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008156721402116212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007793111077347532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007706911248997187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006515015959295654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005904639768866627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0055714107037769375}]
result = search.search('pear apricot coconut banana blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #80 checking search results for 'pear apricot coconut banana blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #80 checking search results for 'pear apricot coconut banana blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking search results for 'pear apricot coconut banana blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-602.html', 'title': 'N-602', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-498.html', 'title': 'N-498', 'score': 0.9987988496513063}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9979467063205739}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html', 'title': 'N-154', 'score': 0.997376797514596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-62.html', 'title': 'N-62', 'score': 0.9965946594810626}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-306.html', 'title': 'N-306', 'score': 0.9962367332689231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html', 'title': 'N-165', 'score': 0.9961612515149125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.9949904017901298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-647.html', 'title': 'N-647', 'score': 0.994736405508155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-766.html', 'title': 'N-766', 'score': 0.9947117224208428}]
result = search.search('pear apricot coconut banana blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #81 checking search results for 'pear apricot coconut banana blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #81 checking search results for 'pear apricot coconut banana blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking search results for 'pear apricot blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018053959266203734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016802090064049858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015118925671089127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.014536600861067131}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008778893486940904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007987156438700276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007828638669574974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006190961644559313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0061078503082408146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.005772304009997428}]
result = search.search('pear apricot blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #82 checking search results for 'pear apricot blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #82 checking search results for 'pear apricot blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking search results for 'pear apricot blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html', 'title': 'N-13', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-875.html', 'title': 'N-875', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-623.html', 'title': 'N-623', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-481.html', 'title': 'N-481', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-589.html', 'title': 'N-589', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-782.html', 'title': 'N-782', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-300.html', 'title': 'N-300', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-532.html', 'title': 'N-532', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-603.html', 'title': 'N-603', 'score': 1.0000000000000002}]
result = search.search('pear apricot blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #83 checking search results for 'pear apricot blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #83 checking search results for 'pear apricot blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking search results for 'kiwi papaya orange blueberry orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018079702728020425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.015970403401292375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013841517726998582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01352499000654755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007642643792419495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.006746539235386097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0059866243626392895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.005849654540776072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0056204243739460666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.005234587151990453}]
result = search.search('kiwi papaya orange blueberry orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #84 checking search results for 'kiwi papaya orange blueberry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #84 checking search results for 'kiwi papaya orange blueberry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking search results for 'kiwi papaya orange blueberry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-935.html', 'title': 'N-935', 'score': 0.9997191096554812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 0.9992342062939674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html', 'title': 'N-379', 'score': 0.9984411445393333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-160.html', 'title': 'N-160', 'score': 0.9977790745397522}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-218.html', 'title': 'N-218', 'score': 0.9977376799870871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-913.html', 'title': 'N-913', 'score': 0.9977308683975691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-992.html', 'title': 'N-992', 'score': 0.9968567759103434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-179.html', 'title': 'N-179', 'score': 0.9967438348857768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-650.html', 'title': 'N-650', 'score': 0.9964037689884276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-679.html', 'title': 'N-679', 'score': 0.9961606424413321}]
result = search.search('kiwi papaya orange blueberry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #85 checking search results for 'kiwi papaya orange blueberry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #85 checking search results for 'kiwi papaya orange blueberry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking search results for 'blueberry lime coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018040088528511578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017355601017897473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01682144511009028}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01545643124200263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008720494964259575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008105155864759905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.0074259246553566045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006505100522961969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0059741323784573645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005932959575717012}]
result = search.search('blueberry lime coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #86 checking search results for 'blueberry lime coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #86 checking search results for 'blueberry lime coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking search results for 'blueberry lime coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-317.html', 'title': 'N-317', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-807.html', 'title': 'N-807', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-324.html', 'title': 'N-324', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-302.html', 'title': 'N-302', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-320.html', 'title': 'N-320', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-935.html', 'title': 'N-935', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-461.html', 'title': 'N-461', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-619.html', 'title': 'N-619', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html', 'title': 'N-826', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-281.html', 'title': 'N-281', 'score': 1.0000000000000002}]
result = search.search('blueberry lime coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #87 checking search results for 'blueberry lime coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #87 checking search results for 'blueberry lime coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking search results for 'fig cherry coconut apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01805714404920478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017054878854468263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016543720702788988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01414729104292662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008382473742459585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007669995691044824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007625258043841251}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.0075620855464276935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0060093996302866695}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005954820979517153}]
result = search.search('fig cherry coconut apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #88 checking search results for 'fig cherry coconut apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #88 checking search results for 'fig cherry coconut apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking search results for 'fig cherry coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-319.html', 'title': 'N-319', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-575.html', 'title': 'N-575', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-172.html', 'title': 'N-172', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-558.html', 'title': 'N-558', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-762.html', 'title': 'N-762', 'score': 0.9980773879895452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-752.html', 'title': 'N-752', 'score': 0.9980458789952962}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9979568863092835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-656.html', 'title': 'N-656', 'score': 0.9977535721123807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-483.html', 'title': 'N-483', 'score': 0.9972877244641991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-776.html', 'title': 'N-776', 'score': 0.9972496613493702}]
result = search.search('fig cherry coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #89 checking search results for 'fig cherry coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #89 checking search results for 'fig cherry coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking search results for 'orange kiwi kiwi tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018597725168147727}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01647995522581073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015429994199579463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.012842160817725512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.00965210086770361}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008424270304485327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00752703298382273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006515792668101296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.005872512119317221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005597133599116016}]
result = search.search('orange kiwi kiwi tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #90 checking search results for 'orange kiwi kiwi tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #90 checking search results for 'orange kiwi kiwi tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking search results for 'orange kiwi kiwi tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-579.html', 'title': 'N-579', 'score': 0.9999960430512848}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 0.9999783642577996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-818.html', 'title': 'N-818', 'score': 0.9999702930611971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-225.html', 'title': 'N-225', 'score': 0.9999595255414705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html', 'title': 'N-415', 'score': 0.9999187172969177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-554.html', 'title': 'N-554', 'score': 0.9999052233000165}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-376.html', 'title': 'N-376', 'score': 0.9998909315710222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-242.html', 'title': 'N-242', 'score': 0.9998495595020983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-863.html', 'title': 'N-863', 'score': 0.9998290490456071}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-965.html', 'title': 'N-965', 'score': 0.9997523417865914}]
result = search.search('orange kiwi kiwi tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #91 checking search results for 'orange kiwi kiwi tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #91 checking search results for 'orange kiwi kiwi tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking search results for 'papaya lime lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.016935036787197308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016811990314156058}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015561183032402002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015445889136644195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010605038734437128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008440949225148526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007589697346587021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0067103580461998396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006385450844273902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006064430180960983}]
result = search.search('papaya lime lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #92 checking search results for 'papaya lime lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #92 checking search results for 'papaya lime lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking search results for 'papaya lime lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-417.html', 'title': 'N-417', 'score': 0.9999991198217356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-973.html', 'title': 'N-973', 'score': 0.9999984601758691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-698.html', 'title': 'N-698', 'score': 0.9999976334748873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-679.html', 'title': 'N-679', 'score': 0.9999965045495423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html', 'title': 'N-37', 'score': 0.9999949665055067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-776.html', 'title': 'N-776', 'score': 0.9999946611217129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-354.html', 'title': 'N-354', 'score': 0.9999932709530641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-936.html', 'title': 'N-936', 'score': 0.9999915642972284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-341.html', 'title': 'N-341', 'score': 0.9999894647775993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-844.html', 'title': 'N-844', 'score': 0.9999888675262525}]
result = search.search('papaya lime lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #93 checking search results for 'papaya lime lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #93 checking search results for 'papaya lime lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking search results for 'orange pear fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018502385358789813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016015447204301314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.014975647849421366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014888903379769699}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008605320849298105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007831637822887608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007796243205378934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006927200521860873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006560133404268173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005838621530969893}]
result = search.search('orange pear fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #94 checking search results for 'orange pear fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #94 checking search results for 'orange pear fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking search results for 'orange pear fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-292.html', 'title': 'N-292', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-714.html', 'title': 'N-714', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-208.html', 'title': 'N-208', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-944.html', 'title': 'N-944', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-350.html', 'title': 'N-350', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-505.html', 'title': 'N-505', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-310.html', 'title': 'N-310', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-834.html', 'title': 'N-834', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-688.html', 'title': 'N-688', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-523.html', 'title': 'N-523', 'score': 1.0000000000000002}]
result = search.search('orange pear fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #95 checking search results for 'orange pear fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #95 checking search results for 'orange pear fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking search results for 'fig tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01849818506465135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01676748542359117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015124780697016048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.013235403531305583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.01047428670193717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008181168187271427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007284338125666096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006619208394874289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005647163929064623}]
result = search.search('fig tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #96 checking search results for 'fig tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #96 checking search results for 'fig tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking search results for 'fig tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-608.html', 'title': 'N-608', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html', 'title': 'N-418', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-427.html', 'title': 'N-427', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-502.html', 'title': 'N-502', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-768.html', 'title': 'N-768', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-147.html', 'title': 'N-147', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-319.html', 'title': 'N-319', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-440.html', 'title': 'N-440', 'score': 1.0000000000000002}]
result = search.search('fig tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #97 checking search results for 'fig tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #97 checking search results for 'fig tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking search results for 'blueberry fig apple lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017702161944795042}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01669137271013427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016675184935679693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014402173627714374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00827602993020855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007467326316901416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007196326608786418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006787233409600938}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005770248961778094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005455507041900625}]
result = search.search('blueberry fig apple lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #98 checking search results for 'blueberry fig apple lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #98 checking search results for 'blueberry fig apple lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking search results for 'blueberry fig apple lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-267.html', 'title': 'N-267', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-421.html', 'title': 'N-421', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-551.html', 'title': 'N-551', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-172.html', 'title': 'N-172', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-511.html', 'title': 'N-511', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-53.html', 'title': 'N-53', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html', 'title': 'N-286', 'score': 0.9984253583141981}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-656.html', 'title': 'N-656', 'score': 0.9981295533188055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9979959814854462}]
result = search.search('blueberry fig apple lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #99 checking search results for 'blueberry fig apple lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #99 checking search results for 'blueberry fig apple lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking search results for 'tomato papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('tomato papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #100 checking search results for 'tomato papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #100 checking search results for 'tomato papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking search results for 'tomato papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 1.0}]
result = search.search('tomato papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #101 checking search results for 'tomato papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #101 checking search results for 'tomato papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking search results for 'kiwi lime tomato peach pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01804358924963029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016642017962658677}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015281652967871817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.012838338310932734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.009165110467956337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008332886351186527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007535049717451132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0073187767265125315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005855902935380046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005609041397586044}]
result = search.search('kiwi lime tomato peach pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #102 checking search results for 'kiwi lime tomato peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #102 checking search results for 'kiwi lime tomato peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking search results for 'kiwi lime tomato peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-921.html', 'title': 'N-921', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-959.html', 'title': 'N-959', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-2.html', 'title': 'N-2', 'score': 0.9981396503495484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-97.html', 'title': 'N-97', 'score': 0.9979358105740671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-519.html', 'title': 'N-519', 'score': 0.9974297985013248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-26.html', 'title': 'N-26', 'score': 0.9968942588913811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.9967553585610209}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-82.html', 'title': 'N-82', 'score': 0.9967068308212329}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-554.html', 'title': 'N-554', 'score': 0.9964938222879209}]
result = search.search('kiwi lime tomato peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #103 checking search results for 'kiwi lime tomato peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #103 checking search results for 'kiwi lime tomato peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking search results for 'banana cherry blueberry pear kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017181087456267622}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016397425951306395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015718714290066615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015246479377296037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00810430015915908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008086866277820211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007708298914622298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0064274531429452325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.00603494454892667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005582580728742852}]
result = search.search('banana cherry blueberry pear kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #104 checking search results for 'banana cherry blueberry pear kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #104 checking search results for 'banana cherry blueberry pear kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking search results for 'banana cherry blueberry pear kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-25.html', 'title': 'N-25', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-186.html', 'title': 'N-186', 'score': 0.9974704496413228}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html', 'title': 'N-614', 'score': 0.9962252583330635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html', 'title': 'N-13', 'score': 0.994799181076779}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-90.html', 'title': 'N-90', 'score': 0.9947665355997242}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 0.9944047083805484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-498.html', 'title': 'N-498', 'score': 0.9942752414986317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html', 'title': 'N-394', 'score': 0.9935414122818649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-469.html', 'title': 'N-469', 'score': 0.9928080505116398}]
result = search.search('banana cherry blueberry pear kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #105 checking search results for 'banana cherry blueberry pear kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #105 checking search results for 'banana cherry blueberry pear kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking search results for 'lime fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01656378033467055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015348505924967507}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01519048132851107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.01048904663368684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008505129405986682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007715739942728333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0065590720673769426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}]
result = search.search('lime fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #106 checking search results for 'lime fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #106 checking search results for 'lime fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking search results for 'lime fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-541.html', 'title': 'N-541', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-279.html', 'title': 'N-279', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-512.html', 'title': 'N-512', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-18.html', 'title': 'N-18', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html', 'title': 'N-996', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-213.html', 'title': 'N-213', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-356.html', 'title': 'N-356', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-366.html', 'title': 'N-366', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 1.0000000000000002}]
result = search.search('lime fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #107 checking search results for 'lime fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #107 checking search results for 'lime fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking search results for 'apricot apricot blueberry kiwi blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018340669151088274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015706489821834365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015255554658079913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.013368672042078771}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007846557372270255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007812159708662689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007021764379659115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006107339630043624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.005774321074237828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005425554055715127}]
result = search.search('apricot apricot blueberry kiwi blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #108 checking search results for 'apricot apricot blueberry kiwi blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #108 checking search results for 'apricot apricot blueberry kiwi blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking search results for 'apricot apricot blueberry kiwi blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-825.html', 'title': 'N-825', 'score': 0.9998747797208873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-125.html', 'title': 'N-125', 'score': 0.9997924478967433}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-489.html', 'title': 'N-489', 'score': 0.9997870990348792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-937.html', 'title': 'N-937', 'score': 0.9997860666144329}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-208.html', 'title': 'N-208', 'score': 0.9997782219206955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-480.html', 'title': 'N-480', 'score': 0.9997727843469766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-63.html', 'title': 'N-63', 'score': 0.9997629086347726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-421.html', 'title': 'N-421', 'score': 0.9997584125568992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-875.html', 'title': 'N-875', 'score': 0.9997464068267069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-777.html', 'title': 'N-777', 'score': 0.999742834136668}]
result = search.search('apricot apricot blueberry kiwi blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #109 checking search results for 'apricot apricot blueberry kiwi blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #109 checking search results for 'apricot apricot blueberry kiwi blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking search results for 'orange blueberry cherry papaya blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01749692965117352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016335604865148814}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.016046822836587035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015483124469788929}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008069988126889294}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.006508869629968592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.0061429180609039605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.00531059019260701}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0052335696973435705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.0051096291381231024}]
result = search.search('orange blueberry cherry papaya blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #110 checking search results for 'orange blueberry cherry papaya blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #110 checking search results for 'orange blueberry cherry papaya blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking search results for 'orange blueberry cherry papaya blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html', 'title': 'N-139', 'score': 0.9997739801899442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-945.html', 'title': 'N-945', 'score': 0.9997183935876665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-343.html', 'title': 'N-343', 'score': 0.9997183935876665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-885.html', 'title': 'N-885', 'score': 0.9997019004088131}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-166.html', 'title': 'N-166', 'score': 0.9996144833229775}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-603.html', 'title': 'N-603', 'score': 0.9995561325631792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.9993569434770196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-358.html', 'title': 'N-358', 'score': 0.9987172879360701}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-988.html', 'title': 'N-988', 'score': 0.9982592188716964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-883.html', 'title': 'N-883', 'score': 0.9977294098692897}]
result = search.search('orange blueberry cherry papaya blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #111 checking search results for 'orange blueberry cherry papaya blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #111 checking search results for 'orange blueberry cherry papaya blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking search results for 'kiwi fig papaya papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01771091690036741}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.014949375119659629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.013752363197631935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013370076335590241}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010988144555282329}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008168645783371745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007755619032946053}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007558810447002061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006221980007511243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006040680676646721}]
result = search.search('kiwi fig papaya papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #112 checking search results for 'kiwi fig papaya papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #112 checking search results for 'kiwi fig papaya papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking search results for 'kiwi fig papaya papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-435.html', 'title': 'N-435', 'score': 0.9999015562317972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-407.html', 'title': 'N-407', 'score': 0.9998834509807555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-872.html', 'title': 'N-872', 'score': 0.9997949911045745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.9997399186613879}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-434.html', 'title': 'N-434', 'score': 0.9996306422632708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-474.html', 'title': 'N-474', 'score': 0.999567277273574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.9995341038876765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-41.html', 'title': 'N-41', 'score': 0.9993765926752636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-214.html', 'title': 'N-214', 'score': 0.9993623868959817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-408.html', 'title': 'N-408', 'score': 0.9993113461237746}]
result = search.search('kiwi fig papaya papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #113 checking search results for 'kiwi fig papaya papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #113 checking search results for 'kiwi fig papaya papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking search results for 'cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #114 checking search results for 'cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #114 checking search results for 'cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking search results for 'cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #115 checking search results for 'cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #115 checking search results for 'cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking search results for 'apricot kiwi orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01675254512630167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016481518909712146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015361212887326331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014797458811379617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008314931070775036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007552554752427976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.0074444458819295616}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0069678556229123495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006344645258295445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006189281100796743}]
result = search.search('apricot kiwi orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #116 checking search results for 'apricot kiwi orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #116 checking search results for 'apricot kiwi orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking search results for 'apricot kiwi orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-757.html', 'title': 'N-757', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-235.html', 'title': 'N-235', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-821.html', 'title': 'N-821', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-677.html', 'title': 'N-677', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html', 'title': 'N-456', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-693.html', 'title': 'N-693', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-866.html', 'title': 'N-866', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-648.html', 'title': 'N-648', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-961.html', 'title': 'N-961', 'score': 1.0000000000000002}]
result = search.search('apricot kiwi orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #117 checking search results for 'apricot kiwi orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #117 checking search results for 'apricot kiwi orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking search results for 'blueberry banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.016694903324254037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016058478899224213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015451202277677916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008698911021167276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008069992927224478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0062848703477832195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.005446197209621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005423949332687883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html', 'title': 'N-80', 'score': 0.00519041795869891}]
result = search.search('blueberry banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #118 checking search results for 'blueberry banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #118 checking search results for 'blueberry banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking search results for 'blueberry banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-455.html', 'title': 'N-455', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-158.html', 'title': 'N-158', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-219.html', 'title': 'N-219', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-541.html', 'title': 'N-541', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-585.html', 'title': 'N-585', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-608.html', 'title': 'N-608', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-649.html', 'title': 'N-649', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-674.html', 'title': 'N-674', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html', 'title': 'N-527', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-556.html', 'title': 'N-556', 'score': 1.0}]
result = search.search('blueberry banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #119 checking search results for 'blueberry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #119 checking search results for 'blueberry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking search results for 'tomato lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('tomato lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #120 checking search results for 'tomato lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #120 checking search results for 'tomato lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking search results for 'tomato lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('tomato lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #121 checking search results for 'tomato lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #121 checking search results for 'tomato lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking search results for 'banana apple apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01817808275762968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017186685975450745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01649204733155145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013654156341594007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008714614853317818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007763316065126145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0077055756898049875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006337220684769914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.005598721906091317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005236941535991732}]
result = search.search('banana apple apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #122 checking search results for 'banana apple apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #122 checking search results for 'banana apple apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking search results for 'banana apple apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html', 'title': 'N-92', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-556.html', 'title': 'N-556', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-152.html', 'title': 'N-152', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-439.html', 'title': 'N-439', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-832.html', 'title': 'N-832', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-409.html', 'title': 'N-409', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-655.html', 'title': 'N-655', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-855.html', 'title': 'N-855', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-395.html', 'title': 'N-395', 'score': 1.0000000000000002}]
result = search.search('banana apple apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #123 checking search results for 'banana apple apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #123 checking search results for 'banana apple apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking search results for 'lime lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('lime lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #124 checking search results for 'lime lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #124 checking search results for 'lime lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking search results for 'lime lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('lime lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #125 checking search results for 'lime lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #125 checking search results for 'lime lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking search results for 'blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0059763991091016985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}]
result = search.search('blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #126 checking search results for 'blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #126 checking search results for 'blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking search results for 'blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 1.0}]
result = search.search('blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #127 checking search results for 'blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #127 checking search results for 'blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking search results for 'cherry peach blueberry fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017824410529992375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017491942304420537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01637054564333002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01506136046403492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007917520479384113}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007801896230617562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007090981932678284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0066680296040388535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006112072184442336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0059763991091017}]
result = search.search('cherry peach blueberry fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #128 checking search results for 'cherry peach blueberry fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #128 checking search results for 'cherry peach blueberry fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking search results for 'cherry peach blueberry fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-677.html', 'title': 'N-677', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-978.html', 'title': 'N-978', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-391.html', 'title': 'N-391', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-46.html', 'title': 'N-46', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9979658302608095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-770.html', 'title': 'N-770', 'score': 0.9978578385555356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-42.html', 'title': 'N-42', 'score': 0.9978108050009052}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-686.html', 'title': 'N-686', 'score': 0.9974626717704024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-886.html', 'title': 'N-886', 'score': 0.9972751037066792}]
result = search.search('cherry peach blueberry fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #129 checking search results for 'cherry peach blueberry fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #129 checking search results for 'cherry peach blueberry fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking search results for 'apricot peach blueberry coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017452196202013586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017218223109884908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016667754745387744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015422199152059396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00847038868572458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007764395707648053}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007127099807599033}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00667526704451898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006169983805535057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005266016929168967}]
result = search.search('apricot peach blueberry coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #130 checking search results for 'apricot peach blueberry coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #130 checking search results for 'apricot peach blueberry coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking search results for 'apricot peach blueberry coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-503.html', 'title': 'N-503', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-199.html', 'title': 'N-199', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-498.html', 'title': 'N-498', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-242.html', 'title': 'N-242', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html', 'title': 'N-327', 'score': 0.9988622810433537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-647.html', 'title': 'N-647', 'score': 0.9985063175387263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html', 'title': 'N-154', 'score': 0.9982062031270568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9980154075078714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html', 'title': 'N-83', 'score': 0.9972233624984683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-921.html', 'title': 'N-921', 'score': 0.9971509573624631}]
result = search.search('apricot peach blueberry coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #131 checking search results for 'apricot peach blueberry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #131 checking search results for 'apricot peach blueberry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking search results for 'apricot apple banana blueberry peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018071199604287613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017097743136715537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01619025587006804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01443254624089054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008698704731546358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007641459310252653}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006811844443300327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005565687591153619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005520289775107171}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.005367394405857192}]
result = search.search('apricot apple banana blueberry peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #132 checking search results for 'apricot apple banana blueberry peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #132 checking search results for 'apricot apple banana blueberry peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking search results for 'apricot apple banana blueberry peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9984644008640727}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-855.html', 'title': 'N-855', 'score': 0.997355456128525}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html', 'title': 'N-154', 'score': 0.9973518850270181}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html', 'title': 'N-268', 'score': 0.996993779959639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html', 'title': 'N-231', 'score': 0.9966257654117867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-967.html', 'title': 'N-967', 'score': 0.9966099351841806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-824.html', 'title': 'N-824', 'score': 0.9960736357911373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0.9958103766084929}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-152.html', 'title': 'N-152', 'score': 0.9957519795451188}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-41.html', 'title': 'N-41', 'score': 0.9946271129432164}]
result = search.search('apricot apple banana blueberry peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #133 checking search results for 'apricot apple banana blueberry peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #133 checking search results for 'apricot apple banana blueberry peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking search results for 'orange kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01771644836050181}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016120024153464734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01521054041859599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.014836395857320689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007810020720919612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00743545368202941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007255073099103813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0066462026602319224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006583063697079186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006171961682195481}]
result = search.search('orange kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #134 checking search results for 'orange kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #134 checking search results for 'orange kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking search results for 'orange kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-541.html', 'title': 'N-541', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html', 'title': 'N-24', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html', 'title': 'N-527', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-757.html', 'title': 'N-757', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-235.html', 'title': 'N-235', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-251.html', 'title': 'N-251', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-643.html', 'title': 'N-643', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-740.html', 'title': 'N-740', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-821.html', 'title': 'N-821', 'score': 1.0000000000000002}]
result = search.search('orange kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #135 checking search results for 'orange kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #135 checking search results for 'orange kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #136 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #136 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking search results for 'coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-158.html', 'title': 'N-158', 'score': 1.0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #137 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #137 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking search results for 'cherry tomato orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01779197330141248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015605960560212085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008237606375610877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007986022153300118}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007441567954506601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007152157124979696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0065574690607028505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0061702911575870255}]
result = search.search('cherry tomato orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #138 checking search results for 'cherry tomato orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #138 checking search results for 'cherry tomato orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking search results for 'cherry tomato orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-500.html', 'title': 'N-500', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html', 'title': 'N-614', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-292.html', 'title': 'N-292', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-791.html', 'title': 'N-791', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html', 'title': 'N-299', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-710.html', 'title': 'N-710', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html', 'title': 'N-151', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-409.html', 'title': 'N-409', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-749.html', 'title': 'N-749', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-811.html', 'title': 'N-811', 'score': 1.0000000000000002}]
result = search.search('cherry tomato orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #139 checking search results for 'cherry tomato orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #139 checking search results for 'cherry tomato orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking search results for 'coconut banana blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01843095342256337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01734089639160151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016150205037733747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015459097824865969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008267594702292554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007719017062636934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.006641571833722995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006177022616961499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005653464064762287}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.00542478613524092}]
result = search.search('coconut banana blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #140 checking search results for 'coconut banana blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #140 checking search results for 'coconut banana blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking search results for 'coconut banana blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-75.html', 'title': 'N-75', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-5.html', 'title': 'N-5', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html', 'title': 'N-530', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-455.html', 'title': 'N-455', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-479.html', 'title': 'N-479', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-302.html', 'title': 'N-302', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html', 'title': 'N-154', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-150.html', 'title': 'N-150', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-64.html', 'title': 'N-64', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html', 'title': 'N-380', 'score': 1.0000000000000002}]
result = search.search('coconut banana blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #141 checking search results for 'coconut banana blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #141 checking search results for 'coconut banana blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking search results for 'kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #142 checking search results for 'kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #142 checking search results for 'kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking search results for 'kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 1.0}]
result = search.search('kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #143 checking search results for 'kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #143 checking search results for 'kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking search results for 'banana blueberry cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01843095342256337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.016822852932887492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016357195904140642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015129111520025253}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008125041580152122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007659735869071143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.006641571833722995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006148071098415371}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.005992673672160885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005228111634906095}]
result = search.search('banana blueberry cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #144 checking search results for 'banana blueberry cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #144 checking search results for 'banana blueberry cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking search results for 'banana blueberry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-757.html', 'title': 'N-757', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-5.html', 'title': 'N-5', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-712.html', 'title': 'N-712', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-989.html', 'title': 'N-989', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-586.html', 'title': 'N-586', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-730.html', 'title': 'N-730', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-834.html', 'title': 'N-834', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-342.html', 'title': 'N-342', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-302.html', 'title': 'N-302', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-688.html', 'title': 'N-688', 'score': 1.0000000000000002}]
result = search.search('banana blueberry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #145 checking search results for 'banana blueberry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #145 checking search results for 'banana blueberry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.005378522404349503}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #146 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #146 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #147 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #147 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking search results for 'fig orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018498652510275358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018398734501200387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01603915337790284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014754656339609836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007846151567708575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.0076973361060651835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.0073514637757687955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006881785309950979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0065579146623500045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005637221492649537}]
result = search.search('fig orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #148 checking search results for 'fig orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #148 checking search results for 'fig orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking search results for 'fig orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-219.html', 'title': 'N-219', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-649.html', 'title': 'N-649', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html', 'title': 'N-24', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-242.html', 'title': 'N-242', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html', 'title': 'N-527', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-556.html', 'title': 'N-556', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-40.html', 'title': 'N-40', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-186.html', 'title': 'N-186', 'score': 1.0000000000000002}]
result = search.search('fig orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #149 checking search results for 'fig orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #149 checking search results for 'fig orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking search results for 'peach apricot pear pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.015913747728253564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015096364267010269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013500144501430247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01033025206992611}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.009435712444713015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008678148688829074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007256133744880059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006541306099051702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006113775654312274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005866513465813998}]
result = search.search('peach apricot pear pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #150 checking search results for 'peach apricot pear pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #150 checking search results for 'peach apricot pear pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking search results for 'peach apricot pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-186.html', 'title': 'N-186', 'score': 0.9996501963859599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-221.html', 'title': 'N-221', 'score': 0.9996391125067771}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-690.html', 'title': 'N-690', 'score': 0.9996088516327973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-630.html', 'title': 'N-630', 'score': 0.9995966867722395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-170.html', 'title': 'N-170', 'score': 0.9995894700607343}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-866.html', 'title': 'N-866', 'score': 0.9995894700607343}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-894.html', 'title': 'N-894', 'score': 0.9995037744808349}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-199.html', 'title': 'N-199', 'score': 0.9994801857920741}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-821.html', 'title': 'N-821', 'score': 0.9994585989430553}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-256.html', 'title': 'N-256', 'score': 0.9994585989430553}]
result = search.search('peach apricot pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #151 checking search results for 'peach apricot pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #151 checking search results for 'peach apricot pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #152 checking search results for 'orange banana fig apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018211480097290643}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017812536320357123}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016102501440325535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014121753629244975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007818774528878334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007532713664943745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00723556249578662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006042693029276133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.005532412143486647}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005237066657594905}]
result = search.search('orange banana fig apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #152 checking search results for 'orange banana fig apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #152 checking search results for 'orange banana fig apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #153 checking search results for 'orange banana fig apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-184.html', 'title': 'N-184', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-945.html', 'title': 'N-945', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-362.html', 'title': 'N-362', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-702.html', 'title': 'N-702', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-254.html', 'title': 'N-254', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-565.html', 'title': 'N-565', 'score': 0.9983655801802911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-260.html', 'title': 'N-260', 'score': 0.9979850796576105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-682.html', 'title': 'N-682', 'score': 0.9973163981248896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-119.html', 'title': 'N-119', 'score': 0.9968632043323549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html', 'title': 'N-24', 'score': 0.9963136462435253}]
result = search.search('orange banana fig apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #153 checking search results for 'orange banana fig apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #153 checking search results for 'orange banana fig apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking search results for 'papaya fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01836887615323217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016916930873335206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014759130498437193}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.0104658581649076}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008513027875913006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008180618936444051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007760674684138653}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0065577838755536515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.00570177532996004}]
result = search.search('papaya fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #154 checking search results for 'papaya fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #154 checking search results for 'papaya fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking search results for 'papaya fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html', 'title': 'N-609', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-649.html', 'title': 'N-649', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-899.html', 'title': 'N-899', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html', 'title': 'N-527', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-40.html', 'title': 'N-40', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-147.html', 'title': 'N-147', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-486.html', 'title': 'N-486', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-516.html', 'title': 'N-516', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-638.html', 'title': 'N-638', 'score': 1.0000000000000002}]
result = search.search('papaya fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #155 checking search results for 'papaya fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #155 checking search results for 'papaya fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking search results for 'banana orange apple fig blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018136605922804763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017387166662335852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01596892289424089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014366297568142455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.00786407454153847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007519132854135801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006487488224749542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005865065259779544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005368022540117588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005267714732332524}]
result = search.search('banana orange apple fig blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #156 checking search results for 'banana orange apple fig blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #156 checking search results for 'banana orange apple fig blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking search results for 'banana orange apple fig blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-362.html', 'title': 'N-362', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-967.html', 'title': 'N-967', 'score': 0.9960604418892771}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html', 'title': 'N-795', 'score': 0.9949016848193383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9947632235837502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html', 'title': 'N-154', 'score': 0.9947378026595989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-971.html', 'title': 'N-971', 'score': 0.99440436168789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-682.html', 'title': 'N-682', 'score': 0.9934229358109038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-878.html', 'title': 'N-878', 'score': 0.9932895433587693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 0.9932308711126743}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html', 'title': 'N-231', 'score': 0.9930382646512677}]
result = search.search('banana orange apple fig blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #157 checking search results for 'banana orange apple fig blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #157 checking search results for 'banana orange apple fig blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking search results for 'orange tomato fig cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01850329213064634}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.0173784445036419}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016027400834492722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014666659671041794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008232035977890684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007898952013050098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007676005405098414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007118310512810054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006560638398768591}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0058479197586655375}]
result = search.search('orange tomato fig cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #158 checking search results for 'orange tomato fig cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #158 checking search results for 'orange tomato fig cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking search results for 'orange tomato fig cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-189.html', 'title': 'N-189', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-292.html', 'title': 'N-292', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-945.html', 'title': 'N-945', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-153.html', 'title': 'N-153', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-49.html', 'title': 'N-49', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-344.html', 'title': 'N-344', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-714.html', 'title': 'N-714', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-781.html', 'title': 'N-781', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html', 'title': 'N-769', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-891.html', 'title': 'N-891', 'score': 1.0000000000000002}]
result = search.search('orange tomato fig cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #159 checking search results for 'orange tomato fig cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #159 checking search results for 'orange tomato fig cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking search results for 'tomato banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.005378522404349503}]
result = search.search('tomato banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #160 checking search results for 'tomato banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #160 checking search results for 'tomato banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking search results for 'tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #161 checking search results for 'tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #161 checking search results for 'tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking search results for 'cherry papaya pear peach blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017710759497427293}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016428326999417917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015600078179469375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014913752590379175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008365163692350701}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007995405631888858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007859697274293202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.0065007718633399636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005851073404067081}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.00550023393566536}]
result = search.search('cherry papaya pear peach blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #162 checking search results for 'cherry papaya pear peach blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #162 checking search results for 'cherry papaya pear peach blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking search results for 'cherry papaya pear peach blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-332.html', 'title': 'N-332', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-46.html', 'title': 'N-46', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9988267457607486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-770.html', 'title': 'N-770', 'score': 0.9981271821284614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.9974212340200346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html', 'title': 'N-140', 'score': 0.9972208286100597}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-492.html', 'title': 'N-492', 'score': 0.9965370185260679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-341.html', 'title': 'N-341', 'score': 0.9965078011445524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-647.html', 'title': 'N-647', 'score': 0.9961379450253408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0.9959990689832231}]
result = search.search('cherry papaya pear peach blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #163 checking search results for 'cherry papaya pear peach blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #163 checking search results for 'cherry papaya pear peach blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking search results for 'tomato pear pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016184087116355057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.015432409039974322}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015384156927729691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.009546945157862806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.00928026239505861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.0087464123087366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008255008574046827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006514901678444992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006472301265204004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0062592771542600775}]
result = search.search('tomato pear pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #164 checking search results for 'tomato pear pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #164 checking search results for 'tomato pear pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking search results for 'tomato pear pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-34.html', 'title': 'N-34', 'score': 0.9999934220105394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-383.html', 'title': 'N-383', 'score': 0.9999918596916473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-344.html', 'title': 'N-344', 'score': 0.9999644530476254}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-119.html', 'title': 'N-119', 'score': 0.9999122604078594}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-748.html', 'title': 'N-748', 'score': 0.9998972423582926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-598.html', 'title': 'N-598', 'score': 0.9998877492822766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-390.html', 'title': 'N-390', 'score': 0.9997614211563056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-563.html', 'title': 'N-563', 'score': 0.9997335490304131}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-703.html', 'title': 'N-703', 'score': 0.9997261489570805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-351.html', 'title': 'N-351', 'score': 0.9997104133357811}]
result = search.search('tomato pear pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #165 checking search results for 'tomato pear pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #165 checking search results for 'tomato pear pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0059763991091016985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #166 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #166 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #167 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #167 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #167 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking search results for 'lime fig papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01837746548066843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016548983055299595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.015275786330254275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015009690079844092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010613266874053283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008498856719664705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.00818469574751626}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007622016921192006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006569924285048918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005622648736085912}]
result = search.search('lime fig papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #168 checking search results for 'lime fig papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #168 checking search results for 'lime fig papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking search results for 'lime fig papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-993.html', 'title': 'N-993', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-213.html', 'title': 'N-213', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-673.html', 'title': 'N-673', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-363.html', 'title': 'N-363', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-617.html', 'title': 'N-617', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-478.html', 'title': 'N-478', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-775.html', 'title': 'N-775', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html', 'title': 'N-798', 'score': 1.0000000000000002}]
result = search.search('lime fig papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #169 checking search results for 'lime fig papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #169 checking search results for 'lime fig papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking search results for 'apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #170 checking search results for 'apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #170 checking search results for 'apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking search results for 'apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #171 checking search results for 'apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #171 checking search results for 'apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking search results for 'apple tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0059763991091016985}]
result = search.search('apple tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #172 checking search results for 'apple tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #172 checking search results for 'apple tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking search results for 'apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #173 checking search results for 'apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #173 checking search results for 'apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking search results for 'tomato banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.005378522404349503}]
result = search.search('tomato banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #174 checking search results for 'tomato banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #174 checking search results for 'tomato banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking search results for 'tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #175 checking search results for 'tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #175 checking search results for 'tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking search results for 'orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}]
result = search.search('orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #176 checking search results for 'orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #176 checking search results for 'orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking search results for 'orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #177 checking search results for 'orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #177 checking search results for 'orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking search results for 'apricot cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017827283954353675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014413379291093242}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010830960286352168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008128554092974197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007921573470605575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007539895840669397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006512528636033623}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006168120884373372}]
result = search.search('apricot cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #178 checking search results for 'apricot cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #178 checking search results for 'apricot cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking search results for 'apricot cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-351.html', 'title': 'N-351', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-509.html', 'title': 'N-509', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-899.html', 'title': 'N-899', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html', 'title': 'N-13', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-195.html', 'title': 'N-195', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-427.html', 'title': 'N-427', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-319.html', 'title': 'N-319', 'score': 1.0}]
result = search.search('apricot cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #179 checking search results for 'apricot cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #179 checking search results for 'apricot cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking search results for 'cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #180 checking search results for 'cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #180 checking search results for 'cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking search results for 'cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #181 checking search results for 'cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #181 checking search results for 'cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking search results for 'papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010993266275301729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}]
result = search.search('papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #182 checking search results for 'papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #182 checking search results for 'papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking search results for 'papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 1.0}]
result = search.search('papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #183 checking search results for 'papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #183 checking search results for 'papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking search results for 'peach kiwi apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018573249654530912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016852024327008337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01659098592989938}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014034153543564392}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008269313589056262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007596475836040287}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007017827152648008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0062864358590972004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.006171207397045928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.0059763991091017}]
result = search.search('peach kiwi apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #184 checking search results for 'peach kiwi apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #184 checking search results for 'peach kiwi apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking search results for 'peach kiwi apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html', 'title': 'N-609', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-833.html', 'title': 'N-833', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html', 'title': 'N-456', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-301.html', 'title': 'N-301', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-269.html', 'title': 'N-269', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-143.html', 'title': 'N-143', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-257.html', 'title': 'N-257', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-879.html', 'title': 'N-879', 'score': 1.0000000000000002}]
result = search.search('peach kiwi apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #185 checking search results for 'peach kiwi apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #185 checking search results for 'peach kiwi apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking search results for 'orange papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017987856620882155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017824962627894424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016024680327195485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007992048400248364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007847002935925197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.0077363230304852235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006624341646345239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006116208657602171}]
result = search.search('orange papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #186 checking search results for 'orange papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #186 checking search results for 'orange papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking search results for 'orange papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-402.html', 'title': 'N-402', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-524.html', 'title': 'N-524', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-649.html', 'title': 'N-649', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html', 'title': 'N-92', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-502.html', 'title': 'N-502', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html', 'title': 'N-527', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-531.html', 'title': 'N-531', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-757.html', 'title': 'N-757', 'score': 1.0}]
result = search.search('orange papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #187 checking search results for 'orange papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #187 checking search results for 'orange papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking search results for 'apricot banana pear cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.016682777762170198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016577339506084945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01567736668728298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014866544413770439}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.00937494372901481}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.00814394769898037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008013678558155256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007205263502879284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006505728898025247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005368300609181838}]
result = search.search('apricot banana pear cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #188 checking search results for 'apricot banana pear cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #188 checking search results for 'apricot banana pear cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking search results for 'apricot banana pear cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-832.html', 'title': 'N-832', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-137.html', 'title': 'N-137', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-57.html', 'title': 'N-57', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-576.html', 'title': 'N-576', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-679.html', 'title': 'N-679', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-875.html', 'title': 'N-875', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-734.html', 'title': 'N-734', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-806.html', 'title': 'N-806', 'score': 0.9986928130126921}]
result = search.search('apricot banana pear cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #189 checking search results for 'apricot banana pear cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #189 checking search results for 'apricot banana pear cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking search results for 'orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.018717687177453108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018605455297310367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016864305070550274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.015493087400703057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008749954127657852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008259637131598427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.00781543640833299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0066192083948742875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006286435859097199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005435059325662192}]
result = search.search('orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #190 checking search results for 'orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #190 checking search results for 'orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking search results for 'orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html', 'title': 'N-122', 'score': 1.0}]
result = search.search('orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #191 checking search results for 'orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #191 checking search results for 'orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking search results for 'coconut apple banana kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.018436160504405916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01716047230073481}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01623249288710549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014517753181100043}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007919117643216391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007842584931691907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007691719285076217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007601243823840943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005825754409870713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0054320745097817084}]
result = search.search('coconut apple banana kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #192 checking search results for 'coconut apple banana kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #192 checking search results for 'coconut apple banana kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking search results for 'coconut apple banana kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-784.html', 'title': 'N-784', 'score': 0.9979335864724723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-501.html', 'title': 'N-501', 'score': 0.9975244528502873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-804.html', 'title': 'N-804', 'score': 0.9974018727645799}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-216.html', 'title': 'N-216', 'score': 0.997292806165909}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html', 'title': 'N-253', 'score': 0.9967543923401553}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-148.html', 'title': 'N-148', 'score': 0.9964606276528569}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-95.html', 'title': 'N-95', 'score': 0.9961686629490769}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-902.html', 'title': 'N-902', 'score': 0.996115810470772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-878.html', 'title': 'N-878', 'score': 0.9956151135123633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-975.html', 'title': 'N-975', 'score': 0.9954485406547477}]
result = search.search('coconut apple banana kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #193 checking search results for 'coconut apple banana kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #193 checking search results for 'coconut apple banana kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking search results for 'apple banana lime apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017300619805966123}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01702162482765968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016459265112658605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01419671646007171}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008677587852484198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007851247681968194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007638093877129092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.0075707276301367355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005937143654429494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.005236161399893994}]
result = search.search('apple banana lime apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #194 checking search results for 'apple banana lime apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #194 checking search results for 'apple banana lime apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking search results for 'apple banana lime apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-184.html', 'title': 'N-184', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-260.html', 'title': 'N-260', 'score': 0.9986108913599487}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-846.html', 'title': 'N-846', 'score': 0.998591375248645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-801.html', 'title': 'N-801', 'score': 0.9982157118871954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-804.html', 'title': 'N-804', 'score': 0.998190380801599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html', 'title': 'N-83', 'score': 0.9979674809976987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-784.html', 'title': 'N-784', 'score': 0.9979446662621143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9978658011139467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html', 'title': 'N-795', 'score': 0.9978643306883035}]
result = search.search('apple banana lime apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #195 checking search results for 'apple banana lime apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #195 checking search results for 'apple banana lime apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking search results for 'papaya lime cherry peach apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017652498175278784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.016425831628959664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01634127617828069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01479018304769221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.00957152196847567}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007910638043709716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007789921462062859}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.007501500920613064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005849960405671419}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005717724302948147}]
result = search.search('papaya lime cherry peach apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #196 checking search results for 'papaya lime cherry peach apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #196 checking search results for 'papaya lime cherry peach apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking search results for 'papaya lime cherry peach apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-64.html', 'title': 'N-64', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-288.html', 'title': 'N-288', 'score': 0.9973020683224894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-938.html', 'title': 'N-938', 'score': 0.9966164169458489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-183.html', 'title': 'N-183', 'score': 0.9955405916424073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-944.html', 'title': 'N-944', 'score': 0.9951156223175295}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html', 'title': 'N-246', 'score': 0.9949606329765834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-45.html', 'title': 'N-45', 'score': 0.9949474037882559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-87.html', 'title': 'N-87', 'score': 0.9947584370106216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-686.html', 'title': 'N-686', 'score': 0.9945644493420874}]
result = search.search('papaya lime cherry peach apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #197 checking search results for 'papaya lime cherry peach apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #197 checking search results for 'papaya lime cherry peach apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking search results for 'apple peach cherry banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01833757954242184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017271409739837602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01669781868605785}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014977103518227513}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007918061459145673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006993113502323862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.006783251649527795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005578434256668219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.005303314989444937}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'title': 'N-70', 'score': 0.00524522394636229}]
result = search.search('apple peach cherry banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #198 checking search results for 'apple peach cherry banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #198 checking search results for 'apple peach cherry banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking search results for 'apple peach cherry banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-819.html', 'title': 'N-819', 'score': 0.9996912200903034}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-844.html', 'title': 'N-844', 'score': 0.9993496399485237}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-345.html', 'title': 'N-345', 'score': 0.9983285773111471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 0.9981242610590182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-408.html', 'title': 'N-408', 'score': 0.9976497881671946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-961.html', 'title': 'N-961', 'score': 0.9966987269410054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-289.html', 'title': 'N-289', 'score': 0.9965347355048735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-95.html', 'title': 'N-95', 'score': 0.9964630444613881}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-878.html', 'title': 'N-878', 'score': 0.9955444415660286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-279.html', 'title': 'N-279', 'score': 0.9950740772612103}]
result = search.search('apple peach cherry banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #199 checking search results for 'apple peach cherry banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #199 checking search results for 'apple peach cherry banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
