import logging
test =logging
test.basicConfig(filename='nooroooo.log',level=test.DEBUG)
test.debug('This message should go to the log file')
test.info('I told you so') # will not print anything
test1 = logging
test1.basicConfig(filename='mukti000.log',level=test1.WARNING)

#test.debug('This message should go to the log file')
test1.warning('Watch out!') # will print a message to the console
test1.info('I told you so') # will not print anything

