
import testingtools
import crawler
import searchdata
import search

output = open('fruits-search-failed.txt', 'w')
success_output = open('fruits-search-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html')



#Test #0 checking search results for 'coconut pear banana peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.016509358403014887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.013827357107386144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012636341448617349}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010376527825252458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008545578525200936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00807165991309894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007823836499624776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007350158592505641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007204525690690759}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006312883497876003}]
result = search.search('coconut pear banana peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #0 checking search results for 'coconut pear banana peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #0 checking search results for 'coconut pear banana peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking search results for 'coconut pear banana peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-371.html', 'title': 'N-371', 'score': 0.9999736712023327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-655.html', 'title': 'N-655', 'score': 0.9999705642860066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-271.html', 'title': 'N-271', 'score': 0.9999539190508948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-843.html', 'title': 'N-843', 'score': 0.9985167246424691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-801.html', 'title': 'N-801', 'score': 0.9978618483824403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-726.html', 'title': 'N-726', 'score': 0.997656244230465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-992.html', 'title': 'N-992', 'score': 0.9976431473943024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-284.html', 'title': 'N-284', 'score': 0.9972784363357068}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-852.html', 'title': 'N-852', 'score': 0.9970968732232205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-337.html', 'title': 'N-337', 'score': 0.9968140132875091}]
result = search.search('coconut pear banana peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #1 checking search results for 'coconut pear banana peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #1 checking search results for 'coconut pear banana peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking search results for 'coconut pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017612586755654788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01522047216337955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013209566400434174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010338178510317679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008485761736665385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008165272931566048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007801162471033136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0074674610757979945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007454976400150275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067306540297334405}]
result = search.search('coconut pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #2 checking search results for 'coconut pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #2 checking search results for 'coconut pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking search results for 'coconut pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html', 'title': 'N-231', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-725.html', 'title': 'N-725', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-654.html', 'title': 'N-654', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-187.html', 'title': 'N-187', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-333.html', 'title': 'N-333', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html', 'title': 'N-191', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html', 'title': 'N-84', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-421.html', 'title': 'N-421', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-211.html', 'title': 'N-211', 'score': 1.0000000000000002}]
result = search.search('coconut pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #3 checking search results for 'coconut pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #3 checking search results for 'coconut pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking search results for 'banana coconut pear tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018061848959776184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015102091987002318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.01326410473642593}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009874466377469563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008589336693142408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008205599403988857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007827657805594192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007500361356632108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007464000765966969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006732656533059661}]
result = search.search('banana coconut pear tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #4 checking search results for 'banana coconut pear tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #4 checking search results for 'banana coconut pear tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking search results for 'banana coconut pear tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html', 'title': 'N-191', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html', 'title': 'N-84', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-319.html', 'title': 'N-319', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-182.html', 'title': 'N-182', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-948.html', 'title': 'N-948', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-625.html', 'title': 'N-625', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-642.html', 'title': 'N-642', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-292.html', 'title': 'N-292', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html', 'title': 'N-424', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0}]
result = search.search('banana coconut pear tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #5 checking search results for 'banana coconut pear tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #5 checking search results for 'banana coconut pear tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking search results for 'peach coconut banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01994607735513016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015564031087860067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012376632176457953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009456655527164428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008407091337731298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007746725522498257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007642777291985349}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007176502495456643}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007123478471415808}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0066270101280618094}]
result = search.search('peach coconut banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #6 checking search results for 'peach coconut banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #6 checking search results for 'peach coconut banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking search results for 'peach coconut banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-648.html', 'title': 'N-648', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-168.html', 'title': 'N-168', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html', 'title': 'N-32', 'score': 0.9999121419714356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-18.html', 'title': 'N-18', 'score': 0.9998226140579269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-481.html', 'title': 'N-481', 'score': 0.9996754194686595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-934.html', 'title': 'N-934', 'score': 0.9996279835384627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html', 'title': 'N-266', 'score': 0.9995117583004987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-82.html', 'title': 'N-82', 'score': 0.9993971886805707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-365.html', 'title': 'N-365', 'score': 0.9993786819707889}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-301.html', 'title': 'N-301', 'score': 0.9993483685776405}]
result = search.search('peach coconut banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #7 checking search results for 'peach coconut banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #7 checking search results for 'peach coconut banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking search results for 'banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #8 checking search results for 'banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #8 checking search results for 'banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking search results for 'banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #9 checking search results for 'banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #9 checking search results for 'banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking search results for 'pear peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017357817777580588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015607807888514187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010421326325841602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873633543065484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082508053526444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007799885382063103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007470358888222107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('pear peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #10 checking search results for 'pear peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #10 checking search results for 'pear peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking search results for 'pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-167.html', 'title': 'N-167', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-19.html', 'title': 'N-19', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-574.html', 'title': 'N-574', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html', 'title': 'N-175', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0}]
result = search.search('pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #11 checking search results for 'pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #11 checking search results for 'pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking search results for 'pear pear peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015483813747218035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.013530675620676398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012890185264339264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009783454449821836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008594625705107722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00823116653794114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007735349761929931}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.00749698294673524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00718603289579419}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006511185004153496}]
result = search.search('pear pear peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #12 checking search results for 'pear pear peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #12 checking search results for 'pear pear peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking search results for 'pear pear peach tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-668.html', 'title': 'N-668', 'score': 0.999998143286198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-422.html', 'title': 'N-422', 'score': 0.9999980564161657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-251.html', 'title': 'N-251', 'score': 0.9999965720491021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-108.html', 'title': 'N-108', 'score': 0.9999942886472858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-789.html', 'title': 'N-789', 'score': 0.9999942886472858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-743.html', 'title': 'N-743', 'score': 0.99998062700091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-676.html', 'title': 'N-676', 'score': 0.99998062700091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-875.html', 'title': 'N-875', 'score': 0.9999698481197927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-617.html', 'title': 'N-617', 'score': 0.9999669703687809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html', 'title': 'N-48', 'score': 0.9999637703191423}]
result = search.search('pear pear peach tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #13 checking search results for 'pear pear peach tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #13 checking search results for 'pear pear peach tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking search results for 'pear coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017612586755654788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01522047216337955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013209566400434174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010338178510317679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008485761736665385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008165272931566048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007801162471033136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0074674610757979945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007454976400150275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067306540297334405}]
result = search.search('pear coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #14 checking search results for 'pear coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #14 checking search results for 'pear coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking search results for 'pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html', 'title': 'N-231', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-725.html', 'title': 'N-725', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-654.html', 'title': 'N-654', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-187.html', 'title': 'N-187', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-333.html', 'title': 'N-333', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html', 'title': 'N-191', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html', 'title': 'N-84', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-421.html', 'title': 'N-421', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-211.html', 'title': 'N-211', 'score': 1.0000000000000002}]
result = search.search('pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #15 checking search results for 'pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #15 checking search results for 'pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking search results for 'tomato apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('tomato apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #16 checking search results for 'tomato apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #16 checking search results for 'tomato apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking search results for 'tomato apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('tomato apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #17 checking search results for 'tomato apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #17 checking search results for 'tomato apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking search results for 'tomato apple peach banana pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018509963353474417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.0153467118745537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013368782359895911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010262630721324151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008640170335869514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008274019188378915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007948399497703151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007845312095231207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007356090445038331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067364556205215375}]
result = search.search('tomato apple peach banana pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #18 checking search results for 'tomato apple peach banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #18 checking search results for 'tomato apple peach banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking search results for 'tomato apple peach banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-356.html', 'title': 'N-356', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html', 'title': 'N-634', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-107.html', 'title': 'N-107', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-474.html', 'title': 'N-474', 'score': 0.9995101044564217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-962.html', 'title': 'N-962', 'score': 0.9994867099266312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-724.html', 'title': 'N-724', 'score': 0.9993385585001612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-649.html', 'title': 'N-649', 'score': 0.999326043630303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-450.html', 'title': 'N-450', 'score': 0.9992399865805257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-468.html', 'title': 'N-468', 'score': 0.999221546228397}]
result = search.search('tomato apple peach banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #19 checking search results for 'tomato apple peach banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #19 checking search results for 'tomato apple peach banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking search results for 'pear coconut coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020049209956188106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.013610580437936325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013302372524944373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009515169184555328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007833838538538033}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007464103938259431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007429456298108799}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0068785848584276095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.006366159257794746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006304171346283819}]
result = search.search('pear coconut coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #20 checking search results for 'pear coconut coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #20 checking search results for 'pear coconut coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking search results for 'pear coconut coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-720.html', 'title': 'N-720', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-712.html', 'title': 'N-712', 'score': 0.9999989887257262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-195.html', 'title': 'N-195', 'score': 0.9999978958869387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-499.html', 'title': 'N-499', 'score': 0.9999674677139083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-872.html', 'title': 'N-872', 'score': 0.9999653561666783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-418.html', 'title': 'N-418', 'score': 0.9999647453940204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-568.html', 'title': 'N-568', 'score': 0.9999615021982693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html', 'title': 'N-381', 'score': 0.9999504290442802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-906.html', 'title': 'N-906', 'score': 0.9999504290442802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html', 'title': 'N-711', 'score': 0.9999504290442802}]
result = search.search('pear coconut coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #21 checking search results for 'pear coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #21 checking search results for 'pear coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking search results for 'tomato pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017694858885956694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015604730243977091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010291542174032615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00847983244606652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008316652066202192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008032820186304992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007864900509665608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007461735571723743}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006745005899958887}]
result = search.search('tomato pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #22 checking search results for 'tomato pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #22 checking search results for 'tomato pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking search results for 'tomato pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html', 'title': 'N-266', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-854.html', 'title': 'N-854', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-877.html', 'title': 'N-877', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-108.html', 'title': 'N-108', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-162.html', 'title': 'N-162', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-380.html', 'title': 'N-380', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-449.html', 'title': 'N-449', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-180.html', 'title': 'N-180', 'score': 1.0000000000000002}]
result = search.search('tomato pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #23 checking search results for 'tomato pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #23 checking search results for 'tomato pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking search results for 'banana coconut pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018061848959776184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015102091987002318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.01326410473642593}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009874466377469563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008589336693142408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008205599403988857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007827657805594192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007500361356632108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007464000765966969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006732656533059661}]
result = search.search('banana coconut pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #24 checking search results for 'banana coconut pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #24 checking search results for 'banana coconut pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking search results for 'banana coconut pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html', 'title': 'N-191', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html', 'title': 'N-84', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-319.html', 'title': 'N-319', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-182.html', 'title': 'N-182', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-948.html', 'title': 'N-948', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-625.html', 'title': 'N-625', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-642.html', 'title': 'N-642', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-292.html', 'title': 'N-292', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html', 'title': 'N-424', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0}]
result = search.search('banana coconut pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #25 checking search results for 'banana coconut pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #25 checking search results for 'banana coconut pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #26 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #26 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #27 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #27 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking search results for 'tomato apple peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02012351132104801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015046801279986971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012830296506182757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00970505373424281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540263121281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007703765613239393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007699410752392975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007535517787028269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006600133869058213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006340808556510877}]
result = search.search('tomato apple peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #28 checking search results for 'tomato apple peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #28 checking search results for 'tomato apple peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking search results for 'tomato apple peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-627.html', 'title': 'N-627', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-213.html', 'title': 'N-213', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.9999999998713559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-395.html', 'title': 'N-395', 'score': 0.9999990672651214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-150.html', 'title': 'N-150', 'score': 0.9999953367411912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-869.html', 'title': 'N-869', 'score': 0.9999801796853832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-220.html', 'title': 'N-220', 'score': 0.9999763142935356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-161.html', 'title': 'N-161', 'score': 0.9999545499882428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-538.html', 'title': 'N-538', 'score': 0.9999468732636774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-830.html', 'title': 'N-830', 'score': 0.9999468732636774}]
result = search.search('tomato apple peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #29 checking search results for 'tomato apple peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #29 checking search results for 'tomato apple peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking search results for 'coconut tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('coconut tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #30 checking search results for 'coconut tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #30 checking search results for 'coconut tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking search results for 'coconut tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('coconut tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #31 checking search results for 'coconut tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #31 checking search results for 'coconut tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking search results for 'banana banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.016645835334778227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014202454281708606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013114474269722435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010418458391320272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008672275451790638}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008249015086348073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007982182796674214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007441895882017828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007376955261597488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006351850059212707}]
result = search.search('banana banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #32 checking search results for 'banana banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #32 checking search results for 'banana banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking search results for 'banana banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-272.html', 'title': 'N-272', 'score': 0.9999999464266566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-106.html', 'title': 'N-106', 'score': 0.9999998319662391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-756.html', 'title': 'N-756', 'score': 0.9999982101507203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-51.html', 'title': 'N-51', 'score': 0.9999979224794264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-703.html', 'title': 'N-703', 'score': 0.999997868201908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-72.html', 'title': 'N-72', 'score': 0.9999940733197302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'title': 'N-433', 'score': 0.9999920973204464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-606.html', 'title': 'N-606', 'score': 0.9999883030844956}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-794.html', 'title': 'N-794', 'score': 0.9999851087204675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-699.html', 'title': 'N-699', 'score': 0.999982577785459}]
result = search.search('banana banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #33 checking search results for 'banana banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #33 checking search results for 'banana banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking search results for 'coconut coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('coconut coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #34 checking search results for 'coconut coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #34 checking search results for 'coconut coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking search results for 'coconut coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('coconut coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #35 checking search results for 'coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #35 checking search results for 'coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking search results for 'banana coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019386170431275697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015687495981135793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013304222075628777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009790379375721218}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00847195213430452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008172606490007742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00784492964762584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007528766580063459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007216021398566428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006761578978050135}]
result = search.search('banana coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #36 checking search results for 'banana coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #36 checking search results for 'banana coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking search results for 'banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-113.html', 'title': 'N-113', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-141.html', 'title': 'N-141', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html', 'title': 'N-84', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-319.html', 'title': 'N-319', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-435.html', 'title': 'N-435', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-389.html', 'title': 'N-389', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-400.html', 'title': 'N-400', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-639.html', 'title': 'N-639', 'score': 1.0}]
result = search.search('banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #37 checking search results for 'banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #37 checking search results for 'banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking search results for 'pear apple banana apple tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02031340886347504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.0147025913745427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.0126581625012859}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009859539650311389}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00799477496618657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007653370329419675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007526107310334177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007500712842772985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.0074015575542838935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006400074301314018}]
result = search.search('pear apple banana apple tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #38 checking search results for 'pear apple banana apple tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #38 checking search results for 'pear apple banana apple tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking search results for 'pear apple banana apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-715.html', 'title': 'N-715', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-166.html', 'title': 'N-166', 'score': 0.999994019451666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-524.html', 'title': 'N-524', 'score': 0.9999707685472187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-215.html', 'title': 'N-215', 'score': 0.9999610384457982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9999542416305387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9999542416305387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-679.html', 'title': 'N-679', 'score': 0.999918393451175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html', 'title': 'N-133', 'score': 0.9996699101744082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-330.html', 'title': 'N-330', 'score': 0.9994731189319831}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-28.html', 'title': 'N-28', 'score': 0.9992834778642036}]
result = search.search('pear apple banana apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #39 checking search results for 'pear apple banana apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #39 checking search results for 'pear apple banana apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking search results for 'banana banana banana peach pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.015246129647551777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012385688613790734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.012265039002134177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010188018457045728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00812559146888124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007692170687375088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007664879171096069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.006975542144816207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006758567159995283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0058177241569886805}]
result = search.search('banana banana banana peach pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #40 checking search results for 'banana banana banana peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #40 checking search results for 'banana banana banana peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking search results for 'banana banana banana peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-932.html', 'title': 'N-932', 'score': 0.9999074611564566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-313.html', 'title': 'N-313', 'score': 0.999713663794288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-74.html', 'title': 'N-74', 'score': 0.9990201032245717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-297.html', 'title': 'N-297', 'score': 0.9988245560994978}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-113.html', 'title': 'N-113', 'score': 0.9983762203614207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-64.html', 'title': 'N-64', 'score': 0.9983753913257609}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-638.html', 'title': 'N-638', 'score': 0.9983592239575432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-599.html', 'title': 'N-599', 'score': 0.9973437606585863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-784.html', 'title': 'N-784', 'score': 0.9972606141379652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-386.html', 'title': 'N-386', 'score': 0.9972116584914668}]
result = search.search('banana banana banana peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #41 checking search results for 'banana banana banana peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #41 checking search results for 'banana banana banana peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #42 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #42 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #43 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #43 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking search results for 'apple banana pear tomato coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018579978788573117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01524387962526817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013262069848873594}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010011579607311036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008471085321040446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008221212826854564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007843074832044569}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00759643936001875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007350953117926903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006739343921847376}]
result = search.search('apple banana pear tomato coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #44 checking search results for 'apple banana pear tomato coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #44 checking search results for 'apple banana pear tomato coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking search results for 'apple banana pear tomato coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-319.html', 'title': 'N-319', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html', 'title': 'N-84', 'score': 0.9996448826208715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-349.html', 'title': 'N-349', 'score': 0.999508222227858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-244.html', 'title': 'N-244', 'score': 0.9992328579973419}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-293.html', 'title': 'N-293', 'score': 0.9992099848685586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-112.html', 'title': 'N-112', 'score': 0.9991374609126861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-450.html', 'title': 'N-450', 'score': 0.998954737227604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-108.html', 'title': 'N-108', 'score': 0.9988425397485641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-986.html', 'title': 'N-986', 'score': 0.9987609571242075}]
result = search.search('apple banana pear tomato coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #45 checking search results for 'apple banana pear tomato coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #45 checking search results for 'apple banana pear tomato coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #46 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #46 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #47 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #47 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #48 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #48 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #49 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #49 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking search results for 'coconut apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02099492456728733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015529043119114919}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013209566400434174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009942990587172044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008131792895327405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007873171422909615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007454976400150275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0072315231468739844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006759252110879896}]
result = search.search('coconut apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #50 checking search results for 'coconut apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #50 checking search results for 'coconut apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking search results for 'coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-143.html', 'title': 'N-143', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-985.html', 'title': 'N-985', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-65.html', 'title': 'N-65', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-382.html', 'title': 'N-382', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html', 'title': 'N-658', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-626.html', 'title': 'N-626', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-375.html', 'title': 'N-375', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-743.html', 'title': 'N-743', 'score': 1.0000000000000002}]
result = search.search('coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #51 checking search results for 'coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #51 checking search results for 'coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking search results for 'coconut tomato apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02099492456728733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015529043119114919}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013209566400434176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009942990587172044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00887554026426307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008131792895327405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007873171422909617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007454976400150275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007231523146873985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006759252110879896}]
result = search.search('coconut tomato apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #52 checking search results for 'coconut tomato apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #52 checking search results for 'coconut tomato apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking search results for 'coconut tomato apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-334.html', 'title': 'N-334', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html', 'title': 'N-472', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-601.html', 'title': 'N-601', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-741.html', 'title': 'N-741', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-257.html', 'title': 'N-257', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-545.html', 'title': 'N-545', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-728.html', 'title': 'N-728', 'score': 1.0000000000000002}]
result = search.search('coconut tomato apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #53 checking search results for 'coconut tomato apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #53 checking search results for 'coconut tomato apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking search results for 'peach apple apple coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020092649735590815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.0152211695830164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012300790611634851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010294863767775227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008262301361029144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007776288076336986}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00768532930392718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007553694679155103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007386172219252567}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00641172855570917}]
result = search.search('peach apple apple coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #54 checking search results for 'peach apple apple coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #54 checking search results for 'peach apple apple coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking search results for 'peach apple apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-756.html', 'title': 'N-756', 'score': 0.9999102306724789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.9998847678190135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-529.html', 'title': 'N-529', 'score': 0.999861395445023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-271.html', 'title': 'N-271', 'score': 0.999861395445023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-393.html', 'title': 'N-393', 'score': 0.9998270372698271}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-40.html', 'title': 'N-40', 'score': 0.999804852726478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-461.html', 'title': 'N-461', 'score': 0.9990531467726993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-186.html', 'title': 'N-186', 'score': 0.9989402800053807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-921.html', 'title': 'N-921', 'score': 0.9986094579318298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-405.html', 'title': 'N-405', 'score': 0.9984529150696058}]
result = search.search('peach apple apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #55 checking search results for 'peach apple apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #55 checking search results for 'peach apple apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking search results for 'pear apple peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019178513309742618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014720462919386789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.0128228785868486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00987180736666412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008482622488578007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007738243476914323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007694959288013001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007621763880118829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006617085377757683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006523509573146741}]
result = search.search('pear apple peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #56 checking search results for 'pear apple peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #56 checking search results for 'pear apple peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking search results for 'pear apple peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-213.html', 'title': 'N-213', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-759.html', 'title': 'N-759', 'score': 0.9997880897528203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-378.html', 'title': 'N-378', 'score': 0.9996641713649298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-279.html', 'title': 'N-279', 'score': 0.9991618961735397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html', 'title': 'N-710', 'score': 0.9991540677820615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-493.html', 'title': 'N-493', 'score': 0.999069350131578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-319.html', 'title': 'N-319', 'score': 0.9989499068554824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-869.html', 'title': 'N-869', 'score': 0.9989303222585132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-86.html', 'title': 'N-86', 'score': 0.9987125427760603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-793.html', 'title': 'N-793', 'score': 0.9986186882650856}]
result = search.search('pear apple peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #57 checking search results for 'pear apple peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #57 checking search results for 'pear apple peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking search results for 'coconut peach pear tomato apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019257101675164628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015444977005299426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013229096104769723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.01016250303163708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008490808618097864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008189235276864132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007833173231455819}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.0077075001419442705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007290052384247568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006737451812099052}]
result = search.search('coconut peach pear tomato apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #58 checking search results for 'coconut peach pear tomato apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #58 checking search results for 'coconut peach pear tomato apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking search results for 'coconut peach pear tomato apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-986.html', 'title': 'N-986', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-268.html', 'title': 'N-268', 'score': 0.9997510597235431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html', 'title': 'N-54', 'score': 0.9996929504182708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-656.html', 'title': 'N-656', 'score': 0.9996082987253341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-539.html', 'title': 'N-539', 'score': 0.9993905110899108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-898.html', 'title': 'N-898', 'score': 0.9993373233224636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-454.html', 'title': 'N-454', 'score': 0.9992854717804709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-450.html', 'title': 'N-450', 'score': 0.9992654885608953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-914.html', 'title': 'N-914', 'score': 0.9992651032857025}]
result = search.search('coconut peach pear tomato apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #59 checking search results for 'coconut peach pear tomato apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #59 checking search results for 'coconut peach pear tomato apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #60 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #60 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #61 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #61 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking search results for 'banana peach coconut tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019723573518688434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015488186567516545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013267025586949407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009943142311040737}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008579544461662461}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008196846883842075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00784887924147178}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007527958956223872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.0074293891148829545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006734565764473395}]
result = search.search('banana peach coconut tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #62 checking search results for 'banana peach coconut tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #62 checking search results for 'banana peach coconut tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking search results for 'banana peach coconut tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-40.html', 'title': 'N-40', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-219.html', 'title': 'N-219', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-357.html', 'title': 'N-357', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-388.html', 'title': 'N-388', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html', 'title': 'N-48', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-849.html', 'title': 'N-849', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-547.html', 'title': 'N-547', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-274.html', 'title': 'N-274', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-428.html', 'title': 'N-428', 'score': 1.0}]
result = search.search('banana peach coconut tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #63 checking search results for 'banana peach coconut tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #63 checking search results for 'banana peach coconut tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking search results for 'pear coconut tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015689888401003903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.013764435102076478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012095145632340942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010380768734506865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008874228466458281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008286532930387995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007991601838242188}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.00749250631780861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007165624914491778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00664671141451962}]
result = search.search('pear coconut tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #64 checking search results for 'pear coconut tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #64 checking search results for 'pear coconut tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking search results for 'pear coconut tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html', 'title': 'N-37', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-448.html', 'title': 'N-448', 'score': 0.9999966356575587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-675.html', 'title': 'N-675', 'score': 0.9999966356575587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-875.html', 'title': 'N-875', 'score': 0.9999669029221905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html', 'title': 'N-48', 'score': 0.9999602275432036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-142.html', 'title': 'N-142', 'score': 0.9999568613477141}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 0.9999390113125309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-400.html', 'title': 'N-400', 'score': 0.9999390113125309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-428.html', 'title': 'N-428', 'score': 0.9999390113125309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html', 'title': 'N-275', 'score': 0.9999390113125309}]
result = search.search('pear coconut tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #65 checking search results for 'pear coconut tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #65 checking search results for 'pear coconut tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking search results for 'pear peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017357817777580588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015607807888514187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010421326325841602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873633543065484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082508053526444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007799885382063103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007470358888222107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('pear peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #66 checking search results for 'pear peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #66 checking search results for 'pear peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking search results for 'pear peach tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-167.html', 'title': 'N-167', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-19.html', 'title': 'N-19', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-574.html', 'title': 'N-574', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html', 'title': 'N-175', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0}]
result = search.search('pear peach tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #67 checking search results for 'pear peach tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #67 checking search results for 'pear peach tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking search results for 'coconut pear pear tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015689888401003903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.013764435102076478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012095145632340942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010380768734506865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008874228466458281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008286532930387995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007991601838242188}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.00749250631780861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007165624914491778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00664671141451962}]
result = search.search('coconut pear pear tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #68 checking search results for 'coconut pear pear tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #68 checking search results for 'coconut pear pear tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking search results for 'coconut pear pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html', 'title': 'N-37', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-448.html', 'title': 'N-448', 'score': 0.9999966356575587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-675.html', 'title': 'N-675', 'score': 0.9999966356575587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-875.html', 'title': 'N-875', 'score': 0.9999669029221905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html', 'title': 'N-48', 'score': 0.9999602275432036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-142.html', 'title': 'N-142', 'score': 0.9999568613477141}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 0.9999390113125309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-400.html', 'title': 'N-400', 'score': 0.9999390113125309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-428.html', 'title': 'N-428', 'score': 0.9999390113125309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html', 'title': 'N-275', 'score': 0.9999390113125309}]
result = search.search('coconut pear pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #69 checking search results for 'coconut pear pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #69 checking search results for 'coconut pear pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking search results for 'coconut pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017612586755654788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01522047216337955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013209566400434174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010338178510317679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008485761736665385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008165272931566048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007801162471033136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0074674610757979945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007454976400150275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067306540297334405}]
result = search.search('coconut pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #70 checking search results for 'coconut pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #70 checking search results for 'coconut pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking search results for 'coconut pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html', 'title': 'N-231', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-725.html', 'title': 'N-725', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-654.html', 'title': 'N-654', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-187.html', 'title': 'N-187', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-333.html', 'title': 'N-333', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html', 'title': 'N-191', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html', 'title': 'N-84', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-421.html', 'title': 'N-421', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-211.html', 'title': 'N-211', 'score': 1.0000000000000002}]
result = search.search('coconut pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #71 checking search results for 'coconut pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #71 checking search results for 'coconut pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking search results for 'apple coconut tomato coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02015287110693174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014261496771611308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013286902337800425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00863077669684834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008519564734648974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0077121089260149215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007314065442605547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00643842580861136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006328732645682908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.006317233230409855}]
result = search.search('apple coconut tomato coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #72 checking search results for 'apple coconut tomato coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #72 checking search results for 'apple coconut tomato coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking search results for 'apple coconut tomato coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-699.html', 'title': 'N-699', 'score': 0.9999998385035237}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-491.html', 'title': 'N-491', 'score': 0.9999941069010598}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-676.html', 'title': 'N-676', 'score': 0.9999900920471041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-247.html', 'title': 'N-247', 'score': 0.9999890913437941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 0.9999780995437946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-67.html', 'title': 'N-67', 'score': 0.9999506884629724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html', 'title': 'N-81', 'score': 0.9999485650910355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html', 'title': 'N-444', 'score': 0.9999355695900428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-650.html', 'title': 'N-650', 'score': 0.999928954438621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html', 'title': 'N-233', 'score': 0.9999169434887949}]
result = search.search('apple coconut tomato coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #73 checking search results for 'apple coconut tomato coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #73 checking search results for 'apple coconut tomato coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking search results for 'pear tomato pear peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01550959481482795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.014887096274117355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012263870567490853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009891463328438918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008604561229578497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008232164150490238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007678881883097347}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007471518187807396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007134939594591021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006528024302606447}]
result = search.search('pear tomato pear peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #74 checking search results for 'pear tomato pear peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #74 checking search results for 'pear tomato pear peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking search results for 'pear tomato pear peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-875.html', 'title': 'N-875', 'score': 0.9999981046857743}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html', 'title': 'N-48', 'score': 0.9999959488974409}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-428.html', 'title': 'N-428', 'score': 0.9999860033474801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-547.html', 'title': 'N-547', 'score': 0.9999725231662807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-351.html', 'title': 'N-351', 'score': 0.9999649492167516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-529.html', 'title': 'N-529', 'score': 0.9999570059657631}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-847.html', 'title': 'N-847', 'score': 0.9999504574836089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-90.html', 'title': 'N-90', 'score': 0.9999404152895602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-294.html', 'title': 'N-294', 'score': 0.9997987200485394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-321.html', 'title': 'N-321', 'score': 0.9997841848972151}]
result = search.search('pear tomato pear peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #75 checking search results for 'pear tomato pear peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #75 checking search results for 'pear tomato pear peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking search results for 'tomato pear peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017357817777580588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015607807888514187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010421326325841602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873633543065484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082508053526444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007799885382063103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007470358888222107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('tomato pear peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #76 checking search results for 'tomato pear peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #76 checking search results for 'tomato pear peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking search results for 'tomato pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-167.html', 'title': 'N-167', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-19.html', 'title': 'N-19', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-574.html', 'title': 'N-574', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html', 'title': 'N-175', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0}]
result = search.search('tomato pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #77 checking search results for 'tomato pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #77 checking search results for 'tomato pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking search results for 'tomato apple pear tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018655248015394157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015606802545382766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010337987121389246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00857805234054004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008256486368199202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008032820186304992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007832925829165897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007335932292012037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00674697588534384}]
result = search.search('tomato apple pear tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #78 checking search results for 'tomato apple pear tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #78 checking search results for 'tomato apple pear tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking search results for 'tomato apple pear tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-354.html', 'title': 'N-354', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-967.html', 'title': 'N-967', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-268.html', 'title': 'N-268', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-986.html', 'title': 'N-986', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-356.html', 'title': 'N-356', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-179.html', 'title': 'N-179', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html', 'title': 'N-634', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-649.html', 'title': 'N-649', 'score': 1.0}]
result = search.search('tomato apple pear tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #79 checking search results for 'tomato apple pear tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #79 checking search results for 'tomato apple pear tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking search results for 'tomato pear peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017357817777580588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015607807888514187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010421326325841602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873633543065484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082508053526444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007799885382063103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007470358888222107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('tomato pear peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #80 checking search results for 'tomato pear peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #80 checking search results for 'tomato pear peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking search results for 'tomato pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-167.html', 'title': 'N-167', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-19.html', 'title': 'N-19', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-574.html', 'title': 'N-574', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html', 'title': 'N-175', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0}]
result = search.search('tomato pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #81 checking search results for 'tomato pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #81 checking search results for 'tomato pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking search results for 'tomato banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('tomato banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #82 checking search results for 'tomato banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #82 checking search results for 'tomato banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking search results for 'tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #83 checking search results for 'tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #83 checking search results for 'tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking search results for 'pear pear banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017446203598850178}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698366356233846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012610530152803749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009008509779098822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008456910680346473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007974608595950831}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0074608759752728135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007375542340917642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007286046737521122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006637036671776635}]
result = search.search('pear pear banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #84 checking search results for 'pear pear banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #84 checking search results for 'pear pear banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking search results for 'pear pear banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-559.html', 'title': 'N-559', 'score': 0.9999999190187754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.9999993518313642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-50.html', 'title': 'N-50', 'score': 0.999998780324474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-661.html', 'title': 'N-661', 'score': 0.9999975925022976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-436.html', 'title': 'N-436', 'score': 0.9999949554941471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-908.html', 'title': 'N-908', 'score': 0.9999867702112808}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-17.html', 'title': 'N-17', 'score': 0.9999668459684256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-619.html', 'title': 'N-619', 'score': 0.9999615022031046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html', 'title': 'N-48', 'score': 0.9999549550537051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html', 'title': 'N-579', 'score': 0.9999471201208573}]
result = search.search('pear pear banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #85 checking search results for 'pear pear banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #85 checking search results for 'pear pear banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking search results for 'tomato coconut tomato banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019386170431275697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015687495981135793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013304222075628779}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00979037937572122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008471952134304522}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008172606490007742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00784492964762584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007528766580063461}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007216021398566428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('tomato coconut tomato banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #86 checking search results for 'tomato coconut tomato banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #86 checking search results for 'tomato coconut tomato banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking search results for 'tomato coconut tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html', 'title': 'N-32', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html', 'title': 'N-48', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-446.html', 'title': 'N-446', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-113.html', 'title': 'N-113', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html', 'title': 'N-459', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-141.html', 'title': 'N-141', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html', 'title': 'N-84', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-435.html', 'title': 'N-435', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-547.html', 'title': 'N-547', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-400.html', 'title': 'N-400', 'score': 1.0000000000000002}]
result = search.search('tomato coconut tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #87 checking search results for 'tomato coconut tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #87 checking search results for 'tomato coconut tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking search results for 'banana apple peach pear pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.015711001187305874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01542799423919201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012724171817779562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009372880087830765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008455244217951127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007971437530956174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007482300265223696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007344045057444832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007041865979932466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006553495183293365}]
result = search.search('banana apple peach pear pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #88 checking search results for 'banana apple peach pear pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #88 checking search results for 'banana apple peach pear pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking search results for 'banana apple peach pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-428.html', 'title': 'N-428', 'score': 0.9999844385177118}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-672.html', 'title': 'N-672', 'score': 0.9999520954565059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-735.html', 'title': 'N-735', 'score': 0.9976853407170155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-440.html', 'title': 'N-440', 'score': 0.996894299829245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-492.html', 'title': 'N-492', 'score': 0.996388246380163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-400.html', 'title': 'N-400', 'score': 0.99532747015496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-515.html', 'title': 'N-515', 'score': 0.9952106839395127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html', 'title': 'N-495', 'score': 0.9948211482795586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-427.html', 'title': 'N-427', 'score': 0.9944910795773035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-675.html', 'title': 'N-675', 'score': 0.9944015776484683}]
result = search.search('banana apple peach pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #89 checking search results for 'banana apple peach pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #89 checking search results for 'banana apple peach pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking search results for 'peach apple tomato apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020217443063169895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01511703615277046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012890185264339264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010295747712849909}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082540577449064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007735349761929931}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007553963534273831}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.0075099244486522086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007432760596528524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0063673668151729024}]
result = search.search('peach apple tomato apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #90 checking search results for 'peach apple tomato apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #90 checking search results for 'peach apple tomato apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking search results for 'peach apple tomato apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-486.html', 'title': 'N-486', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-352.html', 'title': 'N-352', 'score': 0.9999991282714361}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-696.html', 'title': 'N-696', 'score': 0.999994376948778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-108.html', 'title': 'N-108', 'score': 0.9999942886472858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-795.html', 'title': 'N-795', 'score': 0.9999870568660592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-189.html', 'title': 'N-189', 'score': 0.9999637703191423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-934.html', 'title': 'N-934', 'score': 0.9999637703191423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-607.html', 'title': 'N-607', 'score': 0.9999471373829184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-217.html', 'title': 'N-217', 'score': 0.9999444587385002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-756.html', 'title': 'N-756', 'score': 0.9999368235704423}]
result = search.search('peach apple tomato apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #91 checking search results for 'peach apple tomato apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #91 checking search results for 'peach apple tomato apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking search results for 'coconut tomato apple banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019788328922644025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015477529473221946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013264104736425931}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.01000813810081979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008392373242279368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008193588606791934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007858972139884407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00746400076596697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007288570443841599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006759522278364903}]
result = search.search('coconut tomato apple banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #92 checking search results for 'coconut tomato apple banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #92 checking search results for 'coconut tomato apple banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking search results for 'coconut tomato apple banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-319.html', 'title': 'N-319', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-626.html', 'title': 'N-626', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-956.html', 'title': 'N-956', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-428.html', 'title': 'N-428', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-786.html', 'title': 'N-786', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-376.html', 'title': 'N-376', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-82.html', 'title': 'N-82', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-479.html', 'title': 'N-479', 'score': 1.0}]
result = search.search('coconut tomato apple banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #93 checking search results for 'coconut tomato apple banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #93 checking search results for 'coconut tomato apple banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking search results for 'banana coconut pear coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.0202607482578076}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014010094127690963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013196770135760648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00873955114330248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007776691418750163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.0075831001144581875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007464109748536537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006960720188886994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006367006288025557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00635788940871841}]
result = search.search('banana coconut pear coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #94 checking search results for 'banana coconut pear coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #94 checking search results for 'banana coconut pear coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking search results for 'banana coconut pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9999050875494032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9998512107018245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9998512107018245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0.9998356616746938}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-318.html', 'title': 'N-318', 'score': 0.9998203070436321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-568.html', 'title': 'N-568', 'score': 0.9997721313074367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-556.html', 'title': 'N-556', 'score': 0.9996826702812037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-872.html', 'title': 'N-872', 'score': 0.9994520843551554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html', 'title': 'N-683', 'score': 0.9991823226954788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html', 'title': 'N-81', 'score': 0.9989516167782432}]
result = search.search('banana coconut pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #95 checking search results for 'banana coconut pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #95 checking search results for 'banana coconut pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking search results for 'peach apple peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01993158471446681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015205070718291027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012712990138140454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009597794542436061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008408311918693288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007724256850635336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007642977358532382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007444383114249996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006656442027448533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0066099916586182}]
result = search.search('peach apple peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #96 checking search results for 'peach apple peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #96 checking search results for 'peach apple peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking search results for 'peach apple peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-627.html', 'title': 'N-627', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-990.html', 'title': 'N-990', 'score': 0.9998475678503426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-263.html', 'title': 'N-263', 'score': 0.9996978932076122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-831.html', 'title': 'N-831', 'score': 0.9996197127893703}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-473.html', 'title': 'N-473', 'score': 0.9996049013634901}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-559.html', 'title': 'N-559', 'score': 0.9995151146679799}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html', 'title': 'N-43', 'score': 0.9994814239938961}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-708.html', 'title': 'N-708', 'score': 0.9994419507540904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-82.html', 'title': 'N-82', 'score': 0.999396282845981}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-626.html', 'title': 'N-626', 'score': 0.999025623141714}]
result = search.search('peach apple peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #97 checking search results for 'peach apple peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #97 checking search results for 'peach apple peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking search results for 'tomato tomato apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('tomato tomato apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #98 checking search results for 'tomato tomato apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #98 checking search results for 'tomato tomato apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking search results for 'tomato tomato apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('tomato tomato apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #99 checking search results for 'tomato tomato apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #99 checking search results for 'tomato tomato apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking search results for 'peach banana banana coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.0168101963883425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014350696510769069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012548276380513904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.01036519295989223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008662102450348355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008244054732939944}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007842509718224472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007390753332142369}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007276368110935446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006359956767760752}]
result = search.search('peach banana banana coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #100 checking search results for 'peach banana banana coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #100 checking search results for 'peach banana banana coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking search results for 'peach banana banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-347.html', 'title': 'N-347', 'score': 0.9999511650860772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-756.html', 'title': 'N-756', 'score': 0.9999157594850897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-371.html', 'title': 'N-371', 'score': 0.9999033408699525}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-655.html', 'title': 'N-655', 'score': 0.9998978745197834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-52.html', 'title': 'N-52', 'score': 0.9998706161198921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-271.html', 'title': 'N-271', 'score': 0.9998706161198921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-847.html', 'title': 'N-847', 'score': 0.9996432216595569}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-995.html', 'title': 'N-995', 'score': 0.9996168711492333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-430.html', 'title': 'N-430', 'score': 0.9995876508475816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-992.html', 'title': 'N-992', 'score': 0.9993048148046582}]
result = search.search('peach banana banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #101 checking search results for 'peach banana banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #101 checking search results for 'peach banana banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking search results for 'pear peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01865524801539416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015606802545382764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010337987121389244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00857805234054004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082564863681992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007832925829165898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007335932292012038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00674697588534384}]
result = search.search('pear peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #102 checking search results for 'pear peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #102 checking search results for 'pear peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking search results for 'pear peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-356.html', 'title': 'N-356', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-354.html', 'title': 'N-354', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html', 'title': 'N-634', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-649.html', 'title': 'N-649', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-71.html', 'title': 'N-71', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-656.html', 'title': 'N-656', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-268.html', 'title': 'N-268', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-328.html', 'title': 'N-328', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-256.html', 'title': 'N-256', 'score': 1.0000000000000002}]
result = search.search('pear peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #103 checking search results for 'pear peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #103 checking search results for 'pear peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #104 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #104 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #105 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #105 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking search results for 'tomato apple tomato coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02099492456728733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015529043119114919}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013209566400434174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009942990587172044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008131792895327405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007873171422909615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007454976400150275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0072315231468739844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006759252110879896}]
result = search.search('tomato apple tomato coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #106 checking search results for 'tomato apple tomato coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #106 checking search results for 'tomato apple tomato coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking search results for 'tomato apple tomato coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-143.html', 'title': 'N-143', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-985.html', 'title': 'N-985', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-65.html', 'title': 'N-65', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-382.html', 'title': 'N-382', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html', 'title': 'N-658', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-626.html', 'title': 'N-626', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-375.html', 'title': 'N-375', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-743.html', 'title': 'N-743', 'score': 1.0000000000000002}]
result = search.search('tomato apple tomato coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #107 checking search results for 'tomato apple tomato coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #107 checking search results for 'tomato apple tomato coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking search results for 'tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #108 checking search results for 'tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #108 checking search results for 'tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking search results for 'tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #109 checking search results for 'tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #109 checking search results for 'tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
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
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #111 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #111 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking search results for 'tomato apple tomato tomato coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015529043119114919}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013209566400434174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009942990587172044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008131792895327405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007873171422909615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007454976400150277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0072315231468739844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006759252110879896}]
result = search.search('tomato apple tomato tomato coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #112 checking search results for 'tomato apple tomato tomato coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #112 checking search results for 'tomato apple tomato tomato coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking search results for 'tomato apple tomato tomato coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-143.html', 'title': 'N-143', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-181.html', 'title': 'N-181', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-334.html', 'title': 'N-334', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html', 'title': 'N-472', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-601.html', 'title': 'N-601', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-741.html', 'title': 'N-741', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-257.html', 'title': 'N-257', 'score': 1.0}]
result = search.search('tomato apple tomato tomato coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #113 checking search results for 'tomato apple tomato tomato coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #113 checking search results for 'tomato apple tomato tomato coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking search results for 'tomato banana pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.0200489418380704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015054167112095762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013366797481779946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010150683947430527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873810090099705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007947361709192174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007884974975055803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007535811356359569}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730196671054453}]
result = search.search('tomato banana pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #114 checking search results for 'tomato banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #114 checking search results for 'tomato banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking search results for 'tomato banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-601.html', 'title': 'N-601', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-356.html', 'title': 'N-356', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-669.html', 'title': 'N-669', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-150.html', 'title': 'N-150', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-888.html', 'title': 'N-888', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-332.html', 'title': 'N-332', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-535.html', 'title': 'N-535', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-209.html', 'title': 'N-209', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-597.html', 'title': 'N-597', 'score': 1.0000000000000002}]
result = search.search('tomato banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #115 checking search results for 'tomato banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #115 checking search results for 'tomato banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking search results for 'peach coconut banana banana banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.014765281930912304}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.0132969775151478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011768353088239718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010241770887999307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008420446117557033}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007997978800755264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007797214986359693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0070780974757393995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.006744265664908088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.005959370343619028}]
result = search.search('peach coconut banana banana banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #116 checking search results for 'peach coconut banana banana banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #116 checking search results for 'peach coconut banana banana banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking search results for 'peach coconut banana banana banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-90.html', 'title': 'N-90', 'score': 0.9998738563803145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-792.html', 'title': 'N-792', 'score': 0.9996307609008959}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-294.html', 'title': 'N-294', 'score': 0.9995706803586177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-941.html', 'title': 'N-941', 'score': 0.9995154275021768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-64.html', 'title': 'N-64', 'score': 0.9984034913568602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-405.html', 'title': 'N-405', 'score': 0.9981353471856669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-784.html', 'title': 'N-784', 'score': 0.9973585009959083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-284.html', 'title': 'N-284', 'score': 0.996683675701186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-321.html', 'title': 'N-321', 'score': 0.9946403210987543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-132.html', 'title': 'N-132', 'score': 0.9940666925212089}]
result = search.search('peach coconut banana banana banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #117 checking search results for 'peach coconut banana banana banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #117 checking search results for 'peach coconut banana banana banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #118 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #118 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #119 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #119 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking search results for 'coconut coconut pear peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02047547780759897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014120309699273468}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013073896400676915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009857058358267326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007952261383887356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007837628064417314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007578198134328813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.006986301155757017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006924586232238924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00642871513809322}]
result = search.search('coconut coconut pear peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #120 checking search results for 'coconut coconut pear peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #120 checking search results for 'coconut coconut pear peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking search results for 'coconut coconut pear peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-499.html', 'title': 'N-499', 'score': 0.9999755142103733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-318.html', 'title': 'N-318', 'score': 0.9999678248366511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-160.html', 'title': 'N-160', 'score': 0.9998033746419239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-364.html', 'title': 'N-364', 'score': 0.9995221654865065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-782.html', 'title': 'N-782', 'score': 0.9992459194188443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-120.html', 'title': 'N-120', 'score': 0.9991290968972377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-242.html', 'title': 'N-242', 'score': 0.9990365527686302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-34.html', 'title': 'N-34', 'score': 0.9988723362331318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-832.html', 'title': 'N-832', 'score': 0.998703586873818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0.9985341029989766}]
result = search.search('coconut coconut pear peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #121 checking search results for 'coconut coconut pear peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #121 checking search results for 'coconut coconut pear peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking search results for 'peach banana coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01972357351868843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015488186567516543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013267025586949407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009943142311040739}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00857954446166246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008196846883842075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007848879241471781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007527958956223871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.0074293891148829545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006734565764473396}]
result = search.search('peach banana coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #122 checking search results for 'peach banana coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #122 checking search results for 'peach banana coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking search results for 'peach banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-849.html', 'title': 'N-849', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-547.html', 'title': 'N-547', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-49.html', 'title': 'N-49', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-274.html', 'title': 'N-274', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-428.html', 'title': 'N-428', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-719.html', 'title': 'N-719', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-529.html', 'title': 'N-529', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-861.html', 'title': 'N-861', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-893.html', 'title': 'N-893', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-862.html', 'title': 'N-862', 'score': 1.0000000000000002}]
result = search.search('peach banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #123 checking search results for 'peach banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #123 checking search results for 'peach banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking search results for 'peach pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017357817777580588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015607807888514187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010421326325841602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873633543065484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082508053526444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007799885382063103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007470358888222107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('peach pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #124 checking search results for 'peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #124 checking search results for 'peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking search results for 'peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-167.html', 'title': 'N-167', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-19.html', 'title': 'N-19', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-574.html', 'title': 'N-574', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html', 'title': 'N-175', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0}]
result = search.search('peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #125 checking search results for 'peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #125 checking search results for 'peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking search results for 'apple peach apple peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010417067314545846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008507193563889778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008227390811338423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00787315571136734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007248519972589281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006744943947177923}]
result = search.search('apple peach apple peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #126 checking search results for 'apple peach apple peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #126 checking search results for 'apple peach apple peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking search results for 'apple peach apple peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-422.html', 'title': 'N-422', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-105.html', 'title': 'N-105', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-585.html', 'title': 'N-585', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-829.html', 'title': 'N-829', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-566.html', 'title': 'N-566', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-423.html', 'title': 'N-423', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-66.html', 'title': 'N-66', 'score': 1.0}]
result = search.search('apple peach apple peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #127 checking search results for 'apple peach apple peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #127 checking search results for 'apple peach apple peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #128 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #128 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #129 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #129 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking search results for 'peach pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01865524801539416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015606802545382764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010337987121389244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00857805234054004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082564863681992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007832925829165898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007335932292012038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00674697588534384}]
result = search.search('peach pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #130 checking search results for 'peach pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #130 checking search results for 'peach pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking search results for 'peach pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-356.html', 'title': 'N-356', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-354.html', 'title': 'N-354', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html', 'title': 'N-634', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-649.html', 'title': 'N-649', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-71.html', 'title': 'N-71', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-656.html', 'title': 'N-656', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-268.html', 'title': 'N-268', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-328.html', 'title': 'N-328', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-256.html', 'title': 'N-256', 'score': 1.0000000000000002}]
result = search.search('peach pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #131 checking search results for 'peach pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #131 checking search results for 'peach pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking search results for 'banana pear tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.0200489418380704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015054167112095762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013366797481779946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010150683947430527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873810090099705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007947361709192174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007884974975055803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007535811356359569}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730196671054453}]
result = search.search('banana pear tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #132 checking search results for 'banana pear tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #132 checking search results for 'banana pear tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking search results for 'banana pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-601.html', 'title': 'N-601', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-356.html', 'title': 'N-356', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-669.html', 'title': 'N-669', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-150.html', 'title': 'N-150', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-888.html', 'title': 'N-888', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-332.html', 'title': 'N-332', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-535.html', 'title': 'N-535', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-209.html', 'title': 'N-209', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-597.html', 'title': 'N-597', 'score': 1.0000000000000002}]
result = search.search('banana pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #133 checking search results for 'banana pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #133 checking search results for 'banana pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking search results for 'apple banana pear banana banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.015045427522916493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012359565862382644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.012305669476318365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009959173927688098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008310010583696396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007679992953911091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0074606300522659565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00710207532542517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006213904511564811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.005901953046679054}]
result = search.search('apple banana pear banana banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #134 checking search results for 'apple banana pear banana banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #134 checking search results for 'apple banana pear banana banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking search results for 'apple banana pear banana banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-378.html', 'title': 'N-378', 'score': 0.9999923938902627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-348.html', 'title': 'N-348', 'score': 0.999979820332457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-887.html', 'title': 'N-887', 'score': 0.9999371619676191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-419.html', 'title': 'N-419', 'score': 0.9998239728691436}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-759.html', 'title': 'N-759', 'score': 0.9998239728691436}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-504.html', 'title': 'N-504', 'score': 0.9993034438355489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-638.html', 'title': 'N-638', 'score': 0.9986519166143292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-877.html', 'title': 'N-877', 'score': 0.998030442026512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html', 'title': 'N-466', 'score': 0.9964852503402707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-485.html', 'title': 'N-485', 'score': 0.996403129127053}]
result = search.search('apple banana pear banana banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #135 checking search results for 'apple banana pear banana banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #135 checking search results for 'apple banana pear banana banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking search results for 'pear coconut banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018061848959776187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01510209198700232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013264104736425931}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009874466377469564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008589336693142408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008205599403988857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007827657805594192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007500361356632109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00746400076596697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006732656533059662}]
result = search.search('pear coconut banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #136 checking search results for 'pear coconut banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #136 checking search results for 'pear coconut banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking search results for 'pear coconut banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-319.html', 'title': 'N-319', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-182.html', 'title': 'N-182', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-948.html', 'title': 'N-948', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-642.html', 'title': 'N-642', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html', 'title': 'N-424', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-392.html', 'title': 'N-392', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-679.html', 'title': 'N-679', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html', 'title': 'N-191', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html', 'title': 'N-84', 'score': 1.0}]
result = search.search('pear coconut banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #137 checking search results for 'pear coconut banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #137 checking search results for 'pear coconut banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking search results for 'coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019386170431275697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015687495981135793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013304222075628777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009790379375721218}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00847195213430452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008172606490007742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00784492964762584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007528766580063459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007216021398566428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006761578978050135}]
result = search.search('coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #138 checking search results for 'coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #138 checking search results for 'coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking search results for 'coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-113.html', 'title': 'N-113', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-141.html', 'title': 'N-141', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html', 'title': 'N-84', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-319.html', 'title': 'N-319', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-435.html', 'title': 'N-435', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-389.html', 'title': 'N-389', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-400.html', 'title': 'N-400', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-639.html', 'title': 'N-639', 'score': 1.0}]
result = search.search('coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #139 checking search results for 'coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #139 checking search results for 'coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking search results for 'apple pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020083082159211445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014568131253610003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.0128919673046774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010419712217867501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008059087645759421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00775213666292949}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007736419157367055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0075041688694053145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007461624905909457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006368787509068998}]
result = search.search('apple pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #140 checking search results for 'apple pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #140 checking search results for 'apple pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking search results for 'apple pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-106.html', 'title': 'N-106', 'score': 0.9999979493932466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-58.html', 'title': 'N-58', 'score': 0.9999959020769152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html', 'title': 'N-133', 'score': 0.9999825818868451}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-610.html', 'title': 'N-610', 'score': 0.9999759662322202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-127.html', 'title': 'N-127', 'score': 0.9999698800769534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-670.html', 'title': 'N-670', 'score': 0.9999644541788434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-159.html', 'title': 'N-159', 'score': 0.9999624636021719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html', 'title': 'N-894', 'score': 0.9999526020776474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-486.html', 'title': 'N-486', 'score': 0.9999520304532704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-711.html', 'title': 'N-711', 'score': 0.9999516644928412}]
result = search.search('apple pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #141 checking search results for 'apple pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #141 checking search results for 'apple pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #142 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #142 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #143 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #143 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking search results for 'apple coconut peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020010205411443507}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015470709099415636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013261395666620688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.01007438251095659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008470318872053965}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00819394368703473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007856610647138525}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007576358135571883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007276259381139527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006741287070940565}]
result = search.search('apple coconut peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #144 checking search results for 'apple coconut peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #144 checking search results for 'apple coconut peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking search results for 'apple coconut peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-49.html', 'title': 'N-49', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-428.html', 'title': 'N-428', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-119.html', 'title': 'N-119', 'score': 0.9993598385311964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-219.html', 'title': 'N-219', 'score': 0.9993217025328427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-450.html', 'title': 'N-450', 'score': 0.9992521782750529}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-862.html', 'title': 'N-862', 'score': 0.999162087524674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-388.html', 'title': 'N-388', 'score': 0.9989802005451531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-244.html', 'title': 'N-244', 'score': 0.9988626266127983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-552.html', 'title': 'N-552', 'score': 0.9987353161366399}]
result = search.search('apple coconut peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #145 checking search results for 'apple coconut peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #145 checking search results for 'apple coconut peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking search results for 'tomato apple pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020142064363485736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014510144896051007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012856061696853332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.01040988475834211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008038505430468494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007737251058321551}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.0077148723425433585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007495276200856638}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007414191723222562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006346238044348001}]
result = search.search('tomato apple pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #146 checking search results for 'tomato apple pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #146 checking search results for 'tomato apple pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking search results for 'tomato apple pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-486.html', 'title': 'N-486', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html', 'title': 'N-894', 'score': 0.9999999982868103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-696.html', 'title': 'N-696', 'score': 0.9999936588039853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-166.html', 'title': 'N-166', 'score': 0.9999936588039853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-274.html', 'title': 'N-274', 'score': 0.9999786787162261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-715.html', 'title': 'N-715', 'score': 0.9999786787162261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-859.html', 'title': 'N-859', 'score': 0.9999786787162261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-106.html', 'title': 'N-106', 'score': 0.9999698156920414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-217.html', 'title': 'N-217', 'score': 0.9999372860349728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-583.html', 'title': 'N-583', 'score': 0.9999372860349728}]
result = search.search('tomato apple pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #147 checking search results for 'tomato apple pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #147 checking search results for 'tomato apple pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking search results for 'peach peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020191532338175902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015568621717957297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.01212860415922361}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.01045642511470264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00887508090909163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00813415894329162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00797684967170918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007590471320428179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0072654820555777275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006650922470212738}]
result = search.search('peach peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #148 checking search results for 'peach peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #148 checking search results for 'peach peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking search results for 'peach peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-89.html', 'title': 'N-89', 'score': 0.9999999433810121}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-746.html', 'title': 'N-746', 'score': 0.9999890564749674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-70.html', 'title': 'N-70', 'score': 0.9999859117644576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-783.html', 'title': 'N-783', 'score': 0.999985893763983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-379.html', 'title': 'N-379', 'score': 0.9999818616476152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-365.html', 'title': 'N-365', 'score': 0.9999797226935083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-69.html', 'title': 'N-69', 'score': 0.9999769299827954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-598.html', 'title': 'N-598', 'score': 0.9999727517066559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-827.html', 'title': 'N-827', 'score': 0.9999718051221836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.9999482448214125}]
result = search.search('peach peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #149 checking search results for 'peach peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #149 checking search results for 'peach peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking search results for 'pear banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020048941838070402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015054167112095762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013366797481779949}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010150683947430529}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873810090099705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007947361709192174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007884974975055805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.00753581135635957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730196671054454}]
result = search.search('pear banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #150 checking search results for 'pear banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #150 checking search results for 'pear banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking search results for 'pear banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-601.html', 'title': 'N-601', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-356.html', 'title': 'N-356', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-669.html', 'title': 'N-669', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html', 'title': 'N-84', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-150.html', 'title': 'N-150', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-966.html', 'title': 'N-966', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-888.html', 'title': 'N-888', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-332.html', 'title': 'N-332', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-924.html', 'title': 'N-924', 'score': 1.0000000000000002}]
result = search.search('pear banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #151 checking search results for 'pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #151 checking search results for 'pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #152 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #152 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #152 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #153 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #153 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #153 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking search results for 'banana tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.0200489418380704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015054167112095762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013366797481779946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010150683947430527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873810090099705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007947361709192174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007884974975055803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007535811356359569}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730196671054453}]
result = search.search('banana tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #154 checking search results for 'banana tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #154 checking search results for 'banana tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking search results for 'banana tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-601.html', 'title': 'N-601', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-356.html', 'title': 'N-356', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-669.html', 'title': 'N-669', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-150.html', 'title': 'N-150', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-888.html', 'title': 'N-888', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-332.html', 'title': 'N-332', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-535.html', 'title': 'N-535', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-209.html', 'title': 'N-209', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-597.html', 'title': 'N-597', 'score': 1.0000000000000002}]
result = search.search('banana tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #155 checking search results for 'banana tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #155 checking search results for 'banana tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking search results for 'pear tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017357817777580588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015607807888514187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010421326325841602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873633543065484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082508053526444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007799885382063103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007470358888222107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('pear tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #156 checking search results for 'pear tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #156 checking search results for 'pear tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking search results for 'pear tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-167.html', 'title': 'N-167', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-19.html', 'title': 'N-19', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-574.html', 'title': 'N-574', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html', 'title': 'N-175', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0}]
result = search.search('pear tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #157 checking search results for 'pear tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #157 checking search results for 'pear tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking search results for 'peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #158 checking search results for 'peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #158 checking search results for 'peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking search results for 'peach tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('peach tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #159 checking search results for 'peach tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #159 checking search results for 'peach tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking search results for 'coconut tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('coconut tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #160 checking search results for 'coconut tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #160 checking search results for 'coconut tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking search results for 'coconut tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('coconut tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #161 checking search results for 'coconut tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #161 checking search results for 'coconut tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking search results for 'banana peach tomato apple banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.016745346464997042}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.013972952251578142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012980562842043918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.01026763462042037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008655450244501131}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00799019826294777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00794266950189457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007346308366646162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006735502835956617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006324738414079476}]
result = search.search('banana peach tomato apple banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #162 checking search results for 'banana peach tomato apple banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #162 checking search results for 'banana peach tomato apple banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking search results for 'banana peach tomato apple banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-690.html', 'title': 'N-690', 'score': 0.9999594703785437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-214.html', 'title': 'N-214', 'score': 0.9999385208583697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-811.html', 'title': 'N-811', 'score': 0.9998653218225023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-406.html', 'title': 'N-406', 'score': 0.9998105616019446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-194.html', 'title': 'N-194', 'score': 0.9992481170950257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-532.html', 'title': 'N-532', 'score': 0.9989324329551059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-212.html', 'title': 'N-212', 'score': 0.9989231867897924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-558.html', 'title': 'N-558', 'score': 0.9989127160521936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-351.html', 'title': 'N-351', 'score': 0.998884155173687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-966.html', 'title': 'N-966', 'score': 0.9988100635226291}]
result = search.search('banana peach tomato apple banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #163 checking search results for 'banana peach tomato apple banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #163 checking search results for 'banana peach tomato apple banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking search results for 'coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019386170431275697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015687495981135793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013304222075628777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009790379375721218}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00847195213430452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008172606490007742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00784492964762584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007528766580063459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007216021398566428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006761578978050135}]
result = search.search('coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #164 checking search results for 'coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #164 checking search results for 'coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking search results for 'coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html', 'title': 'N-32', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-113.html', 'title': 'N-113', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-18.html', 'title': 'N-18', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-141.html', 'title': 'N-141', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html', 'title': 'N-84', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-319.html', 'title': 'N-319', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-435.html', 'title': 'N-435', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-389.html', 'title': 'N-389', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-400.html', 'title': 'N-400', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-639.html', 'title': 'N-639', 'score': 1.0}]
result = search.search('coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #165 checking search results for 'coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #165 checking search results for 'coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking search results for 'tomato peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('tomato peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #166 checking search results for 'tomato peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #166 checking search results for 'tomato peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #167 checking search results for 'tomato peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('tomato peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #167 checking search results for 'tomato peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #167 checking search results for 'tomato peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking search results for 'pear peach tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01735781777758059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015607807888514189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010421326325841605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873633543065486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082508053526444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007799885382063103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007470358888222108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('pear peach tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #168 checking search results for 'pear peach tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #168 checking search results for 'pear peach tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking search results for 'pear peach tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-167.html', 'title': 'N-167', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-36.html', 'title': 'N-36', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html', 'title': 'N-578', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'title': 'N-433', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-96.html', 'title': 'N-96', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-19.html', 'title': 'N-19', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-804.html', 'title': 'N-804', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-268.html', 'title': 'N-268', 'score': 1.0000000000000002}]
result = search.search('pear peach tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #169 checking search results for 'pear peach tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #169 checking search results for 'pear peach tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking search results for 'banana tomato coconut tomato coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02089587694233865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015172328084251598}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013154204291224669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.008282472616126963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007754873516813364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007361202470690016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007327468041832576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007017028367472793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00646585822817719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html', 'title': 'N-10', 'score': 0.006021215754746013}]
result = search.search('banana tomato coconut tomato coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #170 checking search results for 'banana tomato coconut tomato coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #170 checking search results for 'banana tomato coconut tomato coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking search results for 'banana tomato coconut tomato coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-13.html', 'title': 'N-13', 'score': 0.9999983308847341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-508.html', 'title': 'N-508', 'score': 0.9999964333142173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-236.html', 'title': 'N-236', 'score': 0.9999939701573972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-813.html', 'title': 'N-813', 'score': 0.9999925544497591}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-75.html', 'title': 'N-75', 'score': 0.9999876857559566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-856.html', 'title': 'N-856', 'score': 0.9999876857559566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9999845486308454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-454.html', 'title': 'N-454', 'score': 0.9999787597934324}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-96.html', 'title': 'N-96', 'score': 0.9999772639303501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-977.html', 'title': 'N-977', 'score': 0.9999671630250527}]
result = search.search('banana tomato coconut tomato coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #171 checking search results for 'banana tomato coconut tomato coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #171 checking search results for 'banana tomato coconut tomato coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking search results for 'banana coconut banana pear coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01927249242451688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.013621731587768915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013173309816980505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00983355007394574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008129787502080781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007814612733700144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007757357376611178}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007193067917248502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007092476032751999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006381821986031675}]
result = search.search('banana coconut banana pear coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #172 checking search results for 'banana coconut banana pear coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #172 checking search results for 'banana coconut banana pear coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking search results for 'banana coconut banana pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-141.html', 'title': 'N-141', 'score': 0.9999872085780345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-947.html', 'title': 'N-947', 'score': 0.9999662439065049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-906.html', 'title': 'N-906', 'score': 0.9997918216557654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-499.html', 'title': 'N-499', 'score': 0.9997687018070955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-138.html', 'title': 'N-138', 'score': 0.9996946638256243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html', 'title': 'N-381', 'score': 0.9992120749496622}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-688.html', 'title': 'N-688', 'score': 0.9991818446098913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-242.html', 'title': 'N-242', 'score': 0.9989835180107438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'title': 'N-433', 'score': 0.9987872595149249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-364.html', 'title': 'N-364', 'score': 0.9987642497759702}]
result = search.search('banana coconut banana pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #173 checking search results for 'banana coconut banana pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #173 checking search results for 'banana coconut banana pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking search results for 'coconut tomato pear tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017612586755654788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01522047216337955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013209566400434174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010338178510317679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008485761736665385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008165272931566048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007801162471033136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0074674610757979945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007454976400150275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067306540297334405}]
result = search.search('coconut tomato pear tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #174 checking search results for 'coconut tomato pear tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #174 checking search results for 'coconut tomato pear tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking search results for 'coconut tomato pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html', 'title': 'N-231', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-725.html', 'title': 'N-725', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-654.html', 'title': 'N-654', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-187.html', 'title': 'N-187', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-333.html', 'title': 'N-333', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html', 'title': 'N-191', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html', 'title': 'N-84', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-421.html', 'title': 'N-421', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-211.html', 'title': 'N-211', 'score': 1.0000000000000002}]
result = search.search('coconut tomato pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #175 checking search results for 'coconut tomato pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #175 checking search results for 'coconut tomato pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking search results for 'apple coconut apple peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019859225361862902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01529210684637981}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012439912146109643}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009837766302409129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008090582406056673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007657200289384098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.00753846628684988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007465066966332768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00729215814030921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0064490621960666865}]
result = search.search('apple coconut apple peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #176 checking search results for 'apple coconut apple peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #176 checking search results for 'apple coconut apple peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking search results for 'apple coconut apple peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-529.html', 'title': 'N-529', 'score': 0.9999521534249587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-40.html', 'title': 'N-40', 'score': 0.9999145881043359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-461.html', 'title': 'N-461', 'score': 0.9986038831613497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-393.html', 'title': 'N-393', 'score': 0.9979337370837205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html', 'title': 'N-951', 'score': 0.997883121974493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.9978689810880004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-610.html', 'title': 'N-610', 'score': 0.9969427076553764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-757.html', 'title': 'N-757', 'score': 0.9967872438898558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-581.html', 'title': 'N-581', 'score': 0.9955560403143068}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-407.html', 'title': 'N-407', 'score': 0.9953864622600919}]
result = search.search('apple coconut apple peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #177 checking search results for 'apple coconut apple peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #177 checking search results for 'apple coconut apple peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking search results for 'tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 0.0}]
result = search.search('tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #178 checking search results for 'tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #178 checking search results for 'tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking search results for 'tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 0}]
result = search.search('tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #179 checking search results for 'tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #179 checking search results for 'tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking search results for 'apple peach peach tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01917037365901352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014679785631854275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.0127930337806862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009847955867753822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00847028456044176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007726784366646493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007677049536561884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0075960029578025405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006590234824301288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006510009359438739}]
result = search.search('apple peach peach tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #180 checking search results for 'apple peach peach tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #180 checking search results for 'apple peach peach tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking search results for 'apple peach peach tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-213.html', 'title': 'N-213', 'score': 0.9999705761528844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-759.html', 'title': 'N-759', 'score': 0.9999165893640461}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-378.html', 'title': 'N-378', 'score': 0.9994359653888599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html', 'title': 'N-710', 'score': 0.9988565600770746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-279.html', 'title': 'N-279', 'score': 0.9988184935326119}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-493.html', 'title': 'N-493', 'score': 0.9987090751121496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-869.html', 'title': 'N-869', 'score': 0.9986550934186886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-348.html', 'title': 'N-348', 'score': 0.9986003136406748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html', 'title': 'N-170', 'score': 0.9985792906064428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-319.html', 'title': 'N-319', 'score': 0.9985690535070075}]
result = search.search('apple peach peach tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #181 checking search results for 'apple peach peach tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #181 checking search results for 'apple peach peach tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking search results for 'banana coconut coconut pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.0202607482578076}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014010094127690963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013196770135760648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00873955114330248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007776691418750163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.0075831001144581875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007464109748536537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006960720188886994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006367006288025557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00635788940871841}]
result = search.search('banana coconut coconut pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #182 checking search results for 'banana coconut coconut pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #182 checking search results for 'banana coconut coconut pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking search results for 'banana coconut coconut pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9999050875494032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9998512107018245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9998512107018245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0.9998356616746938}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-318.html', 'title': 'N-318', 'score': 0.9998203070436321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-568.html', 'title': 'N-568', 'score': 0.9997721313074367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-556.html', 'title': 'N-556', 'score': 0.9996826702812037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-872.html', 'title': 'N-872', 'score': 0.9994520843551554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html', 'title': 'N-683', 'score': 0.9991823226954788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html', 'title': 'N-81', 'score': 0.9989516167782432}]
result = search.search('banana coconut coconut pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #183 checking search results for 'banana coconut coconut pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #183 checking search results for 'banana coconut coconut pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking search results for 'peach peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('peach peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #184 checking search results for 'peach peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #184 checking search results for 'peach peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking search results for 'peach peach tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('peach peach tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #185 checking search results for 'peach peach tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #185 checking search results for 'peach peach tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking search results for 'apple apple pear coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019360598380568174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.0147168761512482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012339793157484708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010402247020084788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008086964194183756}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007671209597745074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007659404920975662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007502107921503742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007498600282967491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00640233064624823}]
result = search.search('apple apple pear coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #186 checking search results for 'apple apple pear coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #186 checking search results for 'apple apple pear coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking search results for 'apple apple pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-859.html', 'title': 'N-859', 'score': 0.9999719818491666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-583.html', 'title': 'N-583', 'score': 0.9999173353529385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-271.html', 'title': 'N-271', 'score': 0.9998571402850867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-156.html', 'title': 'N-156', 'score': 0.9998571402850867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-64.html', 'title': 'N-64', 'score': 0.9998422342249111}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-610.html', 'title': 'N-610', 'score': 0.9998189426488199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-996.html', 'title': 'N-996', 'score': 0.9997988006198054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-679.html', 'title': 'N-679', 'score': 0.9997988006198054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html', 'title': 'N-259', 'score': 0.9997447967024746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-441.html', 'title': 'N-441', 'score': 0.9997447967024746}]
result = search.search('apple apple pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #187 checking search results for 'apple apple pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #187 checking search results for 'apple apple pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking search results for 'banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010463140002251431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875540264263067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008318669866925777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #188 checking search results for 'banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #188 checking search results for 'banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking search results for 'banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'title': 'N-39', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'title': 'N-60', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'title': 'N-104', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'title': 'N-124', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'title': 'N-157', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'title': 'N-198', 'score': 1.0}]
result = search.search('banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #189 checking search results for 'banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #189 checking search results for 'banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking search results for 'tomato peach pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017357817777580588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015607807888514187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010421326325841602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873633543065484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082508053526444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00803282018630499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007799885382063103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007470358888222107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('tomato peach pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #190 checking search results for 'tomato peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #190 checking search results for 'tomato peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking search results for 'tomato peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-167.html', 'title': 'N-167', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-179.html', 'title': 'N-179', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-19.html', 'title': 'N-19', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-574.html', 'title': 'N-574', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'title': 'N-174', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html', 'title': 'N-175', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-460.html', 'title': 'N-460', 'score': 1.0}]
result = search.search('tomato peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #191 checking search results for 'tomato peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #191 checking search results for 'tomato peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking search results for 'banana banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.016645835334778227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014202454281708606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013114474269722435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010418458391320272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008672275451790638}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008249015086348073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007982182796674214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007441895882017828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007376955261597488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006351850059212707}]
result = search.search('banana banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #192 checking search results for 'banana banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #192 checking search results for 'banana banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking search results for 'banana banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-272.html', 'title': 'N-272', 'score': 0.9999999464266566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-106.html', 'title': 'N-106', 'score': 0.9999998319662391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-756.html', 'title': 'N-756', 'score': 0.9999982101507203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-51.html', 'title': 'N-51', 'score': 0.9999979224794264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-703.html', 'title': 'N-703', 'score': 0.999997868201908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-72.html', 'title': 'N-72', 'score': 0.9999940733197302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'title': 'N-433', 'score': 0.9999920973204464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-606.html', 'title': 'N-606', 'score': 0.9999883030844956}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-794.html', 'title': 'N-794', 'score': 0.9999851087204675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-699.html', 'title': 'N-699', 'score': 0.999982577785459}]
result = search.search('banana banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #193 checking search results for 'banana banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #193 checking search results for 'banana banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking search results for 'apple pear tomato coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018579978788573117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01524387962526817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013262069848873594}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010011579607311034}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008471085321040446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008221212826854564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00784307483204457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007596439360018749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007350953117926904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006739343921847376}]
result = search.search('apple pear tomato coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #194 checking search results for 'apple pear tomato coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #194 checking search results for 'apple pear tomato coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking search results for 'apple pear tomato coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-319.html', 'title': 'N-319', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html', 'title': 'N-766', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html', 'title': 'N-84', 'score': 0.9996448826208716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-349.html', 'title': 'N-349', 'score': 0.9995082222278578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-244.html', 'title': 'N-244', 'score': 0.9992328579973415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-293.html', 'title': 'N-293', 'score': 0.9992099848685585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-112.html', 'title': 'N-112', 'score': 0.9991374609126861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-450.html', 'title': 'N-450', 'score': 0.9989547372276041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-108.html', 'title': 'N-108', 'score': 0.9988425397485642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-986.html', 'title': 'N-986', 'score': 0.9987609571242075}]
result = search.search('apple pear tomato coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #195 checking search results for 'apple pear tomato coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #195 checking search results for 'apple pear tomato coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking search results for 'apple coconut coconut pear tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019301504161414393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.013871483824796874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013254119327962442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.008977049842972328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007727939575862722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007659925263337076}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007381153102677879}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006552293293422808}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.0065332397681242774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006321041749647647}]
result = search.search('apple coconut coconut pear tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #196 checking search results for 'apple coconut coconut pear tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #196 checking search results for 'apple coconut coconut pear tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking search results for 'apple coconut coconut pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-247.html', 'title': 'N-247', 'score': 0.9999975208426807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html', 'title': 'N-81', 'score': 0.9999918492655547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html', 'title': 'N-233', 'score': 0.9999741503806858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-76.html', 'title': 'N-76', 'score': 0.9999647585851956}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0.9999461243089651}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-87.html', 'title': 'N-87', 'score': 0.9999193412086719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-138.html', 'title': 'N-138', 'score': 0.999342650434861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-676.html', 'title': 'N-676', 'score': 0.9992352068621748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-491.html', 'title': 'N-491', 'score': 0.9991585092841885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-296.html', 'title': 'N-296', 'score': 0.9991470480783582}]
result = search.search('apple coconut coconut pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #197 checking search results for 'apple coconut coconut pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #197 checking search results for 'apple coconut coconut pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking search results for 'peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02099492456728733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015524735848489707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013216295889852696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010158987971029423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008510726413291102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008300270253703926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007412250626492393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730205640271725}]
result = search.search('peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #198 checking search results for 'peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #198 checking search results for 'peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking search results for 'peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-119.html', 'title': 'N-119', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-341.html', 'title': 'N-341', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-40.html', 'title': 'N-40', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-547.html', 'title': 'N-547', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-321.html', 'title': 'N-321', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-294.html', 'title': 'N-294', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-337.html', 'title': 'N-337', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-893.html', 'title': 'N-893', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-655.html', 'title': 'N-655', 'score': 1.0000000000000002}]
result = search.search('peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #199 checking search results for 'peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #199 checking search results for 'peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
