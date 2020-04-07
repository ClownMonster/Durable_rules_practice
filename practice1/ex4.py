from durable.lang import *

with statechart('expense'):
    with state('input'):
        @to('denied')
        @when_all((m.subject == 'approve') & (m.amount > 1000))
        def denied(c):
            print ('expense denied')
        
        @to('pending')    
        @when_all((m.subject == 'approve') & (m.amount <= 1000))
        def request(c):
            print ('requesting expense approval')
        
    with state('pending'):
        @to('approved')
        @when_all(m.subject == 'approved')
        def approved(c):
            print ('expense approved')
            
        @to('denied')
        @when_all(m.subject == 'denied')
        def denied(c):
            print ('expense denied')
        
    state('denied')
    state('approved')
