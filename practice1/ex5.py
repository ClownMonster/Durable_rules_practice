from durable.lang import *

def testfun(val):
    print(val)

with ruleset('test'):
    m.subject.strip()
    @when_all(m.subject.matches('3[47][0-9]{13}'))
    def amex(c):
        testfun("Amex card Detected")

    @when_all(m.subject.matches('4[0-9]{12}([0-9]{3})?'))
    def visa(c):
        print("Here")
        testfun("visa card Detected")

    @when_all(m.subject.matches('(5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|2720)[0-9]{12}'))
    def mastercard(c):
        return('Mastercard detected {0}'.format(c.m.subject))


post('test',{ 'subject':'4212588888883'})
