
import testingtools
import crawler
import searchdata
import search

output = open('fruits-incoming-links-failed.txt', 'w')
success_output = open('fruits-incoming-links-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html')



#Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-404.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-46.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-519.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-404.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-404.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-404.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-519.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-143.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-404.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-519.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-519.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-519.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-264.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-400.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-205.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-17.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-330.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-915.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-192.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-33.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-101.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-834.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-250.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-396.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-406.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-532.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-673.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-300.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-98.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-372.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-22.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-681.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-269.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-203.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-721.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-23.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-762.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-69.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-232.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-718.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-624.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-991.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-291.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-641.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-204.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-148.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-152.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-979.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-72.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-181.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-462.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-514.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-757.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-73.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-901.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-903.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-624.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-901.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-901.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-901.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-669.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-724.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-728.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-45.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-262.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-297.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-262.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-262.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-262.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-250.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-228.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-211.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-250.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-250.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-250.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-88.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-959.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-552.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-340.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-224.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-88.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-88.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-88.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-583.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-335.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-583.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-583.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-583.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-350.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-350.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-350.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-350.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-577.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-21.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-577.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-577.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-577.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-531.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-40.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-531.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-531.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-531.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-395.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-26.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-395.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-395.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-395.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-681.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-681.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-681.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-681.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-336.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-70.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-847.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-336.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-336.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-336.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-40.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-794.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-545.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-135.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-794.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-794.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-794.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-940.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-219.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-940.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-940.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-940.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-770.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-155.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-770.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-770.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-770.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-764.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-295.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-764.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-764.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-764.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-864.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-526.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-864.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-864.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-864.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-118.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-263.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-819.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-218.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-930.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-828.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-118.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-118.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-118.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-67.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-600.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-772.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-353.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-743.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-210.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-948.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-772.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-772.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-772.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-142.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-314.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-14.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-284.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-47.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-65.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-467.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-565.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-591.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-838.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-354.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-439.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-14.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-357.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-245.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-202.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-385.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-394.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-357.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-357.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-357.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-486.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-181.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-486.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-486.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-486.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-632.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-632.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-632.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-632.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-152.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-152.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-152.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-152.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-865.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-438.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-19.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-465.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-234.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-380.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-45.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-234.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-234.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-234.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-656.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-481.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-656.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-656.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-656.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-627.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-241.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-627.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-627.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-627.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-513.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-513.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-513.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-513.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-438.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-154.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-438.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-438.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-438.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-835.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-937.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-40.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-512.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-835.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-835.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-835.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-294.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-117.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-57.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-117.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-117.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-117.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-510.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-510.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-510.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-510.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-332.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-300.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-332.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-332.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-332.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-833.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-122.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-862.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-833.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-833.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-833.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-386.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-379.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-46.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-34.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-386.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-386.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-386.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-533.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-376.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-533.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-533.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-533.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-46.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-399.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-185.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-342.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-81.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-223.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-446.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-52.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-616.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-223.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-223.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-223.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-961.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-36.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-961.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-961.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-961.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-938.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-276.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-375.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-910.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-975.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-938.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-938.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-938.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = None
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #50 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
