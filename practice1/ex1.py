from durable.lang import *

with ruleset('test'):
    @when_all(m.subject == 'world')
    def say_hello(c):
        print(f'Hello {c.m.subject}')

post('test', {'subject':'world'})

