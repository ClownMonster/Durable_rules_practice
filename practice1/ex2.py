from durable.lang import *

with ruleset('clown'):
    @when_all(m.name == 'Mohan')
    def executefuntion(c):
        print(f'Hello {c.m.name}')

post('clown', {'name': 'Mohan'})
