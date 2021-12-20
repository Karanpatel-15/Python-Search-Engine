
import testingtools
import crawler
import searchdata
import search

output = open('tinyfruits-search-failed.txt', 'w')
success_output = open('tinyfruits-search-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html')



#Test #0 checking search results for 'lime blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3067178104303064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11370042386523471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10265342611740245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0882223329527108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07116834968915606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04414631023537236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('lime blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #0 checking search results for 'lime blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #0 checking search results for 'lime blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking search results for 'lime blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9542335955602577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9523187838800629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9512755764799781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8683776088944807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8628814098079822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('lime blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #1 checking search results for 'lime blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #1 checking search results for 'lime blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking search results for 'lime pear peach papaya peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.296099613096195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10543979016296716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08321381836771465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05067325397208836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04354297810735384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.033667288514698024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.029220329550780213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01767850082339576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01767850082339576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('lime pear peach papaya peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #2 checking search results for 'lime pear peach papaya peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #2 checking search results for 'lime pear peach papaya peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking search results for 'lime pear peach papaya peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9183435736855718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9178980598428378}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8831303290441662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.727726906299939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.699476477546095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6316047701842882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6183018056675504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.38212524024957445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.38212524024957445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('lime pear peach papaya peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #3 checking search results for 'lime pear peach papaya peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #3 checking search results for 'lime pear peach papaya peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking search results for 'apricot pear peach blueberry tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11525657567428234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09597004548480666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0521030997012669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.044458766918338215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.042498918502119565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.04206919328888758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.024148572494316463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('apricot pear peach blueberry tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #4 checking search results for 'apricot pear peach blueberry tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #4 checking search results for 'apricot pear peach blueberry tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking search results for 'apricot pear peach blueberry tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9653526191811652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9372031420711563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9186248090379698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8067024285439562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6357484096820486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5219774662036322}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.33718686479947546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('apricot pear peach blueberry tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #5 checking search results for 'apricot pear peach blueberry tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #5 checking search results for 'apricot pear peach blueberry tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking search results for 'tomato lime apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3074633155170225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10265342611740245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08442376869993334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07116834968915606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04274693519677292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('tomato lime apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #6 checking search results for 'tomato lime apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #6 checking search results for 'tomato lime apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking search results for 'tomato lime apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9535877368991585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9011172544194608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8683776088944807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8628814098079822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('tomato lime apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #7 checking search results for 'tomato lime apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #7 checking search results for 'tomato lime apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking search results for 'apple coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.31959743430844756}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10265342611740245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08442376869993334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.044238146876788224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04412558625023501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04274693519677292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('apple coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #8 checking search results for 'apple coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #8 checking search results for 'apple coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking search results for 'apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9912213220900394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9562186676551894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9537856414108277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9011172544194608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8628814098079822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #9 checking search results for 'apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #9 checking search results for 'apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking search results for 'papaya tomato apricot apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('papaya tomato apricot apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #10 checking search results for 'papaya tomato apricot apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #10 checking search results for 'papaya tomato apricot apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking search results for 'papaya tomato apricot apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('papaya tomato apricot apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #11 checking search results for 'papaya tomato apricot apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #11 checking search results for 'papaya tomato apricot apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking search results for 'blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #12 checking search results for 'blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #12 checking search results for 'blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking search results for 'blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #13 checking search results for 'blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #13 checking search results for 'blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking search results for 'fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #14 checking search results for 'fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #14 checking search results for 'fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking search results for 'fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #15 checking search results for 'fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #15 checking search results for 'fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking search results for 'apricot blueberry fig tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11434339965985214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11393409412947837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.04994386950547139}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04600343439164321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0447212047461541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.032807031059864405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('apricot blueberry fig tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #16 checking search results for 'apricot blueberry fig tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #16 checking search results for 'apricot blueberry fig tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking search results for 'apricot blueberry fig tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9943758011396543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.966660084958041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9577041457457331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9577041457457331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('apricot blueberry fig tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #17 checking search results for 'apricot blueberry fig tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #17 checking search results for 'apricot blueberry fig tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #18 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #18 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #19 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #19 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking search results for 'apple papaya orange apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.23338982541539213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1141582967568647}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06823094668999655}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.05594220444749448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04516741596399178}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.044240235609986356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04164319227661221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.029194221565955414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.021677018651928115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('apple papaya orange apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #20 checking search results for 'apple papaya orange apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #20 checking search results for 'apple papaya orange apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking search results for 'apple papaya orange apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9763050526236604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9595887421641762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9562638161484427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8778500474203675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.832536184948152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7238511529705784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.631040439527901}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('apple papaya orange apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #21 checking search results for 'apple papaya orange apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #21 checking search results for 'apple papaya orange apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking search results for 'cherry fig peach blueberry orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3090990616793232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09096391357704746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09035137105239717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04396962703467612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.043838724109757816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.038105875484667165}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03550204784682146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03263249388628025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.024820710640019835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.023655170651432737}]
result = search.search('cherry fig peach blueberry orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #22 checking search results for 'cherry fig peach blueberry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #22 checking search results for 'cherry fig peach blueberry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking search results for 'cherry fig peach blueberry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9586609518237645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9475850441179121}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8236680796613969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.761884965858532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7594731260368511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6879020252634303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5365059012204692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5365059012204692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5113124613123797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.2845508380735398}]
result = search.search('cherry fig peach blueberry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #23 checking search results for 'cherry fig peach blueberry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #23 checking search results for 'cherry fig peach blueberry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking search results for 'orange cherry blueberry apricot blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2852218270741417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10241689826795278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.08727241778408883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07900509074674976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05732733465112079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.045548478681476094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.033471425949299125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.033061808030047456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.031509279582619426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.030401199796830668}]
result = search.search('orange cherry blueberry apricot blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #24 checking search results for 'orange cherry blueberry apricot blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #24 checking search results for 'orange cherry blueberry apricot blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking search results for 'orange cherry blueberry apricot blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9845418190736834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8846064647956862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8608932103692362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7146392933866691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7055869459201302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6994931596147331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.6994931596147331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6810810006392087}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6617216487201125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.657129577461975}]
result = search.search('orange cherry blueberry apricot blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #25 checking search results for 'orange cherry blueberry apricot blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #25 checking search results for 'orange cherry blueberry apricot blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking search results for 'cherry apple papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26355949310202514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10456490654278679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05891243358140317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04436638168878134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04369024113090721}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.029916678785502596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.018716520633617163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('cherry apple papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #26 checking search results for 'cherry apple papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #26 checking search results for 'cherry apple papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking search results for 'cherry apple papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9589904953588361}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9210024052386206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8789488805847455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8174214219437017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7188341226264067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6466565339777288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.4045622994395562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('cherry apple papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #27 checking search results for 'cherry apple papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #27 checking search results for 'cherry apple papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking search results for 'lime orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.22799097236207078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10688190287446392}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10360479815141346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04743770578925645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.044057724095804975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('lime orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #28 checking search results for 'lime orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #28 checking search results for 'lime orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking search results for 'lime orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9523187838800629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8984250260658612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8677610164113153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('lime orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #29 checking search results for 'lime orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #29 checking search results for 'lime orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking search results for 'tomato apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('tomato apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #30 checking search results for 'tomato apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #30 checking search results for 'tomato apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking search results for 'tomato apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('tomato apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #31 checking search results for 'tomato apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #31 checking search results for 'tomato apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking search results for 'peach coconut tomato coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.31553099592644807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.1141320065172364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08992561541198545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05365576700196191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.044224957855891596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0405268937343874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03497041536045179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03497041536045179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03028850496898082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('peach coconut tomato coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #32 checking search results for 'peach coconut tomato coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #32 checking search results for 'peach coconut tomato coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking search results for 'peach coconut tomato coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9786093922166816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9559335836523586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9559335836523586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8543181644245077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7558943207195108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7558943207195108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7558943207195108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6546936504228441}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6546936504228441}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('peach coconut tomato coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #33 checking search results for 'peach coconut tomato coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #33 checking search results for 'peach coconut tomato coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking search results for 'banana papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('banana papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #34 checking search results for 'banana papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #34 checking search results for 'banana papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking search results for 'banana papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('banana papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #35 checking search results for 'banana papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #35 checking search results for 'banana papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking search results for 'cherry apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26418456595817313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11555335018456396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.045037689905185516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04395164122282064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.043467398059126916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.039220518894086606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02453720402607222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('cherry apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #36 checking search results for 'cherry apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #36 checking search results for 'cherry apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking search results for 'cherry apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9713152447659879}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9500257759078112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9494069992606078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8193600656133991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('cherry apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #37 checking search results for 'cherry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #37 checking search results for 'cherry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking search results for 'kiwi tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3052997436712434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06617270707751717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0437312312088018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('kiwi tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #38 checking search results for 'kiwi tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #38 checking search results for 'kiwi tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking search results for 'kiwi tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.946877487331447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9218664874536561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('kiwi tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #39 checking search results for 'kiwi tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #39 checking search results for 'kiwi tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking search results for 'lime lime pear fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3222549725789801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11672376623033238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11150933591599722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04255902221014698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0401124042238361}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03380448031820218}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.032926050931871786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('lime lime pear fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #40 checking search results for 'lime lime pear fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #40 checking search results for 'lime lime pear fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking search results for 'lime lime pear fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.999463592882113}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9776413431679287}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9373221783353205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9199239657990155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7306923416271767}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6940902892341979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.48944107625150024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('lime lime pear fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #41 checking search results for 'lime lime pear fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #41 checking search results for 'lime lime pear fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking search results for 'tomato blueberry blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('tomato blueberry blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #42 checking search results for 'tomato blueberry blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #42 checking search results for 'tomato blueberry blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking search results for 'tomato blueberry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('tomato blueberry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #43 checking search results for 'tomato blueberry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #43 checking search results for 'tomato blueberry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking search results for 'orange fig banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29546744271304826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11741781792010819}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09836736519185917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04592567283238615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04591793916184169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.018989447476008524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('orange fig banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #44 checking search results for 'orange fig banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #44 checking search results for 'orange fig banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking search results for 'orange fig banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.99269496548452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9925278002512044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9869875375382519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9163829172606391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8238939346789916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('orange fig banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #45 checking search results for 'orange fig banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #45 checking search results for 'orange fig banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking search results for 'papaya lime blueberry kiwi lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.31130912260115384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08928013324105079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08431905238016855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07755804393405677}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06253624231587711}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04225823305088256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03640439216158132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03156326970929575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02620904626180582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02620904626180582}]
result = search.search('papaya lime blueberry kiwi lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #46 checking search results for 'papaya lime blueberry kiwi lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #46 checking search results for 'papaya lime blueberry kiwi lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking search results for 'papaya lime blueberry kiwi lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9655153857887202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.946342988648104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8908152775898597}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7868900898244773}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7504685440384187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.706229710416706}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6822480108021968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5665151247582435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5665151247582435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5012313722783172}]
result = search.search('papaya lime blueberry kiwi lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #47 checking search results for 'papaya lime blueberry kiwi lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #47 checking search results for 'papaya lime blueberry kiwi lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking search results for 'coconut fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.28487235510929493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11674212668155656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04470253788755516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04239520044987674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.018989447476008524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #48 checking search results for 'coconut fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #48 checking search results for 'coconut fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking search results for 'coconut fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9813078302886417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9662565961159678}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9163829172606391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8835225885631427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #49 checking search results for 'coconut fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #49 checking search results for 'coconut fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking search results for 'apricot papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('apricot papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #50 checking search results for 'apricot papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #50 checking search results for 'apricot papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking search results for 'apricot papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('apricot papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #51 checking search results for 'apricot papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #51 checking search results for 'apricot papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #52 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #52 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking search results for 'coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #53 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #53 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking search results for 'cherry fig papaya coconut pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2991573297850459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09931985546145145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09683291515203594}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03696238844422371}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0367711936300795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.032876269034177084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0321611246859116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.026998596083995498}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02667900732776557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('cherry fig papaya coconut pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #54 checking search results for 'cherry fig papaya coconut pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #54 checking search results for 'cherry fig papaya coconut pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking search results for 'cherry fig papaya coconut pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9278269851699534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.831871691879535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.81395551519776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7948185957919218}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.779177403907987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7106288213403742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5835814426834581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5766734513625081}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.39242164074467173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('cherry fig papaya coconut pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #55 checking search results for 'cherry fig papaya coconut pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #55 checking search results for 'cherry fig papaya coconut pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking search results for 'banana blueberry peach peach fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30812967236047367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10804282858630819}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.07363064243458789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06426557523041003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.036432100758482834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.036399458756678466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.036200676811335326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03227654746767869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('banana blueberry peach peach fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #56 checking search results for 'banana blueberry peach peach fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #56 checking search results for 'banana blueberry peach peach fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking search results for 'banana blueberry peach peach fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9556544215481722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9049325554689981}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7874890181133488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7867834530370833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7841517584229598}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.76312031134385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6189224748949111}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.25869827767894926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('banana blueberry peach peach fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #57 checking search results for 'banana blueberry peach peach fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #57 checking search results for 'banana blueberry peach peach fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking search results for 'orange blueberry cherry papaya cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29628381709460316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11608015236795156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04536747983675909}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.04430702265157428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03999511205004344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03953530923211995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03918758175674542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03746703541730517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03426722212031584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.017112853029128048}]
result = search.search('orange blueberry cherry papaya cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #58 checking search results for 'orange blueberry cherry papaya cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #58 checking search results for 'orange blueberry cherry papaya cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking search results for 'orange blueberry cherry papaya cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9757434243980202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9563590625209745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9189148765536049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8545656495188689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8470494327086163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.809859390980132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4880099077915742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.37110160626054683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.3698986209541679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.27465364293516414}]
result = search.search('orange blueberry cherry papaya cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #59 checking search results for 'orange blueberry cherry papaya cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #59 checking search results for 'orange blueberry cherry papaya cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking search results for 'orange pear orange tomato fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.28011282848241503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11848660329673855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11290123855711334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04406577610149369}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03377827358498002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03286698514059547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.022911205559852543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.022911205559852543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('orange pear orange tomato fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #60 checking search results for 'orange pear orange tomato fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #60 checking search results for 'orange pear orange tomato fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking search results for 'orange pear orange tomato fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9959715049268728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9524928300075614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9456250605424344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8687610674457187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.730125876499352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6928451659658275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4952314688007776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4952314688007776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('orange pear orange tomato fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #61 checking search results for 'orange pear orange tomato fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #61 checking search results for 'orange pear orange tomato fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking search results for 'pear peach fig banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10667270708363923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.044382175430002085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.036518624736590205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.036282248089665056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03334883104202847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear peach fig banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #62 checking search results for 'pear peach fig banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #62 checking search results for 'pear peach fig banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking search results for 'pear peach fig banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9593318810463842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8966665737107857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7698227418253614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7208433679575882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4427065117995896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear peach fig banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #63 checking search results for 'pear peach fig banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #63 checking search results for 'pear peach fig banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking search results for 'orange peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.27334194193079353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09840042492705911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06947873543551684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06309685343427059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04597953285874892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0438667328211387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04382718835015834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02453720402607222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02453720402607222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('orange peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #64 checking search results for 'orange peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #64 checking search results for 'orange peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking search results for 'orange peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9692613100434179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9481904594567138}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9473356957737032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8241708325633682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('orange peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #65 checking search results for 'orange peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #65 checking search results for 'orange peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking search results for 'orange tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('orange tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #66 checking search results for 'orange tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #66 checking search results for 'orange tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking search results for 'orange tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('orange tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #67 checking search results for 'orange tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #67 checking search results for 'orange tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking search results for 'fig pear apple apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2729503850710145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11553022000696625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11407524410638864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04542188940405291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03489761575913647}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.031256214897042174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.024187257096552783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.013653627516463766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.013653627516463766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('fig pear apple apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #68 checking search results for 'fig pear apple apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #68 checking search results for 'fig pear apple apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking search results for 'fig pear apple apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9818055600135069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9711208177409045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9554581596545315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8465469760122073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7356514228190182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6756109438317381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.29512659173577693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.29512659173577693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.29512659173577693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('fig pear apple apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #69 checking search results for 'fig pear apple apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #69 checking search results for 'fig pear apple apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking search results for 'peach blueberry banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11320752984200066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06617270707751717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06309685343427059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04021585479175914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03798447959373376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('peach blueberry banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #70 checking search results for 'peach blueberry banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #70 checking search results for 'peach blueberry banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking search results for 'peach blueberry banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9481904594567137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8477613772137168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8210440769559838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('peach blueberry banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #71 checking search results for 'peach blueberry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #71 checking search results for 'peach blueberry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking search results for 'pear fig pear lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2936478816596351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.1144699668888812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11425254381855288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.044255593134480506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04175955098571488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.023640690349541645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.016890585177188562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear fig pear lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #72 checking search results for 'pear fig pear lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #72 checking search results for 'pear fig pear lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking search results for 'pear fig pear lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9603809615818384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9587642328195587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9565957729017665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9107396062719564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8803029212928857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5109994659461834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.20609450736259577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear fig pear lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #73 checking search results for 'pear fig pear lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #73 checking search results for 'pear fig pear lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking search results for 'pear cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09884163304040819}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09789197951097453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.046455066807129373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.037932117382417516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02648542910026186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02648542910026186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02648542910026186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('pear cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #74 checking search results for 'pear cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #74 checking search results for 'pear cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking search results for 'pear cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9792856976158909}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.830840342027045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8199122545928149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8199122545928149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5724892093031335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5724892093031335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5724892093031335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('pear cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #75 checking search results for 'pear cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #75 checking search results for 'pear cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #76 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #76 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #77 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #77 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking search results for 'pear kiwi blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30948479568917386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11473564072080805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10577410203077761}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06557266406744591}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04363367322132315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0430732429833672}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04180179185447608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.021053246683308924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear kiwi blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #78 checking search results for 'pear kiwi blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #78 checking search results for 'pear kiwi blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking search results for 'pear kiwi blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9609894327962027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9598572936406086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9431528176079137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8891131035130447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8811933705264312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5255684572228687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5255684572228687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.4550712205328091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear kiwi blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #79 checking search results for 'pear kiwi blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #79 checking search results for 'pear kiwi blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
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
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #81 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #81 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking search results for 'tomato blueberry orange fig peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3055269448144335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10214021900039962}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09837715146228133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04937196694911028}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.043196913357041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0427877640060987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03986401639333151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.027699166810445437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.014781796706548818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.014781796706548818}]
result = search.search('tomato blueberry orange fig peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #82 checking search results for 'tomato blueberry orange fig peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #82 checking search results for 'tomato blueberry orange fig peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking search results for 'tomato blueberry orange fig peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9475821444824675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9337121433257756}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9248682772316622}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8554941647270794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8269360152634594}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6024238413978337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.5839061217146524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.3195122524380067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.3195122524380067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3195122524380067}]
result = search.search('tomato blueberry orange fig peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #83 checking search results for 'tomato blueberry orange fig peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #83 checking search results for 'tomato blueberry orange fig peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking search results for 'apricot apple fig apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30244956435387776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1189018145323858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09351512476479666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.050951997716726274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04019401614880047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03623613198272297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.02949216229514792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.028762236051273562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.028762236051273562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('apricot apple fig apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #84 checking search results for 'apricot apple fig apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #84 checking search results for 'apricot apple fig apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking search results for 'apricot apple fig apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9994616763700905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9380377464328193}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8688037651433277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7832531037523557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7832531037523557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6217029640128007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6217029640128007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6217029640128007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6217029640128007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('apricot apple fig apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #85 checking search results for 'apricot apple fig apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #85 checking search results for 'apricot apple fig apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking search results for 'orange peach blueberry peach cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29628381709460316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07604121094511969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06822919159230352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06578765090727413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.045083342197579895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.035941608733156584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03504409078469524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03426722212031584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.023957401228103973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.022832400837947596}]
result = search.search('orange peach blueberry peach cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #86 checking search results for 'orange peach blueberry peach cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #86 checking search results for 'orange peach blueberry peach cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking search results for 'orange peach blueberry peach cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.950369362250867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.918914876553605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8325147697046525}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7768869096602243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7574868335389382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6368971290542886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5529960675438245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5178452512177558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.49352808492272404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.27465364293516414}]
result = search.search('orange peach blueberry peach cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #87 checking search results for 'orange peach blueberry peach cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #87 checking search results for 'orange peach blueberry peach cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking search results for 'papaya papaya papaya apple apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.19237990138932015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09511802775771146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819389055803945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04390107027359229}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04390107027359229}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.032283763383217916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.010910917908701277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('papaya papaya papaya apple apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #88 checking search results for 'papaya papaya papaya apple apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #88 checking search results for 'papaya papaya papaya apple apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking search results for 'papaya papaya papaya apple apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9997971178777431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9489326721250538}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9489326721250538}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7995405608368183}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6805506895008708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.5966601722297775}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.23584223395731335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('papaya papaya papaya apple apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #89 checking search results for 'papaya papaya papaya apple apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #89 checking search results for 'papaya papaya papaya apple apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking search results for 'fig cherry apple blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2699279769899288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10230224132454399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09126619950843515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.043648493810490914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03986401639333151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03751414018616046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03703230913781845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02787031385110579}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0271317781603663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02647751654119099}]
result = search.search('fig cherry apple blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #90 checking search results for 'fig cherry apple blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #90 checking search results for 'fig cherry apple blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking search results for 'fig cherry apple blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9434731683691545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8599294301164494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8371730730567223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8108775724026149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7644168171988963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6024238413978339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5723181773493412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.5719454115445657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4518585607422051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.3195122524380067}]
result = search.search('fig cherry apple blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #91 checking search results for 'fig cherry apple blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #91 checking search results for 'fig cherry apple blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking search results for 'banana blueberry peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11320752984200066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06617270707751717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06309685343427059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04021585479175914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03798447959373376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('banana blueberry peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #92 checking search results for 'banana blueberry peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #92 checking search results for 'banana blueberry peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking search results for 'banana blueberry peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9481904594567137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8477613772137168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8210440769559838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('banana blueberry peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #93 checking search results for 'banana blueberry peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #93 checking search results for 'banana blueberry peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking search results for 'apricot papaya tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('apricot papaya tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #94 checking search results for 'apricot papaya tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #94 checking search results for 'apricot papaya tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking search results for 'apricot papaya tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('apricot papaya tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #95 checking search results for 'apricot papaya tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #95 checking search results for 'apricot papaya tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking search results for 'apple coconut lime coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29912071311965366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10328873688567686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841340408078325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04371133850315848}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.041668251699880844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03667881311539609}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03468548398295313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03452144138404044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02841495146360588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('apple coconut lime coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #96 checking search results for 'apple coconut lime coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #96 checking search results for 'apple coconut lime coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking search results for 'apple coconut lime coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9277134197417479}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9006697372508451}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8651137872279429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.773199557296108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7497354573538328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7461896353326737}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7072116585965327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6141963203316881}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5333543320414198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('apple coconut lime coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #97 checking search results for 'apple coconut lime coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #97 checking search results for 'apple coconut lime coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking search results for 'kiwi tomato cherry lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3057336113016535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09356002796179039}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07911422423869517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05845926879214732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04715869037607523}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04489499030467398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.043854382692869655}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.034648769220080824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.034648769220080824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03065593376937129}]
result = search.search('kiwi tomato cherry lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #98 checking search results for 'kiwi tomato cherry lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #98 checking search results for 'kiwi tomato cherry lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking search results for 'kiwi tomato cherry lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9482231140482502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9479235083289532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9463988520887046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7864443680332055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7489418585230588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7489418585230588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.662635716326872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.662635716326872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5754180189120104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.46855420847113666}]
result = search.search('kiwi tomato cherry lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #99 checking search results for 'kiwi tomato cherry lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #99 checking search results for 'kiwi tomato cherry lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking search results for 'fig kiwi kiwi fig blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30758189743088676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10764163957228813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09754825571452415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05321439418642181}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.044683238539311734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04287596677985571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03495536689872525}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.018557895496184206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('fig kiwi kiwi fig blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #100 checking search results for 'fig kiwi kiwi fig blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #100 checking search results for 'fig kiwi kiwi fig blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking search results for 'fig kiwi kiwi fig blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9658394358512002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9539555149499769}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.926774802363475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9015723231941346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8199685056686938}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.426516254179341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.426516254179341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.391205586092807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('fig kiwi kiwi fig blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #101 checking search results for 'fig kiwi kiwi fig blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #101 checking search results for 'fig kiwi kiwi fig blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking search results for 'pear tomato blueberry apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11434339965985214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11393409412947837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.04994386950547139}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0447212047461541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04347110321931072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.032807031059864405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear tomato blueberry apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #102 checking search results for 'pear tomato blueberry apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #102 checking search results for 'pear tomato blueberry apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking search results for 'pear tomato blueberry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.966660084958041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9577041457457331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9577041457457331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9163829172606391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear tomato blueberry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #103 checking search results for 'pear tomato blueberry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #103 checking search results for 'pear tomato blueberry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #104 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #104 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #105 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #105 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking search results for 'orange tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('orange tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #106 checking search results for 'orange tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #106 checking search results for 'orange tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking search results for 'orange tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('orange tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #107 checking search results for 'orange tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #107 checking search results for 'orange tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking search results for 'blueberry fig peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.290937082938317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11554046283390036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09600315661933752}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.049371966949110294}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04237878489869555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.040271216332424066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.039864016393331515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.027699166810445448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01478179670654882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01478179670654882}]
result = search.search('blueberry fig peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #108 checking search results for 'blueberry fig peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #108 checking search results for 'blueberry fig peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking search results for 'blueberry fig peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.967730368229199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9160280909944525}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9023321498783243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8704724665229965}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.806980753228528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6024238413978339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.5839061217146526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.31951225243800674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.31951225243800674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.31951225243800674}]
result = search.search('blueberry fig peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #109 checking search results for 'blueberry fig peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #109 checking search results for 'blueberry fig peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking search results for 'apple orange apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2809397297864582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11784313153865693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07140996007155372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.05858687985890729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.046705237746674746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0462388905413633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03896188411072539}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03863307865731355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.022701802690878493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('apple orange apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #110 checking search results for 'apple orange apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #110 checking search results for 'apple orange apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking search results for 'apple orange apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.999465245017212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9905626273200985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9845593704333911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8713256756554348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8713256756554348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8421709213421417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8350637087942264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.4907051731371904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.4907051731371904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('apple orange apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #111 checking search results for 'apple orange apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #111 checking search results for 'apple orange apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking search results for 'orange kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.22799097236207078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10360479815141346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0882223329527108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04508149302055014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.044057724095804975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.044026277828701735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}]
result = search.search('orange kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #112 checking search results for 'orange kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #112 checking search results for 'orange kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking search results for 'orange kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9523187838800629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9516390649100088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.950330381086011}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8677610164113153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}]
result = search.search('orange kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #113 checking search results for 'orange kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #113 checking search results for 'orange kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking search results for 'blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #114 checking search results for 'blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #114 checking search results for 'blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking search results for 'blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #115 checking search results for 'blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #115 checking search results for 'blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking search results for 'banana tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('banana tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #116 checking search results for 'banana tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #116 checking search results for 'banana tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking search results for 'banana tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('banana tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #117 checking search results for 'banana tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #117 checking search results for 'banana tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking search results for 'tomato kiwi apple banana cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2757443025730689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10208384478451668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05845926879214732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.05594220444749448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05430666324539657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04243007540704139}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04087089852330702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03882840708165416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03847610819192249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.030655933769371292}]
result = search.search('tomato kiwi apple banana cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #118 checking search results for 'tomato kiwi apple banana cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #118 checking search results for 'tomato kiwi apple banana cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking search results for 'tomato kiwi apple banana cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8944377621366933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8834347478585992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.858093638351054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8552122226722418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8392857817982872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8316707527173023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6626357163268721}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6626357163268721}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.46855420847113666}]
result = search.search('tomato kiwi apple banana cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #119 checking search results for 'tomato kiwi apple banana cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #119 checking search results for 'tomato kiwi apple banana cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking search results for 'fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #120 checking search results for 'fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #120 checking search results for 'fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking search results for 'fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #121 checking search results for 'fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #121 checking search results for 'fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking search results for 'fig apricot tomato apricot kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3084041414467189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10901827878433282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.049943869505471396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0447212047461541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04470253788755516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.032807031059864405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.018989447476008524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('fig apricot tomato apricot kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #122 checking search results for 'fig apricot tomato apricot kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #122 checking search results for 'fig apricot tomato apricot kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking search results for 'fig apricot tomato apricot kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.966660084958041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9662565961159678}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9565056787277847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9163829172606391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('fig apricot tomato apricot kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #123 checking search results for 'fig apricot tomato apricot kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #123 checking search results for 'fig apricot tomato apricot kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking search results for 'lime tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('lime tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #124 checking search results for 'lime tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #124 checking search results for 'lime tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking search results for 'lime tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('lime tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #125 checking search results for 'lime tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #125 checking search results for 'lime tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking search results for 'kiwi tomato apple banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3074633155170225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0882223329527108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08442376869993334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.08195553289283851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.038888417384739506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}]
result = search.search('kiwi tomato apple banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #126 checking search results for 'kiwi tomato apple banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #126 checking search results for 'kiwi tomato apple banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking search results for 'kiwi tomato apple banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9535877368991585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8197786283658526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7071067811865476}]
result = search.search('kiwi tomato apple banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #127 checking search results for 'kiwi tomato apple banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #127 checking search results for 'kiwi tomato apple banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking search results for 'tomato lime apricot fig banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3084041414467189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11674212668155656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04591793916184169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0447212047461541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.032807031059864405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.018989447476008524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('tomato lime apricot fig banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #128 checking search results for 'tomato lime apricot fig banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #128 checking search results for 'tomato lime apricot fig banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking search results for 'tomato lime apricot fig banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9925278002512044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9813078302886417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.966660084958041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9565056787277847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('tomato lime apricot fig banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #129 checking search results for 'tomato lime apricot fig banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #129 checking search results for 'tomato lime apricot fig banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking search results for 'fig apple blueberry fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.23199019023788336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10376875788150369}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10151917319083928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.045967820475054315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04326955993316789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.02839775579797435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.02638054482906496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.010797274970916586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01053004416278773}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01053004416278773}]
result = search.search('fig apple blueberry fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #130 checking search results for 'fig apple blueberry fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #130 checking search results for 'fig apple blueberry fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking search results for 'fig apple blueberry fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9936059973780849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9352824173344777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8691342912458041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8533471370479838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7195102287885807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.3218885156119846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.22760955217530618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.22760955217530618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.22760955217530618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.22760955217530618}]
result = search.search('fig apple blueberry fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #131 checking search results for 'fig apple blueberry fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #131 checking search results for 'fig apple blueberry fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #132 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #132 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #133 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #133 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking search results for 'fig peach cherry coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2932219460916306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10510029036651272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08448003255745641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04325813238389946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03888314372206024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.035772995159932694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03403966107537803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02589102079603921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.024675220792534574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('fig peach cherry coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #134 checking search results for 'fig peach cherry coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #134 checking search results for 'fig peach cherry coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking search results for 'fig peach cherry coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9350354079837818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9094185805955264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8802867861417208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7732422848800365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7175655000391533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7101199867448399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5596409243537205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5333611015861809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4744419607752676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('fig peach cherry coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #135 checking search results for 'fig peach cherry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #135 checking search results for 'fig peach cherry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking search results for 'peach papaya cherry apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08429015308294771}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06893171849252874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06039426854014499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.045882203326144615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03777409591892746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03602839030474835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03402129366291503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.026710319377464698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('peach papaya cherry apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #136 checking search results for 'peach papaya cherry apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #136 checking search results for 'peach papaya cherry apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking search results for 'peach papaya cherry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.967209576491279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.816496580927726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7787627151498988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7369150856369139}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7353788165870935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7085239029622071}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5773502691896257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5773502691896257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('peach papaya cherry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #137 checking search results for 'peach papaya cherry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #137 checking search results for 'peach papaya cherry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking search results for 'banana orange peach kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2697124020714999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09787781727003618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07240236553680192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05845926879214732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.05574195280437582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.044019698628805136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04398066443130656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04354142866067562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.021677018651928115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.021677018651928115}]
result = search.search('banana orange peach kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #138 checking search results for 'banana orange peach kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #138 checking search results for 'banana orange peach kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking search results for 'banana orange peach kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9514968538500184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.950653119856616}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9178653970769548}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8834347478585993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8365044742736409}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8197936361426021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.46855420847113666}]
result = search.search('banana orange peach kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #139 checking search results for 'banana orange peach kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #139 checking search results for 'banana orange peach kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking search results for 'peach kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3052997436712434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06617270707751717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0437312312088018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('peach kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #140 checking search results for 'peach kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #140 checking search results for 'peach kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking search results for 'peach kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.946877487331447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9218664874536562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('peach kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #141 checking search results for 'peach kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #141 checking search results for 'peach kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking search results for 'papaya peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08442376869993334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07396757065598898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04515414587212144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('papaya peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #142 checking search results for 'papaya peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #142 checking search results for 'papaya peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking search results for 'papaya peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9518619233552359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.902532971784904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('papaya peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #143 checking search results for 'papaya peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #143 checking search results for 'papaya peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking search results for 'tomato apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('tomato apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #144 checking search results for 'tomato apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #144 checking search results for 'tomato apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking search results for 'tomato apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('tomato apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #145 checking search results for 'tomato apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #145 checking search results for 'tomato apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking search results for 'blueberry pear blueberry peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.25813333570310537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11436340835323308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10255531653179518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06591767763306342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.059369236873497114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.039993280857654905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03927255235069877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03079878962284275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.013244539291401269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.013244539291401269}]
result = search.search('blueberry pear blueberry peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #146 checking search results for 'blueberry pear blueberry peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #146 checking search results for 'blueberry pear blueberry peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking search results for 'blueberry pear blueberry peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9578717322322193}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8620567228905903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8488860934612975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8430694569279207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8005923665964205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7244079170484531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6657235815182799}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5283337596546266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.28628404689292464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.28628404689292464}]
result = search.search('blueberry pear blueberry peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #147 checking search results for 'blueberry pear blueberry peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #147 checking search results for 'blueberry pear blueberry peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #148 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #148 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #149 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #149 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking search results for 'lime coconut coconut papaya orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2930827534265618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10074575084267881}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07003740452578357}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05435653515604688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.045657859194289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04177675824851676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.037611183732016766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.032103775400597494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.022083113507999803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('lime coconut coconut papaya orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #150 checking search results for 'lime coconut coconut papaya orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #150 checking search results for 'lime coconut coconut papaya orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking search results for 'lime coconut coconut papaya orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9624803399457287}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9089868789525101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9030151335816967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8468459242643555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8129751930462124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.693931177220449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6632442403506927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5866111456467835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.47733205089062203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('lime coconut coconut papaya orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #151 checking search results for 'lime coconut coconut papaya orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #151 checking search results for 'lime coconut coconut papaya orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #152 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #152 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #152 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #153 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #153 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #153 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking search results for 'peach tomato banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('peach tomato banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #154 checking search results for 'peach tomato banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #154 checking search results for 'peach tomato banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking search results for 'peach tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('peach tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #155 checking search results for 'peach tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #155 checking search results for 'peach tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking search results for 'peach orange coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2492634780257736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09787781727003617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.07082376627359956}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06137992912101013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04534159968444185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04398066443130656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0387533960492232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03065593376937129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03065593376937129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('peach orange coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #156 checking search results for 'peach orange coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #156 checking search results for 'peach orange coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking search results for 'peach orange coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9558135017294763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9506531198566159}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8376643994720712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.819793636142602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7730827838843453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7489418585230587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.662635716326872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.662635716326872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5953285107131405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('peach orange coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #157 checking search results for 'peach orange coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #157 checking search results for 'peach orange coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking search results for 'apricot cherry papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10323393269715217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04657076288956151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04412558625023501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('apricot cherry papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #158 checking search results for 'apricot cherry papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #158 checking search results for 'apricot cherry papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking search results for 'apricot cherry papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9817246031343433}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9537856414108278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8677610164113153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('apricot cherry papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #159 checking search results for 'apricot cherry papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #159 checking search results for 'apricot cherry papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking search results for 'kiwi orange cherry apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.24969392759280867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10162961756971671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06216646071482549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05293644979318099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.049176153101512736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04231482908895899}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04006073048113672}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03993676282926689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0397113302235467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.032206883039731404}]
result = search.search('kiwi orange cherry apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #160 checking search results for 'kiwi orange cherry apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #160 checking search results for 'kiwi orange cherry apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking search results for 'kiwi orange cherry apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8920083377755241}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8659227619244104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8632431699597318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8583703875059779}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8542755074390717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7744178095858276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6961598747649528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6000345719893414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5206866100713995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.42428851480003094}]
result = search.search('kiwi orange cherry apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #161 checking search results for 'kiwi orange cherry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #161 checking search results for 'kiwi orange cherry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking search results for 'apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #162 checking search results for 'apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #162 checking search results for 'apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking search results for 'apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #163 checking search results for 'apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #163 checking search results for 'apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking search results for 'tomato apricot apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('tomato apricot apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #164 checking search results for 'tomato apricot apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #164 checking search results for 'tomato apricot apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking search results for 'tomato apricot apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('tomato apricot apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #165 checking search results for 'tomato apricot apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #165 checking search results for 'tomato apricot apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking search results for 'pear kiwi coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2897566377186737}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10838102249596974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.04636687542255846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04427014264155625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04151825939286692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.030457382201234822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.024314704775054888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01719309262899024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01719309262899024}]
result = search.search('pear kiwi coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #166 checking search results for 'pear kiwi coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #166 checking search results for 'pear kiwi coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #167 checking search results for 'pear kiwi coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9332268899813118}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9110262854821455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8986710364097462}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8974276158217795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5255684572228687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.3716330200800424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.3716330200800424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.3716330200800424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3716330200800424}]
result = search.search('pear kiwi coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #167 checking search results for 'pear kiwi coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #167 checking search results for 'pear kiwi coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #168 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #168 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #169 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #169 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking search results for 'cherry papaya orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2948637039317377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10309083647737671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05299708084078069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.04830200317876409}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04653871973388704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04448994844629568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0439633104224351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.034861673647887205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.018716520633617163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('cherry papaya orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #170 checking search results for 'cherry papaya orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #170 checking search results for 'cherry papaya orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking search results for 'cherry papaya orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9810491245221012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9616614218912227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9502780085914954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9145104405484823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8665581820537283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7535438412612129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6466565339777288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.4045622994395562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.4045622994395562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('cherry papaya orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #171 checking search results for 'cherry papaya orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #171 checking search results for 'cherry papaya orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking search results for 'pear blueberry tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11434339965985216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11393409412947839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.049943869505471396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0447212047461541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04347110321931072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.032807031059864405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear blueberry tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #172 checking search results for 'pear blueberry tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #172 checking search results for 'pear blueberry tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking search results for 'pear blueberry tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.966660084958041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9577041457457333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9577041457457333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9163829172606391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear blueberry tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #173 checking search results for 'pear blueberry tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #173 checking search results for 'pear blueberry tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking search results for 'apple orange apple cherry cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2539069809153766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11565167178162265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.045204180818052817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.043965390096291745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04177638375433026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.040496585753831624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03968564015992446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.032977754753483066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.022154391042836223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('apple orange apple cherry cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #174 checking search results for 'apple orange apple cherry cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #174 checking search results for 'apple orange apple cherry cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking search results for 'apple orange apple cherry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.972141713803539}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9529166738980565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9503229612648045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8753438832319462}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8578150903214631}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.787484461054629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.509744519737981}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.4788727327276089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.276211242089613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('apple orange apple cherry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #175 checking search results for 'apple orange apple cherry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #175 checking search results for 'apple orange apple cherry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking search results for 'peach apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('peach apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #176 checking search results for 'peach apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #176 checking search results for 'peach apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking search results for 'peach apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('peach apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #177 checking search results for 'peach apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #177 checking search results for 'peach apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking search results for 'orange kiwi apricot tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.22799097236207078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10360479815141346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0882223329527108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04508149302055014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.044057724095804975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.044026277828701735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}]
result = search.search('orange kiwi apricot tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #178 checking search results for 'orange kiwi apricot tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #178 checking search results for 'orange kiwi apricot tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking search results for 'orange kiwi apricot tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9523187838800629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9516390649100088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.950330381086011}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8677610164113153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}]
result = search.search('orange kiwi apricot tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #179 checking search results for 'orange kiwi apricot tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #179 checking search results for 'orange kiwi apricot tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking search results for 'coconut apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.31959743430844756}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10265342611740245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08442376869993334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.044238146876788224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04412558625023501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04274693519677292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #180 checking search results for 'coconut apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #180 checking search results for 'coconut apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking search results for 'coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9912213220900394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9562186676551894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9537856414108277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9011172544194608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8628814098079822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #181 checking search results for 'coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #181 checking search results for 'coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking search results for 'coconut tomato tomato kiwi blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2999372132854783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11310109710537065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.10187037535756875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08381617144537605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06691641239511242}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.038351384542362636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03777409591892747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.036808884914396336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.026710319377464705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.026710319377464705}]
result = search.search('coconut tomato tomato kiwi blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #182 checking search results for 'coconut tomato tomato kiwi blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #182 checking search results for 'coconut tomato tomato kiwi blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking search results for 'coconut tomato tomato kiwi blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9472990125221565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9302457691506432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8289748196724714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8164965809277261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8164965809277261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.8164965809277261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.775941506908471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7045397208543136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5773502691896258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5773502691896258}]
result = search.search('coconut tomato tomato kiwi blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #183 checking search results for 'coconut tomato tomato kiwi blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #183 checking search results for 'coconut tomato tomato kiwi blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking search results for 'apple papaya fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26808046481989806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11484400132389776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09215920395027943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04910121087540568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.037669988833599816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03571072686011265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.029412029356386274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.029412029356386274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.026447398367723824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('apple papaya fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #184 checking search results for 'apple papaya fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #184 checking search results for 'apple papaya fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking search results for 'apple papaya fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9653526191811651}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.831443072564954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.814246280102451}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7718963399231442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7718963399231442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6357484096820486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6357484096820486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5991201465263888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.5575184956291365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('apple papaya fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #185 checking search results for 'apple papaya fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #185 checking search results for 'apple papaya fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #186 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #186 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #187 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #187 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking search results for 'apple orange cherry orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.19022474778392903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10008961738502278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08285024952025788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04625648939551286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.041311123955744336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03988121508518862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.038573315261253564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.036630064310166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03129847802664664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('apple orange cherry orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #188 checking search results for 'apple orange cherry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #188 checking search results for 'apple orange cherry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking search results for 'apple orange cherry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9998456486745808}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8929503312677681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8413306152836605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8407070793508065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8337719079619221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7917680500574761}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6939274822828196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.5899760315680562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.38189585159029077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('apple orange cherry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #189 checking search results for 'apple orange cherry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #189 checking search results for 'apple orange cherry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #190 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #190 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking search results for 'coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #191 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #191 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking search results for 'blueberry peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11320752984200068}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06617270707751717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06309685343427059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04021585479175915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03798447959373376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('blueberry peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #192 checking search results for 'blueberry peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #192 checking search results for 'blueberry peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking search results for 'blueberry peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9481904594567138}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8210440769559838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('blueberry peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #193 checking search results for 'blueberry peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #193 checking search results for 'blueberry peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking search results for 'fig blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11434339965985216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11393409412947839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.049943869505471396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.046003434391643214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0447212047461541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.032807031059864405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('fig blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #194 checking search results for 'fig blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #194 checking search results for 'fig blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking search results for 'fig blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9943758011396544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.966660084958041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9577041457457333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9577041457457333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('fig blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #195 checking search results for 'fig blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #195 checking search results for 'fig blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking search results for 'coconut blueberry papaya banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2823977979367868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1087091363959708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07534196181460877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06823094668999655}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05845926879214732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.041908117652922176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03965991348451094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03895166795455802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02654389357899564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.021677018651928115}]
result = search.search('coconut blueberry papaya banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #196 checking search results for 'coconut blueberry papaya banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #196 checking search results for 'coconut blueberry papaya banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking search results for 'coconut blueberry papaya banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9137843364826712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8834347478585993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8758478278522865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8572590017638745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.841950096557909}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.832536184948152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.631040439527901}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5737529337108416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.46855420847113666}]
result = search.search('coconut blueberry papaya banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #197 checking search results for 'coconut blueberry papaya banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #197 checking search results for 'coconut blueberry papaya banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking search results for 'lime pear papaya fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.31415851488624985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11795386435901571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10798154779163133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.041080432825259146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04093611983820491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03515281454114523}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.030617652851382196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.019738135544111947}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.019738135544111947}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('lime pear papaya fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #198 checking search results for 'lime pear papaya fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #198 checking search results for 'lime pear papaya fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking search results for 'lime pear papaya fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9914934222848366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9743526857316858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9044192869175014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.887963884479054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7410310839506608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6618082646594661}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.49949183896749483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.42664476259722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.42664476259722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('lime pear papaya fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #199 checking search results for 'lime pear papaya fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #199 checking search results for 'lime pear papaya fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
